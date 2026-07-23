class SatelliteAgent:

    """
    Satellite Specialist Agent
    """

    name = "SatelliteAgent"

    def execute(self, context):

        return {

            "agent": self.name,

            "status": "completed",

            "summary": {

                "vegetation":

                    context["vegetation_health"],

                "risks":

                    context["risks"]

            }

        }


satellite_agent = SatelliteAgent()