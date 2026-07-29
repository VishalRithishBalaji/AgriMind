from app.agents.base_agent import BaseAgent
from app.prompts.weather_prompt import WEATHER_PROMPT


class WeatherAgent(BaseAgent):

    """
    Weather Specialist Agent
    """

    name = "WeatherAgent"

    prompt = WEATHER_PROMPT


weather_agent = WeatherAgent()