#!/bin/bash

# Ruta a la base de datos
DB="corteya.db"

# Ruta al archivo de respaldo
BACKUP="backup.sql"

# Asegurar que el archivo de backup existe
if [ ! -f "$BACKUP" ]; then
  echo "❌ Archivo de respaldo '$BACKUP' no encontrado."
  exit 1
fi

# Activar claves foráneas en SQLite (recomendado)
sqlite3 $DB "PRAGMA foreign_keys = ON;"

echo "🧹 Eliminando registros existentes..."

# Eliminar registros respetando el orden de claves foráneas
sqlite3 $DB <<EOF
DELETE FROM empleado_especialidad;
DELETE FROM turno;
DELETE FROM servicio;
DELETE FROM especialidad;
DELETE FROM empleado;
DELETE FROM cliente;
EOF

echo "✅ Registros eliminados."

echo "🔁 Restaurando desde backup '$BACKUP'..."
sqlite3 $DB < $BACKUP

echo "✅ Restauración completa."

# Confirmar que las claves foráneas siguen activadas
sqlite3 $DB "PRAGMA foreign_keys = ON;"

# Cómo usarlo:

# 1.Guardá el archivo como restore.sh

# 2.Dale permisos de ejecución:

# chmod +x backup.sh

# 3.Asegurate de tener gestor_turnos.db y backup.sql en el mismo directorio.

# 4.Ejecutalo:
# ./backup.sh