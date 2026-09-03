"""Validation-only C5 one-gluon Wilson-line pilot.

Nothing exported here is a production TMD, a matched QCD operator, or a
physical process prediction.
"""

from .cuts import CutLedger, CutRelation, IntermediateStateCut, LFResolventTerm
from .distribution import DistributionalPoleEvaluator
from .identity import (
    BareWilsonSegment, CouplingConvention, FourierConvention,
    MomentumFlowConvention, PathOrdering, derived_eikonal_pole,
)
from .kernel import OneGluonPilotKernel, PilotAmplitude, PilotKernelInput
from .projectors import (
    PilotProjection, PilotProjector, boer_mulders_like_projector,
    sivers_like_projector,
)
from .serialization import deterministic_json, serialized_round_trip
from .status import C5PilotRecord, C5ResultEnvelope, PhaseBudget, ScientificStatus
from .time_reversal import AntiunitaryLinkReversal

__all__ = [
    "AntiunitaryLinkReversal", "BareWilsonSegment", "C5PilotRecord",
    "C5ResultEnvelope",
    "CouplingConvention", "CutLedger", "CutRelation",
    "DistributionalPoleEvaluator", "FourierConvention",
    "IntermediateStateCut", "LFResolventTerm", "MomentumFlowConvention",
    "OneGluonPilotKernel", "PathOrdering", "PhaseBudget",
    "PilotAmplitude", "PilotKernelInput", "PilotProjection",
    "PilotProjector", "ScientificStatus", "boer_mulders_like_projector",
    "derived_eikonal_pole", "deterministic_json", "serialized_round_trip",
    "sivers_like_projector",
]
