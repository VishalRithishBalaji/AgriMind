from app.agents.memory_agent import memory_agent


class HistoricalCollector:

    def collect(
        self,
        crop,
        weather,
        soil,
        market
    ):

        result = memory_agent.retrieve(

            crop=crop,

            weather=weather,

            soil=soil,

            market=market

        )

        return {

            "source": "historical",

            "status": result.get("status"),

            "similar_cases": result["retrieved_cases"],

            "confidence": 100

        }


historical_collector = HistoricalCollector()