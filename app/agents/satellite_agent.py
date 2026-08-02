"""
==========================================================================
AgriMind

Satellite Specialist Agent

Uses dynamic crop profiles for vegetation analysis.

Author : AgriMind Team
==========================================================================
"""

import json

from app.agents.base_agent import BaseAgent
from app.prompts.satellite_prompt import SATELLITE_PROMPT


class SatelliteAgent(BaseAgent):

    """
    Satellite Specialist Agent

    Responsibilities
    ----------------
    1. Analyze vegetation health.
    2. Analyze water stress.
    3. Analyze exposed soil.
    4. Compare satellite indices with crop profile.
    5. Generate satellite assessment.
    """

    name = "SatelliteAgent"

    ####################################################################
    # Build Prompt
    ####################################################################

    def build_prompt(self, context):

        crop_profile = context["crop_profile"]

        satellite = context["satellite"]

        prompt = f"""
{SATELLITE_PROMPT}

============================================================

CROP PROFILE

{json.dumps(crop_profile, indent=4)}

============================================================

CURRENT SATELLITE DATA

{json.dumps(satellite, indent=4)}

============================================================

TASK

Compare the CURRENT SATELLITE INDICES against the
CROP PROFILE.

Use the crop profile vegetation thresholds
instead of generic thresholds.

Evaluate

1. NDVI health.
2. NDWI water stress.
3. SAVI soil exposure.
4. Vegetation condition.
5. Water availability.
6. Irrigation need.
7. Satellite-related risks.
8. Satellite-related opportunities.
9. Overall vegetation assessment.

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

satellite_agent = SatelliteAgent()