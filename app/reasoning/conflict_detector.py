class ConflictDetector:

    """
    Detect contradictions between specialists.
    """

    def detect(

        self,

        evidence_graph

    ):

        conflicts = []

        nodes = evidence_graph.nodes

        #######################################################

        for i in range(len(nodes)):

            for j in range(i + 1, len(nodes)):

                a = nodes[i]

                b = nodes[j]

                ################################################

                if (

                    "High crop water stress" in a.risks

                    and

                    "Heavy rainfall expected" in b.analysis

                ):

                    conflicts.append(

                        {

                            "agents": [

                                a.agent,

                                b.agent

                            ],

                            "reason":

                                "Satellite indicates drought while weather predicts heavy rainfall.",

                            "severity":

                                "High"

                        }

                    )

        return conflicts


conflict_detector = ConflictDetector()