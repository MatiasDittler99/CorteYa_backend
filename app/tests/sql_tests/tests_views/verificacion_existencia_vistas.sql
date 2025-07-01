-- Verificar que todas las vistas existen
SELECT name FROM sqlite_master WHERE type = 'view' AND name IN (
  'view_clientes_servicios',
  'view_empleados_especialidades',
  'view_empleados_servicios_especialidades',
  'view_resumen_turnos_estado',
  'view_turnos_detallados'
);

-- Verificar estructura de una vista
PRAGMA table_info(view_turnos_detallados);
