-- Crear el trigger solo si no existe
CREATE TRIGGER IF NOT EXISTS trg_validar_cliente_en_turno

-- Se ejecuta ANTES de insertar un nuevo registro en la tabla 'turno'
BEFORE INSERT ON turno

-- El trigger se aplica a cada fila que se intenta insertar
FOR EACH ROW

BEGIN
  -- Verificamos si el cliente especificado en el nuevo turno (NEW.id_cliente) NO existe
  -- Si no existe, abortamos la inserción con un mensaje de error personalizado
  SELECT
    RAISE(ABORT, 'Error: el cliente no existe')  -- Aborta la operación con un mensaje claro

  -- Condición: solo se ejecuta si el cliente no está en la tabla 'cliente'
  WHERE NOT EXISTS (
    SELECT 1
    FROM cliente
    WHERE id_cliente = NEW.id_cliente  -- Compara con el ID que se está intentando insertar
  );
END;
