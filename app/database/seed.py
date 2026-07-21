from datetime import datetime, date

from app.database.database import SessionLocal

from app.database.models.user import User
from app.database.models.farmer import Farmer
from app.database.models.farm import Farm
from app.database.models.crop import Crop
from app.database.models.weather import Weather
from app.database.models.soil import Soil
from app.database.models.satellite import Satellite
from app.database.models.market import Market
from app.database.models.recommendation import Recommendation
from app.database.models.decision_history import DecisionHistory
from app.database.models.memory_store import MemoryStore
from app.database.models.agent_log import AgentLog


db = SessionLocal()


def seed_database():

    print("Checking existing data...")

    if db.query(User).first():
        print("Database already contains data.")
        return

    print("Seeding database...")

    # ======================================================
    # USER
    # ======================================================

    user = User(
        username="farmer1",
        email="farmer1@agrimind.com",
        password="password123",
        role="farmer"
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    # ======================================================
    # FARMER
    # ======================================================

    farmer = Farmer(
        user_id=user.id,
        name="Ramesh Kumar",
        phone="9876543210",
        village="Karamadai",
        district="Coimbatore",
        state="Tamil Nadu",
        farm_size=12.5
    )

    db.add(farmer)
    db.commit()
    db.refresh(farmer)

    # ======================================================
    # FARM
    # ======================================================

    farm = Farm(
        farmer_id=farmer.id,
        farm_name="North Field",
        latitude=11.0168,
        longitude=76.9558,
        total_area=12.5,
        soil_type="Loamy",
        irrigation_type="Drip"
    )

    db.add(farm)
    db.commit()
    db.refresh(farm)

    # ======================================================
    # CROP
    # ======================================================

    crop = Crop(
        farm_id=farm.id,
        crop_name="Rice",
        variety="ADT-43",
        sowing_date=date(2026, 6, 1),
        expected_harvest_date=date(2026, 10, 5),
        season="Kharif",
        area=10,
        expected_yield=5800
    )

    db.add(crop)

    # ======================================================
    # WEATHER
    # ======================================================

    weather = Weather(
        farm_id=farm.id,
        recorded_at=datetime.now(),
        temperature=31.2,
        humidity=78,
        rainfall=12.5,
        wind_speed=7.3,
        pressure=1012
    )

    db.add(weather)

    # ======================================================
    # SOIL
    # ======================================================

    soil = Soil(
        farm_id=farm.id,
        recorded_at=datetime.now(),
        ph=6.8,
        nitrogen=280,
        phosphorus=24,
        potassium=180,
        moisture=42,
        organic_carbon=0.82,
        soil_texture="Loamy"
    )

    db.add(soil)

    # ======================================================
    # SATELLITE
    # ======================================================

    satellite = Satellite(
        farm_id=farm.id,
        capture_date=datetime.now(),
        ndvi=0.82,
        evi=0.69,
        ndwi=0.42,
        surface_temperature=30.5,
        vegetation_health=91
    )

    db.add(satellite)

    # ======================================================
    # MARKET
    # ======================================================

    market = Market(
        crop_name="Rice",
        market_name="Coimbatore Market",
        district="Coimbatore",
        state="Tamil Nadu",
        minimum_price=2350,
        maximum_price=2580,
        modal_price=2450,
        recorded_at=datetime.now()
    )

    db.add(market)

    # ======================================================
    # RECOMMENDATION
    # ======================================================

    recommendation = Recommendation(
        farm_id=farm.id,
        recommendation_type="Irrigation",
        recommendation="Increase irrigation by 15% during next 5 days.",
        confidence=94,
        generated_at=datetime.now(),
        agent_name="Recommendation Agent"
    )

    db.add(recommendation)

    # ======================================================
    # DECISION HISTORY
    # ======================================================

    decision = DecisionHistory(
        farm_id=farm.id,
        decision_type="Irrigation",
        input_summary="Low rainfall forecast",
        final_decision="Increase irrigation frequency",
        confidence=93,
        created_at=datetime.now()
    )

    db.add(decision)

    # ======================================================
    # MEMORY STORE
    # ======================================================

    memory = MemoryStore(
        memory_type="Weather",
        memory_key="weather_karamadai",
        memory_value="Heavy rainfall expected within 3 days.",
        embedding_model="all-MiniLM-L6-v2",
        source="Open-Meteo",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    db.add(memory)

    # ======================================================
    # AGENT LOG
    # ======================================================

    log = AgentLog(
        agent_name="Weather Agent",
        task_name="Weather Analysis",
        status="Completed",
        execution_time=2,
        input_data="Weather API Response",
        output_data="Rainfall Prediction Generated",
        created_at=datetime.now()
    )

    db.add(log)

    db.commit()

    print("Database seeded successfully!")


if __name__ == "__main__":
    seed_database()