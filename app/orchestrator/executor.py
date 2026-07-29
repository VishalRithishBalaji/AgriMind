import time

from app.orchestrator.registry import AGENT_REGISTRY


class Executor:
    """
    Dynamic Agent Executor

    Responsibilities

    1. Execute planner output
    2. Execute specialist agents
    3. Collect SpecialistOutputs
    4. Execute RecommendationAgent
    5. Return unified execution result
    """

    def __init__(self):
        self.registry = AGENT_REGISTRY

    ####################################################################
    # Sort Execution Plan
    ####################################################################

    def sort_plan(self, execution_plan):

        return sorted(
            execution_plan,
            key=lambda x: x["priority"]
        )

    ####################################################################
    # Execute One Agent
    ####################################################################

    def execute_agent(
        self,
        step,
        context
    ):

        agent_name = step["agent"]

        if agent_name not in self.registry:
            raise ValueError(
                f"Unknown agent '{agent_name}'."
            )

        agent = self.registry[agent_name]

        print()
        print("-" * 60)
        print(f"Executing {agent_name}")
        print("-" * 60)

        return agent.execute(context)

    ####################################################################
    # Execute Complete Plan
    ####################################################################

    def execute(
        self,
        plan,
        context
    ):

        start = time.time()

        ordered_plan = self.sort_plan(
            plan["execution_plan"]
        )

        specialist_outputs = {}

        recommendation = None

        ############################################################
        # Execute specialist agents
        ############################################################

        for step in ordered_plan:

            agent_name = step["agent"]

            if agent_name == "RecommendationAgent":
                continue

            try:

                output = self.execute_agent(
                    step,
                    context
                )

            except Exception as e:

                output = {
                    "agent": agent_name,
                    "status": "failed",
                    "analysis": "",
                    "risks": [],
                    "opportunities": [],
                    "confidence": 0.0,
                    "metadata": {
                        "error": str(e)
                    }
                }

            specialist_outputs[agent_name] = output

        ############################################################
        # Execute Recommendation Agent
        ############################################################

        if "RecommendationAgent" in self.registry:

            try:

                recommendation = self.registry[
                    "RecommendationAgent"
                ].execute(
                    specialist_outputs
                )

            except Exception as e:

                recommendation = {
                    "agent": "RecommendationAgent",
                    "status": "failed",
                    "recommendation": "",
                    "priority": "Unknown",
                    "justification": str(e),
                    "confidence": 0.0
                }

            print("\n========== EXECUTION SUMMARY ==========")

            for name, output in specialist_outputs.items():

                print(f"{name:20} -> {output['status']}")

            print("--------------------------------------")

            print(
                "Recommendation ->",
                recommendation["status"]
            )

            print("======================================")

        ############################################################

        elapsed = round(
            time.time() - start,
            3
        )

        return {

            "goal": plan["goal"],

            "execution_plan": ordered_plan,

            "specialists": specialist_outputs,

            "recommendation": recommendation,

            "confidence": plan["confidence"],

            "execution_time": elapsed
        }


########################################################################
# Singleton
########################################################################

executor = Executor()
