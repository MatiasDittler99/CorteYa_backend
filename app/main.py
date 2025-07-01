from fastapi import FastAPI
from sqlmodel import SQLModel
from app.core.base_de_datos import engine  # Donde tengas el engine configurado
from app.seed import seed_db

# Importar los routers
from app.routers import (
    ruta_cliente,
    ruta_empleado,
    ruta_especialidad,
    ruta_empleado_especialidad,
    ruta_servicio,
    ruta_turno,
)

app = FastAPI(title="API de Peluquería/Barbería")

# Crear tablas al iniciar la app
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)
    seed_db()
    
# Incluir los routers
app.include_router(ruta_cliente.router)
app.include_router(ruta_empleado.router)
app.include_router(ruta_especialidad.router)
app.include_router(ruta_empleado_especialidad.router)
app.include_router(ruta_servicio.router)
app.include_router(ruta_turno.router)

