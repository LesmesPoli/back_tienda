## Clonacion del proyecto con Git
```powershell
git clone https://github.com/LesmesPoli/back_tienda.git
``` 

## Creación del entorno virtual
```Windows (PowerShell)
python -m venv env
``` 
```linux/os (bash)
python3 -m venv env
``` 

### Entrar en el entorno virtual
```Windows (PowerShell)
env\Scripts\activate
```
```linux/os (bash)
source env/bin/activate
```

### Instalar dependencias
```
pip install -r requeriments.txt
```
### Para visualizar las dependencias consulta el archivo requirements.txt 
```
pip freeze requeriments.txt
```
```
pip list
```
### Salir del entorno virtual
```Windows (PowerShell)
deactivate
```
```linux/os (bash)
deactivate
```

### Ejecutar servidor local (Generación de cache)
```
uvicorn app.main:app --reload
```
### Ejecutar servidor local (Sin generar cache)
``` Windows (PowerShell)
# Windows
set PYTHONDONTWRITEBYTECODE=1 && uvicorn app.main:app --reload
```
```linux/os (bash)
PYTHONDONTWRITEBYTECODE=1 uvicorn app.main:app --reload
```

Ruta de consultas de fastAPI [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

#### 1. Usuarios

- POST /MongoDB/usuarios → Crear usuario

- GET /MongoDB/usuarios → Listar usuarios

- GET /MongoDB/usuarios/{id} → Obtener usuario

- PUT /MongoDB/usuarios/{id} → Actualizar usuario

- DELETE /MongoDB/usuarios/{id} → Eliminar usuario

#### 2. Servicios

- POST /MongoDB/servicios → Crear servicio

- GET /MongoDB/servicios → Listar servicios

- GET /MongoDB/servicios/{id} → Obtener servicio

- PUT /MongoDB/servicios/{id} → Actualizar servicio

- DELETE /MongoDB/servicios/{id} → Eliminar servicio