## pre requisitos

Antes de clonar y ejecutar el proyecto, asegúrate de tener instalado y configurado lo siguiente:

### 1. Python 3.10+
Verifica la instalación con:
```Windows (PowerShell)
python --version
```
```linux/os (bash)
python3 --version
```

### 2. pip (Administrador de paquetes de Python)
Viene incluido en la mayoría de instalaciones de Python. Verifica con:
```Windows (PowerShell)
pip --version
```

### 3. MongoDB en local
Descarga [MongoDB Compass](https://www.mongodb.com/try/download/community) para explorar y administrar la base de datos con interfaz gráfica.

### 4. Git (para clonar el repositorio). 
Verifica la instalación con:
```Windows (PowerShell)
git --version
```

---

## Clonacion del proyecto con Git
```Windows (PowerShell)
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

---
## Ejecusion de proyecto

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

---

## 📂 Endpoints disponibles

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

---

[Frontend del proyecto](https://github.com/LesmesPoli/front_tienda.git)