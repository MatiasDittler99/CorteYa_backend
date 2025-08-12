from fastapi import FastAPI
from sqlmodel import SQLModel
from app.core.base_de_datos import engine  # Donde tengas el engine configurado
from app.seed import seed_db, crear_usuario_admin_si_no_existe
from fastapi.middleware.cors import CORSMiddleware
import os

# Importar los routers
from app.routers import (
    ruta_cliente,
    ruta_empleado,
    ruta_especialidad,
    ruta_empleado_especialidad,
    ruta_servicio,
    ruta_turno,
    ruta_autenticacion,
    ruta_usuario
)

app = FastAPI(title="API de Peluquería/Barbería")

@app.get("/")
def read_root():
    return {"message": "CorteYa Backend Funcionando"}

# CORS para desarrollo (acepta todo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500", "https://matiasdittler99.github.io-CorteYa"],  # ⬅️ Durante desarrollo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear tablas al iniciar la app
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)
    seed_db()
    crear_usuario_admin_si_no_existe()
    
# Incluir los routers
app.include_router(ruta_cliente.router)
app.include_router(ruta_empleado.router)
app.include_router(ruta_especialidad.router)
app.include_router(ruta_empleado_especialidad.router)
app.include_router(ruta_servicio.router)
app.include_router(ruta_turno.router)
app.include_router(ruta_autenticacion.router)
app.include_router(ruta_usuario.router)

