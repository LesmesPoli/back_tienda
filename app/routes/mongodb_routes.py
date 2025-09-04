from fastapi import APIRouter, HTTPException
from app.models.usuario_model import Usuario
from app.models.servicio_model import Servicio
from app.services import mongoDB
from app.config.nosql import mongodb_cred  # Datos de conexión

router = APIRouter(
    prefix="/MongoDB",
    tags=["CRUD MongoDB"]
)

# ---------------------------
# General
# ---------------------------
@router.get("/check-db")
def check_db():
    return mongoDB.check_database_connection()

# ---------------------------
# CRUD Usuarios
# ---------------------------
@router.post("/usuarios")
def crear_usuario(usuario: Usuario):
    usuario_id = mongoDB.crear_usuario(usuario.dict())
    return {"id": usuario_id}

@router.get("/usuarios")
def listar_usuarios():
    return mongoDB.obtener_usuarios()

@router.get("/usuarios/{usuario_id}")
def obtener_usuario(usuario_id: str):
    usuario = mongoDB.obtener_usuario_por_id(usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put("/usuarios/{usuario_id}")
def actualizar_usuario(usuario_id: str, usuario: Usuario):
    if not mongoDB.actualizar_usuario(usuario_id, usuario.dict()):
        raise HTTPException(status_code=404, detail="Usuario no encontrado o sin cambios")
    return {"mensaje": "Usuario actualizado"}

@router.delete("/usuarios/{usuario_id}")
def eliminar_usuario(usuario_id: str):
    if not mongoDB.eliminar_usuario(usuario_id):
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"mensaje": "Usuario eliminado"}


# ---------------------------
# CRUD Servicios
# ---------------------------
@router.post("/servicios")
def crear_servicio(servicio: Servicio):
    servicio_id = mongoDB.crear_servicio(servicio.dict())
    return {"id": servicio_id}

@router.get("/servicios")
def listar_servicios():
    return mongoDB.obtener_servicios()

@router.get("/servicios/{servicio_id}")
def obtener_servicio(servicio_id: str):
    servicio = mongoDB.obtener_servicio_por_id(servicio_id)
    if servicio is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return servicio

@router.put("/servicios/{servicio_id}")
def actualizar_servicio(servicio_id: str, servicio: Servicio):
    if not mongoDB.actualizar_servicio(servicio_id, servicio.dict()):
        raise HTTPException(status_code=404, detail="Servicio no encontrado o sin cambios")
    return {"mensaje": "Servicio actualizado"}

@router.delete("/servicios/{servicio_id}")
def eliminar_servicio(servicio_id: str):
    if not mongoDB.eliminar_servicio(servicio_id):
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return {"mensaje": "Servicio eliminado"}
