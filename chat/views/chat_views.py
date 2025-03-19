from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests
from ..models import ClientInput, AIResponse
from .ai_views import get_ai_response


@login_required(login_url='login')
def chat_view(request):
    
    # Mostrar el historial de entradas del usuario
    inputs = ClientInput.objects.filter(user=request.user).order_by('-created_at')
    print("client inputs:", inputs)
    return render(request, 'chat/chat.html', {'inputs': inputs})




@login_required(login_url='login')
def client_input(request):
    if request.method == 'POST':
        client_input_text = request.POST.get('client_input')  # Obtener la entrada del usuario
        if client_input_text:
            # 1. Guardar la entrada del usuario en la base de datos
            client_input = ClientInput.objects.create(
                client_input=client_input_text,
                user=request.user
            )
            # 2. Obtener la respuesta de la IA usando nuestra función
            ai_response_text = get_ai_response(client_input_text)
            
            print(f"Pregunta del usuario: {client_input_text}")
            print(f"Respuesta de la IA: {ai_response_text}")
            
            # 3. Guardar la respuesta en la base de datos
            AIResponse.objects.create(
                client_input=client_input,
                response_text=ai_response_text
            )
            # 4. Devolver la respuesta al frontend como JSON
            # return JsonResponse({
            #     'status': 'success',
            #     'client_input': client_input_text,
            #     'ai_response': ai_response_text,
            # })
            return redirect('chat')
    return render(request, 'chat/chat.html')
        