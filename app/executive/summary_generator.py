"""
==========================================================================
AgriMind

Executive Summary Generator

Module 5F

Generates executive-level summaries for dashboards and reports.

Author : AgriMind Team
==========================================================================
"""

from app.executive.executive_models import ExecutiveSummary


class SummaryGenerator:

    """
    Generates concise executive summaries.
    """

    ####################################################################
    # Generate Summary
    ####################################################################

    def generate(

        self,

        context,

        reasoning,

        priority_result,

        impact

    ):

        ############################################################
        # Context
        ############################################################

        crop = context["crop"].title()

        location = context["location"]["district"]

        state = context["location"]["state"]

        priority = priority_result["priority"]

        urgency = priority_result["urgency"]

        risk_level = priority_result["risk_level"]

        ############################################################
        # Executive Summary
        ############################################################

        executive_summary = (

            f"{crop} cultivation in {location}, {state} "

            f"currently has a {risk_level.lower()} operational risk "

            f"requiring {urgency.lower()} attention."

        )

        ############################################################
        # Business Summary
        ############################################################

        market = context["market"]["assessment"]

        trend = market.get(

            "trend",

            "Unknown"

        )

        profitability = impact.profitability

        business_summary = (

            f"Market trend is {trend.lower()} with "

            f"{profitability.lower()} profitability potential."

        )

        ############################################################
        # Technical Summary
        ############################################################

        weather = context["weather"]["assessment"]["status"]

        soil = context["soil"]["assessment"]["soil_health_score"]

        vegetation = context["vegetation_health"]

        technical_summary = (

            f"Weather status: {weather}. "

            f"Soil health score: {soil}. "

            f"Vegetation health: {vegetation}."

        )

        ############################################################
        # Justification
        ############################################################

        if reasoning.merged_risks:

            top_risks = ", ".join(

                reasoning.merged_risks[:3]

            )

        else:

            top_risks = "No major risks detected."

        justification = (

            f"The executive decision is based on "

            f"{len(reasoning.evidence)} specialist agents. "

            f"Primary concerns include: {top_risks}."

        )

        ############################################################

        return ExecutiveSummary(

            executive_summary=executive_summary,

            business_summary=business_summary,

            technical_summary=technical_summary,

            justification=justification

        )


##########################################################################

summary_generator = SummaryGenerator()