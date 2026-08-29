#!/usr/bin/env python3
"""Fail-closed validator for the C34/S0A Branch-G soft package."""

from __future__ import annotations

from dataclasses import is_dataclass
import hashlib
import json
import re
import subprocess
from pathlib import Path

from deuteron_wigner.bridge.s0a.core import (
    ARCHITECTURE_TYPES,
    C32_COLLINEAR_ROOT,
    C33_SOFT_ROOT,
    C34_DESCENDANT_ROOT,
    C34_CONTINUUM_NLO_LAURENT_EXPRESSION,
    C34_CONTINUUM_NLO_LAURENT_EXPRESSION_SHA256,
    C34_CONTINUUM_NLO_SOURCE_EXPRESSION,
    C34_CONTINUUM_NLO_SOURCE_EXPRESSION_SHA256,
    C34_CONTINUUM_SOURCE_LOCATOR,
    C34_NEXT_PACKAGE,
    C34_NO_GO,
    C34_SCOPE,
    C34_STARTING_COMMIT,
    ContributionStatus,
    ALTERNATIVE_ROUTE_COMPONENT_IDS,
    COUNTERTERM_DECISION_COMPONENT_IDS,
    DERIVED_COUNTERTERM_IDS,
    DIRECT_BARE_COMPONENT_IDS,
    EIKONAL_NUMERICAL_CURRENT_PROVED,
    EIKONAL_NUMERICAL_CURRENT_REQUIREMENTS,
    FAULT_CATALOG,
    FOUR_LINE_IDS,
    NONZERO_UNKNOWN,
    REQUIRED_ONE_LOOP_CONTRIBUTIONS,
    SEPARATE_CONTROL_COMPONENT_IDS,
    architecture_examples,
    content_hash,
    default_eikonal_vertices,
    detect_injection,
    deterministic_json,
    exact_c33_tree_boundary,
    execute_injection_payload,
    fail_closed_one_loop_ledger,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "next_level"
VOLUME_XXI = ROOT / "references" / "volume_xxi_regulator_specific_tmd_operators_soft_matching.tex"
VOLUME_XXI_SHA256 = "613d26bcd58b4c9d15b23ef955cbb04feb2edc7d854d4ed63339c50835fa72c4"
PROMPT_SHA256 = "a4a959d2d6401cbf296d6514591b3c5b4c3301a2b5867f0481b83a43d7c374eb"


JSON_DELIVERABLES = (
    "c34_auxiliary_soft_crosscheck.json",
    "c34_bare_soft_coefficient.json",
    "c34_bare_soft_decomposition.json",
    "c34_bare_soft_validation_report.json",
    "c34_c32_continuation_gate.json",
    "c34_continuum_soft_oracle_report.json",
    "c34_continuum_soft_target.json",
    "c34_count_once_report.json",
    "c34_cusp_consistency_report.json",
    "c34_derivation_authority_manifest.json",
    "c34_eikonal_current_manifest.json",
    "c34_endpoint_transverse_closure_report.json",
    "c34_holdout_report.json",
    "c34_injection_manifest.json",
    "c34_mode_cell_integration_report.json",
    "c34_mode_quadrature_plan.json",
    "c34_no_go_decision_tree.json",
    "c34_normative_source_integration.json",
    "c34_one_gluon_vertex_manifest.json",
    "c34_one_loop_dependency_closure.json",
    "c34_one_loop_plan.json",
    "c34_primary_source_manifest.json",
    "c34_rapidity_renormalization_closure.json",
    "c34_real_virtual_assembly.json",
    "c34_regression_report.json",
    "c34_requirement_coverage.json",
    "c34_soft_basis_trajectory.json",
    "c34_soft_collinear_continuation_contract.json",
    "c34_soft_continuum_extrapolation.json",
    "c34_soft_conversion_remainder.json",
    "c34_soft_counterterm_results.json",
    "c34_soft_cs_kernel_convention.json",
    "c34_soft_cut_ledger.json",
    "c34_soft_diagram_results.json",
    "c34_soft_quantum_interface_update.json",
    "c34_soft_rapidity_anomalous_dimension.json",
    "c34_soft_rapidity_counterterm_solution.json",
    "c34_soft_rapidity_structure.json",
    "c34_soft_regulator_conversion.json",
    "c34_soft_regulator_roundtrip.json",
    "c34_soft_remainder_separation.json",
    "c34_soft_side_zero_bin_limit.json",
    "c34_soft_tensor_network_execution.json",
    "c34_soft_trajectory_holdout_report.json",
    "c34_soft_uncertainty_budget.json",
    "c34_soft_uv_closure_report.json",
    "c34_soft_uv_counterterm_solution.json",
    "c34_soft_uv_structure.json",
    "c34_source_sufficiency_decision.json",
    "c34_trajectory_fit_plan.json",
    "c34_volume_xxi_requirement_crosswalk.json",
    "c34_zero_mode_contribution_report.json",
)

MARKDOWN_DELIVERABLES = (
    "c34_implementation_report.md",
    "c34_api.md",
    "c34_missing_calculation_specification.md",
    "c34_unresolved_physics_gaps.md",
)

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


def load(name: str):
    return json.loads((DOCS / name).read_text())


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def assert_content_address(name: str) -> None:
    payload = load(name)
    recorded = payload.pop("content_hash")
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True,
        allow_nan=False,
    ).encode("utf-8")
    assert recorded == hashlib.sha256(encoded).hexdigest(), name


def extract_volume_xxi_ids() -> list[str]:
    result = []
    for raw in VOLUME_XXI.read_text().splitlines():
        line = raw.strip()
        if line.startswith("V21."):
            assert "&" in line and line.endswith(r"\\")
            result.append(line.split("&", 1)[0].strip())
    return result


def extract_prompt_acceptance_descriptions() -> list[str]:
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


def main() -> None:
    assert len(JSON_DELIVERABLES) == 52
    assert len(MARKDOWN_DELIVERABLES) == 4
    assert all((DOCS / name).is_file() for name in JSON_DELIVERABLES)
    assert all((DOCS / name).is_file() for name in MARKDOWN_DELIVERABLES)
    assert (DOCS / "c34_s0a_codex_prompt.md").is_file()
    for name in JSON_DELIVERABLES:
        assert_content_address(name)

    assert file_hash(VOLUME_XXI) == VOLUME_XXI_SHA256
    assert file_hash(DOCS / "c34_s0a_codex_prompt.md") == PROMPT_SHA256
    norm = load("c34_normative_source_integration.json")
    assert norm["resolved_c33_baseline"] == C34_STARTING_COMMIT
    assert norm["c32_ancestor_verified"] and norm["c28_ancestor_verified"]
    assert norm["all_required_present"]
    assert norm["prompt"]["byte_identical"] and norm["volume_xxi"]["byte_identical"]
    assert norm["prompt"]["actual_sha256"] == PROMPT_SHA256
    assert norm["volume_xxi"]["actual_sha256"] == VOLUME_XXI_SHA256

    assert len(ARCHITECTURE_TYPES) == 42
    assert {item.__name__ for item in ARCHITECTURE_TYPES} == EXPECTED_ARCHITECTURE_NAMES
    assert all(is_dataclass(item) and item.__dataclass_params__.frozen for item in ARCHITECTURE_TYPES)
    examples = architecture_examples()
    assert set(examples) == EXPECTED_ARCHITECTURE_NAMES
    for name, value in examples.items():
        assert isinstance(value, next(item for item in ARCHITECTURE_TYPES if item.__name__ == name))
        serialized = json.loads(deterministic_json(value))
        envelope = serialized["c34_identity_envelope"]
        assert envelope["scope"] == C34_SCOPE
        assert envelope["starting_commit"] == C34_STARTING_COMMIT
        assert envelope["parent_soft_root_id"] == C33_SOFT_ROOT
        assert envelope["descendant_root_id"] == C34_DESCENDANT_ROOT
        assert envelope["collinear_root_id"] == C32_COLLINEAR_ROOT
        assert envelope["baryon_number"] == 0
        assert envelope["state_independence_required"]
        assert envelope["hadron_independence_required"]
        assert not envelope["state_independence_proved"]
        assert not envelope["hadron_independence_proved"]
        assert envelope["gauge_identity"] == (
            "COVARIANT_XI_G_PROBE_PLAN_{0,1,2}_GAUGE_COMPLETION_UNRESOLVED"
        )
        assert envelope["mode_cell_identity"] and envelope["quadrature_identity"]
        assert envelope["gauge_identity"] and envelope["zero_mode_status"]
        for key in (
            "consumes_art25", "consumes_process_data", "consumes_bridge_residuals",
            "inference_reachable", "production_reachable",
        ):
            assert envelope[key] is False

    tree = exact_c33_tree_boundary()
    assert tree["tree_value"] == 1 and str(tree["c_f"]) == "4/3"
    assert tree["soft_root_id"] == C33_SOFT_ROOT
    assert tree["collinear_root_id"] == C32_COLLINEAR_ROOT
    assert tree["trace_order"] == FOUR_LINE_IDS
    assert not tree["roots_share_state_or_probability_normalization"]

    allowed = {item.value for item in ContributionStatus}
    assert allowed == {
        "CALCULATED_NONZERO", "CALCULATED_ZERO_BY_EXACT_IDENTITY",
        "CANCELS_WITH_DECLARED_PARTNER",
        "TARGET_SCALELESS_BUT_FINITE_REGULATOR_NONZERO",
        "NOT_APPLICABLE_WITH_PROOF", "UNRESOLVED_BLOCKING",
    }
    ledger = fail_closed_one_loop_ledger()
    assert len(REQUIRED_ONE_LOOP_CONTRIBUTIONS) == len(ledger) == 18
    assert tuple(row.contribution_class for row in ledger) == REQUIRED_ONE_LOOP_CONTRIBUTIONS
    assert all(row.status is ContributionStatus.UNRESOLVED_BLOCKING for row in ledger)
    assert all(row.expression == NONZERO_UNKNOWN and row.blocking for row in ledger)
    assert all(not row.finite_regulator_evaluated and not row.continuum_scaleless_assumed for row in ledger)

    emissions, absorptions = default_eikonal_vertices()
    assert len(emissions) == len(absorptions) == 4
    assert tuple(row.line_id for row in emissions) == FOUR_LINE_IDS
    assert tuple(row.line_id for row in absorptions) == FOUR_LINE_IDS
    assert all(row.exact_hermitian_conjugate for row in absorptions)
    assert [row.delta_component for row in emissions] == [
        "delta_minus", "delta_plus", "delta_plus", "delta_minus"
    ]
    assert [row.i0_sign for row in emissions] == [1, -1, 1, -1]
    assert all(len(row.sign_derivation) == 6 for row in emissions)

    plan = load("c34_one_loop_plan.json")
    assert plan["baryon_number"] == 0 and not plan["shared_state"]
    assert plan["parent_root"] == C33_SOFT_ROOT and plan["collinear_root"] == C32_COLLINEAR_ROOT
    assert plan["selected_realization"] == "S0-FB-EIKONAL-FOCK"
    assert plan["selected_before_results"]
    assert plan["method_family_frozen_before_coefficients"]
    assert not plan["execution_plan_complete"]
    assert plan["wilson_trace_order"] == [
        "C33.LINE.N.DAGGER.B", "C33.LINE.NBAR.B",
        "C33.LINE.NBAR.DAGGER.0", "C33.LINE.N.0",
    ]
    assert [row["cell_tuple"] for row in plan["resolutions"]] == [[4, 6, 5], [8, 12, 10], [12, 18, 15]]
    assert [row["hilbert_dimension"] for row in plan["resolutions"]] == [3841, 30721, 103681]
    assert [row["resolution_id"] for row in plan["resolutions"]] == ["C33.RES.1", "C33.RES.2", "C33.RES.3"]
    sequence = examples["SoftResolutionSequence"]
    assert sequence.resolution_ids == ("C33.RES.1", "C33.RES.2", "C33.RES.3")
    assert sequence.resolution_tuples == ((4, 6, 5), (8, 12, 10), (12, 18, 15))
    assert sequence.dimensions == (3841, 30721, 103681)
    assert plan["zero_mode_policy"] == "EXCLUDE_PRIMARY_RETAIN_SEPARATE_CONTROL"
    assert plan["gauges_xi_g"] == [0.0, 1.0, 2.0]
    assert len(plan["holdout_ids"]) == 24

    quadrature = load("c34_mode_quadrature_plan.json")
    cell_report = load("c34_mode_cell_integration_report.json")
    runtime_cell = examples["SoftModeCellId"]
    runtime_quadrature = examples["SoftModeQuadrature"]
    runtime_current = examples["EikonalCurrent"]
    assert runtime_cell.geometry_status == "VALIDATION_ONLY_NONPHYSICAL_CELL"
    assert not runtime_cell.physical_coefficient_eligible and runtime_cell.source_identity
    assert runtime_cell.resolution_id == "C33.RES.1"
    assert runtime_quadrature.integrated_physical_cell_count == 0
    assert not runtime_quadrature.physical_coefficient_eligible
    assert runtime_current.cell_integration_contract_present
    assert not runtime_current.cell_matrix_elements_executed
    assert not runtime_current.singular_denominator_integrated
    assert quadrature["method_family_and_nominal_order_frozen_before_results"]
    assert not quadrature["fully_specified"]
    assert not quadrature["execution_plan_complete"]
    assert not quadrature["cell_center_substitution_allowed"]
    assert quadrature["physical_numerical_epsilon"] is None
    assert "UNRESOLVED_BLOCKING" in quadrature["singular_cell_treatment"]
    assert cell_report["integrated_cell_count"] == 0
    assert not cell_report["cell_center_sampling_used"] and not cell_report["physical_epsilon_used"]
    assert not cell_report["normalized_cell_functions_available"]
    assert not cell_report["singular_subtraction_kernel_available"]

    current = load("c34_eikonal_current_manifest.json")
    vertices = load("c34_one_gluon_vertex_manifest.json")
    assert current["line_count"] == 4 and current["all_stored_lines_present"]
    assert current["color_trace_tree"] == 1.0 and current["C_F"] == "4/3"
    assert current["ward_contraction"] is None and current["direct_matrix_action"] is None
    assert not current["current_identity_complete"]
    assert current["current_identity_scope"] == "PATH_COLOR_DENOMINATOR_STRUCTURE_ONLY"
    assert current["coupling_symbol"] == "g_s"
    assert current["perturbative_order"] == "O(g_s)"
    assert current["expression"].startswith("g_s ")
    current_proofs = current["numerical_current_proofs"]
    assert current_proofs["required"] == list(EIKONAL_NUMERICAL_CURRENT_REQUIREMENTS)
    assert current_proofs["proved"] == list(EIKONAL_NUMERICAL_CURRENT_PROVED)
    assert current_proofs["unproved"] == [
        item for item in EIKONAL_NUMERICAL_CURRENT_REQUIREMENTS
        if item not in EIKONAL_NUMERICAL_CURRENT_PROVED
    ]
    assert not current_proofs["closed"]
    assert current["blocking_current_definitions"] == current_proofs["unproved"]
    assert current["transverse_phase_scope"] == (
        "TRANSVERSE_BASEPOINT_ONLY_COMPLETE_SEGMENT_UNPROVED"
    )
    assert current["basepoint_only_phase_proved"]
    assert not current["complete_segment_phase_proved"]
    assert all(
        row["path_delta_and_i0_signs_derived_from_c33"]
        and not row["manual_path_delta_or_i0_sign_insertion"]
        for row in current["lines"]
    )
    assert all(row["current_order"] == "O(g_s)" for row in current["lines"])
    assert all(row["operator_expression"].startswith("g_s*") for row in current["lines"])
    assert all(not row["current_numerator_normalization_proved"] for row in current["lines"])
    assert all(row["sigma_l_definition"] is None for row in current["lines"])
    assert all(not row["complete_parameterized_segment_phase_proved"] for row in current["lines"])
    assert all(not row["conjugate_generator_action_proved"] for row in current["lines"])
    assert all(not row["finite_basis_gauge_field_mode_normalization_proved"] for row in current["lines"])
    assert all(not row["finite_basis_interaction_coupling_map_proved"] for row in current["lines"])
    assert vertices["count"] == 8 and not vertices["direct_auxiliary_added"]
    assert vertices["one_gluon_basis_dimensions"] == [3841, 30721, 103681]
    assert all(row["status"] == "UNRESOLVED_BLOCKING" and row["cell_matrix_elements"] is None for row in vertices["records"])

    diagrams = load("c34_soft_diagram_results.json")
    assert diagrams["allowed_statuses"] == [item.value for item in ContributionStatus]
    assert diagrams["count"] == 18 and diagrams["ledger_complete"]
    assert not diagrams["one_loop_ready"] and diagrams["assigned_zero"] == 0
    assert diagrams["continuum_scaleless_substitutions"] == 0
    assert [row["contribution_class"] for row in diagrams["records"]] == list(REQUIRED_ONE_LOOP_CONTRIBUTIONS)
    assert all(row["status"] == "UNRESOLVED_BLOCKING" for row in diagrams["records"])
    assert all(row["value"] is None and row["value_status"] == NONZERO_UNKNOWN for row in diagrams["records"])
    assert all(not row["assigned_zero"] and not row["target_scaleless_assumed"] for row in diagrams["records"])

    counterterms = load("c34_soft_counterterm_results.json")
    assert len(counterterms["records"]) == counterterms["unresolved_count"] == 9
    assert counterterms["derived_count"] == 0
    assert counterterms["counterterm_ids_disjoint_from_contribution_ids"]
    assert counterterms["state_independence_required_for_all"]
    assert counterterms["state_independence_proved_count"] == 0
    assert not counterterms["power_hidden_in_log"]
    assert all(row["state_independence_required"] for row in counterterms["records"])
    assert all(not row["state_independence_proved"] for row in counterterms["records"])
    assert [row["counterterm_id"] for row in counterterms["records"]] == list(DERIVED_COUNTERTERM_IDS)
    dependency = load("c34_one_loop_dependency_closure.json")
    assert dependency["acyclic"] and dependency["all_blockers_visible"] and not dependency["passes"]

    assembly = load("c34_real_virtual_assembly.json")
    cuts = load("c34_soft_cut_ledger.json")
    count_once = load("c34_count_once_report.json")
    assert assembly["candidate_id_sets_disjoint"]
    assert not assembly["branch_assignment_proved"] and not assembly["assembly_executed"]
    assert assembly["real_contribution_ids"] == [] and assembly["virtual_contribution_ids"] == []
    assert assembly["wilson_expansion_value"] is None
    assert assembly["mode_sum_value"] is None and assembly["direct_mode_sum_residual"] is None
    assert len(cuts["records"]) == cuts["count"] == 15
    assert len({row["cut_id"] for row in cuts["records"]}) == 15
    assert cuts["structural_cut_ids_unique"] and not cuts["duplicate_cut_ids"]
    assert cuts["conjugate_pair_double_counted"] is None
    assert cuts["physical_branch_assignment_count"] == 0
    assert cuts["primary_direct_assembly_count"] == 0
    assert all(not row["branch_assignment_proved"] for row in cuts["records"])
    assert all(not row["included_in_primary_direct_assembly"] for row in cuts["records"])
    assert count_once["candidate_real_virtual_id_sets_disjoint"]
    assert count_once["structural_cut_ids_unique"] and count_once["duplicate_cut_count"] == 0
    assert not count_once["physical_real_virtual_sets_available"]
    assert not count_once["physical_count_once_validated"]
    assert count_once["soft_factor_squared_accidentally"] is None
    assert count_once["missing_real_residual"] is None and count_once["missing_virtual_residual"] is None

    bare = load("c34_bare_soft_coefficient.json")
    decomposition = load("c34_bare_soft_decomposition.json")
    bare_validation = load("c34_bare_soft_validation_report.json")
    assert bare["tree_value_exact"] and bare["tree_value"] == 1.0
    assert bare["one_loop_coefficient"] is None and bare["one_loop_status"] == NONZERO_UNKNOWN
    assert not bare["continuum_coefficient_substituted"] and bare["status"] == C34_NO_GO
    soft_id_prefixes = lambda ids: [".".join(item.split(".")[:3]) for item in ids]
    assert decomposition["component_count"] == len(DIRECT_BARE_COMPONENT_IDS) == 13
    assert decomposition["included_component_ids"] == bare["direct_bare_component_ids"]
    assert soft_id_prefixes(bare["direct_bare_component_ids"]) == list(DIRECT_BARE_COMPONENT_IDS)
    assert soft_id_prefixes(bare["separate_control_ids"]) == list(SEPARATE_CONTROL_COMPONENT_IDS)
    assert soft_id_prefixes(bare["excluded_alternative_route_ids"]) == list(ALTERNATIVE_ROUTE_COMPONENT_IDS)
    assert soft_id_prefixes(bare["excluded_counterterm_decision_ids"]) == list(COUNTERTERM_DECISION_COMPONENT_IDS)
    assert bare["counterterm_ids"] == list(DERIVED_COUNTERTERM_IDS)
    role_sets = [
        set(bare["direct_bare_component_ids"]),
        set(bare["separate_control_ids"]),
        set(bare["excluded_alternative_route_ids"]),
        set(bare["excluded_counterterm_decision_ids"]),
        set(bare["counterterm_ids"]),
    ]
    assert all(not role_sets[i] & role_sets[j] for i in range(5) for j in range(i + 1, 5))
    assert decomposition["counterterms_are_separate_derived_objects"]
    assert not decomposition["assembly_executed"]
    assert decomposition["assigned_zero_count"] == 0
    assert decomposition["all_unknown_nonzero"] and not decomposition["merged"]
    assert not bare_validation["one_loop_validated"] and bare_validation["tree_residual"] == 0.0
    assert bare_validation["color_trace_residual"] == 0.0
    assert bare_validation["future_past_residual"] is None and bare_validation["gauge_residuals"] is None

    continuum = load("c34_continuum_soft_target.json")
    continuum_oracle = load("c34_continuum_soft_oracle_report.json")
    assert continuum["source_expression"]
    assert not continuum["graph_level_reconstruction"]
    assert continuum["graph_level_reconstruction_status"] == "NOT_PERFORMED_SOURCE_FINAL_RESULT_ONLY"
    assert not continuum["independent_direct_integral_reconstruction"]
    assert not continuum["finite_basis_identity"] and not continuum["used_as_finite_basis_result"]
    exact_formula = (
        continuum["source_formulae"]["exact_one_loop_eq11"]
        + ";" + continuum["source_formulae"]["B_definition_eq8"]
        + ";L_0=ln(B*abs(delta_plus*delta_minus)*exp(2*gamma_E))"
    ).replace("eps", "epsilon").replace("(L0-", "(L_0-")
    assert exact_formula == C34_CONTINUUM_NLO_SOURCE_EXPRESSION
    assert hashlib.sha256(exact_formula.encode("ascii")).hexdigest() == (
        C34_CONTINUUM_NLO_SOURCE_EXPRESSION_SHA256
    )
    laurent_formula = (
        continuum["source_formulae"]["expanded_one_loop_eq13"]
        + ";L_mu=ln(mu^2*B*exp(2*gamma_E))"
        + ";d^(1,1)=2*C_F"
        + ";l_delta=ln(mu^2/abs(delta_plus*delta_minus))"
    ).replace("eps", "epsilon")
    assert laurent_formula == C34_CONTINUUM_NLO_LAURENT_EXPRESSION
    assert hashlib.sha256(laurent_formula.encode("ascii")).hexdigest() == (
        C34_CONTINUUM_NLO_LAURENT_EXPRESSION_SHA256
    )
    assert C34_CONTINUUM_SOURCE_LOCATOR == "ARXIV:1511.05590v2:Eqs.(2),(7),(8),(11)-(13)"
    assert continuum_oracle["source_transcription_present"]
    assert not continuum_oracle["graph_level_line_pair_reconstruction_present"]
    assert not continuum_oracle["independent_integral_route_complete"]
    assert not continuum_oracle["oracle_validated"] and continuum_oracle["finite_basis_comparison_residual"] is None

    uv = load("c34_soft_uv_structure.json")
    uv_solution = load("c34_soft_uv_counterterm_solution.json")
    uv_closure = load("c34_soft_uv_closure_report.json")
    rapidity = load("c34_soft_rapidity_structure.json")
    rapidity_solution = load("c34_soft_rapidity_counterterm_solution.json")
    rapidity_closure = load("c34_rapidity_renormalization_closure.json")
    assert uv["representation_separates_power_and_log_slots"]
    assert not uv["numerical_power_log_decomposition_completed"]
    assert not uv["power_hidden_in_msbar"]
    assert uv_solution["state_independence_required"]
    assert not uv_solution["state_independence_proved"]
    assert uv_solution["solution"] is None
    assert not uv_closure["passes"] and uv_closure["gauge_residual"] is None
    assert rapidity["delta_plus_kept_distinct"] and rapidity["delta_minus_kept_distinct"]
    assert rapidity["independent_variation_schedule_frozen"]
    assert not rapidity["independent_variations_executed"]
    assert not rapidity["finite_basis_is_rapidity_regulator"]
    assert rapidity_solution["state_independence_required"]
    assert not rapidity_solution["state_independence_proved"]
    assert rapidity_solution["counterterm"] is None
    assert not rapidity_solution["fitted_nonperturbative_cs_term"]
    assert not rapidity_closure["passes"] and rapidity_closure["future_past_residual"] is None
    rad = load("c34_soft_rapidity_anomalous_dimension.json")
    cusp = load("c34_cusp_consistency_report.json")
    assert not rad["extracted_from_closed_calculation"] and not rad["fitted"]
    assert rad["finite_basis_value"] is None and rad["value_status"] == NONZERO_UNKNOWN
    assert not cusp["tested"] and not cusp["passes"] and cusp["residual"] is None

    conversion = load("c34_soft_regulator_conversion.json")
    roundtrip = load("c34_soft_regulator_roundtrip.json")
    trajectory = load("c34_soft_basis_trajectory.json")
    trajectory_plan = load("c34_trajectory_fit_plan.json")
    assert conversion["tree_kernel"] == 1.0 and conversion["one_loop_kernel"] is None
    assert conversion["state_independence_required"]
    assert not conversion["state_independence_proved"]
    assert conversion["hadron_independence_required"]
    assert not conversion["hadron_independence_proved"]
    assert not conversion["flavor_independence_proved"]
    assert conversion["art25_member_independence_required"]
    assert conversion["art25_member_independence_proved"]
    assert conversion["art25_member_independence_proof"] == (
        "HARD_NO_ART25_DEPENDENCY_IN_C34_CONSTRUCTION_GRAPH"
    )
    assert not conversion["art25_input_consumed"]
    assert not conversion["fit_performed"]
    assert roundtrip["tree_roundtrip_residual"] == 0.0 and roundtrip["one_loop_roundtrip_residual"] is None
    assert not roundtrip["validated"]
    assert trajectory["tree_values"] == [1.0, 1.0, 1.0]
    assert trajectory["one_loop_values"] == [None, None, None]
    assert not trajectory["all_three_executed_at_one_loop"] and not trajectory["continuum_claimed"]
    assert trajectory_plan["frozen_before_results"] and trajectory_plan["arbitrary_polynomial_forbidden"]
    assert not trajectory_plan["fit_performed"] and trajectory_plan["holdout_resolution"] == "C33.RES.3"

    zero = load("c34_zero_mode_contribution_report.json")
    endpoint = load("c34_endpoint_transverse_closure_report.json")
    auxiliary = load("c34_auxiliary_soft_crosscheck.json")
    assert zero["c33_policy"] == "EXCLUDE_PRIMARY_RETAIN_SEPARATE_CONTROL"
    assert not zero["primary_basis_contains_exact_zero_modes"] and zero["separate_control_defined"]
    assert not zero["control_evaluated"] and not zero["assigned_zero"] and zero["blocking"]
    assert not endpoint["merged"] and endpoint["blocking"]
    assert all(item["value"] is None for key, item in endpoint.items() if key in {"cusp", "endpoint", "transverse_closure", "infinity_junction"})
    assert auxiliary["role"] == "SOURCE_ORACLE_ONLY"
    assert not auxiliary["minkowski_light_front_modified_delta_identity"] and not auxiliary["added_to_direct_result"]

    zero_bin = load("c34_soft_side_zero_bin_limit.json")
    continuation = load("c34_soft_collinear_continuation_contract.json")
    gate = load("c34_c32_continuation_gate.json")
    assert zero_bin["tree_exact"] and zero_bin["tree_value"] == 0.0
    assert zero_bin["one_loop_value"] is None and not zero_bin["executable"]
    assert zero_bin["missing_subtraction_residual"] is None and zero_bin["duplicate_subtraction_residual"] is None
    joint = zero_bin["joint_regulator"]
    assert joint["collinear_root"] == C32_COLLINEAR_ROOT and joint["soft_root"] == C33_SOFT_ROOT
    assert joint["baryon_numbers"] == [1, 0] and not joint["shared_state"]
    assert continuation["overlap_subtraction_multiplicity"] == 1
    assert not continuation["operator_identical_test_ready"]
    assert not continuation["citation_only_equivalence_used"]
    assert not gate["passes"] and not gate["ready_status_issued"]
    assert gate["no_go"] == C34_NO_GO and gate["outcome_branch"] == "G"
    assert gate["next_package"] == "C35/S0C"
    assert gate["microscopic_proton_export"] == {"shape": [0], "values": None, "status": "EMPTY_NOT_ZERO"}
    assert not gate["bridge_rerun_executed"] and gate["bridge"] == {"common_domain_only": 12, "comparison_ready": 0}

    remainders = load("c34_soft_remainder_separation.json")
    uncertainty = load("c34_soft_uncertainty_budget.json")
    assert remainders["count"] == uncertainty["count"] == 16
    assert not remainders["merged"] and remainders["all_unknown_nonzero"]
    assert all(row["separate"] and row["status"] == NONZERO_UNKNOWN for row in remainders["records"])
    assert not uncertainty["statistical_ensemble"]
    assert not uncertainty["absorbed_into_art25_covariance"]
    assert not uncertainty["absorbed_into_proton_state"]

    holdouts = load("c34_holdout_report.json")
    assert holdouts["count"] == 24 and holdouts["frozen_before_results"] and holdouts["moved"] == 0
    assert all(row["frozen_before_symbolic_simplification"] for row in holdouts["records"])
    assert all(not row["used_in_construction"] and not row["used_in_fit"] for row in holdouts["records"])

    coverage = load("c34_requirement_coverage.json")
    assert coverage["count"] == coverage["c34_requirement_record_count"] == 300
    assert len(coverage["rows"]) == 300 and coverage["acceptance_count"] == 53
    assert coverage["inherited_c33_requirement_count"] == 2140
    assert coverage["count_semantics"] == "C34_ROWS_ONLY_INHERITED_C33_SUITE_REMAINS_SEPARATE"
    assert not coverage["cumulative_requirement_count_asserted"]
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
    assert coverage["benchmark_families"] == [f"S0A-{chr(65 + i)}" for i in range(18)]
    acceptance = coverage["rows"][:53]
    assert [row["requirement_id"] for row in acceptance] == [f"C34.ACC.{i:03d}" for i in range(1, 54)]
    assert all(row["kind"] == "ACCEPTANCE_CRITERION" for row in acceptance)
    assert [row["description"] for row in acceptance] == extract_prompt_acceptance_descriptions()
    critical_acceptance = {row["requirement_id"]: row for row in acceptance}
    assert critical_acceptance["C34.ACC.005"]["disposition"] == "NOT_CLAIMED_DUE_BRANCH_G"
    assert critical_acceptance["C34.ACC.006"]["disposition"] == "NOT_CLAIMED_DUE_BRANCH_G"
    assert critical_acceptance["C34.ACC.045"]["disposition"] == "PASS"
    assert critical_acceptance["C34.ACC.046"]["disposition"] == "PASS"
    assert critical_acceptance["C34.ACC.051"]["disposition"] == "PASS"

    crosswalk = load("c34_volume_xxi_requirement_crosswalk.json")
    extracted = extract_volume_xxi_ids()
    assert crosswalk["count"] == len(extracted) == len(set(extracted)) == 65
    assert [row["requirement_id"] for row in crosswalk["rows"]] == extracted
    assert crosswalk["source"]["sha256"] == VOLUME_XXI_SHA256
    assert crosswalk["source"]["formal_acceptance_count"] == 53
    assert crosswalk["source"]["benchmark_families"] == [f"XXI-{chr(65 + i)}" for i in range(18)]
    assert crosswalk["counts_by_status"] == {
        "C34_CLOSED": 2, "C34_FAIL_CLOSED": 5,
        "INHERITED_CLOSED": 50, "LATER_PACKAGE_DEFERRED": 8,
    }
    assert not crosswalk["positive_one_loop_physics_promoted"]
    assert all(row["evidence_paths"] and not row["positive_one_loop_physics_promoted"] for row in crosswalk["rows"])
    assert all(all((ROOT / path).is_file() for path in row["evidence_paths"]) for row in crosswalk["rows"])

    injections = load("c34_injection_manifest.json")
    assert injections["count"] == 2240 and injections["fault_modes"] == len(FAULT_CATALOG) == 80
    assert injections["ordered"] and injections["all_detected"]
    assert injections["execution_scope"] == "SEMANTIC_CONTROL_STATE_MUTATION_WITH_BASELINE_VALIDATOR"
    assert not injections["identifier_only_dispatch_used_as_evidence"]
    assert injections["semantic_control_mutation_execution_count"] == 2240
    assert injections["semantic_control_failure_detection_count"] == 2240
    assert injections["all_payload_hashes_verified"]
    assert injections["all_expected_diagnostics_match_runtime_dispatch"]
    assert injections["acceptance_criterion_50_satisfied"]
    assert len({row["mutation_payload_sha256"] for row in injections["rows"]}) == 2240
    for row in injections["rows"]:
        assert row["execution_kind"] == "SEMANTIC_CONTROL_STATE_MUTATION"
        assert row["mutation_executed"] and row["semantic_mutation_execution_verified"]
        assert row["payload_hash_verified"]
        assert content_hash(row["mutation_payload"]) == row["mutation_payload_sha256"]
        observed = execute_injection_payload(
            row["mutation_payload"], row["mutation_payload_sha256"]
        )
        assert observed == row["observed_diagnostic"] == row["expected_diagnostic"]
        assert row["independent_reexecution_observed_diagnostic"] == observed
        assert detect_injection(row["injection_id"]) == row["expected_diagnostic"]

    decision = load("c34_source_sufficiency_decision.json")
    no_go = load("c34_no_go_decision_tree.json")
    closure = examples["C34ClosureReport"]
    assert decision["primary_no_go"] == no_go["selected"] == closure.no_go_status == C34_NO_GO
    assert decision["outcome_branch"] == no_go["outcome_branch"] == "G"
    assert decision["next_package"] == no_go["next_package"] == "C35/S0C"
    assert closure.exact_next_package == C34_NEXT_PACKAGE and not closure.continuation_ready
    assert decision["missing_calculations"] and closure.exact_missing_calculation

    regression = load("c34_regression_report.json")
    assert regression["baseline_commit"] == C34_STARTING_COMMIT
    assert regression["baseline_resolved_not_invented"]
    assert regression["baseline_tests"] == 1197
    assert regression["tests"] == 1231
    assert regression["builders"] == 34 and regression["evidence_rows"] == 40 and regression["atlas_pages"] == 166
    assert regression["inherited_c33_requirements"] == 2140
    assert regression["c34_requirement_records"] == 300
    assert not regression["cumulative_requirement_count_asserted"]
    assert regression["inherited_c33_injections"] == 2040
    assert regression["c34_injection_instances"] == 2240
    assert regression["executed_c34_negative_injections"] == 2240
    assert regression["fault_modes"] == 80
    assert regression["immutable_c33_path_count"] == 74
    assert regression["all_immutable_c33_paths_byte_identical"]
    assert all(row["byte_identical"] for row in regression["immutable_c33_paths"])
    assert regression["all_integrity_records_byte_identical"]
    assert regression["authoritative_artifacts_unchanged"] and len(regression["authoritative_artifacts"]) == 8
    assert regression["production_registry"] == 216 and regression["external_art25_members"] == 642
    assert regression["source_covariance"] == {
        "shape": [642, 11], "rank": 10, "nullity": 1,
        "sha256": "33de79398ef3d75657e715abf751b5a12634e7e65e53a95b9ee19b0fb8eea16a",
    }
    assert regression["cross_root_relation"] == "NO_JOINT_MEASURE"
    assert regression["failed_bridge_projection"] == {"shape": [642, 0], "empty_not_zero": True}
    assert regression["msht20_tracked_paths"] == []
    for key in (
        "bridge_rerun", "microscopic_proton_export", "art25_consumed",
        "art25_data_consumed", "art25_chi2_consumed", "bridge_residual_consumed",
        "fit_created", "calibration_created", "likelihood_created",
        "posterior_created", "optimization_created", "reweighting_created",
        "emulator_created", "process_executed", "production_promoted",
    ):
        assert regression[key] is False
    assert regression["deterministic_reconstruction"]

    adr_paths = sorted((DOCS / "architecture_decisions").glob("*_c34_*.md"))
    assert len(adr_paths) == 11
    assert [int(path.name.split("_", 1)[0]) for path in adr_paths] == list(range(199, 210))
    assert "C34/S0A" in (ROOT / "handoff" / "ROADMAP.md").read_text()
    assert "Volume XXI" in (ROOT / "references" / "formalism_volume_index.md").read_text()
    tracked_msht = subprocess.check_output(
        ["git", "ls-files", "MSHT20_REP"], cwd=ROOT, text=True
    ).strip()
    assert tracked_msht == ""
    print("C34_VALIDATION_PASS")


if __name__ == "__main__":
    main()
