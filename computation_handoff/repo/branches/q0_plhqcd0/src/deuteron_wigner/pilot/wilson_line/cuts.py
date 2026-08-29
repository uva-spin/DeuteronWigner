"""Typed light-front denominators and physical cut provenance."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import Enum

from ...formal.diagnostics import ArchitectureError


class SpectrumRule(str, Enum):
    DISCRETE_OFF_SHELL = "DISCRETE_OFF_SHELL"
    DECLARED_CONTINUUM_DENSITY = "DECLARED_CONTINUUM_DENSITY"
    DECLARED_FINITE_VOLUME_DELTA = "DECLARED_FINITE_VOLUME_DELTA"


class CutKind(str, Enum):
    EIKONAL = "EIKONAL"
    LF_ENERGY = "LF_ENERGY"


class CutRelation(str, Enum):
    DISTINCT = "DISTINCT"
    EQUIVALENT_COUNT_ONCE = "EQUIVALENT_COUNT_ONCE"
    SUBTRACTED = "SUBTRACTED"


@dataclass(frozen=True)
class LFResolventTerm:
    initial_state_id: str
    intermediate_state_id: str
    initial_lf_energy: float
    intermediate_lf_energy: float
    pole_sign: int
    source_vertex_id: str
    target_operator_id: str
    cut_support_id: str
    spectrum_rule: SpectrumRule
    regulator_identity: str

    def __post_init__(self) -> None:
        if self.pole_sign not in (-1, 1):
            raise ArchitectureError("C5.CUT.1", "invalid LF resolvent pole sign", expected="+/-1", received=self.pole_sign)

    @property
    def energy_difference(self) -> float:
        return self.initial_lf_energy - self.intermediate_lf_energy

    def absorptive_weight(self, spectral_weight: float = 1.0) -> float:
        if self.spectrum_rule == SpectrumRule.DISCRETE_OFF_SHELL:
            return 0.0
        return -self.pole_sign * spectral_weight

    def to_dict(self) -> dict[str, object]:
        value = asdict(self)
        value["spectrum_rule"] = self.spectrum_rule.value
        return value


@dataclass(frozen=True)
class IntermediateStateCut:
    stable_id: str
    kind: CutKind
    physical_support_id: str
    source_denominator_id: str
    enabled: bool
    spectral_weight: float


@dataclass(frozen=True)
class CutLedgerEntry:
    cut: IntermediateStateCut
    relation: CutRelation
    equivalent_to: str | None = None


class CutLedger:
    def __init__(self) -> None:
        self._entries: list[CutLedgerEntry] = []

    def add(self, cut: IntermediateStateCut, relation: CutRelation = CutRelation.DISTINCT, equivalent_to: str | None = None) -> None:
        same_support = [item for item in self._entries if item.cut.physical_support_id == cut.physical_support_id and item.cut.enabled and cut.enabled]
        if same_support and relation == CutRelation.DISTINCT:
            raise ArchitectureError("C5.CUT.2", "duplicate physical cut requires equivalence or subtraction record", expected="EQUIVALENT_COUNT_ONCE|SUBTRACTED", received=cut.physical_support_id)
        if relation != CutRelation.DISTINCT and not equivalent_to:
            raise ArchitectureError("C5.CUT.2", "cut relation lacks referenced contribution", expected="equivalent_to stable id", received=None)
        self._entries.append(CutLedgerEntry(cut, relation, equivalent_to))

    def active_weight(self) -> float:
        counted: set[str] = set()
        total = 0.0
        for item in self._entries:
            cut = item.cut
            if not cut.enabled or item.relation == CutRelation.SUBTRACTED:
                continue
            if item.relation == CutRelation.EQUIVALENT_COUNT_ONCE and cut.physical_support_id in counted:
                continue
            total += cut.spectral_weight
            counted.add(cut.physical_support_id)
        return total

    def to_dict(self) -> dict[str, object]:
        return {
            "entries": [
                {
                    "cut": {**asdict(item.cut), "kind": item.cut.kind.value},
                    "relation": item.relation.value,
                    "equivalent_to": item.equivalent_to,
                }
                for item in self._entries
            ],
            "active_weight": self.active_weight(),
        }
