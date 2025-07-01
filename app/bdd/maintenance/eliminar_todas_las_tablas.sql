-- Activar las claves foráneas para mantener la integridad referencial
PRAGMA foreign_keys = ON;

-- Eliminar tablas relacionadas (tablas intermedias)
DROP TABLE IF EXISTS empleado_especialidad;

-- Eliminar tablas principales en orden de dependencias
DROP TABLE IF EXISTS turno;
DROP TABLE IF EXISTS servicio;
DROP TABLE IF EXISTS especialidad;
DROP TABLE IF EXISTS empleado;
DROP TABLE IF EXISTS cliente;

-- Desactivar las claves foráneas
PRAGMA foreign_keys = OFF;
