"""
==========================================================================
AgriMind

Historical Collector

Retrieves historical farm records and prepares context for the
Historical Agent.

Author : AgriMind Team
==========================================================================
"""

import sqlite3

from app.config.settings import settings


class HistoricalCollector:

    """
    Historical Collector

    Responsibilities
    ----------------
    1. Retrieve recent farm records for the crop.
    2. Return standardized historical data.
    3. Preserve current context for future similarity search.
    """

    ####################################################################
    # Collect Historical Records
    ####################################################################

    def collect(

        self,

        crop_profile,

        weather=None,

        soil=None,

        satellite=None,

        market=None

    ):

        ############################################################
        # Crop Name
        ############################################################

        crop = crop_profile["crop"]

        ############################################################
        # Database
        ############################################################

        conn = sqlite3.connect(

            settings.SQLITE_DB_PATH

        )

        conn.row_factory = sqlite3.Row

        cursor = conn.cursor()

        ############################################################

        cursor.execute(

            """

            SELECT *

            FROM farm_history

            WHERE LOWER(crop)=LOWER(?)

            ORDER BY id DESC

            LIMIT 5

            """,

            (crop,)

        )

        rows = cursor.fetchall()

        conn.close()

        ############################################################

        records = [

            dict(row)

            for row in rows

        ]

        ############################################################

        return {

            "source": "historical",

            "status": "success",

            "crop": crop,

            "record_count": len(records),

            "current_context": {

                "weather": weather,

                "soil": soil,

                "satellite": satellite,

                "market": market

            },

            "records": records

        }


##########################################################################

historical_collector = HistoricalCollector()