from django.db import models
from authentication.models import CustomUser
from django.core.validators import FileExtensionValidator


class AuditorProfile(models.Model): 
    ISO_AUDITABLE_CHOICES = [
    ('9001', 'ISO 9001 (Quality Management)'),
    ('14001', 'ISO 14001 (Environmental Management)'),
    ('45001', 'ISO 45001 (Occupational Health & Safety)'),
    ('27001', 'ISO 27001 (Information Security)'),
    ('50001', 'ISO 50001 (Energy Management)'),
    ('22301', 'ISO 22301 (Business Continuity)'),
    ('37001', 'ISO 37001 (Anti-Bribery Management)'),
]  
    AUDITOR_ROLE_CHOICES = [
    ('internal', 'Internal Auditor'),
    ('lead', 'Lead Auditor'),
    ('external', 'External Auditor'),
]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    username = models.CharField(max_length= 50)
    name = models.CharField(max_length= 50,blank=True, null=True )
    surname = models.CharField(max_length= 50, blank=True, null=True)
    document = models.CharField(max_length=60, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)
    profile_image = models.ImageField(  upload_to='auditors/profile_images', default= 'auditors/profile_images/default.png',  null=True, blank=True)
    competency = models.CharField(max_length= 50, choices= AUDITOR_ROLE_CHOICES, blank=True, null=True)
    iso_standard = models.CharField(max_length=50, choices=ISO_AUDITABLE_CHOICES, blank=True, null=True)
    
    
    def __str__(self):
        return f'{self.username} {self.surname} {self.iso_standard}'
   
    
   
   
    
class Credential(models.Model):
    auditor_profile = models.ForeignKey(AuditorProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    description = models.TextField(blank=True, null=True)
    certificate_file = models.FileField(upload_to='auditors/credentials/%Y/%m/%d/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title} of {self.auditor_profile}' 