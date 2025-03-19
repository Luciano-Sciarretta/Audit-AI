from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ClientInput(models.Model):
    client_input = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username }: {self.client_input}"
    
    class Meta:
        verbose_name = 'Client Input'
        verbose_name_plural = "Clients Inputs"
        
class AIResponse(models.Model):
    client_input = models.ForeignKey(ClientInput, on_delete=models.CASCADE)
    response_text= models.TextField(default="With out response")
    created_at = models.DateTimeField(default=timezone.now)
    is_final = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Respuesta a {self.client_input.user.username}: {self.response_text[:30]}"
    class Meta:
        verbose_name = 'AI Response'
        verbose_name_plural = "AI Responses"