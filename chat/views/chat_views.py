from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from ..models import ClientInput, AIResponse
from .ai_views import get_ai_response


@login_required(login_url='login')
def chat_view(request):
    
    # Mostrar el historial de entradas del usuario
    inputs = ClientInput.objects.filter(user=request.user).order_by('created_at')
    
    return render(request, 'chat/chat.html', {'inputs': inputs, 'hide_footer': True})


@login_required(login_url='login')
def client_input(request):
    if request.method == 'POST':
        client_input_text = request.POST.get('client_input')  # Obtengo la entrada del usuario
        
        if client_input_text:
            
            # 1. Guardo la entrada del usuario en la base de datos
            client_input = ClientInput.objects.create(
                client_input=client_input_text,
                user=request.user
            )
            # 2. Obtengo la respuesta de la IA usando get_ai_response
            ai_response_text = get_ai_response(client_input_text)
            # 3. Guardo la respuesta en la base de datos
            ai_response = AIResponse.objects.create(
                client_input=client_input,
                response_text=ai_response_text,
            )
            
            
            #4. Devuelvo la respuesta al frontend como JSON
        
        #     return JsonResponse({
        #         'status': 'success',
        #         'client_input': client_input.client_input,
        #         'ai_response': "Mensaje hardcodeado",
        #         'created': "cualquier fecha",
        #         'client_name': client_input.user.clientprofile.name if hasattr(client_input.user, 'clientprofile') else "User"
        # })
            
        
        
            return JsonResponse({
                'status': 'success',
                'client_input': client_input.client_input,
                'ai_response': ai_response.response_text,
                'created': client_input.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'client_name': client_input.user.clientprofile.name if hasattr(client_input.user, 'clientprofile') else "User"
            })
        else:
            
            print("Sigue mandando el input vacío")
            return JsonResponse({
                'status': 'error',
                'message': "The message can't be empty"
            })
        
            
   
        