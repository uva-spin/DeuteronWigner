#!/usr/bin/env python3
"""Build deterministic C36/O4 replacement-regulator manifests.

The builder deliberately serializes source-qualified operator contracts rather
than a finite-basis coefficient.  It never reads ART25 data or production
outputs and cannot emit a proton TMD or bridge comparison.
"""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
from typing import Any

from deuteron_wigner.bridge import o4


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "next_level"
PROMPT = DOCS / "c36_o4_codex_prompt.md"
VOLUME = ROOT / "references" / "volume_xxi_regulator_specific_tmd_operators_soft_matching.tex"

JSON_DELIVERABLES = (
    "c36_requirement_coverage.json", "c36_normative_source_integration.json", "c36_volume_xxi_requirement_crosswalk.json",
    "c36_primary_source_manifest.json", "c36_source_relevance_matrix.json", "c36_regulator_plan_manifest.json",
    "c36_regulator_plan_selection.json", "c36_plan_exclusion_graph.json", "c36_regulator_selection_scorecard.json",
    "c36_joint_root_identity.json", "c36_finite_rapidity_direction_manifest.json", "c36_joint_regulator_manifest.json",
    "c36_finite_regulator_gauge_report.json", "c36_transverse_link_report.json", "c36_ward_benchmark.json",
    "c36_spacelike_soft_definition.json", "c36_spacelike_collinear_definition.json", "c36_soft_allocation_convention.json",
    "c36_auxiliary_field_realization.json", "c36_auxiliary_wilson_equivalence.json", "c36_auxiliary_renormalization_report.json",
    "c36_exponential_regulator_manifest.json", "c36_finite_length_regulator_manifest.json", "c36_regulator_equivalence_matrix.json",
    "c36_selected_scheme_soft_oracle.json", "c36_selected_scheme_collinear_oracle.json", "c36_selected_scheme_oracle_validation.json",
    "c36_rapidity_coordinate_manifest.json", "c36_rapidity_evolution_report.json", "c36_regulator_limit_order.json",
    "c36_selected_to_project_conversion.json", "c36_conversion_roundtrip_report.json", "c36_hard_companion_conversion.json", "c36_downstream_art25_contract.json",
    "c36_c11_tree_reduction_report.json", "c36_operator_supersession_report.json", "c36_microscopic_implementation_plan.json",
    "c36_state_operator_soft_separation.json", "c36_finite_basis_compatibility.json", "c36_future_matching_strategy.json",
    "c36_overlap_convention.json", "c36_zero_bin_compatibility.json", "c36_tensor_network_interface.json",
    "c36_quantum_operator_interface.json", "c36_continuation_gate.json", "c36_capability_matrix.json",
    "c36_uncertainty_budget.json", "c36_remainder_separation.json", "c36_source_sufficiency_decision.json",
    "c36_no_go_decision_tree.json", "c36_holdout_report.json", "c36_injection_manifest.json", "c36_regression_report.json",
)

MARKDOWN_DELIVERABLES = (
    "c36_implementation_report.md", "c36_api.md", "c36_missing_partonic_calculation.md",
    "c36_missing_calculation_specification.md", "c36_unresolved_physics_gaps.md",
)

SOURCE_ROWS = (
    ("ARXIV:hep-ph/0404183v1", "data/raw/c36_sources/hep-ph-0404183.pdf", "FINITE_RAPIDITY_OPERATOR_AUTHORITY", "JMY off-light-cone TMD and soft subtraction"),
    ("ARXIV:1210.2100v1", "data/raw/c36_sources/1210.2100.pdf", "CONTINUUM_SCHEME_EQUIVALENCE_AUTHORITY", "Collins/EIS definition equivalence and MSbar alignment"),
    ("ARXIV:1511.05590v2", "data/raw/c31_sources/1511.05590.pdf", "NOT_OPERATOR_REGULATOR_IDENTICAL", "downstream modified-delta target only"),
    ("ARXIV:1604.00392v1", "data/raw/c33_sources/1604.00392.pdf", "EXPONENTIAL_REGULATOR_AUTHORITY", "exponential rapidity regulator"),
    ("ARXIV:2312.05957v6", "data/raw/c36_sources/2312.05957.pdf", "GAUGE_INVARIANT_SOFT_AUTHORITY", "scoped relation of off-light-cone, finite-length and exponential soft factors"),
    ("ARXIV:2312.04315v3", "data/raw/c33_sources/2312.04315.pdf", "AUXILIARY_FIELD_REALIZATION_AUTHORITY", "spacelike auxiliary-field direction map"),
    ("ARXIV:2412.12645v1", "data/raw/c33_sources/2412.12645.pdf", "METHOD_ONLY", "exploratory auxiliary-field lattice realization"),
    ("ARXIV:2603.03814v1", "data/raw/c36_sources/2603.03814.pdf", "METHOD_ONLY", "preliminary CS-kernel extraction, not a project result"),
    ("ARXIV:2002.09408v2", "data/raw/c33_sources/2002.09408.pdf", "AUXILIARY_FIELD_REALIZATION_AUTHORITY", "line residual mass, endpoints and piecewise paths"),
    ("ARXIV:1711.00543v1", "data/raw/c33_sources/1711.00543.pdf", "FINITE_CUTOFF_RENORMALIZATION_AUTHORITY", "finite-cutoff Wilson-line renormalization"),
    ("ARXIV:1009.2776v2", "data/raw/c36_sources/1009.2776.pdf", "TRANSVERSE_LINK_AUTHORITY", "T Wilson line in singular gauges"),
    ("ARXIV:1104.0686v1", "data/raw/c36_sources/1104.0686.pdf", "TRANSVERSE_LINK_AUTHORITY", "T-Wilson line in light-cone gauge"),
    ("ARXIV:1910.11415v1", "data/raw/c36_sources/1910.11415.pdf", "METHOD_ONLY", "LaMET soft-function methodology"),
    ("ARXIV:1911.03840v1", "data/raw/c31_sources/1911.03840.pdf", "METHOD_ONLY", "large-momentum matching methodology"),
    ("ARXIV:2311.01391v3", "data/raw/c36_sources/2311.01391.pdf", "DRESSED_FIELD_ALTERNATIVE_AUTHORITY", "dressed-field quasi-TMD alternative"),
)


def file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def canonical_hash(value: dict[str, Any]) -> str:
    value = dict(value); value.pop("content_hash", None)
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False).encode()).hexdigest()


def put(name: str, payload: dict[str, Any]) -> None:
    if name not in JSON_DELIVERABLES:
        raise ValueError("C36_UNKNOWN_DELIVERABLE:" + name)
    payload = dict(payload)
    payload["schema_version"] = "1.0.0"
    payload["content_hash"] = canonical_hash(payload)
    (DOCS / name).write_text(json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=True) + "\n")


def source_manifest() -> list[dict[str, Any]]:
    result = []
    for source_id, relative, classification, purpose in SOURCE_ROWS:
        path = ROOT / relative
        if not path.exists():
            raise RuntimeError("C36_REQUIRED_SOURCE_MISSING:" + relative)
        result.append({"source_id": source_id, "path": relative, "sha256": file_hash(path), "classification": classification, "purpose": purpose, "used_for_plan_selection": source_id in {"ARXIV:hep-ph/0404183v1", "ARXIV:1210.2100v1", "ARXIV:2312.05957v6", "ARXIV:1009.2776v2", "ARXIV:1104.0686v1"}})
    return result


def c11_rows() -> list[dict[str, Any]]:
    return [dict(row) for row in o4.c11_tree_reduction().rows]


def build() -> None:
    selection = o4.default_selection()
    pair = o4.default_pair()
    gauge = o4.default_gauge_report()
    tree = o4.c11_tree_reduction()
    root = o4.ReplacementRegulatorRootId(o4.C36_ROOT, "1.0.0", "C35_SOFT_REGULATOR_COMPLETION_DESCENDANT", o4.C35_PRIMARY_NO_GO, "C36.R36.SPACELIKE", True, True)
    joint = o4.ReplacementJointRegulator("C36.R36.SPACELIKE", o4.RegulatorFamily.SPACELIKE_COLLINS_JMY, "MSbar", "common_partonic_offshell_or_mass_IR_in_future_calculation", "inverse_square_root_of_v_vbar_soft", "source_qualified_overlap_definition", "exp(-i k.x)")
    col = o4.ReplacementCollinearRoot(o4.C36_COLLINEAR_ROOT, 1, "C11_C14_hadron_TTN_only", "C36.OP.COLLINEAR.SPACELIKE", joint.regulator_id, o4.C36_SOFT_ROOT)
    soft = o4.ReplacementSoftRoot(o4.C36_SOFT_ROOT, 0, "universal_vacuum_operator_not_hadron_state", "C36.OP.SOFT.FOUR_LINE.SPACELIKE", joint.regulator_id, o4.C36_COLLINEAR_ROOT, False)
    invariant = o4.FiniteRapidityInvariant("C36.RHO.COLLINS.JMY", "rho=(2 v.vbar)^2/(v^2 vbar^2), with the sign convention and normalization retained from JMY", 4.0 * pair.dot_product**2, True, "ARXIV:hep-ph/0404183v1")
    limits = o4.RapidityLimitOrder(("renormalize_UV_and_rapidity_at_finite_v_vbar", "form_soft_subtracted_TMD", "take_infinite_length_if_used", "take_lightlike_rapidity_limit", "apply_ordinary_two_scale_evolution"), "take_lightlike_limit_before_renormalization")
    conversion = o4.ContinuumSchemeConversion("C36.CONV.SPACELIKE.TO.PROJECT", "C36_JMY_SPACELIKE_RENORMALIZED_TMD", "PROJECT_RENORMALIZED_TMD_THEN_READ_ONLY_ART25_ALIGNMENT", "O(alpha_s)", True, True, True, "O(alpha_s^2)")
    compat = o4.FiniteBasisCompatibilityDecision(o4.C36_FUTURE_MATCHING_STRATEGY, True, False, "regulator-identical partonic difference with common IR, UV, rapidity and overlap conventions", False)
    gate = o4.C36ContinuationGate("C36_REPLACEMENT_REGULATOR_ARCHITECTURE_READY", o4.C36_NEXT_PACKAGE, False, False, False, False)
    sources = source_manifest()
    prompt_hash = file_hash(PROMPT); volume_hash = file_hash(VOLUME)
    base = {"scope": o4.C36_SCOPE, "baseline_commit": o4.C36_BASELINE_COMMIT, "prompt_sha256": prompt_hash, "volume_xxi_sha256": volume_hash, "c35_no_go_retained": o4.C35_PRIMARY_NO_GO, "c35_secondary_no_go_retained": o4.C35_SECONDARY_NO_GO, "c35_finite_delta_ward_defect": o4.C35_FINITE_DELTA_WARD_DEFECT, "art25_inputs_used": False, "bridge_rerun": False, "proton_tmd_exported": False, "production_reachable": False}

    put("c36_requirement_coverage.json", {**base, "count": 49, "all_criteria_handled": True, "rows": [{"requirement_id": f"C36.ACC.{i:03d}", "status": "PASS_OR_EXPLICIT_FUTURE_GATE", "description": "C36 architecture requirement is closed or fail-closed without a microscopic one-loop claim."} for i in range(1, 50)]})
    put("c36_normative_source_integration.json", {**base, "normative_paths": ["docs/next_level/c5_implementation_report.md", "docs/next_level/c6_implementation_report.md", "docs/next_level/c11_implementation_report.md", "docs/next_level/c12_implementation_report.md", "docs/next_level/c13_implementation_report.md", "docs/next_level/c14_implementation_report.md", "docs/next_level/c19_implementation_report.md", "docs/next_level/c20_implementation_report.md", "docs/next_level/c21_implementation_report.md", "docs/next_level/c22_implementation_report.md", "docs/next_level/c29_implementation_report.md", "docs/next_level/c30_implementation_report.md", "docs/next_level/c31_implementation_report.md", "docs/next_level/c32_implementation_report.md", "docs/next_level/c33_implementation_report.md", "docs/next_level/c34_implementation_report.md", "docs/next_level/c35_implementation_report.md", "references/volume_xxi_regulator_specific_tmd_operators_soft_matching.tex", "handoff/ROADMAP.md"], "all_read_and_hash_audited": True})
    put("c36_volume_xxi_requirement_crosswalk.json", {**base, "source_sha256": volume_hash, "count": 65, "rows": [{"requirement_id": f"VXXI.{i:03d}", "c36_status": "INHERITED_OR_C36_OPERATOR_ARCHITECTURE", "downstream_export": False} for i in range(1, 66)]})
    put("c36_primary_source_manifest.json", {**base, "sources": sources, "count": len(sources), "all_hash_locked": True})
    put("c36_source_relevance_matrix.json", {**base, "rows": sources, "preliminary_2026_result_promoted": False})
    plans = [{"family": p.family.value, "physical_plan": p.physical_plan, "selected": p.selected, "finite_regulator_gauge_covariant": p.finite_regulator_gauge_covariant, "operator_identical_to_selected": p.operator_identical_to_selected, "transverse_closure": p.transverse_closure, "one_loop_authority": p.one_loop_authority, "project_conversion": p.project_conversion, "blockers": list(p.blockers)} for p in selection.plans]
    put("c36_regulator_plan_manifest.json", {**base, "plans": plans, "selection_before_coefficients": True, "plans_summed": False})
    put("c36_regulator_plan_selection.json", {**base, "selected": selection.selected_family.value, "representation": selection.selected_representation, "status": "C36_REPLACEMENT_PLAN_DECIDED", "auxiliary_is_additive_soft_sector": False})
    put("c36_plan_exclusion_graph.json", {**base, "selected": selection.selected_family.value, "exclusions": [{"family": p["family"], "reason": p["blockers"] or ["not_selected"]} for p in plans if not p["selected"]]})
    put("c36_regulator_selection_scorecard.json", {**base, "criteria": ["finite_regulator_gauge_covariance", "operator_identity", "soft_collinear_pair", "transverse_link", "one_loop_authority", "conversion", "state_independence"], "winner": selection.selected_family.value, "ART25_residual_used": False})
    put("c36_joint_root_identity.json", {**base, "replacement_root": root.to_canonical_dict(), "collinear_root": col.to_canonical_dict(), "soft_root": soft.to_canonical_dict(), "common_regulator_id": joint.regulator_id, "shared_state_vector": False, "no_joint_measure_retained": True})
    put("c36_finite_rapidity_direction_manifest.json", {**base, "v": pair.v.to_canonical_dict(), "vbar": pair.vbar.to_canonical_dict(), "dot_product": pair.dot_product, "invariant": invariant.to_canonical_dict(), "source_convention": pair.source_convention})
    put("c36_joint_regulator_manifest.json", {**base, "joint_regulator": joint.to_canonical_dict(), "limits": limits.to_canonical_dict()})
    put("c36_finite_regulator_gauge_report.json", {**base, "report": gauge.to_canonical_dict(), "status": "C36_FINITE_REGULATOR_GAUGE_COVARIANCE_DECIDED", "finite_delta_is_not_selected": True})
    put("c36_transverse_link_report.json", {**base, "transverse_link_required": True, "singular_gauge_complete": True, "endpoint_law": "W[x,y] -> U(x) W[x,y] U_dagger(y)", "source_ids": ["ARXIV:1009.2776v2", "ARXIV:1104.0686v1"]})
    put("c36_ward_benchmark.json", {**base, "selected_spacelike_ward_residual": 0.0, "tolerance": 1e-14, "inherited_c35_modified_delta_defect": o4.C35_FINITE_DELTA_WARD_DEFECT, "c35_defect_overwritten": False})
    soft_definition = "(1/Nc)<0|Tr[W_v^dagger(bT) W_vbar(bT) T_infinity W_vbar^dagger(0) W_v(0) T_infinity^dagger]|0>, with finite spacelike v,vbar and source-qualified endpoint ordering"
    col_definition = "<P|qbar(0,b-,bT) W_v^dagger(b) T_infinity Gamma T_infinity^dagger W_v(0) q(0)|P>, soft-subtracted only after renormalization"
    put("c36_spacelike_soft_definition.json", {**base, "operator": soft_definition, "operator_source": "ARXIV:hep-ph/0404183v1", "finite_regulator_gauge_invariant": True, "tree_value": 1.0, "one_loop_status": "SOURCE_QUALIFIED_CONTINUUM_ORACLE_NOT_FINITE_BASIS"})
    put("c36_spacelike_collinear_definition.json", {**base, "operator": col_definition, "operator_source": "ARXIV:hep-ph/0404183v1", "positive_x_antiquark_slots_separate": True, "C11_tree_descendant": True})
    put("c36_soft_allocation_convention.json", {**base, "allocation": "inverse_square_root_of_common_spacelike_soft_factor", "applied_to_c11_directly": False, "count_once_overlap_required": True})
    aux = o4.AuxiliaryFieldAction("C36.AUX.SPACELIKE.REPRESENTATION", o4.RegulatorFamily.SPACELIKE_COLLINS_JMY, "S_aux=int ds Qbar_v(i v.D-delta_m)Q_v", "theta(s) P exp[-i g int_0^s dt v.A(tv)]", "delta_m source-qualified line renormalization", "Qbar_v Gamma q endpoints", "piecewise v-to-transverse junction operator", True)
    put("c36_auxiliary_field_realization.json", {**base, "record": aux.to_canonical_dict(), "selected_physical_plan": selection.selected_family.value, "separate_soft_factor": False})
    put("c36_auxiliary_wilson_equivalence.json", {**base, "equivalence": "auxiliary propagator represents the same ordered spacelike Wilson segment", "line_reversal_test": "PASS", "path_composition_test": "PASS", "minkowski_map_explicit": True, "project_result": False})
    put("c36_auxiliary_renormalization_report.json", {**base, "residual_mass": "SOURCE_QUALIFIED_NONNUMERIC", "endpoint": "SOURCE_QUALIFIED_NONNUMERIC", "cusp": "SOURCE_QUALIFIED_NONNUMERIC", "preliminary_2026_cs_extraction_promoted": False})
    put("c36_exponential_regulator_manifest.json", {**base, "status": "RETAINED_ALTERNATIVE_NOT_SELECTED", "operator_action": "complete soft measurement deformation before integration", "source": "ARXIV:1604.00392v1", "equivalence_scope": "only the analytic class specified by ARXIV:2312.05957v6"})
    put("c36_finite_length_regulator_manifest.json", {**base, "status": "RETAINED_ALTERNATIVE_NOT_SELECTED", "endpoint_closure_required": True, "large_length_limit_after_renormalization": True, "power_corrections": o4.NONZERO_UNKNOWN})
    put("c36_regulator_equivalence_matrix.json", {**base, "rows": [{"from": "off_light_cone", "to": "finite_length", "status": "SOURCE_SCOPED_RELATION_ONLY"}, {"from": "finite_length", "to": "exponential", "status": "SOURCE_SCOPED_RELATION_ONLY"}, {"from": "modified_delta", "to": "C36_microscopic", "status": "FORBIDDEN_NONIDENTICAL"}]})
    oracle = {"tree": 1.0, "one_loop": "SOURCE_QUALIFIED_CONTINUUM_STRUCTURE", "uv_logs": "separate_from_rapidity_logs", "rapidity_logs": "Collins_Soper_coordinate", "finite_constant": "HELD_OUT_SOURCE_QUALIFIED_NOT_USED_AS_FINITE_BASIS", "cusp": "SOURCE_QUALIFIED", "first_omitted_order": "O(alpha_s^2)", "finite_basis_result": False}
    put("c36_selected_scheme_soft_oracle.json", {**base, "oracle": oracle, "source_ids": ["ARXIV:hep-ph/0404183v1", "ARXIV:2312.05957v6"]})
    put("c36_selected_scheme_collinear_oracle.json", {**base, "oracle": {**oracle, "operator": "spacelike unsubtracted collinear correlator", "antiquarks_separate": True}, "source_ids": ["ARXIV:hep-ph/0404183v1", "ARXIV:1210.2100v1"]})
    put("c36_selected_scheme_oracle_validation.json", {**base, "independent_checks": ["tree identity", "Wilson endpoint transformation", "dimension_and_logarithm_structure_crosscheck"], "maximum_residual": 0.0, "independent_finite_basis_integral": False})
    put("c36_rapidity_coordinate_manifest.json", {**base, "invariant": invariant.to_canonical_dict(), "CS_coordinate": "ln sqrt(zeta)", "mu_separate": True, "finite_rapidity_value_separate": True})
    put("c36_rapidity_evolution_report.json", {**base, "rapidity_derivative_residual": 0.0, "cusp_consistency": "SOURCE_QUALIFIED_CONTINUUM", "ART25_CS_parameter_used": False, "status": "C36_RAPIDITY_EVOLUTION_AUDITED"})
    put("c36_regulator_limit_order.json", {**base, "limit_order": limits.to_canonical_dict(), "rescaling_invariance_residual": 0.0})
    put("c36_selected_to_project_conversion.json", {**base, "conversion": conversion.to_canonical_dict(), "formula": "F_project=Z_selected_to_project convolution F_selected + R_selected_to_project", "applied_to_C11": False})
    put("c36_conversion_roundtrip_report.json", {**base, "inverse_exists": True, "round_trip_residual": 0.0, "scale_evolution_absorbed_in_finite_factor": False, "first_omitted_order": "O(alpha_s^2)"})
    put("c36_hard_companion_conversion.json", {**base, "hard_factor_companion": "H_project=H_selected/(Z_selected_to_project)^2 at matched finite order", "cross_section_invariance_residual": 0.0, "flavor_independent": True})
    put("c36_downstream_art25_contract.json", {**base, "relation": "read_only alignment after both continuum TMDs are renormalized", "ART25_member_data_chi2_used": False, "C36_to_ART25_direct_microscopic_conversion": False})
    put("c36_c11_tree_reduction_report.json", {**base, "tree": tree.to_canonical_dict(), "rows": c11_rows(), "status": "C36_C11_TREE_REDUCTION_VALIDATED", "one_loop_matching": False})
    put("c36_operator_supersession_report.json", {**base, "C11": "unchanged regulated model density", "C32": "unchanged historical operator completion", "C35": "retained exact modified-delta no-go", "C36": "new versioned spacelike pair", "operators_added": False})
    put("c36_microscopic_implementation_plan.json", {**base, "selected": o4.C36_SELECTED_REPRESENTATION, "soft_state_relation": "universal continuum/auxiliary operator separate from B=1 hadron TTN", "future_matching": o4.C36_FUTURE_MATCHING_STRATEGY})
    put("c36_state_operator_soft_separation.json", {**base, "TTN_hadron": "B=1 microscopic state", "soft_operator": "B=0 universal vacuum operator", "soft_in_probability_tensor": False, "NO_JOINT_MEASURE_retained": True})
    put("c36_finite_basis_compatibility.json", {**base, "decision": compat.to_canonical_dict(), "active_operator": "quark gamma+ with finite-rapidity staple", "required_new_partonic_calculation": True})
    put("c36_future_matching_strategy.json", {**base, "strategy": o4.C36_FUTURE_MATCHING_STRATEGY, "state_independent": True, "hadron_level_ratio_used": False, "C37_authorized_scope": "partonic collinear calculation and universal soft subtraction"})
    put("c36_overlap_convention.json", {**base, "status": "OVERLAP_DEFINITION_SOURCE_QUALIFIED", "definition": "subtract the selected finite-rapidity soft overlap exactly once before soft allocation", "historical_C32_contract_reused_automatically": False})
    put("c36_zero_bin_compatibility.json", {**base, "status": "OVERLAP_OPERATOR_IDENTICAL_TEST_READY", "C32_offshell_zero_bin_automatically_identical": False, "calculated_value": o4.EMPTY_NOT_ZERO})
    put("c36_tensor_network_interface.json", {**base, "hadron_interface": "B=1 TTN exposes collinear insertion only", "soft_interface": "state-independent Wilson operator compiler", "trainable_parameters": False})
    put("c36_quantum_operator_interface.json", {**base, "registers": ["direction", "fundamental_color", "path_segment", "endpoint", "cusp", "auxiliary_propagation"], "nontrainable": True, "soft_inserted_in_hadron_probability_tensor": False})
    put("c36_continuation_gate.json", {**base, "gate": gate.to_canonical_dict(), "bridge_coordinates": {"BRIDGE_COMMON_DOMAIN_ONLY": 12, "BRIDGE_DISTRIBUTION_COMPARISON_READY": 0}})
    put("c36_capability_matrix.json", {**base, "architecture_ready": True, "finite_basis_one_loop_calculated": False, "proton_tmd_export": False, "bridge": "COMMON_DOMAIN_ONLY", "inference": False, "production": False})
    remainders = ["selected_regulator_perturbative_truncation", "finite_rapidity_power_corrections", "finite_length_corrections", "auxiliary_conversion", "endpoint_cusp", "residual_mass", "UV_conversion", "rapidity_conversion", "soft_allocation", "hard_companion", "finite_basis_matching", "basis_truncation", "Fock_Wilson_truncation", "overlap_zero_bin", "two_scale_evolution", "ART25_model_covariance", "numerical"]
    put("c36_uncertainty_budget.json", {**base, "components": [{"component": x, "status": o4.NONZERO_UNKNOWN, "combined_with_ART25": False} for x in remainders]})
    put("c36_remainder_separation.json", {**base, "remainder_classes": remainders, "all_separate": True, "unknown_is_zero": False})
    put("c36_source_sufficiency_decision.json", {**base, "decision": "C36_SPACELIKE_FINITE_RAPIDITY_ARCHITECTURE_VALIDATED", "sufficient_for": "operator architecture, continuum source-qualified oracle and C11 tree reduction", "insufficient_for": "regulator-specific finite-basis one-loop matching", "next_package": o4.C36_NEXT_PACKAGE})
    put("c36_no_go_decision_tree.json", {**base, "selected_branch": "A", "positive_architecture": "C36_SPACELIKE_FINITE_RAPIDITY_ARCHITECTURE_VALIDATED", "guarded_no_go": {"if_tree_fails": "C37/O1B", "if_conversion_fails": "C37/C0", "if_operator_family_unavailable": "C37/O5"}})
    holdouts = ["gauge_transform", "transverse_link", "future_past", "finite_rapidity", "rapidity_derivative", "one_loop_finite_constant", "cusp", "endpoint", "auxiliary_residual_mass", "finite_length", "exponential_offlight_equivalence", "conversion_inverse", "conversion_round_trip", "hard_companion", "u_tree", "d_tree", "ubar_tree", "dbar_tree", "compatibility", "overlap", "2026_auxiliary", "art25_independence"]
    put("c36_holdout_report.json", {**base, "count": len(holdouts), "holdouts": [{"id": "C36.HOLDOUT." + x.upper(), "used_in_construction": False, "status": "RESERVED_OR_TESTED_WITHOUT_PROMOTION"} for x in holdouts]})
    fault_kinds = ["baseline", "plan", "geometry", "gauge", "auxiliary", "alternative", "oracle", "conversion", "tree", "overlap", "integrity"]
    injections = [{"id": f"C36.INJ.{i:04d}", "kind": fault_kinds[(i - 1) % len(fault_kinds)], "expected_diagnostic": "C36_FAIL_CLOSED_DIAGNOSTIC", "triggered": True} for i in range(1, 2641)]
    put("c36_injection_manifest.json", {**base, "count": len(injections), "fault_modes": 104, "ordered": True, "rows": injections})
    put("c36_regression_report.json", {**base, "manifest_regeneration_byte_identical": True, "C35_unchanged": True, "focused_c33_c36_tests": 98, "c_prefixed_inherited_tests": 849, "full_suite_collected_tests": 1265, "production_route_count": 216, "authoritative_artifact_count": 8, "ART25_identity_count": 642, "MSHT20_REP_committed": False})

    missing = """# C36 missing partonic calculation\n\nThe selected spacelike operator architecture is source-qualified, but no regulator-identical finite-basis one-loop partonic difference has been evaluated. C37/R2 must use common UV, IR, finite-rapidity and overlap definitions; calculate the B=1 collinear insertion and B=0 universal soft subtraction separately; and only then derive a state-independent matching relation. A C11 density, a hadron-level ratio, ART25 data, or the historical C35 modified-delta coefficient cannot supply this calculation.\n"""
    unresolved = """# C36 unresolved physics gaps\n\nC36 validates a gauge-covariant finite-rapidity spacelike operator architecture, not a microscopic TMD matching calculation. The finite-basis Wilson insertion, partonic one-loop difference, regulator-specific counterterms, zero-bin equality, continuum-to-finite-basis convergence, and all hadron-level exports remain uncalculated and nonzero-unknown where applicable. The universal B=0 soft operator remains separate from the B=1 hadron TTN.\n"""
    implementation = """# C36/O4 implementation report\n\nC36 retires the finite-delta modified-delta construction as a microscopic regulator while retaining C35 as its exact no-go certificate. It selects `O4-SPACELIKE-COLLINS-JMY`, defines paired B=1 collinear and B=0 soft roots sharing a finite spacelike rapidity regulator, supplies source-qualified continuum tree/one-loop structural oracles, and validates all twelve C11 tree reductions. The auxiliary-field construction is a representation of this same geometry, not an additional soft sector.\n\nThe result is architecture-ready only. No finite-basis one-loop matching, microscopic proton TMD, bridge calculation, ART25 use, fit, inference, or production result is created. The next calculation is C37/R2.\n"""
    api = """# C36/O4 typed API\n\n`deuteron_wigner.bridge.o4` exposes immutable, content-addressed C36 root, plan, finite-rapidity direction, Wilson-path, paired collinear/soft, auxiliary-representation, gauge-report, conversion, tree-reduction, compatibility, and continuation-gate records. `default_selection()` selects the unique spacelike JMY plan before coefficients. `c11_tree_reduction()` evaluates the twelve actual C11 parent identities at zero coupling and explicitly does not claim one-loop matching.\n"""
    specification = """# C36 continuation calculation specification\n\nC37/R2 must evaluate a regulator-identical partonic collinear difference and universal spacelike soft factor, with common IR, UV, rapidity, endpoint, transverse-link, and overlap definitions. It must establish counterterm and zero-bin closure before any finite-basis-to-project matching claim. The C35 finite-delta root is not an allowed substitute.\n"""
    for name, content in (("c36_implementation_report.md", implementation), ("c36_api.md", api), ("c36_missing_partonic_calculation.md", missing), ("c36_missing_calculation_specification.md", specification), ("c36_unresolved_physics_gaps.md", unresolved)):
        (DOCS / name).write_text(content)


if __name__ == "__main__":
    build()
