from app.services import crud_empleado, crud_especialidad, crud_empleado_especialidad
from app.schemas.esquema_empleado import EmpleadoCreate
from app.schemas.esquema_especialidad import EspecialidadCreate
from app.schemas.esquema_empleado_especialidad import EmpleadoEspecialidadCreate

def crear_dependencias(session):
    empleado = crud_empleado.create_empleado(session, EmpleadoCreate(
        nombre_completo="Empleado Test"
    ))
    especialidad = crud_especialidad.create_especialidad(session, EspecialidadCreate(
        nombre_completo="Corte Fade"
    ))
    return empleado.id_empleado, especialidad.id_especialidad

def test_create_empleado_especialidad(session):
    id_empleado, id_especialidad = crear_dependencias(session)
    rel = crud_empleado_especialidad.create_empleado_especialidad(session, EmpleadoEspecialidadCreate(
        id_empleado=id_empleado,
        id_especialidad=id_especialidad
    ))
    assert rel.id_empleado == id_empleado
    assert rel.id_especialidad == id_especialidad

def test_get_empleado_especialidades(session):
    id_empleado, id_especialidad = crear_dependencias(session)
    crud_empleado_especialidad.create_empleado_especialidad(session, EmpleadoEspecialidadCreate(
        id_empleado=id_empleado,
        id_especialidad=id_especialidad
    ))
    relaciones = crud_empleado_especialidad.get_empleado_especialidades(session)
    assert any(r.id_empleado == id_empleado and r.id_especialidad == id_especialidad for r in relaciones)

def test_delete_empleado_especialidad(session):
    id_empleado, id_especialidad = crear_dependencias(session)
    crud_empleado_especialidad.create_empleado_especialidad(session, EmpleadoEspecialidadCreate(
        id_empleado=id_empleado,
        id_especialidad=id_especialidad
    ))
    eliminado = crud_empleado_especialidad.delete_empleado_especialidad(session, id_empleado, id_especialidad)
    assert eliminado is True
