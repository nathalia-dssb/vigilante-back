# En app/models/chatbot_models.py
from pydantic import BaseModel

class Alert(BaseModel):
    type: str
    location: str
    severity: str

class ChatbotRequest(BaseModel):
    query: str
    active_alerts: list[Alert]  # 