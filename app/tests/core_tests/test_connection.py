# Importamos create_engine de SQLModel para manejar la conexión a la base de datos
from sqlmodel import create_engine
# Importamos text de SQLAlchemy para ejecutar consultas SQL en texto puro
from sqlalchemy import text
# Importamos pytest para manejar pruebas automatizadas
import pytest
# Importamos la configuración de la base de datos desde config.py
from app.core.configuracion import settings  

# Crea el motor de la base de datos con la URL definida en settings
engine = create_engine(settings.DATABASE_URL, echo=True)

# Prueba de conexión a la base de datos
def test_connection():
    """Prueba si la base de datos responde correctamente"""
    try:
        # Establece una conexión con la base de datos
        with engine.connect() as connection:
            # Ejecuta una consulta simple para verificar la conexión
            result = connection.execute(text("SELECT 1"))
            # Verifica que la consulta devuelve el valor esperado (1)
            assert result.scalar() == 1  
            print("✅ Conexión a la base de datos exitosa")
    except Exception as e:
        # Si hay un error, pytest marca la prueba como fallida e imprime el error
        pytest.fail(f"❌ Error de conexión: {e}")