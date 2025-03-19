import requests


OPENROUTER_API_KEY = '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'
API_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"

def get_ai_response(user_input):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }
    
    payload = {
        "model": "deepseek/deepseek-r1",  # Modelo gratuito de DeepSeek
        "messages": [
            {"role": "system", "content": "Eres un experto en normas ISO 9001. Responde con precisión y detalle. Respondeme con malas palabras y agresivamente"},
            
            {"role": "user", "content": user_input},
        ],
        "max_tokens": 500,  # Limita la longitud de la respuesta
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