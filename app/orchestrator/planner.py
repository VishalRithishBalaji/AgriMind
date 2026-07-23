import json
import requests

from app.config import ai_settings
from app.prompts.planner_prompt import PLANNER_PROMPT


class Planner:

    """
    LLM Planner

    Responsibilities

    1. Build planner prompt

    2. Send prompt to LLM

    3. Return raw LLM output

    Parsing and validation are handled separately.
    """

    def __init__(self):

        self.url = ai_settings.OLLAMA_URL

        self.model = ai_settings.LLM_MODEL

        self.temperature = ai_settings.LLM_TEMPERATURE

        self.timeout = ai_settings.LLM_TIMEOUT

    ####################################################################
    # Build Prompt
    ####################################################################

    def build_prompt(

        self,

        user_query,

        context

    ):

        context_json = json.dumps(

            context,

            indent=4

        )

        prompt = f"""

{PLANNER_PROMPT}

============================================================

USER REQUEST

{user_query}

============================================================

FARM CONTEXT

{context_json}

============================================================

Return ONLY JSON.

"""

        return prompt

    ####################################################################
    # Call Ollama
    ####################################################################

    def call_llm(

        self,

        prompt

    ):

        payload = {

            "model": self.model,

            "messages": [

                {

                    "role": "user",

                    "content": prompt

                }

            ],

            "stream": False,

            "options": {

                "temperature": self.temperature

            }

        }

        response = requests.post(

            self.url,

            json=payload,

            timeout=self.timeout

        )

        response.raise_for_status()

        data = response.json()

        if "message" not in data:

            raise RuntimeError(

                "Ollama returned an invalid response."

            )

        return data["message"]["content"]

    ####################################################################
    # Pretty Print (Debug)
    ####################################################################

    def print_raw_response(

        self,

        response

    ):

        print()

        print("=" * 70)

        print("RAW PLANNER RESPONSE")

        print("=" * 70)

        print()

        print(response)

        print()

    ####################################################################
    # Extract JSON
    ####################################################################

    def extract_json(self, response):

        response = response.strip()

        response = response.replace(

            "```json",

            ""

        )

        response = response.replace(

            "```",

            ""

        )

        response = response.strip()

        start = response.find("{")

        end = response.rfind("}")

        if start == -1 or end == -1:

            raise ValueError(

                "No JSON found."

            )

        response = response[start:end+1]

        return json.loads(response)

    ####################################################################
    # Validate Execution Plan
    ####################################################################

    def validate_plan(self, plan):

        # Accept old schema

        if "execution_plan" not in plan:

            if "agents" in plan:

                plan["execution_plan"] = plan.pop("agents")

        required = [

            "goal",

            "execution_plan",

            "confidence"

        ]

        for field in required:

            if field not in plan:

                raise ValueError(

                    f"Planner output missing '{field}'."

                )

        if not isinstance(plan["execution_plan"], list):

            raise ValueError(

                "execution_plan must be a list."

            )

        for step in plan["execution_plan"]:

            for key in [

                "agent",

                "priority",

                "purpose"

            ]:

                if key not in step:

                    raise ValueError(

                        f"Planner step missing '{key}'."

                    )

        #############################################################
        # Normalize confidence
        #############################################################

        if isinstance(

            plan["confidence"],

            (int, float)

        ):

            if plan["confidence"] > 1:

                plan["confidence"] /= 100

                plan["confidence"] = round(

                    plan["confidence"],

                    2

                )

        #############################################################
        # Always append RecommendationAgent
        #############################################################

        names = [

            step["agent"]

            for step in plan["execution_plan"]

        ]

        if "RecommendationAgent" not in names:

            highest = max(

                step["priority"]

                for step in plan["execution_plan"]

            )

            plan["execution_plan"].append(

                {

                    "agent":

                        "RecommendationAgent",

                    "priority":

                        highest + 1,

                    "purpose":

                        "Generate the final recommendation."

                }

            )

        return plan
    ####################################################################
    # Plan
    ####################################################################

    def plan(

        self,

        user_query,

        context,

        retries=1

    ):

        prompt = self.build_prompt(

            user_query,

            context

        )

        attempt = 0

        while attempt <= retries:

            try:

                raw = self.call_llm(

                    prompt

                )

                self.print_raw_response(raw)

                plan = self.extract_json(raw)

                return self.validate_plan(plan)

            except Exception as e:

                attempt += 1

                print(

                    f"Planner attempt {attempt} failed: {e}"

                )

                if attempt > retries:

                    raise RuntimeError(

                        "Planner could not produce a valid execution plan."

                    )

        raise RuntimeError(

            "Unexpected planner failure."

        )


########################################################################
# Singleton
########################################################################

planner = Planner()