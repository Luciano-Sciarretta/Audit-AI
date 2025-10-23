from django.db import models
from authentication.models import CustomUser
from django.core.validators import FileExtensionValidator
from clients.models import ClientProfile


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
   
class Audit(models.Model):
    STATUS_CHOICES = [
        ('ia_processing', 'AI Processing'),
        ('ia_completed', 'AI Analysis Completed'), 
        ('assigned', 'Assigned to Auditor'),
        ('in_progress', 'Audit in Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    CLIENT_STATUS = [ 
        ('active', 'active'),
        ('inactive', 'inactive'),
        ]
    
    
    client =models.ForeignKey(ClientProfile, on_delete=models.SET_NULL, null=True)
    auditor = models.ForeignKey(AuditorProfile, on_delete=models.SET_NULL, null=True, blank=True)
    client_status = models.CharField(choices = CLIENT_STATUS, default='active', max_length=200)
    ia_analysis_result = models.TextField(blank=True, null=True)
    ia_recommendations = models.TextField(blank=True, null=True)
    ia_processed_at = models.DateTimeField(blank=True, null=True)
    #Parte del auditor
    auditor_findings = models.TextField(blank=True, null=True)
    auditor_recommendations = models.TextField(blank=True, null=True)
    final_score = models.IntegerField(blank=True, null=True)
    #Campos de control
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default = 'ia_processing' )
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"Audit #{self.id} - {self.client} - {self.status}"
   
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