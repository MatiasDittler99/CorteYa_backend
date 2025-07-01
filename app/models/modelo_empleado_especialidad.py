from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import date, time

if TYPE_CHECKING:
    from app.models.modelo_empleado import Empleado
    from app.models.modelo_especialidad import Especialidad

class EmpleadoEspecialidad(SQLModel, table=True):
    __tablename__="empleadoespecialidad"
    
    id_empleado: int = Field(foreign_key="empleado.id_empleado", primary_key=True)
    id_especialidad: int = Field(foreign_key="especialidad.id_especialidad", primary_key=True)

    empleado: Optional["Empleado"] = Relationship(back_populates="especialidades")
    especialidad: Optional["Especialidad"] = Relationship(back_populates="empleados")
