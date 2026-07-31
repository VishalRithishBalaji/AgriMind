import json

from app.utils.gemini_client import gemini_client

from app.prompts.recommendation_prompt import (

    RECOMMENDATION_PROMPT

)


class RecommendationAgent:

    name = "RecommendationAgent"

    ############################################################

    def execute(

        self,

        reasoning

    ):

        prompt = f"""

{RECOMMENDATION_PROMPT}

=====================================================

COLLABORATIVE REASONING

Summary

{reasoning.summary}

Consensus

{reasoning.consensus}

Merged Risks

{json.dumps(reasoning.merged_risks, indent=4)}

Merged Opportunities

{json.dumps(reasoning.merged_opportunities, indent=4)}

Conflicts

{json.dumps(reasoning.conflicts, indent=4)}

Confidence

{reasoning.confidence}

=====================================================

Return ONLY JSON.

"""

        raw = gemini_client.generate(

            prompt

        )

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

        raw = raw[start:end+1]

        result = json.loads(raw)

        result["agent"] = self.name

        result["status"] = "completed"

        return result


recommendation_agent = RecommendationAgent()