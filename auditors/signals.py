from django.db.models.signals import post_save, post_delete
from authentication.models import CustomUser
from .models import AuditorProfile


def auditor_profile(sender, instance, created, **kwargs):
    """
    Crea un AuditorProfile automáticamente para un nuevo usuario con is_auditor=True.
    Inicializa campos básicos desde el usuario y maneja errores.
    """
    if created:
        print("Al principio de signal")
        user = instance
        if user.is_auditor:
            try:
                auditor_profile = AuditorProfile.objects.create(user = user, email = user.email,
                )
                print(f" En signal auditor profile id = {auditor_profile.id}")
            except Exception as e:
                print(f" EN signal Failed to create AuditorProfile for user {user.username}: {str(e)}")
    
    
def delete_profile(sender, instance, **kwargs):
        try:
            user = instance.user
            user.delete()
        except CustomUser.DoesNotExist:
            pass

post_save.connect(auditor_profile, sender = CustomUser)
post_delete.connect(delete_profile, sender = AuditorProfile)