from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from bson import ObjectId

class PyObjectId(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return str(v)

class CoordenadaSchema(BaseModel):
    latitud: float
    longitud: float

class AlertaSchema(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    suceso: str
    ubicacion: CoordenadaSchema
    fecha: datetime
    clasificacion: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class DomicilioSchema(BaseModel):
    codigo_postal: int 
    calle: str 
    estado: str 
    municipio: str 
    colonia: str

class CiudadanoSchema(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    nombre: str 
    apellidos: str 
    curp: str 
    fecha_nacimiento: datetime
    domicilio: DomicilioSchema 
    sexo: str 
    correo: str
    telefono: str 
    contrasena: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class CuerpoCivilSchema(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    matricula: str 
    tipo_vehiculo: str 
    encargado: str 
    zona: str
    user: str 
    contrasena: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
