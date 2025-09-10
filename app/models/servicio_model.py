from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId


# -------------------
# Helper para ObjectId de Mongo (Pydantic v2)
# -------------------
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        schema = handler(core_schema)
        schema.update(type="string")
        return schema


# -------------------
# Modelo Servicio
# -------------------
class Servicio(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    nombre: str = Field(..., min_length=3, max_length=100)
    descripcion: str = Field(..., min_length=10, max_length=300)
    precio: float = Field(..., gt=0, description="Precio del servicio")
    disponible: bool = True

    def to_mongo(self):
        """Convierte a dict para Mongo, excluyendo el _id si está vacío"""
        return self.dict(by_alias=True, exclude_unset=True, exclude={"id"})

    class Config:
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "nombre": "Desarrollo Web",
                "descripcion": "Creación de aplicaciones web personalizadas",
                "precio": 1500.0,
                "disponible": True
            }
        }
