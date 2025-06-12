from django.db import models
from authentication.models import CustomUser

class ClientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length= 200, blank= True,  null=True)
    phone_number = models.CharField(max_length=200, blank=True)
    email = models.EmailField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name if self.name else  self.user.username
    
