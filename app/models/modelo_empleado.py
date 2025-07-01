from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import date, time

if TYPE_CHECKING:
    from app.models.modelo_empleado_especialidad import EmpleadoEspecialidad
    from app.models.modelo_turno import Turno

class Empleado(SQLModel, table=True):
    __tablename__="empleado"
    
    id_empleado: Optional[int] = Field(default=None, primary_key=True)
    nombre_completo: str

    turnos: List["Turno"] = Relationship(back_populates="empleado")
    especialidades: List["EmpleadoEspecialidad"] = Relationship(back_populates="empleado")
