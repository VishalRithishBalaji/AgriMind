"""
==========================================================================
AgriMind

Dynamic Market Tool

Uses

1. Local Market Dataset
2. Canonical Crop Profile

Author : AgriMind Team
==========================================================================
"""

import pandas as pd


class MarketTool:

    ####################################################################
    # Constructor
    ####################################################################

    def __init__(self):

        self.df = pd.read_csv(

            "data/market_prices.csv"

        )

    ####################################################################
    # Retrieve Market Data
    ####################################################################

    def get_market(

        self,

        crop,

        district=None

    ):

        crop = str(crop).strip().title()

        if district is None:

            district = "Coimbatore"

        district = str(district).strip()

        ############################################################
        # Normalize CSV
        ############################################################

        df = self.df.copy()

        df["Crop"] = df["Crop"].astype(str).str.strip().str.title()

        df["District"] = df["District"].astype(str).str.strip()

        ############################################################
        # 1. Exact Match
        ############################################################

        result = df[

            (df["Crop"] == crop)

            &

            (df["District"] == district)

        ]

        if not result.empty:

            market = result.iloc[0].to_dict()

            market["match_type"] = "district"

            return market

        ############################################################
        # 2. Crop Fallback
        ############################################################

        result = df[

            df["Crop"] == crop

        ]

        if not result.empty:

            market = result.iloc[0].to_dict()

            market["match_type"] = "crop"

            return market

        ############################################################
        # 3. Not Found
        ############################################################

        return None


    ####################################################################
    # Dynamic Market Assessment
    ####################################################################

    def assess_market(

        self,

        market,

        crop_profile

    ):

        score = 100

        opportunities = []

        risks = []

        ############################################################
        # Market Trend
        ############################################################

        trend = str(

            market.get(

                "Trend",

                "Stable"

            )

        ).title()

        ############################################################
        # Canonical Profile
        ############################################################

        market_profile = crop_profile.get(

            "market",

            {}

        )

        harvest_season = market_profile.get(

            "harvest_season",

            "Unknown"

        )

        storage = market_profile.get(

            "storage_capability",

            "Moderate"

        )

        perishability = market_profile.get(

            "perishability",

            "Medium"

        )

        ############################################################
        # Trend Analysis
        ############################################################

        ############################################################
        # Fallback Information
        ############################################################

        if market.get("match_type") == "crop":

            opportunities.append(

                "Used nearest available market because district-specific data was unavailable."

            )

        if trend == "Increasing":

            recommendation = (

                "Market prices are increasing. "

                "Selling now is favorable."

            )

            opportunities.append(

                "Increasing market prices."

            )

        elif trend == "Stable":

            recommendation = (

                "Market prices are stable. "

                "Monitor for future movement."

            )

            score -= 5

        else:

            recommendation = (

                "Prices are decreasing."

            )

            score -= 20

            risks.append(

                "Market prices are falling."

            )

        ############################################################
        # Storage Capability
        ############################################################

        if storage.lower() == "good":

            opportunities.append(

                "Good storage capability allows delayed selling."

            )

        elif storage.lower() == "poor":

            risks.append(

                "Poor storage capability may force early selling."

            )

        ############################################################
        # Perishability
        ############################################################

        if perishability.lower() == "high":

            risks.append(

                "Highly perishable crop."

            )

            recommendation += (

                " Sell immediately after harvest."

            )

        elif perishability.lower() == "low":

            opportunities.append(

                "Low perishability enables flexible selling."

            )

        ############################################################

        score = max(

            score,

            0

        )

        ############################################################

        return {

            "market_score": score,

            "trend": trend,

            "harvest_season": harvest_season,

            "storage_capability": storage,

            "perishability": perishability,

            "recommendation": recommendation,

            "opportunities": opportunities,

            "risks": risks

        }

    ####################################################################
    # Execute
    ####################################################################

    def execute(

        self,

        crop_profile,

        district=None

    ):

        crop = crop_profile["crop"]

        ############################################################

        market = self.get_market(

            crop,

            district

        )

        ############################################################
        # No Market Data
        ############################################################

        if market is None:

            return {

                "agent": "market_tool",

                "status": "failed",

                "confidence": 0,

                "data": {},

                "assessment": {

                    "market_score": 0,

                    "trend": "Unknown",

                    "recommendation":

                        f"No market data available for {crop}.",

                    "opportunities": [],

                    "risks": []

                }

            }

        ############################################################

        assessment = self.assess_market(

            market,

            crop_profile

        )

        ############################################################

        return {

            "agent": "market_tool",

            "status": "success",

            "confidence": assessment["market_score"],

            "match_type":

                market.get(

                    "match_type",

                    "unknown"

                ),

            "data": market,

            "assessment": assessment

        }


##########################################################################
# Singleton
##########################################################################

market_tool = MarketTool()