from django.urls import path, re_path
from .views import  register_views, login_views

urlpatterns = [
    path('register-client/', register_views.register_client, name = 'register-client'),
    path('login/', login_views.login_company, name='login'),
    path("logout/", login_views.logout_company, name="logout"),
    path('register-auditor/<uuid:uuid>', register_views.register_auditor, name='register-auditor')
    
    
    
]