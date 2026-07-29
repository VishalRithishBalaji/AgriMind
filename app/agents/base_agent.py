import json
from dataclasses import asdict

from app.models.specialist_output import SpecialistOutput
from app.utils.llm_client import llm_client


class BaseAgent:
    """
    Base class for all LLM-powered specialist agents.
    """

    name = "BaseAgent"

    prompt = ""

    ####################################################################
    # Build Prompt
    ####################################################################

    def build_prompt(self, context):

        context_json = json.dumps(
            context,
            indent=4
        )

        return f"""
{self.prompt}

======================================================

Farm Context

{context_json}

======================================================

Return ONLY valid JSON.
"""

    ####################################################################
    # Parse JSON
    ####################################################################

    def parse(self, response):

        response = response.strip()

        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        start = response.find("{")
        end = response.rfind("}")

        if start == -1 or end == -1:
            raise ValueError("No JSON returned by LLM.")

        response = response[start:end + 1]

        try:
            return json.loads(response)

        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON returned by LLM: {e}")

    ####################################################################
    # Execute
    ####################################################################

    def execute(self, context):

        prompt = self.build_prompt(context)

        raw = llm_client.generate(prompt)

        result = self.parse(raw)

        output = SpecialistOutput(

            agent=self.name,

            status="completed",

            analysis=result.get(
                "analysis",
                ""
            ),

            risks=result.get(
                "risks",
                []
            ),

            opportunities=result.get(
                "opportunities",
                []
            ),

            confidence=result.get(
                "confidence",
                0.0
            ),

            metadata=result.get(
                "metadata",
                {}
            )

        )

        return asdict(output)