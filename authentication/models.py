from django.db import models
import uuid
from django.utils import timezone
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.conf import settings
from django.contrib import messages


#Clase para que  AuditorAplication herede y separar un poco el código

class AuditorBase(models.Model):
    class Meta:
        abstract = True
        
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
    name = models.CharField(max_length=100, null=False, )
    surname = models.CharField(max_length=100, null=False, )
    document = models.PositiveIntegerField( null=False, unique=True)
    competency =models.CharField(max_length = 50, choices= AUDITOR_ROLE_CHOICES, default="internal")
    iso_standard = models.CharField(max_length = 20, choices = ISO_AUDITABLE_CHOICES, default="9001")
    email1 = models.EmailField(blank= False, unique = True) 
    email2 =  models.EmailField(null = True)
    credentials = models.FileField(upload_to='auditor_docs/', blank=True, null=True, verbose_name="Douments PDF")# Subir muchos documentos

class AuditorApplication(AuditorBase):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    submission_date = models.DateField(auto_now=True)
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default='pending')
    is_processed = models.BooleanField(default=False)
    registration_token = models.UUIDField(null=True, blank=True, unique=True)   
    token_expiry = models.DateTimeField(null=True, blank=True)
    
    
    def generate_registration_token(self):
        self.registration_token = uuid.uuid4()
        self.token_expiry = timezone.now() + timezone.timedelta(days= 7)
        self.save()
        return self.registration_token
    
    
    def approve(self, request = None):
        if self.status != 'pending':
            raise ValidationError("Solo las solicitudes pendientes pueden ser aprobadas.")
        if self.is_processed:
            raise ValidationError("Esta solicitud ya fué procesada.")
        
        self.status = 'approved'
        token = self.generate_registration_token()
        print("Token:", token)
        
        register_url = request.build_absolute_uri( reverse('register-auditor', kwargs={'uuid': str(token)}))
        
        subject = 'Solicitud de Auditor Aprobada'
        message = (
            f"Hola {self.name},\n\n"
            f"Tu solicitud para ser auditor ha sido aprobada.\n"
            f"Por favor, regístrate en el siguiente enlace para crear tu cuenta:\n"
            f"{register_url}\n\n"
            f"Este enlace expira en 7 días.\n"
            f"Gracias,\nEquipo de Auditoría"
        )
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.email1],
            fail_silently=False,
        )
        self.save()
    
        if request:
            
            messages.success(request, f"Solicitud aprobada. Se envió un correo a {self.email1} con el enlace de registro.")
    
    
    def reject(self, request=None):
        if self.status != 'pending':
            raise ValidationError("Solo las solicitudes pendientes pueden ser rechazadas.")
        if self.is_processed:
            raise ValidationError("Esta solicitud ya fue procesada.")

        self.status = 'rejected'
        self.is_processed = True
        
        subject = 'Solicitud de Auditor Rechazada'
        message = (
            f"Hola {self.name},\n\n"
            f"Lamentamos informarte que tu solicitud para ser auditor ha sido rechazada.\n"
            f"Si tienes alguna pregunta, contáctanos.\n\n"
            f"Gracias,\nEquipo de Auditoría"
        )
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.email1],
            fail_silently=False,
        )
        self.save()
        if request:
            messages.success(request, f'Solcitud de {self.name} rechazada.')
            
            
            
    def __str__(self):
        return f'{self.name} {self.surname} - {self.status}'
    
         
         
         
         
