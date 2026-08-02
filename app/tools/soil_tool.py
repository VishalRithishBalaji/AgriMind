"""
==========================================================================
AgriMind

Dynamic Soil Tool

Uses

1. Soil Dataset
2. Canonical Crop Profile

Author : AgriMind Team
==========================================================================
"""

import pandas as pd

from math import radians
from math import sin
from math import cos
from math import sqrt
from math import atan2

from app.config.settings import settings


class SoilTool:

    ####################################################################
    # Constructor
    ####################################################################

    def __init__(self):

        self.df = pd.read_csv(

            "data/soil_data.csv"

        )

    ####################################################################
    # Haversine Distance
    ####################################################################

    def haversine(

        self,

        lat1,

        lon1,

        lat2,

        lon2

    ):

        R = 6371

        dlat = radians(lat2 - lat1)

        dlon = radians(lon2 - lon1)

        a = (

            sin(dlat / 2) ** 2

            +

            cos(radians(lat1))

            *

            cos(radians(lat2))

            *

            sin(dlon / 2) ** 2

        )

        c = 2 * atan2(

            sqrt(a),

            sqrt(1 - a)

        )

        return R * c

    ####################################################################
    # Retrieve Nearest Soil Sample
    ####################################################################

    def get_soil(

        self,

        latitude=None,

        longitude=None

    ):

        if latitude is None:

            latitude = settings.DEFAULT_LATITUDE

        if longitude is None:

            longitude = settings.DEFAULT_LONGITUDE

        nearest = None

        min_distance = float("inf")

        ############################################################

        for _, row in self.df.iterrows():

            distance = self.haversine(

                latitude,

                longitude,

                row["Latitude"],

                row["Longitude"]

            )

            if distance < min_distance:

                min_distance = distance

                nearest = row

        ############################################################

        return {

            "state":

                nearest["State"],

            "district":

                nearest["District"],

            "distance_km":

                round(min_distance, 2),

            "ph":

                float(nearest["pH"]),

            "nitrogen":

                str(nearest["Nitrogen"]).title(),

            "organic_carbon":

                str(nearest["Organic_Carbon"]).title(),

            "sand_percent":

                float(nearest["Sand"]),

            "clay_percent":

                float(nearest["Clay"])

        }

        ####################################################################
    # Dynamic Soil Assessment
    ####################################################################

    def assess_soil(

        self,

        soil,

        crop_profile

    ):

        score = 100

        risks = []

        opportunities = []

        ############################################################
        # Canonical Crop Profile
        ############################################################

        optimal = crop_profile.get(

            "optimal_conditions",

            {}

        )

        soil_profile = crop_profile.get(

            "soil",

            {}

        )

        ############################################################
        # Soil pH
        ############################################################

        ph_cfg = optimal.get(

            "soil_ph",

            {

                "minimum": 6.0,

                "maximum": 7.5

            }

        )

        ph_min = ph_cfg["minimum"]

        ph_max = ph_cfg["maximum"]

        if ph_min <= soil["ph"] <= ph_max:

            ph_status = "Optimal"

            opportunities.append(

                "Soil pH is within the optimal range."

            )

        elif soil["ph"] < ph_min:

            ph_status = "Acidic"

            score -= 15

            risks.append(

                f"Soil pH below optimal ({ph_min}-{ph_max})"

            )

        else:

            ph_status = "Alkaline"

            score -= 15

            risks.append(

                f"Soil pH above optimal ({ph_min}-{ph_max})"

            )

        ############################################################
        # Nitrogen
        ############################################################

        preferred_nitrogen = (

            soil_profile.get(

                "preferred_nitrogen",

                "Medium"

            )

            .strip()

            .title()

        )

        nitrogen = soil["nitrogen"].title()

        if nitrogen == preferred_nitrogen:

            nitrogen_status = "Optimal"

            opportunities.append(

                "Nitrogen level matches crop requirement."

            )

        elif nitrogen == "Medium":

            nitrogen_status = "Moderate"

            score -= 5

            risks.append(

                "Nitrogen level is acceptable but not ideal."

            )

        else:

            nitrogen_status = "Low"

            score -= 20

            risks.append(

                "Nitrogen level is unsuitable."

            )

        ############################################################
        # Organic Carbon
        ############################################################

        preferred_carbon = (

            soil_profile.get(

                "preferred_organic_carbon",

                "High"

            )

            .strip()

            .title()

        )

        carbon = soil["organic_carbon"].title()

        if carbon == preferred_carbon:

            carbon_status = "Optimal"

            opportunities.append(

                "Organic carbon matches crop requirement."

            )

        elif carbon == "Medium":

            carbon_status = "Moderate"

            score -= 5

            risks.append(

                "Organic carbon is acceptable."

            )

        else:

            carbon_status = "Low"

            score -= 15

            risks.append(

                "Organic carbon is below crop requirement."

            )

        ############################################################
        # Soil Texture
        ############################################################

        preferred_texture = [

            t.lower()

            for t in soil_profile.get(

                "preferred_texture",

                []

            )

        ]

        if preferred_texture:

            dominant = (

                "Clay"

                if soil["clay_percent"] >= soil["sand_percent"]

                else "Sand"

            )

            if dominant.lower() in preferred_texture:

                opportunities.append(

                    f"{dominant} texture suits the crop."

                )

            else:

                score -= 5

                risks.append(

                    f"{dominant} texture differs from preferred soil."

                )

        ############################################################

        score = max(

            score,

            0

        )

        ############################################################

        return {

            "soil_health_score": score,

            "ph_status": ph_status,

            "nitrogen_status": nitrogen_status,

            "organic_carbon_status": carbon_status,

            "risks": risks,

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

        ############################################################
        # Retrieve Soil
        ############################################################

        soil = self.get_soil(

            latitude=latitude,

            longitude=longitude

        )

        ############################################################
        # Assess Soil
        ############################################################

        assessment = self.assess_soil(

            soil,

            crop_profile

        )

        ############################################################
        # Standard Response
        ############################################################

        return {

            "agent": "soil_tool",

            "status": "success",

            "confidence": assessment["soil_health_score"],

            "data": soil,

            "assessment": assessment

        }


##########################################################################
# Singleton
##########################################################################

soil_tool = SoilTool()