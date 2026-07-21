from app.memory.memory_manager import memory_manager


class MemoryAgent:

    def __init__(self):

        self.agent_name = "memory_agent"

    def retrieve(

        self,

        crop,

        weather,

        soil,

        market

    ):

        results = memory_manager.retrieve(

            crop=crop,

            weather=weather,

            soil=soil,

            market=market,

            top_k=3

        )

        return {

            "agent": self.agent_name,

            "status": "success",

            "retrieved_cases": results

        }


memory_agent = MemoryAgent()