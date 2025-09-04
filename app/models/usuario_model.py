from pydantic import BaseModel, EmailStr, Field
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
# Modelo Usuario
# -------------------
class Usuario(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id")
    nombre: str = Field(..., min_length=2, max_length=50)
    correo: EmailStr
    contraseña: str = Field(..., min_length=6)
    rol: str = Field(..., description="Puede ser 'admin' o 'cliente'")
    activo: bool = True

    class Config:
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "nombre": "Juan Pérez",
                "correo": "juan@example.com",
                "contraseña": "123456",
                "rol": "admin",
                "activo": True
            }
        }
