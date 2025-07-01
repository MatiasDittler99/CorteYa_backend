from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List

from app.schemas.esquema_especialidad import EspecialidadCreate, EspecialidadRead
from app.services import crud_especialidad
from app.core.base_de_datos import get_session

router = APIRouter(prefix="/especialidades", tags=["Especialidades"])

@router.get("/", response_model=List[EspecialidadRead])
def listar_especialidades(db: Session = Depends(get_session)):
    return crud_especialidad.get_especialidades(db)

@router.post("/", response_model=EspecialidadRead)
def crear_especialidad(especialidad: EspecialidadCreate, db: Session = Depends(get_session)):
    return crud_especialidad.create_especialidad(db, especialidad)

@router.get("/{id}", response_model=EspecialidadRead)
def obtener_especialidad(id: int, db: Session = Depends(get_session)):
    esp = crud_especialidad.get_especialidad(db, id)
    if not esp:
        raise HTTPException(status_code=404, detail="Especialidad no encontrada")
    return esp

@router.put("/{id}", response_model=EspecialidadRead)
def actualizar_especialidad(id: int, especialidad: EspecialidadCreate, db: Session = Depends(get_session)):
    actualizado = crud_especialidad.update_especialidad(db, id, especialidad)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Especialidad no encontrada")
    return actualizado

@router.delete("/{id}")
def eliminar_especialidad(id: int, db: Session = Depends(get_session)):
    eliminado = crud_especialidad.delete_especialidad(db, id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Especialidad no encontrada")
    return {"ok": True}
