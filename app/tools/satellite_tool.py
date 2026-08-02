"""
==========================================================================
AgriMind

Dynamic Satellite Tool

Part 9A

Uses Google Earth Engine

Author : AgriMind Team
==========================================================================
"""

import ee

from app.services.earth_engine_service import (
    earth_engine_service
)


class SatelliteTool:

    ####################################################################
    # NDVI
    ####################################################################

    def ndvi(

        self,

        image,

        region

    ):

        ndvi = image.normalizedDifference(

            ["B8", "B4"]

        ).rename("NDVI")

        return self.reduce_index(

            ndvi,

            region,

            "NDVI"

        )

    ####################################################################
    # NDWI
    ####################################################################

    def ndwi(

        self,

        image,

        region

    ):

        ndwi = image.normalizedDifference(

            ["B3", "B8"]

        ).rename("NDWI")

        return self.reduce_index(

            ndwi,

            region,

            "NDWI"

        )

    ####################################################################
    # SAVI
    ####################################################################

    def savi(

        self,

        image,

        region

    ):

        savi = image.expression(

            "((nir-red)/(nir+red+L))*(1+L)",

            {

                "nir": image.select("B8"),

                "red": image.select("B4"),

                "L": 0.5

            }

        ).rename("SAVI")

        return self.reduce_index(

            savi,

            region,

            "SAVI"

        )

    ####################################################################
    # EVI
    ####################################################################

    def evi(

        self,

        image,

        region

    ):

        evi = image.expression(

            "2.5*((nir-red)/(nir+6*red-7.5*blue+1))",

            {

                "nir": image.select("B8"),

                "red": image.select("B4"),

                "blue": image.select("B2")

            }

        ).rename("EVI")

        return self.reduce_index(

            evi,

            region,

            "EVI"

        )

    ####################################################################
    # Reduce Index
    ####################################################################

    def reduce_index(

        self,

        image,

        region,

        band

    ):

        stats = image.reduceRegion(

            reducer=ee.Reducer.mean(),

            geometry=region,

            scale=10,

            maxPixels=1e9

        )

        value = stats.get(

            band

        )

        if value is None:

            return None

        value = value.getInfo()

        if value is None:

            return None

        return round(

            float(value),

            3

        )

    ####################################################################
    # Retrieve Satellite Statistics
    ####################################################################

    def get_satellite_data(

        self,

        latitude,

        longitude

    ):

        image, metadata, point, region = (

            earth_engine_service.get_best_image(

                latitude,

                longitude

            )

        )

        summary = earth_engine_service.summary(

            metadata,

            image,

            region

        )

        return {

            "image":

                image,

            "region":

                region,

            "metadata":

                metadata,

            "acquisition_date":

                summary["acquisition_date"],

            "cloud_cover":

                summary["cloud_cover"],

            "valid_pixels":

                summary["valid_pixels"],

            "ndvi":

                self.ndvi(

                    image,

                    region

                ),

            "ndwi":

                self.ndwi(

                    image,

                    region

                ),

            "evi":

                self.evi(

                    image,

                    region

                ),

            "savi":

                self.savi(

                    image,

                    region

                )

        }

        ####################################################################
    # Crop Health
    ####################################################################

    def crop_health(

        self,

        ndvi,

        crop_profile

    ):

        if ndvi is None:

            return "Unknown", 0

        thresholds = crop_profile.get(

            "satellite_thresholds",

            {}

        ).get(

            "ndvi",

            {}

        )

        excellent = thresholds.get("excellent", 0.80)
        healthy = thresholds.get("healthy", 0.65)
        moderate = thresholds.get("moderate", 0.45)
        poor = thresholds.get("poor", 0.30)

        if ndvi >= excellent:

            return "Excellent", 100

        elif ndvi >= healthy:

            return "Healthy", 90

        elif ndvi >= moderate:

            return "Moderate", 75

        elif ndvi >= poor:

            return "Poor", 60

        return "Critical", 40

    ####################################################################
    # Water Stress
    ####################################################################

    def water_stress(

        self,

        ndwi,

        crop_profile

    ):

        if ndwi is None:

            return "Unknown"

        thresholds = crop_profile.get(

            "satellite_thresholds",

            {}

        ).get(

            "ndwi",

            {}

        )

        low = thresholds.get(

            "low_stress",

            0.30

        )

        moderate = thresholds.get(

            "moderate_stress",

            0.10

        )

        if ndwi >= low:

            return "Low"

        elif ndwi >= moderate:

            return "Moderate"

        return "High"

    ####################################################################
    # Soil Exposure
    ####################################################################

    def soil_exposure(

        self,

        savi,

        crop_profile

    ):

        if savi is None:

            return "Unknown"

        thresholds = crop_profile.get(

            "satellite_thresholds",

            {}

        ).get(

            "savi",

            {}

        )

        low = thresholds.get(

            "low_exposure",

            0.60

        )

        moderate = thresholds.get(

            "moderate_exposure",

            0.40

        )

        if savi >= low:

            return "Low"

        elif savi >= moderate:

            return "Moderate"

        return "High"

    ####################################################################
    # Vegetation Score
    ####################################################################

    def vegetation_score(

        self,

        ndvi,

        evi,

        savi

    ):

        values = [

            v for v in [

                ndvi,

                evi,

                savi

            ]

            if v is not None

        ]

        if not values:

            return 0

        avg = sum(values) / len(values)

        score = max(

            0,

            min(

                100,

                avg * 100

            )

        )

        return round(

            score,

            2

        )

    ####################################################################
    # Recommendation
    ####################################################################

    def recommendation(

        self,

        crop_health,

        water_stress,

        soil_exposure

    ):

        recommendations = []

        if crop_health in [

            "Poor",

            "Critical"

        ]:

            recommendations.append(

                "Inspect crop for nutrient deficiency or disease."

            )

        if water_stress == "High":

            recommendations.append(

                "Increase irrigation immediately."

            )

        elif water_stress == "Moderate":

            recommendations.append(

                "Monitor soil moisture closely."

            )

        if soil_exposure == "High":

            recommendations.append(

                "Increase ground cover or mulching."

            )

        if not recommendations:

            recommendations.append(

                "Crop conditions are healthy. Continue regular monitoring."

            )

        return " ".join(

            recommendations

        )

        ####################################################################
    # Execute
    ####################################################################

    def execute(

        self,

        crop_profile,

        latitude,

        longitude

    ):

        ############################################################
        # Retrieve Satellite Data
        ############################################################

        try:

            data = self.get_satellite_data(

                latitude,

                longitude

            )

        except Exception as e:

            return {

                "agent": "satellite_tool",

                "status": "failed",

                "confidence": 0,

                "error": str(e),

                "data": {},

                "assessment": {

                    "crop_health": "Unknown",

                    "water_stress": "Unknown",

                    "soil_exposure": "Unknown",

                    "vegetation_score": 0,

                    "recommendation":

                        "Satellite imagery unavailable."

                }

            }

        ############################################################
        # Vegetation Indices
        ############################################################

        ndvi = data.get("ndvi")

        ndwi = data.get("ndwi")

        evi = data.get("evi")

        savi = data.get("savi")

        ############################################################
        # Dynamic Assessment
        ############################################################

        crop_health, confidence = self.crop_health(

            ndvi,

            crop_profile

        )

        water = self.water_stress(

            ndwi,

            crop_profile

        )

        soil = self.soil_exposure(

            savi,

            crop_profile

        )

        vegetation_score = self.vegetation_score(

            ndvi,

            evi,

            savi

        )

        recommendation = self.recommendation(

            crop_health,

            water,

            soil

        )

        ############################################################
        # Response
        ############################################################

        return {

            "agent": "satellite_tool",

            "status": "success",

            "confidence": confidence,

            "data": {

                "acquisition_date":

                    data["acquisition_date"],

                "cloud_cover":

                    data["cloud_cover"],

                "valid_pixels":

                    data["valid_pixels"],

                "ndvi":

                    ndvi,

                "ndwi":

                    ndwi,

                "evi":

                    evi,

                "savi":

                    savi

            },

            "assessment": {

                "crop_health":

                    crop_health,

                "water_stress":

                    water,

                "soil_exposure":

                    soil,

                "vegetation_score":

                    vegetation_score,

                "recommendation":

                    recommendation

            }

        }


##########################################################################
# Singleton
##########################################################################

satellite_tool = SatelliteTool()

