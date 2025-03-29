from fastapi import APIRouter, HTTPException
from database import get_all_citizens, create_civilcorps, get_one_civilcorps, update_civilcorps, delete_citizen
from models import Citizen
#manejador de errores de formato de ID
from bson.errors import InvalidId

civilcorps = APIRouter()

@civilcorps.get("/api/citizens")
async def get_citizens():
    citizens = await get_all_citizens()
    return citizens

@civilcorps.post("/api/citizens", response_model=Citizens)
async def save_citizens(civilcorps : Citizen):
    response = await create_civilcorps(civilcorps.dict(exclude_unset=True))
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@civilcorps.get('/api/citizens/{id}', response_model=Citizen)
async def get_civilcorps(id : str):
    try:
        civilcorps = await get_one_civilcorps(id)
        if civilcorps:
            return citizen
        raise HTTPException(status_code=404, detail=f"civilcorps with id {id} not found")
    except InvalidId:
        raise HTTPException(status_code=404, detail=f"Invalid civilcorps ID format: {id}")

@civilcorps.delete('/api/citizens/{id}')
async def remove_citizens(id : str):
    response = await delete_civilcorps(id)
    if response: 
        return "Successfully deleted Citizen"
    raise HTTPException(404, "Citizen not found")
