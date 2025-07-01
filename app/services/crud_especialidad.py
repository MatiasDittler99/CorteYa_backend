from typing import List, Optional
from sqlmodel import Session, select
from app.models.modelo_especialidad import Especialidad
from app.schemas.esquema_especialidad import EspecialidadCreate

def get_especialidades(db: Session) -> List[Especialidad]:
    return db.exec(select(Especialidad)).all()

def get_especialidad(db: Session, especialidad_id: int) -> Optional[Especialidad]:
    return db.get(Especialidad, especialidad_id)

def create_especialidad(db: Session, especialidad: EspecialidadCreate) -> Especialidad:
    db_esp = Especialidad.from_orm(especialidad)
    db.add(db_esp)
    db.commit()
    db.refresh(db_esp)
    return db_esp

def update_especialidad(db: Session, especialidad_id: int, especialidad_data: EspecialidadCreate) -> Optional[Especialidad]:
    db_esp = db.get(Especialidad, especialidad_id)
    if not db_esp:
        return None
    for key, value in especialidad_data.dict().items():
        setattr(db_esp, key, value)
    db.add(db_esp)
    db.commit()
    db.refresh(db_esp)
    return db_esp

def delete_especialidad(db: Session, especialidad_id: int) -> bool:
    db_esp = db.get(Especialidad, especialidad_id)
    if not db_esp:
        return False
    db.delete(db_esp)
    db.commit()
    return True
