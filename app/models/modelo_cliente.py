from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import date, time

if TYPE_CHECKING:
    from app.models.modelo_turno import Turno

class Cliente(SQLModel, table=True):
    __tablename__="cliente"
    
    id_cliente: Optional[int] = Field(default=None, primary_key=True)
    nombre_completo: str
    telefono: str = Field(unique=True)
    email: str = Field(unique=True)

    turnos: List["Turno"] = Relationship(back_populates="cliente")
