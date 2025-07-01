import pytest
from datetime import datetime, timedelta, date, time
import uuid

from app.services import crud_turno, crud_cliente, crud_empleado, crud_servicio
from app.schemas.esquema_turno import TurnoCreate
from app.schemas.esquema_cliente import ClienteCreate
from app.schemas.esquema_empleado import EmpleadoCreate
from app.schemas.esquema_servicio import ServicioCreate


def setup_dependencies(session):
    telefono_unico = f"15{uuid.uuid4().hex[:6]}"
    email_unico = f"cliente_{uuid.uuid4().hex[:8]}@test.com"
    email_empleado = f"empleado_{uuid.uuid4().hex[:8]}@test.com"
    telefono_empleado = f"11{uuid.uuid4().hex[:6]}"

    cliente = crud_cliente.create_cliente(session, ClienteCreate(
        nombre_completo="Test Cliente",
        telefono=telefono_unico,
        email=email_unico
    ))
    empleado = crud_empleado.create_empleado(session, EmpleadoCreate(
        nombre_completo="Test Empleado",
        telefono=telefono_empleado,
        email=email_empleado
    ))
    servicio = crud_servicio.create_servicio(session, ServicioCreate(
        nombre_servicio="Barba",
        duracion=30,
        precio=800
    ))
    return cliente.id_cliente, empleado.id_empleado, servicio.id_servicio


def test_create_turno(session):
    id_cliente, id_empleado, id_servicio = setup_dependencies(session)
    fecha_hora = datetime.now() + timedelta(days=1)

    turno = crud_turno.create_turno(session, TurnoCreate(
        id_cliente=id_cliente,
        id_empleado=id_empleado,
        id_servicio=id_servicio,
        fecha=fecha_hora.date(),
        hora=fecha_hora.time().replace(second=0, microsecond=0),
        estado="pendiente"
    ))
    assert turno.id_turno is not None


def test_turno_solapado_falla(session):
    id_cliente, id_empleado, id_servicio = setup_dependencies(session)
    fecha_hora = datetime.now() + timedelta(days=1)

    crud_turno.create_turno(session, TurnoCreate(
        id_cliente=id_cliente,
        id_empleado=id_empleado,
        id_servicio=id_servicio,
        fecha=fecha_hora.date(),
        hora=fecha_hora.time().replace(second=0, microsecond=0),
        estado="pendiente"
    ))

    with pytest.raises(Exception) as exc_info:
        crud_turno.create_turno(session, TurnoCreate(
            id_cliente=id_cliente,
            id_empleado=id_empleado,
            id_servicio=id_servicio,
            fecha=fecha_hora.date(),
            hora=(fecha_hora + timedelta(minutes=15)).time().replace(second=0, microsecond=0),
            estado="pendiente"
        ))
    assert "solapa" in str(exc_info.value)


def test_turno_pasado_falla(session):
    id_cliente, id_empleado, id_servicio = setup_dependencies(session)
    fecha_hora_pasada = datetime.now() - timedelta(days=1)

    with pytest.raises(Exception) as exc_info:
        crud_turno.create_turno(session, TurnoCreate(
            id_cliente=id_cliente,
            id_empleado=id_empleado,
            id_servicio=id_servicio,
            fecha=fecha_hora_pasada.date(),
            hora=fecha_hora_pasada.time().replace(second=0, microsecond=0),
            estado="pendiente"
        ))
    assert "pasado" in str(exc_info.value)


def test_turno_duracion_invalida_falla(session):
    cliente = crud_cliente.create_cliente(session, ClienteCreate(
        nombre_completo="Cliente Prueba",
        telefono=f"15{uuid.uuid4().hex[:6]}",
        email=f"cliente_{uuid.uuid4().hex[:8]}@test.com"
    ))
    empleado = crud_empleado.create_empleado(session, EmpleadoCreate(
        nombre_completo="Empleado Prueba",
        telefono=f"11{uuid.uuid4().hex[:6]}",
        email=f"empleado_{uuid.uuid4().hex[:8]}@test.com"
    ))
    servicio = crud_servicio.create_servicio(session, ServicioCreate(
        nombre_servicio="Corte fallido",
        duracion=0,
        precio=500
    ))
    fecha_hora = datetime.now() + timedelta(days=1)

    with pytest.raises(Exception) as exc_info:
        crud_turno.create_turno(session, TurnoCreate(
            id_cliente=cliente.id_cliente,
            id_empleado=empleado.id_empleado,
            id_servicio=servicio.id_servicio,
            fecha=fecha_hora.date(),
            hora=fecha_hora.time().replace(second=0, microsecond=0),
            estado="pendiente"
        ))
    assert "duración" in str(exc_info.value)


def test_turno_cliente_inexistente_falla(session):
    _, id_empleado, id_servicio = setup_dependencies(session)
    fecha_hora = datetime.now() + timedelta(days=1)

    with pytest.raises(Exception) as exc_info:
        crud_turno.create_turno(session, TurnoCreate(
            id_cliente=9999,
            id_empleado=id_empleado,
            id_servicio=id_servicio,
            fecha=fecha_hora.date(),
            hora=fecha_hora.time().replace(second=0, microsecond=0),
            estado="pendiente"
        ))
    assert "Cliente" in str(exc_info.value)


def test_turno_empleado_inexistente_falla(session):
    id_cliente, _, id_servicio = setup_dependencies(session)
    fecha_hora = datetime.now() + timedelta(days=1)

    with pytest.raises(Exception) as exc_info:
        crud_turno.create_turno(session, TurnoCreate(
            id_cliente=id_cliente,
            id_empleado=9999,
            id_servicio=id_servicio,
            fecha=fecha_hora.date(),
            hora=fecha_hora.time().replace(second=0, microsecond=0),
            estado="pendiente"
        ))
    assert "Empleado" in str(exc_info.value)
