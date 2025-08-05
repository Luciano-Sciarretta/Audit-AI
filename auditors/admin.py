from django.contrib import admin
from .models import AuditorProfile, Credential, IsoStandard, Country


class CredentialInline(admin.TabularInline):
    model = Credential
    extra = 0 
    fields = ['title', 'description', 'certificate_file', 'created_at']
    readonly_fields = ['created_at']  
    can_delete = True

@admin.register(AuditorProfile)
class AuditorProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_email', 'name', 'surname', 'competency']
    list_filter = ['competency']
    search_fields = ['user__email', 'name', 'surname']
    inlines = [CredentialInline]
    filter_horizontal = ['iso_standards'] 
    fieldsets = (
        ('Auditor Info', {
            'fields': ('user', 'name', 'surname', 'document', 'country', 'location')
        }),
        ('Contact Info', {
            'fields': ('phone', 'bio')
        }),
        ('Profile Details', {
            'fields': ('profile_image', 'competency', 'iso_standards')
        }),
    )
    
    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'
    get_email.admin_order_field = 'user__email'


@admin.register(IsoStandard)
class IsoStandardAdmin(admin.ModelAdmin):
    list_display = ['code', 'description']
    search_fields = ['code', 'description']

@admin.register(Credential)
class CredentialAdmin(admin.ModelAdmin):
    list_display = ['title', 'auditor_profile', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'auditor_profile__email']


admin.site.register(Country)