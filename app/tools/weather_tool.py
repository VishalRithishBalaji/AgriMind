from app.services.weather_service import weather_service
from app.knowledge.crop_profiles import CROP_PROFILES


class WeatherTool:

    def __init__(self):
        self.tool_name = "weather_tool"

    def analyze(
        self,
        crop="rice",
        latitude=None,
        longitude=None
    ):

        crop = crop.lower()

        if crop not in CROP_PROFILES:
            raise ValueError(f"Unknown crop: {crop}")

        profile = CROP_PROFILES[crop]

        weather = weather_service.get_current_weather(
            latitude,
            longitude
        )

        temperature = weather["temperature"]
        humidity = weather["humidity"]
        rainfall = weather["rainfall"]
        wind = weather["wind_speed"]

        risks = []

        confidence = 100

        # Temperature
        t_min, t_max = profile["temperature"]

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

        # Humidity
        h_min, h_max = profile["humidity"]

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

        # Rainfall
        r_min, r_max = profile["rainfall"]

        if rainfall < r_min:
            risks.append(
                f"Rainfall below optimal ({r_min}-{r_max} mm)"
            )
            confidence -= 8

        elif rainfall > r_max:
            risks.append(
                f"Rainfall above optimal ({r_min}-{r_max} mm)"
            )
            confidence -= 8

        # Wind
        if wind > profile["wind"]:
            risks.append(
                f"Wind speed exceeds {profile['wind']} km/h"
            )
            confidence -= 10

        confidence = max(confidence, 0)

        if confidence >= 90:
            status = "Excellent"
        elif confidence >= 75:
            status = "Good"
        elif confidence >= 60:
            status = "Moderate"
        else:
            status = "Poor"

        return {
            "crop": crop,
            "confidence": confidence,
            "status": status,
            "weather": weather,
            "identified_risks": risks
        }

    def execute(
        self,
        crop="rice",
        latitude=None,
        longitude=None
    ):

        result = self.analyze(
            crop=crop,
            latitude=latitude,
            longitude=longitude
        )

        return {

            "agent": self.tool_name,

            "status": "success",

            "confidence": result["confidence"],

            "data": result["weather"],

            "assessment": {

                "crop": result["crop"],

                "status": result["status"],

                "identified_risks": result["identified_risks"]

            }

        }


weather_tool = WeatherTool()