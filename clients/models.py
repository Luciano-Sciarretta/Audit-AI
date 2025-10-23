from django.db import models
from authentication.models import CustomUser
from django.core.exceptions import ValidationError


class ClientProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length= 200, blank= True,  null=True)
    surname = models.CharField(max_length= 200, blank= True,  null=True)
    country = models.ForeignKey('auditors.Country', on_delete=models.SET_NULL, null=True, blank=True)
    location = models.CharField(max_length=120, null=True, blank=True)
    company_name = models.CharField(max_length=200, blank= True,  null=True)
    phone_number = models.CharField(max_length=200, blank=True)
    company_email = models.CharField(max_length=200, blank=True, null=True)
    document = models.CharField(max_length=60, unique=True, blank=True, null=True)
    cuit = models.CharField(max_length=60, unique=True, blank=True, null=True)
    company_logo = models.ImageField(  upload_to='clients/profile_images', default= 'auditors/profile_images/default.png',  null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    #company_website
    #puesto en la empresa
    
    def __str__(self):
        return self.name if self.name else  self.user.email
    
class Review(models.Model):
    VOTE_OPTIONS = [
        ("up", "Up Vote"),
        ("down", "Down Vote")
    ]
    
    client_profile = models.ForeignKey(ClientProfile, on_delete=models.CASCADE)
    auditor_profile = models.ForeignKey('auditors.AuditorProfile', on_delete=models.CASCADE)
    value = models.CharField(max_length= 10, choices=VOTE_OPTIONS )
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.value
    
    class Meta:
       unique_together = [['client_profile', 'auditor_profile']] 