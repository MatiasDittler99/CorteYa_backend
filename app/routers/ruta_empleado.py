from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List

from app.schemas.esquema_empleado import EmpleadoCreate, EmpleadoRead
from app.services import crud_empleado
from app.core.base_de_datos import get_session

router = APIRouter(prefix="/empleados", tags=["Empleados"])

@router.get("/", response_model=List[EmpleadoRead])
def listar_empleados(db: Session = Depends(get_session)):
    return crud_empleado.get_empleados(db)

@router.post("/", response_model=EmpleadoRead)
def crear_empleado(empleado: EmpleadoCreate, db: Session = Depends(get_session)):
    return crud_empleado.create_empleado(db, empleado)

@router.get("/{empleado_id}", response_model=EmpleadoRead)
def obtener_empleado(empleado_id: int, db: Session = Depends(get_session)):
    emp = crud_empleado.get_empleado(db, empleado_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return emp

@router.put("/{empleado_id}", response_model=EmpleadoRead)
def actualizar_empleado(empleado_id: int, empleado: EmpleadoCreate, db: Session = Depends(get_session)):
    actualizado = crud_empleado.update_empleado(db, empleado_id, empleado)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return actualizado

@router.delete("/{empleado_id}")
def eliminar_empleado(empleado_id: int, db: Session = Depends(get_session)):
    eliminado = crud_empleado.delete_empleado(db, empleado_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return {"ok": True}
