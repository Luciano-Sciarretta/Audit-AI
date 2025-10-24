# import requests
# from django.conf import settings


# OPENROUTER_API_KEY=settings.OPENAI_API_KEY
# API_ENDPOINT = 'https://api.openai.com/v1/chat/completions'



# def get_ai_response(user_input):
#     headers = {
#         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#         "Content-Type": "application/json",
#         "HTTP-Referer": "http://localhost:3000",
#         "X-Title": "AuditAI",
#     }
    
#     payload = {
#         "model": "gpt-4o",  # Modelo gratuito de DeepSeek
#         "messages": [
#             {"role": "system", "content": "Eres un experto en normas ISO 9001. Responde con precisión y detalle."},
            
#             {"role": "user", "content": user_input},
#         ],
#         "max_tokens": 500,
#         "stream": False# Limita la longitud de la respuesta
#     }
    
    
#     # Hacer la solicitud HTTP a OpenRouter
#     try:
#         response = requests.post(API_ENDPOINT, json=payload, headers=headers)
#         response.raise_for_status()  # Si hay un error HTTP, lanza una excepción
#         # Extraer la respuesta de la IA del JSON devuelto
#         ai_text = response.json()["choices"][0]["message"]["content"]
#         return ai_text
#     except requests.exceptions.RequestException as e:
#         # Si falla, devolver un mensaje de error
#         return f"Error al consultar la IA: {str(e)}"

import sys
import os
from django.conf import settings
import requests
import traceback

def get_ai_response(user_input):
    # Configurar API Key
    os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY
    
    print(f"🔍 Procesando: {user_input}")
    
    # PRIMERO: Intentar importación directa del agente principal
    try:
        print("🔄 Intentando importación directa...")
        
        # Rutas absolutas
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../AuditAI-Fer'))
        agents_path = os.path.join(base_path, 'agents')
        etapa1_path = os.path.join(agents_path, 'etapa1')
        
        print(f"📁 Base path: {base_path}")
        print(f"📁 Agents path: {agents_path}")
        print(f"📁 Etapa1 path: {etapa1_path}")
        
        # Agregar todas las rutas necesarias
        sys.path.insert(0, base_path)
        sys.path.insert(0, agents_path) 
        sys.path.insert(0, etapa1_path)
        
        # Intentar importación directa
        from etapa1_agent_profundo import Etapa1AgenteProfundo
        print("✅ Etapa1AgenteProfundo importado")
        
        agent = Etapa1AgenteProfundo()
        print("✅ Agente instanciado")
        
        respuesta = agent.execute(user_input, client_id="web_app")
        print(f"✅ Respuesta: {respuesta[:200]}...")
        return respuesta
        
    except Exception as e:
        print(f"❌ Error con agente principal: {e}")
        traceback.print_exc()
        # Limpiar paths para siguiente intento
        for path in [base_path, agents_path, etapa1_path]:
            if path in sys.path:
                sys.path.remove(path)

    # SEGUNDO: FileManagerAgent como fallback
    try:
        print("🔄 Intentando FileManagerAgent...")
        from agents.file_agent import FileManagerAgent
        agent = FileManagerAgent()
        respuesta = agent.execute(user_input)
        return respuesta
    except Exception as e:
        print(f"❌ Error con FileManagerAgent: {e}")

    # TERCERO: OpenAI como último recurso
    print("🔄 Usando OpenAI fallback...")
    return get_openai_response(user_input)

def get_openai_response(user_input):
    """Tu función original"""
    headers = {
        "Authorization": f"Bearer {settings.OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    
    payload = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": "Eres un experto en normas ISO 9001. Responde con precisión y detalle."},
            {"role": "user", "content": user_input},
        ],
        "max_tokens": 500,
        "stream": False
    }
    
    try:
        response = requests.post('https://api.openai.com/v1/chat/completions', 
                               json=payload, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"