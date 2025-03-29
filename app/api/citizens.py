from fastapi import APIRouter, HTTPException
from app.models.schemas import CiudadanoSchema
from app.models.crud import create_citizen, get_citizen
from bson.errors import InvalidId

router = APIRouter()

# Añadir esta línea para permitir la importación como 'citizens'
citizens = router

@router.post("/citizens", response_model=CiudadanoSchema)
def create_new_citizen(citizen: CiudadanoSchema):
    citizen_data = citizen.dict(exclude_unset=True)
    if "_id" in citizen_data:
        del citizen_data["_id"]
    
    created_citizen = create_citizen(citizen_data)
    if created_citizen:
        return created_citizen
    raise HTTPException(status_code=400, detail="Failed to create citizen")

@router.get('/citizens/{citizen_id}', response_model=CiudadanoSchema)
def get_citizen_by_id(citizen_id: str):
    try:
        citizen = get_citizen(citizen_id)
        if citizen:
            return citizen
        raise HTTPException(status_code=404, detail=f"Citizen with id {citizen_id} not found")
    except InvalidId:
        raise HTTPException(status_code=400, detail=f"Invalid citizen ID format: {citizen_id}")