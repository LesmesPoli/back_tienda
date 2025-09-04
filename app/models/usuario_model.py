from pydantic import BaseModel, EmailStr, Field
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
# Modelo Usuario
# -------------------
class Usuario(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    nombre: str = Field(..., min_length=2, max_length=50)
    correo: EmailStr
    contraseña: str = Field(..., min_length=6)
    rol: str = Field(..., description="Puede ser 'admin' o 'cliente'")
    activo: bool = True
    fecha_creacion: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        json_encoders = {ObjectId: str, datetime: str}
        schema_extra = {
            "example": {
                "nombre": "Juan Pérez",
                "correo": "juan@example.com",
                "contraseña": "123456",
                "rol": "admin",
                "activo": True,
                "fecha_creacion": "2025-09-03T12:00:00"
            }
        }
