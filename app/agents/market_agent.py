from app.agents.base_agent import BaseAgent
from app.prompts.market_prompt import MARKET_PROMPT


class MarketAgent(BaseAgent):
    """
    Market Specialist Agent
    """

    name = "MarketAgent"

    prompt = MARKET_PROMPT


market_agent = MarketAgent()