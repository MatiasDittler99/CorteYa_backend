from typing import List, Optional
from sqlmodel import Session, select
from app.models.modelo_empleado import Empleado
from app.schemas.esquema_empleado import EmpleadoCreate

def get_empleados(db: Session) -> List[Empleado]:
    return db.exec(select(Empleado)).all()

def get_empleado(db: Session, empleado_id: int) -> Optional[Empleado]:
    return db.get(Empleado, empleado_id)

def create_empleado(db: Session, empleado: EmpleadoCreate) -> Empleado:
    db_empleado = Empleado.from_orm(empleado)
    db.add(db_empleado)
    db.commit()
    db.refresh(db_empleado)
    return db_empleado

def update_empleado(db: Session, empleado_id: int, empleado_data: EmpleadoCreate) -> Optional[Empleado]:
    db_empleado = db.get(Empleado, empleado_id)
    if not db_empleado:
        return None
    for key, value in empleado_data.dict().items():
        setattr(db_empleado, key, value)
    db.add(db_empleado)
    db.commit()
    db.refresh(db_empleado)
    return db_empleado

def delete_empleado(db: Session, empleado_id: int) -> bool:
    db_empleado = db.get(Empleado, empleado_id)
    if not db_empleado:
        return False
    db.delete(db_empleado)
    db.commit()
    return True
