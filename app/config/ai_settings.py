from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

CHROMA_DB_PATH = "./vector_db"

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

WEATHER_AGENT = "Weather Agent"
SOIL_AGENT = "Soil Agent"
SATELLITE_AGENT = "Satellite Agent"
MARKET_AGENT = "Market Agent"
MEMORY_AGENT = "Memory Agent"
RECOMMENDATION_AGENT = "Recommendation Agent"

DEFAULT_CONFIDENCE = 80
OLLAMA_URL = "http://localhost:11434/api/chat"

LLM_MODEL = "qwen3:4b"

LLM_TEMPERATURE = 0.3

LLM_TIMEOUT = 300

##########################################################################
# GOOGLE EARTH ENGINE
##########################################################################

GEE_PROJECT_ID = "agrimind-503213"

##########################################################################
# SENTINEL-2 SETTINGS
##########################################################################

SATELLITE_COLLECTION = "COPERNICUS/S2_SR_HARMONIZED"

SATELLITE_ANALYSIS_DAYS = 30

SATELLITE_BUFFER_METERS = 150

SATELLITE_MAX_CLOUD_PERCENT = 20

##########################################################################
# VEGETATION INDEX THRESHOLDS
##########################################################################

NDVI_EXCELLENT = 0.75
NDVI_HEALTHY = 0.60
NDVI_MODERATE = 0.45
NDVI_POOR = 0.30

##########################################################################
# WATER STRESS
##########################################################################

NDWI_LOW_STRESS = 0.30
NDWI_MODERATE_STRESS = 0.10

##########################################################################
# SOIL EXPOSURE
##########################################################################

SAVI_LOW_EXPOSURE = 0.60
SAVI_MODERATE_EXPOSURE = 0.40

##########################################################################
# DEFAULT LOCATION
##########################################################################

DEFAULT_LATITUDE = 11.0168
DEFAULT_LONGITUDE = 76.9558