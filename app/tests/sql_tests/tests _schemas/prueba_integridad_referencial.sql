-- Intentar insertar turno con cliente inexistente
INSERT INTO turno (id_cliente, id_empleado, id_servicio, fecha, hora, estado)
VALUES (9999, 1, 1, '2025-06-01', '10:00', 'pendiente'); -- Cliente 9999 no existe
