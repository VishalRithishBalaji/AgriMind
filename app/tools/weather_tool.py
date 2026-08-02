"""
==========================================================================
AgriMind

Dynamic Weather Tool

Uses
1. Live Weather API
2. Canonical Crop Profile

Author : AgriMind Team
==========================================================================
"""

from app.services.weather_service import weather_service


class WeatherTool:

    def __init__(self):

        self.tool_name = "weather_tool"

    ####################################################################
    # Analyze Weather
    ####################################################################

    def analyze(

        self,

        crop_profile,

        latitude=None,

        longitude=None

    ):

        ############################################################
        # Live Weather
        ############################################################

        weather = weather_service.get_current_weather(

            latitude,

            longitude

        )

        temperature = weather.get("temperature", 0)

        humidity = weather.get("humidity", 0)

        rainfall = weather.get("rainfall", 0)

        wind = weather.get("wind_speed", 0)

        ############################################################
        # Crop Profile
        ############################################################

        crop = crop_profile["crop"]

        optimal = crop_profile["optimal_conditions"]

        ############################################################
        # Temperature
        ############################################################

        temp = optimal["temperature"]

        t_min = temp["minimum"]

        t_max = temp["maximum"]

        ############################################################
        # Humidity
        ############################################################

        hum = optimal["humidity"]

        h_min = hum["minimum"]

        h_max = hum["maximum"]

        ############################################################
        # Rainfall
        ############################################################

        rain = optimal["rainfall"]

        r_min = rain["minimum"]

        r_max = rain["maximum"]

        ############################################################
        # Wind
        ############################################################

        wind_limit = (

            optimal

            .get(

                "wind_speed",

                {}

            )

            .get(

                "maximum",

                30

            )

        )

        ############################################################

        risks = []

        opportunities = []

        confidence = 100

        ############################################################
        # Temperature
        ############################################################

        if temperature < t_min:

            risks.append(

                f"Temperature below optimal ({t_min}-{t_max}°C)"

            )

            confidence -= 10

        elif temperature > t_max:

            risks.append(

                f"Temperature above optimal ({t_min}-{t_max}°C)"

            )

            confidence -= 10

        else:

            opportunities.append(

                "Temperature is within the optimal range."

            )

        ############################################################
        # Humidity
        ############################################################

        if humidity < h_min:

            risks.append(

                f"Humidity below optimal ({h_min}-{h_max}%)"

            )

            confidence -= 8

        elif humidity > h_max:

            risks.append(

                f"Humidity above optimal ({h_min}-{h_max}%)"

            )

            confidence -= 8

        else:

            opportunities.append(

                "Humidity is within the optimal range."

            )

        ############################################################
        # Rainfall
        ############################################################

        if rainfall < r_min:

            risks.append(

                f"Rainfall below optimal ({r_min}-{r_max} {rain['unit']})"

            )

            confidence -= 8

        elif rainfall > r_max:

            risks.append(

                f"Rainfall above optimal ({r_min}-{r_max} {rain['unit']})"

            )

            confidence -= 8

        else:

            opportunities.append(

                "Rainfall is within the optimal range."

            )

        ############################################################
        # Wind Speed
        ############################################################

        if wind > wind_limit:

            risks.append(

                f"Wind speed exceeds safe limit ({wind_limit} km/h)"

            )

            confidence -= 10

        else:

            opportunities.append(

                "Wind conditions are suitable."

            )

        ############################################################

        confidence = max(

            confidence,

            0

        )

        ############################################################
        # Weather Status
        ############################################################

        if confidence >= 90:

            status = "Excellent"

        elif confidence >= 75:

            status = "Good"

        elif confidence >= 60:

            status = "Moderate"

        else:

            status = "Poor"

        ############################################################

        return {

            "crop": crop,

            "confidence": confidence,

            "status": status,

            "weather": weather,

            "identified_risks": risks,

            "opportunities": opportunities

        }

        ####################################################################
    # Execute
    ####################################################################

    def execute(

        self,

        crop_profile,

        latitude=None,

        longitude=None

    ):

        result = self.analyze(

            crop_profile=crop_profile,

            latitude=latitude,

            longitude=longitude

        )

        ############################################################
        # Standard Response
        ############################################################

        return {

            "agent": self.tool_name,

            "status": "success",

            "confidence": result["confidence"],

            "data": result["weather"],

            "assessment": {

                "crop": result["crop"],

                "status": result["status"],

                "identified_risks": result["identified_risks"],

                "opportunities": result["opportunities"]

            }

        }


##########################################################################
# Singleton
##########################################################################

weather_tool = WeatherTool()