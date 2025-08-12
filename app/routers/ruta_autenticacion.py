from fastapi import APIRouter, Depends, HTTPException, Request, Response, Cookie
from sqlmodel import Session
from app.core.base_de_datos import get_session
from app.models.modelo_usuario import Usuario
from app.schemas.esquema_usuario import UsuarioCreate, UsuarioLogin, UsuarioRead, UsuarioUpdate
from app.services import autenticacion as auth
import uuid

router = APIRouter(prefix="/auth", tags=["Auth"])

# Diccionario en memoria para sesiones (ejemplo simple)
sesiones = {}

@router.post("/signup", response_model=UsuarioRead)
def signup(data: UsuarioCreate, db: Session = Depends(get_session)):
    return auth.crear_usuario(db, data)

@router.post("/login", response_model=UsuarioRead)
def login(data: UsuarioLogin, response: Response, db: Session = Depends(get_session)):
    user = auth.autenticar_usuario(db, data.username, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    
    session_id = str(uuid.uuid4())
    sesiones[session_id] = user.id_usuario

    # Setear cookie httpOnly para manejar sesión
    response.set_cookie(key="session_id", value=session_id, httponly=True, secure=False,samesite="none")
    
    return user

@router.post("/logout")
def logout(response: Response, session_id: str = Cookie(default=None)):
    if session_id in sesiones:
        sesiones.pop(session_id)
    response.delete_cookie(key="session_id")
    return {"msg": "Sesión cerrada"}

def get_current_user(session_id: str = Cookie(default=None), db: Session = Depends(get_session)):
    if not session_id or session_id not in sesiones:
        raise HTTPException(status_code=401, detail="No autenticado")
    user_id = sesiones[session_id]
    user = db.get(auth.Usuario, user_id)
    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
    return user

@router.get("/me", response_model=UsuarioRead)
def me(current_user: UsuarioRead = Depends(get_current_user)):
    return current_user

@router.put("/me", response_model=UsuarioRead)
def update_me(
    data: UsuarioUpdate,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_session)
):
    return auth.actualizar_usuario(current_user, data, db)

from fastapi import status

# @router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
# def delete_me(
#     current_user=Depends(get_current_user),
#     db: Session = Depends(get_session),
#     response: Response = None
# ):
#     db.delete(current_user)
#     db.commit()
    
#     # Eliminar la cookie de sesión si existe
#     if response:
#         response.delete_cookie(key="session_id")
    
#     return

@router.delete("/me", status_code=204)
def eliminar_mi_cuenta(
    response: Response,
    current_user: Usuario = Depends(get_current_user),
    db: Session = Depends(get_session)
):
    db.delete(current_user)
    db.commit()

    # Cerrar sesión (borrar cookie)
    if current_user.id_usuario in sesiones.values():
        for sid, uid in list(sesiones.items()):
            if uid == current_user.id_usuario:
                sesiones.pop(sid)
                break
        response.delete_cookie(key="session_id")

    return Response(status_code=204)

@router.get("/debug-cookies")
def debug_cookies(request: Request):
    return {"cookies": request.cookies}
