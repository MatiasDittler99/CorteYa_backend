import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session
from app.main import app
from app.models.modelo_usuario import Usuario
from app.core.base_de_datos import get_session
from app.routers import ruta_autenticacion
from datetime import date
from sqlalchemy.orm.session import make_transient

# Simulamos un usuario autenticado para pruebas
def fake_current_user():
    return Usuario(
        id_usuario=999,
        nombre="Fake",
        apellido="User",
        fecha_nacimiento="1990-01-01",
        email="fakeuser@example.com",
        username="fakeuser",
        hashed_password="fakehashed"
    )

# Reemplazamos get_current_user por el fake
app.dependency_overrides[ruta_autenticacion.get_current_user] = fake_current_user

client = TestClient(app)

@pytest.fixture
def crear_usuario(session: Session):
    def _crear(nombre="Usuario", username="usuario1", email="usuario1@example.com"):
        user = Usuario(
            nombre=nombre,
            apellido="Test",
            fecha_nacimiento=date(1990, 1, 1),
            email=email,
            username=username,
            hashed_password="fakehash"
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    return _crear

def test_obtener_usuarios(client: TestClient, crear_usuario):
    crear_usuario(username="usuario1", email="usuario1@example.com")
    crear_usuario(username="usuario2", email="usuario2@example.com")

    response = client.get("/usuarios/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(u["username"] == "usuario1" for u in data)
    assert any(u["username"] == "usuario2" for u in data)

def test_eliminar_usuario_existente(client: TestClient, crear_usuario, session):
    usuario = crear_usuario(username="eliminarme", email="delete@example.com")
    usuario_id = usuario.id_usuario  # ⚠️ Guardamos el ID antes de eliminar


    response = client.delete(f"/usuarios/{usuario.id_usuario}")
    assert response.status_code == 204

    session.expire_all()  # Forzar recarga
    # Verificar que ya no existe
    eliminado = session.get(Usuario, usuario_id)
    assert eliminado is None

def test_eliminar_usuario_no_existente(client: TestClient):
    response = client.delete("/usuarios/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Usuario no encontrado"
