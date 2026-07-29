import requests

from app.config import ai_settings


class LLMClient:
    """
    Shared Ollama client used by all specialist agents.
    """

    def __init__(self):

        self.url = ai_settings.OLLAMA_URL

        self.model = ai_settings.LLM_MODEL

        self.temperature = ai_settings.LLM_TEMPERATURE

        self.timeout = ai_settings.LLM_TIMEOUT

    ####################################################################
    # Generate Response
    ####################################################################

    def generate(self, prompt: str):

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

        return data["message"]["content"]


llm_client = LLMClient()