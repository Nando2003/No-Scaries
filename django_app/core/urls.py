from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.urls import path, re_path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls', namespace='home')),
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
    path("mail/", include("apps.mailbot.urls", namespace="mailbot")),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

handler404 = "apps.home.views.custom_404_view"