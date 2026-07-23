"""
Agent Registry

Every executable agent is registered here.

The planner NEVER imports agents directly.

The executor loads agents from this registry.

Adding a new agent requires only

1. Create the agent

2. Register it here

The planner will automatically be able to use it.
"""

from app.agents.weather_agent import weather_agent
from app.agents.soil_agent import soil_agent
from app.agents.market_agent import market_agent
from app.agents.satellite_agent import satellite_agent
from app.agents.recommendation_agent import recommendation_agent


AGENT_REGISTRY = {

    "WeatherAgent": weather_agent,

    "SoilAgent": soil_agent,

    "SatelliteAgent": satellite_agent,

    "MarketAgent": market_agent,

    "RecommendationAgent": recommendation_agent

}


AGENT_METADATA = {

    "WeatherAgent": {

        "description":
            "Weather forecasting and environmental analysis.",

        "input":
            "Farm Context",

        "output":
            "Weather assessment"

    },

    "SoilAgent": {

        "description":
            "Soil nutrient and fertility analysis.",

        "input":
            "Farm Context",

        "output":
            "Soil assessment"

    },

    "SatelliteAgent": {

        "description":
            "Satellite vegetation and water stress analysis.",

        "input":
            "Farm Context",

        "output":
            "Vegetation assessment"

    },

    "MarketAgent": {

        "description":
            "Crop market analysis.",

        "input":
            "Farm Context",

        "output":
            "Market assessment"

    },

    "RecommendationAgent": {

        "description":
            "Generate final recommendation.",

        "input":
            "Outputs of previous agents",

        "output":
            "Final recommendation"

    }

}