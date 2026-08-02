"""
==========================================================================
AgriMind

Weather Collector

Collects weather information using the dynamic crop profile.

Author : AgriMind Team
==========================================================================
"""

from app.tools.weather_tool import weather_tool


class WeatherCollector:

    """
    Weather Collector

    Responsibilities
    ----------------
    1. Call WeatherTool.
    2. Normalize the response.
    3. Return standardized weather data.
    """

    ####################################################################
    # Collect
    ####################################################################

    def collect(

        self,

        crop_profile,

        latitude=None,

        longitude=None

    ):

        result = weather_tool.execute(

            crop_profile=crop_profile,

            latitude=latitude,

            longitude=longitude

        )

        return {

            "source": "weather",

            "status": result["status"],

            "timestamp": result["data"].get("time"),

            "raw_data": result["data"],

            "assessment": result["assessment"],

            "confidence": result["confidence"]

        }


##########################################################################

weather_collector = WeatherCollector()