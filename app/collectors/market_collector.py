"""
==========================================================================
AgriMind

Market Collector

Collects market information using the dynamic crop profile.

Author : AgriMind Team
==========================================================================
"""

from app.tools.market_tool import market_tool


class MarketCollector:

    """
    Market Collector

    Responsibilities
    ----------------
    1. Call MarketTool.
    2. Normalize the response.
    3. Return standardized market data.
    """

    ####################################################################
    # Collect
    ####################################################################

    def collect(

        self,

        crop_profile,

        district=None

    ):

        result = market_tool.execute(

            crop_profile=crop_profile,

            district=district

        )

        ############################################################
        # Failed Lookup
        ############################################################

        if result.get("status") != "success":

            return {

                "source": "market",

                "status": "failed",

                "market": None,

                "raw_data": {},

                "assessment": result.get(

                    "assessment",

                    {}

                ),

                "confidence": 0

            }

        ############################################################
        # Successful Lookup
        ############################################################

        raw_data = result.get(

            "data",

            {}

        ) or {}

        return {

            "source": "market",

            "status": "success",

            "market": raw_data.get("Market"),

            "raw_data": raw_data,

            "assessment": result.get(

                "assessment",

                {}

            ),

            "confidence": result.get(

                "confidence",

                0

            )

        }


##########################################################################

market_collector = MarketCollector()