from app.agents.context_agent import context_agent
from app.orchestrator.planner import planner
from app.orchestrator.executor import executor


class DynamicOrchestrator:
    """
    Dynamic Agent Orchestrator

    Pipeline

    User Query
        ↓
    Context Agent
        ↓
    LLM Planner
        ↓
    Executor
        ↓
    Final Result
    """

    def __init__(self):

        self.context_agent = context_agent

        self.planner = planner

        self.executor = executor

    ####################################################################
    # Build Context
    ####################################################################

    def build_context(

        self,

        crop,

        location

    ):

        print()

        print("=" * 70)

        print("BUILDING FARM CONTEXT")

        print("=" * 70)

        context = self.context_agent.analyze(

            crop=crop,

            location=location

        )

        return context

    ####################################################################
    # Create Execution Plan
    ####################################################################

    def create_plan(

        self,

        query,

        context

    ):

        print()

        print("=" * 70)

        print("PLANNING")

        print("=" * 70)

        plan = self.planner.plan(

            user_query=query,

            context=context

        )

        return plan

    ####################################################################
    # Execute Plan
    ####################################################################

    def execute_plan(

        self,

        plan,

        context

    ):

        print()

        print("=" * 70)

        print("EXECUTING")

        print("=" * 70)

        return self.executor.execute(

            plan,

            context

        )

    ####################################################################
    # Complete Workflow
    ####################################################################

    def run(

        self,

        crop,

        location,

        user_query

    ):

        context = self.build_context(

            crop,

            location

        )

        plan = self.create_plan(

            user_query,

            context

        )

        execution = self.execute_plan(

            plan,

            context

        )

        return {

            "query": user_query,

            "context": context,

            "plan": plan,

            "execution": execution,

            "status": "success"

        }


########################################################################
# Singleton
########################################################################

dynamic_orchestrator = DynamicOrchestrator()