import pytest
from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient

from app.main import app
from app.core.base_de_datos import get_session  # tu dependencia original
from app.models.modelo_usuario import Usuario
from app.routers.ruta_autenticacion import get_current_user
from datetime import date

# Creamos un engine en memoria SOLO para tests, sin tocar el engine original
engine_test = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

# Esta función reemplaza la original get_session durante los tests
def override_get_session():
    with Session(engine_test) as session:
        yield session

# Sobrescribimos la dependencia de la app para que use la sesión de tests
app.dependency_overrides[get_session] = override_get_session

# Crear todas las tablas en la DB de test ANTES de correr tests
@pytest.fixture(scope="session", autouse=True)
def create_test_db():
    SQLModel.metadata.create_all(engine_test)
    yield

# Fixture para acceder a la sesión si querés tests directos con ORM
@pytest.fixture(name="session")
def session_fixture():
    with Session(engine_test) as session:
        yield session

# Fixture para tests de rutas con TestClient
@pytest.fixture(name="client")
def client_fixture():
    with TestClient(app) as client:
        yield client

# 🧪 Fixture que prepara la DB y la sesión
@pytest.fixture(scope="function", autouse=True)
def async_session():
    SQLModel.metadata.drop_all(engine_test)
    SQLModel.metadata.create_all(engine_test)
    with Session(engine_test) as session:
        yield session

# 🚨 Sobrescribe get_current_user para que las rutas que lo usen no fallen
@pytest.fixture(autouse=True)
def override_current_user_fixture():
    def override_get_current_user():
        return Usuario(
            id_usuario=999,
            nombre="Admin",
            apellido="Test",
            email="admin@test.com",
            username="admin",
            hashed_password="fake",
            fecha_nacimiento=date(1990, 1, 1)
        )
    app.dependency_overrides[get_current_user] = override_get_current_user
    yield
    app.dependency_overrides.pop(get_current_user, None)
