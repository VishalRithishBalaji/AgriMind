from datetime import datetime

from app.config import ai_settings

from app.collectors.weather_collector import weather_collector
from app.collectors.soil_collector import soil_collector
from app.collectors.market_collector import market_collector
from app.collectors.satellite_collector import satellite_collector
from app.collectors.historical_collector import historical_collector


class DataCollector:

    ####################################################################
    # Collect All Sources
    ####################################################################

    def collect(

        self,

        crop="rice",

        latitude=None,

        longitude=None

    ):

        ################################################################
        # Default Coordinates
        ################################################################

        if latitude is None:

            latitude = ai_settings.DEFAULT_LATITUDE

        if longitude is None:

            longitude = ai_settings.DEFAULT_LONGITUDE

        latitude = float(latitude)
        longitude = float(longitude)

        ################################################################

        print("=" * 70)
        print("MULTI-SOURCE DATA COLLECTION STARTED")
        print("=" * 70)

        print(f"Crop      : {crop}")
        print(f"Latitude  : {latitude}")
        print(f"Longitude : {longitude}")

        print()

        ################################################################
        # Weather
        ################################################################

        weather = weather_collector.collect(

            crop=crop,

            latitude=latitude,

            longitude=longitude

        )

        print("✓ Weather collected")

        ################################################################
        # Soil
        ################################################################

        soil = soil_collector.collect(

            latitude=latitude,

            longitude=longitude

        )

        print("✓ Soil collected")

        district = soil["location"]["district"]

        ################################################################
        # Market
        ################################################################

        market = market_collector.collect(

            crop=crop,

            district=district

        )

        print("✓ Market collected")

        ################################################################
        # Satellite
        ################################################################

        print("Collecting Sentinel-2 imagery...")

        satellite = satellite_collector.collect(

            latitude=latitude,

            longitude=longitude

        )

        if satellite["status"] == "success":

            print(

                "✓ Satellite collected "

                f"(NDVI={satellite['vegetation']['ndvi']:.3f}, "

                f"Cloud={satellite['imagery']['cloud_cover']}%)"

            )

        else:

            print(

                f"⚠ Satellite skipped: "

                f"{satellite['error']}"

            )
        
        ################################################################
        # Historical Memory
        ################################################################

        historical = historical_collector.collect(

            crop=crop,

            weather=f"""

Temperature : {weather['raw_data']['temperature']}

Humidity : {weather['raw_data']['humidity']}

Rainfall : {weather['raw_data']['rainfall']}

""",

            soil=f"""

pH : {soil['raw_data']['ph']}

Nitrogen : {soil['raw_data']['nitrogen']}

Organic Carbon : {soil['raw_data']['organic_carbon']}

""",

            market=f"""

Trend : {market['raw_data']['Trend']}

Price : {market['raw_data']['Price']}

"""

        )

        print("✓ Historical data collected")

        ################################################################

        print()

        print("=" * 70)
        print("ALL SOURCES COLLECTED")
        print("=" * 70)

        ################################################################

        return {

            "metadata": {

                "collection_time":

                    datetime.utcnow().isoformat(),

                "crop":

                    crop,

                "location": {

                    "latitude": latitude,

                    "longitude": longitude

                }

            },

            "weather":

                weather,

            "soil":

                soil,

            "market":

                market,

            "satellite":

                satellite,

            "historical":

                historical

        }


########################################################################

data_collector = DataCollector()