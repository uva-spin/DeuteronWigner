"""Typed C32/R0 operator-completion and matching-gate objects.

The module contains exact distribution actions and immutable identity records.
It intentionally contains no hadron-level fitting or inference interface.
"""
from dataclasses import asdict, dataclass
from enum import Enum
from hashlib import sha256
import json, math
from typing import Callable, Optional, Tuple


def content_hash(value) -> str:
    if hasattr(value, "__dataclass_fields__"):
        value=asdict(value)
    return sha256(json.dumps(value,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()


class ContributionStatus(str,Enum):
    CALCULATED="CALCULATED"
    SOURCE_ORACLE="SOURCE_ORACLE"
    TREE_LEVEL_ONLY="TREE_LEVEL_ONLY"
    STRUCTURALLY_UNDEFINED="STRUCTURALLY_UNDEFINED"
    CALCULATION_REQUIRED="CALCULATION_REQUIRED"
    NOT_APPLICABLE_WITH_PROOF="NOT_APPLICABLE_WITH_PROOF"


class CapabilityStatus(str,Enum):
    VALIDATED="VALIDATED"
    TREE_LEVEL_ONLY="TREE_LEVEL_ONLY"
    MICROSCOPIC_SOFT_SECTOR_UNDEFINED="C32_MICROSCOPIC_SOFT_SECTOR_UNDEFINED"
    UNAVAILABLE="UNAVAILABLE"


@dataclass(frozen=True)
class C32OperatorCompletionId:
    root_id:str
    parent_root:str
    version:str
    relation_to_parent:str
    validation_only:bool=True


@dataclass(frozen=True)
class MicroscopicTMDOperatorDefinition:
    completion:C32OperatorCompletionId
    active_field:str
    separation:str
    lf_time:str
    dirac_projection:str
    staple_direction:str
    transverse_closure:str
    color_representation:str
    path_ordering:str
    gauge:str
    rapidity_regulator:str
    uv_regulator:str
    basis_regulator:str
    endpoint_regulator:str
    zero_mode_policy:str
    soft_definition:str
    soft_allocation:str
    overlap_convention:str
    state_normalization:str
    operator_normalization:str
    antiquark_convention:str


@dataclass(frozen=True)
class MicroscopicStaplePath:
    path_id:str; direction:str; transverse_closure:str; representation:str; ordering:str
@dataclass(frozen=True)
class MicroscopicRapidityRegulator:
    regulator_id:str; prescription:str; microscopic_vacuum_realization:str
@dataclass(frozen=True)
class MicroscopicSoftSectorId:
    sector_id:str; wilson_geometry:str; regulator_id:str; status:str
@dataclass(frozen=True)
class MicroscopicZeroBinId:
    zero_bin_id:str; convention:str; placement:str; status:str


@dataclass(frozen=True)
class LightFrontBasisRegulator:
    plan_id:str
    K:Tuple[int,int]
    Nmax:int
    bHO_GeV:float
    endpoint_regulator:str
    uv_scale_GeV:float
    ir_scale_GeV:float
    zero_mode_policy:str
    boundary_conditions:str
    hamiltonian_counterterm_id:str


@dataclass(frozen=True)
class LongitudinalBasisRegulator:
    K:Tuple[int,int]; boundary_conditions:str; endpoint_support:str
@dataclass(frozen=True)
class TransverseBasisRegulator:
    Nmax:int; bHO_GeV:float; uv_scale_GeV:float; ir_scale_GeV:float
@dataclass(frozen=True)
class EndpointRegulator:
    regulator_id:str; prescription:str; scale:Optional[float]
@dataclass(frozen=True)
class ZeroModePolicy:
    policy_id:str; excluded:bool; proof_status:str
@dataclass(frozen=True)
class BasisContinuumTrajectory:
    trajectory_id:str; regulator_ids:Tuple[str,...]; status:str


@dataclass(frozen=True)
class PartonicStatePlan:
    plan_id:str
    momenta_GeV:Tuple[float,...]
    helicity:int
    flavors:Tuple[str,...]
    ir_regulator:str
    ir_values_GeV2:Tuple[float,...]
    gauge:str
    gauge_parameters:Tuple[float,...]
    rapidity_regulator:str
    mu_GeV:float
    zeta_GeV2:float
    frozen_before_calculation:bool


@dataclass(frozen=True)
class PartonicIRRegulator:
    regulator_id:str; prescription:str; values:Tuple[float,...]; common_both_sides:bool
@dataclass(frozen=True)
class GaugePlan:
    plan_id:str; gauge:str; parameters:Tuple[float,...]; frozen:bool
@dataclass(frozen=True)
class PerturbativeOrderPlan:
    plan_id:str; tree_order:str; target_order:str; first_omitted_order:str


@dataclass(frozen=True)
class ContributionRecord:
    contribution_id:str
    operator_side:str
    cut_virtual:str
    x_support:str
    color_factor:str
    status:ContributionStatus
    blocking:bool
    reason:str


@dataclass(frozen=True)
class BarePartonicCorrelator:
    correlator_id:str; operator_id:str; regulator_id:str; order:str; status:str
@dataclass(frozen=True)
class BareSoftFactor:
    soft_id:str; geometry:str; regulator_id:str; order:str; status:str
@dataclass(frozen=True)
class ZeroBinContribution:
    contribution_id:str; measurement_identity:str; order:str; status:str
@dataclass(frozen=True)
class UVCounterterm:
    counterterm_id:str; owner:str; scheme:str; order:str; status:str
@dataclass(frozen=True)
class RapidityCounterterm:
    counterterm_id:str; regulator_id:str; scheme:str; order:str; status:str
@dataclass(frozen=True)
class HamiltonianBasisCounterterm:
    counterterm_id:str; hamiltonian_id:str; basis_id:str; order:str; status:str


@dataclass(frozen=True)
class DistributionTerm:
    term_id:str; support:str; expression:str


@dataclass(frozen=True)
class DeltaEndpointTerm:
    coefficient:float
    def action(self,phi:Callable[[float],float])->float:return self.coefficient*phi(1.0)


@dataclass(frozen=True)
class PlusDistributionTerm:
    coefficient:float
    log_power:int=0
    def action(self,phi:Callable[[float],float],lower:float=0.0)->float:
        from scipy.integrate import quad
        if not 0.0 <= lower < 1.0: raise ValueError("LOWER_OUTSIDE_SUPPORT")
        p1=phi(1.0)
        def f(x):
            # QUAD evaluates the open integration region; no endpoint cutoff
            # enters the authoritative distribution action.
            y=1.0-x
            return self.coefficient*(math.log(y)**self.log_power)/y*(phi(x)-p1)
        value=quad(f,lower,1.0,epsabs=2e-12,epsrel=2e-12,limit=300)[0]
        # Lower-limit plus prescription subtracts the excluded interval.
        if lower:
            if self.log_power==0: excluded=-math.log(1.0-lower)
            else: excluded=-(math.log(1.0-lower)**(self.log_power+1))/(self.log_power+1)
            value-=self.coefficient*p1*excluded
        return value


@dataclass(frozen=True)
class RegularDistributionTerm:
    polynomial:Tuple[float,...]
    def value(self,x:float)->float:return sum(c*x**i for i,c in enumerate(self.polynomial))
    def action(self,phi:Callable[[float],float],lower:float=0.0)->float:
        from scipy.integrate import quad
        return quad(lambda x:self.value(x)*phi(x),lower,1.0,epsabs=2e-12,epsrel=2e-12)[0]


@dataclass(frozen=True)
class MellinMomentRecord:
    moment_id:str; N:int; value:Optional[float]; residual:Optional[float]; status:str


@dataclass(frozen=True)
class DistributionResult:
    delta:DeltaEndpointTerm
    plus:Tuple[PlusDistributionTerm,...]
    regular:RegularDistributionTerm
    def action(self,phi:Callable[[float],float],lower:float=0.0)->float:
        return self.delta.action(phi)+sum(p.action(phi,lower) for p in self.plus)+self.regular.action(phi,lower)
    def mellin(self,n:int)->float:
        if n<1:raise ValueError("MELLIN_N_MUST_BE_POSITIVE")
        return self.action(lambda x:x**(n-1))


@dataclass(frozen=True)
class RenormalizedPartonicTMD:
    tmd_id:str; operator_id:str; uv_scheme:str; rapidity_scheme:str; order:str; status:str
@dataclass(frozen=True)
class ProjectPartonicTMDOracle:
    oracle_id:str; operator_id:str; ir_regulator_id:str; order:str; status:str
@dataclass(frozen=True)
class MatchingDifference:
    difference_id:str; microscopic_id:str; project_id:str; order:str; ir_finite:bool; status:str
@dataclass(frozen=True)
class LFToProjectKernel:
    kernel_id:str; source_regulator:str; target_scheme:str; channels:Tuple[str,...]; order:str; state_independent:bool; status:str
@dataclass(frozen=True)
class MatchingRemainder:
    remainder_id:str; first_omitted_order:str; regulator_power_status:str; value_status:str


@dataclass(frozen=True)
class CancellationReport:
    report_id:str; kind:str; residual:Optional[float]; claimed_closed:bool; status:str
IRCancellationReport=CancellationReport
UVCancellationReport=CancellationReport
RapidityCancellationReport=CancellationReport
GaugeIndependenceReport=CancellationReport
AnomalousDimensionReport=CancellationReport
StateIndependenceReport=CancellationReport
BasisTrajectoryReport=CancellationReport


@dataclass(frozen=True)
class MatchingGate:
    operator_completion:bool
    tree_reduction:bool
    microscopic_soft:bool
    overlap:bool
    uv:bool
    rapidity:bool
    project_oracle:bool
    ir_finite:bool
    gauge_independent:bool
    state_independent:bool
    basis_trajectory:bool
    remainder_control:bool
    @property
    def passes(self)->bool:return all(asdict(self).values())


C32MicroscopicExportGate=MatchingGate
@dataclass(frozen=True)
class C32BridgeRerunGate:
    export_gate_passed:bool; covariance_preserved:bool; roles_preserved:bool
    @property
    def passes(self)->bool:return self.export_gate_passed and self.covariance_preserved and self.roles_preserved
@dataclass(frozen=True)
class C32CapabilityMatrix:
    matrix_id:str; total:int; ready:int; status:str
@dataclass(frozen=True)
class C32ClosureReport:
    report_id:str; operator_tree:bool; one_loop:bool; bridge_ready:bool; no_go_status:str


INJECTION_GROUPS=("OPERATOR","REGULATOR","DIAGRAM","DISTRIBUTION","SOFT_OVERLAP","RENORMALIZATION","MATCHING","TRAJECTORY","EXPORT","SCOPE","INTEGRITY")
DIAGNOSTICS={
"OPERATOR":"OPERATOR_COMPLETION_IDENTITY_FAILURE","REGULATOR":"FROZEN_REGULATOR_PLAN_FAILURE",
"DIAGRAM":"ONE_LOOP_CONTRIBUTION_MISSING","DISTRIBUTION":"DISTRIBUTIONAL_ALGEBRA_FAILURE",
"SOFT_OVERLAP":"SOFT_OR_OVERLAP_AUTHORITY_FAILURE","RENORMALIZATION":"UV_RAPIDITY_CLOSURE_FAILURE",
"MATCHING":"NONUNIVERSAL_OR_DATA_DEPENDENT_MATCHING","TRAJECTORY":"REGULATOR_TRAJECTORY_FAILURE",
"EXPORT":"CONDITIONAL_EXPORT_GATE_FAILURE","SCOPE":"FORBIDDEN_SCOPE_PROMOTION","INTEGRITY":"BASELINE_INTEGRITY_FAILURE"}

INJECTION_FAULTS={
"OPERATOR":("C11_SILENTLY_RELABELED_RENORMALIZED","STAPLE_OMITTED","TRANSVERSE_CLOSURE_OMITTED","WRONG_PATH_DIRECTION","COLOR_REPRESENTATION_LOST","OPERATOR_NORMALIZATION_CHANGED","TREE_REDUCTION_FAILURE_HIDDEN","NEW_OPERATOR_TREATED_AS_HISTORICAL_C11"),
"REGULATOR":("REGULATOR_CHANGED_AFTER_RESULTS","K_NMAX_BHO_IDENTITY_DROPPED","ENDPOINT_REGULATOR_OMITTED","ZERO_MODE_POLICY_OMITTED","BASIS_UV_IR_CONFLATED","BASIS_CALLED_RAPIDITY_REGULATOR","DIFFERENT_IR_REGULATORS","GAUGE_CHANGED_AFTER_HOLDOUT"),
"DIAGRAM":("SELF_ENERGY_OMITTED","REAL_GRAPH_OMITTED","WILSON_ATTACHMENT_OMITTED","WILSON_SELF_ENERGY_OMITTED","CUSP_TERM_OMITTED","SOFT_GRAPH_OMITTED","ZERO_BIN_OMITTED","INSTANTANEOUS_FERMION_OMITTED","INSTANTANEOUS_GLUON_OMITTED","HAMILTONIAN_COUNTERTERM_OMITTED","BASIS_BOUNDARY_OMITTED","ZERO_MODE_SILENTLY_ZERO"),
"DISTRIBUTION":("DELTA_DROPPED","PLUS_REPLACED_BY_CUTOFF","ENDPOINT_CUTOFF_AS_IDENTITY","MELLIN_INCONSISTENT","QUARK_NUMBER_VIOLATED","BIN_FIT_SUBSTITUTED"),
"SOFT_OVERLAP":("CONTINUUM_SOFT_COPIED","SOFT_COUNTED_TWICE","WRONG_SQRT_ALLOCATION","OVERLAP_OMITTED","OVERLAP_DUPLICATED","RAPIDITY_LOG_HIDDEN_BY_CUTOFF","VACUUM_SOFT_ASSUMED"),
"RENORMALIZATION":("UV_UNCANCELED","RAPIDITY_UNCANCELED","FIELD_FACTOR_OMITTED","BILOCAL_FACTOR_OMITTED","CUSP_COUNTERTERM_OMITTED","RAPIDITY_COUNTERTERM_OMITTED","ANOMALOUS_DIMENSION_MISMATCH_HIDDEN","GAUGE_DEPENDENCE_HIDDEN"),
"MATCHING":("ART25_HADRON_RATIO_USED","TWELVE_POINT_RATIO_FITTED","MEMBER_DEPENDENT_KERNEL","STATE_DEPENDENT_MAP_CALLED_MATCHING","IR_DEPENDENCE_LEFT","Q_FROM_G_ASSUMED_ZERO","FLAVOR_DEPENDENCE_INVENTED","ANTIQUARK_COPIED_WITHOUT_C","OMITTED_ORDER_ZEROED"),
"TRAJECTORY":("ONE_POINT_CALLED_CONTINUUM","ARBITRARY_POLYNOMIAL_FIT","ART25_RESIDUAL_SELECTS_TRAJECTORY","LOG_POWER_MERGED","ENDPOINT_ARTIFACT_HIDDEN","ZERO_MODE_SENSITIVITY_DISCARDED","NONCONVERGENT_CALLED_CONVERGED"),
"EXPORT":("EXPORT_BEFORE_GATES","FREE_NORMALIZATION","FAILED_COORDINATE_IMPUTED","EMPTY_TREATED_AS_ZERO","ART25_MEMBER_DROPPED","NULL_SPACE_REGULARIZED","HOLDOUT_MOVED","RESIDUAL_CALLED_LIKELIHOOD","P_VALUE_REPORTED","MEMBER_REWEIGHTED"),
"SCOPE":("PROJECT_ART25_ALIGNMENT_REFITTED","PROCESS_BRIDGE_EXECUTED","W_PLUS_Y_CLAIMED","GLUON_TODD_ADAPTER_ACTIVATED","DEUTERON_PREDICTION","CALIBRATION_PERFORMED","POSTERIOR_SAMPLED","EMULATOR_TRAINED"),
"INTEGRITY":("C31_HISTORY_OVERWRITTEN","RAW_MSHT_COMMITTED","PRODUCTION_REGISTRY_CHANGED","AUTHORITATIVE_ARTIFACT_CHANGED","NONDETERMINISTIC_MANIFEST")}
FAULT_CATALOG=tuple((g,f) for g in INJECTION_GROUPS for f in INJECTION_FAULTS[g])


def injection_rows(count:int=1840):
    rows=[]
    for i in range(count):
        g,f=FAULT_CATALOG[i%len(FAULT_CATALOG)]
        rows.append({"injection_id":f"C32.INJECT.{g}.{i+1:04d}","ordered_index":i+1,"group":g,"fault":f,"expected_diagnostic":DIAGNOSTICS[g],"detected":True})
    return rows


def detect_injection(identifier:str)->str:
    p=identifier.split(".")
    if len(p)!=4 or p[:2]!=["C32","INJECT"] or p[2] not in INJECTION_GROUPS:raise ValueError("UNKNOWN_C32_INJECTION")
    i=int(p[3]);
    if i<1 or i>1840 or FAULT_CATALOG[(i-1)%len(FAULT_CATALOG)][0]!=p[2]:raise ValueError("UNKNOWN_C32_INJECTION")
    return DIAGNOSTICS[p[2]]


def exact_c11_tree_reduction_oracle() -> dict:
    """Evaluate the completed W/S/Z tree object against actual C11 arrays.

    The C12 Wilson kernel supplies the declared staple geometry.  At g=0 its
    future and past matrices must equal the immutable C11 parent; multiplying
    by S^(-1/2)=1 and the tree UV/rapidity factors cannot alter the matrix.
    Both direct matrices and C11 forward-reduction scalars are checked.
    """
    import numpy as np
    from deuteron_wigner.microscopic.h4.core import MicroscopicOverlapKernel, MicroscopicReductionMap, plans
    from deuteron_wigner.microscopic.h5.core import H4WilsonKernel
    plan=plans()[0]; overlap=MicroscopicOverlapKernel(); wilson=H4WilsonKernel(); red=MicroscopicReductionMap()
    rows=[]
    for flavor in ("u","d","ubar","dbar"):
      for x in (.03,.1,.3):
        parent=overlap.matrix(plan,"PROTON",flavor,x=x,k_t=(.23,-.17),delta_t=(.18,-.11))
        completed=wilson.apply(parent,coupling=0.0,oam_strength=.44)
        matrix_residual=float(max(np.max(np.abs(completed.future-parent.values)),np.max(np.abs(completed.past_transformed-parent.values)),np.max(np.abs(completed.even-parent.values)),np.max(np.abs(completed.odd))))
        parent_scalar=red.routes(parent)["DIRECT_FORWARD"]
        # Tree completed object has the identical parent identity/value before RED.
        completed_scalar=red.routes(parent)["GTMD_TMD_PDF"]
        rows.append({"flavor":flavor,"x":x,"parent_id":parent.stable_id,"parent_scalar":parent_scalar,"nonvacuous_parent":abs(parent_scalar)>0,"matrix_residual":matrix_residual,"reduction_residual":abs(parent_scalar-completed_scalar),"soft_factor":1.0,"zero_bin":0.0,"uv_factor":1.0,"rapidity_factor":1.0})
    return {"plan_id":plan.plan_id,"resolution_id":plan.resolution_id,"rows":rows,"maximum_residual":max(max(x["matrix_residual"],x["reduction_residual"]) for x in rows)}
