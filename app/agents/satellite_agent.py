from app.agents.base_agent import BaseAgent
from app.prompts.satellite_prompt import SATELLITE_PROMPT


class SatelliteAgent(BaseAgent):
    """
    Satellite Specialist Agent
    """

    name = "SatelliteAgent"

    prompt = SATELLITE_PROMPT


satellite_agent = SatelliteAgent()