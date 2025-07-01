from django.urls import path
from .views import MessageCreateView


urlpatterns = [
    path('send-message/<str:pk>', MessageCreateView.as_view(), name='send-message'),
    
]

