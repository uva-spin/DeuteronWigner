"""Typed C34/S0A one-loop soft-sector calculation contracts.

This module is an additive descendant of the immutable C33 baryon-number-zero
vacuum/eikonal root.  It makes the one-loop calculation inputs and failure
boundaries executable without manufacturing a finite-basis coefficient.  The
default graph is deliberately the rigorous Branch-G result: the exact tree
boundary and four-line symbolic current are available, while every required
one-loop contribution remains ``UNRESOLVED_BLOCKING`` until a regulator-
specific calculation supplies it.

Nothing in this module consumes ART25, process data, bridge residuals, or a
proton probability normalization.  No object is reachable from inference or
production.
"""

from __future__ import annotations

import cmath
from dataclasses import dataclass, fields, is_dataclass
from enum import Enum
from fractions import Fraction
from hashlib import sha256
import json
import math
from typing import Any, Dict, Optional, Tuple, Type

from ..s0.core import (
    C32_COLLINEAR_ROOT,
    C33_BASIS_REGULATOR_ID,
    C33_IR_REGULATOR_ID,
    C33_RAPIDITY_REGULATOR_ID,
    C33_SOFT_ROOT,
    C33_SOURCE_SOFT_SCHEME,
    C33_TARGET_SOFT_SCHEME,
    C33_UV_REGULATOR_ID,
    C33_WILSON_GEOMETRY,
    EikonalDirection as C33EikonalDirection,
    SoftRapidityRegulator as C33SoftRapidityRegulator,
    default_four_line_operator,
)


C34_SCOPE = "C34/S0A"
C34_STARTING_COMMIT = "e0b34c74e8f39c9d42cf49cc598f1533d9353a7e"
C34_DESCENDANT_ROOT = "C34_FINITE_BASIS_VACUUM_EIKONAL_SOFT_ONE_LOOP_DESCENDANT"
C34_PLAN_ID = "C34.S0A.ONE_LOOP.PLAN.v1"
C34_COUPLING_NORMALIZATION = "a_s=g_s^2/(4*pi)^2=alpha_s/(4*pi)"
C34_EIKONAL_VERTEX_COUPLING = "g_s"
C34_TARGET_SOFT_EXPANSION = (
    "S_tilde=exp[a_s*C_F*(S^[1]+a_s*S^[2]+...)];"
    "C_F_external_to_reduced_S^[1]"
)
C34_CONTINUUM_SOURCE_ID = "ARXIV:1511.05590v2"
C34_CONTINUUM_SOURCE_FILE_SHA256 = (
    "dda565928e2a52997da094a156b286b31741184e47398d2efaa801a9a97e573d"
)
C34_CONTINUUM_SOURCE_LOCATOR = "ARXIV:1511.05590v2:Eqs.(2),(7),(8),(11)-(13)"
C34_CONTINUUM_NLO_SOURCE_EXPRESSION = (
    "S^[1]=-4*mu^(2*epsilon)*B^epsilon*Gamma(-epsilon)"
    "*(L_0-psi(-epsilon)-gamma_E);"
    "B=b_T^2/4;"
    "L_0=ln(B*abs(delta_plus*delta_minus)*exp(2*gamma_E))"
)
C34_CONTINUUM_NLO_LAURENT_EXPRESSION = (
    "S^[1]=-4/epsilon^2+2*L_mu^2"
    "-(2*d^(1,1)/C_F)*(1/epsilon+L_mu)*l_delta"
    "+pi^2/3+O(epsilon);"
    "L_mu=ln(mu^2*B*exp(2*gamma_E));"
    "d^(1,1)=2*C_F;"
    "l_delta=ln(mu^2/abs(delta_plus*delta_minus))"
)
C34_CONTINUUM_NLO_SOURCE_EXPRESSION_SHA256 = (
    "aed120b66df5ed8eb2eb448997ab2360c3cf94a5933a0bc16728c2b0350343c6"
)
C34_CONTINUUM_NLO_LAURENT_EXPRESSION_SHA256 = (
    "025d792beed9bb1f585d9f3019ba3c8c9c299fc65ebb9476ffe7d5cd9990a9b8"
)
if (
    sha256(C34_CONTINUUM_NLO_SOURCE_EXPRESSION.encode("ascii")).hexdigest()
    != C34_CONTINUUM_NLO_SOURCE_EXPRESSION_SHA256
    or sha256(C34_CONTINUUM_NLO_LAURENT_EXPRESSION.encode("ascii")).hexdigest()
    != C34_CONTINUUM_NLO_LAURENT_EXPRESSION_SHA256
):
    raise RuntimeError("C34_CONTINUUM_SOURCE_FORMULA_HASH_LOCK_MISMATCH")
C34_NO_GO = "C34_SOFT_ONE_LOOP_INCOMPLETE"
C34_NEXT_PACKAGE = (
    "C35/S0C — targeted unresolved soft-diagram and counterterm completion"
)
NONZERO_UNKNOWN = "NONZERO_UNKNOWN"

FOUR_LINE_IDS = (
    "SN_DAGGER_B",
    "SNBAR_B",
    "SNBAR_DAGGER_0",
    "SN_0",
)

EIKONAL_NUMERICAL_CURRENT_REQUIREMENTS = (
    "FOUR_LINE_TRACE_ORDER",
    "REPRESENTATION_CLASS",
    "PATH_ORDERING",
    "DIRECTION_AND_TRANSVERSE_BASEPOINT",
    "MODIFIED_DELTA_SINGLE_GLUON_POLE_SIGN",
    "LIGHT_FRONT_TANGENT_NORMALIZATION",
    "EMISSION_ABSORPTION_NUMERATOR_SIGN",
    "CONJUGATE_GENERATOR_ACTION",
    "COMPLETE_PARAMETERIZED_SEGMENT_PHASE",
    "FINITE_BASIS_GAUGE_FIELD_MODE_NORMALIZATION",
    "FINITE_BASIS_INTERACTION_COUPLING_MAP",
)
EIKONAL_NUMERICAL_CURRENT_PROVED = (
    "FOUR_LINE_TRACE_ORDER",
    "REPRESENTATION_CLASS",
    "PATH_ORDERING",
    "DIRECTION_AND_TRANSVERSE_BASEPOINT",
    "MODIFIED_DELTA_SINGLE_GLUON_POLE_SIGN",
)

RESOLUTION_REFINEMENT_REQUIREMENTS = (
    "ORDERED_C33_RESOLUTION_DESCRIPTORS",
    "MONOTONE_NOMINAL_SUPPORT_EXTENSION",
    "EXPLICIT_CELL_EDGES_AND_WEIGHTS",
    "NORMALIZED_MODE_FUNCTIONS",
    "EXACT_SUCCESSIVE_INJECTION_OR_REFINEMENT_MAPS",
    "DECLARED_COMMON_CONTINUUM_LIMIT",
)
RESOLUTION_REFINEMENT_PROVED = (
    "ORDERED_C33_RESOLUTION_DESCRIPTORS",
    "MONOTONE_NOMINAL_SUPPORT_EXTENSION",
)

CONTINUUM_ORACLE_REQUIREMENTS = (
    "SOURCE_FILE_HASH",
    "SOURCE_EQUATION_TRANSCRIPTION",
    "SOURCE_EXPRESSION_HASH",
    "COUPLING_AND_COLOR_CONVENTION",
    "INDEPENDENT_DIRECT_INTEGRAL_RECONSTRUCTION",
    "CONVENTION_ALIGNMENT_CHECK",
    "ANOMALOUS_DIMENSION_CHECK",
)
CONTINUUM_ORACLE_PROVED = (
    "SOURCE_FILE_HASH",
    "SOURCE_EQUATION_TRANSCRIPTION",
    "SOURCE_EXPRESSION_HASH",
    "COUPLING_AND_COLOR_CONVENTION",
)

REQUIRED_ONE_LOOP_CONTRIBUTIONS = (
    "N_NBAR_EXCHANGE",
    "CONJUGATE_LINE_EXCHANGE",
    "SAME_DIRECTION_LINE_EXCHANGE",
    "REAL_ONE_SOFT_GLUON",
    "VIRTUAL_ONE_SOFT_GLUON",
    "WILSON_LINE_SELF_ENERGY",
    "CUSP_ENDPOINT",
    "TRANSVERSE_CLOSURE",
    "AUXILIARY_FIELD_SELF_ENERGY",
    "SOFT_VACUUM_ENERGY",
    "LIGHT_FRONT_INSTANTANEOUS",
    "GAUGE_FIXING",
    "GHOST",
    "ZERO_MODE",
    "BASIS_BOUNDARY",
    "RAPIDITY_COUNTERTERM",
    "UV_COUNTERTERM",
    "RESIDUAL_LINE_MASS_COUNTERTERM",
)

DIRECT_BARE_CONTRIBUTIONS = (
    "N_NBAR_EXCHANGE",
    "CONJUGATE_LINE_EXCHANGE",
    "SAME_DIRECTION_LINE_EXCHANGE",
    "REAL_ONE_SOFT_GLUON",
    "VIRTUAL_ONE_SOFT_GLUON",
    "WILSON_LINE_SELF_ENERGY",
    "CUSP_ENDPOINT",
    "TRANSVERSE_CLOSURE",
    "SOFT_VACUUM_ENERGY",
    "LIGHT_FRONT_INSTANTANEOUS",
    "GAUGE_FIXING",
    "GHOST",
    "BASIS_BOUNDARY",
)
SEPARATE_CONTROL_CONTRIBUTIONS = ("ZERO_MODE",)
ALTERNATIVE_ROUTE_CONTRIBUTIONS = ("AUXILIARY_FIELD_SELF_ENERGY",)
COUNTERTERM_DECISION_CONTRIBUTIONS = (
    "RAPIDITY_COUNTERTERM",
    "UV_COUNTERTERM",
    "RESIDUAL_LINE_MASS_COUNTERTERM",
)
CONTRIBUTION_ID_BY_CLASS = {
    name: "C34.SOFT.%02d" % (index + 1)
    for index, name in enumerate(REQUIRED_ONE_LOOP_CONTRIBUTIONS)
}
DIRECT_BARE_COMPONENT_IDS = tuple(
    CONTRIBUTION_ID_BY_CLASS[name] for name in DIRECT_BARE_CONTRIBUTIONS
)
SEPARATE_CONTROL_COMPONENT_IDS = tuple(
    CONTRIBUTION_ID_BY_CLASS[name] for name in SEPARATE_CONTROL_CONTRIBUTIONS
)
ALTERNATIVE_ROUTE_COMPONENT_IDS = tuple(
    CONTRIBUTION_ID_BY_CLASS[name] for name in ALTERNATIVE_ROUTE_CONTRIBUTIONS
)
COUNTERTERM_DECISION_COMPONENT_IDS = tuple(
    CONTRIBUTION_ID_BY_CLASS[name] for name in COUNTERTERM_DECISION_CONTRIBUTIONS
)
DERIVED_COUNTERTERM_IDS = (
    "C34.CT.01.LINE_SELF_ENERGY",
    "C34.CT.02.CUSP",
    "C34.CT.03.ENDPOINT",
    "C34.CT.04.TRANSVERSE_CLOSURE",
    "C34.CT.05.VACUUM",
    "C34.CT.06.BASIS_BOUNDARY",
    "C34.CT.07.SOFT_OPERATOR_UV",
    "C34.CT.08.RAPIDITY",
    "C34.CT.09.RESIDUAL_LINE_MASS",
)


@dataclass(frozen=True)
class RequiredProofSet:
    """Separate a scientific requirement from what the repository proves.

    The distinction is deliberately structural: a requirement can be present
    in a frozen plan without being established by a source, derivation, or
    executed finite-basis calculation.  No caller may infer proof merely from
    membership in ``required``.
    """

    required: Tuple[str, ...]
    proved: Tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.required or len(set(self.required)) != len(self.required):
            raise ValueError("C34_PROOF_REQUIREMENTS_EMPTY_OR_DUPLICATED")
        if len(set(self.proved)) != len(self.proved):
            raise ValueError("C34_PROVED_OBLIGATIONS_DUPLICATED")
        if not set(self.proved).issubset(set(self.required)):
            raise ValueError("C34_PROOF_CLAIM_NOT_A_DECLARED_REQUIREMENT")

    @property
    def unproved(self) -> Tuple[str, ...]:
        proved = set(self.proved)
        return tuple(item for item in self.required if item not in proved)

    @property
    def closed(self) -> bool:
        return not self.unproved


class ContributionStatus(str, Enum):
    """The six and only six C34 one-loop contribution decisions."""

    CALCULATED_NONZERO = "CALCULATED_NONZERO"
    CALCULATED_ZERO_BY_EXACT_IDENTITY = "CALCULATED_ZERO_BY_EXACT_IDENTITY"
    CANCELS_WITH_DECLARED_PARTNER = "CANCELS_WITH_DECLARED_PARTNER"
    TARGET_SCALELESS_BUT_FINITE_REGULATOR_NONZERO = (
        "TARGET_SCALELESS_BUT_FINITE_REGULATOR_NONZERO"
    )
    NOT_APPLICABLE_WITH_PROOF = "NOT_APPLICABLE_WITH_PROOF"
    UNRESOLVED_BLOCKING = "UNRESOLVED_BLOCKING"

class SoftTrajectoryStatus(str, Enum):
    RESOLVED = "SOFT_CONTINUUM_TRAJECTORY_RESOLVED"
    LOG_ONLY = "SOFT_LOG_STRUCTURE_RESOLVED_FINITE_REMAINDER_OPEN"
    FINITE_BASIS_ONLY = "SOFT_FINITE_BASIS_ONLY"
    NONUNIVERSAL = "SOFT_NONUNIVERSAL_TRAJECTORY"
    UNAVAILABLE = "SOFT_TRAJECTORY_UNAVAILABLE"


class SoftCollinearStatus(str, Enum):
    SOFT_SIDE_READY = "SOFT_SIDE_ZERO_BIN_OBJECT_READY"
    EXACT_CONVERSION_READY = "SOFT_COLLINEAR_EXACT_CONVERSION_READY"
    READY_FOR_IDENTICAL_TEST = "SOFT_COLLINEAR_READY_FOR_OPERATOR_IDENTICAL_TEST"
    UNRESOLVED = "SOFT_COLLINEAR_COMPATIBILITY_UNRESOLVED"
    INCOMPATIBLE = "SOFT_COLLINEAR_INCOMPATIBLE"


@dataclass(frozen=True)
class C34IdentityEnvelope:
    envelope_version: str
    object_type: str
    object_identity: str
    scope: str
    starting_commit: str
    parent_soft_root_id: str
    descendant_root_id: str
    collinear_root_id: str
    baryon_number: int
    wilson_geometry: str
    color_representation: str
    color_trace: str
    mode_cell_identity: str
    quadrature_identity: str
    gauge_identity: str
    zero_mode_status: str
    rapidity_regulator_id: str
    uv_regulator_id: str
    ir_regulator_id: str
    basis_regulator_id: str
    perturbative_order: str
    source_soft_scheme: str
    target_soft_scheme: str
    first_omitted_order: str
    state_independence_required: bool
    state_independence_proved: bool
    hadron_independence_required: bool
    hadron_independence_proved: bool
    consumes_art25: bool
    consumes_process_data: bool
    consumes_bridge_residuals: bool
    inference_reachable: bool
    production_reachable: bool

    def __post_init__(self) -> None:
        if self.scope != C34_SCOPE or self.starting_commit != C34_STARTING_COMMIT:
            raise ValueError("C34_IDENTITY_ENVELOPE_SCOPE_OR_BASELINE_MISMATCH")
        if self.parent_soft_root_id != C33_SOFT_ROOT:
            raise ValueError("C34_PARENT_SOFT_ROOT_MISMATCH")
        if self.descendant_root_id != C34_DESCENDANT_ROOT:
            raise ValueError("C34_DESCENDANT_ROOT_MISMATCH")
        if self.collinear_root_id != C32_COLLINEAR_ROOT:
            raise ValueError("C34_COLLINEAR_ROOT_IDENTITY_MISMATCH")
        if self.baryon_number != 0:
            raise ValueError("C34_SOFT_ROOT_MUST_HAVE_BARYON_NUMBER_ZERO")
        if self.wilson_geometry != C33_WILSON_GEOMETRY:
            raise ValueError("C34_C33_WILSON_GEOMETRY_CHANGED")
        if (self.color_representation, self.color_trace) != (
            "FUNDAMENTAL", "SINGLET_1_OVER_NC"
        ):
            raise ValueError("C34_QUARK_SOFT_COLOR_IDENTITY_MISMATCH")
        if not all(
            (
                self.rapidity_regulator_id,
                self.uv_regulator_id,
                self.ir_regulator_id,
                self.basis_regulator_id,
                self.perturbative_order,
                self.source_soft_scheme,
                self.target_soft_scheme,
                self.mode_cell_identity,
                self.quadrature_identity,
                self.gauge_identity,
                self.zero_mode_status,
                self.first_omitted_order,
            )
        ):
            raise ValueError("C34_IDENTITY_ENVELOPE_REQUIRED_FIELD_MISSING")
        if not self.state_independence_required or not self.hadron_independence_required:
            raise ValueError("C34_SOFT_OBJECT_UNIVERSALITY_REQUIREMENT_MISSING")
        if self.state_independence_proved and not self.state_independence_required:
            raise ValueError("C34_STATE_INDEPENDENCE_PROOF_WITHOUT_REQUIREMENT")
        if self.hadron_independence_proved and not self.hadron_independence_required:
            raise ValueError("C34_HADRON_INDEPENDENCE_PROOF_WITHOUT_REQUIREMENT")
        if any(
            (
                self.consumes_art25,
                self.consumes_process_data,
                self.consumes_bridge_residuals,
                self.inference_reachable,
                self.production_reachable,
            )
        ):
            raise ValueError("C34_FORBIDDEN_DATA_OR_PRODUCTION_REACHABILITY")

    @property
    def validated(self) -> bool:
        return True


def _canonical(value: Any) -> Any:
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Fraction):
        return {"numerator": value.numerator, "denominator": value.denominator}
    if isinstance(value, complex):
        if not math.isfinite(value.real) or not math.isfinite(value.imag):
            raise ValueError("NONFINITE_VALUE_NOT_SERIALIZABLE")
        return {"real": value.real, "imag": value.imag}
    if is_dataclass(value):
        result = {
            field.name: _canonical(getattr(value, field.name)) for field in fields(value)
        }
        if isinstance(value, _ContentAddressed):
            result["c34_identity_envelope"] = _canonical(
                value.c34_identity_envelope
            )
        return result
    if isinstance(value, dict):
        return {str(key): _canonical(value[key]) for key in sorted(value)}
    if isinstance(value, (tuple, list)):
        return [_canonical(item) for item in value]
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError("NONFINITE_VALUE_NOT_SERIALIZABLE")
    return value


def deterministic_json(value: Any) -> str:
    return json.dumps(
        _canonical(value),
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    )


def content_hash(value: Any) -> str:
    return sha256(deterministic_json(value).encode("utf-8")).hexdigest()


class _ContentAddressed:
    @property
    def c34_identity_envelope(self) -> C34IdentityEnvelope:
        object_identity = type(self).__name__
        for field in fields(self):
            if field.name.endswith("_id"):
                candidate = getattr(self, field.name)
                if isinstance(candidate, str) and candidate:
                    object_identity = candidate
                    break
        order = "O(g_s^2)/O(a_s)"
        for attribute in ("perturbative_order", "order"):
            candidate = getattr(self, attribute, None)
            if isinstance(candidate, str) and candidate:
                order = candidate
                break
        first_omitted_order = getattr(self, "first_omitted_order", None)
        if not isinstance(first_omitted_order, str) or not first_omitted_order:
            first_omitted_order = (
                "O(g_s^2)" if order == "O(g_s)" else "O(a_s^2)"
            )
        mode_cell_identity = "C34.TYPED.MODE.CELL.PLAN"
        for attribute in ("cell_id", "mode_cell_id"):
            candidate = getattr(self, attribute, None)
            if isinstance(candidate, str) and candidate:
                mode_cell_identity = candidate
                break
        quadrature_identity = getattr(
            self, "quadrature_id", "C34.SOFT.CELL.QUADRATURE.v1"
        )
        state_independence_proved = getattr(
            self, "state_independence_proved", False
        )
        hadron_independence_proved = getattr(
            self, "hadron_independence_proved", False
        )
        if not isinstance(state_independence_proved, bool):
            state_independence_proved = False
        if not isinstance(hadron_independence_proved, bool):
            hadron_independence_proved = False
        return C34IdentityEnvelope(
            envelope_version="C34.IDENTITY.ENVELOPE.v1",
            object_type=type(self).__name__,
            object_identity=object_identity,
            scope=C34_SCOPE,
            starting_commit=C34_STARTING_COMMIT,
            parent_soft_root_id=C33_SOFT_ROOT,
            descendant_root_id=C34_DESCENDANT_ROOT,
            collinear_root_id=C32_COLLINEAR_ROOT,
            baryon_number=0,
            wilson_geometry=C33_WILSON_GEOMETRY,
            color_representation="FUNDAMENTAL",
            color_trace="SINGLET_1_OVER_NC",
            mode_cell_identity=mode_cell_identity,
            quadrature_identity=quadrature_identity,
            gauge_identity=(
                "COVARIANT_XI_G_PROBE_PLAN_{0,1,2}_"
                "GAUGE_COMPLETION_UNRESOLVED"
            ),
            zero_mode_status="EXCLUDE_PRIMARY_RETAIN_SEPARATE_CONTROL/AUDIT_REQUIRED",
            rapidity_regulator_id=C33_RAPIDITY_REGULATOR_ID,
            uv_regulator_id=C33_UV_REGULATOR_ID,
            ir_regulator_id=C33_IR_REGULATOR_ID,
            basis_regulator_id=C33_BASIS_REGULATOR_ID,
            perturbative_order=order,
            source_soft_scheme=C33_SOURCE_SOFT_SCHEME,
            target_soft_scheme=C33_TARGET_SOFT_SCHEME,
            first_omitted_order=first_omitted_order,
            state_independence_required=True,
            state_independence_proved=state_independence_proved,
            hadron_independence_required=True,
            hadron_independence_proved=hadron_independence_proved,
            consumes_art25=False,
            consumes_process_data=False,
            consumes_bridge_residuals=False,
            inference_reachable=False,
            production_reachable=False,
        )

    @property
    def identity_validated(self) -> bool:
        return self.c34_identity_envelope.validated

    @property
    def deterministic_json(self) -> str:
        return deterministic_json(self)

    @property
    def content_hash(self) -> str:
        return content_hash(self)


def _require_identifier(value: str, diagnostic: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(diagnostic)


def _validate_status(
    status: ContributionStatus,
    expression: str,
    proof: str = "",
    cancellation_partner_id: str = "",
) -> None:
    if status is ContributionStatus.UNRESOLVED_BLOCKING:
        if expression != NONZERO_UNKNOWN:
            raise ValueError("C34_UNRESOLVED_TERM_MUST_BE_NONZERO_UNKNOWN")
        return
    if status is ContributionStatus.CALCULATED_NONZERO:
        if not expression or expression in (NONZERO_UNKNOWN, "0", "ZERO"):
            raise ValueError("C34_NONZERO_TERM_REQUIRES_CALCULATED_EXPRESSION")
        return
    if status is ContributionStatus.CALCULATED_ZERO_BY_EXACT_IDENTITY:
        if expression not in ("0", "ZERO") or not proof:
            raise ValueError("C34_ZERO_TERM_REQUIRES_EXACT_IDENTITY_PROOF")
        return
    if status is ContributionStatus.CANCELS_WITH_DECLARED_PARTNER:
        if not proof or not cancellation_partner_id:
            raise ValueError("C34_CANCELLATION_REQUIRES_PARTNER_AND_PROOF")
        return
    if status is ContributionStatus.TARGET_SCALELESS_BUT_FINITE_REGULATOR_NONZERO:
        if expression in ("", NONZERO_UNKNOWN, "0", "ZERO") or not proof:
            raise ValueError("C34_FINITE_REGULATOR_NONZERO_REQUIRES_CALCULATION")
        return
    if status is ContributionStatus.NOT_APPLICABLE_WITH_PROOF and not proof:
        raise ValueError("C34_NONAPPLICABILITY_REQUIRES_PROOF")


@dataclass(frozen=True)
class SoftContributionResult(_ContentAddressed):
    contribution_id: str
    contribution_class: str
    status: ContributionStatus
    expression: str
    proof: str = ""
    cancellation_partner_id: str = ""
    blocking: bool = True
    finite_regulator_evaluated: bool = False
    continuum_scaleless_assumed: bool = False

    def __post_init__(self) -> None:
        if self.contribution_class not in REQUIRED_ONE_LOOP_CONTRIBUTIONS:
            raise ValueError("C34_UNKNOWN_ONE_LOOP_CONTRIBUTION_CLASS")
        if self.continuum_scaleless_assumed:
            raise ValueError("C34_CONTINUUM_SCALELESS_ANALOGY_FORBIDDEN")
        _validate_status(
            self.status, self.expression, self.proof, self.cancellation_partner_id
        )
        resolved = self.status is not ContributionStatus.UNRESOLVED_BLOCKING
        if self.blocking == resolved:
            raise ValueError("C34_CONTRIBUTION_BLOCKING_STATUS_INCONSISTENT")

    @property
    def resolved(self) -> bool:
        return self.status is not ContributionStatus.UNRESOLVED_BLOCKING


@dataclass(frozen=True)
class SoftOneLoopPlan(_ContentAddressed):
    plan_id: str
    realization: str
    operator_id: str
    order_id: str
    gauge_parameters: Tuple[float, ...]
    rapidity_regulator_id: str
    uv_target_scheme: str
    resolution_ids: Tuple[str, ...]
    zero_mode_policy: str
    b_points: Tuple[float, ...]
    delta_plus_trajectory: Tuple[float, ...]
    delta_minus_trajectory: Tuple[float, ...]
    quadrature_id: str
    frozen_before_results: bool
    source_predicted_trajectory_only: bool

    def __post_init__(self) -> None:
        if self.realization != "S0-FB-EIKONAL-FOCK":
            raise ValueError("C34_PRIMARY_REALIZATION_CHANGED")
        if self.operator_id != "C33.FOUR_LINE.SOFT.OPERATOR":
            raise ValueError("C34_C33_OPERATOR_IDENTITY_CHANGED")
        if self.gauge_parameters != (0.0, 1.0, 2.0):
            raise ValueError("C34_REQUIRED_GAUGE_HOLDOUTS_MISSING")
        if self.rapidity_regulator_id != C33_RAPIDITY_REGULATOR_ID:
            raise ValueError("C34_MODIFIED_DELTA_PLAN_CHANGED")
        if len(self.resolution_ids) < 3 or len(set(self.resolution_ids)) != len(
            self.resolution_ids
        ):
            raise ValueError("C34_THREE_DISTINCT_SOFT_RESOLUTIONS_REQUIRED")
        if not self.b_points or not self.delta_plus_trajectory or not self.delta_minus_trajectory:
            raise ValueError("C34_FROZEN_REGULATOR_TRAJECTORY_MISSING")
        if any(value <= 0.0 for value in self.delta_plus_trajectory + self.delta_minus_trajectory):
            raise ValueError("C34_MODIFIED_DELTA_VALUES_MUST_BE_POSITIVE")
        if not self.frozen_before_results or not self.source_predicted_trajectory_only:
            raise ValueError("C34_ONE_LOOP_PLAN_NOT_FROZEN_INDEPENDENTLY")


@dataclass(frozen=True)
class SoftOneLoopOrder(_ContentAddressed):
    order_id: str
    coupling_order: str
    perturbative_order: str
    coupling_normalization: str
    target_coefficient_convention: str
    target_convention_proved: bool
    finite_basis_interaction_normalization_proved: bool
    first_omitted_order: str

    def __post_init__(self) -> None:
        if (self.coupling_order, self.perturbative_order) != ("O(g_s^2)", "O(a_s)"):
            raise ValueError("C34_ONE_LOOP_ORDER_MISMATCH")
        if self.coupling_normalization != C34_COUPLING_NORMALIZATION:
            raise ValueError("C34_COUPLING_NORMALIZATION_MISMATCH")
        if self.target_coefficient_convention != C34_TARGET_SOFT_EXPANSION:
            raise ValueError("C34_TARGET_SOFT_EXPANSION_CONVENTION_MISMATCH")
        if not self.target_convention_proved:
            raise ValueError("C34_SOURCE_TARGET_COUPLING_CONVENTION_NOT_PROVED")
        if self.finite_basis_interaction_normalization_proved:
            raise ValueError(
                "C34_FINITE_BASIS_INTERACTION_NORMALIZATION_PREMATURELY_PROVED"
            )
        if self.first_omitted_order != "O(a_s^2)":
            raise ValueError("C34_FIRST_OMITTED_ORDER_MISMATCH")


@dataclass(frozen=True)
class SoftModeCellId(_ContentAddressed):
    cell_id: str
    resolution_id: str
    rapidity_region: str
    omega_interval: Tuple[float, float]
    rapidity_interval: Tuple[float, float]
    kx_interval: Tuple[float, float]
    ky_interval: Tuple[float, float]
    exact_zero_mode: bool
    primary_basis_cell: bool
    geometry_status: str
    physical_coefficient_eligible: bool
    source_identity: str

    def __post_init__(self) -> None:
        if self.rapidity_region not in ("n", "nbar"):
            raise ValueError("C34_MODE_CELL_RAPIDITY_REGION_INVALID")
        for interval in (
            self.omega_interval,
            self.rapidity_interval,
            self.kx_interval,
            self.ky_interval,
        ):
            if len(interval) != 2 or not all(math.isfinite(x) for x in interval):
                raise ValueError("C34_MODE_CELL_NONFINITE_INTERVAL")
            if interval[0] >= interval[1]:
                raise ValueError("C34_MODE_CELL_INTERVAL_NOT_ORDERED")
        if self.omega_interval[0] < 0.0:
            raise ValueError("C34_MODE_CELL_NEGATIVE_ENERGY")
        if self.exact_zero_mode and self.primary_basis_cell:
            raise ValueError("C34_ZERO_MODE_SILENTLY_INCLUDED_IN_PRIMARY_BASIS")
        if not self.geometry_status or not self.source_identity:
            raise ValueError("C34_MODE_CELL_GEOMETRY_PROVENANCE_MISSING")
        if self.geometry_status == "VALIDATION_ONLY_NONPHYSICAL_CELL":
            if self.primary_basis_cell:
                raise ValueError("C34_VALIDATION_CELL_CANNOT_BE_PRIMARY_BASIS_CELL")
            if self.physical_coefficient_eligible:
                raise ValueError("C34_VALIDATION_CELL_CANNOT_ENTER_PHYSICAL_COEFFICIENT")


@dataclass(frozen=True)
class SoftModeQuadrature(_ContentAddressed):
    quadrature_id: str
    method: str
    orders_per_axis: Tuple[int, int, int, int]
    singular_cell_treatment: str
    cell_integration_required: bool
    cell_integration_executed: bool
    regular_cell_rule_frozen: bool
    singular_formula_proved: bool
    mode_measure_proved: bool
    tolerances_frozen: bool
    cell_center_only: bool
    physical_numerical_epsilon: bool
    frozen_before_results: bool
    integrated_physical_cell_count: int
    physical_coefficient_eligible: bool
    status: ContributionStatus

    def __post_init__(self) -> None:
        if len(self.orders_per_axis) != 4 or min(self.orders_per_axis) <= 0:
            raise ValueError("C34_MODE_QUADRATURE_ORDER_INVALID")
        if not self.cell_integration_required or self.cell_center_only:
            raise ValueError("C34_SINGULAR_CELL_CENTER_SAMPLING_FORBIDDEN")
        if not self.regular_cell_rule_frozen:
            raise ValueError("C34_REGULAR_CELL_QUADRATURE_RULE_NOT_FROZEN")
        if self.physical_numerical_epsilon:
            raise ValueError("C34_NUMERICAL_EPSILON_IS_NOT_PHYSICAL_SUPPORT")
        if not self.frozen_before_results:
            raise ValueError("C34_QUADRATURE_NOT_FROZEN_BEFORE_RESULTS")
        if self.cell_integration_executed and not all(
            (self.singular_formula_proved, self.mode_measure_proved, self.tolerances_frozen)
        ):
            raise ValueError("C34_CELL_INTEGRATION_EXECUTED_WITH_UNPROVED_INPUTS")
        if (
            self.cell_integration_executed
            or self.singular_formula_proved
            or self.mode_measure_proved
            or self.tolerances_frozen
            or self.integrated_physical_cell_count != 0
            or self.physical_coefficient_eligible
        ):
            raise ValueError("C34_UNEXECUTED_QUADRATURE_MARKED_PHYSICALLY_ELIGIBLE")
        _validate_status(self.status, NONZERO_UNKNOWN)


@dataclass(frozen=True)
class SoftModeCompletenessRecord(_ContentAddressed):
    record_id: str
    resolution_id: str
    n_omega: int
    n_rapidity: int
    n_transverse: int
    polarizations: int
    adjoint_colors: int
    vacuum_dimension: int
    one_gluon_dimension: int
    total_dimension: int
    both_rapidity_regions: bool
    exact_zero_mode_separate: bool
    normalization_checked: bool
    completeness_status: ContributionStatus

    def __post_init__(self) -> None:
        expected_one = (
            2  # independent n and nbar rapidity regions
            * self.n_omega
            * self.n_rapidity
            * self.n_transverse
            * self.polarizations
            * self.adjoint_colors
        )
        if self.polarizations != 2 or self.adjoint_colors != 8:
            raise ValueError("C34_SOFT_MODE_INTERNAL_DEGREES_DROPPED")
        if self.vacuum_dimension != 1 or self.one_gluon_dimension != expected_one:
            raise ValueError("C34_SOFT_MODE_DIMENSION_MISMATCH")
        if self.total_dimension != 1 + expected_one:
            raise ValueError("C34_SOFT_HILBERT_DIMENSION_MISMATCH")
        if not self.both_rapidity_regions or not self.exact_zero_mode_separate:
            raise ValueError("C34_SOFT_MODE_REGION_OR_ZERO_CONTROL_MISSING")
        _validate_status(self.completeness_status, NONZERO_UNKNOWN)


@dataclass(frozen=True)
class EikonalEmissionVertex(_ContentAddressed):
    vertex_id: str
    line_id: str
    perturbative_order: str
    coupling_symbol: str
    representation_action: str
    orientation: str
    path_ordering: str
    direction: str
    transverse_position: str
    momentum_flow: int
    delta_component: str
    delta_sign: int
    i0_sign: int
    phase: str
    phase_scope: str
    symbolic_expression: str
    sign_derivation: Tuple[str, ...]
    numerical_current_proofs: RequiredProofSet
    status: ContributionStatus

    def __post_init__(self) -> None:
        if self.line_id not in FOUR_LINE_IDS:
            raise ValueError("C34_EIKONAL_LINE_UNKNOWN")
        if (self.perturbative_order, self.coupling_symbol) != (
            "O(g_s)", C34_EIKONAL_VERTEX_COUPLING
        ):
            raise ValueError("C34_ONE_GLUON_VERTEX_ORDER_OR_COUPLING_MISMATCH")
        if self.representation_action not in ("FUNDAMENTAL", "ANTI_FUNDAMENTAL"):
            raise ValueError("C34_EIKONAL_COLOR_ACTION_INVALID")
        if self.orientation not in ("FUTURE", "PAST"):
            raise ValueError("C34_EIKONAL_ORIENTATION_INVALID")
        if self.path_ordering not in ("P", "ANTI_P"):
            raise ValueError("C34_EIKONAL_PATH_ORDERING_LOST")
        if self.direction not in ("n", "nbar"):
            raise ValueError("C34_EIKONAL_DIRECTION_INVALID")
        expected_delta = "delta_minus" if self.direction == "n" else "delta_plus"
        if self.delta_component != expected_delta:
            raise ValueError("C34_EIKONAL_DELTA_COMPONENT_WRONG")
        if self.transverse_position not in ("0", "b"):
            raise ValueError("C34_EIKONAL_TRANSVERSE_POSITION_LOST")
        if self.momentum_flow not in (-1, 1) or self.delta_sign not in (-1, 1) or self.i0_sign not in (-1, 1):
            raise ValueError("C34_EIKONAL_SIGN_INVALID")
        required = {
            "WILSON_ORIENTATION",
            "FOURIER_CONVENTION",
            "MOMENTUM_FLOW",
            "COVARIANT_DERIVATIVE",
            "LINE_CONJUGATION",
            "MODIFIED_DELTA",
        }
        if not required.issubset(set(self.sign_derivation)):
            raise ValueError("C34_EIKONAL_SIGN_INSERTED_WITHOUT_DERIVATION")
        if not self.symbolic_expression or "epsilon" in self.symbolic_expression.lower():
            raise ValueError("C34_EIKONAL_VERTEX_EXPRESSION_INVALID")
        if self.phase_scope != "TRANSVERSE_BASEPOINT_ONLY_COMPLETE_SEGMENT_UNPROVED":
            raise ValueError("C34_EIKONAL_PHASE_SCOPE_OVERSTATED")
        if self.numerical_current_proofs.required != EIKONAL_NUMERICAL_CURRENT_REQUIREMENTS:
            raise ValueError("C34_EIKONAL_NUMERICAL_REQUIREMENTS_CHANGED")
        if self.numerical_current_proofs.proved != EIKONAL_NUMERICAL_CURRENT_PROVED:
            raise ValueError("C34_EIKONAL_NUMERICAL_PROOF_SCOPE_OVERSTATED")
        _validate_status(self.status, NONZERO_UNKNOWN)

    @property
    def numerical_vertex_proved(self) -> bool:
        return self.numerical_current_proofs.closed and self.status is not ContributionStatus.UNRESOLVED_BLOCKING


@dataclass(frozen=True)
class EikonalAbsorptionVertex(_ContentAddressed):
    vertex_id: str
    emission_vertex_id: str
    line_id: str
    perturbative_order: str
    symbolic_expression: str
    exact_hermitian_conjugate: bool
    conjugates_phase_i0_and_color: bool
    emission_numerical_vertex_proved: bool
    numerical_absorption_vertex_proved: bool
    status: ContributionStatus

    def __post_init__(self) -> None:
        if self.line_id not in FOUR_LINE_IDS:
            raise ValueError("C34_ABSORPTION_LINE_UNKNOWN")
        if self.perturbative_order != "O(g_s)":
            raise ValueError("C34_ONE_GLUON_ABSORPTION_ORDER_MISMATCH")
        if not self.exact_hermitian_conjugate or not self.conjugates_phase_i0_and_color:
            raise ValueError("C34_ABSORPTION_NOT_EXACT_LINE_CONJUGATE")
        _require_identifier(self.symbolic_expression, "C34_ABSORPTION_EXPRESSION_MISSING")
        if self.numerical_absorption_vertex_proved and not self.emission_numerical_vertex_proved:
            raise ValueError("C34_ABSORPTION_PROVED_FROM_UNPROVED_EMISSION_VERTEX")
        _validate_status(self.status, NONZERO_UNKNOWN)


@dataclass(frozen=True)
class EikonalCurrent(_ContentAddressed):
    current_id: str
    line_ids: Tuple[str, ...]
    emission_vertex_ids: Tuple[str, ...]
    perturbative_order: str
    symbolic_expression: str
    coupling_normalization: str
    color_action: str
    transverse_phase: str
    transverse_phase_scope: str
    cell_integration_contract_present: bool
    cell_matrix_elements_executed: bool
    singular_denominator_integrated: bool
    four_line_skeleton_proved: bool
    numerical_current_proofs: RequiredProofSet
    current_status: ContributionStatus
    ward_contraction_status: ContributionStatus

    def __post_init__(self) -> None:
        if self.line_ids != FOUR_LINE_IDS or len(self.emission_vertex_ids) != 4:
            raise ValueError("C34_EIKONAL_CURRENT_REQUIRES_ALL_FOUR_ORDERED_LINES")
        if self.perturbative_order != "O(g_s)":
            raise ValueError("C34_EIKONAL_CURRENT_PERTURBATIVE_ORDER_MISMATCH")
        if self.coupling_normalization != C34_EIKONAL_VERTEX_COUPLING:
            raise ValueError("C34_EIKONAL_CURRENT_COUPLING_MISMATCH")
        if "SUM_ell=1..4" not in self.symbolic_expression:
            raise ValueError("C34_EIKONAL_CURRENT_SYMBOLIC_SUM_MISSING")
        if self.transverse_phase_scope != "TRANSVERSE_BASEPOINT_ONLY_COMPLETE_SEGMENT_UNPROVED":
            raise ValueError("C34_EIKONAL_CURRENT_PHASE_SCOPE_OVERSTATED")
        if not self.cell_integration_contract_present:
            raise ValueError("C34_EIKONAL_CURRENT_CELL_INTEGRATION_CONTRACT_MISSING")
        if self.cell_matrix_elements_executed or self.singular_denominator_integrated:
            raise ValueError("C34_UNCALCULATED_SINGULAR_INTEGRAL_MARKED_COMPLETE")
        if not self.four_line_skeleton_proved:
            raise ValueError("C34_FOUR_LINE_CURRENT_SKELETON_NOT_PROVED")
        if self.numerical_current_proofs.required != EIKONAL_NUMERICAL_CURRENT_REQUIREMENTS:
            raise ValueError("C34_EIKONAL_NUMERICAL_REQUIREMENTS_CHANGED")
        if self.numerical_current_proofs.proved != EIKONAL_NUMERICAL_CURRENT_PROVED:
            raise ValueError("C34_EIKONAL_NUMERICAL_PROOF_SCOPE_OVERSTATED")
        _validate_status(self.current_status, NONZERO_UNKNOWN)
        _validate_status(self.ward_contraction_status, NONZERO_UNKNOWN)

    @property
    def complete_current_proved(self) -> bool:
        return (
            self.numerical_current_proofs.closed
            and self.current_status is not ContributionStatus.UNRESOLVED_BLOCKING
        )


@dataclass(frozen=True)
class EikonalPairKernel(_ContentAddressed):
    kernel_id: str
    line_pair: Tuple[str, str]
    pair_class: str
    color_factor: str
    b_phase: str
    cell_integral_expression: str
    status: ContributionStatus
    proof: str = ""

    def __post_init__(self) -> None:
        if len(self.line_pair) != 2 or any(x not in FOUR_LINE_IDS for x in self.line_pair):
            raise ValueError("C34_EIKONAL_PAIR_IDENTITY_INVALID")
        _validate_status(self.status, self.cell_integral_expression, self.proof)


@dataclass(frozen=True)
class EikonalSelfKernel(_ContentAddressed):
    kernel_id: str
    line_id: str
    line_mass_counterterm_separate: bool
    power_divergence_separate: bool
    expression: str
    status: ContributionStatus
    proof: str = ""

    def __post_init__(self) -> None:
        if self.line_id not in FOUR_LINE_IDS:
            raise ValueError("C34_EIKONAL_SELF_LINE_UNKNOWN")
        if not self.line_mass_counterterm_separate or not self.power_divergence_separate:
            raise ValueError("C34_EIKONAL_SELF_DIVERGENCE_HIDDEN")
        _validate_status(self.status, self.expression, self.proof)


@dataclass(frozen=True)
class TransverseClosureKernel(_ContentAddressed):
    kernel_id: str
    closure_id: str
    infinity_junction_separate: bool
    endpoint_separate: bool
    expression: str
    status: ContributionStatus
    proof: str = ""

    def __post_init__(self) -> None:
        if not self.infinity_junction_separate or not self.endpoint_separate:
            raise ValueError("C34_TRANSVERSE_CLOSURE_OWNERSHIP_MERGED")
        _validate_status(self.status, self.expression, self.proof)


@dataclass(frozen=True)
class SoftVirtualAmplitude(_ContentAddressed):
    amplitude_id: str
    operator_expansion_order: str
    line_pair_ids: Tuple[str, ...]
    support: str
    expression: str
    status: ContributionStatus
    proof: str = ""

    def __post_init__(self) -> None:
        _validate_status(self.status, self.expression, self.proof)


@dataclass(frozen=True)
class SoftRealAmplitude(_ContentAddressed):
    amplitude_id: str
    cut_id: str
    mode_cell_ids: Tuple[str, ...]
    support: str
    b_dependent_phase: str
    expression: str
    status: ContributionStatus
    proof: str = ""

    def __post_init__(self) -> None:
        _validate_status(self.status, self.expression, self.proof)


@dataclass(frozen=True)
class SoftCutLedger(_ContentAddressed):
    ledger_id: str
    cut_ids: Tuple[str, ...]
    real_ids: Tuple[str, ...]
    virtual_ids: Tuple[str, ...]
    duplicate_cut_residual: Optional[float]
    numerical_epsilon_used_as_support: bool
    status: ContributionStatus

    def __post_init__(self) -> None:
        if len(set(self.cut_ids)) != len(self.cut_ids):
            raise ValueError("C34_DUPLICATE_CUT_ID")
        if self.numerical_epsilon_used_as_support:
            raise ValueError("C34_NUMERICAL_EPSILON_USED_AS_CUT_SUPPORT")
        _validate_status(self.status, NONZERO_UNKNOWN)


@dataclass(frozen=True)
class SoftRealVirtualAssembly(_ContentAddressed):
    assembly_id: str
    direct_wilson_route_id: str
    mode_sum_route_id: str
    real_counted_once: bool
    virtual_counted_once: bool
    conjugate_pairs_counted_once: bool
    direct_mode_sum_residual: Optional[float]
    missing_real_residual: Optional[float]
    missing_virtual_residual: Optional[float]
    duplicate_cut_residual: Optional[float]
    future_past_residual: Optional[float]
    hermiticity_residual: Optional[float]
    b_rotation_residual: Optional[float]
    status: ContributionStatus

    def __post_init__(self) -> None:
        if self.status is ContributionStatus.UNRESOLVED_BLOCKING:
            if any((self.real_counted_once, self.virtual_counted_once, self.conjugate_pairs_counted_once)):
                raise ValueError("C34_UNRESOLVED_ASSEMBLY_CANNOT_CLAIM_COUNT_ONCE")
            _validate_status(self.status, NONZERO_UNKNOWN)
        else:
            if not all((self.real_counted_once, self.virtual_counted_once, self.conjugate_pairs_counted_once)):
                raise ValueError("C34_REAL_VIRTUAL_COUNT_ONCE_NOT_CLOSED")


@dataclass(frozen=True)
class SoftGaugeContribution(_ContentAddressed):
    contribution_id: str
    xi_values: Tuple[float, ...]
    expression: str
    gauge_residual: Optional[float]
    status: ContributionStatus

    def __post_init__(self) -> None:
        if self.xi_values != (0.0, 1.0, 2.0):
            raise ValueError("C34_GAUGE_AXIS_INCOMPLETE")
        _validate_status(self.status, self.expression)


@dataclass(frozen=True)
class SoftGhostContribution(_ContentAddressed):
    contribution_id: str
    covariant_gauge: bool
    expression: str
    status: ContributionStatus
    proof: str = ""

    def __post_init__(self) -> None:
        _validate_status(self.status, self.expression, self.proof)


@dataclass(frozen=True)
class SoftInstantaneousContribution(_ContentAddressed):
    contribution_id: str
    light_front_operator_class: str
    expression: str
    status: ContributionStatus
    proof: str = ""

    def __post_init__(self) -> None:
        _validate_status(self.status, self.expression, self.proof)


@dataclass(frozen=True)
class SoftZeroModeContribution(_ContentAddressed):
    contribution_id: str
    policy: str
    retained_as_separate_control: bool
    expression: str
    status: ContributionStatus
    proof: str = ""

    def __post_init__(self) -> None:
        if self.policy != "EXCLUDE_PRIMARY_RETAIN_SEPARATE_CONTROL":
            raise ValueError("C34_C33_ZERO_MODE_POLICY_CHANGED")
        if not self.retained_as_separate_control:
            raise ValueError("C34_ZERO_MODE_CONTROL_SILENTLY_DISCARDED")
        _validate_status(self.status, self.expression, self.proof)


@dataclass(frozen=True)
class SoftBoundaryContribution(_ContentAddressed):
    contribution_id: str
    boundary_identity: str
    basis_boundary_separate: bool
    endpoint_separate: bool
    transverse_junction_separate: bool
    expression: str
    status: ContributionStatus
    proof: str = ""

    def __post_init__(self) -> None:
        if self.boundary_identity != "FINITE_CELL/PERIODIC/TRANSVERSE_CLOSED/COVARIANT":
            raise ValueError("C34_C33_BOUNDARY_IDENTITY_CHANGED")
        if not all((self.basis_boundary_separate, self.endpoint_separate, self.transverse_junction_separate)):
            raise ValueError("C34_BOUNDARY_CONTRIBUTIONS_NOT_SEPARATELY_OWNED")
        _validate_status(self.status, self.expression, self.proof)


@dataclass(frozen=True)
class SoftBareCoefficient(_ContentAddressed):
    coefficient_id: str
    operator_id: str
    tree_value: Fraction
    perturbative_order: str
    coupling_normalization: str
    target_coefficient_convention: str
    color_factor_placement: str
    finite_basis_interaction_normalization_proved: bool
    first_omitted_order: str
    component_ids: Tuple[str, ...]
    separate_control_ids: Tuple[str, ...]
    alternative_route_ids: Tuple[str, ...]
    counterterm_decision_ids: Tuple[str, ...]
    derived_counterterm_ids: Tuple[str, ...]
    expression: str
    status: ContributionStatus
    all_direct_bare_components_resolved: bool
    separate_control_assembly_decisions_resolved: bool
    retains_delta_plus_minus: bool
    retains_gauge_and_basis_identity: bool

    def __post_init__(self) -> None:
        if self.tree_value != Fraction(1, 1):
            raise ValueError("C34_C33_TREE_IDENTITY_CHANGED")
        if self.perturbative_order != "O(a_s)":
            raise ValueError("C34_BARE_SOFT_PERTURBATIVE_ORDER_MISMATCH")
        if self.coupling_normalization != C34_COUPLING_NORMALIZATION:
            raise ValueError("C34_BARE_SOFT_COUPLING_CONVENTION_MISMATCH")
        if self.target_coefficient_convention != C34_TARGET_SOFT_EXPANSION:
            raise ValueError("C34_BARE_SOFT_TARGET_EXPANSION_MISMATCH")
        if self.color_factor_placement != "EXTERNAL_TO_REDUCED_S^[1]":
            raise ValueError("C34_BARE_SOFT_COLOR_FACTOR_PLACEMENT_AMBIGUOUS")
        if self.finite_basis_interaction_normalization_proved:
            raise ValueError(
                "C34_FINITE_BASIS_INTERACTION_NORMALIZATION_PREMATURELY_PROVED"
            )
        if self.first_omitted_order != "O(a_s^2)":
            raise ValueError("C34_BARE_SOFT_FIRST_OMITTED_ORDER_MISMATCH")
        if self.component_ids != DIRECT_BARE_COMPONENT_IDS:
            raise ValueError("C34_BARE_SOFT_DIRECT_COMPONENT_SET_MISMATCH")
        if self.separate_control_ids != SEPARATE_CONTROL_COMPONENT_IDS:
            raise ValueError("C34_BARE_SOFT_CONTROL_SET_MISMATCH")
        if self.alternative_route_ids != ALTERNATIVE_ROUTE_COMPONENT_IDS:
            raise ValueError("C34_BARE_SOFT_ALTERNATIVE_SET_MISMATCH")
        if self.counterterm_decision_ids != COUNTERTERM_DECISION_COMPONENT_IDS:
            raise ValueError("C34_BARE_SOFT_COUNTERTERM_SET_MISMATCH")
        if self.derived_counterterm_ids != DERIVED_COUNTERTERM_IDS:
            raise ValueError("C34_BARE_SOFT_DERIVED_COUNTERTERM_SET_MISMATCH")
        if set(self.derived_counterterm_ids) & set(CONTRIBUTION_ID_BY_CLASS.values()):
            raise ValueError("C34_DERIVED_COUNTERTERM_ID_ALIASES_CONTRIBUTION_ID")
        partitions = (
            set(self.component_ids),
            set(self.separate_control_ids),
            set(self.alternative_route_ids),
            set(self.counterterm_decision_ids),
        )
        if any(partitions[i] & partitions[j] for i in range(4) for j in range(i + 1, 4)):
            raise ValueError("C34_BARE_SOFT_COMPONENT_ROLE_OVERLAP")
        if set().union(*partitions) != set(CONTRIBUTION_ID_BY_CLASS.values()):
            raise ValueError("C34_BARE_SOFT_COMPONENT_PARTITION_INCOMPLETE")
        if not self.retains_delta_plus_minus or not self.retains_gauge_and_basis_identity:
            raise ValueError("C34_BARE_SOFT_REGULATOR_IDENTITY_DROPPED")
        if not (
            self.all_direct_bare_components_resolved
            and self.separate_control_assembly_decisions_resolved
        ):
            _validate_status(ContributionStatus.UNRESOLVED_BLOCKING, self.expression)
            if self.status is not ContributionStatus.UNRESOLVED_BLOCKING:
                raise ValueError("C34_BARE_SOFT_PREMATURE_POSITIVE_STATUS")
        else:
            _validate_status(self.status, self.expression)

    @property
    def one_loop_validated(self) -> bool:
        return (
            self.all_direct_bare_components_resolved
            and self.separate_control_assembly_decisions_resolved
            and self.status is not ContributionStatus.UNRESOLVED_BLOCKING
        )


@dataclass(frozen=True)
class SoftBareCoefficientDecomposition(_ContentAddressed):
    decomposition_id: str
    coefficient_id: str
    contributions: Tuple[SoftContributionResult, ...]
    direct_bare_component_ids: Tuple[str, ...]
    separate_control_ids: Tuple[str, ...]
    alternative_route_ids: Tuple[str, ...]
    counterterm_decision_ids: Tuple[str, ...]
    derived_counterterm_ids: Tuple[str, ...]
    every_required_class_present: bool
    all_direct_bare_resolved: bool
    all_separate_control_decisions_resolved: bool
    all_counterterm_decisions_resolved: bool
    all_resolved: bool

    def __post_init__(self) -> None:
        classes = tuple(item.contribution_class for item in self.contributions)
        if classes != REQUIRED_ONE_LOOP_CONTRIBUTIONS:
            raise ValueError("C34_ONE_LOOP_LEDGER_ORDER_OR_COMPLETENESS_FAILURE")
        expected_partitions = (
            DIRECT_BARE_COMPONENT_IDS,
            SEPARATE_CONTROL_COMPONENT_IDS,
            ALTERNATIVE_ROUTE_COMPONENT_IDS,
            COUNTERTERM_DECISION_COMPONENT_IDS,
        )
        actual_partitions = (
            self.direct_bare_component_ids,
            self.separate_control_ids,
            self.alternative_route_ids,
            self.counterterm_decision_ids,
        )
        if actual_partitions != expected_partitions:
            raise ValueError("C34_ONE_LOOP_DECOMPOSITION_ROLE_PARTITION_MISMATCH")
        if self.derived_counterterm_ids != DERIVED_COUNTERTERM_IDS:
            raise ValueError("C34_ONE_LOOP_DECOMPOSITION_COUNTERTERM_IDS_MISMATCH")
        if set(self.derived_counterterm_ids) & set().union(
            *(set(items) for items in actual_partitions)
        ):
            raise ValueError("C34_ONE_LOOP_DECOMPOSITION_COUNTERTERM_ID_ALIAS")
        resolved_by_class = {
            item.contribution_class: item.resolved for item in self.contributions
        }
        direct_resolved = all(
            resolved_by_class[name] for name in DIRECT_BARE_CONTRIBUTIONS
        )
        controls_resolved = all(
            resolved_by_class[name] for name in SEPARATE_CONTROL_CONTRIBUTIONS
        )
        counterterms_resolved = all(
            resolved_by_class[name] for name in COUNTERTERM_DECISION_CONTRIBUTIONS
        )
        computed = all(item.resolved for item in self.contributions)
        if (
            self.every_required_class_present is not True
            or self.all_direct_bare_resolved != direct_resolved
            or self.all_separate_control_decisions_resolved != controls_resolved
            or self.all_counterterm_decisions_resolved != counterterms_resolved
            or self.all_resolved != computed
        ):
            raise ValueError("C34_ONE_LOOP_DECOMPOSITION_STATUS_INCONSISTENT")


@dataclass(frozen=True)
class SoftUVStructure(_ContentAddressed):
    structure_id: str
    power_term: str
    logarithmic_term: str
    cusp_term: str
    finite_term: str
    power_remainder: str
    schema_fields_separate: bool
    numerical_decomposition_completed: bool
    status: ContributionStatus

    def __post_init__(self) -> None:
        if not self.schema_fields_separate:
            raise ValueError("C34_UV_POWER_LOG_STRUCTURE_MERGED")
        if (
            self.status is ContributionStatus.UNRESOLVED_BLOCKING
            and self.numerical_decomposition_completed
        ):
            raise ValueError("C34_UNRESOLVED_UV_STRUCTURE_MARKED_NUMERICALLY_DECOMPOSED")
        if (
            self.status is not ContributionStatus.UNRESOLVED_BLOCKING
            and not self.numerical_decomposition_completed
        ):
            raise ValueError("C34_RESOLVED_UV_STRUCTURE_LACKS_NUMERICAL_DECOMPOSITION")
        _validate_status(self.status, NONZERO_UNKNOWN)


@dataclass(frozen=True)
class SoftRapidityStructure(_ContentAddressed):
    structure_id: str
    delta_plus_term: str
    delta_minus_term: str
    combined_log_term: str
    removal_order: Tuple[str, ...]
    delta_components_aliased: bool
    status: ContributionStatus

    def __post_init__(self) -> None:
        if self.delta_components_aliased:
            raise ValueError("C34_DELTA_PLUS_MINUS_ALIASED")
        if self.removal_order != ("ASSEMBLE_REAL_VIRTUAL", "UV_RENORMALIZE", "RAPIDITY_RENORMALIZE", "REMOVE_DELTA"):
            raise ValueError("C34_RAPIDITY_REGULATOR_REMOVAL_ORDER_WRONG")
        _validate_status(self.status, NONZERO_UNKNOWN)


@dataclass(frozen=True)
class SoftUVCountertermSolution(_ContentAddressed):
    solution_id: str
    owner_ids: Tuple[str, ...]
    power_counterterm_slots_separate: bool
    power_log_separation_proved: bool
    state_independence_required: bool
    state_independence_proved: bool
    inverse_available: bool
    expression: str
    holdout_residual: Optional[float]
    first_omitted_order: str
    status: ContributionStatus

    def __post_init__(self) -> None:
        if not self.power_counterterm_slots_separate or not self.state_independence_required:
            raise ValueError("C34_UV_COUNTERTERM_OWNERSHIP_OR_REQUIREMENT_FAILURE")
        if (
            self.status is ContributionStatus.UNRESOLVED_BLOCKING
            and self.power_log_separation_proved
        ):
            raise ValueError("C34_UNRESOLVED_UV_COUNTERTERM_POWER_LOG_PROOF_OVERSTATED")
        if (
            self.status is ContributionStatus.UNRESOLVED_BLOCKING
            and self.state_independence_proved
        ):
            raise ValueError("C34_UNRESOLVED_UV_COUNTERTERM_UNIVERSALITY_OVERSTATED")
        if (
            self.status is not ContributionStatus.UNRESOLVED_BLOCKING
            and not self.state_independence_proved
        ):
            raise ValueError("C34_RESOLVED_UV_COUNTERTERM_UNIVERSALITY_UNPROVED")
        _validate_status(self.status, self.expression)


@dataclass(frozen=True)
class SoftRapidityCountertermSolution(_ContentAddressed):
    solution_id: str
    regulator_id: str
    derivative_variable: str
    state_independence_required: bool
    state_independence_proved: bool
    fitted_nonperturbative_term: bool
    expression: str
    regulator_residual: Optional[float]
    gauge_residual: Optional[float]
    status: ContributionStatus

    def __post_init__(self) -> None:
        if self.regulator_id != C33_RAPIDITY_REGULATOR_ID:
            raise ValueError("C34_RAPIDITY_COUNTERTERM_REGULATOR_MISMATCH")
        if not self.derivative_variable or not self.state_independence_required:
            raise ValueError("C34_RAPIDITY_COUNTERTERM_IDENTITY_MISSING")
        if self.fitted_nonperturbative_term:
            raise ValueError("C34_FITTED_CS_TERM_FORBIDDEN")
        if (
            self.status is ContributionStatus.UNRESOLVED_BLOCKING
            and self.state_independence_proved
        ):
            raise ValueError("C34_UNRESOLVED_RAPIDITY_COUNTERTERM_UNIVERSALITY_OVERSTATED")
        if (
            self.status is not ContributionStatus.UNRESOLVED_BLOCKING
            and not self.state_independence_proved
        ):
            raise ValueError("C34_RESOLVED_RAPIDITY_COUNTERTERM_UNIVERSALITY_UNPROVED")
        _validate_status(self.status, self.expression)


@dataclass(frozen=True)
class SoftRenormalizedCoefficient(_ContentAddressed):
    coefficient_id: str
    bare_coefficient_id: str
    uv_solution_id: str
    rapidity_solution_id: str
    expression: str
    uv_residual: Optional[float]
    rapidity_residual: Optional[float]
    gauge_residual: Optional[float]
    status: ContributionStatus

    def __post_init__(self) -> None:
        _validate_status(self.status, self.expression)

    @property
    def validated(self) -> bool:
        return (
            self.status is not ContributionStatus.UNRESOLVED_BLOCKING
            and self.uv_residual == 0.0
            and self.rapidity_residual == 0.0
            and self.gauge_residual == 0.0
        )


@dataclass(frozen=True)
class SoftRapidityDerivative(_ContentAddressed):
    derivative_id: str
    source_coefficient_id: str
    derivative_variable: str
    convention: str
    expression: str
    status: ContributionStatus

    def __post_init__(self) -> None:
        _require_identifier(self.derivative_variable, "C34_RAPIDITY_DERIVATIVE_VARIABLE_MISSING")
        _validate_status(self.status, self.expression)


@dataclass(frozen=True)
class SoftCuspConsistency(_ContentAddressed):
    consistency_id: str
    rapidity_derivative_id: str
    cusp_convention: str
    expected_expression: str
    residual: Optional[float]
    status: ContributionStatus

    def __post_init__(self) -> None:
        _validate_status(self.status, NONZERO_UNKNOWN)


@dataclass(frozen=True)
class SoftCSKernelRecord(_ContentAddressed):
    kernel_id: str
    convention: str
    relation_to_soft_rapidity_dimension: str
    art25_nonperturbative_model_used: bool
    expression: str
    status: ContributionStatus

    def __post_init__(self) -> None:
        if self.art25_nonperturbative_model_used:
            raise ValueError("C34_ART25_CS_MODEL_FORBIDDEN")
        _validate_status(self.status, self.expression)


@dataclass(frozen=True)
class SoftContinuumTargetRecord(_ContentAddressed):
    target_id: str
    scheme: str
    source_id: str
    source_file_sha256: str
    source_locator: str
    source_route: str
    reconstruction_route: str
    source_expression: str
    source_expression_hash: str
    source_laurent_expression: str
    source_laurent_expression_hash: str
    reconstruction_expression_hash: Optional[str]
    coupling_normalization: str
    coefficient_convention: str
    color_factor_placement: str
    oracle_proofs: RequiredProofSet
    convention_aligned: bool
    finite_basis_result: bool
    expression: str
    status: ContributionStatus

    def __post_init__(self) -> None:
        if not self.source_route or not self.reconstruction_route:
            raise ValueError("C34_TWO_CONTINUUM_ORACLE_ROUTES_REQUIRED")
        if (
            self.source_id != C34_CONTINUUM_SOURCE_ID
            or self.source_file_sha256 != C34_CONTINUUM_SOURCE_FILE_SHA256
            or self.source_locator != C34_CONTINUUM_SOURCE_LOCATOR
        ):
            raise ValueError("C34_CONTINUUM_SOURCE_IDENTITY_OR_HASH_MISMATCH")
        if (
            self.source_expression != C34_CONTINUUM_NLO_SOURCE_EXPRESSION
            or self.source_expression_hash
            != C34_CONTINUUM_NLO_SOURCE_EXPRESSION_SHA256
            or sha256(self.source_expression.encode("ascii")).hexdigest()
            != self.source_expression_hash
        ):
            raise ValueError("C34_CONTINUUM_SOURCE_EXPRESSION_OR_HASH_MISMATCH")
        if (
            self.source_laurent_expression
            != C34_CONTINUUM_NLO_LAURENT_EXPRESSION
            or self.source_laurent_expression_hash
            != C34_CONTINUUM_NLO_LAURENT_EXPRESSION_SHA256
            or sha256(self.source_laurent_expression.encode("ascii")).hexdigest()
            != self.source_laurent_expression_hash
        ):
            raise ValueError("C34_CONTINUUM_LAURENT_EXPRESSION_OR_HASH_MISMATCH")
        if self.coupling_normalization != C34_COUPLING_NORMALIZATION:
            raise ValueError("C34_CONTINUUM_COUPLING_CONVENTION_MISMATCH")
        if self.coefficient_convention != C34_TARGET_SOFT_EXPANSION:
            raise ValueError("C34_CONTINUUM_COEFFICIENT_CONVENTION_MISMATCH")
        if self.color_factor_placement != "EXTERNAL_TO_REDUCED_S^[1]":
            raise ValueError("C34_CONTINUUM_COLOR_FACTOR_PLACEMENT_AMBIGUOUS")
        if self.oracle_proofs.required != CONTINUUM_ORACLE_REQUIREMENTS:
            raise ValueError("C34_CONTINUUM_ORACLE_REQUIREMENTS_CHANGED")
        if self.oracle_proofs.proved != CONTINUUM_ORACLE_PROVED:
            raise ValueError("C34_CONTINUUM_ORACLE_PROOF_SCOPE_OVERSTATED")
        if self.reconstruction_expression_hash is not None:
            raise ValueError("C34_UNEXECUTED_CONTINUUM_RECONSTRUCTION_HAS_HASH")
        if self.convention_aligned:
            raise ValueError("C34_CONTINUUM_CONVENTION_ALIGNMENT_PREMATURE")
        if self.finite_basis_result:
            raise ValueError("C34_CONTINUUM_TARGET_IS_NOT_FINITE_BASIS_RESULT")
        _validate_status(self.status, self.expression)

    @property
    def source_transcription_proved(self) -> bool:
        return all(
            item in self.oracle_proofs.proved
            for item in (
                "SOURCE_FILE_HASH",
                "SOURCE_EQUATION_TRANSCRIPTION",
                "SOURCE_EXPRESSION_HASH",
                "COUPLING_AND_COLOR_CONVENTION",
            )
        )

    @property
    def independently_validated(self) -> bool:
        return self.oracle_proofs.closed and self.status is not ContributionStatus.UNRESOLVED_BLOCKING


@dataclass(frozen=True)
class SoftFiniteRegulatorDifference(_ContentAddressed):
    difference_id: str
    continuum_target_id: str
    finite_basis_coefficient_id: str
    logarithmic_part: str
    finite_constant: str
    power_part: str
    zero_mode_remainder: str
    numerical_remainder: str
    expression: str
    status: ContributionStatus

    def __post_init__(self) -> None:
        _validate_status(self.status, self.expression)


@dataclass(frozen=True)
class SoftFiniteRegulatorKernel(_ContentAddressed):
    kernel_id: str
    difference_id: str
    state_independence_required: bool
    state_independence_proved: bool
    hadron_independence_required: bool
    hadron_independence_proved: bool
    flavor_independence_required_where_applicable: bool
    flavor_independence_proved: bool
    art25_member_independence_required: bool
    art25_member_independence_proved: bool
    gauge_independence_required: bool
    gauge_independence_proved: bool
    resolution_dependence_required: bool
    resolution_dependence_explicit: bool
    first_omitted_order: str
    expression: str
    status: ContributionStatus

    def __post_init__(self) -> None:
        if not all(
            (
                self.state_independence_required,
                self.hadron_independence_required,
                self.flavor_independence_required_where_applicable,
                self.art25_member_independence_required,
                self.gauge_independence_required,
                self.resolution_dependence_required,
            )
        ):
            raise ValueError("C34_SOFT_CONVERSION_UNIVERSALITY_REQUIREMENT_DROPPED")
        if not self.art25_member_independence_proved:
            raise ValueError("C34_SOFT_CONVERSION_ART25_ISOLATION_NOT_PROVED")
        physics_proofs = (
            self.state_independence_proved,
            self.hadron_independence_proved,
            self.flavor_independence_proved,
            self.gauge_independence_proved,
            self.resolution_dependence_explicit,
        )
        if self.status is ContributionStatus.UNRESOLVED_BLOCKING and any(physics_proofs):
            raise ValueError("C34_UNRESOLVED_SOFT_CONVERSION_UNIVERSALITY_OVERSTATED")
        if self.status is not ContributionStatus.UNRESOLVED_BLOCKING and not all(physics_proofs):
            raise ValueError("C34_RESOLVED_SOFT_CONVERSION_UNIVERSALITY_UNPROVED")
        _validate_status(self.status, self.expression)


@dataclass(frozen=True)
class SoftRoundTripReport(_ContentAddressed):
    report_id: str
    kernel_id: str
    inverse_defined: bool
    roundtrip_residual: Optional[float]
    continuum_recovery_residual: Optional[float]
    holdout_residual: Optional[float]
    status: ContributionStatus

    def __post_init__(self) -> None:
        _validate_status(self.status, NONZERO_UNKNOWN)


@dataclass(frozen=True)
class SoftResolutionSequence(_ContentAddressed):
    sequence_id: str
    resolution_ids: Tuple[str, ...]
    resolution_tuples: Tuple[Tuple[int, int, int], ...]
    dimensions: Tuple[int, ...]
    c33_descriptor_nesting_declared: bool
    nominal_support_extension_monotone: bool
    refinement_proofs: RequiredProofSet
    all_executed: bool

    def __post_init__(self) -> None:
        if self.resolution_ids != ("C33.RES.1", "C33.RES.2", "C33.RES.3"):
            raise ValueError("C34_C33_RESOLUTION_IDENTITIES_CHANGED")
        if self.resolution_tuples != ((4, 6, 5), (8, 12, 10), (12, 18, 15)):
            raise ValueError("C34_C33_RESOLUTION_SEQUENCE_CHANGED")
        if self.dimensions != (3841, 30721, 103681):
            raise ValueError("C34_C33_RESOLUTION_DIMENSIONS_CHANGED")
        if not self.c33_descriptor_nesting_declared or not self.nominal_support_extension_monotone:
            raise ValueError("C34_C33_DESCRIPTOR_SUPPORT_ORDER_CHANGED")
        if self.refinement_proofs.required != RESOLUTION_REFINEMENT_REQUIREMENTS:
            raise ValueError("C34_RESOLUTION_REFINEMENT_REQUIREMENTS_CHANGED")
        if self.refinement_proofs.proved != RESOLUTION_REFINEMENT_PROVED:
            raise ValueError("C34_RESOLUTION_REFINEMENT_SCOPE_OVERSTATED")
        if self.refinement_proofs.closed:
            raise ValueError("C34_UNAVAILABLE_REFINEMENT_MAPS_PREMATURELY_PROVED")

    @property
    def exact_cell_refinement_proved(self) -> bool:
        return "EXACT_SUCCESSIVE_INJECTION_OR_REFINEMENT_MAPS" in self.refinement_proofs.proved

    @property
    def common_continuum_limit_proved(self) -> bool:
        return "DECLARED_COMMON_CONTINUUM_LIMIT" in self.refinement_proofs.proved


@dataclass(frozen=True)
class SoftTrajectoryFitPlan(_ContentAddressed):
    plan_id: str
    allowed_structures: Tuple[str, ...]
    free_coefficient_count: int
    construction_resolution_ids: Tuple[str, ...]
    holdout_resolution_ids: Tuple[str, ...]
    frozen_before_results: bool
    arbitrary_polynomial_forbidden: bool

    def __post_init__(self) -> None:
        if not self.frozen_before_results or not self.arbitrary_polynomial_forbidden:
            raise ValueError("C34_TRAJECTORY_PLAN_NOT_FROZEN_OR_SOURCE_PREDICTED")
        if self.free_coefficient_count > len(self.construction_resolution_ids):
            raise ValueError("C34_TRAJECTORY_OVERFIT")
        if set(self.construction_resolution_ids) & set(self.holdout_resolution_ids):
            raise ValueError("C34_TRAJECTORY_HOLDOUT_LEAKAGE")


@dataclass(frozen=True)
class SoftTrajectoryHoldout(_ContentAddressed):
    holdout_id: str
    axis: str
    value_identity: str
    frozen_before_simplification: bool
    used_in_construction: bool
    residual: Optional[float]

    def __post_init__(self) -> None:
        if not self.frozen_before_simplification or self.used_in_construction:
            raise ValueError("C34_TRAJECTORY_HOLDOUT_USED_IN_CONSTRUCTION")


@dataclass(frozen=True)
class SoftTrajectoryResult(_ContentAddressed):
    result_id: str
    sequence_id: str
    fit_plan_id: str
    holdout_ids: Tuple[str, ...]
    logarithmic_finite_power_separated: bool
    status: SoftTrajectoryStatus
    exact_missing_calculation: str

    @property
    def supports_continuum_claim(self) -> bool:
        return (
            self.status is SoftTrajectoryStatus.RESOLVED
            and self.logarithmic_finite_power_separated
            and not self.exact_missing_calculation
        )


@dataclass(frozen=True)
class SoftSideZeroBinLimit(_ContentAddressed):
    limit_id: str
    measurement_id: str
    b_coordinate_convention: str
    rapidity_convention: str
    uv_target: str
    gauge_convention: str
    offshell_ir_variables: Tuple[str, ...]
    regulator_removal_order: Tuple[str, ...]
    coefficient_expression: str
    status: SoftCollinearStatus

    def __post_init__(self) -> None:
        if self.status is not SoftCollinearStatus.UNRESOLVED and self.coefficient_expression == NONZERO_UNKNOWN:
            raise ValueError("C34_ZERO_BIN_OBJECT_PREMATURE_READINESS")


@dataclass(frozen=True)
class SoftCollinearContinuationContract(_ContentAddressed):
    contract_id: str
    soft_limit_id: str
    c32_collinear_plan_id: str
    common_measurement: bool
    common_b_convention: bool
    common_uv_target: bool
    common_gauge: bool
    exact_offshell_conversion_proved: bool
    citation_only_equivalence_claimed: bool
    status: SoftCollinearStatus

    def __post_init__(self) -> None:
        if self.citation_only_equivalence_claimed:
            raise ValueError("C34_ZERO_BIN_EQUIVALENCE_FROM_CITATION_FORBIDDEN")
        if self.status in (
            SoftCollinearStatus.EXACT_CONVERSION_READY,
            SoftCollinearStatus.READY_FOR_IDENTICAL_TEST,
        ) and not all(
            (
                self.common_measurement,
                self.common_b_convention,
                self.common_uv_target,
                self.common_gauge,
                self.exact_offshell_conversion_proved,
            )
        ):
            raise ValueError("C34_SOFT_COLLINEAR_CONTINUATION_PREMATURE")


@dataclass(frozen=True)
class C34SoftCapabilityMatrix(_ContentAddressed):
    matrix_id: str
    total_capabilities: int
    validated_capabilities: int
    blocking_capabilities: int
    strongest_status: str

    def __post_init__(self) -> None:
        if self.total_capabilities < 0 or self.validated_capabilities < 0 or self.blocking_capabilities < 0:
            raise ValueError("C34_CAPABILITY_COUNT_INVALID")
        if self.validated_capabilities + self.blocking_capabilities > self.total_capabilities:
            raise ValueError("C34_CAPABILITY_COUNT_OVERFLOW")


@dataclass(frozen=True)
class C34ClosureReport(_ContentAddressed):
    report_id: str
    c33_tree_boundary_closed: bool
    plan_frozen: bool
    symbolic_eikonal_current_skeleton_typed: bool
    complete_eikonal_current_closed: bool
    singular_cell_integration_closed: bool
    all_one_loop_contributions_resolved: bool
    real_virtual_count_once_closed: bool
    uv_closed: bool
    rapidity_closed: bool
    gauge_closed: bool
    continuum_oracle_closed: bool
    regulator_conversion_closed: bool
    trajectory_closed: bool
    soft_zero_bin_ready: bool
    continuation_ready: bool
    no_go_status: str
    exact_missing_calculation: str
    exact_next_package: str
    microscopic_proton_exported: bool = False
    bridge_rerun: bool = False
    fit_or_inference_created: bool = False
    production_promoted: bool = False

    def __post_init__(self) -> None:
        if any(
            (
                self.microscopic_proton_exported,
                self.bridge_rerun,
                self.fit_or_inference_created,
                self.production_promoted,
            )
        ):
            raise ValueError("C34_FORBIDDEN_SCOPE_PROMOTION")
        positive_gates = (
            self.c33_tree_boundary_closed,
            self.plan_frozen,
            self.complete_eikonal_current_closed,
            self.singular_cell_integration_closed,
            self.all_one_loop_contributions_resolved,
            self.real_virtual_count_once_closed,
            self.uv_closed,
            self.rapidity_closed,
            self.gauge_closed,
            self.continuum_oracle_closed,
            self.regulator_conversion_closed,
            self.trajectory_closed,
            self.soft_zero_bin_ready,
        )
        if not self.symbolic_eikonal_current_skeleton_typed:
            raise ValueError("C34_EIKONAL_CURRENT_SKELETON_NOT_TYPED")
        if self.complete_eikonal_current_closed and not self.symbolic_eikonal_current_skeleton_typed:
            raise ValueError("C34_COMPLETE_CURRENT_WITHOUT_TYPED_SKELETON")
        if self.continuation_ready and not all(positive_gates):
            raise ValueError("C34_CONTINUATION_GATE_PREMATURE")
        if not self.continuation_ready:
            if not self.no_go_status or not self.exact_missing_calculation or not self.exact_next_package:
                raise ValueError("C34_NO_GO_REQUIRES_EXACT_MISSING_CALCULATION_AND_BRANCH")
        if self.no_go_status == C34_NO_GO and self.exact_next_package != C34_NEXT_PACKAGE:
            raise ValueError("C34_BRANCH_G_NEXT_PACKAGE_MISMATCH")


def exact_c33_tree_boundary() -> Dict[str, Any]:
    """Return and recheck the immutable C33 tree/color boundary.

    The values are exact rationals.  This oracle is intentionally independent
    of every C34 one-loop coefficient.
    """

    operator = default_four_line_operator()
    tree_value = operator.tree_level_soft_factor
    c_f = operator.color_space.c_f
    if tree_value != Fraction(1, 1) or c_f != Fraction(4, 3):
        raise ValueError("C34_C33_EXACT_TREE_OR_COLOR_BOUNDARY_CHANGED")
    return {
        "operator_id": operator.operator_id,
        "trace_order": operator.trace_order,
        "wilson_geometry": C33_WILSON_GEOMETRY,
        "tree_value": tree_value,
        "c_f": c_f,
        "baryon_number": 0,
        "soft_root_id": C33_SOFT_ROOT,
        "collinear_root_id": C32_COLLINEAR_ROOT,
        "roots_share_state_or_probability_normalization": False,
    }


def normalized_transverse_cell_phase(
    cell: SoftModeCellId, b_transverse: Tuple[float, float]
) -> complex:
    """Exact normalized rectangular-cell integral of ``exp(i k_T.b_T)``.

    This is only the nonsingular transverse phase factor.  It deliberately
    does not evaluate the eikonal pole, rapidity, energy, UV, or zero-mode
    integrals and therefore cannot be used as a one-loop soft coefficient.
    """

    if len(b_transverse) != 2 or not all(math.isfinite(x) for x in b_transverse):
        raise ValueError("C34_TRANSVERSE_COORDINATE_INVALID")

    def axis_average(interval: Tuple[float, float], b_value: float) -> complex:
        lo, hi = interval
        width = hi - lo
        if b_value == 0.0:
            return 1.0 + 0.0j
        midpoint = 0.5 * (lo + hi)
        half_phase = 0.5 * width * b_value
        sinc = 1.0 if half_phase == 0.0 else math.sin(half_phase) / half_phase
        return cmath.exp(1j * midpoint * b_value) * sinc

    return axis_average(cell.kx_interval, b_transverse[0]) * axis_average(
        cell.ky_interval, b_transverse[1]
    )


def default_mode_completeness_records() -> Tuple[SoftModeCompletenessRecord, ...]:
    specs = (
        ("C33.RES.1", 4, 6, 5, 3841),
        ("C33.RES.2", 8, 12, 10, 30721),
        ("C33.RES.3", 12, 18, 15, 103681),
    )
    return tuple(
        SoftModeCompletenessRecord(
            record_id="C34.COMPLETENESS." + resolution_id.split(".")[-1],
            resolution_id=resolution_id,
            n_omega=n_omega,
            n_rapidity=n_rapidity,
            n_transverse=n_transverse,
            polarizations=2,
            adjoint_colors=8,
            vacuum_dimension=1,
            one_gluon_dimension=dimension - 1,
            total_dimension=dimension,
            both_rapidity_regions=True,
            exact_zero_mode_separate=True,
            normalization_checked=False,
            completeness_status=ContributionStatus.UNRESOLVED_BLOCKING,
        )
        for resolution_id, n_omega, n_rapidity, n_transverse, dimension in specs
    )


def default_eikonal_vertices() -> Tuple[
    Tuple[EikonalEmissionVertex, ...], Tuple[EikonalAbsorptionVertex, ...]
]:
    operator = default_four_line_operator()
    rapidity = C33SoftRapidityRegulator(
        C33_RAPIDITY_REGULATOR_ID,
        "MODIFIED_DELTA",
        1.0e-3,
        2.0e-3,
        -1,
        1,
        ("COMBINE_REAL_VIRTUAL", "UV_RENORMALIZE", "REMOVE_DELTA"),
    )
    directions = {
        "n": C33EikonalDirection(
            "C33.N", "n", (1, 0, 0, 1), "k_minus", "delta_minus"
        ),
        "nbar": C33EikonalDirection(
            "C33.NBAR", "nbar", (1, 0, 0, -1), "k_plus", "delta_plus"
        ),
    }
    emissions = []
    absorptions = []
    for index, path in enumerate(operator.paths):
        denominator = rapidity.derive_denominator(
            directions[path.source.direction],
            path.source.orientation,
            path.source.conjugate,
            1,
        )
        vertex_id = "C34.EMISSION.%s" % path.path_id
        emission = EikonalEmissionVertex(
            vertex_id=vertex_id,
            line_id=path.path_id,
            perturbative_order="O(g_s)",
            coupling_symbol=C34_EIKONAL_VERTEX_COUPLING,
            representation_action=path.source.representation,
            orientation=path.source.orientation,
            path_ordering=path.path_ordering,
            direction=path.source.direction,
            transverse_position=path.source.transverse_position,
            momentum_flow=1,
            delta_component=denominator.delta_component,
            delta_sign=denominator.delta_sign,
            i0_sign=denominator.i0_sign,
            phase="exp(+i k_T.x_%sT)" % (index + 1),
            phase_scope="TRANSVERSE_BASEPOINT_ONLY_COMPLETE_SEGMENT_UNPROVED",
            symbolic_expression=(
                "g_s*T_%d^a*sigma_%d*v_%d^mu*exp(+i k_T.x_%dT)*"
                "D_%d(k;delta,i0)" % (index + 1, index + 1, index + 1, index + 1, index + 1)
            ),
            sign_derivation=denominator.derivation,
            numerical_current_proofs=RequiredProofSet(
                EIKONAL_NUMERICAL_CURRENT_REQUIREMENTS,
                EIKONAL_NUMERICAL_CURRENT_PROVED,
            ),
            status=ContributionStatus.UNRESOLVED_BLOCKING,
        )
        emissions.append(emission)
        absorptions.append(
            EikonalAbsorptionVertex(
                vertex_id="C34.ABSORPTION.%s" % path.path_id,
                emission_vertex_id=vertex_id,
                line_id=path.path_id,
                perturbative_order="O(g_s)",
                symbolic_expression="HERMITIAN_CONJUGATE[%s]" % emission.symbolic_expression,
                exact_hermitian_conjugate=True,
                conjugates_phase_i0_and_color=True,
                emission_numerical_vertex_proved=False,
                numerical_absorption_vertex_proved=False,
                status=ContributionStatus.UNRESOLVED_BLOCKING,
            )
        )
    return tuple(emissions), tuple(absorptions)


def fail_closed_one_loop_ledger() -> Tuple[SoftContributionResult, ...]:
    return tuple(
        SoftContributionResult(
            contribution_id="C34.SOFT.%02d" % (index + 1),
            contribution_class=name,
            status=ContributionStatus.UNRESOLVED_BLOCKING,
            expression=NONZERO_UNKNOWN,
            blocking=True,
            finite_regulator_evaluated=False,
            continuum_scaleless_assumed=False,
        )
        for index, name in enumerate(REQUIRED_ONE_LOOP_CONTRIBUTIONS)
    )


def architecture_examples() -> Dict[str, _ContentAddressed]:
    """Build one deterministic Branch-G object for every required C34 type."""

    unresolved = ContributionStatus.UNRESOLVED_BLOCKING
    emissions, absorptions = default_eikonal_vertices()
    records = default_mode_completeness_records()
    sequence = SoftResolutionSequence(
        sequence_id="C34.RESOLUTION.SEQUENCE",
        resolution_ids=tuple(item.resolution_id for item in records),
        resolution_tuples=((4, 6, 5), (8, 12, 10), (12, 18, 15)),
        dimensions=(3841, 30721, 103681),
        c33_descriptor_nesting_declared=True,
        nominal_support_extension_monotone=True,
        refinement_proofs=RequiredProofSet(
            RESOLUTION_REFINEMENT_REQUIREMENTS,
            RESOLUTION_REFINEMENT_PROVED,
        ),
        all_executed=False,
    )
    order = SoftOneLoopOrder(
        order_id="C34.ORDER.ONE_LOOP",
        coupling_order="O(g_s^2)",
        perturbative_order="O(a_s)",
        coupling_normalization=C34_COUPLING_NORMALIZATION,
        target_coefficient_convention=C34_TARGET_SOFT_EXPANSION,
        target_convention_proved=True,
        finite_basis_interaction_normalization_proved=False,
        first_omitted_order="O(a_s^2)",
    )
    cell = SoftModeCellId(
        "C34.CELL.SCHEMA.EXAMPLE.NONPHYSICAL",
        "C33.RES.1",
        "n",
        (0.01, 0.02),
        (-3.0, -2.0),
        (-0.5, 0.0),
        (0.0, 0.5),
        False,
        False,
        "VALIDATION_ONLY_NONPHYSICAL_CELL",
        False,
        "C34_RUNTIME_SCHEMA_ORACLE_NOT_A_C33_MODE_CELL",
    )
    quadrature = SoftModeQuadrature(
        quadrature_id="C34.SOFT.CELL.QUADRATURE.v1",
        method="REGULAR_CELL_GAUSS_LEGENDRE_PLAN_SINGULAR_RULE_UNPROVED",
        orders_per_axis=(16, 16, 16, 16),
        singular_cell_treatment="ANALYTIC_SINGULAR_SUBTRACTION_REQUIRED_UNPROVED",
        cell_integration_required=True,
        cell_integration_executed=False,
        regular_cell_rule_frozen=True,
        singular_formula_proved=False,
        mode_measure_proved=False,
        tolerances_frozen=False,
        cell_center_only=False,
        physical_numerical_epsilon=False,
        frozen_before_results=True,
        integrated_physical_cell_count=0,
        physical_coefficient_eligible=False,
        status=unresolved,
    )
    plan = SoftOneLoopPlan(
        C34_PLAN_ID,
        "S0-FB-EIKONAL-FOCK",
        "C33.FOUR_LINE.SOFT.OPERATOR",
        order.order_id,
        (0.0, 1.0, 2.0),
        C33_RAPIDITY_REGULATOR_ID,
        "PROJECT_MSBAR_SOFT_CONVENTION",
        sequence.resolution_ids,
        "EXCLUDE_PRIMARY_RETAIN_SEPARATE_CONTROL/AUDIT_REQUIRED",
        (0.125, 0.25, 0.5, 1.0),
        (0.004, 0.002, 0.001, 0.0005),
        (0.006, 0.003, 0.0015, 0.00075),
        quadrature.quadrature_id,
        True,
        True,
    )
    current = EikonalCurrent(
        current_id="C34.EIKONAL.CURRENT.FOUR_LINE",
        line_ids=FOUR_LINE_IDS,
        emission_vertex_ids=tuple(item.vertex_id for item in emissions),
        perturbative_order="O(g_s)",
        symbolic_expression=(
            "g_s*SUM_ell=1..4[T_ell^a*sigma_ell_UNRESOLVED*"
            "v_ell^mu_UNNORMALIZED*exp(+i k_T.x_ellT)*D_ell(k;delta,i0)]"
        ),
        coupling_normalization=C34_EIKONAL_VERTEX_COUPLING,
        color_action="REPRESENTATION_CLASSES_STORED_GENERATOR_ACTION_UNRESOLVED",
        transverse_phase="STORED_BASEPOINT_PHASE_COMPLETE_SEGMENT_PHASE_UNRESOLVED",
        transverse_phase_scope="TRANSVERSE_BASEPOINT_ONLY_COMPLETE_SEGMENT_UNPROVED",
        cell_integration_contract_present=True,
        cell_matrix_elements_executed=False,
        singular_denominator_integrated=False,
        four_line_skeleton_proved=True,
        numerical_current_proofs=RequiredProofSet(
            EIKONAL_NUMERICAL_CURRENT_REQUIREMENTS,
            EIKONAL_NUMERICAL_CURRENT_PROVED,
        ),
        current_status=unresolved,
        ward_contraction_status=unresolved,
    )
    pair = EikonalPairKernel(
        "C34.PAIR.N_NBAR",
        ("SN_DAGGER_B", "SNBAR_B"),
        "N_NBAR_EXCHANGE",
        "C_F=4/3",
        "exp(+i k_T.b_T)-1",
        NONZERO_UNKNOWN,
        unresolved,
    )
    self_kernel = EikonalSelfKernel(
        "C34.SELF.SN_DAGGER_B",
        "SN_DAGGER_B",
        True,
        True,
        NONZERO_UNKNOWN,
        unresolved,
    )
    closure_kernel = TransverseClosureKernel(
        "C34.TRANSVERSE.CLOSURE",
        "C33.TRANSVERSE.CLOSURE",
        True,
        True,
        NONZERO_UNKNOWN,
        unresolved,
    )
    virtual = SoftVirtualAmplitude(
        "C34.VIRTUAL.AMPLITUDE",
        "SECOND_ORDER_WILSON_EXPANSION",
        tuple(item.vertex_id for item in emissions),
        "UNCUT_VACUUM_CONTRACTION",
        NONZERO_UNKNOWN,
        unresolved,
    )
    real = SoftRealAmplitude(
        "C34.REAL.AMPLITUDE",
        "C34.CUT.ONE_SOFT_GLUON",
        (cell.cell_id,),
        "ONE_GLUON_CUT_CELL_INTEGRATED",
        "exp(+i k_T.b_T)",
        NONZERO_UNKNOWN,
        unresolved,
    )
    cut = SoftCutLedger(
        "C34.CUT.LEDGER",
        ("C34.CUT.ONE_SOFT_GLUON",),
        (real.amplitude_id,),
        (virtual.amplitude_id,),
        None,
        False,
        unresolved,
    )
    assembly = SoftRealVirtualAssembly(
        "C34.REAL.VIRTUAL.ASSEMBLY",
        "C34.ROUTE.WILSON_EXPANSION",
        "C34.ROUTE.MODE_SUM_CUT",
        False,
        False,
        False,
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        unresolved,
    )
    gauge = SoftGaugeContribution(
        "C34.GAUGE", (0.0, 1.0, 2.0), NONZERO_UNKNOWN, None, unresolved
    )
    ghost = SoftGhostContribution("C34.GHOST", True, NONZERO_UNKNOWN, unresolved)
    instantaneous = SoftInstantaneousContribution(
        "C34.INSTANTANEOUS", "LIGHT_FRONT_CONSTRAINT_FIELD", NONZERO_UNKNOWN, unresolved
    )
    zero = SoftZeroModeContribution(
        "C34.ZERO.MODE",
        "EXCLUDE_PRIMARY_RETAIN_SEPARATE_CONTROL",
        True,
        NONZERO_UNKNOWN,
        unresolved,
    )
    boundary = SoftBoundaryContribution(
        "C34.BOUNDARY",
        "FINITE_CELL/PERIODIC/TRANSVERSE_CLOSED/COVARIANT",
        True,
        True,
        True,
        NONZERO_UNKNOWN,
        unresolved,
    )
    ledger = fail_closed_one_loop_ledger()
    decomposition = SoftBareCoefficientDecomposition(
        decomposition_id="C34.BARE.DECOMPOSITION",
        coefficient_id="C34.BARE.COEFFICIENT",
        contributions=ledger,
        direct_bare_component_ids=DIRECT_BARE_COMPONENT_IDS,
        separate_control_ids=SEPARATE_CONTROL_COMPONENT_IDS,
        alternative_route_ids=ALTERNATIVE_ROUTE_COMPONENT_IDS,
        counterterm_decision_ids=COUNTERTERM_DECISION_COMPONENT_IDS,
        derived_counterterm_ids=DERIVED_COUNTERTERM_IDS,
        every_required_class_present=True,
        all_direct_bare_resolved=False,
        all_separate_control_decisions_resolved=False,
        all_counterterm_decisions_resolved=False,
        all_resolved=False,
    )
    bare = SoftBareCoefficient(
        coefficient_id="C34.BARE.COEFFICIENT",
        operator_id="C33.FOUR_LINE.SOFT.OPERATOR",
        tree_value=Fraction(1, 1),
        perturbative_order="O(a_s)",
        coupling_normalization=C34_COUPLING_NORMALIZATION,
        target_coefficient_convention=C34_TARGET_SOFT_EXPANSION,
        color_factor_placement="EXTERNAL_TO_REDUCED_S^[1]",
        finite_basis_interaction_normalization_proved=False,
        first_omitted_order="O(a_s^2)",
        component_ids=DIRECT_BARE_COMPONENT_IDS,
        separate_control_ids=SEPARATE_CONTROL_COMPONENT_IDS,
        alternative_route_ids=ALTERNATIVE_ROUTE_COMPONENT_IDS,
        counterterm_decision_ids=COUNTERTERM_DECISION_COMPONENT_IDS,
        derived_counterterm_ids=DERIVED_COUNTERTERM_IDS,
        expression=NONZERO_UNKNOWN,
        status=unresolved,
        all_direct_bare_components_resolved=False,
        separate_control_assembly_decisions_resolved=False,
        retains_delta_plus_minus=True,
        retains_gauge_and_basis_identity=True,
    )
    uv_structure = SoftUVStructure(
        "C34.UV.STRUCTURE",
        NONZERO_UNKNOWN,
        NONZERO_UNKNOWN,
        NONZERO_UNKNOWN,
        NONZERO_UNKNOWN,
        NONZERO_UNKNOWN,
        True,
        False,
        unresolved,
    )
    rapidity_structure = SoftRapidityStructure(
        "C34.RAPIDITY.STRUCTURE",
        NONZERO_UNKNOWN,
        NONZERO_UNKNOWN,
        NONZERO_UNKNOWN,
        ("ASSEMBLE_REAL_VIRTUAL", "UV_RENORMALIZE", "RAPIDITY_RENORMALIZE", "REMOVE_DELTA"),
        False,
        unresolved,
    )
    uv_solution = SoftUVCountertermSolution(
        "C34.UV.SOLUTION",
        ("LINE_SELF", "CUSP_ENDPOINT", "TRANSVERSE_CLOSURE", "RESIDUAL_LINE_MASS", "VACUUM", "SOFT_OPERATOR"),
        True,
        False,
        True,
        False,
        False,
        NONZERO_UNKNOWN,
        None,
        "O(a_s^2)",
        unresolved,
    )
    rapidity_solution = SoftRapidityCountertermSolution(
        "C34.RAPIDITY.SOLUTION",
        C33_RAPIDITY_REGULATOR_ID,
        "d/d ln sqrt(delta_plus*delta_minus)",
        True,
        False,
        False,
        NONZERO_UNKNOWN,
        None,
        None,
        unresolved,
    )
    renormalized = SoftRenormalizedCoefficient(
        "C34.RENORMALIZED.COEFFICIENT",
        bare.coefficient_id,
        uv_solution.solution_id,
        rapidity_solution.solution_id,
        NONZERO_UNKNOWN,
        None,
        None,
        None,
        unresolved,
    )
    derivative = SoftRapidityDerivative(
        "C34.RAPIDITY.DERIVATIVE",
        renormalized.coefficient_id,
        "d/d ln sqrt(delta_plus*delta_minus)",
        "SOFT_RAPIDITY_ANOMALOUS_DIMENSION_SOURCE_CONVENTION",
        NONZERO_UNKNOWN,
        unresolved,
    )
    cusp = SoftCuspConsistency(
        "C34.CUSP.CONSISTENCY",
        derivative.derivative_id,
        "dD/dln(mu)=Gamma_cusp",
        NONZERO_UNKNOWN,
        None,
        unresolved,
    )
    cs = SoftCSKernelRecord(
        "C34.CS.KERNEL",
        "PROJECT_SOFT_TO_TMD_D_CONVENTION_EXPLICIT",
        "D_TMD=DECLARED_SIGN_AND_FACTOR_TIMES_GAMMA_RAP_SOFT",
        False,
        NONZERO_UNKNOWN,
        unresolved,
    )
    continuum = SoftContinuumTargetRecord(
        target_id="C34.CONTINUUM.TARGET",
        scheme="CONTINUUM_MODIFIED_DELTA_MSBAR",
        source_id=C34_CONTINUUM_SOURCE_ID,
        source_file_sha256=C34_CONTINUUM_SOURCE_FILE_SHA256,
        source_locator=C34_CONTINUUM_SOURCE_LOCATOR,
        source_route="SOURCE_EXPRESSION_TRANSCRIPTION",
        reconstruction_route="DIRECT_SYMBOLIC_INTEGRAL_RECONSTRUCTION_REQUIRED",
        source_expression=C34_CONTINUUM_NLO_SOURCE_EXPRESSION,
        source_expression_hash=C34_CONTINUUM_NLO_SOURCE_EXPRESSION_SHA256,
        source_laurent_expression=C34_CONTINUUM_NLO_LAURENT_EXPRESSION,
        source_laurent_expression_hash=C34_CONTINUUM_NLO_LAURENT_EXPRESSION_SHA256,
        reconstruction_expression_hash=None,
        coupling_normalization=C34_COUPLING_NORMALIZATION,
        coefficient_convention=C34_TARGET_SOFT_EXPANSION,
        color_factor_placement="EXTERNAL_TO_REDUCED_S^[1]",
        oracle_proofs=RequiredProofSet(
            CONTINUUM_ORACLE_REQUIREMENTS,
            CONTINUUM_ORACLE_PROVED,
        ),
        convention_aligned=False,
        finite_basis_result=False,
        expression=NONZERO_UNKNOWN,
        status=unresolved,
    )
    difference = SoftFiniteRegulatorDifference(
        "C34.FB.CONT.DIFFERENCE",
        continuum.target_id,
        renormalized.coefficient_id,
        NONZERO_UNKNOWN,
        NONZERO_UNKNOWN,
        NONZERO_UNKNOWN,
        NONZERO_UNKNOWN,
        NONZERO_UNKNOWN,
        NONZERO_UNKNOWN,
        unresolved,
    )
    conversion = SoftFiniteRegulatorKernel(
        kernel_id="C34.FB.TO.CONT.KERNEL",
        difference_id=difference.difference_id,
        state_independence_required=True,
        state_independence_proved=False,
        hadron_independence_required=True,
        hadron_independence_proved=False,
        flavor_independence_required_where_applicable=True,
        flavor_independence_proved=False,
        art25_member_independence_required=True,
        art25_member_independence_proved=True,
        gauge_independence_required=True,
        gauge_independence_proved=False,
        resolution_dependence_required=True,
        resolution_dependence_explicit=False,
        first_omitted_order="O(a_s^2)",
        expression=NONZERO_UNKNOWN,
        status=unresolved,
    )
    roundtrip = SoftRoundTripReport(
        "C34.ROUNDTRIP",
        conversion.kernel_id,
        False,
        None,
        None,
        None,
        unresolved,
    )
    trajectory_plan = SoftTrajectoryFitPlan(
        "C34.TRAJECTORY.PLAN",
        ("UV_LOG", "RAPIDITY_WINDOW_LOG", "FINITE_CONSTANT", "SOURCE_PREDICTED_POWER"),
        2,
        ("C33.RES.1", "C33.RES.2"),
        ("C33.RES.3",),
        True,
        True,
    )
    holdout = SoftTrajectoryHoldout(
        "C34.HOLDOUT.RESOLUTION.R3",
        "SOFT_RESOLUTION",
        "C33.RES.3",
        True,
        False,
        None,
    )
    trajectory = SoftTrajectoryResult(
        "C34.TRAJECTORY.RESULT",
        sequence.sequence_id,
        trajectory_plan.plan_id,
        (holdout.holdout_id,),
        False,
        SoftTrajectoryStatus.UNAVAILABLE,
        "The regulator-specific one-loop values at R1-R3 have not been calculated.",
    )
    zero_bin = SoftSideZeroBinLimit(
        "C34.SOFT.SIDE.ZERO.BIN",
        "C33.MEAS.B",
        "b_TMD_PROJECT_CONVENTION",
        "MODIFIED_DELTA_DISTINCT_DELTA_PLUS_MINUS",
        "PROJECT_MSBAR_SOFT_CONVENTION",
        "COVARIANT_XI_G",
        ("p2_offshell",),
        ("ASSEMBLE", "UV_RENORMALIZE", "RAPIDITY_RENORMALIZE", "REMOVE_REGULATORS"),
        NONZERO_UNKNOWN,
        SoftCollinearStatus.UNRESOLVED,
    )
    continuation = SoftCollinearContinuationContract(
        "C34.C32.CONTINUATION.CONTRACT",
        zero_bin.limit_id,
        "C32.PARTONIC.PLAN",
        True,
        True,
        True,
        True,
        False,
        False,
        SoftCollinearStatus.UNRESOLVED,
    )
    capability = C34SoftCapabilityMatrix(
        "C34.CAPABILITY", 18, 3, 15, "BRANCH_G_FAIL_CLOSED"
    )
    closure = C34ClosureReport(
        report_id="C34.CLOSURE",
        c33_tree_boundary_closed=True,
        plan_frozen=True,
        symbolic_eikonal_current_skeleton_typed=True,
        complete_eikonal_current_closed=False,
        singular_cell_integration_closed=False,
        all_one_loop_contributions_resolved=False,
        real_virtual_count_once_closed=False,
        uv_closed=False,
        rapidity_closed=False,
        gauge_closed=False,
        continuum_oracle_closed=False,
        regulator_conversion_closed=False,
        trajectory_closed=False,
        soft_zero_bin_ready=False,
        continuation_ready=False,
        no_go_status=C34_NO_GO,
        exact_missing_calculation=(
            "The one-gluon numerator signs, light-front tangent and field "
            "normalizations, exact cell refinement maps, all 18 finite-regulator "
            "one-loop contributions, and independent continuum reconstruction "
            "remain unproved."
        ),
        exact_next_package=C34_NEXT_PACKAGE,
    )
    objects = (
        plan,
        order,
        cell,
        quadrature,
        records[0],
        current,
        emissions[0],
        absorptions[0],
        pair,
        self_kernel,
        closure_kernel,
        virtual,
        real,
        cut,
        assembly,
        gauge,
        ghost,
        instantaneous,
        zero,
        boundary,
        bare,
        decomposition,
        uv_structure,
        rapidity_structure,
        uv_solution,
        rapidity_solution,
        renormalized,
        derivative,
        cusp,
        cs,
        continuum,
        difference,
        conversion,
        roundtrip,
        sequence,
        trajectory_plan,
        holdout,
        trajectory,
        zero_bin,
        continuation,
        capability,
        closure,
    )
    return {type(item).__name__: item for item in objects}


ARCHITECTURE_TYPES: Tuple[Type[_ContentAddressed], ...] = (
    SoftOneLoopPlan,
    SoftOneLoopOrder,
    SoftModeCellId,
    SoftModeQuadrature,
    SoftModeCompletenessRecord,
    EikonalCurrent,
    EikonalEmissionVertex,
    EikonalAbsorptionVertex,
    EikonalPairKernel,
    EikonalSelfKernel,
    TransverseClosureKernel,
    SoftVirtualAmplitude,
    SoftRealAmplitude,
    SoftCutLedger,
    SoftRealVirtualAssembly,
    SoftGaugeContribution,
    SoftGhostContribution,
    SoftInstantaneousContribution,
    SoftZeroModeContribution,
    SoftBoundaryContribution,
    SoftBareCoefficient,
    SoftBareCoefficientDecomposition,
    SoftUVStructure,
    SoftRapidityStructure,
    SoftUVCountertermSolution,
    SoftRapidityCountertermSolution,
    SoftRenormalizedCoefficient,
    SoftRapidityDerivative,
    SoftCuspConsistency,
    SoftCSKernelRecord,
    SoftContinuumTargetRecord,
    SoftFiniteRegulatorDifference,
    SoftFiniteRegulatorKernel,
    SoftRoundTripReport,
    SoftResolutionSequence,
    SoftTrajectoryFitPlan,
    SoftTrajectoryHoldout,
    SoftTrajectoryResult,
    SoftSideZeroBinLimit,
    SoftCollinearContinuationContract,
    C34SoftCapabilityMatrix,
    C34ClosureReport,
)


INJECTION_GROUPS = (
    "BASELINE_ROOT",
    "EIKONAL_CURRENT",
    "MODE_BASIS",
    "ONE_LOOP_DIAGRAMS",
    "COUNT_ONCE",
    "UV_RENORMALIZATION",
    "RAPIDITY_RENORMALIZATION",
    "CONTINUUM_CONVERSION",
    "ZERO_MODE_ENDPOINTS",
    "SOFT_COLLINEAR_INTERFACE",
    "SCOPE_LEAKAGE",
    "INTEGRITY",
)

INJECTION_DIAGNOSTICS = {
    "BASELINE_ROOT": "C34_BASELINE_OR_ROOT_IDENTITY_FAILURE",
    "EIKONAL_CURRENT": "C34_EIKONAL_CURRENT_IDENTITY_FAILURE",
    "MODE_BASIS": "C34_MODE_BASIS_OR_QUADRATURE_FAILURE",
    "ONE_LOOP_DIAGRAMS": "C34_ONE_LOOP_LEDGER_INCOMPLETE",
    "COUNT_ONCE": "C34_REAL_VIRTUAL_COUNT_ONCE_FAILURE",
    "UV_RENORMALIZATION": "C34_UV_RENORMALIZATION_FAILURE",
    "RAPIDITY_RENORMALIZATION": "C34_RAPIDITY_RENORMALIZATION_FAILURE",
    "CONTINUUM_CONVERSION": "C34_FINITE_REGULATOR_CONVERSION_FAILURE",
    "ZERO_MODE_ENDPOINTS": "C34_ZERO_MODE_ENDPOINT_CLOSURE_FAILURE",
    "SOFT_COLLINEAR_INTERFACE": "C34_SOFT_COLLINEAR_INTERFACE_FAILURE",
    "SCOPE_LEAKAGE": "C34_FORBIDDEN_SCOPE_PROMOTION",
    "INTEGRITY": "C34_BASELINE_INTEGRITY_FAILURE",
}

INJECTION_FAULTS = {
    "BASELINE_ROOT": (
        "INVENTED_C33_COMMIT",
        "C33_BASELINE_NOT_REPRODUCED",
        "B0_SOFT_INSERTED_IN_PROTON_NORMALIZATION",
        "C33_PATH_RECORD_MODIFIED",
        "C33_TREE_IDENTITY_OVERWRITTEN",
    ),
    "EIKONAL_CURRENT": (
        "LINE_OMITTED",
        "CONJUGATE_ACTION_WRONG",
        "PATH_ORDER_LOST",
        "TRANSVERSE_POSITION_LOST",
        "WRONG_DELTA_REGULATOR_ASSIGNED",
        "I0_SIGN_INSERTED_MANUALLY",
        "COLOR_ACTION_TRANSPOSED_INCORRECTLY",
        "SINGULAR_CELL_SAMPLED_AT_CENTER",
    ),
    "MODE_BASIS": (
        "ONE_GLUON_NORMALIZATION_WRONG",
        "RAPIDITY_REGIONS_ALIASED",
        "POLARIZATION_DROPPED",
        "ADJOINT_COLOR_DROPPED",
        "ZERO_MODE_SILENTLY_INCLUDED",
        "ZERO_MODE_SILENTLY_DISCARDED",
        "COMPLETENESS_INFERRED_FROM_ONE_RESOLUTION",
    ),
    "ONE_LOOP_DIAGRAMS": (
        "REAL_GRAPH_OMITTED",
        "VIRTUAL_GRAPH_OMITTED",
        "SAME_DIRECTION_DECLARED_SCALELESS_BY_ANALOGY",
        "SELF_ENERGY_OMITTED",
        "CUSP_OMITTED",
        "ENDPOINT_OMITTED",
        "TRANSVERSE_CLOSURE_OMITTED",
        "GHOST_GAUGE_TERM_OMITTED",
        "INSTANTANEOUS_TERM_OMITTED",
        "VACUUM_ENERGY_OMITTED",
        "BASIS_BOUNDARY_TERM_OMITTED",
    ),
    "COUNT_ONCE": (
        "REAL_CONTRIBUTION_DUPLICATED",
        "VIRTUAL_CONTRIBUTION_DUPLICATED",
        "CONJUGATE_PAIR_DOUBLE_COUNTED",
        "CUT_SUPPORT_DUPLICATED",
        "SOFT_FACTOR_SQUARED_ACCIDENTALLY",
        "INVERSE_SQUARE_ROOT_APPLIED_TWICE",
    ),
    "UV_RENORMALIZATION": (
        "POWER_DIVERGENCE_HIDDEN_IN_LOG",
        "LINEAR_DIVERGENCE_DROPPED",
        "LINE_MASS_COUNTERTERM_OMITTED",
        "CUSP_COUNTERTERM_DUPLICATED",
        "UV_FACTOR_TUNED_TO_CONTINUUM_FINITE_CONSTANT",
        "UV_HOLDOUT_USED_IN_DETERMINATION",
    ),
    "RAPIDITY_RENORMALIZATION": (
        "DELTA_PLUS_MINUS_ALIASED",
        "REGULATOR_REMOVED_BEFORE_ASSEMBLY",
        "RAPIDITY_LOG_ABSORBED_IN_UV_FACTOR",
        "ZETA_CONFUSED_WITH_BARE_REGULATOR",
        "CS_MODEL_IMPORTED_FROM_ART25",
        "GAUGE_DEPENDENCE_HIDDEN_IN_RAPIDITY_COUNTERTERM",
    ),
    "CONTINUUM_CONVERSION": (
        "CONTINUUM_RESULT_COPIED_AS_FINITE_RESULT",
        "FINITE_CONSTANT_FITTED_TO_ART25",
        "INVERSE_MAP_ABSENT",
        "ROUNDTRIP_FAILURE_HIDDEN",
        "ONE_RESOLUTION_CALLED_CONTINUUM",
        "ARBITRARY_POLYNOMIAL_TRAJECTORY",
        "FIRST_OMITTED_ORDER_SET_ZERO",
    ),
    "ZERO_MODE_ENDPOINTS": (
        "ZERO_MODE_CONTROL_IGNORED",
        "ENDPOINT_MERGED_WITH_CUSP_WITHOUT_IDENTITY",
        "TRANSVERSE_JUNCTION_OMITTED",
        "ZERO_MODE_SENSITIVITY_CALLED_NUMERICAL_NOISE",
    ),
    "SOFT_COLLINEAR_INTERFACE": (
        "ZERO_BIN_EQUALITY_CLAIMED_FROM_CITATION",
        "OFFSHELL_IR_ISSUE_IGNORED",
        "DIFFERENT_MEASUREMENTS_ACCEPTED",
        "DIFFERENT_B_CONVENTIONS_ACCEPTED",
        "COLLINEAR_ONE_LOOP_COEFFICIENT_FABRICATED",
        "SOFT_SECTOR_CALLED_COMPLETE_TMD",
    ),
    "SCOPE_LEAKAGE": (
        "MICROSCOPIC_PROTON_TMD_EXPORTED",
        "TWELVE_POINT_BRIDGE_RERUN",
        "RESIDUAL_CALLED_LIKELIHOOD",
        "P_VALUE_REPORTED",
        "CALIBRATION_PERFORMED",
        "MEMBER_REWEIGHTED",
        "EMULATOR_TRAINED",
        "PROCESS_DEUTERON_GLUON_TODD_STATUS_PROMOTED",
    ),
    "INTEGRITY": (
        "ART25_MEMBER_USED",
        "ART25_DATA_OR_CHI2_USED",
        "RAW_MSHT_FILES_COMMITTED",
        "PRODUCTION_REGISTRY_CHANGED",
        "AUTHORITATIVE_ARTIFACT_CHANGED",
        "NONDETERMINISTIC_MANIFEST",
    ),
}


# Each fault below changes a concrete semantic control rather than toggling a
# generic ``detected`` flag.  The baseline intentionally represents the
# contract that the corresponding negative test protects; it is not a claim
# that the unresolved C34 physics calculation has closed.
INJECTION_CONTROL_BASELINE: Dict[str, Dict[str, Any]] = {
    "BASELINE_ROOT": {
        "starting_commit": C34_STARTING_COMMIT,
        "baseline_reproduced": True,
        "b0_soft_in_proton_normalization": False,
        "c33_path_records_immutable": True,
        "tree_soft_factor": "1_EXACT",
    },
    "EIKONAL_CURRENT": {
        "ordered_line_count": 4,
        "conjugate_action": "ANTI_FUNDAMENTAL",
        "path_ordering_retained": True,
        "transverse_positions_retained": True,
        "delta_assignment": "DIRECTION_DERIVED",
        "i0_assignment": "DERIVATION_PIPELINE",
        "color_action": "REPRESENTATION_DERIVED",
        "singular_cell_method": "CELL_INTEGRATION_REQUIRED",
    },
    "MODE_BASIS": {
        "one_gluon_norm": "POSITIVE_TYPED_NORMALIZATION",
        "rapidity_regions": ("n", "nbar"),
        "polarization_count": 2,
        "adjoint_color_count": 8,
        "zero_mode_in_primary": False,
        "zero_mode_control_retained": True,
        "resolution_evidence_count": 3,
    },
    "ONE_LOOP_DIAGRAMS": {
        "real_graph_present": True,
        "virtual_graph_present": True,
        "same_direction_finite_regulator_decision": "EXPLICIT_REQUIRED",
        "self_energy_present": True,
        "cusp_present": True,
        "endpoint_present": True,
        "transverse_closure_present": True,
        "ghost_gauge_decision_present": True,
        "instantaneous_decision_present": True,
        "vacuum_energy_decision_present": True,
        "basis_boundary_decision_present": True,
    },
    "COUNT_ONCE": {
        "real_multiplicity": 1,
        "virtual_multiplicity": 1,
        "conjugate_pair_multiplicity": 1,
        "cut_support_multiplicity": 1,
        "soft_factor_power": 1,
        "inverse_sqrt_multiplicity": 1,
    },
    "UV_RENORMALIZATION": {
        "power_log_separate": True,
        "linear_divergence_visible": True,
        "line_mass_counterterm_slot_present": True,
        "cusp_counterterm_multiplicity": 1,
        "continuum_finite_constant_used_for_tuning": False,
        "holdout_used_in_determination": False,
    },
    "RAPIDITY_RENORMALIZATION": {
        "delta_components_distinct": True,
        "removal_order": "AFTER_ASSEMBLY_AND_RENORMALIZATION",
        "rapidity_log_absorbed_into_uv": False,
        "zeta_is_bare_regulator": False,
        "art25_cs_model_used": False,
        "gauge_dependence_hidden": False,
    },
    "CONTINUUM_CONVERSION": {
        "continuum_substituted_for_finite": False,
        "finite_constant_fit_to_art25": False,
        "inverse_map_required": True,
        "roundtrip_failure_hidden": False,
        "resolutions_used_for_continuum_claim": 3,
        "trajectory_family": "SOURCE_PREDICTED_ONLY",
        "first_omitted_order": "O(a_s^2)",
    },
    "ZERO_MODE_ENDPOINTS": {
        "zero_mode_control_retained": True,
        "endpoint_identity_separate": True,
        "transverse_junction_present": True,
        "zero_mode_sensitivity_class": "PHYSICS_CONTROL",
    },
    "SOFT_COLLINEAR_INTERFACE": {
        "citation_only_equivalence": False,
        "offshell_ir_issue_explicit": True,
        "different_measurements_accepted": False,
        "different_b_conventions_accepted": False,
        "collinear_coefficients_fabricated": False,
        "soft_called_complete_tmd": False,
    },
    "SCOPE_LEAKAGE": {
        "microscopic_proton_exported": False,
        "twelve_point_bridge_rerun": False,
        "residual_called_likelihood": False,
        "p_value_reported": False,
        "calibration_performed": False,
        "member_reweighted": False,
        "emulator_trained": False,
        "physics_status_promoted": False,
    },
    "INTEGRITY": {
        "art25_member_used": False,
        "art25_data_or_chi2_used": False,
        "raw_msht_committed": False,
        "production_registry_count": 216,
        "authoritative_artifacts_unchanged": True,
        "manifest_deterministic": True,
    },
}


INJECTION_MUTATION_SPECS: Dict[str, Tuple[Tuple[str, str, Any], ...]] = {
    "BASELINE_ROOT": (
        ("INVENTED_C33_COMMIT", "starting_commit", "0" * 40),
        ("C33_BASELINE_NOT_REPRODUCED", "baseline_reproduced", False),
        ("B0_SOFT_INSERTED_IN_PROTON_NORMALIZATION", "b0_soft_in_proton_normalization", True),
        ("C33_PATH_RECORD_MODIFIED", "c33_path_records_immutable", False),
        ("C33_TREE_IDENTITY_OVERWRITTEN", "tree_soft_factor", "0_INEXACT"),
    ),
    "EIKONAL_CURRENT": (
        ("LINE_OMITTED", "ordered_line_count", 3),
        ("CONJUGATE_ACTION_WRONG", "conjugate_action", "FUNDAMENTAL"),
        ("PATH_ORDER_LOST", "path_ordering_retained", False),
        ("TRANSVERSE_POSITION_LOST", "transverse_positions_retained", False),
        ("WRONG_DELTA_REGULATOR_ASSIGNED", "delta_assignment", "ALIASED_DELTA"),
        ("I0_SIGN_INSERTED_MANUALLY", "i0_assignment", "MANUAL_SIGN"),
        ("COLOR_ACTION_TRANSPOSED_INCORRECTLY", "color_action", "WRONG_TRANSPOSE"),
        ("SINGULAR_CELL_SAMPLED_AT_CENTER", "singular_cell_method", "CENTER_SAMPLE"),
    ),
    "MODE_BASIS": (
        ("ONE_GLUON_NORMALIZATION_WRONG", "one_gluon_norm", "NEGATIVE_OR_UNNORMALIZED"),
        ("RAPIDITY_REGIONS_ALIASED", "rapidity_regions", ("n", "n")),
        ("POLARIZATION_DROPPED", "polarization_count", 1),
        ("ADJOINT_COLOR_DROPPED", "adjoint_color_count", 7),
        ("ZERO_MODE_SILENTLY_INCLUDED", "zero_mode_in_primary", True),
        ("ZERO_MODE_SILENTLY_DISCARDED", "zero_mode_control_retained", False),
        ("COMPLETENESS_INFERRED_FROM_ONE_RESOLUTION", "resolution_evidence_count", 1),
    ),
    "ONE_LOOP_DIAGRAMS": (
        ("REAL_GRAPH_OMITTED", "real_graph_present", False),
        ("VIRTUAL_GRAPH_OMITTED", "virtual_graph_present", False),
        ("SAME_DIRECTION_DECLARED_SCALELESS_BY_ANALOGY", "same_direction_finite_regulator_decision", "TARGET_SCALELESS_ASSUMED"),
        ("SELF_ENERGY_OMITTED", "self_energy_present", False),
        ("CUSP_OMITTED", "cusp_present", False),
        ("ENDPOINT_OMITTED", "endpoint_present", False),
        ("TRANSVERSE_CLOSURE_OMITTED", "transverse_closure_present", False),
        ("GHOST_GAUGE_TERM_OMITTED", "ghost_gauge_decision_present", False),
        ("INSTANTANEOUS_TERM_OMITTED", "instantaneous_decision_present", False),
        ("VACUUM_ENERGY_OMITTED", "vacuum_energy_decision_present", False),
        ("BASIS_BOUNDARY_TERM_OMITTED", "basis_boundary_decision_present", False),
    ),
    "COUNT_ONCE": (
        ("REAL_CONTRIBUTION_DUPLICATED", "real_multiplicity", 2),
        ("VIRTUAL_CONTRIBUTION_DUPLICATED", "virtual_multiplicity", 2),
        ("CONJUGATE_PAIR_DOUBLE_COUNTED", "conjugate_pair_multiplicity", 2),
        ("CUT_SUPPORT_DUPLICATED", "cut_support_multiplicity", 2),
        ("SOFT_FACTOR_SQUARED_ACCIDENTALLY", "soft_factor_power", 2),
        ("INVERSE_SQUARE_ROOT_APPLIED_TWICE", "inverse_sqrt_multiplicity", 2),
    ),
    "UV_RENORMALIZATION": (
        ("POWER_DIVERGENCE_HIDDEN_IN_LOG", "power_log_separate", False),
        ("LINEAR_DIVERGENCE_DROPPED", "linear_divergence_visible", False),
        ("LINE_MASS_COUNTERTERM_OMITTED", "line_mass_counterterm_slot_present", False),
        ("CUSP_COUNTERTERM_DUPLICATED", "cusp_counterterm_multiplicity", 2),
        ("UV_FACTOR_TUNED_TO_CONTINUUM_FINITE_CONSTANT", "continuum_finite_constant_used_for_tuning", True),
        ("UV_HOLDOUT_USED_IN_DETERMINATION", "holdout_used_in_determination", True),
    ),
    "RAPIDITY_RENORMALIZATION": (
        ("DELTA_PLUS_MINUS_ALIASED", "delta_components_distinct", False),
        ("REGULATOR_REMOVED_BEFORE_ASSEMBLY", "removal_order", "BEFORE_ASSEMBLY"),
        ("RAPIDITY_LOG_ABSORBED_IN_UV_FACTOR", "rapidity_log_absorbed_into_uv", True),
        ("ZETA_CONFUSED_WITH_BARE_REGULATOR", "zeta_is_bare_regulator", True),
        ("CS_MODEL_IMPORTED_FROM_ART25", "art25_cs_model_used", True),
        ("GAUGE_DEPENDENCE_HIDDEN_IN_RAPIDITY_COUNTERTERM", "gauge_dependence_hidden", True),
    ),
    "CONTINUUM_CONVERSION": (
        ("CONTINUUM_RESULT_COPIED_AS_FINITE_RESULT", "continuum_substituted_for_finite", True),
        ("FINITE_CONSTANT_FITTED_TO_ART25", "finite_constant_fit_to_art25", True),
        ("INVERSE_MAP_ABSENT", "inverse_map_required", False),
        ("ROUNDTRIP_FAILURE_HIDDEN", "roundtrip_failure_hidden", True),
        ("ONE_RESOLUTION_CALLED_CONTINUUM", "resolutions_used_for_continuum_claim", 1),
        ("ARBITRARY_POLYNOMIAL_TRAJECTORY", "trajectory_family", "ARBITRARY_POLYNOMIAL"),
        ("FIRST_OMITTED_ORDER_SET_ZERO", "first_omitted_order", "0"),
    ),
    "ZERO_MODE_ENDPOINTS": (
        ("ZERO_MODE_CONTROL_IGNORED", "zero_mode_control_retained", False),
        ("ENDPOINT_MERGED_WITH_CUSP_WITHOUT_IDENTITY", "endpoint_identity_separate", False),
        ("TRANSVERSE_JUNCTION_OMITTED", "transverse_junction_present", False),
        ("ZERO_MODE_SENSITIVITY_CALLED_NUMERICAL_NOISE", "zero_mode_sensitivity_class", "NUMERICAL_NOISE"),
    ),
    "SOFT_COLLINEAR_INTERFACE": (
        ("ZERO_BIN_EQUALITY_CLAIMED_FROM_CITATION", "citation_only_equivalence", True),
        ("OFFSHELL_IR_ISSUE_IGNORED", "offshell_ir_issue_explicit", False),
        ("DIFFERENT_MEASUREMENTS_ACCEPTED", "different_measurements_accepted", True),
        ("DIFFERENT_B_CONVENTIONS_ACCEPTED", "different_b_conventions_accepted", True),
        ("COLLINEAR_ONE_LOOP_COEFFICIENT_FABRICATED", "collinear_coefficients_fabricated", True),
        ("SOFT_SECTOR_CALLED_COMPLETE_TMD", "soft_called_complete_tmd", True),
    ),
    "SCOPE_LEAKAGE": (
        ("MICROSCOPIC_PROTON_TMD_EXPORTED", "microscopic_proton_exported", True),
        ("TWELVE_POINT_BRIDGE_RERUN", "twelve_point_bridge_rerun", True),
        ("RESIDUAL_CALLED_LIKELIHOOD", "residual_called_likelihood", True),
        ("P_VALUE_REPORTED", "p_value_reported", True),
        ("CALIBRATION_PERFORMED", "calibration_performed", True),
        ("MEMBER_REWEIGHTED", "member_reweighted", True),
        ("EMULATOR_TRAINED", "emulator_trained", True),
        ("PROCESS_DEUTERON_GLUON_TODD_STATUS_PROMOTED", "physics_status_promoted", True),
    ),
    "INTEGRITY": (
        ("ART25_MEMBER_USED", "art25_member_used", True),
        ("ART25_DATA_OR_CHI2_USED", "art25_data_or_chi2_used", True),
        ("RAW_MSHT_FILES_COMMITTED", "raw_msht_committed", True),
        ("PRODUCTION_REGISTRY_CHANGED", "production_registry_count", 217),
        ("AUTHORITATIVE_ARTIFACT_CHANGED", "authoritative_artifacts_unchanged", False),
        ("NONDETERMINISTIC_MANIFEST", "manifest_deterministic", False),
    ),
}

FAULT_CATALOG = tuple(
    (group, fault) for group in INJECTION_GROUPS for fault in INJECTION_FAULTS[group]
)


def _injection_payload(index: int, group: str, fault: str) -> Dict[str, Any]:
    specs = {name: (field, replacement) for name, field, replacement in INJECTION_MUTATION_SPECS[group]}
    field, replacement = specs[fault]
    before = INJECTION_CONTROL_BASELINE[group][field]
    return {
        "payload_version": "C34.INJECTION.MUTATION.v1",
        "instance_index": index,
        "operation": "REPLACE",
        "path": ["domains", group, field],
        "expected_before": _canonical(before),
        "replacement": _canonical(replacement),
        "fault": fault,
    }


def _validate_injection_control_state(state: Dict[str, Any]) -> str:
    violations = []
    for group in INJECTION_GROUPS:
        expected = INJECTION_CONTROL_BASELINE[group]
        actual = state["domains"][group]
        for field, expected_value in expected.items():
            if actual[field] != expected_value:
                violations.append((group, field))
    if len(violations) != 1:
        raise ValueError("C34_INJECTION_MUST_CREATE_EXACTLY_ONE_SEMANTIC_VIOLATION")
    return INJECTION_DIAGNOSTICS[violations[0][0]]


def execute_injection_payload(
    payload: Dict[str, Any], expected_payload_sha256: Optional[str] = None
) -> str:
    """Apply one semantic mutation and obtain its validator diagnostic.

    The diagnostic is selected only after comparing the mutated control state
    with the complete safe baseline.  Neither the payload's fault label nor an
    injection identifier determines the returned diagnostic.
    """

    if expected_payload_sha256 is not None and content_hash(payload) != expected_payload_sha256:
        raise ValueError("C34_INJECTION_PAYLOAD_HASH_MISMATCH")
    if payload.get("payload_version") != "C34.INJECTION.MUTATION.v1":
        raise ValueError("C34_INJECTION_PAYLOAD_VERSION_MISMATCH")
    if payload.get("operation") != "REPLACE":
        raise ValueError("C34_INJECTION_OPERATION_UNSUPPORTED")
    path = payload.get("path")
    if not isinstance(path, list) or len(path) != 3 or path[0] != "domains":
        raise ValueError("C34_INJECTION_MUTATION_PATH_INVALID")
    _, group, field = path
    if group not in INJECTION_CONTROL_BASELINE or field not in INJECTION_CONTROL_BASELINE[group]:
        raise ValueError("C34_INJECTION_MUTATION_TARGET_UNKNOWN")

    state = {
        "domains": {
            name: dict(values) for name, values in INJECTION_CONTROL_BASELINE.items()
        }
    }
    if _canonical(state["domains"][group][field]) != payload.get("expected_before"):
        raise ValueError("C34_INJECTION_MUTATION_PRECONDITION_FAILED")
    replacement = payload.get("replacement")
    # Canonical tuples serialize as lists; restore the one tuple-valued control
    # so validation compares like with like.
    if isinstance(state["domains"][group][field], tuple) and isinstance(replacement, list):
        replacement = tuple(replacement)
    if replacement == state["domains"][group][field]:
        raise ValueError("C34_INJECTION_MUTATION_IS_NO_OP")
    state["domains"][group][field] = replacement
    return _validate_injection_control_state(state)


def injection_rows(count: int = 2240) -> Tuple[Dict[str, Any], ...]:
    if count < 2240:
        raise ValueError("C34_MINIMUM_2240_ORDERED_INJECTIONS_REQUIRED")
    rows = []
    for index in range(count):
        group, fault = FAULT_CATALOG[index % len(FAULT_CATALOG)]
        payload = _injection_payload(index + 1, group, fault)
        payload_sha256 = content_hash(payload)
        observed_diagnostic = execute_injection_payload(
            payload, expected_payload_sha256=payload_sha256
        )
        expected_diagnostic = INJECTION_DIAGNOSTICS[group]
        rows.append(
            {
                "injection_id": "C34.INJECT.%s.%04d" % (group, index + 1),
                "ordered_index": index + 1,
                "group": group,
                "fault": fault,
                "mutation_payload": payload,
                "mutation_payload_sha256": payload_sha256,
                "mutation_executed": True,
                "expected_diagnostic": expected_diagnostic,
                "observed_diagnostic": observed_diagnostic,
                "detected": observed_diagnostic == expected_diagnostic,
            }
        )
    return tuple(rows)


def detect_injection(identifier: str, count: int = 2240) -> str:
    parts = identifier.split(".")
    if (
        len(parts) != 4
        or parts[:2] != ["C34", "INJECT"]
        or parts[2] not in INJECTION_GROUPS
    ):
        raise ValueError("UNKNOWN_C34_INJECTION")
    try:
        index = int(parts[3])
    except ValueError as exc:
        raise ValueError("UNKNOWN_C34_INJECTION") from exc
    if count < 2240 or not 1 <= index <= count:
        raise ValueError("UNKNOWN_C34_INJECTION")
    group, _ = FAULT_CATALOG[(index - 1) % len(FAULT_CATALOG)]
    if group != parts[2]:
        raise ValueError("UNKNOWN_C34_INJECTION")
    _, fault = FAULT_CATALOG[(index - 1) % len(FAULT_CATALOG)]
    payload = _injection_payload(index, group, fault)
    return execute_injection_payload(
        payload, expected_payload_sha256=content_hash(payload)
    )


if len(ARCHITECTURE_TYPES) != 42:
    raise RuntimeError("C34_ARCHITECTURE_TYPE_COUNT_MISMATCH")
if len(REQUIRED_ONE_LOOP_CONTRIBUTIONS) != 18:
    raise RuntimeError("C34_REQUIRED_CONTRIBUTION_COUNT_MISMATCH")
if len(FAULT_CATALOG) != 80:
    raise RuntimeError("C34_FAULT_CATALOG_COUNT_MISMATCH")
if tuple(INJECTION_MUTATION_SPECS) != INJECTION_GROUPS:
    raise RuntimeError("C34_INJECTION_MUTATION_GROUP_ORDER_MISMATCH")
for _group in INJECTION_GROUPS:
    if tuple(item[0] for item in INJECTION_MUTATION_SPECS[_group]) != INJECTION_FAULTS[_group]:
        raise RuntimeError("C34_INJECTION_MUTATION_FAULT_ORDER_MISMATCH:%s" % _group)
    if len({item[1] for item in INJECTION_MUTATION_SPECS[_group]}) != len(
        INJECTION_MUTATION_SPECS[_group]
    ):
        raise RuntimeError("C34_INJECTION_MUTATION_TARGET_DUPLICATED:%s" % _group)
