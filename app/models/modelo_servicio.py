from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import date, time

if TYPE_CHECKING:
    from app.models.modelo_turno import Turno

class Servicio(SQLModel, table=True):
    __tablename__="servicio"
    
    id_servicio: Optional[int] = Field(default=None, primary_key=True)
    nombre_servicio: str
    duracion: int
    precio: float

    turnos: List["Turno"] = Relationship(back_populates="servicio")
