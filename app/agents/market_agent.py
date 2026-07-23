class MarketAgent:

    """
    Market Specialist Agent
    """

    name = "MarketAgent"

    def execute(self, context):

        return {

            "agent": self.name,

            "status": "completed",

            "summary": {

                "trend":

                    context["market_trend"],

                "opportunities":

                    context["opportunities"]

            }

        }


market_agent = MarketAgent()