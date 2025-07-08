from django.urls import path
from .views import MessageCreateView, inbox, single_message


urlpatterns = [
    path('send-message/<str:pk>', MessageCreateView.as_view(), name='send-message'),
    path('inbox/', inbox, name= 'inbox'),
    path('single-message/<str:pk>', single_message, name='single-message')
]

