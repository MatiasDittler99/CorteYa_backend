# Importamos BaseSettings de pydantic_settings para gestionar la configuración basada en variables de entorno
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

# Definimos una clase para manejar la configuración de la aplicación
class Settings(BaseSettings):
    API_KEY: str = Field(default="", alias="API_KEY")  # Valor por defecto: cadena vacía
    BASE_URL: str = Field(default="", alias="BASE_URL")
    DATABASE_URL: str = Field(..., alias="DATABASE_URL")  # Este sigue siendo obligatorio

    # Configuración adicional para indicar que las variables deben cargarse desde un archivo .env
    model_config = SettingsConfigDict(env_file=".env")

# Crea una instancia de Settings, lo que cargará automáticamente las variables definidas en el archivo .env
settings = Settings()
print(settings.DATABASE_URL)