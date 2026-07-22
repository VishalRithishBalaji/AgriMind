from app.tools.soil_tool import soil_tool


class SoilCollector:

    def collect(
        self,
        latitude=None,
        longitude=None
    ):

        result = soil_tool.execute(
            latitude=latitude,
            longitude=longitude
        )

        return {

            "source": "soil",

            "status": result.get("status"),

            "location": {

                "district": result["data"].get("district"),

                "state": result["data"].get("state")

            },

            "raw_data": result["data"],

            "assessment": result["assessment"],

            "confidence": result.get("confidence")

        }


soil_collector = SoilCollector()