import sqlite3

from app.config.settings import settings


class HistoricalCollector:
    """
    Retrieves historical farm records.

    Future versions can use the weather, soil, satellite,
    and market arguments for similarity search.
    """

    def collect(
        self,
        crop,
        weather=None,
        soil=None,
        satellite=None,
        market=None,
    ):

        conn = sqlite3.connect(settings.SQLITE_DB_PATH)
        conn.row_factory = sqlite3.Row

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM farm_history
            WHERE crop = ?
            ORDER BY id DESC
            LIMIT 5
            """,
            (crop,),
        )

        rows = cursor.fetchall()

        conn.close()

        return {
            "status": "success",
            "current_context": {
                "weather": weather,
                "soil": soil,
                "satellite": satellite,
                "market": market,
            },
            "records": [dict(row) for row in rows],
        }


historical_collector = HistoricalCollector()