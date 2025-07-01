-- Ver plan de ejecución (requiere SQLite con soporte EXPLAIN QUERY PLAN o motores compatibles)
EXPLAIN QUERY PLAN SELECT * FROM view_clientes_servicios WHERE id_cliente = 1;
EXPLAIN QUERY PLAN SELECT * FROM view_turnos_detallados WHERE fecha = '2025-06-01';

-- Puedes hacer EXPLAIN también sobre las otras vistas si usas filtros
EXPLAIN QUERY PLAN SELECT * FROM view_empleados_especialidades WHERE especialidad = 'Peluquería';
