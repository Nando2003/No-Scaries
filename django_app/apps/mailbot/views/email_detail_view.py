from django.http import Http404
from django.views.generic.detail import DetailView
from apps.mailbot.models import Email


class EmailDetailView(DetailView):
    model = Email
    template_name = "mailbot/detail.html"
    
    def get_object(self, queryset = None):
        obj = super().get_object(queryset)
        user = self.request.user
        
        if not user.is_authenticated or obj.user != user: # type: ignore
            raise Http404("Email não encontrado")
        
        return obj
    