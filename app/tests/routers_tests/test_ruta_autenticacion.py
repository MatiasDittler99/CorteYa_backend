import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session
from app.main import app
from app.core.base_de_datos import get_session
from app.models.modelo_usuario import Usuario
from app.schemas.esquema_usuario import UsuarioCreate, UsuarioLogin, UsuarioUpdate

# Cliente de pruebas
client = TestClient(app)

@pytest.fixture
def user_data():
    return {
        "nombre": "Test",
        "apellido": "User",
        "fecha_nacimiento": "1990-01-01",
        "email": "testuser@example.com",
        "username": "testuser",
        "password": "testpassword123"
    }

def test_signup(user_data):
    response = client.post("/auth/signup", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == user_data["username"]
    assert "id_usuario" in data

def test_signup_usuario_duplicado(user_data):
    # Crear primero
    client.post("/auth/signup", json=user_data)
    # Intentar crear duplicado
    response = client.post("/auth/signup", json=user_data)
    assert response.status_code == 400
    assert response.json()["detail"] == "Nombre de usuario ya existe"

def test_login_y_cookie(user_data):
    # Crear usuario
    client.post("/auth/signup", json=user_data)
    login_data = {"username": user_data["username"], "password": user_data["password"]}
    response = client.post("/auth/login", json=login_data)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == user_data["username"]

    # Verificar que viene cookie session_id httpOnly
    cookies = response.cookies
    assert "session_id" in cookies
    # No hagas return acá

def test_me_y_update(user_data):
    # Crear usuario
    client.post("/auth/signup", json=user_data)
    login_data = {"username": user_data["username"], "password": user_data["password"]}
    login_response = client.post("/auth/login", json=login_data)
    cookies = login_response.cookies

    # Acceso a /me con cookie
    me_response = client.get("/auth/me", cookies={"session_id": cookies["session_id"]})
    assert me_response.status_code == 200
    me_data = me_response.json()
    assert me_data["username"] == user_data["username"]

    # Actualizar nombre y email
    update_data = {"nombre": "NuevoNombre", "email": "nuevo@example.com"}
    update_response = client.put("/auth/me", json=update_data, cookies={"session_id": cookies["session_id"]})
    assert update_response.status_code == 200
    updated_user = update_response.json()
    assert updated_user["nombre"] == "NuevoNombre"
    assert updated_user["email"] == "nuevo@example.com"

def test_logout(user_data):
    # Crear usuario y login
    client.post("/auth/signup", json=user_data)
    login_data = {"username": user_data["username"], "password": user_data["password"]}
    login_response = client.post("/auth/login", json=login_data)
    cookies = login_response.cookies

    # Logout
    logout_response = client.post("/auth/logout", cookies={"session_id": cookies["session_id"]})
    assert logout_response.status_code == 200
    assert logout_response.json()["msg"] == "Sesión cerrada"

    # Acceso a /me tras logout falla
    me_response = client.get("/auth/me", cookies={"session_id": cookies["session_id"]})
    assert me_response.status_code == 401
    assert me_response.json()["detail"] == "No autenticado"

