"""Explicit zero-mode and transverse-boundary sectors."""

from __future__ import annotations

from dataclasses import dataclass

from .identity import (
    C35IdentityEnvelope,
    ContributionStatus,
    ProofSet,
    require_identity,
    validate_contribution,
)
from .serialization import ContentAddressed


@dataclass(frozen=True)
class SoftZeroModeSector(ContentAddressed):
    identity: C35IdentityEnvelope
    sector_id: str
    gauge_plan_id: str
    constraint_equations: tuple[str, ...]
    retained_modes: tuple[str, ...]
    excluded_primary_modes: tuple[str, ...]
    ward_role: str | None
    line_self_energy_role: str | None
    rapidity_role: str | None
    transverse_link_role: str | None
    contribution_status: ContributionStatus
    value_expression: str | None
    cancellation_partner_id: str | None
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        validate_contribution(
            self.contribution_status,
            self.proof,
            value_expression=self.value_expression,
            cancellation_partner_id=self.cancellation_partner_id,
        )
        if self.contribution_status is not ContributionStatus.UNRESOLVED_BLOCKING:
            if not self.constraint_equations or not all(
                (self.ward_role, self.line_self_energy_role, self.rapidity_role, self.transverse_link_role)
            ):
                raise ValueError("resolved zero-mode sector requires every physical role")


@dataclass(frozen=True)
class SoftBoundarySector(ContentAddressed):
    identity: C35IdentityEnvelope
    sector_id: str
    gauge_plan_id: str
    boundary_conditions: tuple[str, ...]
    endpoint_ids: tuple[str, ...]
    cusp_ids: tuple[str, ...]
    transverse_junction_ids: tuple[str, ...]
    residual_gauge_transformations: tuple[str, ...]
    contribution_status: ContributionStatus
    value_expression: str | None
    cancellation_partner_id: str | None
    proof: ProofSet

    def __post_init__(self) -> None:
        require_identity(self.identity, type(self).__name__)
        validate_contribution(
            self.contribution_status,
            self.proof,
            value_expression=self.value_expression,
            cancellation_partner_id=self.cancellation_partner_id,
        )
        if self.contribution_status is not ContributionStatus.UNRESOLVED_BLOCKING:
            if not all(
                (
                    self.boundary_conditions,
                    self.endpoint_ids,
                    self.cusp_ids,
                    self.transverse_junction_ids,
                    self.residual_gauge_transformations,
                )
            ):
                raise ValueError("resolved boundary sector needs endpoints, cusps, and gauge data")


__all__ = ["SoftBoundarySector", "SoftZeroModeSector"]
