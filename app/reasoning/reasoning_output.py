from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class CollaborativeReasoning:

    summary: str

    consensus: str

    merged_risks: List[str]

    merged_opportunities: List[str]

    conflicts: List[Dict]

    confidence: float

    evidence: List[Dict] = field(

        default_factory=list

    )

    metadata: Dict = field(

        default_factory=dict

    )