import json

from dataclasses import asdict

from app.models.reasoning_models import EvidenceNode

from app.reasoning.evidence_graph import EvidenceGraph

from app.reasoning.conflict_detector import conflict_detector

from app.reasoning.consensus import consensus_builder

from app.reasoning.confidence_fusion import confidence_fusion

from app.reasoning.reasoning_output import CollaborativeReasoning

from app.prompts.collaborative_prompt import (

    SYSTEM_PROMPT,

    build_prompt

)

from app.utils.gemini_client import gemini_client


class CollaborativeEngine:

    """
    Multi-Agent Collaborative Reasoning Engine
    """

    ###########################################################

    def build_graph(

        self,

        specialist_outputs

    ):

        graph = EvidenceGraph()

        #######################################################

        for output in specialist_outputs.values():

            node = EvidenceNode(

                agent=output["agent"],

                analysis=output["analysis"],

                risks=output.get(

                    "risks",

                    []

                ),

                opportunities=output.get(

                    "opportunities",

                    []

                ),

                confidence=output.get(

                    "confidence",

                    0.5

                ),

                metadata=output.get(

                    "metadata",

                    {}

                )

            )

            graph.add(node)

        #######################################################

        return graph

    ###########################################################

    def collaborative_reasoning(

        self,

        context,

        specialist_outputs

    ):

        #######################################################
        # Step 1
        #######################################################

        graph = self.build_graph(

            specialist_outputs

        )

        #######################################################
        # Step 2
        #######################################################

        conflicts = conflict_detector.detect(

            graph

        )

        #######################################################
        # Step 3
        #######################################################

        consensus = consensus_builder.build(

            graph

        )

        #######################################################
        # Step 4
        #######################################################

        confidence = confidence_fusion.compute(

            graph

        )

        #######################################################
        # Step 5
        #######################################################

        prompt = build_prompt(

            context=context,

            evidence=graph.to_dict()

        )

        #######################################################
        # Step 6
        #######################################################

        response = gemini_client.generate(

            system_prompt=SYSTEM_PROMPT,

            prompt=prompt,

            temperature=0.2

        )

        #######################################################
        # Step 7
        #######################################################

        try:

            reasoning = json.loads(response)

        except Exception:

            reasoning = {

                "summary":

                    consensus["summary"],

                "consensus":

                    "Collaborative reasoning fallback.",

                "merged_risks":

                    consensus["merged_risks"],

                "merged_opportunities":

                    consensus["merged_opportunities"],

                "conflicts":

                    conflicts,

                "confidence":

                    confidence

            }

        #######################################################
        # Step 8
        #######################################################

        return CollaborativeReasoning(

            summary=reasoning["summary"],

            consensus=reasoning["consensus"],

            merged_risks=reasoning["merged_risks"],

            merged_opportunities=

                reasoning["merged_opportunities"],

            conflicts=reasoning["conflicts"],

            confidence=reasoning["confidence"],

            evidence=graph.to_dict(),

            metadata={

                "agents":

                    graph.get_agents(),

                "agent_count":

                    len(graph.nodes)

            }

        )


collaborative_engine = CollaborativeEngine()