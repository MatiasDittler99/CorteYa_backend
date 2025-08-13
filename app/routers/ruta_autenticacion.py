from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session
from app.core.base_de_datos import get_session
from app.models.modelo_usuario import Usuario
from app.schemas.esquema_usuario import UsuarioCreate, UsuarioLogin, UsuarioRead, UsuarioUpdate
from app.services import autenticacion as auth
from app.auth_utils import create_access_token, verify_token
from typing import Optional

router = APIRouter(prefix="/auth", tags=["Auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

@router.post("/signup", response_model=UsuarioRead)
def signup(data: UsuarioCreate, db: Session = Depends(get_session)):
    return auth.crear_usuario(db, data)

@router.post("/login")
def login(data: UsuarioLogin, db: Session = Depends(get_session)):
    user = auth.autenticar_usuario(db, data.username, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
    access_token = create_access_token(data={"sub": str(user.id_usuario)})
    return {"access_token": access_token, "token_type": "bearer", "user": user}

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_session)) -> Usuario:
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido o expirado")
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
    user = db.get(Usuario, int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario no encontrado")
    return user

@router.get("/me", response_model=UsuarioRead)
def me(current_user: Usuario = Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=UsuarioRead)
def update_me(
    data: UsuarioUpdate,
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_session)
):
    try:
        return auth.actualizar_usuario(current_user, data, db)
    except HTTPException:
        raise
    except Exception as e:
        print("Error en /auth/me PUT:", e)
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_mi_cuenta(
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_session)
):
    db.delete(current_user)
    db.commit()
    return
