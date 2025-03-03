from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ClientInput(models.Model):
    client_input = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username }"
    
    class Meta:
        verbose_name = 'Client Input'
        verbose_name_plural = "Clients Inputs"