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