"""
==========================================================================
AgriMind

Dynamic Executor

Module 5E Integration

Author : AgriMind Team
==========================================================================
"""

import logging
from typing import Dict, List

from app.reasoning.collaborative_engine import collaborative_engine

# Import your existing agents
from app.agents.weather_agent import weather_agent
from app.agents.soil_agent import soil_agent
from app.agents.satellite_agent import satellite_agent
from app.agents.market_agent import market_agent
from app.agents.historical_agent import historical_agent
from app.agents.recommendation_agent import recommendation_agent


logger = logging.getLogger(__name__)


class DynamicExecutor:

    """
    Executes the dynamic execution plan.

    Workflow

    Planner
        ↓
    Specialist Agents
        ↓
    Collaborative Reasoning
        ↓
    Recommendation Agent
    """

    ####################################################################
    # Agent Registry
    ####################################################################

    def __init__(self):

        self.agent_registry = {

            "WeatherAgent": weather_agent,

            "SoilAgent": soil_agent,

            "SatelliteAgent": satellite_agent,

            "HistoricalAgent": historical_agent,

            "MarketAgent": market_agent

        }

    ####################################################################
    # Execute Specialist Agents
    ####################################################################

    def execute_specialists(

        self,

        execution_plan,

        context

    ):

        outputs = []

        for step in execution_plan:

            agent_name = step["agent"]

            if agent_name not in self.agent_registry:

                logger.warning(

                    f"Unknown agent: {agent_name}"

                )

                continue

            logger.info(

                f"Running {agent_name}"

            )

            agent = self.agent_registry[agent_name]

            result = agent.analyze(context)

            result["agent"] = agent_name

            outputs.append(result)

        return outputs

    ####################################################################
    # Main Execute
    ####################################################################

    def execute(

        self,

        plan,

        context

    ):

        specialist_outputs = {}

        ##########################################################

        for step in plan["execution_plan"]:

            agent_name = step["agent"]

            if agent_name == "RecommendationAgent":

                continue

            if agent_name not in self.agent_registry:

                continue

            logger.info(

                f"Running {agent_name}"

            )

            agent = self.agent_registry[agent_name]

            result = agent.execute(

                context

            )

            result["agent"] = agent_name

            specialist_outputs[agent_name] = result

        ##########################################################
        # Gemini Collaborative Reasoning
        ##########################################################

        reasoning = collaborative_engine.collaborative_reasoning(

            context,

            specialist_outputs

        )

        ##########################################################
        # Gemini Recommendation
        ##########################################################

        recommendation = recommendation_agent.execute(

            reasoning

        )

        ##########################################################

        return {

            "goal":

                plan["goal"],

            "execution_plan":

                plan["execution_plan"],

            "specialists":

                specialist_outputs,

            "reasoning":

                reasoning,

            "recommendation":

                recommendation,

            "confidence":

                reasoning.confidence

        }

##########################################################################

executor = DynamicExecutor()