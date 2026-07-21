from app.tools.weather_tool import weather_tool
from app.tools.soil_tool import soil_tool
from app.tools.market_tool import market_tool

from app.agents.memory_agent import memory_agent
from app.agents.reasoning_agent import reasoning_agent
from app.agents.recommendation_agent import recommendation_agent

from app.fusion.bayesian_fusion import bayesian_fusion


class AIOrchestrator:

    def execute(
        self,
        crop="rice",
        latitude=None,
        longitude=None
    ):

        # ---------------------------------
        # Weather Analysis
        # ---------------------------------
        weather = weather_tool.execute(
            crop=crop,
            latitude=latitude,
            longitude=longitude
        )

        # ---------------------------------
        # Soil Analysis
        # ---------------------------------
        soil = soil_tool.execute(
            latitude=latitude,
            longitude=longitude
        )

        district = soil["data"]["district"]

        # ---------------------------------
        # Market Analysis
        # ---------------------------------
        market = market_tool.execute(
            crop=crop,
            district=district
        )

        # ---------------------------------
        # Memory Retrieval
        # ---------------------------------
        memory = memory_agent.retrieve(
            crop=crop,
            weather=f"{weather['data']['temperature']}°C, Humidity {weather['data']['humidity']}%, Rainfall {weather['data']['rainfall']} mm",
            soil=f"pH {soil['data']['ph']}, Nitrogen {soil['data']['nitrogen']}, Organic Carbon {soil['data']['organic_carbon']}",
            market=f"Trend {market['data']['Trend']}, Price {market['data']['Price']}"
        )

        # ---------------------------------
        # LLM Reasoning
        # ---------------------------------
        reasoning = reasoning_agent.execute(
            weather=weather,
            soil=soil,
            market=market,
            memory=memory["retrieved_cases"]["documents"]
        )

        # ---------------------------------
        # Bayesian Decision Fusion
        # ---------------------------------
        fusion = bayesian_fusion.fuse(
            weather=weather,
            soil=soil,
            market=market,
            memory=memory,
            reasoning=reasoning
        )

        # ---------------------------------
        # Final Recommendation
        # ---------------------------------
        recommendation = recommendation_agent.generate(
            crop=crop,
            weather=weather,
            soil=soil,
            market=market,
            reasoning=reasoning,
            fusion=fusion
        )

        # ---------------------------------
        # Final Output
        # ---------------------------------
        return {

            "status": "success",

            "crop": crop,

            "weather": weather,

            "soil": soil,

            "market": market,

            "memory": memory,

            "reasoning": reasoning,

            "fusion": fusion,

            "recommendation": recommendation

        }


orchestrator = AIOrchestrator()