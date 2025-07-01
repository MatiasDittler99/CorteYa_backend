from typing import List, Optional
from datetime import date, time, datetime
from sqlmodel import SQLModel, Field
from pydantic import BaseModel, validator, constr
from enum import Enum

from app.schemas.esquema_cliente import ClienteRead
from app.schemas.esquema_empleado import EmpleadoRead
from app.schemas.esquema_servicio import ServicioRead

class EstadoTurno(str, Enum):
    pendiente = "pendiente"
    confirmado = "confirmado"
    cancelado = "cancelado"
    

class TurnoBase(SQLModel):
    id_cliente: int
    id_empleado: int
    id_servicio: int
    fecha: date
    hora: time
    estado: EstadoTurno

    @validator('fecha')
    def fecha_no_pasada(cls, v):
        if v < datetime.now().date():
            raise ValueError("La fecha no puede ser en el pasado")
        return v

    @validator('hora')
    def hora_sin_segundos(cls, v):
        if v.second != 0 or v.microsecond != 0:
            raise ValueError("La hora no debe tener segundos ni microsegundos")
        return v

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