import sys
import os
from django.conf import settings
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la API key desde las variables de entorno
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_API_KEY:
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    print("🔑 API Key cargada desde .env")
else:
    print("⚠️ ADVERTENCIA: No se encontró OPENAI_API_KEY en las variables de entorno")
    raise ValueError("OPENAI_API_KEY no está configurada en el archivo .env")

base_path = os.path.join(os.path.dirname(__file__), '../../AuditAI-Fer')
sys.path.insert(0, base_path)

print(f"📍 Paths configurados. Base: {base_path}")

# CARGAR SUPERVISOR
supervisor_agent = None

try:
    from supervisor import SupervisorAgent
    supervisor_agent = SupervisorAgent()
    print("✅ SupervisorAgent cargado")
except Exception as e:
    print(f"❌ Error cargando supervisor: {e}")
    import traceback
    traceback.print_exc()

def get_ai_response(user_input):
    if supervisor_agent:
        try:
            return supervisor_agent.execute(user_input)
        except Exception as e:
            return f"⚠️ Error del sistema: {str(e)}"
    return "🔧 Sistema no disponible"