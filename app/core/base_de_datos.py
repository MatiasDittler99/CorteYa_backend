# Importamos SQLModel para definir modelos y manejar la base de datos
from sqlmodel import SQLModel, Session, create_engine
# Importamos la configuración desde el módulo settings
from .configuracion import settings  

# Obtenemos la URL de la base de datos desde las variables de entorno
DATABASE_URL = settings.DATABASE_URL  

# Creamos el motor de la base de datos usando la URL configurada
# 'echo=True' permite ver las consultas SQL generadas en la consola (útil para depuración)
engine = create_engine(DATABASE_URL, echo=True)

# Función para inicializar la base de datos creando las tablas definidas en los modelos
def init_db():
    SQLModel.metadata.create_all(engine)

# Función generadora que proporciona una sesión de base de datos y la cierra automáticamente
def get_session():
    with Session(engine) as session:
        yield session  # 'yield' permite que la sesión se use como un generador en dependencias (por ejemplo, en FastAPI)
