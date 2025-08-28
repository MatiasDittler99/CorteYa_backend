from faker import Faker
from sqlmodel import Session, select
from datetime import datetime, timedelta, time, date
from random import choice, randint, sample
from app.models.modelo_cliente import Cliente
from app.models.modelo_empleado import Empleado
from app.models.modelo_especialidad import Especialidad
from app.models.modelo_servicio import Servicio
from app.models.modelo_empleado_especialidad import EmpleadoEspecialidad
from app.models.modelo_turno import Turno
from app.core.base_de_datos import engine
from app.models.modelo_usuario import Usuario
from app.services.autenticacion import get_password_hash

faker = Faker()

def seed_db():
    with Session(engine) as session:
        # Evitar duplicar seed si ya hay datos
        existe_cliente = session.exec(select(Cliente)).first()
        if existe_cliente:
            print("Datos ya cargados, saltando seed.")
            return

        # 1. Crear Clientes
        clientes = []
        for _ in range(15):
            cliente = Cliente(
                nombre_completo=faker.name(),
                telefono=faker.unique.msisdn()[0:10],
                email=faker.unique.email()
            )
            session.add(cliente)
            clientes.append(cliente)
        
        # 2. Crear Empleados
        empleados = []
        for _ in range(8):
            empleado = Empleado(nombre_completo=faker.name())
            session.add(empleado)
            empleados.append(empleado)
        
        # 3. Crear Especialidades
        especialidades_nombres = [
            "Corte de cabello", "Barba", "Tinte", "Peinado", "Masajes capilares"
        ]
        especialidades = []
        for nombre in especialidades_nombres:
            existe_esp = session.exec(select(Especialidad).where(Especialidad.nombre_completo == nombre)).first()
            if not existe_esp:
                esp = Especialidad(nombre_completo=nombre)
                session.add(esp)
                session.commit()  # confirmar ID antes de relacionar
                especialidades.append(esp)
            else:
                especialidades.append(existe_esp)
        
        # 4. Crear Servicios
        servicios = []
        for i, nombre in enumerate(especialidades_nombres):
            serv = Servicio(
                nombre_servicio=f"{nombre} básico",
                duracion=30 + 10 * i,
                precio=500 + 200 * i
            )
            session.add(serv)
            servicios.append(serv)
        session.commit()  # confirmar IDs
        
        # 5. Crear relaciones Empleado-Especialidad
        for empleado in empleados:
            cantidad = randint(1, 3)
            esp_asignadas = sample(especialidades, k=cantidad)
            relaciones_existentes = set()
            for esp in esp_asignadas:
                key = (empleado.id_empleado, esp.id_especialidad)
                if key not in relaciones_existentes:
                    relaciones_existentes.add(key)
                    rel = EmpleadoEspecialidad(
                        id_empleado=empleado.id_empleado,
                        id_especialidad=esp.id_especialidad
                    )
                    session.add(rel)
        session.commit()
        
        # 6. Crear Turnos
        estados = ["pendiente", "confirmado", "cancelado"]
        for cliente in clientes:
            # cada cliente tendrá entre 1 y 3 turnos
            for _ in range(randint(1, 3)):
                empleado = choice(empleados)
                servicio = choice(servicios)
                fecha_turno = date.today() + timedelta(days=randint(1, 30))
                hora_turno = time(hour=randint(9, 17), minute=choice([0, 15, 30, 45]))
                turno = Turno(
                    id_cliente=cliente.id_cliente,
                    id_empleado=empleado.id_empleado,
                    id_servicio=servicio.id_servicio,
                    fecha=fecha_turno,
                    hora=hora_turno,
                    estado=choice(estados)
                )
                session.add(turno)
        session.commit()
        print("Seed completo: clientes, empleados, especialidades, servicios, relaciones y turnos.")

def crear_usuario_admin_si_no_existe():
    with Session(engine) as session:
        existe_usuario = session.exec(select(Usuario).where(Usuario.username == "admin")).first()
        if not existe_usuario:
            usuario_inicial = Usuario(
                username="admin",
                email="admin@example.com",
                hashed_password=get_password_hash("admin123"),
                nombre="Admin",
                apellido="Sistema",
                fecha_nacimiento=date(1990, 1, 1),
            )
            session.add(usuario_inicial)
            session.commit()
            print("Usuario inicial creado.")
        else:
            print("Usuario inicial ya existe.")

if __name__ == "__main__":
    seed_db()
    crear_usuario_admin_si_no_existe()
