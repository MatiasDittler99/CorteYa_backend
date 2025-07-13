from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from app.core.base_de_datos import get_session
from app.schemas.esquema_usuario import UsuarioRead
from app.models.modelo_usuario import Usuario
from typing import List
from fastapi import HTTPException, status, Response
from app.routers.ruta_autenticacion import get_current_user  # Import necesario


router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.get("/", response_model=List[UsuarioRead])
def obtener_usuarios(db: Session = Depends(get_session)):
    usuarios = db.exec(select(Usuario)).all()
    return usuarios


@router.delete("/{id_usuario}", status_code=204)
def eliminar_usuario(
    id_usuario: int,
    db: Session = Depends(get_session),
    # Si solo la querés para pruebas locales y no querés protegerla, podés comentar la autenticación temporalmente
    current_user = Depends(get_current_user)  # protege con login
):
    usuario = db.get(Usuario, id_usuario)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    db.delete(usuario)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
