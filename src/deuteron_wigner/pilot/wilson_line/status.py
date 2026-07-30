"""Fail-closed C5 scientific status, phase budget, and downstream gates."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum

from ...formal.diagnostics import ArchitectureError


class ScientificStatus(str, Enum):
    VALIDATION_ONLY = "VALIDATION_ONLY"
    UNSUBTRACTED_REGULATED_PILOT = "UNSUBTRACTED_REGULATED_PILOT"
    LINK_SHORTENING_REQUIRED = "LINK_SHORTENING_REQUIRED"
    UV_MATCHING_REQUIRED = "UV_MATCHING_REQUIRED"
    RAPIDITY_SOFT_MATCHING_REQUIRED = "RAPIDITY_SOFT_MATCHING_REQUIRED"
    PHYSICAL_PROCESS_MAP_NOT_APPLIED = "PHYSICAL_PROCESS_MAP_NOT_APPLIED"
    NO_EVOLUTION_APPLIED = "NO_EVOLUTION_APPLIED"
    WILSON_ORDER_1 = "WILSON_ORDER_1"


UNRESOLVED = "UNRESOLVED_NOT_ZERO"


@dataclass(frozen=True)
class C5PilotRecord:
    """Complete identity carried by an authoritative serialized pilot value."""

    state_id: str
    member_id: str
    recoil_id: str
    overlap_id: str
    operator_id: str
    path_id: str
    representation: str
    wilson_order: int
    pole_id: str
    intermediate_state_id: str
    cut_ledger_id: str
    oam_helicity_blocks: tuple[str, ...]
    projector_id: str
    regulator_identity: str
    numerical_tolerances: tuple[tuple[str, float], ...]
    value: complex


@dataclass(frozen=True)
class PhaseBudget:
    unsubtracted_hadronic_or_collinear_phase: float
    soft_overlap_contribution: str = UNRESOLVED
    rapidity_counterterm_contribution: str = UNRESOLVED
    uv_matching_contribution: str = UNRESOLVED
    glauber_or_process_contribution: str = UNRESOLVED
    unresolved_remainder: str = UNRESOLVED

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class C5ResultEnvelope:
    stable_id: str
    payload: dict[str, object]
    phase_budget: PhaseBudget
    statuses: tuple[ScientificStatus, ...] = tuple(ScientificStatus)
    source_commit: str = "62125f0857e597e8f9548f279ae70b1634764a24"
    configuration_hash: str = "C5_ANALYTIC_V1"

    def __post_init__(self) -> None:
        missing = set(ScientificStatus) - set(self.statuses)
        if missing:
            raise ArchitectureError("C5.STATUS.1", "C5 output is missing unresolved scientific status", expected=tuple(x.value for x in ScientificStatus), received=tuple(x.value for x in missing))

    def require_volume_iv(self, *, helicity_matrices=False, correlated_pn=False, phase_soft_covariance=False, separated_rescattering=False) -> None:
        gates = (
            ("complete_helicity_matrices", helicity_matrices),
            ("correlated_proton_neutron_members", correlated_pn),
            ("phase_soft_and_covariance", phase_soft_covariance),
            ("partonic_vs_nuclear_rescattering", separated_rescattering),
        )
        for name, passed in gates:
            if not passed:
                raise ArchitectureError("C5.STATUS.2", "Volume IV nuclear entry gate is closed", expected=name, received=False)

    def require_volume_v(self, *, closed_basis=False, lf_qcd_matching=False, completed_matching=False, scheme_evolution=False, process_identity=False) -> None:
        gates = (
            ("closed_regulated_operator_basis", closed_basis),
            ("lf_to_qcd_matching_map", lf_qcd_matching),
            ("uv_rapidity_soft_link_shortening", completed_matching),
            ("scheme_and_evolution_identity", scheme_evolution),
            ("process_link_color_glauber_identity", process_identity),
        )
        for name, passed in gates:
            if not passed:
                raise ArchitectureError("C5.STATUS.2", "Volume V matching/evolution gate is closed", expected=name, received=False)

    def require_production(self) -> None:
        raise ArchitectureError("C5.STATUS.1", "validation-only result cannot enter production", expected="excluded from production root and 216-route registry", received=self.stable_id)

    def to_dict(self) -> dict[str, object]:
        return {
            "stable_id": self.stable_id, "payload": self.payload,
            "phase_budget": self.phase_budget.to_dict(),
            "statuses": [item.value for item in self.statuses],
            "source_commit": self.source_commit,
            "configuration_hash": self.configuration_hash,
        }
