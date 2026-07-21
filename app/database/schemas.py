from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


# ============================================================
# USER
# ============================================================

class UserBase(BaseModel):
    username: str
    email: str
    role: str = "farmer"


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


# ============================================================
# FARMER
# ============================================================

class FarmerBase(BaseModel):
    name: str
    phone: Optional[str] = None
    village: Optional[str] = None
    district: Optional[str] = None
    state: Optional[str] = None
    farm_size: Optional[float] = None


class FarmerCreate(FarmerBase):
    user_id: int


class FarmerResponse(FarmerBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)


# ============================================================
# FARM
# ============================================================

class FarmBase(BaseModel):
    farm_name: str
    latitude: float
    longitude: float
    total_area: float
    soil_type: str
    irrigation_type: str


class FarmCreate(FarmBase):
    farmer_id: int


class FarmResponse(FarmBase):
    id: int
    farmer_id: int

    model_config = ConfigDict(from_attributes=True)


# ============================================================
# CROP
# ============================================================

class CropBase(BaseModel):
    crop_name: str
    variety: Optional[str] = None
    sowing_date: Optional[date] = None
    expected_harvest_date: Optional[date] = None
    season: Optional[str] = None
    area: Optional[float] = None
    expected_yield: Optional[float] = None


class CropCreate(CropBase):
    farm_id: int


class CropResponse(CropBase):
    id: int
    farm_id: int

    model_config = ConfigDict(from_attributes=True)


# ============================================================
# WEATHER
# ============================================================

class WeatherBase(BaseModel):
    recorded_at: datetime
    temperature: float
    humidity: float
    rainfall: float
    wind_speed: float
    pressure: float


class WeatherCreate(WeatherBase):
    farm_id: int


class WeatherResponse(WeatherBase):
    id: int
    farm_id: int

    model_config = ConfigDict(from_attributes=True)


# ============================================================
# SOIL
# ============================================================

class SoilBase(BaseModel):
    recorded_at: datetime
    ph: float
    nitrogen: float
    phosphorus: float
    potassium: float
    moisture: float
    organic_carbon: float
    soil_texture: str


class SoilCreate(SoilBase):
    farm_id: int


class SoilResponse(SoilBase):
    id: int
    farm_id: int

    model_config = ConfigDict(from_attributes=True)


# ============================================================
# SATELLITE
# ============================================================

class SatelliteBase(BaseModel):
    capture_date: datetime
    ndvi: float
    evi: float
    ndwi: float
    surface_temperature: float
    vegetation_health: float


class SatelliteCreate(SatelliteBase):
    farm_id: int


class SatelliteResponse(SatelliteBase):
    id: int
    farm_id: int

    model_config = ConfigDict(from_attributes=True)


# ============================================================
# MARKET
# ============================================================

class MarketBase(BaseModel):
    crop_name: str
    market_name: str
    district: str
    state: str
    minimum_price: float
    maximum_price: float
    modal_price: float
    recorded_at: datetime


class MarketCreate(MarketBase):
    pass


class MarketResponse(MarketBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


# ============================================================
# RECOMMENDATION
# ============================================================

class RecommendationBase(BaseModel):
    recommendation_type: str
    recommendation: str
    confidence: int
    generated_at: datetime
    agent_name: str


class RecommendationCreate(RecommendationBase):
    farm_id: int


class RecommendationResponse(RecommendationBase):
    id: int
    farm_id: int

    model_config = ConfigDict(from_attributes=True)


# ============================================================
# DECISION HISTORY
# ============================================================

class DecisionHistoryBase(BaseModel):
    decision_type: str
    input_summary: str
    final_decision: str
    confidence: int
    created_at: datetime


class DecisionHistoryCreate(DecisionHistoryBase):
    farm_id: int


class DecisionHistoryResponse(DecisionHistoryBase):
    id: int
    farm_id: int

    model_config = ConfigDict(from_attributes=True)


# ============================================================
# MEMORY STORE
# ============================================================

class MemoryStoreBase(BaseModel):
    memory_type: str
    memory_key: str
    memory_value: str
    embedding_model: str
    source: str
    created_at: datetime
    updated_at: datetime


class MemoryStoreCreate(MemoryStoreBase):
    pass


class MemoryStoreResponse(MemoryStoreBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


# ============================================================
# AGENT LOG
# ============================================================

class AgentLogBase(BaseModel):
    agent_name: str
    task_name: str
    status: str
    execution_time: int
    input_data: str
    output_data: str
    created_at: datetime


class AgentLogCreate(AgentLogBase):
    pass


class AgentLogResponse(AgentLogBase):
    id: int

    model_config = ConfigDict(from_attributes=True)