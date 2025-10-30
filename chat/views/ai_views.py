import sys
import os
from django.conf import settings
import requests
import traceback
from AuditAI.settings import BASE_DIR
import sys

# Configurar API Key
os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY

 # Rutas absolutas
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../AuditAI-Fer'))
print("base path", base_path)
agents_path = os.path.join(base_path, 'agents')
etapa1_path = os.path.join(agents_path, 'etapa1')

sys.path.insert(0, base_path)
sys.path.insert(0, agents_path) 
sys.path.insert(0, etapa1_path)

print(f"📍 Paths configurados. Base: {base_path}")


#  IMPORTACIONES E INICIALIZACIÓN UNA SOLA VEZ
agente_principal = None
file_agent = None


try:
    from etapa1_agent_profundo import Etapa1AgenteProfundo
    agente_principal = Etapa1AgenteProfundo()
    print("✅ Agente principal cargado y listo")
except Exception as e:
    print(f"❌ Agente principal no disponible:  {e}")
    
    
try:
    from agents.file_agent import FileManagerAgent  
    file_agent = FileManagerAgent()  # ← UNA SOLA INSTANCIA
    print("✅ FileManagerAgent cargado y listo")
except Exception as e:
    print(f"❌ FileManagerAgent no disponible: {e}")


def get_ai_response(user_input):
    print(f"🔍 Procesando: {user_input}")
    
    if agente_principal:
        try:
            print("🔄 Usando agente principal")
       
            respuesta = agente_principal.execute(user_input, client_id="web_app")
            print(f"✅ Respuesta: {respuesta[:200]}...")
            return respuesta
            
        except Exception as e:
            print(f"❌ Error con agente principal: {e}")
            traceback.print_exc()
         

    # SEGUNDO: FileManagerAgent como fallback
    if file_agent: 
        try:
            print("🔄 Intentando FileManagerAgent...")
            
            respuesta = file_agent.execute(user_input)
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