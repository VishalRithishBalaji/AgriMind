"""
==========================================================================
AgriMind

Executive Priority Engine

Module 5F

Determines

1. Priority
2. Risk Level
3. Urgency
4. Action Ordering

Author : AgriMind Team
==========================================================================
"""

from app.executive.executive_models import ExecutivePriority


class PriorityEngine:

    """
    Executive Priority Engine
    """

    ####################################################################
    # Compute Priority
    ####################################################################

    def compute(

        self,

        context,

        reasoning

    ):

        priorities = []

        ############################################################
        # Initial Scores
        ############################################################

        severity_score = 0

        crop = context["crop"]

        ############################################################
        # Weather
        ############################################################

        for risk in reasoning.merged_risks:

            risk_lower = risk.lower()

            ########################################################

            if "water stress" in risk_lower:

                severity_score += 35

                priorities.append(

                    ExecutivePriority(

                        issue="Water Stress",

                        severity="Critical",

                        urgency="Immediate",

                        owner="Farmer",

                        action="Increase irrigation immediately"

                    )

                )

            ########################################################

            elif "vegetation" in risk_lower:

                severity_score += 30

                priorities.append(

                    ExecutivePriority(

                        issue="Vegetation Health",

                        severity="Critical",

                        urgency="Immediate",

                        owner="Agronomist",

                        action="Inspect crop for disease and nutrient deficiency"

                    )

                )

            ########################################################

            elif "rainfall" in risk_lower:

                severity_score += 20

                priorities.append(

                    ExecutivePriority(

                        issue="Rainfall",

                        severity="High",

                        urgency="Today",

                        owner="Farmer",

                        action="Supplement rainfall through irrigation"

                    )

                )

            ########################################################

            elif "nitrogen" in risk_lower:

                severity_score += 15

                priorities.append(

                    ExecutivePriority(

                        issue="Nitrogen",

                        severity="Medium",

                        urgency="Within 3 Days",

                        owner="Farmer",

                        action="Apply nitrogen fertilizer"

                    )

                )

            ########################################################

            elif "organic carbon" in risk_lower:

                severity_score += 15

                priorities.append(

                    ExecutivePriority(

                        issue="Organic Carbon",

                        severity="Medium",

                        urgency="Within 1 Week",

                        owner="Farmer",

                        action="Apply compost or organic manure"

                    )

                )

            ########################################################

            elif "soil texture" in risk_lower:

                severity_score += 10

                priorities.append(

                    ExecutivePriority(

                        issue="Soil Structure",

                        severity="Medium",

                        urgency="Next Season",

                        owner="Agronomist",

                        action="Improve soil structure using organic matter"

                    )

                )

            ########################################################

            elif "market" in risk_lower:

                severity_score += 5

        ############################################################
        # Overall Risk Level
        ############################################################

        if severity_score >= 80:

            risk_level = "Critical"

            priority = "P1"

            urgency = "Immediate"

        elif severity_score >= 60:

            risk_level = "High"

            priority = "P2"

            urgency = "Today"

        elif severity_score >= 35:

            risk_level = "Moderate"

            priority = "P3"

            urgency = "This Week"

        else:

            risk_level = "Low"

            priority = "P4"

            urgency = "Monitor"

        ############################################################
        # Sort
        ############################################################

        severity_order = {

            "Critical": 4,

            "High": 3,

            "Medium": 2,

            "Low": 1

        }

        priorities.sort(

            key=lambda p: severity_order[p.severity],

            reverse=True

        )

        ############################################################
        # Ordered Actions
        ############################################################

        ordered_actions = [

            item.action

            for item in priorities

        ]

        ############################################################

        return {

            "crop": crop,

            "priority": priority,

            "risk_level": risk_level,

            "urgency": urgency,

            "severity_score": severity_score,

            "priorities": priorities,

            "ordered_actions": ordered_actions

        }


##########################################################################

priority_engine = PriorityEngine()