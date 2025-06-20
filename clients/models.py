from django.db import models
from authentication.models import CustomUser

class ClientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length= 200, blank= True,  null=True)
    company_name = models.CharField(max_length=200, blank= True,  null=True)
    phone_number = models.CharField(max_length=200, blank=True)
    document = models.CharField(max_length=60, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)
    cuit = models.CharField(max_length=60, unique=True, blank=True, null=True)
    company_logo = models.ImageField(  upload_to='clients/profile_images', default= 'auditors/profile_images/default.png',  null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name if self.name else  self.user.username
    
