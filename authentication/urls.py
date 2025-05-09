from django.urls import path, re_path
from .views import auditor_application_views, register_views, login_views

urlpatterns = [
    path('register/', register_views.register_company, name = 'register-company'),
    path('login/', login_views.login_company, name='login'),
    path("logout/", login_views.logout_company, name="logout"),
    path('register/<uuid:uuid>', register_views.register_auditor, name='register-auditor')
    
    
    
]