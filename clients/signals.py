from django.db.models.signals import post_delete
from django.db.models.signals import post_save
from authentication.models import CustomUser
from .models import ClientProfile

def client_profile(sender, instance,  created, **kwargs):
    if created:
        if instance.is_auditor == False:
            try:
                ClientProfile.objects.create(user = instance)
                
            except Exception as e:
                print(f"Error en señal de  client Profile: {str(e)}")
        
        
            
def client_delete_profile(sender, instance,**kwargs):
    
    try:
        user = instance.user
        user.delete()
        print(f'User de {user.username} borrado correctamente')
    except CustomUser.DoesNotExist:
            pass


def client_update_profile(sender, instance, created, **kwargs):
    user = instance.user
    if user.is_auditor == False and not created:
        user.save()
        
    else:
        print(f'No se puedo actualizar el perfil de {instance.name}')
        
        
        


post_save.connect(client_profile, sender = CustomUser)
post_delete.connect(client_delete_profile, sender = ClientProfile)
post_save.connect(client_update_profile, sender = ClientProfile)