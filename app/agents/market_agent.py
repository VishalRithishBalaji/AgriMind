"""
==========================================================================
AgriMind

Market Specialist Agent

Uses dynamic crop profiles.

Author : AgriMind Team
==========================================================================
"""

import json

from app.agents.base_agent import BaseAgent
from app.prompts.market_prompt import MARKET_PROMPT


class MarketAgent(BaseAgent):

    """
    Market Specialist Agent

    Responsibilities
    ----------------
    1. Analyze current market conditions.
    2. Compare with crop market profile.
    3. Detect selling opportunities.
    4. Detect market risks.
    5. Suggest marketing strategy.
    """

    name = "MarketAgent"

    ####################################################################
    # Build Prompt
    ####################################################################

    def build_prompt(self, context):

        crop_profile = context["crop_profile"]

        market = context["market"]

        prompt = f"""
{MARKET_PROMPT}

============================================================

CROP PROFILE

{json.dumps(crop_profile, indent=4)}

============================================================

CURRENT MARKET DATA

{json.dumps(market, indent=4)}

============================================================

TASK

Compare the CURRENT MARKET CONDITIONS against the
CROP PROFILE.

Evaluate

1. Current market trend.
2. Current selling opportunity.
3. Market risks.
4. Market opportunities.
5. Harvest timing.
6. Whether selling now is recommended.
7. Overall market assessment.

Return ONLY valid JSON.

Schema

{{
    "analysis": "",
    "risks": [],
    "opportunities": [],
    "confidence": 0.95
}}

"""

        return prompt


##########################################################################

market_agent = MarketAgent()