from pprint import pprint

from app.agents.reasoning_agent import reasoning_agent


weather = {

    "temperature":29.5,

    "humidity":58,

    "rainfall":0

}

soil = {

    "ph":6.5,

    "nitrogen":"Medium",

    "organic_carbon":"High"

}

market = {

    "price":2350,

    "trend":"Increasing"

}

memory = """

Rice

Hot and Dry

Medium Nitrogen

Increasing Market

Recommendation:

Irrigate every 3 days

Apply Nitrogen Fertilizer

Yield increased 18%

"""

result = reasoning_agent.execute(

    weather,

    soil,

    market,

    memory

)

pprint(result)