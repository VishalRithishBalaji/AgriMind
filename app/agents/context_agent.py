from app.collectors.data_collector import data_collector


class ContextAgent:

    """
    Context Understanding Agent

    Responsibilities
    ----------------
    1. Collect data from all collectors
    2. Build unified farm context
    3. Identify risks and opportunities
    4. Compute confidence score
    """

    ####################################################################
    # Main API
    ####################################################################

    def analyze(

        self,

        crop="rice",

        location=None,

        latitude=None,

        longitude=None

    ):

        data = data_collector.collect(

            crop=crop,

            latitude=latitude,

            longitude=longitude

        )

        weather = data["weather"]
        soil = data["soil"]
        satellite = data["satellite"]
        market = data["market"]
        historical = data["historical"]

        risks = []
        opportunities = []

        ##################################################################
        # Weather
        ##################################################################

        risks.extend(

            weather["assessment"]["identified_risks"]

        )

        ##################################################################
        # Soil
        ##################################################################

        if soil["assessment"]["soil_health_score"] >= 90:

            opportunities.append(

                "Excellent soil quality"

            )

        ##################################################################
        # Satellite
        ##################################################################

        if satellite["status"] == "success":

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

        ##################################################################
        # Market
        ##################################################################

        if market["assessment"]["trend"] == "Increasing":

            opportunities.append(

                "Market prices increasing"

            )

        ##################################################################
        # Historical
        ##################################################################

        similarity = 100 - (

            historical["similar_cases"]["distances"][0][0] * 100

        )

        ##################################################################
        # Confidence
        ##################################################################

        confidence = (

            weather["confidence"] +

            soil["confidence"] +

            market["confidence"] +

            satellite["confidence"]

        ) / 4

        ##################################################################

        context = {

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

        return context

    ####################################################################
    # Backward Compatibility
    ####################################################################

    def build_context(

        self,

        crop="rice",

        latitude=None,

        longitude=None

    ):

        return self.analyze(

            crop=crop,

            latitude=latitude,

            longitude=longitude

        )


context_agent = ContextAgent()