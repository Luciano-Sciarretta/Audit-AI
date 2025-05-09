from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import AuditorProfile


def auditor_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        auditor_profile = AuditorProfile.objects.create(user = user)
        print(f" auditor profile id = {auditor_profile.id}")
        
    
    
def delete_profile(sender, instance, **kwargs):
        try:
            user = instance.user
            user.delete()
        except User.DoesNotExist:
            pass

post_save.connect(auditor_profile, sender = User)
post_delete.connect(delete_profile, sender = AuditorProfile)