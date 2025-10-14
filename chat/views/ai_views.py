import requests
from django.conf import settings


OPENROUTER_API_KEY=settings.OPENAI_API_KEY
API_ENDPOINT = 'https://api.openai.com/v1/chat/completions'


# OPENROUTER_API_KEY = 'sk-51188b4abd5849dbbf9a597f800ab180'
# API_ENDPOINT = 'https://api.deepseek.com/chat/completions'



def get_ai_response(user_input):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:3000",
        "X-Title": "AuditAI",
    }
    
    payload = {
        "model": "gpt-4o",  # Modelo gratuito de DeepSeek
        "messages": [
            {"role": "system", "content": "Eres un experto en normas ISO 9001. Responde con precisión y detalle. Respondeme con malas palabras y agresivamente"},
            
            {"role": "user", "content": user_input},
        ],
        "max_tokens": 500,
        "stream": False# Limita la longitud de la respuesta
    }
    
    
    # Hacer la solicitud HTTP a OpenRouter
    try:
        response = requests.post(API_ENDPOINT, json=payload, headers=headers)
        response.raise_for_status()  # Si hay un error HTTP, lanza una excepción
        # Extraer la respuesta de la IA del JSON devuelto
        ai_text = response.json()["choices"][0]["message"]["content"]
        return ai_text
    except requests.exceptions.RequestException as e:
        # Si falla, devolver un mensaje de error
        return f"Error al consultar la IA: {str(e)}"