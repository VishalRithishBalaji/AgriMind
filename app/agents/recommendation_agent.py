"""
==========================================================================
AgriMind

Recommendation Agent

Module 5F

Responsibilities
----------------
1. Consume Executive Decision.
2. Use Crop Profile.
3. Produce executable farm recommendations.
4. Generate action plan.
5. Estimate monitoring strategy.

Author : AgriMind Team
==========================================================================
"""

import json

from app.prompts.recommendation_prompt import RECOMMENDATION_PROMPT
from app.utils.groq_client import groq_client


class RecommendationAgent:

    """
    Final Decision Agent
    """

    name = "RecommendationAgent"

    ####################################################################
    # Execute
    ####################################################################

    def execute(

        self,

        context,

        reasoning,

        executive

    ):

        crop_profile = context["crop_profile"]

        ############################################################
        # Prompt
        ############################################################

        prompt = f"""
{RECOMMENDATION_PROMPT}

================================================================

CROP PROFILE

{json.dumps(crop_profile, indent=4)}

================================================================

CURRENT FARM CONTEXT

{json.dumps(context, indent=4)}

================================================================

COLLABORATIVE REASONING

Summary

{reasoning.summary}

------------------------------------------------------------

Consensus

{reasoning.consensus}

------------------------------------------------------------

Merged Risks

{json.dumps(reasoning.merged_risks, indent=4)}

------------------------------------------------------------

Merged Opportunities

{json.dumps(reasoning.merged_opportunities, indent=4)}

------------------------------------------------------------

Confidence

{reasoning.confidence}

================================================================

EXECUTIVE DECISION

{json.dumps(executive, indent=4)}

================================================================

TASK

The Executive Decision above is the validated farm decision.

Your responsibility is NOT to re-decide.

Your responsibility is to convert that executive decision into an
actionable farm execution plan.

Return ONLY valid JSON.

Schema

{{
    "recommendation":"",
    "priority":"",
    "justification":"",
    "actions":[],
    "expected_outcome":"",
    "monitoring_plan":[],
    "confidence":0.95
}}

"""

        ############################################################
        # LLM
        ############################################################

        raw = groq_client.generate(

            prompt

        )

        ############################################################
        # Clean JSON
        ############################################################

        raw = raw.replace(

            "```json",

            ""

        )

        raw = raw.replace(

            "```",

            ""

        )

        raw = raw.strip()

        start = raw.find("{")
        end = raw.rfind("}")

        if start == -1 or end == -1:

            raise ValueError(

                "RecommendationAgent returned invalid JSON."

            )

        raw = raw[start:end + 1]

        result = json.loads(raw)

        ############################################################
        # Metadata
        ############################################################

        result["agent"] = self.name

        result["status"] = "completed"

        result["executive_decision"] = executive.get(

            "decision",

            ""

        )

        result["executive_priority"] = executive.get(

            "priority",

            ""

        )

        ############################################################

        return result


##########################################################################

recommendation_agent = RecommendationAgent()