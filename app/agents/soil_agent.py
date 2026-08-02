"""
==========================================================================
AgriMind

Soil Specialist Agent

Uses dynamic crop profiles.

Author : AgriMind Team
==========================================================================
"""

import json

from app.agents.base_agent import BaseAgent
from app.prompts.soil_prompt import SOIL_PROMPT


class SoilAgent(BaseAgent):

    """
    Soil Specialist Agent

    Responsibilities
    ----------------
    1. Analyze current soil health.
    2. Compare with crop requirements.
    3. Identify nutrient deficiencies.
    4. Recommend soil improvements.
    """

    name = "SoilAgent"

    ####################################################################
    # Build Prompt
    ####################################################################

    def build_prompt(self, context):

        crop_profile = context["crop_profile"]

        soil = context["soil"]

        prompt = f"""
{SOIL_PROMPT}

============================================================

CROP PROFILE

{json.dumps(crop_profile, indent=4)}

============================================================

CURRENT SOIL DATA

{json.dumps(soil, indent=4)}

============================================================

TASK

Compare the CURRENT SOIL CONDITIONS against the
CROP PROFILE.

Evaluate

1. Soil suitability.
2. Soil pH.
3. Nitrogen status.
4. Organic carbon.
5. Soil texture.
6. Soil-related risks.
7. Soil-related opportunities.
8. Overall soil assessment.

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

soil_agent = SoilAgent()