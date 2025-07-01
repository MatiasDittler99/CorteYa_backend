from typing import List, Optional
from datetime import datetime, timedelta, time as dtime
from sqlmodel import Session, select
from app.models.modelo_turno import Turno
from app.models.modelo_servicio import Servicio
from app.models.modelo_cliente import Cliente
from app.models.modelo_empleado import Empleado
from app.schemas.esquema_turno import TurnoCreate
from fastapi import HTTPException

def get_turnos(db: Session) -> List[Turno]:
    return db.exec(select(Turno)).all()

def get_turno(db: Session, turno_id: int) -> Optional[Turno]:
    return db.get(Turno, turno_id)

def create_turno(db: Session, turno: TurnoCreate) -> Turno:
    # Validar fecha y hora no en el pasado
    fecha_hora_turno = datetime.combine(turno.fecha, turno.hora)
    if fecha_hora_turno < datetime.now():
        raise HTTPException(status_code=400, detail="No se puede crear un turno en el pasado.")

    # Validar duración positiva del servicio
    servicio = db.get(Servicio, turno.id_servicio)
    if not servicio:
        raise HTTPException(status_code=400, detail="Servicio no encontrado.")
    if servicio.duracion <= 0:
        raise HTTPException(status_code=400, detail="La duración del servicio debe ser mayor a 0.")

    # (Opcional) Validar existencia de cliente y empleado
    if not db.get(Cliente, turno.id_cliente):
        raise HTTPException(status_code=404, detail="Cliente no encontrado.")
    if not db.get(Empleado, turno.id_empleado):
        raise HTTPException(status_code=404, detail="Empleado no encontrado.")
    # Validar solapamiento de turnos para el mismo empleado
    if _check_solapamiento(db, turno):
        raise HTTPException(status_code=400, detail="El turno se solapa con otro turno existente para este empleado.")

    db_turno = Turno.from_orm(turno)
    db.add(db_turno)
    db.commit()
    db.refresh(db_turno)
    return db_turno

def update_turno(db: Session, turno_id: int, turno_data: TurnoCreate) -> Optional[Turno]:
    db_turno = db.get(Turno, turno_id)
    if not db_turno:
        return None

    if _check_solapamiento(db, turno_data, turno_id):
        raise HTTPException(status_code=400, detail="El turno se solapa con otro turno existente para este empleado.")

    for key, value in turno_data.dict().items():
        setattr(db_turno, key, value)
    db.add(db_turno)
    db.commit()
    db.refresh(db_turno)
    return db_turno

def delete_turno(db: Session, turno_id: int) -> bool:
    db_turno = db.get(Turno, turno_id)
    if not db_turno:
        return False
    db.delete(db_turno)
    db.commit()
    return True

def _check_solapamiento(db: Session, turno: TurnoCreate, turno_id: Optional[int] = None) -> bool:
    """
    Retorna True si hay solapamiento con otro turno para el mismo empleado en la misma fecha.
    turno_id es para ignorar el turno actual al actualizar.
    """
    # Obtener duración del servicio nuevo
    servicio = db.get(Servicio, turno.id_servicio)
    if not servicio:
        raise HTTPException(status_code=400, detail="Servicio no encontrado.")

    # Calcular rango horario del nuevo turno
    inicio_nuevo = datetime.combine(turno.fecha, turno.hora)
    fin_nuevo = inicio_nuevo + timedelta(minutes=servicio.duracion)

    # Query para turnos existentes del mismo empleado en la misma fecha (excepto el que se actualiza)
    query = select(Turno).where(
        Turno.id_empleado == turno.id_empleado,
        Turno.fecha == turno.fecha
    )
    if turno_id:
        query = query.where(Turno.id_turno != turno_id)

    turnos_existentes = db.exec(query).all()

    for t in turnos_existentes:
        servicio_existente = db.get(Servicio, t.id_servicio)
        inicio_existente = datetime.combine(t.fecha, t.hora)
        fin_existente = inicio_existente + timedelta(minutes=servicio_existente.duracion)

        # Condiciones para solapamiento
        if (inicio_nuevo < fin_existente and fin_nuevo > inicio_existente):
            return True
    return False
