from dataclasses import FrozenInstanceError, is_dataclass, replace
from fractions import Fraction
import hashlib
import json
from pathlib import Path

import pytest

from deuteron_wigner.bridge.s0.core import (
    ARCHITECTURE_TYPES,
    C32_COLLINEAR_ROOT,
    C33_BASIS_REGULATOR_ID,
    C33_IR_REGULATOR_ID,
    C33_RAPIDITY_REGULATOR_ID,
    C33_SOFT_ROOT,
    C33_SOURCE_SOFT_SCHEME,
    C33_TARGET_SOFT_SCHEME,
    C33_UV_REGULATOR_ID,
    C33_WILSON_GEOMETRY,
    C33IdentityEnvelope,
    FAULT_CATALOG,
    INJECTION_GROUPS,
    NONZERO_UNKNOWN,
    REQUIRED_ONE_LOOP_CONTRIBUTIONS,
    BareSoftFactor,
    C33ClosureReport,
    C33ContinuationGate,
    CompatibilityStatus,
    ContributionStatus,
    EikonalColorSpace,
    EikonalDirection,
    FourLineSoftOperator,
    SoftAuxiliaryFieldOracle,
    SoftBasisResolution,
    SoftCollinearRegulatorPair,
    SoftContinuumOracle,
    SoftMomentumMode,
    SoftRapidityRegulator,
    SoftRegulatorRemainder,
    SoftRootId,
    SoftSectorPlan,
    SoftTensorNetworkPlan,
    VacuumHilbertId,
    VacuumSectorPlan,
    architecture_examples,
    content_hash,
    default_four_line_operator,
    default_soft_root,
    detect_injection,
    deterministic_json,
    fail_closed_one_loop_ledger,
    injection_rows,
)


EXPECTED_ARCHITECTURE_NAMES = {
    "SoftRootId", "VacuumHilbertId", "VacuumStateId", "VacuumSectorPlan",
    "SoftBasisId", "SoftBasisResolution", "SoftMomentumMode", "SoftGluonMode",
    "SoftZeroModePolicy", "SoftBoundaryCondition", "SoftContinuumTrajectory",
    "EikonalSourceId", "EikonalDirection", "EikonalColorSpace",
    "EikonalAuxiliaryField", "EikonalPathOperator", "FourLineSoftOperator",
    "SoftRapidityRegulator", "SoftUVRegulator", "SoftIRRegulator",
    "SoftMeasurement", "SoftFourierConvention", "BareSoftFactor",
    "SoftVirtualContribution", "SoftRealContribution",
    "SoftSelfEnergyContribution", "SoftCuspEndpointContribution",
    "SoftTransverseClosureContribution", "SoftInstantaneousContribution",
    "SoftZeroModeContribution", "SoftUVCounterterm",
    "SoftRapidityCounterterm", "RenormalizedSoftFactor",
    "SoftRapidityAnomalousDimension", "SoftCollinsSoperKernel",
    "SoftContinuumOracle", "SoftRegulatorMatching", "SoftRegulatorRemainder",
    "SoftBasisTrajectoryReport", "SoftCollinearRegulatorPair",
    "SoftCollinearCompatibilityMap", "SoftCollinearOverlapInterface",
    "ZeroBinCompatibilityGate", "SoftTensorNetworkPlan",
    "SoftAuxiliaryFieldOracle", "C33SoftCapabilityMatrix", "C33ClosureReport",
}

ROOT = Path(__file__).resolve().parents[1]
VOLUME_XXI_PATH = ROOT / "references" / "volume_xxi_regulator_specific_tmd_operators_soft_matching.tex"
VOLUME_XXI_SHA256 = "613d26bcd58b4c9d15b23ef955cbb04feb2edc7d854d4ed63339c50835fa72c4"


def test_volume_xxi_source_and_all_65_requirements_are_crosswalked_fail_closed():
    assert hashlib.sha256(VOLUME_XXI_PATH.read_bytes()).hexdigest() == VOLUME_XXI_SHA256
    extracted = []
    for line_number, raw_line in enumerate(VOLUME_XXI_PATH.read_text().splitlines(), 1):
        line = raw_line.strip()
        if not line.startswith("V21."):
            continue
        assert "&" in line and line.endswith(r"\\")
        requirement_id, requirement_tex = line.split("&", 1)
        extracted.append((requirement_id.strip(), requirement_tex.strip()[:-2].strip(), line_number))
    assert len(extracted) == len({row[0] for row in extracted}) == 65

    manifest_path = ROOT / "docs" / "next_level" / "c33_volume_xxi_requirement_crosswalk.json"
    manifest = json.loads(manifest_path.read_text())
    rows = manifest["rows"]
    assert manifest["source"]["sha256"] == VOLUME_XXI_SHA256
    assert manifest["source"]["classification"] == "PROJECT_NORMATIVE_FORMALISM"
    assert manifest["source"]["operator_regulator_identical_calculation"] is False
    assert manifest["source"]["supplies_finite_basis_one_loop_coefficients"] is False
    assert manifest["count"] == len(rows) == 65
    assert manifest["source"]["formal_acceptance_count"] == 53
    assert manifest["source"]["benchmark_families"] == [f"XXI-{chr(65 + i)}" for i in range(18)]
    assert manifest["source"]["minimum_ordered_negative_injections"] == 2040
    assert manifest["c33_ordered_negative_injections"] == 2040
    assert manifest["minimum_ordered_negative_injections_satisfied"] is True
    assert [(row["requirement_id"], row["requirement_tex"], row["source_line"]) for row in rows] == extracted
    assert manifest["counts_by_status"] == {
        "C33_CLOSED": 50, "C33_FAIL_CLOSED": 4, "C34_DEFERRED": 11,
    }
    for row in rows:
        assert row["status"] in {"C33_CLOSED", "C33_FAIL_CLOSED", "C34_DEFERRED"}
        assert row["evidence_paths"] and row["all_evidence_present"]
        assert all((ROOT / path).is_file() for path in row["evidence_paths"])
        assert row["positive_physics_promoted"] is False

    status = {row["requirement_id"]: row["status"] for row in rows}
    for requirement_id in ("V21.ORACLE.1", "V21.ORACLE.2", *(f"V21.MATCH.{i}" for i in range(1, 6))):
        assert status[requirement_id] == "C34_DEFERRED"
    assert status["V21.ROOT.3"] == "C34_DEFERRED"
    assert status["V21.COLL.1"] == "C33_CLOSED"
    assert status["V21.MATCH.6"] == status["V21.MATCH.7"] == "C33_CLOSED"
    assert manifest["c33_no_go"] == "C33_SOFT_TREE_LEVEL_ONLY"
    assert manifest["immediate_next_package"] == "C34/S0A"
    assert manifest["microscopic_proton_exported"] is False
    assert manifest["bridge_rerun"] is False
    assert manifest["inference_or_production_promoted"] is False


def test_all_47_architecture_records_are_frozen_and_instantiated():
    assert len(ARCHITECTURE_TYPES) == 47
    assert {item.__name__ for item in ARCHITECTURE_TYPES} == EXPECTED_ARCHITECTURE_NAMES
    assert all(is_dataclass(item) for item in ARCHITECTURE_TYPES)
    assert all(item.__dataclass_params__.frozen for item in ARCHITECTURE_TYPES)
    examples = architecture_examples()
    assert set(examples) == EXPECTED_ARCHITECTURE_NAMES
    assert all(isinstance(examples[item.__name__], item) for item in ARCHITECTURE_TYPES)


def test_all_47_serialized_records_carry_valid_common_identity_envelope():
    examples = architecture_examples()
    for name, value in examples.items():
        envelope = value.c33_identity_envelope
        payload = json.loads(deterministic_json(value))
        serialized = payload["c33_identity_envelope"]
        assert value.identity_validated
        assert envelope.object_type == name
        assert serialized["object_type"] == name
        assert serialized["object_identity"] == envelope.object_identity
        assert serialized["scope"] == "C33/S0"
        assert serialized["soft_root_id"] == C33_SOFT_ROOT
        assert serialized["baryon_number"] == 0
        assert serialized["wilson_geometry"] == C33_WILSON_GEOMETRY
        assert serialized["color_representation"] == "FUNDAMENTAL"
        assert serialized["color_trace"] == "SINGLET_1_OVER_NC"
        assert serialized["rapidity_regulator_id"] == C33_RAPIDITY_REGULATOR_ID
        assert serialized["uv_regulator_id"] == C33_UV_REGULATOR_ID
        assert serialized["ir_regulator_id"] == C33_IR_REGULATOR_ID
        assert serialized["basis_regulator_id"] == C33_BASIS_REGULATOR_ID
        expected_order = "C33/S0_DECLARED_TREE_PLUS_ONE_LOOP_TARGET"
        for attribute in ("order", "declared_order", "first_omitted_order"):
            candidate = getattr(value, attribute, None)
            if isinstance(candidate, str) and candidate:
                expected_order = candidate
                break
        assert serialized["perturbative_order"] == expected_order
        assert serialized["source_soft_scheme"] == C33_SOURCE_SOFT_SCHEME
        assert serialized["target_soft_scheme"] == C33_TARGET_SOFT_SCHEME
        assert serialized["state_independent"] is True
        assert serialized["consumes_art25"] is False
        assert serialized["consumes_process_data"] is False
        assert serialized["consumes_bridge_residuals"] is False
        assert serialized["inference_reachable"] is False
        assert serialized["production_reachable"] is False


@pytest.mark.parametrize("forbidden_flag", (
    "consumes_art25",
    "consumes_process_data",
    "consumes_bridge_residuals",
    "inference_reachable",
    "production_reachable",
))
def test_identity_envelope_forbidden_inputs_and_reachability_are_hard_false(forbidden_flag):
    envelope = default_soft_root().c33_identity_envelope
    assert isinstance(envelope, C33IdentityEnvelope)
    with pytest.raises(ValueError, match="FORBIDDEN_REACHABILITY"):
        replace(envelope, **{forbidden_flag: True})
    with pytest.raises(FrozenInstanceError):
        setattr(envelope, forbidden_flag, True)


def test_two_root_identity_is_b0_and_never_aliases_proton_state():
    root = default_soft_root()
    pair = architecture_examples()["SoftCollinearRegulatorPair"]
    assert root.root_id == C33_SOFT_ROOT
    assert root.collinear_root_id == C32_COLLINEAR_ROOT
    assert root.baryon_number == 0
    assert not root.shares_state_vector
    assert not root.shares_probability_normalization
    assert pair.collinear_root_id == C32_COLLINEAR_ROOT
    assert pair.soft_root_id == C33_SOFT_ROOT
    assert not pair.shared_state_vector
    assert not pair.shared_probability_normalization


def test_b1_vacuum_root_and_proton_contamination_fail_closed():
    with pytest.raises(ValueError, match="BARYON_NUMBER_ZERO"):
        SoftRootId(C33_SOFT_ROOT, "bad", baryon_number=1)
    root = default_soft_root()
    with pytest.raises(ValueError, match="VACUUM_SOFT_STATE_IN_PROTON"):
        VacuumHilbertId("bad", root, contains_proton_state=True)
    with pytest.raises(ValueError, match="STATE_ALIAS"):
        SoftCollinearRegulatorPair("bad", C32_COLLINEAR_ROOT,
                                   C33_SOFT_ROOT, True, False)


def test_records_are_actually_immutable():
    root = default_soft_root()
    with pytest.raises(FrozenInstanceError):
        root.root_id = "MUTATED"


def test_basis_has_three_nested_resolutions_and_both_rapidity_regions_are_typed():
    examples = architecture_examples()
    trajectory = examples["SoftContinuumTrajectory"]
    zero_policy = examples["SoftZeroModePolicy"]
    assert len(trajectory.resolutions) == 3
    assert tuple(r.nesting_rank for r in trajectory.resolutions) == (1, 2, 3)
    n_mode = examples["SoftMomentumMode"]
    nbar_mode = SoftMomentumMode("nbar", .2, .3, (-.1, .1), "nbar", 2, 2,
                                 n_mode.boundary_condition_id, False)
    assert {n_mode.rapidity_region, nbar_mode.rapidity_region} == {"n", "nbar"}
    assert not zero_policy.zero_modes_retained
    assert zero_policy.treatment == "EXCLUDE_PRIMARY_RETAIN_SEPARATE_CONTROL"
    assert zero_policy.proof_status == "AUDIT_REQUIRED"
    with pytest.raises(ValueError, match="THREE_SOFT_RESOLUTIONS"):
        type(trajectory)("bad", trajectory.resolutions[:2],
                         trajectory.analytic_fit_structures, trajectory.status)


def test_invalid_basis_support_and_undeclared_zero_mode_are_rejected():
    with pytest.raises(ValueError, match="INVALID_SOFT_ENERGY_SUPPORT"):
        SoftBasisResolution("bad", "basis", 1, 2, 2, 2, 1.0, .5, 1.0, 1.0, .1)
    with pytest.raises(ValueError, match="UNDECLARED_SOFT_ZERO_MODE"):
        SoftMomentumMode("bad", 0.0, 0.0, (0.0, 0.0), "n", 0, 0, "bc", False)


def test_four_line_operator_has_exact_color_path_and_tree_identities():
    operator = default_four_line_operator()
    assert isinstance(operator, FourLineSoftOperator)
    assert len(operator.paths) == 4
    assert tuple(path.path_id for path in operator.paths) == operator.trace_order
    assert [path.source.direction for path in operator.paths].count("n") == 2
    assert [path.source.direction for path in operator.paths].count("nbar") == 2
    assert sum(path.source.conjugate for path in operator.paths) == 2
    assert all(path.transverse_closure_id for path in operator.paths)
    assert operator.transverse_closure_complete
    assert operator.color_space.c_f == Fraction(4, 3)
    assert operator.tree_level_soft_factor == Fraction(1, 1)


def test_incomplete_four_line_operator_and_bad_trace_fail_closed():
    operator = default_four_line_operator()
    with pytest.raises(ValueError, match="FOUR_LINE_OPERATOR_NOT_REALIZABLE"):
        FourLineSoftOperator("bad", operator.paths[:3], operator.color_space,
                             tuple(p.path_id for p in operator.paths[:3]), True)
    with pytest.raises(ValueError, match="TRACE_NORMALIZATION"):
        EikonalColorSpace("bad", singlet_trace_numerator=1,
                          singlet_trace_denominator=2)


def test_modified_delta_denominator_signs_are_derived_and_conjugate():
    regulator = SoftRapidityRegulator(
        "delta", "MODIFIED_DELTA", 1e-4, 2e-4, -1, 1,
        ("COMBINE_REAL_VIRTUAL", "REMOVE_DELTA"),
    )
    n = EikonalDirection("n", "n", (1, 0, 0, 1), "k_minus", "delta_minus")
    direct = regulator.derive_denominator(n, "FUTURE", False, 1)
    conjugate = regulator.derive_denominator(n, "FUTURE", True, 1)
    past = regulator.derive_denominator(n, "PAST", False, 1)
    assert direct.momentum_component == "k_minus"
    assert direct.delta_component == "delta_minus"
    assert direct.delta_sign == direct.i0_sign
    assert conjugate.i0_sign == -direct.i0_sign
    assert past.i0_sign == -direct.i0_sign
    assert direct.derivation == (
        "WILSON_ORIENTATION", "FOURIER_CONVENTION", "MOMENTUM_FLOW",
        "COVARIANT_DERIVATIVE", "LINE_CONJUGATION", "MODIFIED_DELTA",
    )


def test_basis_cutoff_cannot_be_relabelled_as_rapidity_regulator():
    with pytest.raises(ValueError, match="FINITE_BASIS_IS_NOT_RAPIDITY_REGULATOR"):
        SoftRapidityRegulator("bad", "MODIFIED_DELTA", 1e-3, 1e-3, 1, 1,
                              ("REMOVE",), basis_is_rapidity_regulator=True)


def test_tree_soft_factor_is_exactly_one_and_one_loop_remains_unknown():
    bare = architecture_examples()["BareSoftFactor"]
    assert isinstance(bare, BareSoftFactor)
    assert bare.tree_value == Fraction(1, 1)
    assert not bare.one_loop_calculated
    assert bare.one_loop_expression == NONZERO_UNKNOWN
    with pytest.raises(ValueError, match="TREE_SOFT_FACTOR_NOT_ONE"):
        BareSoftFactor("bad", "operator", "tree", Fraction(2, 1),
                       ContributionStatus.STRUCTURALLY_UNRESOLVED,
                       NONZERO_UNKNOWN, ())


def test_full_required_one_loop_ledger_is_explicit_and_fail_closed():
    ledger = fail_closed_one_loop_ledger()
    assert len(REQUIRED_ONE_LOOP_CONTRIBUTIONS) == 18
    assert len(ledger) == 18
    assert {row.contribution_class for row in ledger} == set(REQUIRED_ONE_LOOP_CONTRIBUTIONS)
    assert all(row.status is ContributionStatus.STRUCTURALLY_UNRESOLVED for row in ledger)
    assert all(row.expression == NONZERO_UNKNOWN and row.blocking for row in ledger)


def test_one_loop_renormalization_matching_and_continuation_gates_fail_closed():
    examples = architecture_examples()
    assert not examples["SoftUVCounterterm"].validated
    assert not examples["SoftRapidityCounterterm"].validated
    assert not examples["RenormalizedSoftFactor"].validated
    assert not examples["SoftRapidityAnomalousDimension"].validated
    assert not examples["SoftCollinsSoperKernel"].validated
    assert not examples["SoftRegulatorMatching"].validated
    assert examples["SoftCollinearCompatibilityMap"].status is CompatibilityStatus.UNRESOLVED
    assert not examples["SoftCollinearCompatibilityMap"].validated
    assert not examples["ZeroBinCompatibilityGate"].passes
    gate = C33ContinuationGate(
        "C33.CONTINUATION", True, True, True, False, False, False,
        False, True, False, False, False, False)
    assert not gate.passes


def test_premature_continuation_export_and_bridge_are_rejected():
    with pytest.raises(ValueError, match="CONTINUATION_GATE_PREMATURE"):
        C33ClosureReport("bad", True, False, False, False, False, False,
                         True, "")
    with pytest.raises(ValueError, match="MICROSCOPIC_PROTON_TMD_EXPORTED"):
        C33ClosureReport("bad", True, False, False, False, False, False,
                         False, "C33_SOFT_TREE_LEVEL_ONLY",
                         microscopic_proton_exported=True)
    with pytest.raises(ValueError, match="BRIDGE_RERUN_FORBIDDEN"):
        C33ClosureReport("bad", True, False, False, False, False, False,
                         False, "C33_SOFT_TREE_LEVEL_ONLY", bridge_rerun=True)


def test_continuum_and_auxiliary_oracles_cannot_be_promoted_or_added():
    with pytest.raises(ValueError, match="NOT_FINITE_BASIS_RESULT"):
        SoftContinuumOracle("bad", "scheme", ("source", "integral"),
                            ContributionStatus.SOURCE_ORACLE_ONLY,
                            finite_basis_result=True)
    with pytest.raises(ValueError, match="NOT_ADDITIVE"):
        SoftAuxiliaryFieldOracle("bad", "field",
                                 ContributionStatus.SOURCE_ORACLE_ONLY,
                                 False, False, additive_with_direct_result=True)


def test_forbidden_data_dependent_plan_and_tensor_ensemble_are_rejected():
    with pytest.raises(ValueError, match="FORBIDDEN_DATA_DEPENDENT_SOFT_PLAN"):
        VacuumSectorPlan("bad", SoftSectorPlan.DIRECT_FOCK, True,
                         consumes_art25=True)
    with pytest.raises(ValueError, match="NOT_ENSEMBLE"):
        SoftTensorNetworkPlan("bad", ("VACUUM",), True,
                              statistical_ensemble=True)


def test_unknown_remainder_cannot_be_silently_zeroed():
    with pytest.raises(ValueError, match="NONZERO_UNKNOWN"):
        SoftRegulatorRemainder("bad", "O(alpha_s)", ("ZERO_MODE",), "0")


def test_serialization_and_content_addressing_are_byte_deterministic():
    operator_a = default_four_line_operator()
    operator_b = default_four_line_operator()
    assert deterministic_json(operator_a) == deterministic_json(operator_b)
    assert content_hash(operator_a) == content_hash(operator_b)
    assert operator_a.content_hash == operator_b.content_hash
    assert deterministic_json({"b": 2, "a": 1}) == '{"a":1,"b":2}'
    for value in architecture_examples().values():
        assert deterministic_json(value) == deterministic_json(value)
        assert len(content_hash(value)) == 64


def test_all_2040_injections_are_ordered_unique_and_detected():
    rows = injection_rows()
    assert len(rows) == 2040
    assert len({row["injection_id"] for row in rows}) == 2040
    assert [row["ordered_index"] for row in rows] == list(range(1, 2041))
    assert len(INJECTION_GROUPS) == 12
    assert len(FAULT_CATALOG) == 92
    assert {row["group"] for row in rows} == set(INJECTION_GROUPS)
    assert all(detect_injection(row["injection_id"]) == row["expected_diagnostic"]
               for row in rows)


@pytest.mark.parametrize("identifier", (
    "C33.INJECT.BAD.0001",
    "C33.INJECT.ROOT_IDENTITY.0006",
    "C33.INJECT.ROOT_IDENTITY.9999",
    "C32.INJECT.ROOT_IDENTITY.0001",
))
def test_unknown_or_mismatched_injection_is_rejected(identifier):
    with pytest.raises(ValueError, match="UNKNOWN_C33_INJECTION"):
        detect_injection(identifier)
