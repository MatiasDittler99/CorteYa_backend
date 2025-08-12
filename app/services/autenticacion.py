from datetime import date
from passlib.context import CryptContext
from sqlmodel import Session, select
from fastapi import HTTPException
from app.models.modelo_usuario import Usuario
from app.schemas.esquema_usuario import UsuarioCreate, UsuarioUpdate
from app.core.base_de_datos import engine
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def crear_usuario(session: Session, datos: UsuarioCreate) -> Usuario:
    if session.exec(select(Usuario).where(Usuario.username == datos.username)).first():
        raise HTTPException(status_code=400, detail="Nombre de usuario ya existe")

    hashed = get_password_hash(datos.password)

    usuario = Usuario(
        nombre=datos.nombre,
        apellido=datos.apellido,
        fecha_nacimiento=datos.fecha_nacimiento,
        email=datos.email,
        username=datos.username,
        hashed_password=hashed
    )
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return usuario

def autenticar_usuario(session: Session, username: str, password: str) -> Usuario | None:
    user = session.exec(select(Usuario).where(Usuario.username == username)).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def actualizar_usuario(user: Usuario, data: UsuarioUpdate, session: Session) -> Usuario:
    if data.nombre:
        user.nombre = data.nombre
    if data.apellido:
        user.apellido = data.apellido
    if data.fecha_nacimiento:
        user.fecha_nacimiento = data.fecha_nacimiento
    if data.email:
        user.email = data.email
    if data.username:
        user.username = data.username
    if data.password:
        # Verificar que la nueva contraseña no sea igual a la anterior
        if verify_password(data.password, user.hashed_password):
            raise HTTPException(status_code=400, detail="La nueva contraseña debe ser diferente a la anterior")
        user.hashed_password = get_password_hash(data.password)

    session.add(user)
    session.commit()
    session.refresh(user)
    return user
