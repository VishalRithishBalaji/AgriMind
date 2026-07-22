from app.tools.market_tool import market_tool


class MarketCollector:

    def collect(
        self,
        crop,
        district
    ):

        result = market_tool.execute(
            crop=crop,
            district=district
        )

        return {

            "source": "market",

            "status": result.get("status"),

            "market": result["data"].get("Market"),

            "raw_data": result["data"],

            "assessment": result["assessment"],

            "confidence": result.get("confidence")

        }


market_collector = MarketCollector()