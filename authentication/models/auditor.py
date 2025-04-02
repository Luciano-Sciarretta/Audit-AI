from django.db import models

class AuditorApplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    
    name = models.CharField(max_length=100, null=False)
    surname = models.CharField(max_length=100, null=False )
    document = models.PositiveIntegerField( null=False)
    location = models.CharField(max_length=200, null=False)
    #Competencias (En que norma sos auditor, interno o líder) Tipo de certificado
    #Tipo de Norma
    email = models.EmailField( unique=True, null=False)
    phone = models.CharField(max_length= 30, null=False)
    documents = models.FileField(upload_to='auditor_docs/', blank=True, null=True, verbose_name="Douments PDF")
    
    submission_date = models.DateField(auto_now=True)
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f'{self.name} - {self.status}'
    
        
            