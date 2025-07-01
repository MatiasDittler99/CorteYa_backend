from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from datetime import datetime, timedelta, date, time

from app.schemas.esquema_turno import TurnoCreate, TurnoRead
from app.services import crud_turno
from app.core.base_de_datos import get_session
from app.models.modelo_turno import Turno
from app.models.modelo_servicio import Servicio

router = APIRouter(prefix="/turnos", tags=["Turnos"])

@router.get("/", response_model=List[TurnoRead])
def listar_turnos(db: Session = Depends(get_session)):
    return crud_turno.get_turnos(db)

@router.get("/{id}", response_model=TurnoRead)
def obtener_turno(id: int, db: Session = Depends(get_session)):
    turno = crud_turno.get_turno(db, id)
    if not turno:
        raise HTTPException(status_code=404, detail="Turno no encontrado")
    return turno

@router.post("/", response_model=TurnoRead)
def crear_turno(turno: TurnoCreate, db: Session = Depends(get_session)):
    return crud_turno.create_turno(db, turno)

@router.put("/{id}", response_model=TurnoRead)
def actualizar_turno(id: int, turno: TurnoCreate, db: Session = Depends(get_session)):
    actualizado = crud_turno.update_turno(db, id, turno)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Turno no encontrado")
    return actualizado

@router.delete("/{id}")
def eliminar_turno(id: int, db: Session = Depends(get_session)):
    eliminado = crud_turno.delete_turno(db, id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Turno no encontrado")
    return {"ok": True}
