-- Vista: view_clientes_servicios
SELECT * FROM view_clientes_servicios LIMIT 5;

-- Vista: view_empleados_especialidades
SELECT * FROM view_empleados_especialidades LIMIT 5;

-- Vista: view_empleados_servicios_especialidades
SELECT * FROM view_empleados_servicios_especialidades LIMIT 5;

-- Vista: view_resumen_turnos_estado
SELECT * FROM view_resumen_turnos_estado;

-- Vista: view_turnos_detallados
SELECT * FROM view_turnos_detallados LIMIT 5;

-- Comprobar que 'pendiente' existe en el resumen
SELECT * FROM view_resumen_turnos_estado WHERE estado = 'pendiente';

-- Verificar que un cliente conocido aparece en view_turnos_detallados
SELECT * FROM view_turnos_detallados WHERE cliente = 'Cliente Actualizado';
