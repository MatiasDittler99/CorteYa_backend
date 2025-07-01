from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List

from app.schemas.esquema_servicio import ServicioCreate, ServicioRead
from app.services import crud_servicio
from app.core.base_de_datos import get_session

router = APIRouter(prefix="/servicios", tags=["Servicios"])

@router.get("/", response_model=List[ServicioRead])
def listar_servicios(db: Session = Depends(get_session)):
    return crud_servicio.get_servicios(db)

@router.post("/", response_model=ServicioRead)
def crear_servicio(servicio: ServicioCreate, db: Session = Depends(get_session)):
    return crud_servicio.create_servicio(db, servicio)

@router.get("/{id}", response_model=ServicioRead)
def obtener_servicio(id: int, db: Session = Depends(get_session)):
    serv = crud_servicio.get_servicio(db, id)
    if not serv:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return serv

@router.put("/{id}", response_model=ServicioRead)
def actualizar_servicio(id: int, servicio: ServicioCreate, db: Session = Depends(get_session)):
    actualizado = crud_servicio.update_servicio(db, id, servicio)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return actualizado

@router.delete("/{id}")
def eliminar_servicio(id: int, db: Session = Depends(get_session)):
    eliminado = crud_servicio.delete_servicio(db, id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return {"ok": True}
