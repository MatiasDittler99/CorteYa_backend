from typing import List, Optional
from datetime import date, time
from sqlmodel import SQLModel, Field

class ClienteBase(SQLModel):
    nombre_completo: str
    telefono: str
    email: str

class ClienteCreate(ClienteBase):
    pass

class ClienteRead(ClienteBase):
    id_cliente: int

    class Config:
        orm_mode = True