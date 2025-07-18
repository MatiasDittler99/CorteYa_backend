from fastapi import FastAPI
from sqlmodel import SQLModel
from app.core.base_de_datos import engine  # Donde tengas el engine configurado
from app.seed import seed_db, crear_usuario_admin_si_no_existe

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

