class WeatherAgent:

    """
    Weather Specialist Agent
    """

    name = "WeatherAgent"

    def execute(self, context):

        return {

            "agent": self.name,

            "status": "completed",

            "summary": {

                "weather":

                    context["weather_status"]

            }

        }


weather_agent = WeatherAgent()