"""Factorized regulator-trajectory and holdout records."""

from __future__ import annotations

from dataclasses import dataclass

from .identity import (
    AvailabilityStatus,
    C35IdentityEnvelope,
    ProofSet,
    require_identity,
)
from .serialization import ContentAddressed


@dataclass(frozen=True)
class SoftTrajectoryAxis(ContentAddressed):
    identity: C35IdentityEnvelope
    axis_id: str
    parameter_name: str
    values: tuple[str, ...]
    fixed_parameter_values: tuple[tuple[str, str], ...]
    regulator_role: str
    ordered_limit: int
    holdout_indices: tuple[int, ...]
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.availability is AvailabilityStatus.AVAILABLE:
            if len(self.values) < 2 or not self.fixed_parameter_values or not self.holdout_indices:
                raise ValueError("available trajectory axis needs variation, fixed context, and holdouts")
            if any(index < 0 or index >= len(self.values) for index in self.holdout_indices):
                raise ValueError("trajectory holdout index is out of range")
            if not self.proof.closed:
                raise ValueError("available trajectory axis has open proof obligations")
        elif self.values or self.fixed_parameter_values or self.holdout_indices:
            raise ValueError("unavailable trajectory axis must be empty-not-zero")


@dataclass(frozen=True)
class SoftTrajectoryFamily(ContentAddressed):
    identity: C35IdentityEnvelope
    family_id: str
    axis_ids: tuple[str, ...]
    varied_axis_id: str | None
    fixed_axis_ids: tuple[str, ...]
    resolution_ids: tuple[str, ...]
    coefficient_count: int
    construction_point_ids: tuple[str, ...]
    holdout_point_ids: tuple[str, ...]
    factorized_design: bool
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.coefficient_count < 0:
            raise ValueError("coefficient count cannot be negative")
        if self.availability is AvailabilityStatus.AVAILABLE:
            if not self.factorized_design or not self.varied_axis_id or self.varied_axis_id not in self.axis_ids:
                raise ValueError("available trajectory must vary one identified axis")
            if len(self.construction_point_ids) < self.coefficient_count or not self.holdout_point_ids:
                raise ValueError("trajectory is underdetermined or lacks a holdout")
            if set(self.construction_point_ids).intersection(self.holdout_point_ids):
                raise ValueError("trajectory holdouts may not enter construction")
            if not self.proof.closed:
                raise ValueError("available trajectory family has open proof obligations")
        elif any((self.axis_ids, self.varied_axis_id, self.fixed_axis_ids, self.resolution_ids, self.construction_point_ids, self.holdout_point_ids)):
            raise ValueError("unavailable trajectory family must be empty-not-zero")


@dataclass(frozen=True)
class SoftTrajectoryResult(ContentAddressed):
    identity: C35IdentityEnvelope
    result_id: str
    family_id: str
    fit_model: str | None
    coefficients: tuple[tuple[str, str], ...]
    covariance_hash: str | None
    construction_residuals: tuple[float, ...]
    holdout_residuals: tuple[float, ...]
    tolerance: float
    identified_components: tuple[str, ...]
    unresolved_components: tuple[str, ...]
    availability: AvailabilityStatus
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        if self.tolerance <= 0:
            raise ValueError("trajectory tolerance must be positive")
        material = (self.fit_model, self.coefficients, self.covariance_hash, self.construction_residuals, self.holdout_residuals, self.identified_components)
        if self.availability is AvailabilityStatus.AVAILABLE:
            if any(value in (None, (), "") for value in material):
                raise ValueError("available trajectory result requires coefficients and holdout evidence")
            if any(abs(value) > self.tolerance for value in self.holdout_residuals):
                raise ValueError("trajectory holdout prediction exceeds tolerance")
            if not self.proof.closed:
                raise ValueError("available trajectory result has open proof obligations")
        elif any(value not in (None, (), "") for value in material):
            raise ValueError("unavailable trajectory result must be empty-not-zero")


__all__ = ["SoftTrajectoryAxis", "SoftTrajectoryFamily", "SoftTrajectoryResult"]
