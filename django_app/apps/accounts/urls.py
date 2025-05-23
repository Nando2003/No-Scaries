from django.urls import path
from apps.accounts.forms.login_form import LoginForm
from apps.accounts.views.register_view import RegisterView
from django.contrib.auth.views import LoginView, LogoutView

app_name = "accounts"

urlpatterns = [
    
    path('login/', LoginView.as_view(
        template_name='registration/login.html', 
        redirect_authenticated_user=True, 
        authentication_form=LoginForm
    ), name='login'),
    
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
