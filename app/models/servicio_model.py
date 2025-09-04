from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from bson import ObjectId


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
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


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
    fecha_creacion: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {ObjectId: str, datetime: str}
        schema_extra = {
            "example": {
                "nombre": "Desarrollo Web",
                "descripcion": "Servicio de creación de páginas y aplicaciones web.",
                "precio": 1200.50,
                "cantidad": 10,
                "imagen_url": "https://example.com/servicio.png",
                "en_promocion": True,
                "disponible": True,
                "fecha_creacion": "2025-09-03T12:00:00"
            }
        }
