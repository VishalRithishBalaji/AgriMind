class SoilAgent:

    """
    Soil Specialist Agent
    """

    name = "SoilAgent"

    def execute(self, context):

        return {

            "agent": self.name,

            "status": "completed",

            "summary": {

                "soil_health":

                    context["soil_health"]

            }

        }


soil_agent = SoilAgent()