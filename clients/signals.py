from django.db.models.signals import post_delete
from django.db.models.signals import post_save
from authentication.models import CustomUser
from .models import ClientProfile





def client_profile(sender, instance,  created, **kwargs):
    if created:
        if instance.is_auditor == False:
            try:
                ClientProfile.objects.create(user = instance, email = instance.email)
                
            except Exception as e:
                print(f"Error en señal de  client Profile: {str(e)}")
                
                
post_save.connect(client_profile, sender = CustomUser)