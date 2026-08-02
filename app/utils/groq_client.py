"""
==========================================================================
AgriMind

Groq Client

Central Groq API wrapper used throughout the project.

Author : AgriMind Team
==========================================================================
"""

import os
import time
import logging
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

logger = logging.getLogger(__name__)


class GroqClient:
    """
    Shared Groq Client

    Responsibilities
    ----------------
    1. Connect to Groq
    2. Execute prompts
    3. Retry failed requests
    4. Standardize responses
    """

    ####################################################################
    # Constructor
    ####################################################################

    def __init__(self):

        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:

            raise ValueError(

                "GROQ_API_KEY environment variable not found."

            )

        self.client = Groq(

            api_key=api_key

        )

        ################################################################

        self.model = os.getenv(

            "GROQ_MODEL",

            "llama-3.3-70b-versatile"

        )

        self.temperature = float(

            os.getenv(

                "GROQ_TEMPERATURE",

                0.2

            )

        )

        self.max_tokens = int(

            os.getenv(

                "GROQ_MAX_TOKENS",

                4096

            )

        )

        self.retries = int(

            os.getenv(

                "GROQ_RETRIES",

                3

            )

        )

        logger.info(

            f"Groq model loaded: {self.model}"

        )

    ####################################################################
    # Generate
    ####################################################################

    def generate(

        self,

        prompt: str,

        system_prompt: str = "",

        temperature: float | None = None

    ) -> str:

        if temperature is None:

            temperature = self.temperature

        messages = []

        if system_prompt:

            messages.append(

                {

                    "role": "system",

                    "content": system_prompt

                }

            )

        messages.append(

            {

                "role": "user",

                "content": prompt

            }

        )

        last_exception = None

        ################################################################

        for attempt in range(

            1,

            self.retries + 1

        ):

            try:

                response = self.client.chat.completions.create(

                    model=self.model,

                    messages=messages,

                    temperature=temperature,

                    max_tokens=self.max_tokens

                )

                text = (

                    response

                    .choices[0]

                    .message

                    .content

                )

                return self.clean_response(

                    text

                )

            except Exception as e:

                last_exception = e

                logger.warning(

                    f"Groq attempt {attempt} failed: {e}"

                )

                time.sleep(

                    attempt

                )

        ################################################################

        raise RuntimeError(

            f"Groq failed after {self.retries} retries.\n"

            f"{last_exception}"

        )

    ####################################################################
    # Remove Markdown
    ####################################################################

    @staticmethod
    def clean_response(

        text: str

    ) -> str:

        if text is None:

            return ""

        text = text.strip()

        text = text.replace(

            "```json",

            ""

        )

        text = text.replace(

            "```",

            ""

        )

        return text.strip()

    ####################################################################
    # Ping
    ####################################################################

    def ping(self):

        try:

            self.generate(

                "Reply with OK."

            )

            return True

        except Exception:

            return False


##########################################################################
# Singleton
##########################################################################

groq_client = GroqClient()