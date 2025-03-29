from fastapi import APIRouter, HTTPException
from models.dbconnection import get_one_alert, create_alert
from models.schemas import Alerta
#manejador de errores de formato de ID
from bson.errors import InvalidId

alert = APIRouter()

@alert.post("/api/alerts", response_model=Alerta)
async def save_alerts(alert : Alerta):
    response = await create_alert(alert.dict(exclude_unset=True))
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@alert.get('/api/alerts/{id}', response_model=Alerta)
async def get_alert(id : str):
    try:
        alert = await get_one_alert(id)
        if alert:
            return alert
        raise HTTPException(status_code=404, detail=f"alert with id {id} not found")
    except InvalidId:
        raise HTTPException(status_code=404, detail=f"Invalid alert ID format: {id}")
