"""
==========================================================================
AgriMind

Dynamic Multi-Agent Orchestrator

Pipeline

User Query
      │
      ▼
Crop Knowledge Agent
      │
      ▼
Data Collection
      │
      ▼
Context Understanding
      │
      ▼
Planner
      │
      ▼
Specialist Agents
      │
      ▼
Collaborative Reasoning
      │
      ▼
Executive Decision Intelligence
      │
      ▼
Recommendation Agent

Author : AgriMind Team
==========================================================================
"""

import time

from app.agents.crop_knowledge_agent import crop_knowledge_agent
from app.collectors.data_collector import data_collector
from app.agents.context_agent import context_agent
from app.orchestrator.planner import planner
from app.orchestrator.executor import executor


class DynamicOrchestrator:

    """
    Complete AgriMind Dynamic Orchestrator.
    """

    ####################################################################
    # Main Pipeline
    ####################################################################

    def run(

        self,

        user_query,

        crop="rice",

        latitude=11.0168,

        longitude=76.9558

    ):

        overall_start = time.time()

        ################################################################
        # STEP 1
        # Crop Knowledge
        ################################################################

        print("\nLoading Crop Knowledge...\n")

        crop_result = crop_knowledge_agent.execute(

            crop

        )

        crop_profile = crop_result["crop_profile"]

        ################################################################
        # STEP 2
        # Collect Farm Data
        ################################################################

        print("\nCollecting Farm Data...\n")

        collected_data = data_collector.collect(

            crop_profile=crop_profile,

            latitude=latitude,

            longitude=longitude

        )

        ################################################################
        # STEP 3
        # Context Understanding
        ################################################################

        print("\nBuilding Farm Context...\n")

        context = context_agent.analyze(

            collected_data

        )

        ################################################################
        # STEP 4
        # Dynamic Planning
        ################################################################

        print("\nPlanning...\n")

        plan = planner.plan(

            user_query,

            context

        )

        ################################################################
        # STEP 5
        # Multi-Agent Execution
        ################################################################

        print("\nExecuting Specialists...\n")

        execution = executor.execute(

            plan,

            context

        )

        ################################################################
        # Final Result
        ################################################################

        total_time = round(

            time.time() - overall_start,

            3

        )

        ################################################################

        return {

            ############################################################
            # Query
            ############################################################

            "query":

                user_query,

            ############################################################
            # Crop Knowledge
            ############################################################

            "crop_profile":

                crop_profile,

            ############################################################
            # Raw Data
            ############################################################

            "raw_data":

                collected_data,

            ############################################################
            # Context
            ############################################################

            "context":

                context,

            ############################################################
            # Planner
            ############################################################

            "plan":

                plan,

            ############################################################
            # Module 5F Output
            ############################################################

            "reasoning":

                execution["reasoning"],

            "executive":

                execution["executive"],

            "recommendation":

                execution["recommendation"],

            ############################################################
            # Full Execution
            ############################################################

            "execution":

                execution,

            ############################################################

            "status":

                "success",

            "total_time":

                total_time

        }


##########################################################################
# Singleton
##########################################################################

dynamic_orchestrator = DynamicOrchestrator()