from fastapi import APIRouter, HTTPException
from app.models.schemas import AlertaSchema
from app.models.crud import create_alert, get_alert
from bson.errors import InvalidId
from bson import ObjectId

router = APIRouter()

# Añadir esta línea para permitir la importación como 'alert'
alert = router

@router.post("/alerts", response_model=AlertaSchema)
def save_alert(alert: AlertaSchema):
    alert_data = alert.dict(exclude_unset=True)
    if "_id" in alert_data:
        del alert_data["_id"]
    
    created_alert = create_alert(alert_data)
    if created_alert:
        return created_alert
    raise HTTPException(status_code=400, detail="Failed to create alert")

@router.get('/alerts/{alert_id}', response_model=AlertaSchema)
def get_alert_by_id(alert_id: str):
    try:
        alert = get_alert(alert_id)
        if alert:
            return alert
        raise HTTPException(status_code=404, detail=f"Alert with id {alert_id} not found")
    except InvalidId:
        raise HTTPException(status_code=400, detail=f"Invalid alert ID format: {alert_id}")

@router.get('/alerts', response_model=list[AlertaSchema])
def get_all_alerts():
    return list(get_alert(alert_id) for alert_id in get_alerts_ids())