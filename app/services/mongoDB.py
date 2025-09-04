from bson import ObjectId
from pymongo import MongoClient
from fastapi import HTTPException
from app.config.nosql import mongodb_cred  # Datos de conexión

# ---------------------------
# Conexión a la base de datos
# ---------------------------

client = MongoClient(mongodb_cred["MONGO_URI"])
db = client[mongodb_cred["DB_NAME"]]

usuarios_collection = db["usuarios"]
servicios_collection = db["servicios"]

# ---------------------------
# Utils
# ---------------------------

def check_database_connection():
    try:
        client.server_info()
        return {"status": "success", "message": "Conectado a la base de datos"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"No se pudo conectar a la base de datos: {str(e)}"
        )

# ---------------------------
# CRUD Usuarios
# ---------------------------

def crear_usuario(usuario: dict):
    result = usuarios_collection.insert_one(usuario)
    return str(result.inserted_id)

def obtener_usuarios():
    usuarios = list(usuarios_collection.find())
    for usuario in usuarios:
        usuario["_id"] = str(usuario["_id"])
    return usuarios

def obtener_usuario_por_id(usuario_id: str):
    usuario = usuarios_collection.find_one({"_id": ObjectId(usuario_id)})
    if usuario:
        usuario["_id"] = str(usuario["_id"])
    return usuario

def actualizar_usuario(usuario_id: str, nuevos_datos: dict):
    result = usuarios_collection.update_one(
        {"_id": ObjectId(usuario_id)},
        {"$set": nuevos_datos}
    )
    return result.modified_count > 0

def eliminar_usuario(usuario_id: str):
    result = usuarios_collection.delete_one({"_id": ObjectId(usuario_id)})
    return result.deleted_count > 0


# ---------------------------
# CRUD Servicios
# ---------------------------

def crear_servicio(servicio: dict):
    result = servicios_collection.insert_one(servicio)
    return str(result.inserted_id)

def obtener_servicios():
    servicios = list(servicios_collection.find())
    for servicio in servicios:
        servicio["_id"] = str(servicio["_id"])
    return servicios

def obtener_servicio_por_id(servicio_id: str):
    servicio = servicios_collection.find_one({"_id": ObjectId(servicio_id)})
    if servicio:
        servicio["_id"] = str(servicio["_id"])
    return servicio

def actualizar_servicio(servicio_id: str, nuevos_datos: dict):
    result = servicios_collection.update_one(
        {"_id": ObjectId(servicio_id)},
        {"$set": nuevos_datos}
    )
    return result.modified_count > 0

def eliminar_servicio(servicio_id: str):
    result = servicios_collection.delete_one({"_id": ObjectId(servicio_id)})
    return result.deleted_count > 0
