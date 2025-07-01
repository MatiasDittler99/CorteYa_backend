from faker import Faker
from sqlmodel import Session, select
from datetime import datetime, timedelta, time, date
from random import choice, randint
from app.models.modelo_cliente import Cliente
from app.models.modelo_empleado import Empleado
from app.models.modelo_especialidad import Especialidad
from app.models.modelo_servicio import Servicio
from app.models.modelo_empleado_especialidad import EmpleadoEspecialidad
from app.models.modelo_turno import Turno
from app.core.base_de_datos import engine
from random import sample

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
                telefono=faker.unique.msisdn()[0:10],  # cadena tipo teléfono corta
                email=faker.unique.email()
            )
            session.add(cliente)
            clientes.append(cliente)
        
        # 2. Crear Empleados
        empleados = []
        for _ in range(8):
            empleado = Empleado(
                nombre_completo=faker.name()
            )
            session.add(empleado)
            empleados.append(empleado)
        
        # 3. Crear Especialidades
        especialidades_nombres = [
            "Corte de cabello", "Barba", "Tinte", "Peinado", "Masajes capilares"
        ]
        especialidades = []
        for nombre in especialidades_nombres:
            esp = Especialidad(nombre_completo=nombre)
            session.add(esp)
            especialidades.append(esp)
        
        # 4. Crear Servicios
        servicios = []
        for i in range(len(especialidades_nombres)):
            serv = Servicio(
                nombre_servicio=especialidades_nombres[i] + " básico",
                duracion=30 + 10 * i,  # 30, 40, 50...
                precio=500 + 200 * i
            )
            session.add(serv)
            servicios.append(serv)
        
        session.commit()  # Confirmar hasta acá para que tengan IDs
        
        # 5. Crear relaciones Empleado-Especialidad
        for empleado in empleados:
            # Le asignamos entre 1 y 3 especialidades al azar
            cantidad = randint(1, 3)
            esp_asignadas = sample(especialidades, length=cantidad)
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
        for _ in range(30):
            cliente = choice(clientes)
            empleado = choice(empleados)
            servicio = choice(servicios)
            
            # Fecha aleatoria en próximos 30 días
            fecha_turno = date.today() + timedelta(days=randint(1, 30))
            
            # Hora aleatoria entre 9am y 6pm
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
