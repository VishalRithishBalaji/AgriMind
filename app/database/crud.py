from sqlalchemy.orm import Session

from app.database.models.user import User
from app.database.models.farmer import Farmer
from app.database.models.farm import Farm
from app.database.models.crop import Crop
from app.database.models.weather import Weather
from app.database.models.soil import Soil

from app.database import schemas


# =====================================================
# USER CRUD
# =====================================================

def create_user(db: Session, user: schemas.UserCreate):

    db_user = User(
        username=user.username,
        email=user.email,
        password=user.password,
        role=user.role
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user(db: Session, user_id: int):

    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )


def get_user_by_email(db: Session, email: str):

    return (
        db.query(User)
        .filter(User.email == email)
        .first()
    )


def get_users(db: Session):

    return db.query(User).all()


def delete_user(db: Session, user_id: int):

    user = get_user(db, user_id)

    if user:

        db.delete(user)

        db.commit()

    return user


# =====================================================
# FARMER CRUD
# =====================================================

def create_farmer(db: Session, farmer: schemas.FarmerCreate):

    db_farmer = Farmer(**farmer.model_dump())

    db.add(db_farmer)

    db.commit()

    db.refresh(db_farmer)

    return db_farmer


def get_farmer(db: Session, farmer_id: int):

    return (
        db.query(Farmer)
        .filter(Farmer.id == farmer_id)
        .first()
    )


def get_farmers(db: Session):

    return db.query(Farmer).all()


def update_farmer(db: Session,
                  farmer_id: int,
                  farmer: schemas.FarmerCreate):

    db_farmer = get_farmer(db, farmer_id)

    if db_farmer:

        for key, value in farmer.model_dump().items():

            setattr(db_farmer, key, value)

        db.commit()

        db.refresh(db_farmer)

    return db_farmer


def delete_farmer(db: Session,
                  farmer_id: int):

    farmer = get_farmer(db, farmer_id)

    if farmer:

        db.delete(farmer)

        db.commit()

    return farmer


# =====================================================
# FARM CRUD
# =====================================================

def create_farm(db: Session,
                farm: schemas.FarmCreate):

    db_farm = Farm(**farm.model_dump())

    db.add(db_farm)

    db.commit()

    db.refresh(db_farm)

    return db_farm


def get_farm(db: Session,
             farm_id: int):

    return (
        db.query(Farm)
        .filter(Farm.id == farm_id)
        .first()
    )


def get_farms(db: Session):

    return db.query(Farm).all()


def update_farm(db: Session,
                farm_id: int,
                farm: schemas.FarmCreate):

    db_farm = get_farm(db, farm_id)

    if db_farm:

        for key, value in farm.model_dump().items():

            setattr(db_farm, key, value)

        db.commit()

        db.refresh(db_farm)

    return db_farm


def delete_farm(db: Session,
                farm_id: int):

    farm = get_farm(db, farm_id)

    if farm:

        db.delete(farm)

        db.commit()

    return farm


# =====================================================
# CROP CRUD
# =====================================================

def create_crop(db: Session,
                crop: schemas.CropCreate):

    db_crop = Crop(**crop.model_dump())

    db.add(db_crop)

    db.commit()

    db.refresh(db_crop)

    return db_crop


def get_crop(db: Session,
             crop_id: int):

    return (
        db.query(Crop)
        .filter(Crop.id == crop_id)
        .first()
    )


def get_crops(db: Session):

    return db.query(Crop).all()


def update_crop(db: Session,
                crop_id: int,
                crop: schemas.CropCreate):

    db_crop = get_crop(db, crop_id)

    if db_crop:

        for key, value in crop.model_dump().items():

            setattr(db_crop, key, value)

        db.commit()

        db.refresh(db_crop)

    return db_crop


def delete_crop(db: Session,
                crop_id: int):

    crop = get_crop(db, crop_id)

    if crop:

        db.delete(crop)

        db.commit()

    return crop


# =====================================================
# WEATHER CRUD
# =====================================================

def create_weather(db: Session,
                   weather: schemas.WeatherCreate):

    db_weather = Weather(**weather.model_dump())

    db.add(db_weather)

    db.commit()

    db.refresh(db_weather)

    return db_weather


def get_weather(db: Session,
                weather_id: int):

    return (
        db.query(Weather)
        .filter(Weather.id == weather_id)
        .first()
    )


def get_weather_records(db: Session):

    return db.query(Weather).all()


def delete_weather(db: Session,
                   weather_id: int):

    weather = get_weather(db, weather_id)

    if weather:

        db.delete(weather)

        db.commit()

    return weather


# =====================================================
# SOIL CRUD
# =====================================================

def create_soil(db: Session,
                soil: schemas.SoilCreate):

    db_soil = Soil(**soil.model_dump())

    db.add(db_soil)

    db.commit()

    db.refresh(db_soil)

    return db_soil


def get_soil(db: Session,
             soil_id: int):

    return (
        db.query(Soil)
        .filter(Soil.id == soil_id)
        .first()
    )


def get_soil_records(db: Session):

    return db.query(Soil).all()


def delete_soil(db: Session,
                soil_id: int):

    soil = get_soil(db, soil_id)

    if soil:

        db.delete(soil)

        db.commit()

    return soil

from app.database.models.satellite import Satellite
from app.database.models.market import Market
from app.database.models.recommendation import Recommendation
from app.database.models.decision_history import DecisionHistory
from app.database.models.memory_store import MemoryStore
from app.database.models.agent_log import AgentLog


# =====================================================
# SATELLITE CRUD
# =====================================================

def create_satellite(db: Session,
                     satellite: schemas.SatelliteCreate):

    db_satellite = Satellite(**satellite.model_dump())

    db.add(db_satellite)
    db.commit()
    db.refresh(db_satellite)

    return db_satellite


def get_satellite(db: Session,
                  satellite_id: int):

    return (
        db.query(Satellite)
        .filter(Satellite.id == satellite_id)
        .first()
    )


def get_satellite_records(db: Session):

    return db.query(Satellite).all()


def update_satellite(db: Session,
                     satellite_id: int,
                     satellite: schemas.SatelliteCreate):

    db_satellite = get_satellite(db, satellite_id)

    if db_satellite:

        for key, value in satellite.model_dump().items():
            setattr(db_satellite, key, value)

        db.commit()
        db.refresh(db_satellite)

    return db_satellite


def delete_satellite(db: Session,
                     satellite_id: int):

    satellite = get_satellite(db, satellite_id)

    if satellite:
        db.delete(satellite)
        db.commit()

    return satellite


# =====================================================
# MARKET CRUD
# =====================================================

def create_market(db: Session,
                  market: schemas.MarketCreate):

    db_market = Market(**market.model_dump())

    db.add(db_market)
    db.commit()
    db.refresh(db_market)

    return db_market


def get_market(db: Session,
               market_id: int):

    return (
        db.query(Market)
        .filter(Market.id == market_id)
        .first()
    )


def get_market_prices(db: Session):

    return db.query(Market).all()


def update_market(db: Session,
                  market_id: int,
                  market: schemas.MarketCreate):

    db_market = get_market(db, market_id)

    if db_market:

        for key, value in market.model_dump().items():
            setattr(db_market, key, value)

        db.commit()
        db.refresh(db_market)

    return db_market


def delete_market(db: Session,
                  market_id: int):

    market = get_market(db, market_id)

    if market:
        db.delete(market)
        db.commit()

    return market


# =====================================================
# RECOMMENDATION CRUD
# =====================================================

def create_recommendation(db: Session,
                          recommendation: schemas.RecommendationCreate):

    db_recommendation = Recommendation(**recommendation.model_dump())

    db.add(db_recommendation)
    db.commit()
    db.refresh(db_recommendation)

    return db_recommendation


def get_recommendation(db: Session,
                       recommendation_id: int):

    return (
        db.query(Recommendation)
        .filter(Recommendation.id == recommendation_id)
        .first()
    )


def get_recommendations(db: Session):

    return db.query(Recommendation).all()


def update_recommendation(db: Session,
                          recommendation_id: int,
                          recommendation: schemas.RecommendationCreate):

    db_recommendation = get_recommendation(db, recommendation_id)

    if db_recommendation:

        for key, value in recommendation.model_dump().items():
            setattr(db_recommendation, key, value)

        db.commit()
        db.refresh(db_recommendation)

    return db_recommendation


def delete_recommendation(db: Session,
                          recommendation_id: int):

    recommendation = get_recommendation(db, recommendation_id)

    if recommendation:
        db.delete(recommendation)
        db.commit()

    return recommendation


# =====================================================
# DECISION HISTORY CRUD
# =====================================================

def create_decision_history(db: Session,
                            decision: schemas.DecisionHistoryCreate):

    db_decision = DecisionHistory(**decision.model_dump())

    db.add(db_decision)
    db.commit()
    db.refresh(db_decision)

    return db_decision


def get_decision_history(db: Session,
                         decision_id: int):

    return (
        db.query(DecisionHistory)
        .filter(DecisionHistory.id == decision_id)
        .first()
    )


def get_all_decision_history(db: Session):

    return db.query(DecisionHistory).all()


def delete_decision_history(db: Session,
                            decision_id: int):

    decision = get_decision_history(db, decision_id)

    if decision:
        db.delete(decision)
        db.commit()

    return decision


# =====================================================
# MEMORY STORE CRUD
# =====================================================

def create_memory(db: Session,
                  memory: schemas.MemoryStoreCreate):

    db_memory = MemoryStore(**memory.model_dump())

    db.add(db_memory)
    db.commit()
    db.refresh(db_memory)

    return db_memory


def get_memory(db: Session,
               memory_id: int):

    return (
        db.query(MemoryStore)
        .filter(MemoryStore.id == memory_id)
        .first()
    )


def get_memory_by_key(db: Session,
                      key: str):

    return (
        db.query(MemoryStore)
        .filter(MemoryStore.memory_key == key)
        .first()
    )


def get_all_memory(db: Session):

    return db.query(MemoryStore).all()


def update_memory(db: Session,
                  memory_id: int,
                  memory: schemas.MemoryStoreCreate):

    db_memory = get_memory(db, memory_id)

    if db_memory:

        for key, value in memory.model_dump().items():
            setattr(db_memory, key, value)

        db.commit()
        db.refresh(db_memory)

    return db_memory


def delete_memory(db: Session,
                  memory_id: int):

    memory = get_memory(db, memory_id)

    if memory:
        db.delete(memory)
        db.commit()

    return memory


# =====================================================
# AGENT LOG CRUD
# =====================================================

def create_agent_log(db: Session,
                     log: schemas.AgentLogCreate):

    db_log = AgentLog(**log.model_dump())

    db.add(db_log)
    db.commit()
    db.refresh(db_log)

    return db_log


def get_agent_log(db: Session,
                  log_id: int):

    return (
        db.query(AgentLog)
        .filter(AgentLog.id == log_id)
        .first()
    )


def get_agent_logs(db: Session):

    return db.query(AgentLog).all()


def delete_agent_log(db: Session,
                     log_id: int):

    log = get_agent_log(db, log_id)

    if log:
        db.delete(log)
        db.commit()

    return log