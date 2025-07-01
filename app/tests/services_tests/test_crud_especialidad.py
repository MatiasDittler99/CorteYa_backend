from app.services import crud_especialidad
from app.schemas.esquema_especialidad import EspecialidadCreate

def test_create_especialidad(session):
    especialidad = crud_especialidad.create_especialidad(session, EspecialidadCreate(
        nombre_completo="Coloración"
    ))
    assert especialidad.id_especialidad is not None
    assert especialidad.nombre_completo == "Coloración"

def test_get_especialidad(session):
    especialidad = crud_especialidad.create_especialidad(session, EspecialidadCreate(
        nombre_completo="Peinado"
    ))
    fetched = crud_especialidad.get_especialidad(session, especialidad.id_especialidad)
    assert fetched is not None
    assert fetched.nombre_completo == "Peinado"

def test_update_especialidad(session):
    especialidad = crud_especialidad.create_especialidad(session, EspecialidadCreate(
        nombre_completo="Antiguo"
    ))
    updated = crud_especialidad.update_especialidad(session, especialidad.id_especialidad, EspecialidadCreate(
        nombre_completo="Actualizado"
    ))
    assert updated.nombre_completo == "Actualizado"

def test_delete_especialidad(session):
    especialidad = crud_especialidad.create_especialidad(session, EspecialidadCreate(
        nombre_completo="Eliminar"
    ))
    eliminado = crud_especialidad.delete_especialidad(session, especialidad.id_especialidad)
    assert eliminado is True
    assert crud_especialidad.get_especialidad(session, especialidad.id_especialidad) is None
