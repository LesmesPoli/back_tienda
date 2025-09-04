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
    nombre: str = Field(..., min_length=2, max_length=100)
    descripcion: str
    precio: float = Field(..., gt=0)
    cantidad: int = Field(..., ge=0)
    imagen_url: Optional[str] = None
    en_promocion: bool = False
    disponible: bool = True

    class Config:
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "nombre": "Desarrollo Web",
                "descripcion": "Servicio de creación de páginas y aplicaciones web.",
                "precio": 1200.50,
                "cantidad": 10,
                "imagen_url": "https://example.com/servicio.png",
                "en_promocion": True,
                "disponible": True
            }
        }
