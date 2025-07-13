import pytest
from datetime import date
from sqlmodel import Session
from app.services import autenticacion
from app.models.modelo_usuario import Usuario
from app.schemas.esquema_usuario import UsuarioCreate, UsuarioUpdate
from fastapi import HTTPException

def test_crear_usuario_exitoso(session: Session):
    data = UsuarioCreate(
        nombre="Juan",
        apellido="Perez",
        fecha_nacimiento=date(1990, 1, 1),
        email="juan@example.com",
        username="juan123",
        password="password123"
    )
    usuario = autenticacion.crear_usuario(session, data)
    assert usuario.id_usuario is not None
    assert usuario.nombre == "Juan"
    assert usuario.hashed_password != "password123"  # Debe estar hasheada

def test_crear_usuario_duplicado(session: Session):
    data = UsuarioCreate(
        nombre="Juan",
        apellido="Perez",
        fecha_nacimiento=date(1990, 1, 1),
        email="juan@example.com",
        username="juan123",
        password="password123"
    )
    autenticacion.crear_usuario(session, data)
    # Intentar crear otro usuario con mismo username debe fallar
    with pytest.raises(HTTPException) as excinfo:
        autenticacion.crear_usuario(session, data)
    assert excinfo.value.status_code == 400
    assert "Nombre de usuario ya existe" in excinfo.value.detail

def test_autenticar_usuario_exitoso(session: Session):
    data = UsuarioCreate(
        nombre="Ana",
        apellido="Lopez",
        fecha_nacimiento=date(1992, 2, 2),
        email="ana@example.com",
        username="ana456",
        password="secretpass"
    )
    autenticacion.crear_usuario(session, data)

    user = autenticacion.autenticar_usuario(session, "ana456", "secretpass")
    assert user is not None
    assert user.username == "ana456"

def test_autenticar_usuario_falla(session: Session):
    data = UsuarioCreate(
        nombre="Ana",
        apellido="Lopez",
        fecha_nacimiento=date(1992, 2, 2),
        email="ana@example.com",
        username="ana456",
        password="secretpass"
    )
    autenticacion.crear_usuario(session, data)

    # Contraseña incorrecta
    user = autenticacion.autenticar_usuario(session, "ana456", "wrongpass")
    assert user is None

    # Username no existe
    user = autenticacion.autenticar_usuario(session, "noexiste", "secretpass")
    assert user is None

def test_actualizar_usuario(session: Session):
    data = UsuarioCreate(
        nombre="Luis",
        apellido="Martinez",
        fecha_nacimiento=date(1985, 5, 5),
        email="luis@example.com",
        username="luis789",
        password="initpass"
    )
    usuario = autenticacion.crear_usuario(session, data)

    old_hashed_password = usuario.hashed_password  # Guardar hash previo

    update_data = UsuarioUpdate(
        nombre="Luis Alberto",
        email="luis.alberto@example.com",
        password="newpass123"
    )
    usuario_actualizado = autenticacion.actualizar_usuario(usuario, update_data, session)

    assert usuario_actualizado.nombre == "Luis Alberto"
    assert usuario_actualizado.email == "luis.alberto@example.com"
    assert usuario_actualizado.hashed_password != old_hashed_password  # Comparar con hash previo

    # Verificar que se puede autenticar con la nueva contraseña
    user = autenticacion.autenticar_usuario(session, "luis789", "newpass123")
    assert user is not None
    assert user.id_usuario == usuario_actualizado.id_usuario
