"""C35/S0C regulator-completion and fail-closed soft-sector contracts.

The formal package surface is explicit.  The historical compatibility module
remains available as :mod:`deuteron_wigner.bridge.s0c.core`, but its names do
not shadow the typed architecture records introduced here.
"""

from . import core
from .basis import (
    PoleCellPartition,
    SingularCellSubtraction,
    SoftCell,
    SoftCellBoundary,
    SoftCellMeasure,
    SoftCellQuadrature,
    SoftCellShape,
    SoftModeCollection,
    SoftPartitionOfUnity,
    SoftRefinementMap,
)
from .conventions import (
    LightFrontConvention,
    NullVectorNormalization,
    RapidityRegulatorRescaling,
    RealCutMeasure,
    RealSoftCoordinateChart,
    SoftCoordinateChart,
    SoftJacobian,
    VirtualContourPlan,
    VirtualLoopMeasure,
    VirtualSoftCoordinateChart,
)
from .gauge import (
    CovariantKreinPlan,
    GaugeCompleteSoftPlan,
    GaugePlanSupersession,
    LightFrontPhysicalPlan,
    SoftAuxiliaryMode,
    SoftBRSTOrConstraintReport,
    SoftFreeAction,
    SoftFreeHamiltonian,
    SoftGaugeMode,
    SoftGhostMode,
    SoftInstantaneousKernel,
    SoftPolarizationMetric,
)
from .identity import (
    AvailabilityStatus,
    C28_SCIENTIFIC_ANCESTOR,
    C32_B1_ROOT,
    C32_OPERATOR_COMPLETION_COMMIT,
    C33_B0_ROOT,
    C34_DESCENDANT_ROOT,
    C34_STARTING_COMMIT,
    C35_BASELINE_COMMIT,
    C35_DESCENDANT_ROOT,
    C35_PROMPT_SHA256,
    C35IdentityEnvelope,
    ContributionStatus,
    EvidenceRef,
    GaugePlanKind,
    OutcomeBranch,
    ProofSet,
    VOLUME_XXI_SHA256,
    ValidationStatus,
    identity_for,
)
from .overlap import C35CapabilityMatrix, C35ClosureReport, SoftSideOverlapObject
from .renormalization import (
    SoftBareOneLoopResult,
    SoftCountertermSystem,
    SoftRenormalizedOneLoopResult,
)
from .sectors import SoftBoundarySector, SoftZeroModeSector
from .serialization import ContentAddressed, canonical_value, content_hash, deterministic_json
from .trajectory import SoftTrajectoryAxis, SoftTrajectoryFamily, SoftTrajectoryResult
from .wilson import (
    ExecutableBoundaryKernel,
    ExecutableCuspKernel,
    ExecutableEikonalVertex,
    ExecutableLinePairKernel,
    ExecutableSelfKernel,
    FiniteSegmentLimit,
    LongitudinalWilsonSegment,
    ModifiedDeltaDampingOperator,
    TransverseInfinitySegment,
    WilsonSegmentParameterization,
)


FORMAL_ARCHITECTURE_TYPES = (
    GaugeCompleteSoftPlan,
    CovariantKreinPlan,
    LightFrontPhysicalPlan,
    GaugePlanSupersession,
    LightFrontConvention,
    NullVectorNormalization,
    RapidityRegulatorRescaling,
    SoftCoordinateChart,
    RealSoftCoordinateChart,
    VirtualSoftCoordinateChart,
    SoftJacobian,
    SoftCell,
    SoftCellBoundary,
    SoftCellShape,
    SoftCellMeasure,
    SoftCellQuadrature,
    SoftPartitionOfUnity,
    SoftRefinementMap,
    SoftModeCollection,
    SoftGaugeMode,
    SoftPolarizationMetric,
    SoftGhostMode,
    SoftAuxiliaryMode,
    SoftInstantaneousKernel,
    SoftFreeAction,
    SoftFreeHamiltonian,
    RealCutMeasure,
    VirtualLoopMeasure,
    VirtualContourPlan,
    PoleCellPartition,
    SingularCellSubtraction,
    WilsonSegmentParameterization,
    LongitudinalWilsonSegment,
    TransverseInfinitySegment,
    ModifiedDeltaDampingOperator,
    FiniteSegmentLimit,
    ExecutableEikonalVertex,
    ExecutableLinePairKernel,
    ExecutableSelfKernel,
    ExecutableCuspKernel,
    ExecutableBoundaryKernel,
    SoftZeroModeSector,
    SoftBoundarySector,
    SoftBRSTOrConstraintReport,
    SoftBareOneLoopResult,
    SoftCountertermSystem,
    SoftRenormalizedOneLoopResult,
    SoftTrajectoryFamily,
    SoftTrajectoryAxis,
    SoftTrajectoryResult,
    SoftSideOverlapObject,
    C35CapabilityMatrix,
    C35ClosureReport,
)

# Compatibility spelling used by the independent C35 validator.  Unlike the
# historical ``core.ARCHITECTURE_TYPES`` string ledger, this is the actual
# ordered class registry.
ARCHITECTURE_TYPES = FORMAL_ARCHITECTURE_TYPES


def _unresolved_architecture_example(object_type):
    """Construct one valid fail-closed schema example for *object_type*.

    These examples contain no coefficient or fabricated zero.  They exercise
    the public constructors and therefore remain subject to every invariant of
    the corresponding formal record.
    """

    from dataclasses import fields

    name = object_type.__name__
    envelope = identity_for("C35.ARCH.EXAMPLE." + name, name)
    values = {}
    for field in fields(object_type):
        field_name = field.name
        annotation = str(field.type)
        if field_name == "identity":
            value = envelope
        elif field_name == "proof":
            value = ProofSet(required=("C35_EXAMPLE_UNRESOLVED",))
        elif field_name == "availability":
            value = AvailabilityStatus.UNRESOLVED_BLOCKING
        elif field_name == "validation":
            value = ValidationStatus.UNRESOLVED_BLOCKING
        elif field_name == "contribution_status":
            value = ContributionStatus.UNRESOLVED_BLOCKING
        elif field_name == "kind":
            value = GaugePlanKind.UNAVAILABLE
        elif field_name == "outcome_branch":
            value = OutcomeBranch.NO_COMPATIBLE_REGULATOR
        elif "tuple" in annotation:
            value = ()
        elif "bool" in annotation:
            value = False
        elif "int" in annotation:
            value = 0
        elif "float" in annotation:
            value = None if "None" in annotation else 0.0
        elif "None" in annotation:
            value = None
        elif "str" in annotation:
            value = "C35.ARCH.EXAMPLE." + field_name if field_name.endswith("_id") else ""
        else:  # pragma: no cover - all current fields are covered above
            raise TypeError(f"no example value rule for {name}.{field_name}: {annotation}")

        if field_name == "tolerance":
            value = 1.0e-12
        elif field_name == "delta_component":
            value = "delta+"
        elif field_name == "numerical_epsilon_role":
            value = "NONE"
        elif field_name == "relation_status":
            value = "SOFT_COLLINEAR_COMPATIBILITY_UNRESOLVED"
        elif field_name == "metric_entry":
            value = None
        values[field_name] = value

    if object_type is LightFrontConvention:
        envelope = identity_for(
            "C35.ARCH.EXAMPLE." + name,
            name,
            light_front_convention_id="C35.LF.CONVENTION.SQRT2.v1",
            evidence_ids=("C35.DERIVATION.LF.NORMALIZATION",),
        )
        values.update(
            identity=envelope,
            convention_id="C35.ARCH.EXAMPLE.LF",
            plus_definition="(v0+v3)/sqrt(2)",
            minus_definition="(v0-v3)/sqrt(2)",
            metric_signature="+---",
            n_components=(2.0**-0.5, 0.0, 0.0, 2.0**-0.5),
            nbar_components=(2.0**-0.5, 0.0, 0.0, -2.0**-0.5),
            n_dot_nbar=1.0,
            k_plus_projection="nbar.k",
            k_minus_projection="n.k",
            integration_measure="d4k/(2*pi)^4",
            validation=ValidationStatus.VALIDATED,
            proof=ProofSet(
                required=("EXACT_LIGHT_FRONT_ALGEBRA",),
                proved=("EXACT_LIGHT_FRONT_ALGEBRA",),
                evidence_ids=("C35.DERIVATION.LF.NORMALIZATION",),
            ),
        )
    elif object_type is SoftCellBoundary:
        values.update(
            coordinate_names=("u",),
            lower=("0",),
            upper=("1",),
            lower_closed=(True,),
            upper_closed=(False,),
            boundary_condition="UNRESOLVED_BOUNDARY",
        )
    elif object_type is GaugePlanSupersession:
        values.update(
            prior_plan_id="C34.PLANNED.COVARIANT",
            replacement_plan_id="S0C-UNAVAILABLE",
            reason="No regulator-identical gauge-complete authority is available.",
            selected_before_results=True,
            prior_results_inspected=False,
            effective_version="C35",
            evidence_ids=("C35.SOURCE.SUFFICIENCY.NO_GO",),
        )
    elif object_type is ExecutableLinePairKernel:
        values.update(line_pair=("UNRESOLVED-L1", "UNRESOLVED-L2"), vertex_ids=("UNRESOLVED-V1", "UNRESOLVED-V2"))
    elif object_type is C35ClosureReport:
        values.update(
            package_statuses=("C35_SOURCE_SUFFICIENCY_DECISION_COMPLETE",),
            blocking_requirements=("GAUGE_COMPLETE_REGULATOR",),
            missing_calculation_ids=("C36.O4.REPLACEMENT_REGULATOR",),
            exact_next_package="C36/O4",
            no_scope_leakage=True,
        )
    return object_type(**values)


def architecture_examples():
    """Return deterministic fail-closed examples for all 53 formal records."""

    return {
        object_type.__name__: _unresolved_architecture_example(object_type)
        for object_type in ARCHITECTURE_TYPES
    }


__all__ = [
    "ARCHITECTURE_TYPES",
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
    "C35CapabilityMatrix",
    "C35ClosureReport",
    "C35IdentityEnvelope",
    "ContentAddressed",
    "ContributionStatus",
    "CovariantKreinPlan",
    "EvidenceRef",
    "ExecutableBoundaryKernel",
    "ExecutableCuspKernel",
    "ExecutableEikonalVertex",
    "ExecutableLinePairKernel",
    "ExecutableSelfKernel",
    "FORMAL_ARCHITECTURE_TYPES",
    "FiniteSegmentLimit",
    "GaugeCompleteSoftPlan",
    "GaugePlanKind",
    "GaugePlanSupersession",
    "LightFrontConvention",
    "LightFrontPhysicalPlan",
    "LongitudinalWilsonSegment",
    "ModifiedDeltaDampingOperator",
    "NullVectorNormalization",
    "OutcomeBranch",
    "PoleCellPartition",
    "ProofSet",
    "RapidityRegulatorRescaling",
    "RealCutMeasure",
    "RealSoftCoordinateChart",
    "SingularCellSubtraction",
    "SoftAuxiliaryMode",
    "SoftBRSTOrConstraintReport",
    "SoftBareOneLoopResult",
    "SoftBoundarySector",
    "SoftCell",
    "SoftCellBoundary",
    "SoftCellMeasure",
    "SoftCellQuadrature",
    "SoftCellShape",
    "SoftCoordinateChart",
    "SoftCountertermSystem",
    "SoftFreeAction",
    "SoftFreeHamiltonian",
    "SoftGaugeMode",
    "SoftGhostMode",
    "SoftInstantaneousKernel",
    "SoftJacobian",
    "SoftModeCollection",
    "SoftPartitionOfUnity",
    "SoftPolarizationMetric",
    "SoftRefinementMap",
    "SoftRenormalizedOneLoopResult",
    "SoftSideOverlapObject",
    "SoftTrajectoryAxis",
    "SoftTrajectoryFamily",
    "SoftTrajectoryResult",
    "SoftZeroModeSector",
    "TransverseInfinitySegment",
    "VOLUME_XXI_SHA256",
    "ValidationStatus",
    "VirtualContourPlan",
    "VirtualLoopMeasure",
    "VirtualSoftCoordinateChart",
    "WilsonSegmentParameterization",
    "canonical_value",
    "content_hash",
    "core",
    "deterministic_json",
    "identity_for",
    "architecture_examples",
]
