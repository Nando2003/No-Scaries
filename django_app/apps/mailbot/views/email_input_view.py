from PyPDF2 import PdfReader
from django.urls import reverse
from django.views.generic import FormView
from apps.mailbot.models.email import Email
from apps.mailbot.forms.email_input_form import EmailInputForm
from apps.mailbot.services import HuggingFaceService, CleaningService

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class EmailInputView(FormView):
    template_name = 'mailbot/input.html'
    form_class = EmailInputForm
    
    def get_success_url(self):
        return reverse('mailbot:detail', args=[self.email.id]) # type: ignore
    
    def form_valid(self, form: EmailInputForm):
        uploaded_file = form.cleaned_data['uploaded_file']
        manual_text = form.cleaned_data['manual_text']

        if uploaded_file:
            
            if uploaded_file.name.endswith('.pdf'):
                try:
                    pdf = PdfReader(uploaded_file)
                    text: list[str] = []
                    
                    for page in pdf.pages:
                        text.append(page.extract_text())
                        
                    content = "\n".join(text)
                    
                except Exception as e:
                    raise FileExistsError("Erro ao ler o arquivo PDF: " + str(e))
            
            elif uploaded_file.name.endswith('.txt'):
                content = uploaded_file.read().decode('utf-8', errors='ignore')

            else:
                form.add_error('uploaded_file', "Formato de arquivo não suportado. Use .pdf ou .txt.")
                return self.form_invalid(form)
            
        elif manual_text:
            content = manual_text
        
        else:
            form.add_error(None, "Você deve enviar um arquivo OU digitar o texto do e-mail.")
            return self.form_invalid(form)
        
        clean_content = (CleaningService(content)
                            .to_lower()
                            .remove_html()
                            .remove_emails()
                            .remove_phones()
                            .remove_cpf()
                            .remove_cnpj()
                            .remove_credit_card()
                            .remove_punctuation()
                            .normalize_spaces()
                            .remove_stopwords()
                            .stemming()
                            .get())
        
        hugging_face_service = HuggingFaceService(clean_content)
        hugging_face_raw_response = hugging_face_service.get_response()
        hugging_face_response = hugging_face_service.parse_response(hugging_face_raw_response)

        CLASSIFICATION_MAP = {
            "Produtivo": "productive",
            "Improdutivo": "non_productive",
        }
        
        classification = CLASSIFICATION_MAP.get(hugging_face_response["classification"])
        
        if not classification:
            form.add_error(None, "Classificação inválida retornada pela API.")
            return self.form_invalid(form)
        
        self.email = Email.objects.create(
            content=content,
            content_type=classification,
            suggestion=hugging_face_response["suggestion_response"],
            user=self.request.user,
        )
        
        return super().form_valid(form)
    