CREATE VIEW IF NOT EXISTS view_clientes_servicios AS
SELECT DISTINCT
    c.id_cliente,
    c.nombre_completo AS cliente,
    s.id_servicio,
    s.nombre_servicio AS servicio
FROM turno t
JOIN cliente c ON t.id_cliente = c.id_cliente
JOIN servicio s ON t.id_servicio = s.id_servicio;
