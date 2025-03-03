from django.urls import path
from .views import chat_views




urlpatterns = [
    path('', chat_views.chat_view, name='chat' ),
    path('client_input/', chat_views.client_input, name='client_input'),
]
