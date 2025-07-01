-- Actualizar nombre de cliente
UPDATE cliente
SET nombre_completo = 'Cliente Actualizado'
WHERE id_cliente = 1;

-- Confirmar cambio
SELECT * FROM cliente WHERE id_cliente = 1;
