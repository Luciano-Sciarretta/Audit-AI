from django.contrib import admin
from .models.auditor import AuditorApplication, AuditorProfile
from django.core.exceptions import ValidationError

# Register your models here.

class AuditorApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'document', 'photo', 'location', 'competency', 'iso_standard', 'phone', 'documents' , 'email1', 'submission_date', 'is_processed','status']
    list_filter = ['status', 'is_processed']
    search_fields = ['name', 'surname', 'email1']
    actions = ['approve_applications', 'reject_applications']
    
    
    def approve_applications(self, request, applications):
        for application in applications:
            try:
                application.approve(request)
            except ValidationError as e:
                self.message_user(request, f"Error al aprobar {application}: {str(e)}", level='error')

    approve_applications.short_description = "Aprobar solicitudes seleccionadas"

    def reject_applications(self, request, applications):
        for application in applications:
            try:
                application.reject(request)
            except ValidationError as e:
                self.message_user(request, f"Error al rechazar {application}: {str(e)}", level='error')

    reject_applications.short_description = "Rechazar solicitudes seleccionadas"




class AuditorProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email1', 'user', 'approved_at']
    search_fields = ['name', 'surname', 'email1', 'user__username']
    readonly_fields = ['approved_at']

admin.site.register(AuditorApplication, AuditorApplicationAdmin)
admin.site.register(AuditorProfile, AuditorProfileAdmin)



