from django.urls import path
from .views import client_profile, client_edit_account

urlpatterns = [
    path('client-profile/<str:pk>/', client_profile, name='client-profile'),
    path('client-edit-account/<str:pk>', client_edit_account, name='client-edit-account'),
]
