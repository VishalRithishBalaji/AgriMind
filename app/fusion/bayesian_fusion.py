from math import prod


class BayesianFusion:

    def __init__(self):

        self.weights = {
            "weather": 0.25,
            "soil": 0.30,
            "market": 0.20,
            "memory": 0.10,
            "reasoning": 0.15
        }

    def normalize(self, confidence):

        confidence = max(0, min(confidence, 100))
        return confidence / 100

    def memory_confidence(self, memory):

        try:
            distances = memory["retrieved_cases"]["distances"][0]

            if not distances:
                return 0.50

            avg_distance = sum(distances) / len(distances)

            similarity = max(0, 1 - avg_distance)

            return similarity

        except Exception:
            return 0.50

    def reasoning_confidence(self, reasoning):

        if reasoning["status"] == "success":
            return 0.90

        return 0.40

    def fuse(self, weather, soil, market, memory, reasoning):

        weather_p = self.normalize(weather["confidence"])
        soil_p = self.normalize(soil["confidence"])
        market_p = self.normalize(market["confidence"])

        memory_p = self.memory_confidence(memory)

        reasoning_p = self.reasoning_confidence(reasoning)

        weighted_score = (

            weather_p * self.weights["weather"] +

            soil_p * self.weights["soil"] +

            market_p * self.weights["market"] +

            memory_p * self.weights["memory"] +

            reasoning_p * self.weights["reasoning"]

        )

        overall = round(weighted_score * 100, 2)

        if overall >= 90:
            decision = "Highly Recommended"

        elif overall >= 75:
            decision = "Recommended"

        elif overall >= 60:
            decision = "Proceed with Caution"

        else:
            decision = "Not Recommended"

        return {

            "agent": "bayesian_fusion",

            "status": "success",

            "overall_confidence": overall,

            "decision": decision,

            "weights": self.weights,

            "component_scores": {

                "weather": round(weather_p * 100, 2),

                "soil": round(soil_p * 100, 2),

                "market": round(market_p * 100, 2),

                "memory": round(memory_p * 100, 2),

                "reasoning": round(reasoning_p * 100, 2)

            }

        }


bayesian_fusion = BayesianFusion()