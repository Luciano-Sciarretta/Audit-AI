from django.db import models
from django.core.validators import FileExtensionValidator

class AuditorApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
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
    
    name = models.CharField(max_length=100, null=False)
    surname = models.CharField(max_length=100, null=False )
    document = models.PositiveIntegerField( null=False)
    photo = models.ImageField(upload_to='auditors/photos/', default='auditors/photos/default.png', null=False , blank= True, validators=[
            FileExtensionValidator(['jpg', 'jpeg', 'png', 'webp']),
             
        ],
        verbose_name="Profile Photo")
    location = models.CharField(max_length=200, null=False)
    competency =models.CharField(max_length = 50, choices= AUDITOR_ROLE_CHOICES)
    iso_standard = models.CharField(max_length = 20, choices = ISO_AUDITABLE_CHOICES)
    email1 = models.EmailField() 
    email2 =  models.EmailField()
    phone = models.CharField(max_length= 30, null=False)
    documents = models.FileField(upload_to='auditor_docs/', blank=True, null=True, verbose_name="Douments PDF")# Subir muchos documentos
    submission_date = models.DateField(auto_now=True)
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f'{self.name} - {self.status}'
    
        
            