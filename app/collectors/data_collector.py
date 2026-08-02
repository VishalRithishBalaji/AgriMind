"""
==========================================================================
AgriMind

Multi-Source Data Collector

Collects all external data sources using the dynamic crop profile.

Author : AgriMind Team
==========================================================================
"""

from datetime import datetime

from app.config import ai_settings

from app.collectors.weather_collector import weather_collector
from app.collectors.soil_collector import soil_collector
from app.collectors.market_collector import market_collector
from app.collectors.satellite_collector import satellite_collector
from app.collectors.historical_collector import historical_collector


class DataCollector:

    def collect(

        self,

        crop_profile,

        latitude=None,

        longitude=None

    ):

        crop = crop_profile["crop"]

        if latitude is None:
            latitude = ai_settings.DEFAULT_LATITUDE

        if longitude is None:
            longitude = ai_settings.DEFAULT_LONGITUDE

        latitude = float(latitude)
        longitude = float(longitude)

        print("=" * 70)
        print("MULTI-SOURCE DATA COLLECTION STARTED")
        print("=" * 70)

        print(f"Crop      : {crop}")
        print(f"Latitude  : {latitude}")
        print(f"Longitude : {longitude}")
        print()

        ############################################################
        # Weather
        ############################################################

        weather = weather_collector.collect(

            crop_profile=crop_profile,

            latitude=latitude,

            longitude=longitude

        )

        print("✓ Weather collected")

        ############################################################
        # Soil
        ############################################################

        soil = soil_collector.collect(

            crop_profile=crop_profile,

            latitude=latitude,

            longitude=longitude

        )

        print("✓ Soil collected")

        district = soil["location"]["district"]

        ############################################################
        # Market
        ############################################################

        market = market_collector.collect(

            crop_profile=crop_profile,

            district=district

        )

        print("✓ Market collected")

        ############################################################
        # Satellite
        ############################################################

        print("Collecting Sentinel-2 imagery...")

        satellite = satellite_collector.collect(

            crop_profile=crop_profile,

            latitude=latitude,

            longitude=longitude

        )

        if satellite["status"] == "success":

            print(

                f"✓ Satellite collected "
                f"(NDVI={satellite['vegetation']['ndvi']:.3f}, "
                f"Cloud={satellite['imagery']['cloud_cover']}%)"

            )

            satellite_summary = f"""
NDVI : {satellite['vegetation']['ndvi']}
EVI : {satellite['vegetation']['evi']}
SAVI : {satellite['vegetation']['savi']}
Vegetation Health : {satellite['vegetation']['health']}
NDWI : {satellite['water']['ndwi']}
Water Stress : {satellite['water']['stress']}
Soil Exposure : {satellite['soil']['exposure']}
"""

        else:

            print(f"⚠ Satellite skipped")

            print(f"Reason : {satellite.get('error')}")

            satellite_summary = f"""
Satellite data unavailable.

Reason:
{satellite.get('error')}
"""

        ############################################################
        # Weather Summary
        ############################################################

        weather_summary = f"""
Temperature : {weather['raw_data']['temperature']}
Humidity : {weather['raw_data']['humidity']}
Rainfall : {weather['raw_data']['rainfall']}
"""

        ############################################################
        # Soil Summary
        ############################################################

        soil_summary = f"""
pH : {soil['raw_data']['ph']}
Nitrogen : {soil['raw_data']['nitrogen']}
Organic Carbon : {soil['raw_data']['organic_carbon']}
"""

        ############################################################
        # Market Summary
        ############################################################

        market_summary = f"""
Trend : {market['raw_data'].get('Trend')}
Price : {market['raw_data'].get('Price')}
"""

        ############################################################
        # Historical
        ############################################################

        historical = historical_collector.collect(

            crop_profile=crop_profile,

            weather=weather_summary,

            soil=soil_summary,

            satellite=satellite_summary,

            market=market_summary

        )

        print("✓ Historical data collected")

        print()
        print("=" * 70)
        print("ALL SOURCES COLLECTED")
        print("=" * 70)

        return {

            "metadata": {

                "collection_time": datetime.utcnow().isoformat(),

                "crop": crop,

                "crop_profile": crop_profile,

                "location": {

                    "latitude": latitude,

                    "longitude": longitude

                }

            },

            "weather": weather,

            "soil": soil,

            "market": market,

            "satellite": satellite,

            "historical": historical

        }


##########################################################################

data_collector = DataCollector()