"""
==========================================================================
AgriMind

Soil Collector

Collects soil information using the dynamic crop profile.

Author : AgriMind Team
==========================================================================
"""

from app.tools.soil_tool import soil_tool


class SoilCollector:

    """
    Soil Collector

    Responsibilities
    ----------------
    1. Call SoilTool.
    2. Normalize the response.
    3. Return standardized soil data.
    """

    ####################################################################
    # Collect
    ####################################################################

    def collect(

        self,

        crop_profile,

        latitude=None,

        longitude=None

    ):

        result = soil_tool.execute(

            crop_profile=crop_profile,

            latitude=latitude,

            longitude=longitude

        )

        ############################################################

        return {

            "source": "soil",

            "status": result["status"],

            "location": {

                "district": result["data"].get("district"),

                "state": result["data"].get("state")

            },

            "raw_data": result["data"],

            "assessment": result["assessment"],

            "confidence": result["confidence"]

        }


##########################################################################

soil_collector = SoilCollector()