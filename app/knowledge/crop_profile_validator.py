"""
==========================================================================
AgriMind

Crop Profile Validator

Validates, repairs and upgrades crop profiles.

This is the SINGLE SOURCE OF TRUTH for the Crop Profile schema.

Every profile loaded from

• Groq
• SQLite
• JSON Cache

passes through this validator.

Author : AgriMind Team
==========================================================================
"""

from copy import deepcopy


class CropProfileValidator:

    ####################################################################
    # Default Canonical Schema
    ####################################################################

    DEFAULT_SCHEMA = {

        "crop": "",

        "scientific_name": "",

        "family": "",

        "type": "",

        "category": "",

        "growth_duration_days": 0,

        "growth_stages": [

            "Germination",
            "Vegetative",
            "Flowering",
            "Harvest"

        ],

        "optimal_conditions": {

            "temperature": {

                "minimum": 20,
                "maximum": 30,
                "unit": "C"

            },

            "humidity": {

                "minimum": 60,
                "maximum": 80,
                "unit": "%"

            },

            "rainfall": {

                "minimum": 800,
                "maximum": 1500,
                "unit": "mm/year"

            },

            "soil_ph": {

                "minimum": 6.0,
                "maximum": 7.0

            },

            "wind_speed": {

                "maximum": 30,
                "unit": "km/h"

            },

            "sunlight_hours": {

                "minimum": 6,
                "maximum": 10

            }

        },

        "soil": {

            "preferred_texture": [

                "Loam"

            ],

            "preferred_nitrogen": "Medium",

            "preferred_organic_carbon": "Medium",

            "preferred_drainage": "Good"

        },

        "water": {

            "irrigation_type": "",

            "water_requirement": "Medium",

            "critical_growth_stage": "",

            "recommended_frequency": ""

        },

        "satellite_thresholds": {

            "ndvi": {

                "excellent": 0.80,

                "healthy": 0.65,

                "moderate": 0.45,

                "poor": 0.30

            },

            "ndwi": {

                "low_stress": 0.30,

                "moderate_stress": 0.10,

                "high_stress": 0.00

            },

            "savi": {

                "low_exposure": 0.60,

                "moderate_exposure": 0.40,

                "high_exposure": 0.20

            }

        },

        "market": {

            "keywords": [],

            "major_states": [],

            "major_countries": [],

            "harvest_season": "",

            "storage_capability": "Moderate",

            "perishability": "Medium"

        },

        "nutrition": {

            "primary_nutrients": [],

            "commercial_products": []

        },

        "common_diseases": [],

        "common_pests": [],

        "fertilizer": {

            "recommended": "",

            "npk_ratio": "",

            "organic_options": []

        },

        "yield": {

            "average_tonnes_per_hectare": 0,

            "excellent_tonnes_per_hectare": 0

        },

        "recommendations": {

            "irrigation": "",

            "fertilizer": "",

            "harvesting": "",

            "storage": ""

        },

        "summary": "",

        "references": [],

        "generated_by": "Groq",

        "version": 2

    }

    ####################################################################
    # Recursive Merge
    ####################################################################

    def merge_defaults(self, defaults, profile):

        result = deepcopy(defaults)

        for key, value in profile.items():

            if (

                key in result

                and isinstance(result[key], dict)

                and isinstance(value, dict)

            ):

                result[key] = self.merge_defaults(

                    result[key],

                    value

                )

            else:

                result[key] = value

        return result

    ####################################################################
    # Migrate Older Schemas
    ####################################################################

    def migrate(self, profile):

        ############################################################
        # vegetation_indices -> satellite_thresholds
        ############################################################

        if (

            "vegetation_indices" in profile

            and

            "satellite_thresholds" not in profile

        ):

            profile["satellite_thresholds"] = profile.pop(

                "vegetation_indices"

            )

        ############################################################
        # Older fertilizer format
        ############################################################

        if (

            "fertilizer_recommendation" in profile

            and

            "fertilizer" not in profile

        ):

            profile["fertilizer"] = {

                "recommended": profile["fertilizer_recommendation"],

                "npk_ratio": "",

                "organic_options": []

            }

        ############################################################
        # Older irrigation format
        ############################################################

        if (

            "recommended_irrigation" in profile

            and

            "water" not in profile

        ):

            profile["water"] = {

                "irrigation_type":

                    profile["recommended_irrigation"],

                "water_requirement": "Medium",

                "critical_growth_stage": "",

                "recommended_frequency": ""

            }

        return profile

    ####################################################################
    # Normalize
    ####################################################################

    def normalize(self, profile):

        ############################################################
        # Strings
        ############################################################

        profile["crop"] = profile["crop"].lower()

        ############################################################
        # Soil values
        ############################################################

        soil = profile["soil"]

        if "preferred_nitrogen" in soil:

            soil["preferred_nitrogen"] = (

                str(

                    soil["preferred_nitrogen"]

                ).title()

            )

        if "preferred_organic_carbon" in soil:

            soil["preferred_organic_carbon"] = (

                str(

                    soil["preferred_organic_carbon"]

                ).title()

            )

        return profile

    ####################################################################
    # Validate
    ####################################################################

    def validate(self, profile):

        if not isinstance(profile, dict):

            raise ValueError(

                "Crop profile must be a dictionary."

            )

        ############################################################
        # Upgrade older schema
        ############################################################

        profile = self.migrate(profile)

        ############################################################
        # Fill missing values
        ############################################################

        profile = self.merge_defaults(

            self.DEFAULT_SCHEMA,

            profile

        )

        ############################################################
        # Normalize values
        ############################################################

        profile = self.normalize(profile)

        ############################################################
        # Version
        ############################################################

        profile["version"] = 2

        return profile


##########################################################################

crop_profile_validator = CropProfileValidator()