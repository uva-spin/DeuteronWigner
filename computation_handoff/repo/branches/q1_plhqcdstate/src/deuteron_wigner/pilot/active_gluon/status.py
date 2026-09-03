"""C6 scientific status and fail-closed Volume IV/V/VI gates."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from ...formal.diagnostics import ArchitectureError


class C6ScientificStatus(str, Enum):
    VALIDATION_ONLY = "VALIDATION_ONLY"
    UNSUBTRACTED_ACTIVE_GLUON_PILOT = "UNSUBTRACTED_ACTIVE_GLUON_PILOT"
    SOFT_OVERLAP_ACCOUNTED_ANALYTICALLY = "SOFT_OVERLAP_ACCOUNTED_ANALYTICALLY"
    RAPIDITY_CANCELLATION_BENCHMARKED = "RAPIDITY_CANCELLATION_BENCHMARKED"
    UV_MATCHING_REQUIRED = "UV_MATCHING_REQUIRED"
    PHYSICAL_TMD_SCHEME_NOT_ASSIGNED = "PHYSICAL_TMD_SCHEME_NOT_ASSIGNED"
    LINK_SHORTENING_REQUIRED = "LINK_SHORTENING_REQUIRED"
    NO_EVOLUTION_APPLIED = "NO_EVOLUTION_APPLIED"
    NO_PROCESS_MAP_APPLIED = "NO_PROCESS_MAP_APPLIED"
    WILSON_ORDER_1 = "WILSON_ORDER_1"


@dataclass(frozen=True)
class ActiveGluonResultEnvelope:
    stable_id: str
    record: dict[str, object]
    statuses: tuple[C6ScientificStatus, ...] = tuple(C6ScientificStatus)
    source_commit: str = "c4aeb380bc3c23b8dcf2fb6a4528042de598cb48"
    configuration_hash: str = "C6_ACTIVE_GLUON_ANALYTIC_V1"

    def __post_init__(self) -> None:
        missing = set(C6ScientificStatus) - set(self.statuses)
        if missing:
            raise ArchitectureError("C6.STATUS.1", "active-gluon record lacks unresolved status", expected=tuple(item.value for item in C6ScientificStatus), received=tuple(item.value for item in missing))

    def require_volume_iv(self, **gates: bool) -> None:
        required = (
            "complete_helicity_matrices", "correlated_pn_members",
            "phase_soft_covariance", "partonic_nuclear_subtraction",
            "matched_nuclear_operators_currents",
        )
        self._require("Volume IV", required, gates)

    def require_volume_v(self, **gates: bool) -> None:
        required = (
            "closed_operator_basis", "lf_qcd_matching", "uv_renormalization",
            "rapidity_soft_scheme", "link_shortening", "rank_evolution",
            "process_link_color_glauber", "hard_and_fixed_order_subtraction",
        )
        self._require("Volume V", required, gates)

    def require_volume_vi(self, **gates: bool) -> None:
        required = (
            "shared_parameter_ownership", "typed_likelihood",
            "covariance_discrepancy", "calibration_holdout",
            "posterior_member_store",
        )
        self._require("Volume VI", required, gates)

    @staticmethod
    def _require(volume: str, required: tuple[str, ...], gates: dict[str, bool]) -> None:
        for name in required:
            if not gates.get(name, False):
                raise ArchitectureError("C6.STATUS.1", f"{volume} gate is closed", expected=name, received=False)

    def require_production(self) -> None:
        raise ArchitectureError("C6.STATUS.1", "C6 result cannot enter production", expected="validation-only isolated graph", received=self.stable_id)

    def to_dict(self) -> dict[str, object]:
        return {
            "stable_id": self.stable_id, "record": self.record,
            "statuses": [item.value for item in self.statuses],
            "source_commit": self.source_commit,
            "configuration_hash": self.configuration_hash,
        }
