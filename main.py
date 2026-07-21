from fastapi import FastAPI

from app.config.settings import settings
from app.utils.logger import logger

from app.api import (
    farmer_router,
    farm_router,
    crop_router,
    recommendation_router,
    weather_router,
)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="AgriMind - Dynamic Memory-Augmented Collaborative Multi-Agent Decision Intelligence Framework for Precision Agriculture",
)

# =====================================================
# ROOT ENDPOINT
# =====================================================

@app.get("/")
def root():
    return {
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "status": "Running"
    }


# =====================================================
# REGISTER ROUTERS
# =====================================================

app.include_router(farmer_router)
app.include_router(farm_router)
app.include_router(crop_router)
app.include_router(recommendation_router)
app.include_router(weather_router)


# =====================================================
# STARTUP EVENT
# =====================================================

@app.on_event("startup")
async def startup_event():
    logger.info("==========================================")
    logger.info(f"{settings.PROJECT_NAME} Started")
    logger.info(f"Version : {settings.VERSION}")
    logger.info("==========================================")


# =====================================================
# SHUTDOWN EVENT
# =====================================================

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("AgriMind stopped.")