-- Mostrar empleados y sus especialidades
SELECT e.nombre_completo AS empleado, es.nombre_completo AS especialidad
FROM empleado_especialidad ee
JOIN empleado e ON ee.id_empleado = e.id_empleado
JOIN especialidad es ON ee.id_especialidad = es.id_especialidad
ORDER BY e.nombre_completo;
