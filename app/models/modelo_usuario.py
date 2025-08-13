from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"

    id_usuario: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    apellido: str
    fecha_nacimiento: Optional[date] = None
    email: str = Field(unique=True)
    username: str = Field(unique=True, index=True)
    hashed_password: str