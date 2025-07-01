CREATE VIEW IF NOT EXISTS view_resumen_turnos_estado AS
SELECT
    estado,
    COUNT(*) AS cantidad_turnos
FROM turno
GROUP BY estado;
