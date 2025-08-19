from django.urls import path
from .views import client_views, reviews_views



urlpatterns = [
    path('client-profile/<str:pk>/', client_views.client_profile, name='client-profile'),
    path('client-edit-account/<str:pk>/', client_views.client_edit_account, name='client-edit-account'),
    path('client-review/', reviews_views.client_review, name = 'client-review')
  
]
