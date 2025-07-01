-- Eliminar un servicio (si tiene restricciones referenciales activas en cascada)
DELETE FROM turno WHERE id_servicio = 1;
DELETE FROM servicio WHERE id_servicio = 1;

-- Confirmar
SELECT * FROM turno WHERE id_servicio = 1;
SELECT * FROM servicio WHERE id_servicio = 1;
