"""Machine-readable provenance and validity contracts for model components."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Mapping


class EvidenceClass(str, Enum):
    EXACT = "exact_constraint"
    PHENOMENOLOGY = "phenomenology_constrained"
    LATTICE = "lattice_informed"
    MODEL = "model_dependent"
    UNCONSTRAINED = "unconstrained_parameterization"


class Mechanism(str, Enum):
    NUCLEON_IMPULSE = "nucleon_impulse"
    OFF_SHELL = "off_shell"
    COHERENT = "coherent_shadowing"
    MESON_EXCHANGE = "meson_exchange"
    NON_NUCLEONIC = "non_nucleonic"
    ISOSPIN_BREAKING = "isospin_breaking"


@dataclass(frozen=True)
class ValidityDomain:
    x_min: float
    x_max: float
    q_min_gev: float
    q_max_gev: float
    k_max_gev: float | None = None
    process: str = "universal_T_even"

    def __post_init__(self) -> None:
        if not 0.0 <= self.x_min < self.x_max <= 1.0:
            raise ValueError("invalid x validity range")
        if self.q_min_gev <= 0.0 or self.q_max_gev < self.q_min_gev:
            raise ValueError("invalid Q validity range")
        if self.k_max_gev is not None and self.k_max_gev <= 0.0:
            raise ValueError("k maximum must be positive")

    def contains(self, *, x: float, q_gev: float, k_gev: float | None = None) -> bool:
        if not self.x_min <= x <= self.x_max:
            return False
        if not self.q_min_gev <= q_gev <= self.q_max_gev:
            return False
        return not (
            k_gev is not None
            and self.k_max_gev is not None
            and k_gev > self.k_max_gev
        )


@dataclass(frozen=True)
class ComponentProvenance:
    name: str
    evidence: EvidenceClass
    mechanism: Mechanism
    sources: tuple[str, ...]
    assumptions: tuple[str, ...]
    validity: ValidityDomain
    uncertainty_kind: str
    replaceable_interface: str

    def __post_init__(self) -> None:
        if not self.name or not self.sources:
            raise ValueError("component provenance requires a name and source")
        if not self.uncertainty_kind or not self.replaceable_interface:
            raise ValueError("uncertainty and replacement interface are required")


@dataclass(frozen=True)
class PredictionTrace:
    """Trace a predicted quantity through operator, nuclear, and mechanism layers."""

    species: str
    flavor: int
    operator_projection: str
    target_channel: str
    gauge_link: str
    components: tuple[ComponentProvenance, ...]

    def evidence_summary(self) -> Mapping[str, int]:
        return {
            evidence.value: sum(
                component.evidence == evidence for component in self.components
            )
            for evidence in EvidenceClass
        }

    def require_no_hidden_completion(self) -> None:
        if not self.components:
            raise ValueError("prediction has no provenance components")
        for component in self.components:
            if component.evidence == EvidenceClass.UNCONSTRAINED:
                if "parameter" not in component.uncertainty_kind.lower():
                    raise ValueError(
                        f"unconstrained component {component.name} lacks "
                        "an explicit parameter uncertainty"
                    )
