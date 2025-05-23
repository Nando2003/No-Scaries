from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.accounts.models.custom_user import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            "placeholder": "E-mail",
            "autocomplete": "off"
        })
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={"placeholder": "Usuário", "autocomplete": "off"}),
            'password1': forms.PasswordInput(attrs={"placeholder": "Senha", "autocomplete": "new-password"}),
            'password2': forms.PasswordInput(attrs={"placeholder": "Confirme a senha", "autocomplete": "new-password"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            old_class = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = old_class + ' form-control bg-secondary text-light border-0 py-2 mb-2'

            if not field.widget.attrs.get('placeholder'):
                
                if field_name == 'username':
                    field.widget.attrs['placeholder'] = 'Usuário'
                    
                elif field_name == 'password1':
                    field.widget.attrs['placeholder'] = 'Senha'
                    
                elif field_name == 'password2':
                    field.widget.attrs['placeholder'] = 'Confirme a senha'
                    
