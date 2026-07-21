from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    """
    Application Configuration
    """

    # ----------------------------
    # PostgreSQL
    # ----------------------------
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", 5432))
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")

    # ----------------------------
    # APIs
    # ----------------------------
    OPEN_METEO_URL = os.getenv("OPEN_METEO_URL")
    SOILGRIDS_URL = os.getenv("SOILGRIDS_URL")
    AGMARKNET_URL = os.getenv("AGMARKNET_URL")

    # ----------------------------
    # Default Location
    # ----------------------------
    DEFAULT_LATITUDE = float(os.getenv("DEFAULT_LATITUDE", "11.0168"))
    DEFAULT_LONGITUDE = float(os.getenv("DEFAULT_LONGITUDE", "76.9558"))

    # ----------------------------
    # Application
    # ----------------------------
    LOG_LEVEL = os.getenv("LOG_LEVEL")
    PROJECT_NAME = os.getenv("PROJECT_NAME")
    VERSION = os.getenv("VERSION")


settings = Settings()