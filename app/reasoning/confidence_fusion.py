class ConfidenceFusion:

    """
    Weighted confidence computation.
    """

    WEIGHTS = {

        "WeatherAgent": 0.25,

        "SoilAgent": 0.25,

        "SatelliteAgent": 0.35,

        "MarketAgent": 0.15

    }

    ###########################################################

    def compute(

        self,

        evidence_graph

    ):

        score = 0

        total = 0

        #######################################################

        for node in evidence_graph.nodes:

            weight = self.WEIGHTS.get(

                node.agent,

                0.25

            )

            score += (

                node.confidence

                * weight

            )

            total += weight

        #######################################################

        if total == 0:

            return 0

        return round(

            score / total,

            2

        )


confidence_fusion = ConfidenceFusion()