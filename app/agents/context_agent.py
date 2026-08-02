"""
==========================================================================
AgriMind

Context Understanding Agent

Author : AgriMind Team
==========================================================================
"""


class ContextAgent:

    """
    Builds the unified farm context.
    """

    ####################################################################
    # Build Context
    ####################################################################

    def analyze(self, data):

        weather = data.get("weather", {})
        soil = data.get("soil", {})
        satellite = data.get("satellite", {})
        market = data.get("market", {})
        historical = data.get("historical", {})

        crop_profile = data["metadata"]["crop_profile"]
        crop = crop_profile["crop"]

        ############################################################
        # Risks & Opportunities
        ############################################################

        risks = []

        opportunities = []

        ############################################################
        # Weather
        ############################################################

        weather_assessment = weather.get(

            "assessment",

            {}

        )

        risks.extend(

            weather_assessment.get(

                "identified_risks",

                []

            )

        )

        opportunities.extend(

            weather_assessment.get(

                "opportunities",

                []

            )

        )

        ############################################################
        # Soil
        ############################################################

        soil_assessment = soil.get(

            "assessment",

            {}

        )

        soil_health = soil_assessment.get(

            "soil_health_score",

            0

        )

        if soil_health >= 90:

            opportunities.append(

                "Excellent soil quality"

            )

        risks.extend(

            soil_assessment.get(

                "risks",

                []

            )

        )

        opportunities.extend(

            soil_assessment.get(

                "opportunities",

                []

            )

        )

        ############################################################
        # Satellite
        ############################################################

        vegetation_health = "Unknown"

        if satellite.get("status") == "success":

            vegetation = satellite.get(

                "vegetation",

                {}

            )

            water = satellite.get(

                "water",

                {}

            )

            soil_sat = satellite.get(

                "soil",

                {}

            )

            vegetation_health = vegetation.get(

                "health",

                "Unknown"

            )

            if vegetation_health == "Critical":

                risks.append(

                    "Vegetation health is critical"

                )

            if water.get("stress") == "High":

                risks.append(

                    "High crop water stress"

                )

            if soil_sat.get("exposure") == "High":

                risks.append(

                    "Large exposed soil area"

                )

        else:

            risks.append(

                "Satellite analysis unavailable"

            )

        ############################################################
        # Market
        ############################################################

        market_assessment = market.get(

            "assessment",

            {}

        )

        market_trend = market_assessment.get(

            "trend",

            "Unknown"

        )

        if (

            market.get("status") == "success"

            and

            market_trend == "Increasing"

        ):

            opportunities.append(

                "Market prices increasing"

            )

        risks.extend(

            market_assessment.get(

                "risks",

                []

            )

        )

        opportunities.extend(

            market_assessment.get(

                "opportunities",

                []

            )

        )

        ############################################################
        # Historical
        ############################################################

        records = historical.get(

            "records",

            []

        )

        historical_similarity = historical.get(

            "similarity",

            0.0

        )

        if records:

            opportunities.append(

                f"{len(records)} historical records available"

            )

        else:

            risks.append(

                "No historical records available"

            )

        ############################################################
        # Confidence
        ############################################################

        confidence_scores = []

        for source in [

            weather,

            soil,

            market,

            satellite

        ]:

            if source.get("status") == "success":

                confidence_scores.append(

                    source.get(

                        "confidence",

                        0

                    )

                )

        confidence = (

            sum(confidence_scores) / len(confidence_scores)

            if confidence_scores

            else 0

        )

        ############################################################
        # Final Context
        ############################################################

        return {

            ########################################################
            # Crop
            ########################################################

            "crop": crop,

            "crop_profile": crop_profile,

            ########################################################
            # Location
            ########################################################

            "location": {

                "district":

                    soil.get(

                        "location",

                        {}

                    ).get(

                        "district",

                        "Unknown"

                    ),

                "state":

                    soil.get(

                        "location",

                        {}

                    ).get(

                        "state",

                        "Unknown"

                    )

            },

            ########################################################
            # Raw Sources
            ########################################################

            "weather": weather,

            "soil": soil,

            "satellite": satellite,

            "market": market,

            "historical": historical,

            ########################################################
            # Historical
            ########################################################

            "historical_records":

                len(records),

            "historical_similarity":

                round(

                    historical_similarity,

                    2

                ),

            ########################################################
            # Summary
            ########################################################

            "weather_status":

                weather_assessment.get(

                    "status",

                    "Unknown"

                ),

            "soil_health":

                soil_health,

            "vegetation_health":

                vegetation_health,

            "market_trend":

                market_trend,

            ########################################################
            # Insights
            ########################################################

            "risks":

                list(

                    dict.fromkeys(risks)

                ),

            "opportunities":

                list(

                    dict.fromkeys(opportunities)

                ),

            ########################################################
            # Overall Confidence
            ########################################################

            "confidence":

                round(

                    confidence,

                    2

                )

        }


##########################################################################

context_agent = ContextAgent()