class ContextAgent:
    """
    Context Understanding Agent

    Responsibilities
    ----------------
    1. Build unified farm context
    2. Identify risks
    3. Identify opportunities
    4. Compute confidence
    """

    def analyze(self, data):

        weather = data["weather"]
        soil = data["soil"]
        satellite = data["satellite"]
        market = data["market"]
        historical = data["historical"]

        crop = data["metadata"]["crop"]

        risks = []
        opportunities = []

        ############################################################
        # Weather
        ############################################################

        risks.extend(
            weather["assessment"]["identified_risks"]
        )

        ############################################################
        # Soil
        ############################################################

        if soil["assessment"]["soil_health_score"] >= 90:

            opportunities.append(
                "Excellent soil quality"
            )

        ############################################################
        # Satellite
        ############################################################

        if satellite["vegetation"]["health"] == "Critical":
            risks.append(
                "Vegetation health is critical"
            )

        if satellite["water"]["stress"] == "High":
            risks.append(
                "High crop water stress"
            )

        if satellite["soil"]["exposure"] == "High":
            risks.append(
                "Large exposed soil area"
            )

        ############################################################
        # Market
        ############################################################

        if market["assessment"]["trend"] == "Increasing":

            opportunities.append(
                "Market prices increasing"
            )

        ############################################################
        # Historical
        ############################################################

        similarity = 100 - (
            historical["similar_cases"]["distances"][0][0] * 100
        )

        ############################################################

        confidence = (
            weather["confidence"]
            + soil["confidence"]
            + market["confidence"]
            + satellite["confidence"]
        ) / 4

        ############################################################

        return {

            "crop": crop,

            "location": soil["location"]["district"],

            "weather_status":
                weather["assessment"]["status"],

            "soil_health":
                soil["assessment"]["soil_health_score"],

            "vegetation_health":
                satellite["vegetation"]["health"],

            "market_trend":
                market["assessment"]["trend"],

            "historical_similarity":
                round(similarity, 2),

            "risks":
                risks,

            "opportunities":
                opportunities,

            "confidence":
                round(confidence, 2)

        }


context_agent = ContextAgent()