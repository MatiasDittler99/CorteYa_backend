# CorteYa Backend

## 🚀 Tecnologías

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLModel](https://sqlmodel.tiangolo.com/)
- [SQLite](https://www.sqlite.org/index.html)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Pytest](https://docs.pytest.org/)

## Instalación y configuracion

1. Clonar repo:
git clone https://github.com/MatiasDittler99/CorteYa_backend.git
cd CorteYa_backend

2. Crear entorno virtual:
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows

3. Instalar dependencias:
pip install -r requirements.txt

4. Crear `.env` basado en `.env.example` o Copiar el archivo .env.example a .env: cp .env.example .env y Editá el .env con la URL de tu base de datos: DATABASE_URL=sqlite:///./corteya.db

5. Iniciar servidor:
uvicorn app.main:app --reload

6. Acceder a http://127.0.0.1:8000/docs para la documentación API

## Tests
pytest

## Migraciones con Alembic

1. Para crear una migración automática:
alembic revision --autogenerate -m "Mensaje de la migración"

2. Para aplicar las migraciones pendientes:
alembic upgrade head

## Endpoints API RESTful
Método	Endpoint	   Descripción	Request Body (si aplica)

Clientes

GET	    /clientes	    Listar todos los clientes	—
GET	    /clientes/{id}	Obtener cliente por ID	—
POST	/clientes	    Crear un cliente	JSON con datos del cliente
PUT	    /clientes/{id}	Actualizar un cliente	JSON con datos actualizados
DELETE	/clientes/{id}	Eliminar un cliente	—

Empleados

GET	    /empleados	    Listar todos los empleados	—
GET	    /empleados/{id}	Obtener empleado por ID	—
POST	/empleados	    Crear un empleado	JSON con datos del empleado
PUT	    /empleados/{id}	Actualizar un empleado	JSON con datos actualizados
DELETE	/empleados/{id}	Eliminar un empleado	—

Especialidades

GET	    /especialidades	        Listar todas las especialidades	—
GET	    /especialidades/{id}	Obtener especialidad por ID	—
POST	/especialidades	        Crear una especialidad	JSON con datos de especialidad
PUT	    /especialidades/{id}	Actualizar una especialidad	JSON con datos actualizados
DELETE	/especialidades/{id}	Eliminar una especialidad	—

Relación Empleado - Especialidad			

GET	    /empleado-especialidades	Listar todas las relaciones	—
POST	/empleado-especialidades	Crear relación entre empleado y especialidad	JSON con id_empleado y id_especialidad
DELETE	/empleado-especialidades	Eliminar relación entre empleado y especialidad	Query params: id_empleado, id_especialidad

Servicios			

GET	    /servicios	    Listar todos los servicios	—
GET	    /servicios/{id}	Obtener servicio por ID	—
POST	/servicios	    Crear un servicio	JSON con datos del servicio
PUT	    /servicios/{id}	Actualizar un servicio	JSON con datos actualizados
DELETE	/servicios/{id}	Eliminar un servicio	—

Turnos			

GET	    /turnos	        Listar todos los turnos	—
GET	    /turnos/{id}	Obtener turno por ID	—
POST	/turnos	        Crear un turno	JSON con datos del turno
PUT	    /turnos/{id}	Actualizar un turno	JSON con datos actualizados
DELETE	/turnos/{id}	Eliminar un turno	—

Nota sobre filtros
El endpoint GET /turnos soporta filtros por query params, por ejemplo:

/turnos?fecha=2025-06-01

/turnos?estado=pendiente

/turnos?cliente_id=3

/turnos?empleado_id=2