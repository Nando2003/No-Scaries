import os
from django import forms


class EmailInputForm(forms.Form):
    uploaded_file = forms.FileField(
        label='Upload de arquivo (.pdf, .txt)',
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control bg-secondary text-light border-0 py-2 mb-2',
            'accept': '.pdf,.txt',
        })
    )
    
    manual_text = forms.CharField(
        label='Ou escreva/cole o e-mail',
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control bg-secondary text-light border-0 py-2 mb-2',
            'placeholder': 'Digite ou cole o texto do e-mail aqui...',
            'rows': 6,
        })
    )
    
    def clean(self):
        cleaned_data = super().clean()
        file = cleaned_data.get("uploaded_file")
        manual_text = cleaned_data.get("manual_text")

        if not file and not manual_text:
            self.add_error('uploaded_file', "Você deve enviar um arquivo OU digitar o texto do e-mail.")
            self.add_error('manual_text', "Você deve enviar um arquivo OU digitar o texto do e-mail.")

        if file and manual_text:
            self.add_error('uploaded_file', "Por favor, preencha apenas um dos campos: upload OU texto manual.")
            self.add_error('manual_text', "Por favor, preencha apenas um dos campos: upload OU texto manual.")
            
        if file:
            ext = os.path.splitext(file.name)[1].lower()
            
            if ext not in ['.pdf', '.txt']:
                self.add_error('uploaded_file', 'Apenas arquivos PDF ou TXT são permitidos.')
                
            max_size = 2 * 1024 * 1024
            if file.size > max_size:
                self.add_error('uploaded_file', 'Arquivo muito grande. O limite é 2MB.')
                
        return cleaned_data

