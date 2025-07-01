from typing import List
from sqlmodel import Session, select
from app.models.modelo_empleado_especialidad import EmpleadoEspecialidad
from app.schemas.esquema_empleado_especialidad import EmpleadoEspecialidadCreate

def get_empleado_especialidades(db: Session) -> List[EmpleadoEspecialidad]:
    return db.exec(select(EmpleadoEspecialidad)).all()

def create_empleado_especialidad(db: Session, rel: EmpleadoEspecialidadCreate) -> EmpleadoEspecialidad:
    db_rel = EmpleadoEspecialidad.from_orm(rel)
    db.add(db_rel)
    db.commit()
    db.refresh(db_rel)
    return db_rel

def delete_empleado_especialidad(db: Session, id_empleado: int, id_especialidad: int) -> bool:
    rel = db.get(EmpleadoEspecialidad, (id_empleado, id_especialidad))
    if not rel:
        return False
    db.delete(rel)
    db.commit()
    return True
