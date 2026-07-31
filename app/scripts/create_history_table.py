import sqlite3

conn = sqlite3.connect("app/database/agrimind.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS farm_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    season TEXT,

    crop TEXT,

    yield REAL,

    rainfall REAL,

    soil_moisture REAL,

    ndvi REAL,

    disease TEXT,

    irrigation TEXT,

    recommendation TEXT,

    outcome TEXT

)
""")

conn.commit()
conn.close()

print("farm_history table created successfully.")