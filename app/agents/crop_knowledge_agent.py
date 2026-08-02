"""
==========================================================================
AgriMind

Crop Knowledge Agent

Responsibilities

1. Receive crop name
2. Retrieve crop profile
3. Generate profile if missing
4. Return standardized output

Author : AgriMind Team
==========================================================================
"""

from app.knowledge.crop_profile_manager import crop_profile_manager


class CropKnowledgeAgent:

    """
    Dynamic Crop Knowledge Agent
    """

    name = "CropKnowledgeAgent"

    ####################################################################
    # Execute
    ####################################################################

    def execute(

        self,

        crop

    ):

        profile = crop_profile_manager.get_profile(

            crop

        )

        return {

            "agent": self.name,

            "status": "completed",

            "confidence": 1.0,

            "crop_profile": profile

        }

    ####################################################################
    # Alias
    ####################################################################

    def analyze(

        self,

        crop

    ):

        return self.execute(

            crop

        )


##########################################################################

crop_knowledge_agent = CropKnowledgeAgent()