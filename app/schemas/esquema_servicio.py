from typing import List, Optional
from datetime import date, time
from sqlmodel import SQLModel, Field
from pydantic import validator

class ServicioBase(SQLModel):
    nombre_servicio: str
    duracion: int
    precio: float
    
    @validator("duracion")
    def duracion_positiva(cls, v):
        if v <= 0:
            raise ValueError("La duración debe ser un número positivo")
        return v

    @validator("precio")
    def precio_positivo(cls, v):
        if v <= 0:
            raise ValueError("El precio debe ser mayor a cero")
        return v

class ServicioCreate(ServicioBase):
    pass

class ServicioRead(ServicioBase):
    id_servicio: int

    class Config:
        orm_mode = True