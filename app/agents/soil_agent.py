from app.agents.base_agent import BaseAgent
from app.prompts.soil_prompt import SOIL_PROMPT


class SoilAgent(BaseAgent):

    """
    Soil Specialist Agent
    """

    name = "SoilAgent"

    prompt = SOIL_PROMPT


soil_agent = SoilAgent()