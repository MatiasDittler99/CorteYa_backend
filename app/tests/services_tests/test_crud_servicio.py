from app.services import crud_servicio
from app.schemas.esquema_servicio import ServicioCreate

def test_create_servicio(session):
    servicio = crud_servicio.create_servicio(session, ServicioCreate(
        nombre_servicio="Corte Clásico",
        duracion=30,
        precio=1500.0
    ))
    assert servicio.id_servicio is not None
    assert servicio.nombre_servicio == "Corte Clásico"
