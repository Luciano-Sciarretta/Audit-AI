from django.apps import AppConfig


class AuditorsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auditors'
    
    
    def ready(self):
        import auditors.signals