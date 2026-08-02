"""
==========================================================================
AgriMind

Executive Decision Intelligence Models

Module 5F

Shared dataclasses used by the Executive Intelligence Engine.

Author : AgriMind Team
==========================================================================
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any


##########################################################################
# Executive Priority
##########################################################################

@dataclass
class ExecutivePriority:

    issue: str

    severity: str

    urgency: str

    owner: str

    action: str


##########################################################################
# Impact Assessment
##########################################################################

@dataclass
class ExecutiveImpact:

    agronomic_impact: str

    economic_impact: str

    environmental_impact: str

    operational_impact: str

    expected_benefit: str

    yield_risk: str

    profitability: str


##########################################################################
# Executive Summary
##########################################################################

@dataclass
class ExecutiveSummary:

    executive_summary: str

    business_summary: str

    technical_summary: str

    justification: str


##########################################################################
# Executive Decision
##########################################################################

@dataclass
class ExecutiveDecision:

    crop: str

    decision: str

    priority: str

    urgency: str

    risk_level: str

    confidence: float

    action_order: List[str] = field(default_factory=list)

    priorities: List[ExecutivePriority] = field(default_factory=list)

    impact: ExecutiveImpact = None

    summary: ExecutiveSummary = None

    supporting_evidence: List[str] = field(default_factory=list)

    metadata: Dict[str, Any] = field(default_factory=dict)


##########################################################################
# Executive Report
##########################################################################

@dataclass
class ExecutiveReport:

    decision: ExecutiveDecision

    generated_by: str = "ExecutiveDecisionEngine"

    version: str = "1.0"

    status: str = "completed"