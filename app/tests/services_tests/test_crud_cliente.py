from app.services import crud_cliente
from app.schemas.esquema_cliente import ClienteCreate

def test_create_cliente(session):
    cliente_in = ClienteCreate(
        nombre_completo="Juan Pérez",
        telefono="123456789",
        email="juan@example.com"
    )
    cliente = crud_cliente.create_cliente(session, cliente_in)
    assert cliente.id_cliente is not None
    assert cliente.nombre_completo == "Juan Pérez"

def test_get_cliente(session):
    cliente_in = ClienteCreate(
        nombre_completo="María López",
        telefono="987654321",
        email="maria@example.com"
    )
    cliente_creado = crud_cliente.create_cliente(session, cliente_in)
    cliente = crud_cliente.get_cliente(session, cliente_creado.id_cliente)
    assert cliente is not None
    assert cliente.email == "maria@example.com"

def test_update_cliente(session):
    cliente = crud_cliente.create_cliente(session, ClienteCreate(
        nombre_completo="Carlos",
        telefono="111222333",
        email="carlos@example.com"
    ))
    updated = crud_cliente.update_cliente(session, cliente.id_cliente, ClienteCreate(
        nombre_completo="Carlos Actualizado",
        telefono="111222333",
        email="carlosnuevo@example.com"
    ))
    assert updated.nombre_completo == "Carlos Actualizado"
    assert updated.email == "carlosnuevo@example.com"

def test_delete_cliente(session):
    cliente = crud_cliente.create_cliente(session, ClienteCreate(
        nombre_completo="Eliminar",
        telefono="000000000",
        email="delete@example.com"
    ))
    deleted = crud_cliente.delete_cliente(session, cliente.id_cliente)
    assert deleted is True
    assert crud_cliente.get_cliente(session, cliente.id_cliente) is None
