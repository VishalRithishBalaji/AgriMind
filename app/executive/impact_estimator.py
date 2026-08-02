"""
==========================================================================
AgriMind

Executive Impact Estimator

Module 5F

Estimates

1. Agronomic Impact
2. Economic Impact
3. Environmental Impact
4. Operational Impact
5. Expected Benefits

Author : AgriMind Team
==========================================================================
"""

from app.executive.executive_models import ExecutiveImpact


class ImpactEstimator:

    """
    Estimates the impact of current farm conditions.
    """

    ####################################################################
    # Estimate Impact
    ####################################################################

    def estimate(

        self,

        context,

        reasoning,

        priority_result

    ):

        ############################################################
        # Inputs
        ############################################################

        risks = reasoning.merged_risks

        opportunities = reasoning.merged_opportunities

        risk_level = priority_result["risk_level"]

        market = context["market"]

        satellite = context["satellite"]

        ############################################################
        # Scores
        ############################################################

        agronomic_score = 100
        economic_score = 100
        environmental_score = 100
        operational_score = 100

        ############################################################
        # Agronomic
        ############################################################

        for risk in risks:

            r = risk.lower()

            if "vegetation" in r:
                agronomic_score -= 30

            elif "water stress" in r:
                agronomic_score -= 25

            elif "nitrogen" in r:
                agronomic_score -= 15

            elif "organic carbon" in r:
                agronomic_score -= 10

            elif "soil texture" in r:
                agronomic_score -= 10

            elif "rainfall" in r:
                agronomic_score -= 10

        agronomic_score = max(0, agronomic_score)

        ############################################################
        # Economic
        ############################################################

        trend = market["assessment"].get(

            "trend",

            "Stable"

        )

        if trend == "Increasing":

            economic_score += 5

        elif trend == "Stable":

            pass

        else:

            economic_score -= 20

        if risk_level == "Critical":

            economic_score -= 20

        elif risk_level == "High":

            economic_score -= 10

        economic_score = min(

            100,

            max(

                economic_score,

                0

            )

        )

        ############################################################
        # Environmental
        ############################################################

        if satellite["status"] == "success":

            if satellite["water"]["stress"] == "High":

                environmental_score -= 25

            if satellite["soil"]["exposure"] == "High":

                environmental_score -= 20

        environmental_score = max(

            0,

            environmental_score

        )

        ############################################################
        # Operational
        ############################################################

        operational_score -= (

            len(risks) * 5

        )

        operational_score = max(

            0,

            operational_score

        )

        ############################################################
        # Labels
        ############################################################

        def label(score):

            if score >= 85:

                return "Excellent"

            elif score >= 70:

                return "Good"

            elif score >= 50:

                return "Moderate"

            else:

                return "Poor"

        ############################################################
        # Yield Risk
        ############################################################

        if agronomic_score >= 85:

            yield_risk = "Low"

        elif agronomic_score >= 65:

            yield_risk = "Moderate"

        elif agronomic_score >= 45:

            yield_risk = "High"

        else:

            yield_risk = "Severe"

        ############################################################
        # Profitability
        ############################################################

        if (

            economic_score >= 80

            and

            trend == "Increasing"

        ):

            profitability = "High"

        elif economic_score >= 60:

            profitability = "Moderate"

        else:

            profitability = "Low"

        ############################################################
        # Expected Benefit
        ############################################################

        if risk_level == "Critical":

            expected_benefit = (

                "Immediate intervention can significantly reduce crop loss."

            )

        elif risk_level == "High":

            expected_benefit = (

                "Timely corrective action will improve productivity."

            )

        elif opportunities:

            expected_benefit = (

                "Current conditions provide opportunities for improved profitability."

            )

        else:

            expected_benefit = (

                "Continue monitoring crop conditions."

            )

        ############################################################

        return ExecutiveImpact(

            agronomic_impact=label(

                agronomic_score

            ),

            economic_impact=label(

                economic_score

            ),

            environmental_impact=label(

                environmental_score

            ),

            operational_impact=label(

                operational_score

            ),

            expected_benefit=expected_benefit,

            yield_risk=yield_risk,

            profitability=profitability

        )


##########################################################################

impact_estimator = ImpactEstimator()