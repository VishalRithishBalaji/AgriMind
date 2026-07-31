import os

from groq import Groq


class GeminiClient:
    """
    Groq Client
    (Keeps class name unchanged to avoid changing imports.)
    """

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError(
                "GROQ_API_KEY not found."
            )

        self.client = Groq(
            api_key=api_key
        )

        self.model = os.getenv(
            "GROQ_MODEL",
            "llama-3.3-70b-versatile"
        )

        print(f"✓ Groq model: {self.model}")

    ##############################################################

    def generate(

        self,

        prompt,

        system_prompt="",

        temperature=0.2

    ):

        response = self.client.chat.completions.create(

            model=self.model,

            temperature=temperature,

            messages=[

                {

                    "role": "system",

                    "content": system_prompt

                },

                {

                    "role": "user",

                    "content": prompt

                }

            ]

        )

        text = response.choices[0].message.content.strip()

        if text.startswith("```"):

            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

        return text


gemini_client = GeminiClient()