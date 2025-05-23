from django.urls import path
from apps.mailbot.views.email_input_view import EmailInputView
from apps.mailbot.views.email_detail_view import EmailDetailView
from apps.mailbot.views.email_list_view import EmailListView

app_name = 'mailbot'

urlpatterns = [
    path('input/', EmailInputView.as_view(), name='input'),
    path('<int:pk>/', EmailDetailView.as_view(), name='detail'),
    path('', EmailListView.as_view(), name='list'),
]
