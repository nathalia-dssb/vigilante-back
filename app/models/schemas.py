from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from bson import ObjectId
from typing import Any, Optional
from pydantic_core import core_schema
from pydantic import GetCoreSchemaHandler, GetJsonSchemaHandler

class PyObjectId(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: Any):
        if isinstance(v, ObjectId):
            return str(v)
        if ObjectId.is_valid(v):
            return str(v)
        raise ValueError("Invalid ObjectId")
    
    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source_type: Any, _handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        return core_schema.union_schema([
            # Permite cadenas de texto
            core_schema.chain_schema([
                core_schema.str_schema(),
                core_schema.no_info_plain_validator_function(cls.validate),
            ]),
            # Permite ObjectId directo
            core_schema.chain_schema([
                core_schema.is_instance_schema(ObjectId),
                core_schema.no_info_plain_validator_function(lambda x: str(x)),
            ]),
        ])

    @classmethod
    def __get_pydantic_json_schema__(cls, _schema_generator: GetJsonSchemaHandler, _field_schema):
        return {"type": "string", "format": "objectid"}

class CoordenadaSchema(BaseModel):
    latitud: float
    longitud: float

class AlertaSchema(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    suceso: str
    ubicacion: CoordenadaSchema
    fecha: datetime
    clasificacion: str

    model_config = ConfigDict(
        validate_by_name=True,  # Reemplaza a allow_population_by_field_name
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )

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

    model_config = ConfigDict(
        validate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )

class CuerpoCivilSchema(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    matricula: str 
    tipo_vehiculo: str 
    encargado: str 
    zona: str
    user: str 
    contrasena: str

    model_config = ConfigDict(
        validate_by_name=True,
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )