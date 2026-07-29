import time

from app.collectors.data_collector import data_collector
from app.agents.context_agent import context_agent
from app.orchestrator.planner import planner
from app.orchestrator.executor import executor


class DynamicOrchestrator:
    """
    Complete AgriMind Multi-Agent Orchestrator

    Pipeline
    --------
    User Query
        ↓
    Data Collection
        ↓
    Context Understanding
        ↓
    Planning
        ↓
    Specialist Execution
        ↓
    Recommendation
    """

    def run(
        self,
        user_query,
        crop="rice",
        latitude=11.0168,
        longitude=76.9558
    ):

        overall_start = time.time()

        ############################################################
        # Step 1 : Collect Data
        ############################################################

        print("\nCollecting Farm Data...\n")

        collected_data = data_collector.collect(
            crop=crop,
            latitude=latitude,
            longitude=longitude
        )

        ############################################################
        # Step 2 : Build Context
        ############################################################

        print("\nBuilding Farm Context...\n")

        context = context_agent.analyze(
            collected_data
        )

        ############################################################
        # Step 3 : Plan
        ############################################################

        print("\nPlanning...\n")

        plan = planner.plan(
            user_query,
            context
        )

        ############################################################
        # Step 4 : Execute
        ############################################################

        print("\nExecuting Specialists...\n")

        execution = executor.execute(
            plan,
            context
        )

        ############################################################

        total_time = round(
            time.time() - overall_start,
            3
        )

        return {

            "query": user_query,

            "raw_data": collected_data,

            "context": context,

            "plan": plan,

            "execution": execution,

            "status": "success",

            "total_time": total_time

        }


########################################################################
# Singleton
########################################################################

dynamic_orchestrator = DynamicOrchestrator()