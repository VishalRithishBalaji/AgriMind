from datetime import datetime

from app.tools.satellite_tool import satellite_tool


class SatelliteCollector:

    ####################################################################
    # Collect Satellite Data
    ####################################################################

    def collect(
        self,
        latitude,
        longitude
    ):

        ################################################################
        # Validate Coordinates
        ################################################################

        if latitude is None or longitude is None:

            return {

                "source": "satellite",

                "status": "failed",

                "confidence": 0,

                "error": "Latitude and Longitude are required.",

                "timestamp": datetime.utcnow().isoformat(),

                "location": {

                    "latitude": latitude,

                    "longitude": longitude

                }

            }

        try:

            latitude = float(latitude)
            longitude = float(longitude)

        except (TypeError, ValueError):

            return {

                "source": "satellite",

                "status": "failed",

                "confidence": 0,

                "error": "Invalid coordinate format.",

                "timestamp": datetime.utcnow().isoformat(),

                "location": {

                    "latitude": latitude,

                    "longitude": longitude

                }

            }

        ################################################################
        # Execute Satellite Tool
        ################################################################

        try:

            result = satellite_tool.execute(

                latitude=latitude,

                longitude=longitude

            )

        except Exception as e:

            return {

                "source": "satellite",

                "status": "failed",

                "confidence": 0,

                "error": str(e),

                "timestamp": datetime.utcnow().isoformat(),

                "location": {

                    "latitude": latitude,

                    "longitude": longitude

                }

            }

        ################################################################
        # Success Response
        ################################################################

        return {

            "source": "satellite",

            "status": result["status"],

            "confidence": result["confidence"],

            "timestamp": datetime.utcnow().isoformat(),

            "location": {

                "latitude": latitude,

                "longitude": longitude

            },

            "imagery": {

                "acquisition_date":

                    result["data"]["acquisition_date"],

                "cloud_cover":

                    result["data"]["cloud_cover"],

                "valid_pixels":

                    result["data"]["valid_pixels"]

            },

            "vegetation": {

                "ndvi":

                    result["data"]["ndvi"],

                "evi":

                    result["data"]["evi"],

                "savi":

                    result["data"]["savi"],

                "health":

                    result["assessment"]["crop_health"]

            },

            "water": {

                "ndwi":

                    result["data"]["ndwi"],

                "stress":

                    result["assessment"]["water_stress"]

            },

            "soil": {

                "exposure":

                    result["assessment"]["soil_exposure"]

            },

            "assessment": {

                "vegetation_score":

                    result["assessment"]["vegetation_score"],

                "recommendation":

                    result["assessment"]["recommendation"]

            }

        }


########################################################################
# Singleton
########################################################################

satellite_collector = SatelliteCollector()