import pandas as pd
from math import radians, sin, cos, sqrt, atan2

from app.config.settings import settings


class SoilTool:

    def __init__(self):

        self.df = pd.read_csv("data/soil_data.csv")

    def haversine(self, lat1, lon1, lat2, lon2):

        R = 6371

        dlat = radians(lat2 - lat1)
        dlon = radians(lon2 - lon1)

        a = (
            sin(dlat / 2) ** 2
            + cos(radians(lat1))
            * cos(radians(lat2))
            * sin(dlon / 2) ** 2
        )

        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        return R * c

    def get_soil(
        self,
        latitude=None,
        longitude=None,
    ):

        if latitude is None:
            latitude = settings.DEFAULT_LATITUDE

        if longitude is None:
            longitude = settings.DEFAULT_LONGITUDE

        nearest = None
        min_distance = float("inf")

        for _, row in self.df.iterrows():

            distance = self.haversine(
                latitude,
                longitude,
                row["Latitude"],
                row["Longitude"],
            )

            if distance < min_distance:

                min_distance = distance
                nearest = row

        return {

            "state": nearest["State"],

            "district": nearest["District"],

            "distance_km": round(min_distance, 2),

            "ph": nearest["pH"],

            "nitrogen": nearest["Nitrogen"],

            "organic_carbon": nearest["Organic_Carbon"],

            "sand_percent": nearest["Sand"],

            "clay_percent": nearest["Clay"]

        }
    
    def assess_soil(self, soil):

        score = 100
        risks = []

        # pH assessment
        if 6.0 <= soil["ph"] <= 7.5:
            ph_status = "Optimal"
        elif soil["ph"] < 6.0:
            ph_status = "Acidic"
            score -= 15
            risks.append("Soil is acidic.")
        else:
            ph_status = "Alkaline"
            score -= 15
            risks.append("Soil is alkaline.")

        # Nitrogen assessment
        nitrogen = soil["nitrogen"]

        if nitrogen == "High":
            nitrogen_status = "Good"
        elif nitrogen == "Medium":
            nitrogen_status = "Moderate"
            score -= 5
        else:
            nitrogen_status = "Low"
            score -= 20
            risks.append("Nitrogen deficiency.")

        # Organic carbon assessment
        organic = soil["organic_carbon"]

        if organic == "High":
            carbon_status = "Excellent"
        elif organic == "Medium":
            carbon_status = "Average"
            score -= 5
        else:
            carbon_status = "Low"
            score -= 15
            risks.append("Low organic carbon.")

        return {
            "soil_health_score": max(score, 0),
            "ph_status": ph_status,
            "nitrogen_status": nitrogen_status,
            "organic_carbon_status": carbon_status,
            "risks": risks
        }
    def execute(
        self,
        latitude=None,
        longitude=None,
    ):

        soil = self.get_soil(
            latitude=latitude,
            longitude=longitude,
        )

        assessment = self.assess_soil(soil)

        return {

            "agent": "soil_tool",

            "status": "success",

            "confidence": assessment["soil_health_score"],

            "data": soil,

            "assessment": assessment

        }

soil_tool = SoilTool()