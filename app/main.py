from typing import Union

from fastapi import FastAPI
from app.api.alerts import alert  # alert es ya un APIRouter
from app.api.citizens import citizens  # citizens es ya un APIRouter  
from app.api.civil_corps import civil_corps  # civil_corps es ya un APIRouter
from app.routers.chatbot_router import router as chatbot_router
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()  # Esto carga las variables de .env
from fastapi import FastAPI
from app.routers.chatbot_router import router as chatbot_router  # Importar el router

from PIL import Image
import requests

origins = [
    os.getenv('FRONTEND_URL', 'http://localhost:3000')
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Bienvenido al sistema de monitoreo y chatbot!"}

# Incluir los routers
app.include_router(alert, prefix="/api", tags=["alerts"])  # Eliminar .router
app.include_router(citizens, prefix="/api", tags=["citizens"])  # Eliminar .router
app.include_router(civil_corps, prefix="/api", tags=["civil-corps"])  # Eliminar .router
app.include_router(chatbot_router)

# Ejecutar el servidor
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

