-- Asegurarse de que estamos trabajando en la base de datos correcta
-- (Si usas ATTACH, ajústalo a tu entorno o archivo físico)
-- ATTACH DATABASE 'gestor_turnos.db' AS gestor;

-- Habilitar claves foráneas para mantener integridad
PRAGMA foreign_keys = ON;

-- Truncar las tablas en orden para evitar violación de claves foráneas
DELETE FROM empleado_especialidad;
DELETE FROM turno;
DELETE FROM servicio;
DELETE FROM especialidad;
DELETE FROM empleado;
DELETE FROM cliente;

-- Restaurar el respaldo (suponiendo que el archivo de respaldo es 'backup.sql')
-- El respaldo debe contener tanto el esquema como los datos
.read backup.sql

-- Asegurar que las claves foráneas siguen activadas
PRAGMA foreign_keys = ON;
