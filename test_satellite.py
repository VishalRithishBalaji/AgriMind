from pprint import pprint

from app.tools.satellite_tool import satellite_tool

result = satellite_tool.execute(

    latitude=11.0168,

    longitude=76.9558

)

pprint(result)