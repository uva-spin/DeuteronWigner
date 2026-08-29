from dataclasses import FrozenInstanceError, is_dataclass, replace
from fractions import Fraction
import cmath
import hashlib
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys

import pytest

from deuteron_wigner.bridge.s0a.core import (
    ARCHITECTURE_TYPES,
    C32_COLLINEAR_ROOT,
    C33_SOFT_ROOT,
    C34_DESCENDANT_ROOT,
    C34_COUPLING_NORMALIZATION,
    C34_EIKONAL_VERTEX_COUPLING,
    C34_TARGET_SOFT_EXPANSION,
    C34_CONTINUUM_SOURCE_FILE_SHA256,
    C34_CONTINUUM_NLO_SOURCE_EXPRESSION,
    C34_CONTINUUM_NLO_SOURCE_EXPRESSION_SHA256,
    C34_CONTINUUM_NLO_LAURENT_EXPRESSION,
    C34_CONTINUUM_NLO_LAURENT_EXPRESSION_SHA256,
    C34_NEXT_PACKAGE,
    C34_NO_GO,
    C34_STARTING_COMMIT,
    ContributionStatus,
    C34IdentityEnvelope,
    DIRECT_BARE_CONTRIBUTIONS,
    DIRECT_BARE_COMPONENT_IDS,
    SEPARATE_CONTROL_CONTRIBUTIONS,
    SEPARATE_CONTROL_COMPONENT_IDS,
    ALTERNATIVE_ROUTE_CONTRIBUTIONS,
    ALTERNATIVE_ROUTE_COMPONENT_IDS,
    COUNTERTERM_DECISION_CONTRIBUTIONS,
    COUNTERTERM_DECISION_COMPONENT_IDS,
    DERIVED_COUNTERTERM_IDS,
    EIKONAL_NUMERICAL_CURRENT_PROVED,
    EIKONAL_NUMERICAL_CURRENT_REQUIREMENTS,
    FAULT_CATALOG,
    FOUR_LINE_IDS,
    INJECTION_GROUPS,
    NONZERO_UNKNOWN,
    REQUIRED_ONE_LOOP_CONTRIBUTIONS,
    SoftModeCellId,
    architecture_examples,
    content_hash,
    default_eikonal_vertices,
    detect_injection,
    deterministic_json,
    exact_c33_tree_boundary,
    execute_injection_payload,
    fail_closed_one_loop_ledger,
    injection_rows,
    normalized_transverse_cell_phase,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "next_level"
VOLUME_XXI = ROOT / "references" / "volume_xxi_regulator_specific_tmd_operators_soft_matching.tex"
VOLUME_XXI_SHA256 = "613d26bcd58b4c9d15b23ef955cbb04feb2edc7d854d4ed63339c50835fa72c4"

EXPECTED_ARCHITECTURE_NAMES = {
    "SoftOneLoopPlan", "SoftOneLoopOrder", "SoftModeCellId",
    "SoftModeQuadrature", "SoftModeCompletenessRecord", "EikonalCurrent",
    "EikonalEmissionVertex", "EikonalAbsorptionVertex", "EikonalPairKernel",
    "EikonalSelfKernel", "TransverseClosureKernel", "SoftVirtualAmplitude",
    "SoftRealAmplitude", "SoftCutLedger", "SoftRealVirtualAssembly",
    "SoftGaugeContribution", "SoftGhostContribution",
    "SoftInstantaneousContribution", "SoftZeroModeContribution",
    "SoftBoundaryContribution", "SoftBareCoefficient",
    "SoftBareCoefficientDecomposition", "SoftUVStructure",
    "SoftRapidityStructure", "SoftUVCountertermSolution",
    "SoftRapidityCountertermSolution", "SoftRenormalizedCoefficient",
    "SoftRapidityDerivative", "SoftCuspConsistency", "SoftCSKernelRecord",
    "SoftContinuumTargetRecord", "SoftFiniteRegulatorDifference",
    "SoftFiniteRegulatorKernel", "SoftRoundTripReport",
    "SoftResolutionSequence", "SoftTrajectoryFitPlan",
    "SoftTrajectoryHoldout", "SoftTrajectoryResult", "SoftSideZeroBinLimit",
    "SoftCollinearContinuationContract", "C34SoftCapabilityMatrix",
    "C34ClosureReport",
}


def load(name):
    return json.loads((DOCS / name).read_text())


def prompt_acceptance_descriptions():
    prompt = (DOCS / "c34_s0a_codex_prompt.md").read_text()
    section = prompt.split("# 30. Acceptance criteria", 1)[1].split(
        "A rigorous negative result is valid.", 1
    )[0]
    numbered = [
        (int(match.group(1)), match.group(2))
        for line in section.splitlines()
        if (match := re.fullmatch(r"(\d+)\. (.+)", line.strip()))
    ]
    assert [index for index, _ in numbered] == list(range(1, 54))
    return [description for _, description in numbered]


def test_c34_validator_passes_as_an_independent_package_check():
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(ROOT / "src")
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_c34.py")],
        cwd=ROOT, env=environment, check=True, text=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    assert result.stdout.strip() == "C34_VALIDATION_PASS"


def test_all_42_architecture_objects_are_frozen_and_instantiated():
    assert len(ARCHITECTURE_TYPES) == 42
    assert {item.__name__ for item in ARCHITECTURE_TYPES} == EXPECTED_ARCHITECTURE_NAMES
    assert all(is_dataclass(item) and item.__dataclass_params__.frozen for item in ARCHITECTURE_TYPES)
    examples = architecture_examples()
    assert set(examples) == EXPECTED_ARCHITECTURE_NAMES
    assert all(isinstance(examples[item.__name__], item) for item in ARCHITECTURE_TYPES)
    with pytest.raises(FrozenInstanceError):
        examples["SoftOneLoopPlan"].plan_id = "MUTATED"


def test_every_architecture_object_has_the_b0_isolated_identity_envelope():
    for name, value in architecture_examples().items():
        envelope = value.c34_identity_envelope
        assert isinstance(envelope, C34IdentityEnvelope)
        assert envelope.object_type == name
        assert envelope.starting_commit == C34_STARTING_COMMIT
        assert envelope.parent_soft_root_id == C33_SOFT_ROOT
        assert envelope.descendant_root_id == C34_DESCENDANT_ROOT
        assert envelope.collinear_root_id == C32_COLLINEAR_ROOT
        assert envelope.baryon_number == 0
        assert envelope.state_independence_required
        assert envelope.hadron_independence_required
        assert not envelope.state_independence_proved
        assert not envelope.hadron_independence_proved
        assert envelope.mode_cell_identity and envelope.quadrature_identity
        assert envelope.gauge_identity == (
            "COVARIANT_XI_G_PROBE_PLAN_{0,1,2}_GAUGE_COMPLETION_UNRESOLVED"
        )
        assert envelope.zero_mode_status
        assert not envelope.consumes_art25
        assert not envelope.consumes_process_data
        assert not envelope.consumes_bridge_residuals
        assert not envelope.inference_reachable and not envelope.production_reachable
        serialized = json.loads(deterministic_json(value))
        assert serialized["c34_identity_envelope"]["object_type"] == name


@pytest.mark.parametrize(
    "field",
    ("consumes_art25", "consumes_process_data", "consumes_bridge_residuals",
     "inference_reachable", "production_reachable"),
)
def test_envelope_forbidden_reachability_is_hard_false(field):
    envelope = architecture_examples()["SoftOneLoopPlan"].c34_identity_envelope
    with pytest.raises(ValueError, match="FORBIDDEN_DATA_OR_PRODUCTION_REACHABILITY"):
        replace(envelope, **{field: True})


def test_envelope_rejects_b1_and_wrong_root():
    envelope = architecture_examples()["SoftOneLoopPlan"].c34_identity_envelope
    with pytest.raises(ValueError, match="BARYON_NUMBER_ZERO"):
        replace(envelope, baryon_number=1)
    with pytest.raises(ValueError, match="PARENT_SOFT_ROOT_MISMATCH"):
        replace(envelope, parent_soft_root_id=C32_COLLINEAR_ROOT)


def test_exact_c33_tree_color_root_and_trace_boundary_is_unchanged():
    boundary = exact_c33_tree_boundary()
    assert boundary["tree_value"] == Fraction(1, 1)
    assert boundary["c_f"] == Fraction(4, 3)
    assert boundary["trace_order"] == FOUR_LINE_IDS
    assert boundary["soft_root_id"] == C33_SOFT_ROOT
    assert boundary["collinear_root_id"] == C32_COLLINEAR_ROOT
    assert boundary["baryon_number"] == 0
    assert boundary["roots_share_state_or_probability_normalization"] is False


def test_exact_c33_resolution_ids_dimensions_and_holdout_are_preserved():
    examples = architecture_examples()
    sequence = examples["SoftResolutionSequence"]
    assert sequence.resolution_ids == ("C33.RES.1", "C33.RES.2", "C33.RES.3")
    assert sequence.resolution_tuples == ((4, 6, 5), (8, 12, 10), (12, 18, 15))
    assert sequence.dimensions == (3841, 30721, 103681)
    assert sequence.c33_descriptor_nesting_declared
    assert sequence.nominal_support_extension_monotone
    assert not sequence.refinement_proofs.closed
    assert sequence.refinement_proofs.unproved == (
        "EXPLICIT_CELL_EDGES_AND_WEIGHTS",
        "NORMALIZED_MODE_FUNCTIONS",
        "EXACT_SUCCESSIVE_INJECTION_OR_REFINEMENT_MAPS",
        "DECLARED_COMMON_CONTINUUM_LIMIT",
    )
    assert not sequence.exact_cell_refinement_proved
    assert not sequence.common_continuum_limit_proved
    assert not sequence.all_executed
    holdout = examples["SoftTrajectoryHoldout"]
    assert holdout.value_identity == "C33.RES.3"
    assert holdout.frozen_before_simplification and not holdout.used_in_construction


def test_six_and_only_six_contribution_statuses_are_available():
    assert [item.value for item in ContributionStatus] == [
        "CALCULATED_NONZERO",
        "CALCULATED_ZERO_BY_EXACT_IDENTITY",
        "CANCELS_WITH_DECLARED_PARTNER",
        "TARGET_SCALELESS_BUT_FINITE_REGULATOR_NONZERO",
        "NOT_APPLICABLE_WITH_PROOF",
        "UNRESOLVED_BLOCKING",
    ]


def test_all_18_required_contributions_are_explicit_nonzero_unknown_blockers():
    ledger = fail_closed_one_loop_ledger()
    assert len(REQUIRED_ONE_LOOP_CONTRIBUTIONS) == len(ledger) == 18
    assert tuple(row.contribution_class for row in ledger) == REQUIRED_ONE_LOOP_CONTRIBUTIONS
    assert all(row.status is ContributionStatus.UNRESOLVED_BLOCKING for row in ledger)
    assert all(row.expression == NONZERO_UNKNOWN and row.blocking for row in ledger)
    assert all(not row.finite_regulator_evaluated for row in ledger)
    assert all(not row.continuum_scaleless_assumed for row in ledger)


def test_bare_alternative_control_and_counterterm_roles_are_disjoint():
    examples = architecture_examples()
    bare = examples["SoftBareCoefficient"]
    decomposition = examples["SoftBareCoefficientDecomposition"]
    assert len(DIRECT_BARE_CONTRIBUTIONS) == len(DIRECT_BARE_COMPONENT_IDS) == 13
    assert SEPARATE_CONTROL_CONTRIBUTIONS == ("ZERO_MODE",)
    assert ALTERNATIVE_ROUTE_CONTRIBUTIONS == ("AUXILIARY_FIELD_SELF_ENERGY",)
    assert COUNTERTERM_DECISION_CONTRIBUTIONS == (
        "RAPIDITY_COUNTERTERM", "UV_COUNTERTERM", "RESIDUAL_LINE_MASS_COUNTERTERM"
    )
    role_sets = [
        set(DIRECT_BARE_COMPONENT_IDS),
        set(SEPARATE_CONTROL_COMPONENT_IDS),
        set(ALTERNATIVE_ROUTE_COMPONENT_IDS),
        set(COUNTERTERM_DECISION_COMPONENT_IDS),
    ]
    assert all(not role_sets[i] & role_sets[j] for i in range(4) for j in range(i + 1, 4))
    assert len(set().union(*role_sets)) == 18
    assert bare.component_ids == DIRECT_BARE_COMPONENT_IDS
    assert bare.separate_control_ids == SEPARATE_CONTROL_COMPONENT_IDS
    assert bare.alternative_route_ids == ALTERNATIVE_ROUTE_COMPONENT_IDS
    assert bare.counterterm_decision_ids == COUNTERTERM_DECISION_COMPONENT_IDS
    assert bare.derived_counterterm_ids == DERIVED_COUNTERTERM_IDS
    assert not set(bare.component_ids) & set(bare.alternative_route_ids)
    assert not set(bare.component_ids) & set(bare.counterterm_decision_ids)
    assert not set(bare.component_ids) & set(bare.derived_counterterm_ids)
    assert decomposition.direct_bare_component_ids == bare.component_ids
    assert decomposition.derived_counterterm_ids == DERIVED_COUNTERTERM_IDS
    with pytest.raises(ValueError, match="DIRECT_COMPONENT_SET_MISMATCH"):
        replace(bare, component_ids=bare.component_ids + bare.alternative_route_ids)


def test_unresolved_contribution_cannot_be_silently_zero_or_nonblocking():
    row = fail_closed_one_loop_ledger()[0]
    with pytest.raises(ValueError, match="MUST_BE_NONZERO_UNKNOWN"):
        replace(row, expression="0")
    with pytest.raises(ValueError, match="BLOCKING_STATUS_INCONSISTENT"):
        replace(row, blocking=False)
    with pytest.raises(ValueError, match="SCALELESS_ANALOGY_FORBIDDEN"):
        replace(row, continuum_scaleless_assumed=True)


def test_exact_zero_status_requires_proof_and_declared_cancellation_requires_partner():
    row = fail_closed_one_loop_ledger()[0]
    with pytest.raises(ValueError, match="ZERO_TERM_REQUIRES_EXACT_IDENTITY_PROOF"):
        replace(
            row, status=ContributionStatus.CALCULATED_ZERO_BY_EXACT_IDENTITY,
            expression="0", blocking=False,
        )
    exact_zero = replace(
        row, status=ContributionStatus.CALCULATED_ZERO_BY_EXACT_IDENTITY,
        expression="0", proof="EXACT_WARD_IDENTITY", blocking=False,
    )
    assert exact_zero.resolved
    with pytest.raises(ValueError, match="CANCELLATION_REQUIRES_PARTNER"):
        replace(
            row, status=ContributionStatus.CANCELS_WITH_DECLARED_PARTNER,
            expression="PARTNER_CANCELLATION", proof="PAIR_IDENTITY", blocking=False,
        )


def _axis_average(interval, b_value):
    lower, upper = interval
    width = upper - lower
    if b_value == 0.0:
        return 1.0 + 0.0j
    midpoint = (lower + upper) / 2.0
    half_argument = width * b_value / 2.0
    return cmath.exp(1j * midpoint * b_value) * math.sin(half_argument) / half_argument


def test_validation_cell_phase_matches_independent_analytic_rectangle_limit():
    cell = architecture_examples()["SoftModeCellId"]
    assert cell.geometry_status == "VALIDATION_ONLY_NONPHYSICAL_CELL"
    assert not cell.primary_basis_cell
    assert not cell.physical_coefficient_eligible
    assert cell.source_identity == "C34_RUNTIME_SCHEMA_ORACLE_NOT_A_C33_MODE_CELL"
    assert normalized_transverse_cell_phase(cell, (0.0, 0.0)) == 1.0 + 0.0j
    b_value = (0.37, -0.29)
    expected = _axis_average(cell.kx_interval, b_value[0]) * _axis_average(
        cell.ky_interval, b_value[1]
    )
    assert normalized_transverse_cell_phase(cell, b_value) == pytest.approx(expected, abs=2e-15)
    assert normalized_transverse_cell_phase(cell, (1e-10, -2e-10)) == pytest.approx(1.0 + 0.0j, abs=2e-10)


def test_validation_cell_cannot_be_promoted_or_hide_exact_zero_mode():
    cell = architecture_examples()["SoftModeCellId"]
    with pytest.raises(ValueError, match="VALIDATION_CELL_CANNOT_ENTER_PHYSICAL"):
        replace(cell, physical_coefficient_eligible=True)
    with pytest.raises(ValueError, match="VALIDATION_CELL_CANNOT_BE_PRIMARY"):
        replace(cell, primary_basis_cell=True)
    with pytest.raises(ValueError, match="ZERO_MODE_SILENTLY_INCLUDED"):
        replace(cell, exact_zero_mode=True, primary_basis_cell=True)
    with pytest.raises(ValueError, match="TRANSVERSE_COORDINATE_INVALID"):
        normalized_transverse_cell_phase(cell, (float("nan"), 0.0))


def test_singular_cell_center_epsilon_and_fake_execution_are_rejected():
    quadrature = architecture_examples()["SoftModeQuadrature"]
    assert quadrature.cell_integration_required and not quadrature.cell_integration_executed
    assert quadrature.regular_cell_rule_frozen
    assert not quadrature.singular_formula_proved
    assert not quadrature.mode_measure_proved
    assert not quadrature.tolerances_frozen
    assert not quadrature.cell_center_only
    assert not quadrature.physical_numerical_epsilon
    assert quadrature.integrated_physical_cell_count == 0
    assert not quadrature.physical_coefficient_eligible
    with pytest.raises(ValueError, match="CELL_CENTER_SAMPLING_FORBIDDEN"):
        replace(quadrature, cell_center_only=True)
    with pytest.raises(ValueError, match="EPSILON_IS_NOT_PHYSICAL_SUPPORT"):
        replace(quadrature, physical_numerical_epsilon=True)
    with pytest.raises(ValueError, match="UNEXECUTED_QUADRATURE_MARKED_PHYSICALLY_ELIGIBLE"):
        replace(quadrature, integrated_physical_cell_count=1)
    with pytest.raises(ValueError, match="EXECUTED_WITH_UNPROVED_INPUTS"):
        replace(quadrature, cell_integration_executed=True)


def test_all_four_emission_absorption_lines_and_derived_signs_are_typed():
    emissions, absorptions = default_eikonal_vertices()
    assert tuple(row.line_id for row in emissions) == FOUR_LINE_IDS
    assert tuple(row.line_id for row in absorptions) == FOUR_LINE_IDS
    assert [row.representation_action for row in emissions] == [
        "ANTI_FUNDAMENTAL", "FUNDAMENTAL", "ANTI_FUNDAMENTAL", "FUNDAMENTAL"
    ]
    assert [row.path_ordering for row in emissions] == ["ANTI_P", "P", "ANTI_P", "P"]
    assert [row.transverse_position for row in emissions] == ["b", "b", "0", "0"]
    assert [row.delta_component for row in emissions] == [
        "delta_minus", "delta_plus", "delta_plus", "delta_minus"
    ]
    assert [row.i0_sign for row in emissions] == [1, -1, 1, -1]
    assert all(len(row.sign_derivation) == 6 for row in emissions)
    assert all(row.perturbative_order == "O(g_s)" for row in emissions)
    assert all(row.coupling_symbol == C34_EIKONAL_VERTEX_COUPLING for row in emissions)
    assert all(
        row.phase_scope == "TRANSVERSE_BASEPOINT_ONLY_COMPLETE_SEGMENT_UNPROVED"
        for row in emissions
    )
    assert all(not row.numerical_vertex_proved for row in emissions)
    assert all(
        row.numerical_current_proofs.unproved == (
            "LIGHT_FRONT_TANGENT_NORMALIZATION",
            "EMISSION_ABSORPTION_NUMERATOR_SIGN",
            "CONJUGATE_GENERATOR_ACTION",
            "COMPLETE_PARAMETERIZED_SEGMENT_PHASE",
            "FINITE_BASIS_GAUGE_FIELD_MODE_NORMALIZATION",
            "FINITE_BASIS_INTERACTION_COUPLING_MAP",
        )
        for row in emissions
    )
    assert all(row.exact_hermitian_conjugate and row.conjugates_phase_i0_and_color for row in absorptions)
    assert all(not row.emission_numerical_vertex_proved for row in absorptions)
    assert all(not row.numerical_absorption_vertex_proved for row in absorptions)


def test_symbolic_current_has_contract_but_no_executed_cell_matrix_elements():
    current = architecture_examples()["EikonalCurrent"]
    manifest = load("c34_eikonal_current_manifest.json")
    assert current.line_ids == FOUR_LINE_IDS
    assert len(current.emission_vertex_ids) == 4
    assert "SUM_ell=1..4" in current.symbolic_expression
    assert current.perturbative_order == "O(g_s)"
    assert current.coupling_normalization == C34_EIKONAL_VERTEX_COUPLING
    assert current.four_line_skeleton_proved
    assert current.transverse_phase_scope == "TRANSVERSE_BASEPOINT_ONLY_COMPLETE_SEGMENT_UNPROVED"
    assert not current.complete_current_proved
    assert "EMISSION_ABSORPTION_NUMERATOR_SIGN" in current.numerical_current_proofs.unproved
    assert "LIGHT_FRONT_TANGENT_NORMALIZATION" in current.numerical_current_proofs.unproved
    assert current.current_status is ContributionStatus.UNRESOLVED_BLOCKING
    assert current.cell_integration_contract_present
    assert not current.cell_matrix_elements_executed
    assert not current.singular_denominator_integrated
    assert current.ward_contraction_status is ContributionStatus.UNRESOLVED_BLOCKING
    assert manifest["coupling_symbol"] == "g_s"
    assert manifest["perturbative_order"] == "O(g_s)"
    assert manifest["expression"].startswith("g_s ")
    proofs = manifest["numerical_current_proofs"]
    assert proofs["required"] == list(EIKONAL_NUMERICAL_CURRENT_REQUIREMENTS)
    assert proofs["proved"] == list(EIKONAL_NUMERICAL_CURRENT_PROVED)
    assert proofs["unproved"] == [
        item for item in EIKONAL_NUMERICAL_CURRENT_REQUIREMENTS
        if item not in EIKONAL_NUMERICAL_CURRENT_PROVED
    ]
    assert manifest["blocking_current_definitions"] == proofs["unproved"]
    assert not proofs["closed"]
    assert all(row["current_order"] == "O(g_s)" for row in manifest["lines"])
    assert all(row["operator_expression"].startswith("g_s*") for row in manifest["lines"])


def test_vertex_and_loop_coupling_conventions_and_orders_are_not_aliased():
    examples = architecture_examples()
    order = examples["SoftOneLoopOrder"]
    bare = examples["SoftBareCoefficient"]
    assert C34_COUPLING_NORMALIZATION == "a_s=g_s^2/(4*pi)^2=alpha_s/(4*pi)"
    assert C34_EIKONAL_VERTEX_COUPLING == "g_s"
    assert order.coupling_order == "O(g_s^2)"
    assert order.perturbative_order == "O(a_s)"
    assert order.target_coefficient_convention == C34_TARGET_SOFT_EXPANSION
    assert order.target_convention_proved
    assert not order.finite_basis_interaction_normalization_proved
    assert order.first_omitted_order == "O(a_s^2)"
    assert bare.coupling_normalization == C34_COUPLING_NORMALIZATION
    assert bare.color_factor_placement == "EXTERNAL_TO_REDUCED_S^[1]"
    assert not bare.finite_basis_interaction_normalization_proved
    assert bare.first_omitted_order == "O(a_s^2)"
    assert examples["EikonalCurrent"].c34_identity_envelope.first_omitted_order == "O(g_s^2)"
    assert order.c34_identity_envelope.first_omitted_order == "O(a_s^2)"


def test_unresolved_renormalization_and_conversion_require_universality_without_claiming_it():
    examples = architecture_examples()
    uv = examples["SoftUVCountertermSolution"]
    rapidity = examples["SoftRapidityCountertermSolution"]
    conversion = examples["SoftFiniteRegulatorKernel"]
    uv_structure = examples["SoftUVStructure"]
    assert uv.power_counterterm_slots_separate
    assert not uv.power_log_separation_proved
    assert uv.state_independence_required and not uv.state_independence_proved
    assert rapidity.state_independence_required and not rapidity.state_independence_proved
    assert conversion.state_independence_required and not conversion.state_independence_proved
    assert conversion.hadron_independence_required and not conversion.hadron_independence_proved
    assert conversion.flavor_independence_required_where_applicable
    assert not conversion.flavor_independence_proved
    assert conversion.gauge_independence_required and not conversion.gauge_independence_proved
    assert conversion.resolution_dependence_required and not conversion.resolution_dependence_explicit
    assert conversion.art25_member_independence_required
    assert conversion.art25_member_independence_proved
    conversion_manifest = load("c34_soft_regulator_conversion.json")
    assert conversion_manifest["state_independence_required"]
    assert not conversion_manifest["state_independence_proved"]
    assert conversion_manifest["hadron_independence_required"]
    assert not conversion_manifest["hadron_independence_proved"]
    assert conversion_manifest["art25_member_independence_required"]
    assert conversion_manifest["art25_member_independence_proved"]
    assert conversion_manifest["art25_member_independence_proof"] == (
        "HARD_NO_ART25_DEPENDENCY_IN_C34_CONSTRUCTION_GRAPH"
    )
    assert not conversion_manifest["art25_input_consumed"]
    assert uv_structure.schema_fields_separate
    assert not uv_structure.numerical_decomposition_completed
    with pytest.raises(ValueError, match="UV_COUNTERTERM_UNIVERSALITY_OVERSTATED"):
        replace(uv, state_independence_proved=True)
    with pytest.raises(ValueError, match="POWER_LOG_PROOF_OVERSTATED"):
        replace(uv, power_log_separation_proved=True)
    with pytest.raises(ValueError, match="RAPIDITY_COUNTERTERM_UNIVERSALITY_OVERSTATED"):
        replace(rapidity, state_independence_proved=True)
    with pytest.raises(ValueError, match="SOFT_CONVERSION_UNIVERSALITY_OVERSTATED"):
        replace(conversion, state_independence_proved=True)
    with pytest.raises(ValueError, match="UV_STRUCTURE_MARKED_NUMERICALLY_DECOMPOSED"):
        replace(uv_structure, numerical_decomposition_completed=True)


def test_every_runtime_readiness_gate_remains_fail_closed_on_branch_g():
    examples = architecture_examples()
    assert not examples["SoftBareCoefficient"].one_loop_validated
    assert not examples["SoftRenormalizedCoefficient"].validated
    assert not examples["SoftTrajectoryResult"].supports_continuum_claim
    assert examples["SoftCollinearContinuationContract"].status.value == "SOFT_COLLINEAR_COMPATIBILITY_UNRESOLVED"
    closure = examples["C34ClosureReport"]
    assert closure.symbolic_eikonal_current_skeleton_typed
    assert not closure.complete_eikonal_current_closed
    assert closure.no_go_status == C34_NO_GO
    assert closure.exact_next_package == C34_NEXT_PACKAGE
    assert not closure.continuation_ready
    with pytest.raises(ValueError, match="CONTINUATION_GATE_PREMATURE"):
        replace(closure, continuation_ready=True)


def test_continuum_source_formula_file_and_expression_hashes_are_exact_but_oracle_is_open():
    record = architecture_examples()["SoftContinuumTargetRecord"]
    source_pdf = ROOT / "data" / "raw" / "c31_sources" / "1511.05590.pdf"
    assert hashlib.sha256(source_pdf.read_bytes()).hexdigest() == C34_CONTINUUM_SOURCE_FILE_SHA256
    assert record.source_file_sha256 == C34_CONTINUUM_SOURCE_FILE_SHA256
    assert record.source_expression == C34_CONTINUUM_NLO_SOURCE_EXPRESSION
    assert record.source_expression_hash == C34_CONTINUUM_NLO_SOURCE_EXPRESSION_SHA256
    assert hashlib.sha256(record.source_expression.encode("ascii")).hexdigest() == (
        "aed120b66df5ed8eb2eb448997ab2360c3cf94a5933a0bc16728c2b0350343c6"
    )
    assert record.source_laurent_expression == C34_CONTINUUM_NLO_LAURENT_EXPRESSION
    assert record.source_laurent_expression_hash == C34_CONTINUUM_NLO_LAURENT_EXPRESSION_SHA256
    assert hashlib.sha256(record.source_laurent_expression.encode("ascii")).hexdigest() == (
        "025d792beed9bb1f585d9f3019ba3c8c9c299fc65ebb9476ffe7d5cd9990a9b8"
    )
    assert "L_mu=ln(mu^2*B*exp(2*gamma_E))" in record.source_laurent_expression
    assert record.source_locator == "ARXIV:1511.05590v2:Eqs.(2),(7),(8),(11)-(13)"
    assert record.source_transcription_proved
    assert "INDEPENDENT_DIRECT_INTEGRAL_RECONSTRUCTION" in record.oracle_proofs.unproved
    assert "CONVENTION_ALIGNMENT_CHECK" in record.oracle_proofs.unproved
    assert not record.independently_validated
    assert not record.convention_aligned and not record.finite_basis_result
    assert record.status is ContributionStatus.UNRESOLVED_BLOCKING
    with pytest.raises(ValueError, match="SOURCE_EXPRESSION_OR_HASH_MISMATCH"):
        replace(record, source_expression_hash="0" * 64)


def test_c34_has_exactly_52_json_and_four_public_markdown_deliverables():
    json_files = sorted(DOCS.glob("c34_*.json"))
    markdown_files = sorted(
        path for path in DOCS.glob("c34_*.md")
        if path.name != "c34_s0a_codex_prompt.md"
    )
    assert len(json_files) == 52
    assert [path.name for path in markdown_files] == [
        "c34_api.md", "c34_implementation_report.md",
        "c34_missing_calculation_specification.md",
        "c34_unresolved_physics_gaps.md",
    ]


def test_all_24_holdouts_are_frozen_and_never_used_in_construction():
    holdouts = load("c34_holdout_report.json")
    assert holdouts["count"] == len(holdouts["records"]) == 24
    assert holdouts["frozen_before_results"] and holdouts["moved"] == 0
    assert len({row["holdout_id"] for row in holdouts["records"]}) == 24
    assert all(row["frozen_before_symbolic_simplification"] for row in holdouts["records"])
    assert all(row["frozen_before_counterterm_solution"] for row in holdouts["records"])
    assert all(not row["used_in_construction"] and not row["used_in_fit"] for row in holdouts["records"])


def test_all_53_acceptance_rows_and_18_benchmark_families_are_covered():
    coverage = load("c34_requirement_coverage.json")
    assert coverage["acceptance_count"] == 53
    assert coverage["count"] == coverage["c34_requirement_record_count"] == len(coverage["rows"]) == 300
    assert coverage["inherited_c33_requirement_count"] == 2140
    assert coverage["count_semantics"] == "C34_ROWS_ONLY_INHERITED_C33_SUITE_REMAINS_SEPARATE"
    assert not coverage["cumulative_requirement_count_asserted"]
    assert coverage["benchmark_families"] == [f"S0A-{chr(65 + i)}" for i in range(18)]
    assert coverage["all_rows_described"] and coverage["all_rows_mapped_to_evidence"]
    assert coverage["all_acceptance_rows_have_concrete_evidence"]
    assert not coverage["all_acceptance_criteria_positively_satisfied"]
    assert not coverage["all_requirement_rows_positively_satisfied"]
    assert coverage["all_acceptance_rows_have_valid_branch_g_disposition"]
    assert coverage["positive_one_loop_claim_withheld_by_branch_g"]
    assert coverage["acceptance_disposition_counts"] == {
        "PASS": 35,
        "FAIL_CLOSED_GUARD_SATISFIED": 6,
        "NOT_CLAIMED_DUE_BRANCH_G": 12,
    }
    rows = coverage["rows"][:53]
    assert [row["requirement_id"] for row in rows] == [f"C34.ACC.{i:03d}" for i in range(1, 54)]
    assert all(row["kind"] == "ACCEPTANCE_CRITERION" for row in rows)
    assert [row["description"] for row in rows] == prompt_acceptance_descriptions()
    critical = {row["requirement_id"]: row for row in rows}
    assert critical["C34.ACC.005"]["description"] == "The one-loop plan is frozen before results."
    assert critical["C34.ACC.005"]["disposition"] == "NOT_CLAIMED_DUE_BRANCH_G"
    assert critical["C34.ACC.006"]["description"] == (
        "The quadrature/cell-integration plan is frozen before results."
    )
    assert critical["C34.ACC.006"]["disposition"] == "NOT_CLAIMED_DUE_BRANCH_G"
    assert critical["C34.ACC.045"]["description"] == (
        "Every no-go result contains an exact missing-calculation specification."
    )
    assert critical["C34.ACC.045"]["disposition"] == "PASS"
    assert critical["C34.ACC.046"]["description"] == (
        "All inherited tests, builders, requirements, injections, and manifests remain passing."
    )
    assert critical["C34.ACC.046"]["disposition"] == "PASS"
    assert critical["C34.ACC.051"]["description"] == (
        "All C34 manifests reproduce byte-for-byte."
    )
    assert critical["C34.ACC.051"]["disposition"] == "PASS"


def test_all_65_volume_xxi_rows_are_source_ordered_and_fail_closed():
    assert hashlib.sha256(VOLUME_XXI.read_bytes()).hexdigest() == VOLUME_XXI_SHA256
    source_ids = []
    for raw in VOLUME_XXI.read_text().splitlines():
        line = raw.strip()
        if line.startswith("V21."):
            source_ids.append(line.split("&", 1)[0].strip())
    crosswalk = load("c34_volume_xxi_requirement_crosswalk.json")
    assert crosswalk["count"] == len(source_ids) == len(set(source_ids)) == 65
    assert [row["requirement_id"] for row in crosswalk["rows"]] == source_ids
    assert crosswalk["counts_by_status"] == {
        "C34_CLOSED": 2, "C34_FAIL_CLOSED": 5,
        "INHERITED_CLOSED": 50, "LATER_PACKAGE_DEFERRED": 8,
    }
    assert not crosswalk["positive_one_loop_physics_promoted"]


def test_all_2240_injections_cover_exactly_80_stable_faults_and_detect():
    rows = injection_rows()
    manifest = load("c34_injection_manifest.json")
    assert len(rows) == 2240
    assert len(FAULT_CATALOG) == 80 and len(INJECTION_GROUPS) == 12
    assert len({row["injection_id"] for row in rows}) == 2240
    assert {row["fault"] for row in rows} == {fault for _, fault in FAULT_CATALOG}
    assert all(row["mutation_executed"] for row in rows)
    assert all(row["observed_diagnostic"] == row["expected_diagnostic"] for row in rows)
    assert all(
        content_hash(row["mutation_payload"]) == row["mutation_payload_sha256"]
        for row in rows
    )
    assert len({row["mutation_payload_sha256"] for row in rows}) == 2240
    assert all(
        execute_injection_payload(
            row["mutation_payload"], row["mutation_payload_sha256"]
        ) == row["expected_diagnostic"]
        for row in rows
    )
    assert all(detect_injection(row["injection_id"]) == row["expected_diagnostic"] for row in rows)
    assert manifest["semantic_control_mutation_execution_count"] == 2240
    assert manifest["semantic_control_failure_detection_count"] == 2240
    assert not manifest["identifier_only_dispatch_used_as_evidence"]
    assert all(row["semantic_mutation_execution_verified"] for row in manifest["rows"])
    tampered = dict(rows[0]["mutation_payload"])
    tampered["replacement"] = tampered["expected_before"]
    with pytest.raises(ValueError, match="PAYLOAD_HASH_MISMATCH"):
        execute_injection_payload(tampered, rows[0]["mutation_payload_sha256"])
    with pytest.raises(ValueError, match="MUTATION_IS_NO_OP"):
        execute_injection_payload(tampered)
    with pytest.raises(ValueError, match="MINIMUM_2240"):
        injection_rows(2239)


def test_branch_g_and_exact_c35_s0c_package_are_consistent_everywhere():
    decision = load("c34_source_sufficiency_decision.json")
    tree = load("c34_no_go_decision_tree.json")
    gate = load("c34_c32_continuation_gate.json")
    assert decision["primary_no_go"] == tree["selected"] == gate["no_go"] == C34_NO_GO
    assert decision["outcome_branch"] == tree["outcome_branch"] == gate["outcome_branch"] == "G"
    assert decision["next_package"] == tree["next_package"] == gate["next_package"] == "C35/S0C"
    assert decision["missing_calculations"]
    assert not gate["passes"] and not gate["ready_status_issued"]


def test_registry_art25_covariance_and_eight_artifacts_are_isolated():
    regression = load("c34_regression_report.json")
    assert regression["baseline_commit"] == C34_STARTING_COMMIT
    assert regression["immutable_c33_path_count"] == 74
    assert regression["all_immutable_c33_paths_byte_identical"]
    assert regression["authoritative_artifacts_unchanged"]
    assert len(regression["authoritative_artifacts"]) == 8
    assert all(row["byte_identical"] for row in regression["authoritative_artifacts"])
    assert regression["production_registry"] == 216
    assert regression["external_art25_members"] == 642
    assert regression["source_covariance"]["shape"] == [642, 11]
    assert regression["source_covariance"]["rank"] == 10
    assert regression["source_covariance"]["nullity"] == 1
    assert regression["cross_root_relation"] == "NO_JOINT_MEASURE"
    assert regression["failed_bridge_projection"] == {"shape": [642, 0], "empty_not_zero": True}
    assert regression["inherited_c33_requirements"] == 2140
    assert regression["c34_requirement_records"] == 300
    assert not regression["cumulative_requirement_count_asserted"]
    assert regression["inherited_c33_injections"] == 2040
    assert regression["c34_injection_instances"] == 2240
    assert regression["executed_c34_negative_injections"] == 2240
    for key in (
        "bridge_rerun", "microscopic_proton_export", "art25_consumed",
        "art25_data_consumed", "art25_chi2_consumed", "bridge_residual_consumed",
        "fit_created", "calibration_created", "likelihood_created",
        "posterior_created", "optimization_created", "reweighting_created",
        "emulator_created", "process_executed", "production_promoted",
    ):
        assert regression[key] is False


def test_runtime_and_manifest_serialization_is_deterministic():
    first = architecture_examples()
    second = architecture_examples()
    assert tuple(first) == tuple(second)
    for name in first:
        assert deterministic_json(first[name]) == deterministic_json(second[name])
        assert content_hash(first[name]) == content_hash(second[name])
        assert len(content_hash(first[name])) == 64
    for path in DOCS.glob("c34_*.json"):
        payload = json.loads(path.read_text())
        recorded = payload.pop("content_hash")
        encoded = json.dumps(
            payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True,
            allow_nan=False,
        ).encode()
        assert recorded == hashlib.sha256(encoded).hexdigest(), path.name


def test_c34_builder_reproduces_all_json_byte_for_byte():
    paths = sorted(DOCS.glob("c34_*.json"))
    assert len(paths) == 52
    before = {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
    test_count = load("c34_regression_report.json")["tests"]
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(ROOT / "src")
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "build_c34_manifests.py"), str(test_count)],
        cwd=ROOT, env=environment, check=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
    )
    after = {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
    assert after == before
