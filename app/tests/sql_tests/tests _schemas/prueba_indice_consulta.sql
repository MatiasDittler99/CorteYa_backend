-- Búsqueda usando índice por fecha y empleado
EXPLAIN QUERY PLAN
SELECT * FROM turno WHERE fecha = '2025-06-18' AND id_empleado = 2;
