-- Habilitamos las claves foráneas para asegurar la integridad referencial
PRAGMA foreign_keys = ON;

-- Eliminar los registros de la tabla intermedia que relaciona empleados y especialidades
DELETE FROM empleado_especialidad;

-- Eliminar los registros de la tabla de turnos (depende de cliente, empleado y servicio)
DELETE FROM turno;

-- Eliminar los registros de las tablas principales
DELETE FROM servicio;
DELETE FROM especialidad;
DELETE FROM empleado;
DELETE FROM cliente;

-- Deshabilitamos las claves foráneas
PRAGMA foreign_keys = OFF;
