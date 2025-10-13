from django.db import models
from authentication.models import CustomUser
from django.core.validators import FileExtensionValidator


class AuditorProfile(models.Model): 

    AUDITOR_ROLE_CHOICES = [
    ('internal', 'Internal Auditor'),
    ('lead', 'Lead Auditor'),
    ('external', 'External Auditor'),
]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length= 50 )
    surname = models.CharField(max_length= 50)
    document = models.CharField(max_length=60, unique=True)
    phone = models.CharField(max_length=50)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(  upload_to='auditors/profile_images', default= 'auditors/profile_images/default.png',  null=True, blank=True)
    country = models.ForeignKey("Country", on_delete=models.SET_NULL, null = True )
    location = models.CharField( max_length=80 )
    competency = models.CharField(max_length= 50, choices= AUDITOR_ROLE_CHOICES, blank=True, null=True)
    
    iso_standards = models.ManyToManyField('IsoStandard', blank = True)
    
    def __str__(self):
        return f'{self.name} {self.user.last_name} '
   
    
   
class IsoStandard(models.Model):
    code = models.CharField(max_length = 20, unique=True)
    description = models.CharField(max_length= 100)
    def __str__(self):
        return f'{self.code } - {self.description}'
    
    
class Credential(models.Model):
    auditor_profile = models.ForeignKey(AuditorProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    description = models.TextField(blank=True, null=True)
    certificate_file = models.FileField(upload_to='auditors/credentials/%Y/%m/%d/', validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg'])]) 
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title} of {self.auditor_profile}' 
    
    
class Country(models.Model):
    name = models.CharField(max_length=200,  null=True, blank=True)
    
    language = models.CharField(max_length=100, null=True, blank=True)
    timezone = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.name or "Unnamed Country"
    
    class Meta:
        verbose_name_plural = "Countries"