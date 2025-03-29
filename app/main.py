from dotenv import load_dotenv
load_dotenv()  # Esto carga las variables de .env
from fastapi import FastAPI
from app.routers.chatbot_router import router as chatbot_router  # Importar el router


# Inicializar la aplicación FastAPI
app = FastAPI(
    title="Sistema de Monitoreo y Chatbot",
    description="API para gestionar alertas y proporcionar un chatbot interactivo.",
    version="1.0.0"
)

# Incluir los routers
app.include_router(chatbot_router)

# Ruta de prueba para verificar que la API está funcionando
@app.get("/")
def read_root():
    return {"message": "Bienvenido al sistema de monitoreo y chatbot!"}

# Ejecutar el servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)