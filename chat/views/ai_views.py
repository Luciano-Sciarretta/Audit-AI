import sys
import os
from django.conf import settings

# ✅ SOLO PARA PRUEBAS LOCALES - LUEGO REVOCAR
TEMPORAL_API_KEY = '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'  # Usa tu key
os.environ["OPENAI_API_KEY"] = TEMPORAL_API_KEY
print("🔑 API Key temporal configurada")

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