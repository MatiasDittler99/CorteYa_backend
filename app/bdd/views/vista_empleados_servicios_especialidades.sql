CREATE VIEW IF NOT EXISTS view_empleados_servicios_especialidades AS
SELECT DISTINCT
    e.id_empleado,
    e.nombre_completo AS empleado,
    esp.nombre_completo AS especialidad,
    s.nombre_servicio AS servicio
FROM turno t
JOIN empleado e ON t.id_empleado = e.id_empleado
JOIN servicio s ON t.id_servicio = s.id_servicio
LEFT JOIN empleado_especialidad ee ON e.id_empleado = ee.id_empleado
LEFT JOIN especialidad esp ON ee.id_especialidad = esp.id_especialidad;
