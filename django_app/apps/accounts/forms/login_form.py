from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control bg-secondary text-light border-0 py-2 mb-2'
            
            if visible.name == 'username':
                visible.field.widget.attrs['placeholder'] = 'Usuário'
            elif visible.name == 'password':
                visible.field.widget.attrs['placeholder'] = 'Senha'
