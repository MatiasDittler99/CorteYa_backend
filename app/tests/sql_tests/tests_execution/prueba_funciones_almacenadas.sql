-- Simular suma total de precios por cliente (como una función agregada)
SELECT c.nombre_completo, SUM(s.precio) AS total_gastado
FROM turno t
JOIN cliente c ON t.id_cliente = c.id_cliente
JOIN servicio s ON t.id_servicio = s.id_servicio
GROUP BY c.id_cliente;
