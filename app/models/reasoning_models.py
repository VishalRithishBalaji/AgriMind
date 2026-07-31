from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class EvidenceNode:

    agent: str

    analysis: str

    risks: List[str]

    opportunities: List[str]

    confidence: float

    metadata: Dict = field(default_factory=dict)


@dataclass
class Conflict:

    agents: List[str]

    reason: str

    severity: str


@dataclass
class Consensus:

    summary: str

    merged_risks: List[str]

    merged_opportunities: List[str]

    agreement_score: float

    confidence: float


@dataclass
class ReasoningResult:

    evidence_count: int

    conflicts: List[Conflict]

    consensus: Consensus

    overall_confidence: float