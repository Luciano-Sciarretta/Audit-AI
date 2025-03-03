from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..models import ClientInput

@login_required(login_url='login')
def chat_view(request):
    return render(request, 'chat/chat.html' )

@login_required(login_url='login')
def client_input(request):
    if request.method == 'POST':
        client_input = request.POST.get('client_input')
        if client_input:
            ClientInput.objects.create(client_input= client_input, user=request.user)
        
            
    return render(request, 'chat/chat.html' )
        