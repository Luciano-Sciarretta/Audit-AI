from django.urls import path
from .views import auditor_application, application_submitted



urlpatterns = [
path("auditor-application/", auditor_application, name='auditor-application'),
path('application-submitted/', application_submitted, name='application-submitted'),    
]

