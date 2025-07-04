from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import date, time
from enum import Enum as PyEnum
from sqlalchemy import Column, Enum

if TYPE_CHECKING:
    from app.models.modelo_cliente import Cliente
    from app.models.modelo_empleado import Empleado
    from app.models.modelo_servicio import Servicio
    
class EstadoTurnoEnum(str, PyEnum):
    pendiente = "pendiente"
    confirmado = "confirmado"
    cancelado = "cancelado"

class Turno(SQLModel, table=True):
    __tablename__="turno"
    
    id_turno: Optional[int] = Field(default=None, primary_key=True)
    id_cliente: int = Field(foreign_key="cliente.id_cliente")
    id_empleado: int = Field(foreign_key="empleado.id_empleado")
    id_servicio: int = Field(foreign_key="servicio.id_servicio")

    fecha: date
    hora: time
    estado: EstadoTurnoEnum = Field(
        sa_column=Column(Enum(EstadoTurnoEnum), nullable=False)
    )

    cliente: Optional["Cliente"] = Relationship(back_populates="turnos")
    empleado: Optional["Empleado"] = Relationship(back_populates="turnos")
    servicio: Optional["Servicio"] = Relationship(back_populates="turnos")
