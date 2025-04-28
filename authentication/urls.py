from django.urls import path, re_path
from .views import register_views, login_views, auditor_views

urlpatterns = [
    path('register/', register_views.register_company, name = 'register'),
    path('login/', login_views.login_company, name='login'),
    path("logout/", login_views.logout_company, name="logout"),
    path("auditor-application/", auditor_views.auditor_application, name='auditor-application'),
    path('application-submitted/', auditor_views.application_submitted, name='application-submitted'),
    path('register/<uuid:uuid>', register_views.register_auditor, name='register-auditor')
    
    
    
]