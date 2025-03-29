from fastapi import APIRouter, HTTPException
from database import get_all_alerts, create_alert, get_one_alert, update_alert, delete_alert
from models import Alert
#manejador de errores de formato de ID
from bson.errors import InvalidId

alert = APIRouter()

@alert.get("/api/alerts")
async def get_alerts():
    alerts = await get_all_alerts()
    return alerts

@alert.post("/api/alerts", response_model=Alerts)
async def save_alerts(alert : Alert):
    response = await create_alert(alert.dict(exclude_unset=True))
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@alert.get('/api/alerts/{id}', response_model=Alert)
async def get_alert(id : str):
    try:
        alert = await get_one_alert(id)
        if alert:
            return alert
        raise HTTPException(status_code=404, detail=f"alert with id {id} not found")
    except InvalidId:
        raise HTTPException(status_code=404, detail=f"Invalid alert ID format: {id}")

@alert.delete('/api/alerts/{id}')
async def remove_alerts(id : str):
    response = await delete_alert(id)
    if response: 
        return "Successfully deleted Alert"
    raise HTTPException(404, "Alert not found")
