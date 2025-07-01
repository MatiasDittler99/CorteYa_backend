from typing import List, Optional
from datetime import date, time
from sqlmodel import SQLModel, Field

class EmpleadoBase(SQLModel):
    nombre_completo: str

class EmpleadoCreate(EmpleadoBase):
    pass

class EmpleadoRead(EmpleadoBase):
    id_empleado: int

    class Config:
        orm_mode = True