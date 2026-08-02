"""
==========================================================================
AgriMind

Crop Profile Repository

Persistent storage for crop knowledge.

Stores profiles in

1. SQLite
2. JSON Cache

Every loaded profile is automatically

• validated
• repaired
• upgraded
• re-saved if necessary

Author : AgriMind Team
==========================================================================
"""

import json
import sqlite3

from pathlib import Path
from datetime import datetime

from app.knowledge.crop_profile_validator import (
    crop_profile_validator
)


class CropProfileRepository:

    ####################################################################
    # Constructor
    ####################################################################

    def __init__(self):

        self.db_path = "app/database/crop_profiles.db"

        self.json_dir = Path(
            "app/knowledge/crop_profiles"
        )

        self.json_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.initialize()

    ####################################################################
    # Database
    ####################################################################

    def initialize(self):

        conn = sqlite3.connect(self.db_path)

        cursor = conn.cursor()

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS crop_profiles(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            crop TEXT UNIQUE,

            profile_json TEXT,

            source TEXT,

            confidence REAL,

            created_at TEXT,

            updated_at TEXT

        )

        """)

        conn.commit()

        conn.close()

    ####################################################################
    # Exists
    ####################################################################

    def exists(self, crop):

        conn = sqlite3.connect(self.db_path)

        cursor = conn.cursor()

        cursor.execute(

            "SELECT 1 FROM crop_profiles WHERE crop=?",

            (crop.lower(),)

        )

        result = cursor.fetchone()

        conn.close()

        return result is not None

    ####################################################################
    # Load JSON Cache
    ####################################################################

    def load_json(self, crop):

        json_file = self.json_dir / f"{crop.lower()}.json"

        if not json_file.exists():

            return None

        with open(

            json_file,

            "r",

            encoding="utf-8"

        ) as f:

            profile = json.load(f)

        return profile

    ####################################################################
    # Load SQLite
    ####################################################################

    def load_sqlite(self, crop):

        conn = sqlite3.connect(self.db_path)

        cursor = conn.cursor()

        cursor.execute(

            "SELECT profile_json FROM crop_profiles WHERE crop=?",

            (crop.lower(),)

        )

        row = cursor.fetchone()

        conn.close()

        if row is None:

            return None

        return json.loads(row[0])

    ####################################################################
    # Load
    ####################################################################

    def load(self, crop):

        ############################################################
        # JSON Cache First
        ############################################################

        profile = self.load_json(crop)

        ############################################################
        # SQLite Fallback
        ############################################################

        if profile is None:

            profile = self.load_sqlite(crop)

        if profile is None:

            return None

        ############################################################
        # Validate & Upgrade
        ############################################################

        repaired = crop_profile_validator.validate(profile)

        ############################################################
        # Auto Save Upgraded Profile
        ############################################################

        if repaired != profile:

            self.save(

                repaired,

                source="AutoMigration"

            )

        return repaired

    ####################################################################
    # Save
    ####################################################################

    def save(

        self,

        profile,

        source="Groq",

        confidence=1.0

    ):

        ############################################################
        # Validate Before Saving
        ############################################################

        profile = crop_profile_validator.validate(profile)

        crop = profile["crop"].lower()

        profile_json = json.dumps(

            profile,

            indent=4,

            ensure_ascii=False

        )

        timestamp = datetime.utcnow().isoformat()

        ############################################################
        # SQLite
        ############################################################

        conn = sqlite3.connect(self.db_path)

        cursor = conn.cursor()

        cursor.execute("""

        INSERT OR REPLACE INTO crop_profiles(

            crop,

            profile_json,

            source,

            confidence,

            created_at,

            updated_at

        )

        VALUES(

            ?, ?, ?, ?, ?, ?

        )

        """, (

            crop,

            profile_json,

            source,

            confidence,

            timestamp,

            timestamp

        ))

        conn.commit()

        conn.close()

        ############################################################
        # JSON Cache
        ############################################################

        json_file = self.json_dir / f"{crop}.json"

        with open(

            json_file,

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                profile,

                f,

                indent=4,

                ensure_ascii=False

            )

        return profile

    ####################################################################
    # Update
    ####################################################################

    def update(self, profile):

        return self.save(

            profile,

            source="Update"

        )

    ####################################################################
    # Delete
    ####################################################################

    def delete(self, crop):

        conn = sqlite3.connect(self.db_path)

        cursor = conn.cursor()

        cursor.execute(

            "DELETE FROM crop_profiles WHERE crop=?",

            (crop.lower(),)

        )

        conn.commit()

        conn.close()

        json_file = self.json_dir / f"{crop.lower()}.json"

        if json_file.exists():

            json_file.unlink()

    ####################################################################
    # List Crops
    ####################################################################

    def list_crops(self):

        conn = sqlite3.connect(self.db_path)

        cursor = conn.cursor()

        cursor.execute(

            "SELECT crop FROM crop_profiles ORDER BY crop"

        )

        rows = cursor.fetchall()

        conn.close()

        return [

            row[0]

            for row in rows

        ]


##########################################################################

crop_profile_repository = CropProfileRepository()