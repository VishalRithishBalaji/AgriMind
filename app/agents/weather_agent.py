"""
==========================================================================
AgriMind

Weather Specialist Agent

Uses the dynamic crop profile instead of hardcoded crop logic.

Author : AgriMind Team
==========================================================================
"""

import json

from app.agents.base_agent import BaseAgent
from app.prompts.weather_prompt import WEATHER_PROMPT


class WeatherAgent(BaseAgent):

    """
    Weather Specialist Agent

    Responsibilities
    ----------------
    1. Analyze live weather conditions.
    2. Compare with crop-specific optimal conditions.
    3. Identify weather risks.
    4. Identify weather opportunities.
    """

    name = "WeatherAgent"

    ####################################################################
    # Build Prompt
    ####################################################################

    def build_prompt(self, context):

        crop_profile = context["crop_profile"]

        weather = context["weather"]

        prompt = f"""
{WEATHER_PROMPT}

============================================================

CROP PROFILE

{json.dumps(crop_profile, indent=4)}

============================================================

CURRENT WEATHER

{json.dumps(weather, indent=4)}

============================================================

TASK

Compare the CURRENT WEATHER against the CROP PROFILE.

Determine

1. Whether the current weather is suitable.
2. Weather-related risks.
3. Weather-related opportunities.
4. A concise weather assessment.
5. Confidence score.

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

weather_agent = WeatherAgent()