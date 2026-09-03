"""Shared identities, evidence gates, and status vocabularies for C35/S0C."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable

from .serialization import ContentAddressed


C35_BASELINE_COMMIT = "6bdb44be2afc79e817f69ce0e35813da8a394db7"
C34_STARTING_COMMIT = "e0b34c74e8f39c9d42cf49cc598f1533d9353a7e"
C32_OPERATOR_COMPLETION_COMMIT = "0d7b94a5e86882b23a56d4c1f11900d554756a18"
C28_SCIENTIFIC_ANCESTOR = "52678312906bf5cc0bb8664e2486d5d676a6b723"
C35_DESCENDANT_ROOT = "C35_SOFT_REGULATOR_COMPLETION_DESCENDANT"
C34_DESCENDANT_ROOT = "C34_FINITE_BASIS_VACUUM_EIKONAL_SOFT_ONE_LOOP_DESCENDANT"
C33_B0_ROOT = "C33_FINITE_BASIS_VACUUM_EIKONAL_SOFT_ROOT"
C32_B1_ROOT = "C32_MICROSCOPIC_TMD_OPERATOR_COMPLETION"
VOLUME_XXI_SHA256 = "613d26bcd58b4c9d15b23ef955cbb04feb2edc7d854d4ed63339c50835fa72c4"
C35_PROMPT_SHA256 = "1918dcd06e391498d77cfd1ddae73a5fadbdea496bf03e353e6ec7c809ac05c9"


class AvailabilityStatus(str, Enum):
    """Whether an object is materially present, absent, or unresolved."""

    AVAILABLE = "AVAILABLE"
    UNAVAILABLE_EMPTY_NOT_ZERO = "UNAVAILABLE_EMPTY_NOT_ZERO"
    UNRESOLVED_BLOCKING = "UNRESOLVED_BLOCKING"


class ValidationStatus(str, Enum):
    """Evidence state of a calculation or structural assertion."""

    VALIDATED = "VALIDATED"
    CALCULATED = "CALCULATED"
    PLANNED = "PLANNED"
    UNAVAILABLE_EMPTY_NOT_ZERO = "UNAVAILABLE_EMPTY_NOT_ZERO"
    UNRESOLVED_BLOCKING = "UNRESOLVED_BLOCKING"


class ContributionStatus(str, Enum):
    """The exact six-state C35 contribution vocabulary."""

    CALCULATED_NONZERO = "CALCULATED_NONZERO"
    CALCULATED_ZERO_BY_EXACT_IDENTITY = "CALCULATED_ZERO_BY_EXACT_IDENTITY"
    CANCELS_WITH_DECLARED_PARTNER = "CANCELS_WITH_DECLARED_PARTNER"
    TARGET_SCALELESS_BUT_FINITE_REGULATOR_NONZERO = (
        "TARGET_SCALELESS_BUT_FINITE_REGULATOR_NONZERO"
    )
    NOT_APPLICABLE_WITH_GAUGE_ACTION_PROOF = (
        "NOT_APPLICABLE_WITH_GAUGE_ACTION_PROOF"
    )
    UNRESOLVED_BLOCKING = "UNRESOLVED_BLOCKING"


class GaugePlanKind(str, Enum):
    COVARIANT_KREIN = "S0C-COVARIANT-KREIN"
    LIGHT_FRONT_PHYSICAL = "S0C-LIGHT_FRONT-PHYSICAL"
    AUXILIARY_EIKONAL = "S0C-AUXILIARY-EIKONAL"
    UNAVAILABLE = "S0C-UNAVAILABLE"


class OutcomeBranch(str, Enum):
    REGULATOR_AND_ONE_LOOP_CLOSE = "BRANCH_A"
    REGULATOR_CLOSES_DIAGRAMS_REMAIN = "BRANCH_B"
    MODE_BASIS_DOES_NOT_CLOSE = "BRANCH_C"
    ZERO_MODES_BLOCK = "BRANCH_D"
    AUXILIARY_ROUTE = "BRANCH_E"
    TRAJECTORY_UNRESOLVED = "BRANCH_F"
    NO_COMPATIBLE_REGULATOR = "BRANCH_G"


@dataclass(frozen=True)
class EvidenceRef(ContentAddressed):
    """Auditable evidence supporting one specific assertion."""

    evidence_id: str
    classification: str
    locator: str
    sha256_digest: str
    assertion: str
    proved: bool

    def __post_init__(self) -> None:
        _require_text(self.evidence_id, "evidence_id")
        _require_text(self.classification, "classification")
        _require_text(self.locator, "locator")
        _require_text(self.assertion, "assertion")
        if len(self.sha256_digest) != 64 or any(
            char not in "0123456789abcdef" for char in self.sha256_digest
        ):
            raise ValueError("sha256_digest must be a lowercase SHA-256 digest")


@dataclass(frozen=True)
class ProofSet(ContentAddressed):
    """Explicit proof obligations and the subset discharged by evidence."""

    required: tuple[str, ...] = ()
    proved: tuple[str, ...] = ()
    evidence_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if len(set(self.required)) != len(self.required):
            raise ValueError("proof obligations must be unique")
        if len(set(self.proved)) != len(self.proved):
            raise ValueError("proved obligations must be unique")
        unknown = set(self.proved).difference(self.required)
        if unknown:
            raise ValueError(f"proved obligations were not required: {sorted(unknown)}")
        if self.proved and not self.evidence_ids:
            raise ValueError("proved obligations require evidence identities")
        _require_unique_text(self.required, "required")
        _require_unique_text(self.proved, "proved")
        _require_unique_text(self.evidence_ids, "evidence_ids")

    @property
    def closed(self) -> bool:
        # An empty obligation list is useful for an unresolved placeholder but
        # is not evidence that a positive scientific gate has closed.
        return bool(self.required) and set(self.proved) == set(self.required)

    @property
    def missing(self) -> tuple[str, ...]:
        return tuple(item for item in self.required if item not in self.proved)


@dataclass(frozen=True)
class C35IdentityEnvelope(ContentAddressed):
    """Complete identity inherited by every formal C35 object.

    The reachability flags are intentionally fixed false.  A C35 soft-sector
    object cannot become a process, bridge, inference, or production object by
    construction.
    """

    object_id: str
    object_type: str
    gauge_plan_id: str
    light_front_convention_id: str
    real_chart_id: str
    virtual_chart_id: str
    mode_collection_id: str
    wilson_segment_set_id: str
    rapidity_regulator_id: str
    uv_regulator_id: str
    ir_regulator_id: str
    basis_regulator_id: str
    perturbative_order: str
    source_scheme: str
    target_scheme: str
    first_omitted_order: str
    evidence_ids: tuple[str, ...] = ()
    schema_version: str = "1.0.0"
    c35_descendant_root: str = C35_DESCENDANT_ROOT
    c34_descendant_root: str = C34_DESCENDANT_ROOT
    c34_completion_commit: str = C35_BASELINE_COMMIT
    c33_b0_root: str = C33_B0_ROOT
    c33_completion_commit: str = C34_STARTING_COMMIT
    c32_b1_root: str = C32_B1_ROOT
    c32_completion_commit: str = C32_OPERATOR_COMPLETION_COMMIT
    c28_scientific_ancestor: str = C28_SCIENTIFIC_ANCESTOR
    baryon_number: int = 0
    state_independent: bool = True
    hadron_independent: bool = True
    art25_independent: bool = True
    process_reachable: bool = False
    bridge_reachable: bool = False
    inference_reachable: bool = False
    production_reachable: bool = False

    def __post_init__(self) -> None:
        for name in (
            "object_id",
            "object_type",
            "gauge_plan_id",
            "light_front_convention_id",
            "real_chart_id",
            "virtual_chart_id",
            "mode_collection_id",
            "wilson_segment_set_id",
            "rapidity_regulator_id",
            "uv_regulator_id",
            "ir_regulator_id",
            "basis_regulator_id",
            "perturbative_order",
            "source_scheme",
            "target_scheme",
            "first_omitted_order",
        ):
            _require_text(getattr(self, name), name)
        _require_unique_text(self.evidence_ids, "evidence_ids")
        if self.c35_descendant_root != C35_DESCENDANT_ROOT:
            raise ValueError("C35 descendant root mismatch")
        if self.c34_descendant_root != C34_DESCENDANT_ROOT:
            raise ValueError("C34 descendant root mismatch")
        if self.c34_completion_commit != C35_BASELINE_COMMIT:
            raise ValueError("C34 completion commit mismatch")
        if self.c33_completion_commit != C34_STARTING_COMMIT:
            raise ValueError("C33 completion commit mismatch")
        if self.c32_completion_commit != C32_OPERATOR_COMPLETION_COMMIT:
            raise ValueError("C32 completion commit mismatch")
        if self.c28_scientific_ancestor != C28_SCIENTIFIC_ANCESTOR:
            raise ValueError("C28 scientific ancestor mismatch")
        if self.c33_b0_root != C33_B0_ROOT or self.c32_b1_root != C32_B1_ROOT:
            raise ValueError("C32/C33 root ancestry mismatch")
        if self.gauge_plan_id not in {item.value for item in GaugePlanKind}:
            raise ValueError("unknown C35 gauge-plan identity")
        if self.baryon_number != 0:
            raise ValueError("C35 soft objects must remain in the B=0 root")
        if not (self.state_independent and self.hadron_independent and self.art25_independent):
            raise ValueError("C35 identities must be state, hadron, and ART25 independent")
        if any(
            (
                self.process_reachable,
                self.bridge_reachable,
                self.inference_reachable,
                self.production_reachable,
            )
        ):
            raise ValueError("C35 identities are unreachable from downstream routes")


def identity_for(
    object_id: str,
    object_type: str,
    *,
    gauge_plan_id: str = GaugePlanKind.UNAVAILABLE.value,
    light_front_convention_id: str = "UNRESOLVED_LIGHT_FRONT_CONVENTION",
    real_chart_id: str = "UNRESOLVED_REAL_CHART",
    virtual_chart_id: str = "UNRESOLVED_VIRTUAL_CHART",
    mode_collection_id: str = "UNAVAILABLE_EMPTY_NOT_ZERO",
    wilson_segment_set_id: str = "UNAVAILABLE_EMPTY_NOT_ZERO",
    rapidity_regulator_id: str = "MODIFIED_DELTA_UNRESOLVED",
    uv_regulator_id: str = "FINITE_CELL_UV_UNRESOLVED",
    ir_regulator_id: str = "FINITE_CELL_IR_UNRESOLVED",
    basis_regulator_id: str = "FINITE_CELL_UNRESOLVED",
    perturbative_order: str = "O(ALPHA_S)",
    source_scheme: str = "C35_FINITE_BASIS_UNRESOLVED",
    target_scheme: str = "PROJECT_TMD_SCHEME",
    first_omitted_order: str = "O(ALPHA_S^2)_NONZERO_UNKNOWN",
    evidence_ids: Iterable[str] = (),
) -> C35IdentityEnvelope:
    """Construct an explicit identity without inferring any field from a name."""

    return C35IdentityEnvelope(
        object_id=object_id,
        object_type=object_type,
        gauge_plan_id=gauge_plan_id,
        light_front_convention_id=light_front_convention_id,
        real_chart_id=real_chart_id,
        virtual_chart_id=virtual_chart_id,
        mode_collection_id=mode_collection_id,
        wilson_segment_set_id=wilson_segment_set_id,
        rapidity_regulator_id=rapidity_regulator_id,
        uv_regulator_id=uv_regulator_id,
        ir_regulator_id=ir_regulator_id,
        basis_regulator_id=basis_regulator_id,
        perturbative_order=perturbative_order,
        source_scheme=source_scheme,
        target_scheme=target_scheme,
        first_omitted_order=first_omitted_order,
        evidence_ids=tuple(evidence_ids),
    )


def require_identity(identity: C35IdentityEnvelope, expected_type: str) -> None:
    if identity.object_type != expected_type:
        raise ValueError(
            f"identity object_type {identity.object_type!r} does not match {expected_type!r}"
        )


def require_closed(status: ValidationStatus, proof: ProofSet, field: str) -> None:
    if status in (ValidationStatus.VALIDATED, ValidationStatus.CALCULATED) and not proof.closed:
        raise ValueError(f"{field} cannot be {status.value} with open proof obligations")


def require_materialized(
    status: AvailabilityStatus,
    values: Iterable[object],
    *,
    field: str,
) -> None:
    materialized = tuple(values)
    if status is AvailabilityStatus.AVAILABLE and not materialized:
        raise ValueError(f"{field} is AVAILABLE but has no materialized content")
    if status is not AvailabilityStatus.AVAILABLE and materialized:
        raise ValueError(f"{field} has content while status is {status.value}")


def validate_contribution(
    status: ContributionStatus,
    proof: ProofSet,
    *,
    value_expression: str | None,
    cancellation_partner_id: str | None,
) -> None:
    if status is ContributionStatus.UNRESOLVED_BLOCKING:
        if value_expression is not None or cancellation_partner_id is not None:
            raise ValueError("unresolved contributions must be empty-not-zero")
        return
    if not proof.closed:
        raise ValueError(f"{status.value} requires a closed proof set")
    if status is ContributionStatus.CANCELS_WITH_DECLARED_PARTNER:
        _require_text(cancellation_partner_id, "cancellation_partner_id")
    elif cancellation_partner_id is not None:
        raise ValueError("only a cancellation status may name a cancellation partner")
    if status in (
        ContributionStatus.CALCULATED_NONZERO,
        ContributionStatus.CALCULATED_ZERO_BY_EXACT_IDENTITY,
        ContributionStatus.TARGET_SCALELESS_BUT_FINITE_REGULATOR_NONZERO,
    ):
        _require_text(value_expression, "value_expression")


def _require_text(value: object, field: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a non-empty string")


def _require_unique_text(values: Iterable[str], field: str) -> None:
    collected = tuple(values)
    for value in collected:
        _require_text(value, field)
    if len(set(collected)) != len(collected):
        raise ValueError(f"{field} must not contain duplicates")


__all__ = [
    "AvailabilityStatus",
    "C28_SCIENTIFIC_ANCESTOR",
    "C32_B1_ROOT",
    "C32_OPERATOR_COMPLETION_COMMIT",
    "C33_B0_ROOT",
    "C34_DESCENDANT_ROOT",
    "C34_STARTING_COMMIT",
    "C35_BASELINE_COMMIT",
    "C35_DESCENDANT_ROOT",
    "C35_PROMPT_SHA256",
    "C35IdentityEnvelope",
    "ContributionStatus",
    "EvidenceRef",
    "GaugePlanKind",
    "OutcomeBranch",
    "ProofSet",
    "VOLUME_XXI_SHA256",
    "ValidationStatus",
    "identity_for",
    "require_closed",
    "require_identity",
    "require_materialized",
    "validate_contribution",
]
