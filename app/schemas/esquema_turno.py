from typing import List, Optional
from datetime import date, time
from sqlmodel import SQLModel, Field

from app.schemas.esquema_cliente import ClienteRead
from app.schemas.esquema_empleado import EmpleadoRead
from app.schemas.esquema_servicio import ServicioRead

class TurnoBase(SQLModel):
    id_cliente: int
    id_empleado: int
    id_servicio: int
    fecha: date
    hora: time
    estado: str  # validar que sea 'pendiente', 'confirmado', 'cancelado' en la lógica

class TurnoCreate(TurnoBase):
    pass

class TurnoRead(TurnoBase):
    id_turno: int

    # Para evitar recursividad excesiva se suelen incluir solo ids o datos resumidos:
    # Podés agregar datos anidados con cuidado:
    cliente: Optional[ClienteRead] = None
    empleado: Optional[EmpleadoRead] = None
    servicio: Optional[ServicioRead] = None

    class Config:
        orm_mode = True