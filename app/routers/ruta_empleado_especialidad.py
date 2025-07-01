from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List

from app.schemas.esquema_empleado_especialidad import EmpleadoEspecialidadCreate, EmpleadoEspecialidadRead
from app.services import crud_empleado_especialidad
from app.core.base_de_datos import get_session

router = APIRouter(prefix="/empleado-especialidades", tags=["EmpleadoEspecialidad"])

@router.get("/", response_model=List[EmpleadoEspecialidadRead])
def listar_relaciones(db: Session = Depends(get_session)):
    return crud_empleado_especialidad.get_empleado_especialidades(db)

@router.post("/", response_model=EmpleadoEspecialidadRead)
def crear_relacion(rel: EmpleadoEspecialidadCreate, db: Session = Depends(get_session)):
    return crud_empleado_especialidad.create_empleado_especialidad(db, rel)

@router.delete("/", status_code=204)
def eliminar_relacion(id_empleado: int, id_especialidad: int, db: Session = Depends(get_session)):
    eliminado = crud_empleado_especialidad.delete_empleado_especialidad(db, id_empleado, id_especialidad)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Relación no encontrada")
    return {"ok": True}
