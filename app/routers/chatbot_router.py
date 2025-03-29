from fastapi import APIRouter, FastAPI
from google import genai
import os

app = FastAPI()
router = APIRouter(prefix="/api/chatbot", tags=["Chatbot"])


# Configuración directa (sin modelos Pydantic ni manejo complejo de errores)
GEMINI_API_KEY = "AIzaSyDiL7x2jREusEKSJu-vRxFmwSmrnIK41VE" # ← Usa tu clave temporalmente
client = genai.Client(api_key=GEMINI_API_KEY)

@router.get("/ask/")
async def ask_simple(question: str):    
    """Endpoint mínimo para probar la conexión con Gemini"""
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[{"text": question}]  # ¡Estructura requerida en v1.0+!
        )
        return {"response": response.text}
    
    except Exception as e:
        return {
            "error": str(e),
            "details": "Revisa la consola para más información"
        }

app.include_router(router)