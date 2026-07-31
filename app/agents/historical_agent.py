import json

from app.utils.llm_client import llm_client

from app.prompts.historical_prompt import HISTORICAL_PROMPT

from app.collectors.historical_collector import historical_collector


class HistoricalAgent:

    name = "HistoricalAgent"

    ########################################################

    def execute(

        self,

        context

    ):

        crop = context["crop"]

        history = historical_collector.collect(

            crop

        )

        prompt = f"""

{HISTORICAL_PROMPT}

=====================================

Current Context

{json.dumps(context, indent=4)}

=====================================

Historical Records

{json.dumps(history, indent=4)}

=====================================

Return ONLY JSON.

"""

        raw = llm_client.generate(

            prompt

        )

        raw = raw.replace("```json","")

        raw = raw.replace("```","")

        raw = raw.strip()

        start = raw.find("{")

        end = raw.rfind("}")

        raw = raw[start:end+1]

        result = json.loads(raw)

        result["agent"] = self.name

        result["status"] = "completed"

        return result


historical_agent = HistoricalAgent()