import pandas as pd

from app.config.settings import settings


class MarketTool:

    def __init__(self):

        self.df = pd.read_csv("data/market_prices.csv")

    def get_market(
        self,
        crop,
        district=None
    ):

        crop = crop.title()

        if district is None:
            district = "Coimbatore"

        result = self.df[
            (self.df["Crop"] == crop)
            &
            (self.df["District"] == district)
        ]

        if result.empty:

            return None

        return result.iloc[0].to_dict()

    def assess_market(self, market):

        score = 100
        advice = ""

        trend = market["Trend"]

        if trend == "Increasing":

            advice = "Good time to sell."

        elif trend == "Stable":

            advice = "Market is stable."

            score -= 5

        else:

            advice = "Consider delaying sale."

            score -= 20

        return {

            "market_score": score,

            "trend": trend,

            "recommendation": advice

        }

    def execute(
        self,
        crop,
        district=None
    ):

        market = self.get_market(
            crop,
            district
        )

        if market is None:

            return {

                "agent": "market_tool",

                "status": "failed",

                "confidence": 0,

                "data": None,

                "assessment": {

                    "message": "Crop not found"

                }

            }

        assessment = self.assess_market(
            market
        )

        return {

            "agent": "market_tool",

            "status": "success",

            "confidence": assessment["market_score"],

            "data": market,

            "assessment": assessment

        }


market_tool = MarketTool()