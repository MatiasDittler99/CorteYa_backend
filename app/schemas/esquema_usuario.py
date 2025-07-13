from pydantic import BaseModel, EmailStr
from pydantic import constr
from datetime import date
from typing import Optional, Annotated

class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    fecha_nacimiento: date
    email: EmailStr
    username: Annotated[str,constr(min_length=4, max_length=30)]

class UsuarioCreate(UsuarioBase):
    password: Annotated[str, constr(min_length=8)]

class UsuarioLogin(BaseModel):
    username: str
    password: str

class UsuarioRead(BaseModel):
    id_usuario: int
    nombre: str
    apellido: str
    fecha_nacimiento: date
    email: EmailStr
    username: str

    class Config:
        orm_mode = True

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    fecha_nacimiento: Optional[str] = None
    email: Optional[EmailStr] = None
    username: Optional[Annotated[str, constr(min_length=4, max_length=30)]] = None
    password: Optional[Annotated[str, constr(min_length=8)]] = None
    
    model_config = {"from_attributes": True}
