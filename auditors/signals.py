from django.db.models.signals import post_save, post_delete
from authentication.models import CustomUser
from .models import AuditorProfile


def auditor_profile(sender, instance, created, **kwargs):
    """
    Crea un AuditorProfile automáticamente para un nuevo usuario con is_auditor=True.
    Inicializa campos básicos desde el usuario y maneja errores.
    """
    if created:
        user = instance
        if user.is_auditor:
            try:
                auditor_profile = AuditorProfile.objects.create(user = user, email = user.email,
                )
                print(f" En signal auditor profile id = {auditor_profile.id}")
            except Exception as e:
                print(f" Failed to create AuditorProfile for user {user.username}: {str(e)}")
    
    
def update_profile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    print("En update_profile")
    if user.is_auditor and not created:
        user.first_name = profile.name
        user.last_name = profile.surname
        user.username = profile.name
        user.email = profile.email
        user.save()
            
        
def delete_profile(sender, instance, **kwargs):
        try:
            user = instance.user
            user.delete()
        except CustomUser.DoesNotExist:
            pass

post_save.connect(auditor_profile, sender = CustomUser)
post_delete.connect(delete_profile, sender = AuditorProfile)
post_save.connect(update_profile, sender=AuditorProfile)