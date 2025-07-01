-- Tabla intermedia que representa la relación muchos a muchos entre empleados y especialidades
CREATE TABLE IF NOT EXISTS empleado_especialidad (
  id_empleado INTEGER NOT NULL,                          -- ID del empleado (clave foránea, obligatorio)
  id_especialidad INTEGER NOT NULL,                      -- ID de la especialidad (clave foránea, obligatorio)

  PRIMARY KEY (id_empleado, id_especialidad),            -- Clave primaria compuesta que evita duplicados en la relación

  FOREIGN KEY (id_empleado) REFERENCES Empleado(id_empleado),         -- Relación con la tabla Empleado
  FOREIGN KEY (id_especialidad) REFERENCES Especialidad(id_especialidad) -- Relación con la tabla Especialidad
);
