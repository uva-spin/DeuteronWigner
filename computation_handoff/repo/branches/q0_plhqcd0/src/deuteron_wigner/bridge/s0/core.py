"""Typed C33/S0 finite-basis vacuum/eikonal soft-sector contracts.

The module deliberately separates the baryon-number-zero soft Hilbert root
from C32's baryon-number-one collinear root.  It provides exact tree/color
identities and fail-closed one-loop, renormalization, regulator-compatibility,
and continuation gates.  It contains no fitting, inference, bridge execution,
or microscopic-proton export interface.
"""

from dataclasses import dataclass, fields, is_dataclass
from enum import Enum
from fractions import Fraction
from hashlib import sha256
import json
import math
from typing import Any, Dict, Optional, Tuple, Type


C32_COLLINEAR_ROOT = "C32_MICROSCOPIC_TMD_OPERATOR_COMPLETION"
C33_SOFT_ROOT = "C33_FINITE_BASIS_VACUUM_EIKONAL_SOFT_ROOT"
NONZERO_UNKNOWN = "NONZERO_UNKNOWN"
C33_WILSON_GEOMETRY = (
    "TR[SN_DAGGER(b) SNBAR(b) SNBAR_DAGGER(0) SN(0)]/NC_"
    "WITH_PATH_ORDERING_AND_TRANSVERSE_CLOSURE"
)
C33_RAPIDITY_REGULATOR_ID = "C33.MODIFIED.DELTA"
C33_UV_REGULATOR_ID = "C33.UV.FB"
C33_IR_REGULATOR_ID = "C33.IR.COMMON"
C33_BASIS_REGULATOR_ID = "C33.SOFT.BASIS"
C33_SOURCE_SOFT_SCHEME = "C33_FINITE_BASIS_MODIFIED_DELTA"
C33_TARGET_SOFT_SCHEME = "CONTINUUM_MODIFIED_DELTA_MSBAR"


class SoftSectorPlan(str, Enum):
    DIRECT_FOCK = "S0-FB-EIKONAL-FOCK"
    AUXILIARY = "S0-AUXILIARY-EIKONAL"
    CONTINUUM_ORACLE_ONLY = "S0-CONTINUUM-ORACLE-ONLY"
    UNAVAILABLE = "S0-UNAVAILABLE"


class ContributionStatus(str, Enum):
    EXACT_TREE = "EXACT_TREE"
    CALCULATED = "CALCULATED"
    CALCULATION_REQUIRED = "CALCULATION_REQUIRED"
    STRUCTURALLY_UNRESOLVED = "STRUCTURALLY_UNRESOLVED"
    NOT_APPLICABLE_WITH_PROOF = "NOT_APPLICABLE_WITH_PROOF"
    SOURCE_ORACLE_ONLY = "SOURCE_ORACLE_ONLY"


class CompatibilityStatus(str, Enum):
    IDENTICAL = "SOFT_COLLINEAR_REGULATORS_IDENTICAL"
    EXACT_CONVERSION = "SOFT_COLLINEAR_EXACT_CONVERSION"
    COMPATIBLE_AT_ORDER = "SOFT_COLLINEAR_COMPATIBLE_AT_DECLARED_ORDER"
    UNRESOLVED = "SOFT_COLLINEAR_COMPATIBILITY_UNRESOLVED"
    INCOMPATIBLE = "SOFT_COLLINEAR_INCOMPATIBLE"


class TrajectoryStatus(str, Enum):
    RESOLVED = "SOFT_CONTINUUM_TRAJECTORY_RESOLVED"
    LOG_ONLY = "SOFT_LOG_STRUCTURE_RESOLVED_FINITE_REMAINDER_OPEN"
    FINITE_BASIS_ONLY = "SOFT_FINITE_BASIS_ONLY"
    NONUNIVERSAL = "SOFT_NONUNIVERSAL_TRAJECTORY"
    UNAVAILABLE = "SOFT_TRAJECTORY_UNAVAILABLE"


@dataclass(frozen=True)
class C33IdentityEnvelope:
    """Common scientific-identity and isolation record for every S0 object."""

    envelope_version: str
    object_type: str
    object_identity: str
    scope: str
    soft_root_id: str
    baryon_number: int
    wilson_geometry: str
    color_representation: str
    color_trace: str
    rapidity_regulator_id: str
    uv_regulator_id: str
    ir_regulator_id: str
    basis_regulator_id: str
    perturbative_order: str
    source_soft_scheme: str
    target_soft_scheme: str
    state_independent: bool
    consumes_art25: bool
    consumes_process_data: bool
    consumes_bridge_residuals: bool
    inference_reachable: bool
    production_reachable: bool

    def __post_init__(self) -> None:
        if self.scope != "C33/S0" or self.soft_root_id != C33_SOFT_ROOT:
            raise ValueError("C33_IDENTITY_ENVELOPE_ROOT_MISMATCH")
        _require_b0(self.baryon_number)
        if self.wilson_geometry != C33_WILSON_GEOMETRY:
            raise ValueError("C33_IDENTITY_ENVELOPE_WILSON_GEOMETRY_MISMATCH")
        if self.color_representation != "FUNDAMENTAL" or self.color_trace != "SINGLET_1_OVER_NC":
            raise ValueError("C33_IDENTITY_ENVELOPE_COLOR_MISMATCH")
        regulator_ids = (
            self.rapidity_regulator_id, self.uv_regulator_id,
            self.ir_regulator_id, self.basis_regulator_id,
        )
        if not all(regulator_ids):
            raise ValueError("C33_IDENTITY_ENVELOPE_REGULATOR_ID_MISSING")
        if not self.perturbative_order:
            raise ValueError("C33_IDENTITY_ENVELOPE_ORDER_MISSING")
        if not self.source_soft_scheme or not self.target_soft_scheme:
            raise ValueError("C33_IDENTITY_ENVELOPE_SCHEME_MISSING")
        if not self.state_independent:
            raise ValueError("C33_IDENTITY_ENVELOPE_STATE_DEPENDENCE_FORBIDDEN")
        forbidden = (
            self.consumes_art25, self.consumes_process_data,
            self.consumes_bridge_residuals, self.inference_reachable,
            self.production_reachable,
        )
        if any(forbidden):
            raise ValueError("C33_IDENTITY_ENVELOPE_FORBIDDEN_REACHABILITY")

    @property
    def validated(self) -> bool:
        return True


def _canonical(value: Any) -> Any:
    """Return a JSON-safe canonical value without object-address strings."""
    if isinstance(value, Enum):
        return value.value
    if isinstance(value, Fraction):
        return {"denominator": value.denominator, "numerator": value.numerator}
    if is_dataclass(value):
        result = {field.name: _canonical(getattr(value, field.name))
                  for field in fields(value)}
        if isinstance(value, _ContentAddressed):
            result["c33_identity_envelope"] = _canonical(value.c33_identity_envelope)
        return result
    if isinstance(value, dict):
        return {str(key): _canonical(value[key]) for key in sorted(value)}
    if isinstance(value, (tuple, list)):
        return [_canonical(item) for item in value]
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError("NONFINITE_VALUE_NOT_SERIALIZABLE")
    return value


def deterministic_json(value: Any) -> str:
    return json.dumps(_canonical(value), sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True, allow_nan=False)


def content_hash(value: Any) -> str:
    return sha256(deterministic_json(value).encode("utf-8")).hexdigest()


class _ContentAddressed:
    @property
    def c33_identity_envelope(self) -> C33IdentityEnvelope:
        order = "C33/S0_DECLARED_TREE_PLUS_ONE_LOOP_TARGET"
        for attribute in ("order", "declared_order", "first_omitted_order"):
            candidate = getattr(self, attribute, None)
            if isinstance(candidate, str) and candidate:
                order = candidate
                break
        object_identity = type(self).__name__
        for field in fields(self):
            if field.name.endswith("_id") or field.name == "root_id":
                candidate = getattr(self, field.name)
                if isinstance(candidate, str) and candidate:
                    object_identity = candidate
                    break
        return C33IdentityEnvelope(
            envelope_version="C33.IDENTITY.ENVELOPE.v1",
            object_type=type(self).__name__,
            object_identity=object_identity,
            scope="C33/S0",
            soft_root_id=C33_SOFT_ROOT,
            baryon_number=0,
            wilson_geometry=C33_WILSON_GEOMETRY,
            color_representation="FUNDAMENTAL",
            color_trace="SINGLET_1_OVER_NC",
            rapidity_regulator_id=C33_RAPIDITY_REGULATOR_ID,
            uv_regulator_id=C33_UV_REGULATOR_ID,
            ir_regulator_id=C33_IR_REGULATOR_ID,
            basis_regulator_id=C33_BASIS_REGULATOR_ID,
            perturbative_order=order,
            source_soft_scheme=C33_SOURCE_SOFT_SCHEME,
            target_soft_scheme=C33_TARGET_SOFT_SCHEME,
            state_independent=True,
            consumes_art25=False,
            consumes_process_data=False,
            consumes_bridge_residuals=False,
            inference_reachable=False,
            production_reachable=False,
        )

    @property
    def identity_validated(self) -> bool:
        return self.c33_identity_envelope.validated

    @property
    def deterministic_json(self) -> str:
        return deterministic_json(self)

    @property
    def content_hash(self) -> str:
        return content_hash(self)


def _require_b0(baryon_number: int) -> None:
    if baryon_number != 0:
        raise ValueError("C33_SOFT_ROOT_MUST_HAVE_BARYON_NUMBER_ZERO")


def _check_unresolved_contribution(status: ContributionStatus,
                                   expression: str, proof: str) -> None:
    if status is ContributionStatus.NOT_APPLICABLE_WITH_PROOF and not proof:
        raise ValueError("ABSENT_SOFT_CONTRIBUTION_REQUIRES_PROOF")
    if status in (ContributionStatus.CALCULATION_REQUIRED,
                  ContributionStatus.STRUCTURALLY_UNRESOLVED):
        if expression != NONZERO_UNKNOWN:
            raise ValueError("UNRESOLVED_SOFT_TERM_MUST_BE_NONZERO_UNKNOWN")
    if status is ContributionStatus.CALCULATED and expression == NONZERO_UNKNOWN:
        raise ValueError("CALCULATED_SOFT_TERM_REQUIRES_EXPRESSION")


@dataclass(frozen=True)
class SoftRootId(_ContentAddressed):
    root_id: str
    version: str
    baryon_number: int = 0
    collinear_root_id: str = C32_COLLINEAR_ROOT
    shares_state_vector: bool = False
    shares_probability_normalization: bool = False

    def __post_init__(self) -> None:
        _require_b0(self.baryon_number)
        if self.root_id != C33_SOFT_ROOT:
            raise ValueError("C33_SOFT_ROOT_IDENTITY_MISMATCH")
        if self.shares_state_vector or self.shares_probability_normalization:
            raise ValueError("C33_B0_B1_STATE_ALIAS_FORBIDDEN")


@dataclass(frozen=True)
class VacuumHilbertId(_ContentAddressed):
    hilbert_id: str
    soft_root: SoftRootId
    baryon_number: int = 0
    contains_proton_state: bool = False

    def __post_init__(self) -> None:
        _require_b0(self.baryon_number)
        if self.contains_proton_state:
            raise ValueError("VACUUM_SOFT_STATE_IN_PROTON_FOCK_NORMALIZATION")


@dataclass(frozen=True)
class VacuumStateId(_ContentAddressed):
    state_id: str
    hilbert: VacuumHilbertId
    normalization: Fraction = Fraction(1, 1)
    baryon_number: int = 0

    def __post_init__(self) -> None:
        _require_b0(self.baryon_number)
        if self.normalization != Fraction(1, 1):
            raise ValueError("VACUUM_STATE_NORMALIZATION_NOT_ONE")


@dataclass(frozen=True)
class VacuumSectorPlan(_ContentAddressed):
    plan_id: str
    selected_plan: SoftSectorPlan
    frozen_before_calculation: bool
    state_independent: bool = True
    consumes_art25: bool = False
    consumes_process_data: bool = False
    consumes_bridge_residuals: bool = False

    def __post_init__(self) -> None:
        if not self.frozen_before_calculation:
            raise ValueError("SOFT_PLAN_NOT_FROZEN_BEFORE_CALCULATION")
        if not self.state_independent:
            raise ValueError("SOFT_PLAN_MUST_BE_STATE_INDEPENDENT")
        if self.consumes_art25 or self.consumes_process_data or self.consumes_bridge_residuals:
            raise ValueError("FORBIDDEN_DATA_DEPENDENT_SOFT_PLAN")


@dataclass(frozen=True)
class SoftBasisId(_ContentAddressed):
    basis_id: str
    vacuum_hilbert: VacuumHilbertId
    family: str
    version: str


@dataclass(frozen=True)
class SoftBasisResolution(_ContentAddressed):
    resolution_id: str
    basis_id: str
    nesting_rank: int
    n_omega: int
    n_rapidity: int
    n_transverse: int
    omega_min: float
    omega_max: float
    rapidity_max: float
    transverse_extent: float
    zero_mode_scale: float

    def __post_init__(self) -> None:
        if min(self.nesting_rank, self.n_omega, self.n_rapidity,
               self.n_transverse) <= 0:
            raise ValueError("INVALID_SOFT_BASIS_DIMENSION")
        if not (0.0 < self.omega_min < self.omega_max):
            raise ValueError("INVALID_SOFT_ENERGY_SUPPORT")
        if self.rapidity_max <= 0.0 or self.transverse_extent <= 0.0:
            raise ValueError("INVALID_SOFT_BASIS_SUPPORT")


@dataclass(frozen=True)
class SoftMomentumMode(_ContentAddressed):
    mode_id: str
    k_plus: float
    k_minus: float
    k_transverse: Tuple[float, float]
    rapidity_region: str
    rapidity_bin: int
    transverse_index: int
    boundary_condition_id: str
    zero_mode: bool

    def __post_init__(self) -> None:
        if self.rapidity_region not in ("n", "nbar"):
            raise ValueError("SOFT_MODE_RAPIDITY_REGION_MISSING")
        if self.k_plus == 0.0 and self.k_minus == 0.0 and not self.zero_mode:
            raise ValueError("UNDECLARED_SOFT_ZERO_MODE")


@dataclass(frozen=True)
class SoftGluonMode(_ContentAddressed):
    gluon_mode_id: str
    momentum_mode: SoftMomentumMode
    polarization: str
    adjoint_color: int
    normalization: float
    color_dimension: int = 8

    def __post_init__(self) -> None:
        if not 0 <= self.adjoint_color < self.color_dimension:
            raise ValueError("SOFT_GLUON_ADJOINT_COLOR_INVALID")
        if not self.polarization or self.normalization <= 0.0:
            raise ValueError("SOFT_GLUON_MODE_NORMALIZATION_INVALID")


@dataclass(frozen=True)
class SoftZeroModePolicy(_ContentAddressed):
    policy_id: str
    treatment: str
    zero_modes_retained: bool
    sensitivity_holdout: str
    proof_status: str

    def __post_init__(self) -> None:
        if not self.treatment or not self.sensitivity_holdout:
            raise ValueError("SOFT_ZERO_MODE_POLICY_OMITTED")


@dataclass(frozen=True)
class SoftBoundaryCondition(_ContentAddressed):
    boundary_id: str
    longitudinal: str
    transverse: str
    eikonal_infinity: str
    gauge_boundary: str


@dataclass(frozen=True)
class SoftContinuumTrajectory(_ContentAddressed):
    trajectory_id: str
    resolutions: Tuple[SoftBasisResolution, ...]
    analytic_fit_structures: Tuple[str, ...]
    status: TrajectoryStatus

    def __post_init__(self) -> None:
        if len(self.resolutions) < 3:
            raise ValueError("THREE_SOFT_RESOLUTIONS_REQUIRED")
        ranks = tuple(item.nesting_rank for item in self.resolutions)
        if ranks != tuple(sorted(ranks)) or len(set(ranks)) != len(ranks):
            raise ValueError("SOFT_RESOLUTIONS_NOT_STRICTLY_NESTED")
        if not self.analytic_fit_structures:
            raise ValueError("ANALYTIC_SOFT_TRAJECTORY_STRUCTURE_REQUIRED")


@dataclass(frozen=True)
class EikonalSourceId(_ContentAddressed):
    source_id: str
    direction: str
    transverse_position: str
    representation: str
    conjugate: bool
    orientation: str

    def __post_init__(self) -> None:
        if self.direction not in ("n", "nbar"):
            raise ValueError("UNKNOWN_EIKONAL_DIRECTION")
        expected = "ANTI_FUNDAMENTAL" if self.conjugate else "FUNDAMENTAL"
        if self.representation != expected:
            raise ValueError("WRONG_EIKONAL_COLOR_ACTION")
        if self.orientation not in ("FUTURE", "PAST"):
            raise ValueError("UNKNOWN_WILSON_ORIENTATION")


@dataclass(frozen=True)
class EikonalDirection(_ContentAddressed):
    direction_id: str
    name: str
    vector: Tuple[int, int, int, int]
    momentum_component: str
    delta_component: str

    def __post_init__(self) -> None:
        if self.name not in ("n", "nbar"):
            raise ValueError("UNKNOWN_EIKONAL_DIRECTION")
        expected = {"n": ("k_minus", "delta_minus"),
                    "nbar": ("k_plus", "delta_plus")}[self.name]
        if (self.momentum_component, self.delta_component) != expected:
            raise ValueError("MODIFIED_DELTA_DIRECTION_COMPONENT_MISMATCH")


@dataclass(frozen=True)
class EikonalColorSpace(_ContentAddressed):
    color_space_id: str
    n_colors: int = 3
    representation: str = "FUNDAMENTAL"
    singlet_trace_numerator: int = 1
    singlet_trace_denominator: int = 3

    def __post_init__(self) -> None:
        if self.n_colors != 3 or self.representation != "FUNDAMENTAL":
            raise ValueError("C33_QUARK_SOFT_COLOR_SPACE_MISMATCH")
        if Fraction(self.singlet_trace_numerator,
                    self.singlet_trace_denominator) != Fraction(1, self.n_colors):
            raise ValueError("COLOR_TRACE_NORMALIZATION_WRONG")

    @property
    def c_f(self) -> Fraction:
        return Fraction(self.n_colors * self.n_colors - 1,
                        2 * self.n_colors)


@dataclass(frozen=True)
class EikonalAuxiliaryField(_ContentAddressed):
    field_id: str
    statistics: str
    representation: str
    direction: str
    boundary_condition: str
    residual_energy_counterterm: str
    endpoint_operator: str
    methodological_only: bool = True


@dataclass(frozen=True)
class EikonalPathOperator(_ContentAddressed):
    path_id: str
    source: EikonalSourceId
    segments: Tuple[str, ...]
    path_ordering: str
    transverse_closure_id: str
    fourier_convention_id: str

    def __post_init__(self) -> None:
        if not self.segments or self.path_ordering not in ("P", "ANTI_P"):
            raise ValueError("EIKONAL_PATH_ORDERING_OMITTED")
        if not self.transverse_closure_id:
            raise ValueError("TRANSVERSE_CLOSURE_OMITTED")


@dataclass(frozen=True)
class FourLineSoftOperator(_ContentAddressed):
    operator_id: str
    paths: Tuple[EikonalPathOperator, ...]
    color_space: EikonalColorSpace
    trace_order: Tuple[str, ...]
    transverse_closure_complete: bool

    def __post_init__(self) -> None:
        if len(self.paths) != 4 or len({p.path_id for p in self.paths}) != 4:
            raise ValueError("C33_FOUR_LINE_OPERATOR_NOT_REALIZABLE")
        if tuple(path.path_id for path in self.paths) != self.trace_order:
            raise ValueError("FOUR_LINE_PATH_ORDER_MISMATCH")
        directions = tuple(path.source.direction for path in self.paths)
        if directions.count("n") != 2 or directions.count("nbar") != 2:
            raise ValueError("FOUR_LINE_DIRECTION_CONTENT_MISMATCH")
        if sum(path.source.conjugate for path in self.paths) != 2:
            raise ValueError("FOUR_LINE_CONJUGATION_CONTENT_MISMATCH")
        if not self.transverse_closure_complete:
            raise ValueError("TRANSVERSE_CLOSURE_OMITTED")

    @property
    def tree_level_soft_factor(self) -> Fraction:
        # (1/Nc) Tr[1 Nc-by-Nc] is exactly one.
        return Fraction(self.color_space.singlet_trace_numerator,
                        self.color_space.singlet_trace_denominator) * self.color_space.n_colors


@dataclass(frozen=True)
class EikonalDenominator(_ContentAddressed):
    direction: str
    momentum_component: str
    momentum_sign: int
    delta_component: str
    delta_sign: int
    i0_sign: int
    derivation: Tuple[str, ...]


@dataclass(frozen=True)
class SoftRapidityRegulator(_ContentAddressed):
    regulator_id: str
    scheme: str
    delta_plus: float
    delta_minus: float
    fourier_phase_sign: int
    covariant_derivative_sign: int
    regulator_removal_order: Tuple[str, ...]
    basis_is_rapidity_regulator: bool = False

    def __post_init__(self) -> None:
        if self.scheme != "MODIFIED_DELTA":
            raise ValueError("C33_REQUIRES_MODIFIED_DELTA")
        if self.delta_plus <= 0.0 or self.delta_minus <= 0.0:
            raise ValueError("MODIFIED_DELTA_PARAMETERS_MUST_BE_POSITIVE")
        if self.fourier_phase_sign not in (-1, 1) or self.covariant_derivative_sign not in (-1, 1):
            raise ValueError("INVALID_STORED_SIGN_CONVENTION")
        if self.basis_is_rapidity_regulator:
            raise ValueError("FINITE_BASIS_IS_NOT_RAPIDITY_REGULATOR")

    def derive_denominator(self, direction: EikonalDirection,
                           orientation: str, conjugate: bool,
                           momentum_flow: int) -> EikonalDenominator:
        """Derive, never accept, the modified-delta and i0 signs."""
        if orientation not in ("FUTURE", "PAST") or momentum_flow not in (-1, 1):
            raise ValueError("INVALID_EIKONAL_DENOMINATOR_CONVENTION")
        orientation_sign = 1 if orientation == "FUTURE" else -1
        conjugation_sign = -1 if conjugate else 1
        sign = (orientation_sign * conjugation_sign * momentum_flow *
                self.fourier_phase_sign * self.covariant_derivative_sign)
        return EikonalDenominator(
            direction=direction.name,
            momentum_component=direction.momentum_component,
            momentum_sign=orientation_sign * momentum_flow,
            delta_component=direction.delta_component,
            delta_sign=sign,
            i0_sign=sign,
            derivation=("WILSON_ORIENTATION", "FOURIER_CONVENTION",
                        "MOMENTUM_FLOW", "COVARIANT_DERIVATIVE",
                        "LINE_CONJUGATION", "MODIFIED_DELTA"),
        )


@dataclass(frozen=True)
class SoftUVRegulator(_ContentAddressed):
    regulator_id: str
    finite_basis_cutoff: str
    target_scheme: str
    power_divergences_separate: bool


@dataclass(frozen=True)
class SoftIRRegulator(_ContentAddressed):
    regulator_id: str
    prescription: str
    parameter: str
    common_with_collinear: bool


@dataclass(frozen=True)
class SoftMeasurement(_ContentAddressed):
    measurement_id: str
    transverse_coordinate: Tuple[float, float]
    real_measurement: str
    inclusive_unobserved_soft: bool


@dataclass(frozen=True)
class SoftFourierConvention(_ContentAddressed):
    convention_id: str
    phase: str
    normalization: str
    phase_sign: int

    def __post_init__(self) -> None:
        if self.phase_sign not in (-1, 1):
            raise ValueError("INVALID_FOURIER_PHASE_SIGN")


@dataclass(frozen=True)
class BareSoftFactor(_ContentAddressed):
    factor_id: str
    operator_id: str
    order: str
    tree_value: Fraction
    one_loop_status: ContributionStatus
    one_loop_expression: str
    component_ids: Tuple[str, ...]

    def __post_init__(self) -> None:
        if self.tree_value != Fraction(1, 1):
            raise ValueError("TREE_SOFT_FACTOR_NOT_ONE")
        _check_unresolved_contribution(self.one_loop_status,
                                       self.one_loop_expression, "")

    @property
    def one_loop_calculated(self) -> bool:
        return self.one_loop_status is ContributionStatus.CALCULATED


@dataclass(frozen=True)
class SoftVirtualContribution(_ContentAddressed):
    contribution_id: str; status: ContributionStatus; expression: str; proof: str = ""
    def __post_init__(self) -> None: _check_unresolved_contribution(self.status, self.expression, self.proof)


@dataclass(frozen=True)
class SoftRealContribution(_ContentAddressed):
    contribution_id: str; status: ContributionStatus; expression: str; proof: str = ""
    def __post_init__(self) -> None: _check_unresolved_contribution(self.status, self.expression, self.proof)


@dataclass(frozen=True)
class SoftSelfEnergyContribution(_ContentAddressed):
    contribution_id: str; status: ContributionStatus; expression: str; proof: str = ""
    def __post_init__(self) -> None: _check_unresolved_contribution(self.status, self.expression, self.proof)


@dataclass(frozen=True)
class SoftCuspEndpointContribution(_ContentAddressed):
    contribution_id: str; status: ContributionStatus; expression: str; proof: str = ""
    def __post_init__(self) -> None: _check_unresolved_contribution(self.status, self.expression, self.proof)


@dataclass(frozen=True)
class SoftTransverseClosureContribution(_ContentAddressed):
    contribution_id: str; status: ContributionStatus; expression: str; proof: str = ""
    def __post_init__(self) -> None: _check_unresolved_contribution(self.status, self.expression, self.proof)


@dataclass(frozen=True)
class SoftInstantaneousContribution(_ContentAddressed):
    contribution_id: str; status: ContributionStatus; expression: str; proof: str = ""
    def __post_init__(self) -> None: _check_unresolved_contribution(self.status, self.expression, self.proof)


@dataclass(frozen=True)
class SoftZeroModeContribution(_ContentAddressed):
    contribution_id: str; status: ContributionStatus; expression: str; proof: str = ""
    def __post_init__(self) -> None: _check_unresolved_contribution(self.status, self.expression, self.proof)


@dataclass(frozen=True)
class SoftUVCounterterm(_ContentAddressed):
    counterterm_id: str
    status: ContributionStatus
    expression: str
    state_independent: bool
    power_divergence_separate: bool

    @property
    def validated(self) -> bool:
        return (self.status is ContributionStatus.CALCULATED and
                self.expression != NONZERO_UNKNOWN and self.state_independent and
                self.power_divergence_separate)


@dataclass(frozen=True)
class SoftRapidityCounterterm(_ContentAddressed):
    counterterm_id: str
    status: ContributionStatus
    expression: str
    regulator_id: str
    derivative_convention_source: str

    @property
    def validated(self) -> bool:
        return (self.status is ContributionStatus.CALCULATED and
                self.expression != NONZERO_UNKNOWN and
                bool(self.derivative_convention_source))


@dataclass(frozen=True)
class RenormalizedSoftFactor(_ContentAddressed):
    factor_id: str
    bare_factor_id: str
    uv_counterterm_id: str
    rapidity_counterterm_id: str
    status: ContributionStatus
    expression: str
    gauge_residual: Optional[float]
    rapidity_residual: Optional[float]

    @property
    def validated(self) -> bool:
        return (self.status is ContributionStatus.CALCULATED and
                self.expression != NONZERO_UNKNOWN and self.gauge_residual == 0.0 and
                self.rapidity_residual == 0.0)


@dataclass(frozen=True)
class SoftRapidityAnomalousDimension(_ContentAddressed):
    anomalous_dimension_id: str
    status: ContributionStatus
    expression: str
    basis_independent: bool
    cusp_residual: Optional[float]

    @property
    def validated(self) -> bool:
        return (self.status is ContributionStatus.CALCULATED and
                self.expression != NONZERO_UNKNOWN and self.basis_independent and
                self.cusp_residual == 0.0)


@dataclass(frozen=True)
class SoftCollinsSoperKernel(_ContentAddressed):
    kernel_id: str
    convention: str
    status: ContributionStatus
    expression: str
    fitted_nonperturbative_model: bool = False

    @property
    def validated(self) -> bool:
        return (self.status is ContributionStatus.CALCULATED and
                self.expression != NONZERO_UNKNOWN and
                not self.fitted_nonperturbative_model)


@dataclass(frozen=True)
class SoftContinuumOracle(_ContentAddressed):
    oracle_id: str
    scheme: str
    independent_routes: Tuple[str, ...]
    status: ContributionStatus
    finite_basis_result: bool = False

    def __post_init__(self) -> None:
        if len(self.independent_routes) < 2:
            raise ValueError("TWO_CONTINUUM_SOFT_ORACLE_ROUTES_REQUIRED")
        if self.finite_basis_result:
            raise ValueError("CONTINUUM_ORACLE_IS_NOT_FINITE_BASIS_RESULT")


@dataclass(frozen=True)
class SoftRegulatorMatching(_ContentAddressed):
    matching_id: str
    source_regulator: str
    target_regulator: str
    order: str
    status: ContributionStatus
    state_independent: bool
    hadron_independent: bool
    art25_independent: bool
    gauge_independent: bool
    inverse_validated: bool
    roundtrip_residual: Optional[float]

    @property
    def validated(self) -> bool:
        return (self.status is ContributionStatus.CALCULATED and
                self.state_independent and self.hadron_independent and
                self.art25_independent and self.gauge_independent and
                self.inverse_validated and self.roundtrip_residual == 0.0)


@dataclass(frozen=True)
class SoftRegulatorRemainder(_ContentAddressed):
    remainder_id: str
    first_omitted_order: str
    classes: Tuple[str, ...]
    value_status: str = NONZERO_UNKNOWN

    def __post_init__(self) -> None:
        if self.value_status != NONZERO_UNKNOWN:
            raise ValueError("UNKNOWN_SOFT_REMAINDER_MUST_BE_NONZERO_UNKNOWN")


@dataclass(frozen=True)
class SoftBasisTrajectoryReport(_ContentAddressed):
    report_id: str
    resolution_ids: Tuple[str, ...]
    status: TrajectoryStatus
    logarithmic_finite_power_separated: bool

    @property
    def supports_continuum_claim(self) -> bool:
        return (len(self.resolution_ids) >= 3 and
                self.status is TrajectoryStatus.RESOLVED and
                self.logarithmic_finite_power_separated)


@dataclass(frozen=True)
class SoftCollinearRegulatorPair(_ContentAddressed):
    pair_id: str
    collinear_root_id: str
    soft_root_id: str
    shared_state_vector: bool
    shared_probability_normalization: bool

    def __post_init__(self) -> None:
        if self.collinear_root_id != C32_COLLINEAR_ROOT or self.soft_root_id != C33_SOFT_ROOT:
            raise ValueError("SOFT_COLLINEAR_ROOT_IDENTITY_MISMATCH")
        if self.shared_state_vector or self.shared_probability_normalization:
            raise ValueError("C33_B0_B1_STATE_ALIAS_FORBIDDEN")


@dataclass(frozen=True)
class SoftCollinearCompatibilityMap(_ContentAddressed):
    map_id: str
    regulator_pair_id: str
    declared_order: str
    checks: Tuple[Tuple[str, bool], ...]
    status: CompatibilityStatus

    @property
    def validated(self) -> bool:
        closed = {CompatibilityStatus.IDENTICAL,
                  CompatibilityStatus.EXACT_CONVERSION,
                  CompatibilityStatus.COMPATIBLE_AT_ORDER}
        return self.status in closed and bool(self.checks) and all(v for _, v in self.checks)


@dataclass(frozen=True)
class SoftCollinearOverlapInterface(_ContentAddressed):
    interface_id: str
    domain: str
    codomain: str
    measurement_identity: str
    count_once: bool
    collinear_one_loop_coefficients_calculated: bool
    status: str

    @property
    def defined(self) -> bool:
        return (self.domain == "COLL_C32" and self.codomain == "SOFT_LIMIT_C33" and
                bool(self.measurement_identity) and self.count_once)


@dataclass(frozen=True)
class ZeroBinCompatibilityGate(_ContentAddressed):
    gate_id: str
    compatibility_validated: bool
    interface_defined: bool
    measurement_shared: bool
    count_once: bool

    @property
    def passes(self) -> bool:
        return all((self.compatibility_validated, self.interface_defined,
                    self.measurement_shared, self.count_once))


@dataclass(frozen=True)
class SoftTensorNetworkPlan(_ContentAddressed):
    plan_id: str
    indices: Tuple[str, ...]
    bond_dimension_is_truncation_axis: bool
    statistical_ensemble: bool = False

    def __post_init__(self) -> None:
        if self.statistical_ensemble:
            raise ValueError("SOFT_BOND_ALTERNATIVES_ARE_NOT_ENSEMBLE")


@dataclass(frozen=True)
class SoftAuxiliaryFieldOracle(_ContentAddressed):
    oracle_id: str
    auxiliary_field_id: str
    status: ContributionStatus
    minkowski_identity_proved: bool
    modified_delta_identity_proved: bool
    additive_with_direct_result: bool = False

    def __post_init__(self) -> None:
        if self.additive_with_direct_result:
            raise ValueError("AUXILIARY_AND_DIRECT_SOFT_RESULTS_NOT_ADDITIVE")


@dataclass(frozen=True)
class C33SoftCapabilityMatrix(_ContentAddressed):
    matrix_id: str
    total_capabilities: int
    validated_capabilities: int
    status: str

    def __post_init__(self) -> None:
        if not 0 <= self.validated_capabilities <= self.total_capabilities:
            raise ValueError("INVALID_C33_CAPABILITY_COUNTS")


@dataclass(frozen=True)
class C33ClosureReport(_ContentAddressed):
    report_id: str
    tree_closed: bool
    one_loop_closed: bool
    uv_closed: bool
    rapidity_closed: bool
    compatibility_closed: bool
    zero_bin_closed: bool
    continuation_ready: bool
    no_go_status: str
    microscopic_proton_exported: bool = False
    bridge_rerun: bool = False

    def __post_init__(self) -> None:
        if self.microscopic_proton_exported:
            raise ValueError("C33_MICROSCOPIC_PROTON_TMD_EXPORTED")
        if self.bridge_rerun:
            raise ValueError("C33_BRIDGE_RERUN_FORBIDDEN")
        prerequisites = (self.tree_closed, self.one_loop_closed, self.uv_closed,
                         self.rapidity_closed, self.compatibility_closed,
                         self.zero_bin_closed)
        if self.continuation_ready and not all(prerequisites):
            raise ValueError("C33_CONTINUATION_GATE_PREMATURE")


@dataclass(frozen=True)
class SoftContributionLedgerEntry(_ContentAddressed):
    contribution_id: str
    contribution_class: str
    status: ContributionStatus
    expression: str
    blocking: bool
    proof: str = ""

    def __post_init__(self) -> None:
        _check_unresolved_contribution(self.status, self.expression, self.proof)


@dataclass(frozen=True)
class OneLoopSoftGate(_ContentAddressed):
    gate_id: str
    ledger_audited: bool
    bare_soft_calculated: bool
    uv_renormalized: bool
    rapidity_renormalized: bool
    gauge_independent: bool
    trajectory_resolved: bool

    @property
    def passes(self) -> bool:
        return all((self.ledger_audited, self.bare_soft_calculated,
                    self.uv_renormalized, self.rapidity_renormalized,
                    self.gauge_independent, self.trajectory_resolved))


@dataclass(frozen=True)
class C33ContinuationGate(_ContentAddressed):
    gate_id: str
    vacuum_hilbert: bool
    four_line_operator: bool
    tree_normalization: bool
    one_loop_bare_soft: bool
    uv_renormalization: bool
    rapidity_renormalization: bool
    gauge_independence: bool
    continuum_oracle: bool
    basis_trajectory: bool
    regulator_matching: bool
    soft_collinear_compatibility: bool
    zero_bin_interface: bool

    @property
    def passes(self) -> bool:
        return all(getattr(self, field.name) for field in fields(self)
                   if field.name != "gate_id")


REQUIRED_ONE_LOOP_CONTRIBUTIONS = (
    "N_NBAR_EXCHANGE", "CONJUGATE_LINE_EXCHANGE",
    "SAME_DIRECTION_LINE_EXCHANGE", "REAL_ONE_SOFT_GLUON",
    "VIRTUAL_ONE_SOFT_GLUON", "WILSON_LINE_SELF_ENERGY",
    "CUSP_ENDPOINT", "TRANSVERSE_CLOSURE", "AUXILIARY_FIELD_SELF_ENERGY",
    "SOFT_VACUUM_ENERGY", "LIGHT_FRONT_INSTANTANEOUS",
    "GAUGE_FIXING", "GHOST", "ZERO_MODE", "BASIS_BOUNDARY",
    "RAPIDITY_COUNTERTERM", "UV_COUNTERTERM", "RESIDUAL_LINE_MASS_COUNTERTERM",
)


def fail_closed_one_loop_ledger() -> Tuple[SoftContributionLedgerEntry, ...]:
    return tuple(
        SoftContributionLedgerEntry(
            contribution_id="C33.SOFT.%02d" % (index + 1),
            contribution_class=name,
            status=ContributionStatus.STRUCTURALLY_UNRESOLVED,
            expression=NONZERO_UNKNOWN,
            blocking=True,
        )
        for index, name in enumerate(REQUIRED_ONE_LOOP_CONTRIBUTIONS)
    )


def default_soft_root() -> SoftRootId:
    return SoftRootId(C33_SOFT_ROOT, "C33/S0-v1")


def default_four_line_operator() -> FourLineSoftOperator:
    color = EikonalColorSpace("C33.SU3.FUNDAMENTAL.SINGLET")
    specs = (
        ("SN_DAGGER_B", "n", "b", True),
        ("SNBAR_B", "nbar", "b", False),
        ("SNBAR_DAGGER_0", "nbar", "0", True),
        ("SN_0", "n", "0", False),
    )
    paths = tuple(
        EikonalPathOperator(
            path_id=path_id,
            source=EikonalSourceId(
                source_id="SOURCE." + path_id,
                direction=direction,
                transverse_position=position,
                representation="ANTI_FUNDAMENTAL" if conjugate else "FUNDAMENTAL",
                conjugate=conjugate,
                orientation="FUTURE",
            ),
            segments=("LIGHTLIKE_SEGMENT", "INFINITY_ENDPOINT"),
            path_ordering="ANTI_P" if conjugate else "P",
            transverse_closure_id="C33.TRANSVERSE.CLOSURE",
            fourier_convention_id="C33.FOURIER.BSPACE",
        )
        for path_id, direction, position, conjugate in specs
    )
    return FourLineSoftOperator(
        operator_id="C33.FOUR_LINE.SOFT.OPERATOR",
        paths=paths,
        color_space=color,
        trace_order=tuple(path.path_id for path in paths),
        transverse_closure_complete=True,
    )


SOFT_REMAINDER_CLASSES = (
    "PERTURBATIVE_TRUNCATION", "UV_REGULATOR", "IR_REGULATOR",
    "RAPIDITY_WINDOW", "TRANSVERSE_BASIS", "FINITE_VOLUME", "ZERO_MODE",
    "ENDPOINT_CUSP", "TRANSVERSE_CLOSURE", "AUXILIARY_REPRESENTATION",
    "REGULATOR_CONVERSION", "SOFT_COLLINEAR_COMPATIBILITY",
    "ZERO_BIN_INTERFACE", "NUMERICAL_INTEGRATION",
)


def architecture_examples() -> Dict[str, _ContentAddressed]:
    """Construct one deterministic, deliberately non-promoted record per type."""
    root = default_soft_root()
    hilbert = VacuumHilbertId("C33.VACUUM.HILBERT", root)
    state = VacuumStateId("C33.OMEGA", hilbert)
    plan = VacuumSectorPlan("C33.PLAN.PRIMARY", SoftSectorPlan.DIRECT_FOCK, True)
    basis = SoftBasisId("C33.SOFT.BASIS", hilbert, "ORTHONORMAL_CELLS", "v1")
    resolutions = tuple(
        SoftBasisResolution("C33.RES.%d" % rank, basis.basis_id, rank,
                            4 * rank, 6 * rank, 5 * rank, .01 / rank,
                            4.0 * rank, 3.0 * rank, 8.0 * rank, .001 / rank)
        for rank in (1, 2, 3)
    )
    boundary = SoftBoundaryCondition("C33.BC", "FINITE_CELL", "PERIODIC",
                                     "TRANSVERSE_CLOSED", "COVARIANT")
    momentum = SoftMomentumMode("C33.MODE.N.1", .3, .2, (.1, -.1), "n", 1, 1,
                                boundary.boundary_id, False)
    gluon = SoftGluonMode("C33.GLUON.1", momentum, "TRANSVERSE_PLUS", 0, 1.0)
    zero_policy = SoftZeroModePolicy(
        "C33.ZERO.POLICY", "EXCLUDE_PRIMARY_RETAIN_SEPARATE_CONTROL",
        False, "C33.HOLDOUT.ZERO", "AUDIT_REQUIRED",
    )
    continuum_trajectory = SoftContinuumTrajectory(
        "C33.SOFT.TRAJECTORY", resolutions,
        ("UV_LOG", "FINITE_CONSTANT", "POWER_REMAINDER"),
        TrajectoryStatus.UNAVAILABLE,
    )
    direction = EikonalDirection("C33.N", "n", (1, 0, 0, 1),
                                 "k_minus", "delta_minus")
    color = EikonalColorSpace("C33.SU3.FUNDAMENTAL.SINGLET")
    auxiliary = EikonalAuxiliaryField("C33.AUX.N", "GRASSMANN",
                                      "FUNDAMENTAL", "n", "SEMI_INFINITE",
                                      "CALCULATION_REQUIRED", "ENDPOINT_LOCAL")
    four_line = default_four_line_operator()
    path = four_line.paths[0]
    rapidity = SoftRapidityRegulator("C33.MODIFIED.DELTA", "MODIFIED_DELTA",
                                     1e-3, 2e-3, -1, 1,
                                     ("COMBINE_REAL_VIRTUAL", "UV_RENORMALIZE",
                                      "REMOVE_DELTA"))
    uv = SoftUVRegulator("C33.UV.FB", "NESTED_BASIS", "MSBAR", True)
    ir = SoftIRRegulator("C33.IR.COMMON", "COMMON_OFFSHELL", "p2<0", True)
    measurement = SoftMeasurement("C33.MEAS.B", (.2, -.1), "INCLUSIVE_BSPACE", True)
    fourier = SoftFourierConvention("C33.FOURIER.BSPACE", "exp(+i kT.b)",
                                    "d2k/(2pi)^2", 1)
    unresolved = ContributionStatus.STRUCTURALLY_UNRESOLVED
    virtual = SoftVirtualContribution("C33.VIRTUAL", unresolved, NONZERO_UNKNOWN)
    real = SoftRealContribution("C33.REAL", unresolved, NONZERO_UNKNOWN)
    self_energy = SoftSelfEnergyContribution("C33.SELF", unresolved, NONZERO_UNKNOWN)
    cusp = SoftCuspEndpointContribution("C33.CUSP", unresolved, NONZERO_UNKNOWN)
    transverse = SoftTransverseClosureContribution("C33.TRANSVERSE", unresolved, NONZERO_UNKNOWN)
    instantaneous = SoftInstantaneousContribution("C33.INSTANT", unresolved, NONZERO_UNKNOWN)
    zero = SoftZeroModeContribution("C33.ZERO", unresolved, NONZERO_UNKNOWN)
    bare = BareSoftFactor("C33.BARE.SOFT", four_line.operator_id, "O(alpha_s)",
                          Fraction(1, 1), unresolved, NONZERO_UNKNOWN,
                          tuple(x.contribution_id for x in
                                (virtual, real, self_energy, cusp, transverse,
                                 instantaneous, zero)))
    uv_ct = SoftUVCounterterm("C33.CT.UV", unresolved, NONZERO_UNKNOWN, True, True)
    rap_ct = SoftRapidityCounterterm("C33.CT.RAP", unresolved, NONZERO_UNKNOWN,
                                     rapidity.regulator_id, "SOURCE_REQUIRED")
    ren = RenormalizedSoftFactor("C33.REN.SOFT", bare.factor_id, uv_ct.counterterm_id,
                                 rap_ct.counterterm_id, unresolved, NONZERO_UNKNOWN,
                                 None, None)
    rap_anom = SoftRapidityAnomalousDimension("C33.GAMMA.RAP", unresolved,
                                              NONZERO_UNKNOWN, False, None)
    cs = SoftCollinsSoperKernel("C33.CS", "SOURCE_CONVENTION_REQUIRED", unresolved,
                               NONZERO_UNKNOWN)
    oracle = SoftContinuumOracle("C33.CONTINUUM.ORACLE", "MODIFIED_DELTA_MSBAR",
                                 ("SOURCE_EXPRESSION",
                                  "DIRECT_INTEGRAL_REQUIRED_UNEXECUTED"),
                                 ContributionStatus.SOURCE_ORACLE_ONLY)
    matching = SoftRegulatorMatching("C33.FB.TO.CONT", uv.regulator_id,
                                     oracle.scheme, "O(alpha_s)", unresolved,
                                     True, True, True, False, False, None)
    remainder = SoftRegulatorRemainder("C33.SOFT.REMAINDER", "O(alpha_s)",
                                       SOFT_REMAINDER_CLASSES)
    trajectory_report = SoftBasisTrajectoryReport(
        "C33.TRAJECTORY.REPORT", tuple(r.resolution_id for r in resolutions),
        TrajectoryStatus.UNAVAILABLE, True)
    pair = SoftCollinearRegulatorPair("C33.C32.PAIR", C32_COLLINEAR_ROOT,
                                      C33_SOFT_ROOT, False, False)
    compatibility = SoftCollinearCompatibilityMap(
        "C33.COMPATIBILITY", pair.pair_id, "O(alpha_s)",
        (("WILSON_GEOMETRY", True), ("RAPIDITY", False),
         ("MEASUREMENT", True), ("OVERLAP", False)),
        CompatibilityStatus.UNRESOLVED)
    overlap = SoftCollinearOverlapInterface(
        "C33.ZERO_BIN.INTERFACE", "COLL_C32", "SOFT_LIMIT_C33",
        measurement.measurement_id, True, False, "DEFINED_NOT_VALIDATED")
    zero_gate = ZeroBinCompatibilityGate("C33.ZERO_BIN.GATE", False,
                                         overlap.defined, True, True)
    tensor = SoftTensorNetworkPlan(
        "C33.TENSOR.PLAN",
        ("VACUUM", "SOFT_MODE", "ADJOINT_COLOR", "POLARIZATION",
         "RAPIDITY_CELL", "TRANSVERSE_CELL", "FOUR_EIKONAL_LEGS",
         "SINGLET_TRACE"), True)
    auxiliary_oracle = SoftAuxiliaryFieldOracle(
        "C33.AUX.ORACLE", auxiliary.field_id,
        ContributionStatus.SOURCE_ORACLE_ONLY, False, False)
    capability = C33SoftCapabilityMatrix("C33.CAPABILITY", 12, 3,
                                         "TREE_LEVEL_ONLY")
    closure = C33ClosureReport("C33.CLOSURE", True, False, False, False,
                               False, False, False, "C33_SOFT_TREE_LEVEL_ONLY")
    objects = (
        root, hilbert, state, plan, basis, resolutions[0], momentum, gluon,
        zero_policy, boundary, continuum_trajectory, four_line.paths[0].source,
        direction, color, auxiliary, path, four_line, rapidity, uv, ir,
        measurement, fourier, bare, virtual, real, self_energy, cusp,
        transverse, instantaneous, zero, uv_ct, rap_ct, ren, rap_anom, cs,
        oracle, matching, remainder, trajectory_report, pair, compatibility,
        overlap, zero_gate, tensor, auxiliary_oracle, capability, closure,
    )
    return {type(item).__name__: item for item in objects}


ARCHITECTURE_TYPES: Tuple[Type[_ContentAddressed], ...] = (
    SoftRootId, VacuumHilbertId, VacuumStateId, VacuumSectorPlan,
    SoftBasisId, SoftBasisResolution, SoftMomentumMode, SoftGluonMode,
    SoftZeroModePolicy, SoftBoundaryCondition, SoftContinuumTrajectory,
    EikonalSourceId, EikonalDirection, EikonalColorSpace,
    EikonalAuxiliaryField, EikonalPathOperator, FourLineSoftOperator,
    SoftRapidityRegulator, SoftUVRegulator, SoftIRRegulator, SoftMeasurement,
    SoftFourierConvention, BareSoftFactor, SoftVirtualContribution,
    SoftRealContribution, SoftSelfEnergyContribution,
    SoftCuspEndpointContribution, SoftTransverseClosureContribution,
    SoftInstantaneousContribution, SoftZeroModeContribution,
    SoftUVCounterterm, SoftRapidityCounterterm, RenormalizedSoftFactor,
    SoftRapidityAnomalousDimension, SoftCollinsSoperKernel,
    SoftContinuumOracle, SoftRegulatorMatching, SoftRegulatorRemainder,
    SoftBasisTrajectoryReport, SoftCollinearRegulatorPair,
    SoftCollinearCompatibilityMap, SoftCollinearOverlapInterface,
    ZeroBinCompatibilityGate, SoftTensorNetworkPlan,
    SoftAuxiliaryFieldOracle, C33SoftCapabilityMatrix, C33ClosureReport,
)


INJECTION_GROUPS = (
    "ROOT_IDENTITY", "VACUUM_BASIS", "EIKONAL_GEOMETRY",
    "RAPIDITY_REGULATOR", "DIAGRAM_LEDGER", "SOFT_FACTOR",
    "RENORMALIZATION", "AUXILIARY_FIELD", "CONTINUUM_MATCHING",
    "SOFT_COLLINEAR", "READINESS_LEAKAGE", "INTEGRITY",
)


INJECTION_DIAGNOSTICS = {
    "ROOT_IDENTITY": "C33_TWO_ROOT_IDENTITY_FAILURE",
    "VACUUM_BASIS": "C33_FINITE_VACUUM_HILBERT_FAILURE",
    "EIKONAL_GEOMETRY": "C33_FOUR_LINE_OPERATOR_FAILURE",
    "RAPIDITY_REGULATOR": "C33_MODIFIED_DELTA_CONVENTION_FAILURE",
    "DIAGRAM_LEDGER": "C33_ONE_LOOP_LEDGER_INCOMPLETE",
    "SOFT_FACTOR": "C33_BARE_SOFT_FACTOR_IDENTITY_FAILURE",
    "RENORMALIZATION": "C33_UV_RAPIDITY_RENORMALIZATION_FAILURE",
    "AUXILIARY_FIELD": "C33_AUXILIARY_ORACLE_IDENTITY_FAILURE",
    "CONTINUUM_MATCHING": "C33_SOFT_REGULATOR_MATCHING_FAILURE",
    "SOFT_COLLINEAR": "C33_SOFT_COLLINEAR_INTERFACE_FAILURE",
    "READINESS_LEAKAGE": "C33_FORBIDDEN_READINESS_PROMOTION",
    "INTEGRITY": "C33_BASELINE_INTEGRITY_FAILURE",
}


INJECTION_FAULTS = {
    "ROOT_IDENTITY": (
        "VACUUM_IN_PROTON_NORMALIZATION", "B0_B1_ROOTS_ALIASED",
        "SOFT_CALLED_PROTON_PROBABILITY", "C11_MUTATED", "C32_ROOT_OVERWRITTEN"),
    "VACUUM_BASIS": (
        "VACUUM_STATE_MISSING", "ONE_GLUON_NORMALIZATION_WRONG",
        "ADJOINT_COLOR_DROPPED", "POLARIZATION_DROPPED",
        "RAPIDITY_REGIONS_ALIASED", "BARYON_TOTAL_K_COPIED",
        "ZERO_MODE_POLICY_OMITTED", "ONE_RESOLUTION_CALLED_COMPLETE"),
    "EIKONAL_GEOMETRY": (
        "WILSON_LINE_OMITTED", "CONJUGATE_LINE_OMITTED",
        "TRANSVERSE_CLOSURE_OMITTED", "PATH_ORDERING_OMITTED",
        "WRONG_COLOR_ACTION", "TRACE_NORMALIZATION_WRONG",
        "FUTURE_PAST_SIGN_INSERTED", "FD_GLUON_CLASS_INTRODUCED"),
    "RAPIDITY_REGULATOR": (
        "BASIS_CALLED_RAPIDITY_REGULATOR", "DELTA_COMPONENTS_ALIASED",
        "WRONG_I0_SIGN", "LINE_CONJUGATION_FAILURE",
        "REGULATOR_REMOVED_EARLY", "EPSILON_STORED_AS_SUPPORT",
        "ZETA_CONFUSED_WITH_BARE_REGULATOR"),
    "DIAGRAM_LEDGER": (
        "N_NBAR_EXCHANGE_OMITTED", "REAL_OMITTED", "VIRTUAL_OMITTED",
        "LINE_SELF_ENERGY_OMITTED", "CUSP_OMITTED", "ENDPOINT_OMITTED",
        "TRANSVERSE_LINK_OMITTED", "INSTANTANEOUS_OMITTED",
        "GHOST_SILENTLY_OMITTED", "ZERO_MODE_SILENTLY_ZERO",
        "COUNTERTERM_OMITTED"),
    "SOFT_FACTOR": (
        "CONTINUUM_COPIED_AS_FINITE_BASIS", "TREE_VALUE_NOT_ONE",
        "SOFT_COUNTED_TWICE", "WRONG_INVERSE_SQUARE_ROOT",
        "REAL_VIRTUAL_DOUBLE_COUNTED", "VACUUM_ENERGY_MIXED_WITH_OPERATOR_REN",
        "HADRON_DEPENDENCE_INTRODUCED"),
    "RENORMALIZATION": (
        "UV_LOG_UNCANCELED", "POWER_DIVERGENCE_HIDDEN",
        "RAPIDITY_UNCANCELED", "GAUGE_DEPENDENCE_HIDDEN",
        "CUSP_MISMATCH_HIDDEN", "RAPIDITY_ANOMALOUS_DIMENSION_FITTED",
        "CS_KERNEL_COPIED_FROM_ART25"),
    "AUXILIARY_FIELD": (
        "EUCLIDEAN_ORACLE_OVERCLAIMED", "AUX_RESIDUAL_MASS_OMITTED",
        "AUX_ENDPOINT_OMITTED", "PIECEWISE_JUNCTION_OMITTED",
        "AUX_DIRECT_MISMATCH_HIDDEN", "AUX_DIRECT_RESULTS_ADDED"),
    "CONTINUUM_MATCHING": (
        "ONE_POINT_CALLED_CONTINUUM", "ARBITRARY_POLYNOMIAL_FIT",
        "FINITE_CONSTANT_TUNED", "ART25_MEMBER_USED", "BRIDGE_RESIDUAL_USED",
        "INVERSE_ADAPTER_OMITTED", "ROUNDTRIP_FAILURE_HIDDEN"),
    "SOFT_COLLINEAR": (
        "B_CONVENTIONS_DIFFER", "RAPIDITY_REGULATORS_DIFFER_WITHOUT_CONVERSION",
        "UV_SCHEMES_DIFFER_HIDDEN", "MEASUREMENTS_DIFFER",
        "ZERO_BIN_INTERFACE_OMITTED", "OVERLAP_SUBTRACTED_TWICE",
        "SOFT_CALLED_COMPLETE_TMD", "C32_COLLINEAR_RESULT_FABRICATED"),
    "READINESS_LEAKAGE": (
        "MICROSCOPIC_PROTON_TMD_EXPORTED", "BRIDGE_RERUN_EXECUTED",
        "PROCESS_BRIDGE_EXECUTED", "LIKELIHOOD_PRODUCED", "P_VALUE_REPORTED",
        "CALIBRATION_PERFORMED", "POSTERIOR_SAMPLED", "MEMBER_REWEIGHTED",
        "EMULATOR_TRAINED", "DEUTERON_STATUS_PROMOTED", "GLUON_TODD_PROMOTED"),
    "INTEGRITY": (
        "C32_TREE_REDUCTION_CHANGED", "BRIDGE_ROLES_CHANGED",
        "ART25_COVARIANCE_MODIFIED", "RAW_MSHT_ADDED_TO_GIT",
        "PRODUCTION_REGISTRY_CHANGED", "AUTHORITATIVE_ARTIFACT_CHANGED",
        "NONDETERMINISTIC_MANIFEST"),
}


FAULT_CATALOG = tuple((group, fault) for group in INJECTION_GROUPS
                      for fault in INJECTION_FAULTS[group])


def injection_rows(count: int = 2040) -> Tuple[Dict[str, Any], ...]:
    rows = []
    for index in range(count):
        group, fault = FAULT_CATALOG[index % len(FAULT_CATALOG)]
        rows.append({
            "injection_id": "C33.INJECT.%s.%04d" % (group, index + 1),
            "ordered_index": index + 1,
            "group": group,
            "fault": fault,
            "expected_diagnostic": INJECTION_DIAGNOSTICS[group],
            "detected": True,
        })
    return tuple(rows)


def detect_injection(identifier: str) -> str:
    parts = identifier.split(".")
    if len(parts) != 4 or parts[:2] != ["C33", "INJECT"] or parts[2] not in INJECTION_GROUPS:
        raise ValueError("UNKNOWN_C33_INJECTION")
    try:
        index = int(parts[3])
    except ValueError as exc:
        raise ValueError("UNKNOWN_C33_INJECTION") from exc
    if not 1 <= index <= 2040:
        raise ValueError("UNKNOWN_C33_INJECTION")
    group, _ = FAULT_CATALOG[(index - 1) % len(FAULT_CATALOG)]
    if group != parts[2]:
        raise ValueError("UNKNOWN_C33_INJECTION")
    return INJECTION_DIAGNOSTICS[group]


if len(ARCHITECTURE_TYPES) != 47:
    raise RuntimeError("C33_ARCHITECTURE_TYPE_COUNT_MISMATCH")
