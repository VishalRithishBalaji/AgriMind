import ee

from app.services.earth_engine_service import (
    earth_engine_service
)

from app.config import ai_settings


class SatelliteTool:

    ####################################################################
    # Generic Reduction
    ####################################################################

    def reduce_index(
        self,
        image,
        region,
        band_name
    ):

        stats = image.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=region,
            scale=10,
            maxPixels=1e9
        )

        value = stats.get(band_name)

        if value is None:
            return None

        value = value.getInfo()

        if value is None:
            return None

        return round(float(value), 4)

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
    # EVI
    ####################################################################

    def evi(
        self,
        image,
        region
    ):

        evi = image.expression(

            "2.5*((NIR-RED)/(NIR+6*RED-7.5*BLUE+1))",

            {

                "NIR": image.select("B8"),

                "RED": image.select("B4"),

                "BLUE": image.select("B2")

            }

        ).rename("EVI")

        return self.reduce_index(
            evi,
            region,
            "EVI"
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

            "((NIR-RED)/(NIR+RED+L))*(1+L)",

            {

                "NIR": image.select("B8"),

                "RED": image.select("B4"),

                "L": 0.5

            }

        ).rename("SAVI")

        return self.reduce_index(
            savi,
            region,
            "SAVI"
        )

        ####################################################################
    # Crop Health Assessment
    ####################################################################

    def crop_health(self, ndvi):

        if ndvi is None:
            return "Unknown", 0

        if ndvi >= ai_settings.NDVI_EXCELLENT:
            return "Excellent", 98

        elif ndvi >= ai_settings.NDVI_HEALTHY:
            return "Healthy", 90

        elif ndvi >= ai_settings.NDVI_MODERATE:
            return "Moderate", 75

        elif ndvi >= ai_settings.NDVI_POOR:
            return "Poor", 55

        return "Critical", 30

    ####################################################################
    # Water Stress
    ####################################################################

    def water_stress(self, ndwi):

        if ndwi is None:
            return "Unknown"

        if ndwi >= ai_settings.NDWI_LOW_STRESS:
            return "Low"

        elif ndwi >= ai_settings.NDWI_MODERATE_STRESS:
            return "Moderate"

        return "High"

    ####################################################################
    # Soil Exposure
    ####################################################################

    def soil_exposure(self, savi):

        if savi is None:
            return "Unknown"

        if savi >= ai_settings.SAVI_LOW_EXPOSURE:
            return "Low"

        elif savi >= ai_settings.SAVI_MODERATE_EXPOSURE:
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

        if ndvi is None:
            return 0

        if evi is None:
            evi = ndvi

        if savi is None:
            savi = ndvi

        score = (

            ndvi * 0.45 +

            evi * 0.35 +

            savi * 0.20

        )

        score = max(0.0, min(score, 1.0))

        return round(score * 100, 2)

    ####################################################################
    # Recommendation Engine
    ####################################################################

    def recommendation(
        self,
        health,
        stress,
        soil
    ):

        recommendations = []

        if health == "Excellent":

            recommendations.append(
                "Crop is performing exceptionally well."
            )

        elif health == "Healthy":

            recommendations.append(
                "Maintain current nutrient and irrigation practices."
            )

        elif health == "Moderate":

            recommendations.append(
                "Monitor crop growth and inspect for nutrient deficiencies."
            )

        elif health == "Poor":

            recommendations.append(
                "Field inspection is recommended. Review irrigation and fertilization."
            )

        else:

            recommendations.append(
                "Immediate agronomic inspection is recommended."
            )

        if stress == "High":

            recommendations.append(
                "Increase irrigation or investigate moisture availability."
            )

        elif stress == "Moderate":

            recommendations.append(
                "Monitor soil moisture over the next few days."
            )

        if soil == "High":

            recommendations.append(
                "Consider mulching or cover crops to reduce exposed soil."
            )

        elif soil == "Moderate":

            recommendations.append(
                "Monitor soil cover and erosion risk."
            )

        return " ".join(recommendations)
        ####################################################################
    # Execute
    ####################################################################

    def execute(
        self,
        latitude,
        longitude
    ):

        (
            image,
            metadata,
            point,
            region
        ) = earth_engine_service.get_best_image(
            latitude,
            longitude
        )

        ################################################################
        # Vegetation Indices
        ################################################################

        ndvi = self.ndvi(
            image,
            region
        )

        evi = self.evi(
            image,
            region
        )

        ndwi = self.ndwi(
            image,
            region
        )

        savi = self.savi(
            image,
            region
        )

        ################################################################
        # Assessments
        ################################################################

        crop_health, confidence = self.crop_health(
            ndvi
        )

        water_stress = self.water_stress(
            ndwi
        )

        soil_exposure = self.soil_exposure(
            savi
        )

        vegetation_score = self.vegetation_score(
            ndvi,
            evi,
            savi
        )

        recommendation = self.recommendation(
            crop_health,
            water_stress,
            soil_exposure
        )

        ################################################################
        # Metadata
        ################################################################

        summary = earth_engine_service.summary(
            metadata,
            image,
            region
        )

        ################################################################
        # Response
        ################################################################

        return {

            "agent": "satellite_tool",

            "status": "success",

            "confidence": confidence,

            "data": {

                "latitude": float(latitude),

                "longitude": float(longitude),

                "acquisition_date":
                    summary["acquisition_date"],

                "cloud_cover":
                    summary["cloud_cover"],

                "valid_pixels":
                    summary["valid_pixels"],

                "ndvi":
                    ndvi,

                "evi":
                    evi,

                "ndwi":
                    ndwi,

                "savi":
                    savi

            },

            "assessment": {

                "crop_health":
                    crop_health,

                "water_stress":
                    water_stress,

                "soil_exposure":
                    soil_exposure,

                "vegetation_score":
                    vegetation_score,

                "recommendation":
                    recommendation

            }

        }


########################################################################
# Singleton
########################################################################

satellite_tool = SatelliteTool()