import time

from app.orchestrator.registry import AGENT_REGISTRY


class Executor:

    """
    Dynamic Agent Executor

    Responsibilities

    1. Execute planner output

    2. Execute agents in priority order

    3. Collect outputs

    4. Return unified execution result
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

        result = agent.execute(

            context

        )

        return result

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

        results = {}

        for step in ordered_plan:

            try:

                output = self.execute_agent(

                    step,

                    context

                )

            except Exception as e:

                output = {

                    "agent": step["agent"],

                    "status": "failed",

                    "error": str(e)

                }

            results[step["agent"]] = output

        elapsed = round(

            time.time() - start,

            3

        )

        return {

            "goal":

                plan["goal"],

            "execution_plan":

                ordered_plan,

            "results":

                results,

            "confidence":

                plan["confidence"],

            "execution_time":

                elapsed

        }


########################################################################
# Singleton
########################################################################

executor = Executor()