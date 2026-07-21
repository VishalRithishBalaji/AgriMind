import json

from app.memory.chroma_store import chroma_store


class MemoryManager:

    def load_cases(
        self,
        json_path
    ):

        with open(
            json_path,
            "r",
            encoding="utf-8"
        ) as f:

            cases = json.load(f)

        for case in cases:

            document = f"""
Crop: {case['crop']}
District: {case['district']}
Weather: {case['weather']}
Soil: {case['soil']}
Market: {case['market']}
Recommendation: {case['recommendation']}
Outcome: {case['outcome']}
"""

            metadata = {

                "crop": case["crop"],

                "district": case["district"]

            }

            chroma_store.add_case(

                case["id"],

                document,

                metadata

            )

    def retrieve(
        self,
        crop,
        weather,
        soil,
        market,
        top_k=3
    ):

        query = f"""
Crop: {crop}
Weather: {weather}
Soil: {soil}
Market: {market}
"""

        return chroma_store.search(

            query,

            top_k

        )


memory_manager = MemoryManager()