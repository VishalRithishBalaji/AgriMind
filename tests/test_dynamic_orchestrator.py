from pprint import pprint

from app.orchestrator.dynamic_orchestrator import dynamic_orchestrator

result = dynamic_orchestrator.run(
    user_query="Should I irrigate my rice crop today?",
    crop="rice",
    latitude=11.0168,
    longitude=76.9558
)

pprint(result)