-- Ver definición de cada vista
SELECT sql FROM sqlite_master WHERE type = 'view' AND name = 'view_clientes_servicios';
SELECT sql FROM sqlite_master WHERE type = 'view' AND name = 'view_empleados_especialidades';
SELECT sql FROM sqlite_master WHERE type = 'view' AND name = 'view_empleados_servicios_especialidades';
SELECT sql FROM sqlite_master WHERE type = 'view' AND name = 'view_resumen_turnos_estado';
SELECT sql FROM sqlite_master WHERE type = 'view' AND name = 'view_turnos_detallados';
