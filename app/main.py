from dotenv import load_dotenv
load_dotenv()  # Esto carga las variables de .env
from fastapi import FastAPI
from app.routers.chatbot_router import router as chatbot_router  # Importar el router
from routes.alerts import alert



app.include_router(alerts.router, prefix="/api", tags=["alerts"])
app.include_router(citizens.router, prefix="/api", tags=["citizens"])
app.include_router(civil_corps.router, prefix="/api", tags=["civil-corps"])

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
