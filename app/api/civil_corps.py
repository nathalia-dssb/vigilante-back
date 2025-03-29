from fastapi import APIRouter, HTTPException
from app.models.schemas import CuerpoCivilSchema
from app.models.crud import create_civil_corps, get_civil_corps
from bson.errors import InvalidId

router = APIRouter()

@router.post("/civil-corps", response_model=CuerpoCivilSchema)
def create_new_civil_corps(civil_corps: CuerpoCivilSchema):
    civil_corps_data = civil_corps.dict(exclude_unset=True)
    if "_id" in civil_corps_data:
        del civil_corps_data["_id"]
    
    created_civil_corps = create_civil_corps(civil_corps_data)
    if created_civil_corps:
        return created_civil_corps
    raise HTTPException(status_code=400, detail="Failed to create civil corps member")

@router.get('/civil-corps/{civil_corps_id}', response_model=CuerpoCivilSchema)
def get_civil_corps_by_id(civil_corps_id: str):
    try:
        civil_corps = get_civil_corps(civil_corps_id)
        if civil_corps:
            return civil_corps
        raise HTTPException(status_code=404, detail=f"Civil corps member with id {civil_corps_id} not found")
    except InvalidId:
        raise HTTPException(status_code=400, detail=f"Invalid civil corps ID format: {civil_corps_id}")
