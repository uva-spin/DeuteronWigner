"""Typed independent uncertainty axes and sourced joint-probability contract."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Mapping

import numpy as np


class UncertaintyAxis(str, Enum):
    WAVE_FUNCTION = "wave_function"
    INTERNAL_QUADRATURE = "internal_quadrature"
    EXTERNAL_GRID = "external_grid"
    TRANSFORM = "transform"
    PDF_TMD_FIT = "pdf_tmd_fit"
    EVOLUTION_PROFILE = "evolution_profile"
    NUCLEAR_MECHANISM = "nuclear_mechanism"


class EnsembleKind(str, Enum):
    MONTE_CARLO = "monte_carlo_replicas"
    HESSIAN = "hessian_eigenvectors"
    CORRELATED_SCENARIOS = "correlated_named_scenarios"
    SENSITIVITY_ENVELOPE = "nonprobabilistic_sensitivity_envelope"
    CONVERGENCE_SEQUENCE = "numerical_convergence_sequence"


@dataclass(frozen=True)
class UncertaintyEnsemble:
    name: str
    axis: UncertaintyAxis
    kind: EnsembleKind
    member_ids: tuple[str, ...]
    source: str
    central_member: str
    correlated_dimensions: tuple[str, ...]

    def __post_init__(self) -> None:
        if (
            not self.name
            or not self.source
            or not self.member_ids
            or not self.correlated_dimensions
        ):
            raise ValueError("uncertainty ensemble metadata is incomplete")
        if len(set(self.member_ids)) != len(self.member_ids):
            raise ValueError("uncertainty member IDs must be unique")
        if self.central_member not in self.member_ids:
            raise ValueError("central member must belong to the ensemble")


@dataclass(frozen=True)
class JointProbabilityInput:
    axes: tuple[UncertaintyAxis, ...]
    covariance: np.ndarray
    source: str
    parameter_labels: tuple[str, ...]

    def __post_init__(self) -> None:
        covariance = np.asarray(self.covariance, dtype=float)
        if not self.source or not self.axes or not self.parameter_labels:
            raise ValueError("joint probability requires axes, labels, and source")
        if len(set(self.axes)) != len(self.axes):
            raise ValueError("joint probability axes must be unique")
        n = len(self.parameter_labels)
        if (
            covariance.shape != (n, n)
            or not np.all(np.isfinite(covariance))
            or not np.allclose(covariance, covariance.T, atol=1e-13, rtol=0)
            or np.linalg.eigvalsh(covariance)[0] < -1e-12
        ):
            raise ValueError("joint covariance must be finite, symmetric, and PSD")
        object.__setattr__(self, "covariance", covariance)


@dataclass(frozen=True)
class SeparatedUncertaintyLedger:
    ensembles: Mapping[str, UncertaintyEnsemble]

    def __post_init__(self) -> None:
        if not self.ensembles:
            raise ValueError("uncertainty ledger cannot be empty")
        for name, ensemble in self.ensembles.items():
            if name != ensemble.name:
                raise ValueError("uncertainty ledger key must equal ensemble name")

    @property
    def axes(self) -> frozenset[UncertaintyAxis]:
        return frozenset(item.axis for item in self.ensembles.values())

    def require_all_axes(self) -> None:
        missing = set(UncertaintyAxis) - set(self.axes)
        if missing:
            raise ValueError(
                f"uncertainty ledger is missing axes: "
                f"{sorted(axis.value for axis in missing)}"
            )

    def joint_covariance(
        self, joint: JointProbabilityInput | None = None
    ) -> np.ndarray:
        if joint is None:
            raise ValueError(
                "independent uncertainty axes cannot be collapsed into a "
                "joint covariance without a sourced joint probability"
            )
        if not set(joint.axes) <= set(self.axes):
            raise ValueError("joint probability references an unavailable axis")
        return joint.covariance.copy()

