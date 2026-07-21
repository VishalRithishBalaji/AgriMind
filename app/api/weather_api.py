from fastapi import APIRouter, Query, HTTPException

from app.tools.weather_tool import weather_tool

router = APIRouter(
    prefix="/weather",
    tags=["Weather Tool"]
)


@router.get("/analyze")
def analyze_weather(
    crop: str = Query(..., description="Crop name"),
    latitude: float | None = None,
    longitude: float | None = None
):

    try:

        return weather_tool.execute(
            crop=crop,
            latitude=latitude,
            longitude=longitude
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )