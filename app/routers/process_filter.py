from fastapi import APIRouter, FastAPI
from google import genai
from app.controllers.mlController import first, second
import os

app = FastAPI()
router = APIRouter(prefix="/api/process", tags=["Process"])

@router.get("/filter/")
async def get_response():
    """"Get response from model"""
    try:
        return {"message": second()}
    except Exception as e:
        return {
            "error": str(e),
            "details": "Check the console for more information"
        }
