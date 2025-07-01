from typing import List, Optional
from datetime import date, time
from sqlmodel import SQLModel, Field

class EmpleadoEspecialidadBase(SQLModel):
    id_empleado: int
    id_especialidad: int

class EmpleadoEspecialidadCreate(EmpleadoEspecialidadBase):
    pass

class EmpleadoEspecialidadRead(EmpleadoEspecialidadBase):
    # Opcionalmente puedes agregar datos anidados
    # pero ojo con ciclos infinitos
    class Config:
        orm_mode = True