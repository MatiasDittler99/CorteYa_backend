-- Tabla que almacena información de los clientes
CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,     -- Identificador único del cliente (clave primaria autoincremental)
    nombre_completo TEXT NOT NULL,                    -- Nombre completo del cliente (campo obligatorio)
    telefono TEXT NOT NULL UNIQUE,                    -- Teléfono del cliente (único y obligatorio)
    email TEXT NOT NULL UNIQUE                        -- Correo electrónico del cliente (único y obligatorio)
);

-- Tabla que almacena información de los empleados
CREATE TABLE IF NOT EXISTS empleado (
    id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,    -- Identificador único del empleado (clave primaria autoincremental)
    nombre_completo TEXT NOT NULL                     -- Nombre completo del empleado (campo obligatorio)
);

-- Tabla que almacena las especialidades que puede tener un empleado
CREATE TABLE IF NOT EXISTS especialidad (
  id_especialidad INTEGER PRIMARY KEY AUTOINCREMENT,  -- Identificador único de la especialidad
  nombre_completo TEXT NOT NULL UNIQUE                -- Nombre de la especialidad (único y obligatorio)
);

-- Tabla que representa los servicios ofrecidos por la peluquería/barbería
CREATE TABLE IF NOT EXISTS servicio (
    id_servicio INTEGER PRIMARY KEY AUTOINCREMENT,    -- Identificador único del servicio
    nombre_servicio TEXT NOT NULL,                    -- Nombre del servicio (obligatorio)
    duracion INTEGER NOT NULL,                        -- Duración del servicio en minutos (obligatorio)
    precio REAL NOT NULL                              -- Precio del servicio (obligatorio)
);

-- Tabla que representa los turnos agendados
CREATE TABLE IF NOT EXISTS turno (
    id_turno INTEGER PRIMARY KEY AUTOINCREMENT,       -- Identificador único del turno
    id_cliente INTEGER NOT NULL,                      -- Clave foránea al cliente que reservó el turno
    id_empleado INTEGER NOT NULL,                     -- Clave foránea al empleado asignado
    id_servicio INTEGER NOT NULL,                     -- Clave foránea al servicio solicitado
    fecha DATE NOT NULL,                              -- Fecha del turno (obligatorio)
    hora TIME NOT NULL,                               -- Hora del turno (obligatorio)
    estado TEXT CHECK(estado IN ('pendiente', 'confirmado', 'cancelado')) NOT NULL,  
                                                      -- Estado del turno (solo puede ser 'pendiente', 'confirmado' o 'cancelado')
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente),      -- Relación con cliente
    FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado),  -- Relación con empleado
    FOREIGN KEY (id_servicio) REFERENCES Servicio(id_servicio)   -- Relación con servicio
);
