-- Creacion de índices

-- CLIENTE
CREATE UNIQUE INDEX IF NOT EXISTS idx_cliente_telefono ON cliente(telefono);
CREATE UNIQUE INDEX IF NOT EXISTS idx_cliente_email ON cliente(email);
CREATE INDEX IF NOT EXISTS idx_cliente_nombre ON cliente(nombre_completo);

-- EMPLEADO
CREATE INDEX IF NOT EXISTS idx_empleado_nombre ON empleado(nombre_completo);

-- ESPECIALIDAD
CREATE UNIQUE INDEX IF NOT EXISTS idx_especialidad_nombre ON especialidad(nombre_completo);

-- EMPLEADO_ESPECIALIDAD
CREATE INDEX IF NOT EXISTS idx_empleado_especialidad_empleado ON empleado_especialidad(id_empleado);
CREATE INDEX IF NOT EXISTS idx_empleado_especialidad_especialidad ON empleado_especialidad(id_especialidad);

-- SERVICIO
CREATE INDEX IF NOT EXISTS idx_servicio_nombre ON servicio(nombre_servicio);
CREATE INDEX IF NOT EXISTS idx_servicio_precio ON servicio(precio);

-- TURNO
CREATE INDEX IF NOT EXISTS idx_turno_fecha ON turno(fecha);
CREATE INDEX IF NOT EXISTS idx_turno_estado ON turno(estado);
CREATE INDEX IF NOT EXISTS idx_turno_hora ON turno(hora);

-- Índices por claves foráneas en turno
CREATE INDEX IF NOT EXISTS idx_turno_cliente_id ON turno(id_cliente);
CREATE INDEX IF NOT EXISTS idx_turno_empleado_id ON turno(id_empleado);
CREATE INDEX IF NOT EXISTS idx_turno_servicio_id ON turno(id_servicio);

-- Índices combinados para búsquedas más complejas
CREATE INDEX IF NOT EXISTS idx_turno_fecha_empleado ON turno(fecha, id_empleado);
CREATE INDEX IF NOT EXISTS idx_turno_fecha_cliente ON turno(fecha, id_cliente);
CREATE INDEX IF NOT EXISTS idx_turno_empleado_hora ON turno(id_empleado, hora);

-- ÍNDICE EXTRA: combinación completa clave para validación de solapamiento
CREATE INDEX IF NOT EXISTS idx_turno_fecha_hora_empleado ON turno(id_empleado, fecha, hora);

-- Índice combinado por cliente y estado para filtros frecuentes de historial
CREATE INDEX IF NOT EXISTS idx_turno_cliente_estado ON turno(id_cliente, estado);

-- Índice por fecha y hora (sin empleado) si hacés reportes generales o agenda diaria sin filtro por empleado
CREATE INDEX IF NOT EXISTS idx_turno_fecha_hora ON turno(fecha, hora);

-- Ïndice adicional
CREATE INDEX IF NOT EXISTS idx_esp_empleado ON empleado_especialidad(id_especialidad, id_empleado);
