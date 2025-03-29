from fastapi import APIRouter, HTTPException
from database import get_all_citizens, create_citizen, get_one_citizen, update_citizen, delete_citizen
from models import Citizen
#manejador de errores de formato de ID
from bson.errors import InvalidId

citizen = APIRouter()

@citizen.get("/api/citizens")
async def get_citizens():
    citizens = await get_all_citizens()
    return citizens

@citizen.post("/api/citizens", response_model=Citizens)
async def save_citizens(citizen : Citizen):
    response = await create_citizen(citizen.dict(exclude_unset=True))
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@citizen.get('/api/citizens/{id}', response_model=Citizen)
async def get_citizen(id : str):
    try:
        citizen = await get_one_citizen(id)
        if citizen:
            return citizen
        raise HTTPException(status_code=404, detail=f"citizen with id {id} not found")
    except InvalidId:
        raise HTTPException(status_code=404, detail=f"Invalid citizen ID format: {id}")

@citizen.delete('/api/citizens/{id}')
async def remove_citizens(id : str):
    response = await delete_citizen(id)
    if response: 
        return "Successfully deleted Citizen"
    raise HTTPException(404, "Citizen not found")
