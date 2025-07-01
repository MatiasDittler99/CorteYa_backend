from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import date, time

if TYPE_CHECKING:
    from app.models.modelo_empleado_especialidad import EmpleadoEspecialidad

class Especialidad(SQLModel, table=True):
    __tablename__="especialidad"
    
    id_especialidad: Optional[int] = Field(default=None, primary_key=True)
    nombre_completo: str = Field(unique=True)

    empleados: List["EmpleadoEspecialidad"] = Relationship(back_populates="especialidad")
