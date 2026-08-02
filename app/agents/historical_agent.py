"""
==========================================================================
AgriMind

Historical Specialist Agent

Uses dynamic crop profiles and historical memory.

Author : AgriMind Team
==========================================================================
"""

import json

from app.agents.base_agent import BaseAgent
from app.prompts.historical_prompt import HISTORICAL_PROMPT


class HistoricalAgent(BaseAgent):

    """
    Historical Specialist Agent

    Responsibilities
    ----------------
    1. Analyze historical farm records.
    2. Compare current conditions with previous seasons.
    3. Identify recurring patterns.
    4. Learn from past successes and failures.
    5. Generate evidence-based recommendations.
    """

    name = "HistoricalAgent"

    prompt = HISTORICAL_PROMPT

    ####################################################################
    # Build Prompt
    ####################################################################

    def build_prompt(self, context):

        crop_profile = context["crop_profile"]

        ############################################################
        # Historical records already collected
        ############################################################

        historical = context["historical"]

        ############################################################

        prompt = f"""
{HISTORICAL_PROMPT}

============================================================

CROP PROFILE

{json.dumps(crop_profile, indent=4)}

============================================================

CURRENT FARM CONTEXT

{json.dumps(context, indent=4)}

============================================================

HISTORICAL DATA

{json.dumps(historical, indent=4)}

============================================================

TASK

Compare the CURRENT FARM CONDITIONS against the
HISTORICAL RECORDS.

Determine

1. Similar historical seasons.
2. Successful farming practices.
3. Failed farming practices.
4. Recurring farming patterns.
5. Historical risks.
6. Historical opportunities.
7. Recommendation based on historical evidence.

If there are no historical records,
explicitly mention it.

Return ONLY valid JSON.

Schema

{{
    "analysis": "",
    "patterns": [],
    "previous_successes": [],
    "previous_failures": [],
    "recommendation": "",
    "confidence": 0.95
}}

"""

        return prompt

    ####################################################################
    # Parse Response
    ####################################################################

    def parse_response(self, response):

        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        start = response.find("{")
        end = response.rfind("}")

        if start == -1 or end == -1:
            raise ValueError("No JSON found in HistoricalAgent response.")

        response = response[start:end + 1]

        result = json.loads(response)

        result["agent"] = self.name
        result["status"] = "completed"

        return result


##########################################################################

historical_agent = HistoricalAgent()