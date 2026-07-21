import requests

from app.config.settings import settings


class WeatherService:

    def __init__(self):

        self.base_url = settings.OPEN_METEO_URL

    # --------------------------------------------------
    # Current Weather
    # --------------------------------------------------

    def get_current_weather(
        self,
        latitude=None,
        longitude=None,
    ):

        if latitude is None:
            latitude = settings.DEFAULT_LATITUDE

        if longitude is None:
            longitude = settings.DEFAULT_LONGITUDE

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": [
                "temperature_2m",
                "relative_humidity_2m",
                "rain",
                "wind_speed_10m",
                "surface_pressure",
            ],
            "timezone": "auto",
        }

        response = requests.get(
            self.base_url,
            params=params,
            timeout=15,
        )

        response.raise_for_status()

        data = response.json()

        current = data["current"]

        return {

            "latitude": latitude,

            "longitude": longitude,

            "temperature": current["temperature_2m"],

            "humidity": current["relative_humidity_2m"],

            "rainfall": current["rain"],

            "wind_speed": current["wind_speed_10m"],

            "pressure": current["surface_pressure"],

            "time": current["time"],

        }


weather_service = WeatherService()