from typing import List, Optional
from datetime import date, time
from sqlmodel import SQLModel, Field

class ServicioBase(SQLModel):
    nombre_servicio: str
    duracion: int
    precio: float

class ServicioCreate(ServicioBase):
    pass

class ServicioRead(ServicioBase):
    id_servicio: int

    class Config:
        orm_mode = True