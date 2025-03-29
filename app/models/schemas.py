from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Optional
import datetime

# Clase PyObjectId compatible con Pydantic v2
class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_json_schema__(cls, schema: dict):
        schema.update({
            'type': 'string',
            'format': 'objectid',
        })
        return schema

    @classmethod
    def __get_pydantic_core_schema__(cls, source, handler):
        return handler(str)  # Usa str para validar ObjectId

#Modelo cuerpo_civil
class CiudadanoSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(PyObjectId()), alias="_id")
    matricula: str 
    tipo_vehiculo: str 
    encargado: str 
    zona: str
    user: str 
    contrasena: str  

    class Config:
        from_attributes = True 
    
    @classmethod
    def from_document(cls, document):
        document['_id'] = str(document['_id'])
        return cls(**document)

#Modelo ciudadano
class DomicilioSchema(BaseModel):
    codigo_postal: int 
    calle: str 
    estado: str 
    municipio: str 
    colonia: str

class CiudadanoSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(PyObjectId()), alias="_id")
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
        from_attributes = True 
    
    @classmethod
    def from_document(cls, document):
        document['_id'] = str(document['_id'])
        return cls(**document)

#Modelo alerta
class CoordenadaSchema(BaseModel):
    latitud: int
    longitud: int

class Alerta(BaseModel):
    id: str = Field(default_factory=lambda: str(PyObjectId()), alias="_id")
    suceso: str
    ubicacion: CoordenadaSchema
    fecha: datetime
    clasificacion: str

    class Config:
        from_attributes = True  # Especifica que se pueden usar atributos de clases en lugar de solo campos de dictado

    # Método para construir el modelo a partir de un documento de MongoDB
    @classmethod
    def from_document(cls, document):
        # Convierte el ObjectId a string antes de crear el modelo
        document['_id'] = str(document['_id'])
        return cls(**document)

# Modelo Task que usa PyObjectId
class Task(BaseModel):
    id: str = Field(default_factory=lambda: str(PyObjectId()), alias="_id")
    title: str
    description: str
    completed: bool = False

    class Config:
        from_attributes = True  # Especifica que se pueden usar atributos de clases en lugar de solo campos de dictado

    # Método para construir el modelo a partir de un documento de MongoDB
    @classmethod
    def from_document(cls, document):
        # Convierte el ObjectId a string antes de crear el modelo
        document['_id'] = str(document['_id'])
        return cls(**document)

class UpdateTask(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

    class Config:
        from_attributes = True  # Reemplaza orm_mode
        populate_by_name = True  # Reemplaza allow_population_by_field_name
        json_encoders = {
            ObjectId: str
        }