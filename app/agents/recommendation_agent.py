import json

from app.utils.llm_client import llm_client

from app.prompts.recommendation_prompt import RECOMMENDATION_PROMPT


class RecommendationAgent:

    name = "RecommendationAgent"

    def execute(

        self,

        specialist_outputs

    ):

        prompt = f"""

{RECOMMENDATION_PROMPT}

====================================================

SPECIALIST OUTPUTS

{json.dumps(specialist_outputs, indent=4)}

====================================================

Return ONLY JSON.

"""

        raw = llm_client.generate(

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