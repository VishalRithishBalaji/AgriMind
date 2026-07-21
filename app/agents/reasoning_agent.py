import requests

from app.config import ai_settings


class ReasoningAgent:

    def __init__(self):

        # Convert generate endpoint to chat endpoint
        self.url = ai_settings.OLLAMA_URL.replace("/generate", "/chat")
        self.model = ai_settings.LLM_MODEL

    # ----------------------------------------------------
    # Memory Formatting
    # ----------------------------------------------------

    def format_memory(self, memory_docs):

        if not memory_docs:
            return "No similar farming cases available."

        if isinstance(memory_docs, list):

            if len(memory_docs) > 0 and isinstance(memory_docs[0], list):
                docs = memory_docs[0]
            else:
                docs = memory_docs

            output = []

            for i, doc in enumerate(docs[:3], start=1):

                output.append(
                    f"""
Case {i}

{doc.strip()}
"""
                )

            return "\n".join(output)

        return str(memory_docs)

    # ----------------------------------------------------
    # User Prompt
    # ----------------------------------------------------

    def build_user_prompt(
        self,
        weather,
        soil,
        market,
        memory
    ):

        return f"""
Weather Assessment

{weather["assessment"]}

Soil Assessment

{soil["assessment"]}

Market Assessment

{market["assessment"]}

Similar Farming Cases

{memory}
"""

    # ----------------------------------------------------
    # Execute
    # ----------------------------------------------------

    def execute(
        self,
        weather,
        soil,
        market,
        memory
    ):

        print("=" * 70)
        print("Reasoning Agent Started")

        memory_text = self.format_memory(memory)

        user_prompt = self.build_user_prompt(
            weather,
            soil,
            market,
            memory_text
        )

        print(f"Prompt Length : {len(user_prompt)} characters")

        payload = {

            "model": self.model,

            "messages": [

                {
                    "role": "system",
                    "content": """
You are AgriMind's Agricultural Decision Intelligence Agent.

You are NOT a reasoning model.

Never reveal your internal reasoning.

Never explain your thinking.

Never write sentences like:

- First I need to...
- Let me analyze...
- I think...
- My reasoning...
- Step 1...

Return ONLY the final recommendation.

Write exactly using these headings:

## Farming Situation

## Risks

## Irrigation Recommendation

## Fertilizer Recommendation

## Selling Advice

## Final Recommendation

Maximum 250 words.
"""
                },

                {
                    "role": "user",
                    "content": user_prompt
                }

            ],

            "stream": False,

            "think": False,

            "options": {

                "temperature": 0.2,

                "num_predict": 512

            }

        }

        print("Sending request to Ollama Chat API...")

        try:

            response = requests.post(
                self.url,
                json=payload,
                timeout=300
            )

            response.raise_for_status()

            result = response.json()

            print("\n========== RAW CHAT RESPONSE ==========")
            print(result)
            print("=======================================\n")

            analysis = ""

            if "message" in result:

                analysis = result["message"].get(
                    "content",
                    ""
                ).strip()

            elif "response" in result:

                analysis = result["response"].strip()

            elif "content" in result:

                analysis = result["content"].strip()

            if not analysis:

                analysis = "No recommendation generated."

            print("Reasoning Agent Completed")
            print("=" * 70)

            return {

                "agent": "reasoning_agent",

                "status": "success",

                "analysis": analysis

            }

        except requests.exceptions.Timeout:

            return {

                "agent": "reasoning_agent",

                "status": "failed",

                "analysis": "Ollama request timed out."

            }

        except requests.exceptions.RequestException as e:

            return {

                "agent": "reasoning_agent",

                "status": "failed",

                "analysis": f"HTTP Error: {e}"

            }

        except Exception as e:

            return {

                "agent": "reasoning_agent",

                "status": "failed",

                "analysis": str(e)

            }


reasoning_agent = ReasoningAgent()