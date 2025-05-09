from django.contrib import admin
from .models import AuditorProfile, Credential

admin.site.register(AuditorProfile)
admin.site.register(Credential)