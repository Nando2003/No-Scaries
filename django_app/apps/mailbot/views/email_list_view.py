from django.views.generic import ListView
from apps.mailbot.models import Email

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required(login_url='/accounts/login/'), name='dispatch')
class EmailListView(ListView):
    model = Email
    template_name = 'mailbot/list.html'
    context_object_name = 'emails'
    paginate_by = 10
    ordering = ['-created_at']

    def get_queryset(self):
        return Email.objects.filter(user=self.request.user).order_by('-created_at')
