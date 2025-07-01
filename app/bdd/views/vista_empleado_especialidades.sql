CREATE VIEW IF NOT EXISTS view_empleados_especialidades AS
SELECT
    e.id_empleado,
    e.nombre_completo AS empleado,
    esp.nombre_completo AS especialidad
FROM empleado e
JOIN empleado_especialidad ee ON e.id_empleado = ee.id_empleado
JOIN especialidad esp ON ee.id_especialidad = esp.id_especialidad;