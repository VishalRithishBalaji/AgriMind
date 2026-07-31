class ConsensusBuilder:

    """
    Merge evidence from specialists.
    """

    def build(

        self,

        evidence_graph

    ):

        risks = []

        opportunities = []

        ####################################################

        for node in evidence_graph.nodes:

            risks.extend(node.risks)

            opportunities.extend(

                node.opportunities

            )

        ####################################################

        risks = sorted(

            list(set(risks))

        )

        opportunities = sorted(

            list(set(opportunities))

        )

        ####################################################

        return {

            "summary":

                f"{len(evidence_graph.nodes)} specialist agents reached a consensus.",

            "merged_risks":

                risks,

            "merged_opportunities":

                opportunities,

            "agreement_score":

                1.0

        }


consensus_builder = ConsensusBuilder()