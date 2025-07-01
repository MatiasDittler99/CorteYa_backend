## Mantenimiento de la Base de Datos

Para realizar tareas de mantenimiento de la base de datos, como agregar nuevas tablas, columnas o índices, se pueden crear scripts SQL.

### Ejemplo de script de mantenimiento:

-- Desactivar las claves foráneas para permitir cambios en la estructura
PRAGMA foreign_keys = OFF;

-- Crear una nueva tabla si no existe
CREATE TABLE IF NOT EXISTS nuevo_contenido (
    id_contenido INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descripcion TEXT
);

-- Agregar una columna a una tabla existente
ALTER TABLE contenido ADD COLUMN fecha_publicacion DATETIME;

-- Crear un índice para optimizar las búsquedas
CREATE INDEX IF NOT EXISTS idx_contenido_fecha_publicacion ON contenido(fecha_publicacion);

-- Reactivar las claves foráneas después de los cambios
PRAGMA foreign_keys = ON;

## Mantenimiento de la Base de Datos - Gestor de Turnos

Este script SQL permite realizar tareas de mantenimiento como agregar nuevas tablas, columnas o índices, asegurando integridad referencial y compatibilidad con SQLite3.

-- Desactivar claves foráneas temporalmente para permitir cambios estructurales
PRAGMA foreign_keys = OFF;

-- Crear una nueva tabla si no existe (por ejemplo: historial de turnos cancelados)
CREATE TABLE IF NOT EXISTS historial_cancelaciones (
    id_cancelacion INTEGER PRIMARY KEY AUTOINCREMENT,
    id_turno INTEGER NOT NULL,
    motivo TEXT,
    fecha_cancelacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_turno) REFERENCES turno(id_turno)
);

-- Agregar una columna a una tabla existente (por ejemplo: campo observaciones en turno)
ALTER TABLE turno ADD COLUMN observaciones TEXT;

-- Crear un índice para optimizar búsquedas por fecha y estado en los turnos
CREATE INDEX IF NOT EXISTS idx_turno_fecha_estado ON turno(fecha, estado);

-- Crear un índice para optimizar búsquedas por nombre de empleado
CREATE INDEX IF NOT EXISTS idx_empleado_nombre ON empleado(nombre_completo);

-- Reactivar claves foráneas después de los cambios
PRAGMA foreign_keys = ON;

-- Sugerencias opcionales:
Podémos agregar una tabla bitacora_log si queremos auditar acciones de mantenimiento o cambios críticos.

También podemos crear vistas (CREATE VIEW) para facilitar reportes diarios o semanales.

