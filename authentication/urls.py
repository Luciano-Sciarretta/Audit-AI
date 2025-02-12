from django.urls import path
from .views import register_views, login_views

urlpatterns = [
    path('register/', register_views.register_company, name = 'register'),
    path('login/', login_views.login_company, name='login'),
    path("logout/", login_views.logout_company, name="logout"),
]