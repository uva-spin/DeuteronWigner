#!/usr/bin/env python3
"""Fail-closed validator for the C33/S0 tree-level soft-sector package."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

from deuteron_wigner.bridge.s0.core import (
    ARCHITECTURE_TYPES,
    C32_COLLINEAR_ROOT,
    C33_SOFT_ROOT,
    FAULT_CATALOG,
    EikonalDirection,
    SoftRapidityRegulator,
    architecture_examples,
    default_four_line_operator,
    detect_injection,
    deterministic_json,
    fail_closed_one_loop_ledger,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "next_level"
VOLUME_XXI_PATH = ROOT / "references" / "volume_xxi_regulator_specific_tmd_operators_soft_matching.tex"
VOLUME_XXI_SHA256 = "613d26bcd58b4c9d15b23ef955cbb04feb2edc7d854d4ed63339c50835fa72c4"


def load(name: str):
    return json.loads((DOCS / name).read_text())


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


DELIVERABLES = (
    "c33_implementation_report.md", "c33_api.md", "c33_requirement_coverage.json",
    "c33_normative_source_integration.json", "c33_primary_source_manifest.json",
    "c33_source_relevance_matrix.json", "c33_two_root_tmd_identity.json",
    "c33_soft_collinear_provenance_graph.json", "c33_soft_sector_plan_manifest.json",
    "c33_soft_sector_plan_selection.json", "c33_vacuum_hilbert_manifest.json",
    "c33_soft_basis_manifest.json", "c33_soft_zero_mode_policy.json",
    "c33_soft_basis_trajectory_plan.json", "c33_eikonal_color_space.json",
    "c33_four_line_operator_manifest.json", "c33_eikonal_path_reversal_report.json",
    "c33_auxiliary_field_soft_oracle.json", "c33_auxiliary_direct_equivalence_report.json",
    "c33_soft_rapidity_regulator_manifest.json", "c33_eikonal_denominator_report.json",
    "c33_soft_diagram_ledger.json", "c33_soft_counterterm_ledger.json",
    "c33_soft_dependency_graph.json", "c33_bare_soft_factor.json",
    "c33_bare_soft_oracle_report.json", "c33_soft_uv_renormalization.json",
    "c33_soft_uv_anomalous_dimension_report.json", "c33_soft_rapidity_renormalization.json",
    "c33_soft_rapidity_anomalous_dimension.json", "c33_soft_collins_soper_kernel_oracle.json",
    "c33_continuum_soft_oracle.json", "c33_continuum_soft_validation_report.json",
    "c33_soft_regulator_matching_library.json", "c33_soft_regulator_roundtrip_report.json",
    "c33_soft_regulator_remainder.json", "c33_soft_basis_trajectory.json",
    "c33_soft_continuum_extrapolation.json", "c33_soft_power_correction_manifest.json",
    "c33_soft_collinear_regulator_pair.json", "c33_soft_collinear_compatibility_report.json",
    "c33_zero_bin_interface_contract.json", "c33_soft_tensor_network_manifest.json",
    "c33_soft_quantum_interface_contract.json", "c33_c32_continuation_gate.json",
    "c33_soft_uncertainty_budget.json", "c33_soft_remainder_separation.json",
    "c33_source_sufficiency_decision.json", "c33_no_go_decision_tree.json",
    "c33_missing_calculation_specification.md", "c33_holdout_report.json",
    "c33_injection_manifest.json", "c33_regression_report.json",
    "c33_unresolved_physics_gaps.md", "c33_volume_xxi_requirement_crosswalk.json",
)


def extract_volume_xxi_ids() -> list[str]:
    rows = []
    for raw_line in VOLUME_XXI_PATH.read_text().splitlines():
        line = raw_line.strip()
        if not line.startswith("V21."):
            continue
        assert "&" in line and line.endswith(r"\\")
        rows.append(line.split("&", 1)[0].strip())
    return rows


def main() -> None:
    assert all((DOCS / name).is_file() for name in DELIVERABLES)

    norm = load("c33_normative_source_integration.json")
    assert norm["all_required_present"] and norm["volume_xxi_present"]
    assert norm["volume_xxi_present_at_c33_execution"] is False
    assert norm["volume_xxi_present_now"] is True
    assert norm["volume_xxi_path"] == str(VOLUME_XXI_PATH.relative_to(ROOT))
    assert norm["volume_xxi_expected_sha256"] == VOLUME_XXI_SHA256
    assert norm["volume_xxi_sha256"] == file_hash(VOLUME_XXI_PATH) == VOLUME_XXI_SHA256
    assert norm["volume_xxi_status"] == "INTEGRATED_POST_C33_NO_NUMERICAL_CHANGE"
    assert norm["prompt_sha256"] == file_hash(DOCS / "c33_s0_codex_prompt.md")
    volume_xxi_norm = next(row for row in norm["records"] if row["path"] == str(VOLUME_XXI_PATH.relative_to(ROOT)))
    assert volume_xxi_norm["classification"] == "PROJECT_NORMATIVE_FORMALISM"
    assert not volume_xxi_norm["operator_regulator_identical_calculation"]
    assert not volume_xxi_norm["supplies_finite_basis_one_loop_coefficients"]

    crosswalk = load("c33_volume_xxi_requirement_crosswalk.json")
    extracted_v21_ids = extract_volume_xxi_ids()
    crosswalk_ids = [row["requirement_id"] for row in crosswalk["rows"]]
    assert crosswalk["source"]["path"] == str(VOLUME_XXI_PATH.relative_to(ROOT))
    assert crosswalk["source"]["sha256"] == VOLUME_XXI_SHA256
    assert crosswalk["source"]["classification"] == "PROJECT_NORMATIVE_FORMALISM"
    assert not crosswalk["source"]["operator_regulator_identical_calculation"]
    assert not crosswalk["source"]["supplies_finite_basis_one_loop_coefficients"]
    assert crosswalk["source"]["historical_c33_execution_status"] == "ABSENT_NOT_INVENTED"
    assert crosswalk["source"]["integration_status"] == "INTEGRATED_POST_C33_NO_NUMERICAL_CHANGE"
    assert crosswalk["count"] == crosswalk["source"]["formal_requirement_count"] == 65
    assert crosswalk["source"]["formal_acceptance_count"] == 53
    assert crosswalk["source"]["benchmark_families"] == [f"XXI-{chr(65 + i)}" for i in range(18)]
    assert crosswalk["source"]["minimum_ordered_negative_injections"] == 2040
    assert crosswalk["c33_ordered_negative_injections"] == 2040
    assert crosswalk["minimum_ordered_negative_injections_satisfied"]
    assert len(extracted_v21_ids) == len(set(extracted_v21_ids)) == 65
    assert crosswalk_ids == extracted_v21_ids and crosswalk["all_ids_unique"]
    assert crosswalk["counts_by_status"] == {
        "C33_CLOSED": 50, "C33_FAIL_CLOSED": 4, "C34_DEFERRED": 11,
    }
    assert crosswalk["all_evidence_present"]
    for row in crosswalk["rows"]:
        assert row["status"] in crosswalk["status_definitions"]
        assert row["evidence_paths"] and row["all_evidence_present"]
        assert all((ROOT / path).is_file() for path in row["evidence_paths"])
        assert not row["positive_physics_promoted"]
    deferred = {row["requirement_id"] for row in crosswalk["rows"] if row["status"] == "C34_DEFERRED"}
    assert {"V21.ORACLE.1", "V21.ORACLE.2"} <= deferred
    assert {f"V21.MATCH.{i}" for i in range(1, 6)} <= deferred
    status_by_id = {row["requirement_id"]: row["status"] for row in crosswalk["rows"]}
    assert status_by_id["V21.ROOT.3"] == "C34_DEFERRED"
    assert status_by_id["V21.COLL.1"] == "C33_CLOSED"
    assert status_by_id["V21.MATCH.6"] == status_by_id["V21.MATCH.7"] == "C33_CLOSED"
    assert crosswalk["c33_no_go"] == "C33_SOFT_TREE_LEVEL_ONLY"
    assert crosswalk["immediate_next_package"] == "C34/S0A"
    assert not crosswalk["microscopic_proton_exported"]
    assert not crosswalk["bridge_rerun"] and not crosswalk["inference_or_production_promoted"]
    hashed = dict(crosswalk)
    recorded_hash = hashed.pop("content_hash")
    assert recorded_hash == hashlib.sha256(
        json.dumps(hashed, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

    sources = load("c33_primary_source_manifest.json")
    assert sources["count"] == 11 and sources["all_present"]
    for row in sources["records"]:
        assert row["present"] and row["sha256"] == file_hash(ROOT / row["path"])
        assert row["url"].startswith("https://arxiv.org/pdf/")
        assert row["reconstruction_command"].startswith("curl -L https://arxiv.org/pdf/")
        assert "NOT_OPERATOR_REGULATOR_IDENTICAL" in row["classifications"]
        assert not row["operator_identical_to_c33_finite_basis"]
        assert not row["used_as_finite_basis_coefficient"]
    relevance = load("c33_source_relevance_matrix.json")
    assert relevance["all_not_operator_regulator_identical"] and len(relevance["rows"]) == 11

    roots = load("c33_two_root_tmd_identity.json")
    assert roots["collinear_root"]["root_id"] == C32_COLLINEAR_ROOT
    assert roots["collinear_root"]["baryon_number"] == 1
    assert roots["soft_root"]["root_id"] == C33_SOFT_ROOT
    assert roots["soft_root"]["baryon_number"] == 0
    assert not roots["shared_state_vector"] and not roots["shared_probability_normalization"]
    assert not roots["composition_is_probability_sum"]

    plans = load("c33_soft_sector_plan_manifest.json")
    selection = load("c33_soft_sector_plan_selection.json")
    assert plans["mutually_exclusive"] and len(plans["plans"]) == 4
    assert selection["selected_plan"] == "S0-FB-EIKONAL-FOCK"
    assert selection["selected_before_numerical_comparison"] and not selection["plans_added"]

    basis = load("c33_soft_basis_manifest.json")
    hilbert = load("c33_vacuum_hilbert_manifest.json")
    resolutions = basis["resolutions"]
    assert len(resolutions) == 3
    assert [row["nesting_rank"] for row in resolutions] == [1, 2, 3]
    assert [row["hilbert_dimension"] for row in resolutions] == [3841, 30721, 103681]
    assert all(row["rapidity_regions"] == ["n", "nbar"] for row in resolutions)
    assert all(not row["fixed_total_K"] for row in resolutions)
    assert hilbert["baryon_number"] == 0
    assert hilbert["proton_state_reference"] is None
    zero = load("c33_soft_zero_mode_policy.json")
    assert zero["zero_mode_contribution"] == "NONZERO_UNKNOWN"
    assert zero["replacement_task"].startswith("C34/S0A")

    operator = default_four_line_operator()
    color = load("c33_eikonal_color_space.json")
    op = load("c33_four_line_operator_manifest.json")
    assert color["C_F"] == 4 / 3 and color["tree_trace"] == 1.0
    assert len(color["lines"]) == 4 and color["f_d_color_class"] is None
    assert all(row["orientation_variants"] == ["FUTURE", "PAST"] for row in color["lines"])
    assert all("TRANSVERSE_CLOSURE" in row["segments"] for row in color["lines"])
    assert operator.tree_level_soft_factor.numerator == 1
    assert op["tree_value"] == 1.0 and op["tree_value_exact"] and op["one_loop_value"] is None
    reversal = load("c33_eikonal_path_reversal_report.json")
    assert reversal["hermitian_conjugation_residual_tree"] == 0.0
    assert reversal["future_past_residual_tree"] == 0.0
    assert reversal["one_loop_residuals"] is None and not reversal["manual_signs_used"]

    reg = SoftRapidityRegulator("validation", "MODIFIED_DELTA", 1e-4, 2e-4, -1, 1,
                                ("COMBINE_REAL_VIRTUAL", "REMOVE_DELTA"))
    directions = {
        "n": EikonalDirection("n", "n", (1, 0, 0, 1), "k_minus", "delta_minus"),
        "nbar": EikonalDirection("nbar", "nbar", (1, 0, 0, -1), "k_plus", "delta_plus"),
    }
    denominator_report = load("c33_eikonal_denominator_report.json")
    assert denominator_report["manual_sign_insertions"] == 0
    for row in denominator_report["records"]:
        direction = "nbar" if ".NBAR" in row["line_id"] else "n"
        conjugate = ".DAGGER" in row["line_id"]
        derived = reg.derive_denominator(directions[direction], "FUTURE", conjugate, 1)
        assert row["component"] == derived.momentum_component
        assert row["delta"] == derived.delta_component
        assert row["i0_sign"] == ("+" if derived.i0_sign > 0 else "-")
    rapidity = load("c33_soft_rapidity_regulator_manifest.json")
    assert not rapidity["finite_basis_is_rapidity_regulator"]
    assert rapidity["physical_numerical_epsilon"] is None
    assert not rapidity["zeta_is_bare_regulator"]

    ledger = load("c33_soft_diagram_ledger.json")
    assert ledger["count"] == 18 and ledger["calculated_one_loop"] == 0
    assert ledger["silent_zero"] == 0 and ledger["all_required_explicit"]
    assert len(fail_closed_one_loop_ledger()) == 18
    assert all(row["status"] == "CALCULATION_REQUIRED" and row["assigned_zero"] is False for row in ledger["records"])
    assert all(row["symbolic_expression"] is None and row["numerical_implementation"] is None for row in ledger["records"])
    counterterms = load("c33_soft_counterterm_ledger.json")
    assert len(counterterms["records"]) == 3 and counterterms["derived"] == 0

    bare = load("c33_bare_soft_factor.json")
    assert bare["tree_value"] == 1.0 and bare["tree_exact"]
    assert bare["one_loop_coefficient"] is None
    assert bare["one_loop_value_status"] == "NONZERO_UNKNOWN"
    assert not bare["continuum_value_substituted"] and bare["status"] == "C33_SOFT_TREE_LEVEL_ONLY"
    assert load("c33_bare_soft_oracle_report.json")["tree_residual"] == 0.0

    uv = load("c33_soft_uv_renormalization.json")
    rap = load("c33_soft_rapidity_renormalization.json")
    rad = load("c33_soft_rapidity_anomalous_dimension.json")
    assert uv["one_loop_Z_uv"] is None and not uv["state_independent_claim"]
    assert rap["one_loop_R_rapidity"] is None and rap["regulator_cancellation_residual"] is None
    assert rad["finite_basis_value"] is None and not rad["fitted"]

    continuum = load("c33_continuum_soft_oracle.json")
    continuum_check = load("c33_continuum_soft_validation_report.json")
    assert continuum["status"] == "SOURCE_QUALIFIED_CONTINUUM_ORACLE"
    assert not continuum["finite_basis_identity"] and not continuum["used_as_finite_basis_result"]
    assert continuum_check["source_expression_present"]
    assert not continuum_check["independent_symbolic_or_direct_integral_reconstruction"]
    assert continuum_check["numerical_residual"] is None

    matching = load("c33_soft_regulator_matching_library.json")
    trajectory = load("c33_soft_basis_trajectory.json")
    compatibility = load("c33_soft_collinear_compatibility_report.json")
    zero_bin = load("c33_zero_bin_interface_contract.json")
    assert matching["one_loop_kernel"] is None and not matching["fit_performed"]
    assert load("c33_soft_regulator_remainder.json")["value_status"] == "NONZERO_UNKNOWN"
    assert trajectory["status"] == "SOFT_TRAJECTORY_UNAVAILABLE"
    assert trajectory["one_loop_observables"] == [None, None, None]
    assert compatibility["status"] == "SOFT_COLLINEAR_COMPATIBILITY_UNRESOLVED"
    assert not compatibility["full_tmd_ready"]
    pair_axes = {row["axis"] for row in load("c33_soft_collinear_regulator_pair.json")["axes"]}
    assert {"fourier_convention", "external_state_IR", "overlap", "removal_order"} <= pair_axes
    assert zero_bin["status"] == "C33_ZERO_BIN_INTERFACE_DEFINED"
    assert not zero_bin["executable"] and zero_bin["subtraction_multiplicity"] == 1
    assert zero_bin["tree_value"] == 0.0 and zero_bin["tree_value_exact"]
    assert zero_bin["one_loop_value"] is None
    assert zero_bin["missing_subtraction_residual"] is None
    assert zero_bin["duplicate_subtraction_residual"] is None

    gate = load("c33_c32_continuation_gate.json")
    assert not gate["passes"] and not gate["ready_status_issued"]
    assert gate["no_go"] == "C33_SOFT_TREE_LEVEL_ONLY" and gate["next_package"] == "C34/S0A"
    assert gate["microscopic_proton_export"]["shape"] == [0]
    assert gate["microscopic_proton_export"]["status"] == "EMPTY_NOT_ZERO"
    assert not gate["bridge_rerun_executed"] and gate["bridge"] == {"common_domain_only": 12, "comparison_ready": 0}

    remainders = load("c33_soft_remainder_separation.json")
    assert len(remainders["components"]) == 14 and not remainders["merged"]
    assert all(row["status"] == "NONZERO_UNKNOWN" and row["separate"] for row in remainders["components"])
    decision = load("c33_source_sufficiency_decision.json")
    tree = load("c33_no_go_decision_tree.json")
    assert decision["primary_no_go"] == "C33_SOFT_TREE_LEVEL_ONLY"
    assert decision["outcome_branch"] == "E" and decision["next_package"] == "C34/S0A"
    assert tree["selected"] == decision["primary_no_go"] and len(decision["missing_calculations"]) == 8

    holdouts = load("c33_holdout_report.json")
    assert holdouts["count"] == 25 and holdouts["moved"] == 0
    assert all(not row["used_in_derivation"] and not row["used_in_fit"] for row in holdouts["records"])
    injections = load("c33_injection_manifest.json")
    assert injections["count"] == 2040 and injections["fault_modes"] == len(FAULT_CATALOG) == 92
    assert injections["count"] >= crosswalk["source"]["minimum_ordered_negative_injections"]
    assert injections["ordered"] and injections["all_detected"]
    assert all(detect_injection(row["injection_id"]) == row["expected_diagnostic"] for row in injections["rows"])
    coverage = load("c33_requirement_coverage.json")
    assert coverage["count"] == 2140 and coverage["acceptance_count"] == 51
    assert len(coverage["benchmark_families"]) == 18 and coverage["all_covered"]

    examples = architecture_examples()
    assert len(ARCHITECTURE_TYPES) == len(examples) == 47
    for value in examples.values():
        serial = json.loads(deterministic_json(value))
        envelope = serial["c33_identity_envelope"]
        assert envelope["baryon_number"] == 0
        assert envelope["soft_root_id"] == C33_SOFT_ROOT
        assert envelope["consumes_art25"] is False
        assert envelope["inference_reachable"] is False
        assert envelope["production_reachable"] is False

    regression = load("c33_regression_report.json")
    assert regression["baseline_commit"] == "0d7b94a5e86882b23a56d4c1f11900d554756a18"
    assert regression["required_c28_ancestor"] == "52678312906bf5cc0bb8664e2486d5d676a6b723"
    assert regression["baseline_tests"] == 1167
    assert regression["builders"] == 33 and regression["evidence_rows"] == 39 and regression["atlas_pages"] == 165
    assert regression["requirements"] == 2140 and regression["injections"] == 2040 and regression["fault_modes"] == 92
    assert regression["all_immutable_records_byte_identical"]
    assert regression["authoritative_artifacts_unchanged"] and len(regression["authoritative_artifacts"]) == 8
    assert regression["production_registry"] == 216 and regression["external_art25_members"] == 642
    assert regression["source_covariance"]["rank"] == 10 and regression["source_covariance"]["nullity"] == 1
    assert regression["cross_root_relation"] == "NO_JOINT_MEASURE" and not regression["bridge_rerun"]
    for key in ("fit_created", "calibration_created", "likelihood_created", "posterior_created",
                "optimization_created", "reweighting_created", "emulator_created",
                "process_executed", "production_promoted"):
        assert not regression[key]

    adr_paths = sorted((DOCS / "architecture_decisions").glob("*_c33_*.md"))
    assert len(adr_paths) == 13
    assert (DOCS / "architecture_decisions" / "198_c33_volume_xxi_integration.md") in adr_paths
    assert "C33/S0" in (ROOT / "handoff" / "ROADMAP.md").read_text()
    assert "C33/S0" in (ROOT / "references" / "formalism_volume_index.md").read_text()
    tracked_msht = subprocess.check_output(["git", "ls-files", "MSHT20_REP"], cwd=ROOT, text=True).strip()
    assert tracked_msht == ""
    print("C33_VALIDATION_PASS")


if __name__ == "__main__":
    main()
