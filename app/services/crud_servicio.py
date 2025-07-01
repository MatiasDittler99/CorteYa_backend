from typing import List, Optional
from sqlmodel import Session, select
from app.models.modelo_servicio import Servicio
from app.schemas.esquema_servicio import ServicioCreate

def get_servicios(db: Session) -> List[Servicio]:
    return db.exec(select(Servicio)).all()

def get_servicio(db: Session, servicio_id: int) -> Optional[Servicio]:
    return db.get(Servicio, servicio_id)

def create_servicio(db: Session, servicio: ServicioCreate) -> Servicio:
    db_servicio = Servicio.from_orm(servicio)
    db.add(db_servicio)
    db.commit()
    db.refresh(db_servicio)
    return db_servicio

def update_servicio(db: Session, servicio_id: int, servicio_data: ServicioCreate) -> Optional[Servicio]:
    db_servicio = db.get(Servicio, servicio_id)
    if not db_servicio:
        return None
    for key, value in servicio_data.dict().items():
        setattr(db_servicio, key, value)
    db.add(db_servicio)
    db.commit()
    db.refresh(db_servicio)
    return db_servicio

def delete_servicio(db: Session, servicio_id: int) -> bool:
    db_servicio = db.get(Servicio, servicio_id)
    if not db_servicio:
        return False
    db.delete(db_servicio)
    db.commit()
    return True
