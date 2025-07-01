-- Consulta general de turnos
SELECT t.id_turno, c.nombre_completo AS cliente, e.nombre_completo AS empleado, s.nombre_servicio, t.fecha, t.hora, t.estado
FROM turno t
JOIN cliente c ON t.id_cliente = c.id_cliente
JOIN empleado e ON t.id_empleado = e.id_empleado
JOIN servicio s ON t.id_servicio = s.id_servicio
ORDER BY t.fecha, t.hora;
