# app/tests/__init__.py
import pytest

@pytest.fixture(scope="session")
def db_connection():
    from app.core.base_de_datos import engine
    with engine.connect() as conn:
        yield conn  # Retorna la conexión para pruebas
