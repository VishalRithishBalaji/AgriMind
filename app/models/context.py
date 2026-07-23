from dataclasses import dataclass
from typing import List


@dataclass
class FarmContext:

    crop: str

    location: str

    weather_status: str

    soil_health: str

    vegetation_health: str

    market_trend: str

    historical_similarity: float

    risks: List[str]

    opportunities: List[str]

    confidence: float