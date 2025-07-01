from typing import List, Optional
from datetime import date, time
from sqlmodel import SQLModel, Field

class EspecialidadBase(SQLModel):
    nombre_completo: str

class EspecialidadCreate(EspecialidadBase):
    pass

class EspecialidadRead(EspecialidadBase):
    id_especialidad: int

    class Config:
        orm_mode = True