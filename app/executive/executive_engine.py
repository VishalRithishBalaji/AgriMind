"""
==========================================================================
AgriMind

Executive Decision Engine

Module 5F

Synthesizes

1. Context
2. Collaborative Reasoning
3. Priority Engine
4. Impact Estimator
5. Executive Summary

into a single Executive Decision.

Author : AgriMind Team
==========================================================================
"""

from app.executive.priority_engine import priority_engine
from app.executive.impact_estimator import impact_estimator
from app.executive.summary_generator import summary_generator

from app.executive.executive_models import (

    ExecutiveDecision,

    ExecutiveReport

)


class ExecutiveDecisionEngine:

    """
    Executive Decision Intelligence Engine
    """

    ####################################################################
    # Infer Decision
    ####################################################################

    def infer_decision(

        self,

        context,

        reasoning,

        priority_result

    ):

        ############################################################
        # Risks
        ############################################################

        risks = [

            risk.lower()

            for risk in reasoning.merged_risks

        ]

        ############################################################
        # Decision Logic
        ############################################################

        if any(

            "water stress" in r

            for r in risks

        ):

            return (

                "Immediate Irrigation"

            )

        ############################################################

        if any(

            "vegetation" in r

            for r in risks

        ):

            return (

                "Field Inspection"

            )

        ############################################################

        if any(

            "nitrogen" in r

            for r in risks

        ):

            return (

                "Apply Nitrogen Fertilizer"

            )

        ############################################################

        if any(

            "organic carbon" in r

            for r in risks

        ):

            return (

                "Apply Organic Manure"

            )

        ############################################################

        trend = context["market"]["assessment"].get(

            "trend",

            ""

        )

        if trend == "Increasing":

            return (

                "Prepare for Harvest and Selling"

            )

        ############################################################

        return (

            "Continue Monitoring"

        )

    ####################################################################
    # Supporting Evidence
    ####################################################################

    def build_evidence(

        self,

        reasoning

    ):

        evidence = []

        ############################################################

        for agent in reasoning.evidence:

            analysis = agent.get(

                "analysis",

                ""

            )

            if analysis:

                evidence.append(

                    f"{agent['agent']}: {analysis}"

                )

        ############################################################

        return evidence

    ####################################################################
    # Execute
    ####################################################################

    def execute(

        self,

        context,

        reasoning

    ):

        ############################################################
        # Priority
        ############################################################

        priority_result = priority_engine.compute(

            context,

            reasoning

        )

        ############################################################
        # Impact
        ############################################################

        impact = impact_estimator.estimate(

            context,

            reasoning,

            priority_result

        )

        ############################################################
        # Summary
        ############################################################

        summary = summary_generator.generate(

            context,

            reasoning,

            priority_result,

            impact

        )

        ############################################################
        # Decision
        ############################################################

        decision = self.infer_decision(

            context,

            reasoning,

            priority_result

        )

        ############################################################
        # Evidence
        ############################################################

        evidence = self.build_evidence(

            reasoning

        )

        ############################################################
        # Executive Decision Object
        ############################################################

        executive_decision = ExecutiveDecision(

            crop=context["crop"],

            decision=decision,

            priority=priority_result["priority"],

            urgency=priority_result["urgency"],

            risk_level=priority_result["risk_level"],

            confidence=round(

                reasoning.confidence,

                2

            ),

            action_order=priority_result["ordered_actions"],

            priorities=priority_result["priorities"],

            impact=impact,

            summary=summary,

            supporting_evidence=evidence,

            metadata={

                "location": context["location"],

                "historical_records": context[

                    "historical_records"

                ],

                "generated_from": "Collaborative Reasoning"

            }

        )

        ############################################################

        return ExecutiveReport(

            decision=executive_decision

        )


##########################################################################
# Singleton
##########################################################################

executive_engine = ExecutiveDecisionEngine()