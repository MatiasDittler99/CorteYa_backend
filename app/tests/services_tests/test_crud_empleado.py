from app.services import crud_empleado
from app.schemas.esquema_empleado import EmpleadoCreate

def test_create_empleado(session):
    empleado = crud_empleado.create_empleado(session, EmpleadoCreate(
        nombre_completo="Barbero 1"
    ))
    assert empleado.id_empleado is not None
    assert empleado.nombre_completo == "Barbero 1"

def test_get_empleado(session):
    empleado = crud_empleado.create_empleado(session, EmpleadoCreate(
        nombre_completo="Barbero 2"
    ))
    fetched = crud_empleado.get_empleado(session, empleado.id_empleado)
    assert fetched is not None
    assert fetched.nombre_completo == "Barbero 2"

def test_update_empleado(session):
    empleado = crud_empleado.create_empleado(session, EmpleadoCreate(
        nombre_completo="Antiguo Nombre"
    ))
    updated = crud_empleado.update_empleado(session, empleado.id_empleado, EmpleadoCreate(
        nombre_completo="Nuevo Nombre"
    ))
    assert updated.nombre_completo == "Nuevo Nombre"

def test_delete_empleado(session):
    empleado = crud_empleado.create_empleado(session, EmpleadoCreate(
        nombre_completo="Eliminar"
    ))
    eliminado = crud_empleado.delete_empleado(session, empleado.id_empleado)
    assert eliminado is True
    assert crud_empleado.get_empleado(session, empleado.id_empleado) is None
