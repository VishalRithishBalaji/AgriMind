from app.tools.weather_tool import weather_tool


class WeatherCollector:

    def collect(
        self,
        crop,
        latitude=None,
        longitude=None
    ):

        result = weather_tool.execute(
            crop=crop,
            latitude=latitude,
            longitude=longitude
        )

        return {

            "source": "weather",

            "status": result.get("status"),

            "timestamp": result["data"].get("time"),

            "raw_data": result["data"],

            "assessment": result["assessment"],

            "confidence": result.get("confidence")

        }


weather_collector = WeatherCollector()