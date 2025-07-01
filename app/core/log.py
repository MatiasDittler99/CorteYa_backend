# Importamos el módulo de logging
import logging

# Configuración básica del logger
logging.basicConfig(
    level=logging.INFO,  # Establece el nivel global de logging (puede ser DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Formato del log
    # Establece los manejadores de logging
    handlers=[
        logging.StreamHandler(),  # Muestra los logs en consola
        logging.FileHandler("app.log")  # También guarda los logs en un archivo
    ]
)

logger = logging.getLogger(__name__)  # Crea un logger para este módulo