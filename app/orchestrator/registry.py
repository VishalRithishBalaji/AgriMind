"""
Agent Registry

Central registry for all executable AI agents.

Responsibilities
----------------
1. Provide a single source of truth for available agents.
2. Supply metadata to the Planner.
3. Allow the Executor to dynamically instantiate agents.
4. Support future capability-based agent selection.
"""

from app.agents.weather_agent import weather_agent
from app.agents.soil_agent import soil_agent
from app.agents.satellite_agent import satellite_agent
from app.agents.market_agent import market_agent
from app.agents.historical_agent import historical_agent
from app.agents.recommendation_agent import recommendation_agent

########################################################################
# Agent Instances
########################################################################

AGENT_REGISTRY = {

    "WeatherAgent": weather_agent,

    "SoilAgent": soil_agent,

    "SatelliteAgent": satellite_agent,

    "MarketAgent": market_agent,

    "HistoricalAgent": historical_agent,

    "RecommendationAgent": recommendation_agent

}


########################################################################
# Agent Metadata
########################################################################

AGENT_METADATA = {

    "WeatherAgent": {

        "type": "specialist",

        "priority": 1,

        "description":
            "Analyzes weather conditions including temperature, humidity, rainfall, and wind.",

        "input":
            "FarmContext",

        "output":
            "SpecialistOutput",

        "dependencies": [],

        "capabilities": [
            "weather",
            "rainfall",
            "humidity",
            "temperature",
            "wind"
        ]

    },

    "SoilAgent": {

        "type": "specialist",

        "priority": 2,

        "description":
            "Analyzes soil health, fertility, nutrients, moisture, and pH.",

        "input":
            "FarmContext",

        "output":
            "SpecialistOutput",

        "dependencies": [],

        "capabilities": [
            "soil",
            "nutrients",
            "fertility",
            "moisture",
            "ph"
        ]

    },

    "SatelliteAgent": {

        "type": "specialist",

        "priority": 3,

        "description":
            "Analyzes satellite imagery including NDVI, EVI, NDWI, vegetation health, water stress, and exposed soil.",

        "input":
            "FarmContext",

        "output":
            "SpecialistOutput",

        "dependencies": [],

        "capabilities": [
            "ndvi",
            "evi",
            "ndwi",
            "vegetation",
            "water stress",
            "satellite"
        ]

    },

    "MarketAgent": {

        "type": "specialist",

        "priority": 4,

        "description":
            "Analyzes crop prices, demand, trends, and selling opportunities.",

        "input":
            "FarmContext",

        "output":
            "SpecialistOutput",

        "dependencies": [],

        "capabilities": [
            "market",
            "pricing",
            "demand",
            "selling"
        ]

    },

    "HistoricalAgent": {

    "type": "specialist",

    "priority": 5,

    "description":
        "Analyzes historical farm records, previous crop cycles, irrigation history, disease outbreaks, and past recommendations.",

    "input":
        "FarmContext",

    "output":
        "SpecialistOutput",

    "dependencies": [],

    "capabilities": [

        "history",

        "yield analysis",

        "crop cycles",

        "irrigation history",

        "disease history",

        "seasonal patterns",

        "memory"

    ]

},

    "RecommendationAgent": {

    "type": "decision",

    "priority": 6,

    "description":
        "Generates the final agricultural recommendation from the collaborative reasoning output.",

    "input":
        "CollaborativeReasoning",

    "output":
        "Recommendation",

    "dependencies": [

        "WeatherAgent",

        "SoilAgent",

        "SatelliteAgent",

        "MarketAgent",

        "HistoricalAgent"

    ],

    "capabilities": [

        "recommendation",

        "decision",

        "action planning",

        "executive summary"

    ]

}

}