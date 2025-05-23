from django.db import models


class Email(models.Model):
    
    CONTENT_TYPE_CHOICES = [
        ('productive', 'Produtivo'),
        ('non_productive', 'Improdutivo'),
    ]
    
    content = models.TextField()
    
    content_type = models.CharField(
        max_length=50, choices=CONTENT_TYPE_CHOICES)
    
    suggestion = models.TextField()
    
    user = models.ForeignKey(
        'accounts.CustomUser', on_delete=models.CASCADE, related_name='emails')
    
    created_at = models.DateTimeField(auto_now_add=True)
    