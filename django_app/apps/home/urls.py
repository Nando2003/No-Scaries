from django.urls import path
from apps.home.views import HomeView, AboutView
from django.views.generic.base import RedirectView

app_name = "home"

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('', RedirectView.as_view(pattern_name='home:home', permanent=False)),
]
