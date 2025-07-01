-- Eliminar vistas de relaciones primero
DROP VIEW IF EXISTS view_empleados_especialidades;
DROP VIEW IF EXISTS view_empleados_servicios_especialidades;

-- Eliminar vistas intermedias
DROP VIEW IF EXISTS view_clientes_servicios;

-- Eliminar vistas principales
DROP VIEW IF EXISTS view_turnos_detallados;
DROP VIEW IF EXISTS view_resumen_turnos_estado;

-- Confirmación de eliminación
SELECT COUNT(*) AS vistas_restantes 
FROM sqlite_master 
WHERE type='view';
