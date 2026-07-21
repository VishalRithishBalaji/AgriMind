class RecommendationAgent:

    def generate(
        self,
        crop,
        weather,
        soil,
        market,
        reasoning,
        fusion
    ):

        actions = []

        # --------------------------
        # Weather-based recommendations
        # --------------------------
        weather_risks = weather["assessment"].get("identified_risks", [])

        if any("Rainfall" in risk for risk in weather_risks):
            actions.append("Provide irrigation because rainfall is below the recommended level.")

        if weather["data"]["temperature"] > 35:
            actions.append("Protect crops from heat stress.")

        if weather["data"]["wind_speed"] > 25:
            actions.append("Inspect crops for possible wind damage.")

        # --------------------------
        # Soil-based recommendations
        # --------------------------
        if soil["assessment"]["nitrogen_status"] == "Low":
            actions.append("Apply nitrogen-rich fertilizer.")

        elif soil["assessment"]["nitrogen_status"] == "Moderate":
            actions.append("Apply a moderate dose of nitrogen fertilizer.")

        if soil["assessment"]["organic_carbon_status"] == "Low":
            actions.append("Add compost or organic manure.")

        # --------------------------
        # Market recommendations
        # --------------------------
        trend = market["assessment"]["trend"]

        if trend == "Increasing":
            actions.append("Current market prices are favorable. Consider selling harvested crops.")

        elif trend == "Decreasing":
            actions.append("Delay selling if storage facilities are available.")

        else:
            actions.append("Monitor market prices regularly.")

        # --------------------------
        # Priority
        # --------------------------
        confidence = fusion["overall_confidence"]

        if confidence >= 90:
            priority = "Very High"

        elif confidence >= 80:
            priority = "High"

        elif confidence >= 65:
            priority = "Medium"

        else:
            priority = "Low"

        # --------------------------
        # Expected Outcome
        # --------------------------
        expected_outcome = {

            "crop_health": weather["assessment"]["status"],

            "soil_health_score": soil["assessment"]["soil_health_score"],

            "market_condition": trend,

            "overall_confidence": confidence,

            "decision": fusion["decision"]

        }

        return {

            "agent": "recommendation_agent",

            "status": "success",

            "crop": crop,

            "priority": priority,

            "decision": fusion["decision"],

            "overall_confidence": confidence,

            "actions": actions,

            "llm_analysis": reasoning["analysis"],

            "expected_outcome": expected_outcome

        }


recommendation_agent = RecommendationAgent()