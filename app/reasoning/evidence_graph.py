from app.models.reasoning_models import EvidenceNode


class EvidenceGraph:

    """
    Stores outputs from specialist agents.
    """

    def __init__(self):

        self.nodes = []

    ###########################################################

    def add(self, node: EvidenceNode):

        self.nodes.append(node)

    ###########################################################

    def get_agents(self):

        return [

            node.agent

            for node in self.nodes

        ]

    ###########################################################

    def get_all_risks(self):

        risks = []

        for node in self.nodes:

            risks.extend(node.risks)

        return risks

    ###########################################################

    def get_all_opportunities(self):

        ops = []

        for node in self.nodes:

            ops.extend(node.opportunities)

        return ops

    ###########################################################

    def average_confidence(self):

        if not self.nodes:

            return 0

        return sum(

            node.confidence

            for node in self.nodes

        ) / len(self.nodes)

    ###########################################################

    def to_dict(self):

        return [

            {

                "agent": node.agent,

                "analysis": node.analysis,

                "risks": node.risks,

                "opportunities": node.opportunities,

                "confidence": node.confidence,

                "metadata": node.metadata

            }

            for node in self.nodes

        ]