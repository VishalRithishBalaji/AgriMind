"""
==========================================================================
AgriMind

Executive Decision Agent

Module 5F

Acts as the interface between the Executor and the
Executive Decision Engine.

Workflow

Collaborative Reasoning
        │
        ▼
Executive Decision Engine
        │
        ▼
Executive Report

Author : AgriMind Team
==========================================================================
"""

import time

from app.executive.executive_engine import executive_engine


class ExecutiveAgent:

    """
    Executive Decision Agent

    Responsibilities
    ----------------

    1. Receive Context

    2. Receive Collaborative Reasoning

    3. Generate Executive Decision

    4. Return standardized agent output
    """

    ####################################################################
    # Execute
    ####################################################################

    def execute(

        self,

        context,

        reasoning

    ):

        start = time.time()

        ############################################################
        # Executive Engine
        ############################################################

        report = executive_engine.execute(

            context=context,

            reasoning=reasoning

        )

        decision = report.decision

        ############################################################
        # Standardized Agent Response
        ############################################################

        result = {

            "agent":

                "ExecutiveAgent",

            "status":

                "completed",

            "confidence":

                decision.confidence,

            ########################################################
            # Decision
            ########################################################

            "decision":

                decision.decision,

            "priority":

                decision.priority,

            "urgency":

                decision.urgency,

            "risk_level":

                decision.risk_level,

            ########################################################
            # Action Plan
            ########################################################

            "action_order":

                decision.action_order,

            "priorities": [

                {

                    "issue":

                        p.issue,

                    "severity":

                        p.severity,

                    "urgency":

                        p.urgency,

                    "owner":

                        p.owner,

                    "action":

                        p.action

                }

                for p in decision.priorities

            ],

            ########################################################
            # Impact
            ########################################################

            "impact": {

                "agronomic":

                    decision.impact.agronomic_impact,

                "economic":

                    decision.impact.economic_impact,

                "environmental":

                    decision.impact.environmental_impact,

                "operational":

                    decision.impact.operational_impact,

                "yield_risk":

                    decision.impact.yield_risk,

                "profitability":

                    decision.impact.profitability,

                "expected_benefit":

                    decision.impact.expected_benefit

            },

            ########################################################
            # Executive Summary
            ########################################################

            "summary": {

                "executive":

                    decision.summary.executive_summary,

                "business":

                    decision.summary.business_summary,

                "technical":

                    decision.summary.technical_summary,

                "justification":

                    decision.summary.justification

            },

            ########################################################
            # Evidence
            ########################################################

            "supporting_evidence":

                decision.supporting_evidence,

            ########################################################

            "metadata":

                decision.metadata,

            ########################################################

            "execution_time":

                round(

                    (time.time() - start) * 1000,

                    3

                )

        }

        ############################################################

        return result


##########################################################################
# Singleton
##########################################################################

executive_agent = ExecutiveAgent()