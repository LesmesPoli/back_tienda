from fastapi import FastAPI
from app.routes import (
    mongodb_routes,
)
app = FastAPI()

@app.get("/", tags=["Inicio"])
def index():
    return "wenas"

# DB noSQL
app.include_router(mongodb_routes.router)
