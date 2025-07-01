-- Insertar clientes
INSERT INTO cliente (nombre_completo, telefono, email) VALUES
('Juan Pérez', '1111111111', 'juan@example.com'),
('María Gómez', '2222222222', 'maria@example.com'),
('Carlos Sánchez', '3333333333', 'carlos@example.com');

-- Insertar empleados
INSERT INTO empleado (nombre_completo) VALUES
('Lucía Fernández'),
('Pedro Rodríguez'),
('Ana Torres');

-- Insertar especialidades
INSERT INTO especialidad (nombre_completo) VALUES
('Corte de Cabello'),
('Coloración'),
('Barba'),
('Peinados');

-- Insertar rekacion entre empleados y especialidades
INSERT INTO empleado_especialidad (id_empleado, id_especialidad) VALUES
(1, 1),  -- Lucía hace Corte de Cabello
(1, 2),  -- Lucía también hace Coloración
(2, 1),  -- Pedro hace Corte de Cabello
(2, 3),  -- Pedro también hace Barba
(3, 4);  -- Ana hace Peinados

-- Insertar servicios
INSERT INTO servicio (nombre_servicio, duracion, precio) VALUES
('Corte Clásico', 30, 1500),
('Coloración Completa', 90, 5000),
('Perfilado de Barba', 20, 1000),
('Peinado de Fiesta', 45, 3000);


-- Insertar turnos (test funcionales)
INSERT INTO turno (id_cliente, id_empleado, id_servicio, fecha, hora, estado) VALUES
(1, 1, 1, '2025-06-18', '10:00:00', 'confirmado'),  -- Juan con Lucía por Corte Clásico
(2, 2, 3, '2025-06-18', '11:00:00', 'pendiente'),   -- María con Pedro por Barba
(3, 3, 4, '2025-06-19', '14:30:00', 'cancelado'),   -- Carlos con Ana por Peinado
(1, 1, 2, '2025-06-20', '09:00:00', 'pendiente');   -- Juan con Lucía por Coloración

-- Comentar el que se quiera usar 

-- Confirmar clientes
SELECT * FROM cliente;

-- Confirmar empleados
SELECT * FROM empleado;

-- Confirmar especialidades
SELECT * FROM especialidad;

-- Confirmar relacion entre empleados y especialidades
SELECT 
  e.id_empleado,
  e.nombre_completo AS empleado,
  esp.nombre_completo AS especialidad
FROM empleado_especialidad ee
JOIN empleado e ON ee.id_empleado = e.id_empleado
JOIN especialidad esp ON ee.id_especialidad = esp.id_especialidad;

-- Confirmar servicios
SELECT * FROM servicio;

-- Confirmar turnos agendados
SELECT 
  t.id_turno,
  c.nombre_completo AS cliente,
  e.nombre_completo AS empleado,
  s.nombre_servicio,
  t.fecha,
  t.hora,
  t.estado
FROM turno t
JOIN cliente c ON t.id_cliente = c.id_cliente
JOIN empleado e ON t.id_empleado = e.id_empleado
JOIN servicio s ON t.id_servicio = s.id_servicio;