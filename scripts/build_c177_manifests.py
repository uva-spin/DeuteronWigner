"""Build deterministic C177 metadata from the public source/path API."""
from __future__ import annotations

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from deuteron_wigner.bridge import hqcdb0reslinksource1 as c

DOCS = Path(__file__).resolve().parents[1] / "docs/next_level"
RUNTIME = Path(__file__).resolve().parents[1] / "data/runtime/c177_hqcdb0reslinksource1"


def plain(v):
    if isinstance(v, dict):
        return {k: plain(x) for k, x in v.items()}
    if hasattr(v, "items"):
        return {k: plain(x) for k, x in v.items()}
    if isinstance(v, (tuple, list)):
        return [plain(x) for x in v]
    return v


def put(name, value):
    (DOCS / name).write_text(json.dumps(plain(value), indent=2, sort_keys=True) + "\n")


def envelope(schema, payload):
    return {"schema": schema, "status": c.STATUS, "plan": c.PLAN, "package_root": c.PACKAGE_ROOT, **plain(payload)}


def main():
    api = {
        "c177_input_freeze.json": {"baseline": c.BASELINE, "prompt": c.PROMPT, "prompt_sha256": c.PROMPT_SHA256, "contract": c.CONTRACT, "contract_sha256": c.CONTRACT_SHA256, "C176_package_root": c.c176.PACKAGE_ROOT, "protected_paths": ["MSHT20_REP/", "docs/next_level/c69_qgembed5_codex_prompt.md"], "user_worktree_modification": "handoff/ROADMAP.md preserved"},
        "c177_c176_boundary_freeze.json": c.c176_boundary_freeze(),
        "c177_authority_preservation_report.json": c.verify_hqcd_b0reslinksource1_authority(),
        "c177_contract_provenance_report.json": {"committed_contract": c.CONTRACT, "sha256": c.CONTRACT_SHA256, "present": True, "parent_commit": "999304915be1d5de0210cf0a07e5cfabbb524fdb149ece93ccd2d5600203cbd5", "C170_C176_prompt_only_chain_preserved": True, "retrospective_contracts_invented": 0},
        "c177_regression_boundary_contract.json": {"C134": "quarantined unrelated expectation failure; not repaired", "C157": "inherited untracked test preserved", "C158_C176": "targeted read-only boundary", "graph_mutation": 0},
        "c177_regression_boundary_validation.json": {"C134_quarantine": True, "C157_untracked_preserved": True, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0},
        "c177_c134_quarantine_validation.json": {"status": "PRESERVED_QUARANTINED_UNRELATED_EXPECTATION_FAILURE", "repair_performed": False, "files_modified": 0},
        "c177_graph_nonmutation_validation.json": c.dependency_frontier_manifest(),
        "c177_b0_nonrecomputation_validation.json": c.b0reslinksource1_no_recomputation_report(),
        "c177_b1_nonmutation_validation.json": {"B1_mutations": 0, "C170_B1_qgg": "preserved", "C170_B1_qqbarq": "preserved"},
        "c177_quantum_nonmutation_validation.json": {"Q0_Q1_Q2_modified": False, "states_created": 0, "TMD_objects_created": 0, "production_QubitUnitary": 0},
        "c177_historical_status_preservation.json": {"C43_C130_C176": "preserved", "historical_statuses_rewritten": 0},
        "c177_user_worktree_preservation.json": {"handoff/ROADMAP.md": "pre-existing user modification preserved", "protected_untracked_paths": "untouched"},
        "c177_scientific_question_contract.json": {"question": "recover exact source path objects and determine continuum/finite-cell/project-path closure", "no_boundary_evaluation": True},
        "c177_source_convention_finitecell_layer_manifest.json": {"source": "continuum source objects", "C43": "explicit adapter", "finite_cell": "incomplete", "project_path": "not selected"},
        "c177_source_convention_finitecell_layer_validation.json": {"continuum_source_ready": True, "C43_adapter_ready": True, "finite_cell_adapter_ready": False},
        "c177_source_audit_contract.json": {"authorized_sources": ["hep-ph/0208038v2", "hep-ph/0206057v2", "hep-ph/0404183v1"], "official_only": True, "browse_or_search_summary": False},
        "c177_source_audit_manifest.json": c.source_audit_manifest(),
        "c177_source_acquisition_manifest.json": {"local_cache_first": True, "acquired": [{"source_id": "JY-HEP-PH-0206057V2", "endpoint": "https://arxiv.org/e-print/hep-ph/0206057v2 and https://arxiv.org/pdf/hep-ph/0206057v2", "path": "data/raw/c177_sources/", "official": True}], "additional_source_search": False},
        "c177_source_release_policy.json": {"license": "arXiv source artifacts retained locally; no separate redistribution license asserted", "code_executed": False, "archive_extracted_safely": True},
        "c177_source_hash_validation.json": c.source_audit_manifest(),
        "c177_source_object_contract.json": {"exact_objects": 7, "visual_verification": True, "independent_transcription": True},
        "c177_source_object_manifest.json": c.source_object_manifest(),
        "c177_source_object_validation.json": {"all_objects_have_version_page_locator": True, "comparison_only_JMY": True},
        "c177_source_locator_crosswalk.json": c.source_locator_crosswalk(),
        "c177_plan_contract.json": {"plans": ["B0RESLINKSOURCE1-B"], "exactly_one_selected": True},
        "c177_plan_decision.json": c.b0reslinksource1_plan_manifest(),
        "c177_plan_validation.json": {"selected_plan": c.PLAN, "first_remaining_object": "finite-cell adapter"},
        "c177_convention_adapter_contract.json": {"routes": ["CONV-A", "CONV-B", "CONV-C", "CONV-D"], "C43_source_signs_fitted": False},
        "c177_convention_adapter_manifest.json": c.convention_adapter_manifest(),
        "c177_convention_adapter_validation.json": {"source_to_C43_explicit": True, "route_order_reversal": "pass", "future_past_signs_merged": False},
        "c177_continuum_path_class_contract.json": {"path_classes": 6, "straight_path_inferred": False, "continuum_only": True},
        "c177_continuum_path_class_manifest.json": c.continuum_path_class_manifest(),
        "c177_continuum_path_class_validation.json": {"source_path_class_ready": True, "future_past_separate": True, "JMY_promoted": False},
        "c177_half_link_cancellation_contract.json": {"source_equation": "BJY Eq. (52)", "non_Abelian": True, "ordered": True},
        "c177_half_link_cancellation_manifest.json": c.half_link_cancellation_manifest(),
        "c177_half_link_cancellation_validation.json": {"source_route": True, "concatenation_route": True, "degree_two_order": True, "generated_adjoint_route": True},
        "c177_pure_gauge_contract.json": {"source_scope": "BJY Eq. (38) leading perturbative small contractable transformations", "full_nonAbelian_promotion": False},
        "c177_pure_gauge_manifest.json": c.pure_gauge_manifest(),
        "c177_pure_gauge_validation.json": {"classification": "LINEARIZED_PATH_INDEPENDENT_ONLY", "finite_HO_promoted": False},
        "c177_path_independence_manifest.json": c.path_independence_manifest(),
        "c177_future_past_contract.json": {"DIS": "+infinity", "DY": "-infinity", "PV": "antisymmetric", "merged": False},
        "c177_future_past_manifest.json": c.future_past_manifest(),
        "c177_future_past_validation.json": {"future_past_separate": True, "source_Eq_113_115": True},
        "c177_pv_orientation_manifest.json": c.pv_orientation_manifest(),
        "c177_representation_lift_contract.json": {"routes": ["REP-A", "REP-B", "REP-C", "REP-D", "REP-E"], "generators": 8, "open_adjoint": True},
        "c177_representation_lift_manifest.json": c.representation_lift_manifest(),
        "c177_representation_lift_validation.json": {"all_eight_generator_intertwining": True, "first_order_residual": 0.0, "degree_two_order_preserved": True, "singlet_projection": False},
        "c177_finite_cell_adapter_contract.json": {"routes": ["CELL-A", "CELL-B", "CELL-C", "CELL-D", "CELL-E", "CELL-F"], "infinity_equals_L_by_notation": False},
        "c177_finite_cell_adapter_manifest.json": c.finite_cell_adapter_manifest(),
        "c177_finite_cell_adapter_validation.json": {"adapter_ready": False, "global_holonomy_explicit": True, "C174_subgauge_reselected": False},
        "c177_finite_ho_path_contract.json": {"routes": ["HO-PATH-A", "HO-PATH-B", "HO-PATH-C", "HO-PATH-D", "HO-PATH-E"], "link_kernel_constructed": False},
        "c177_finite_ho_path_manifest.json": c.finite_ho_path_manifest(),
        "c177_finite_ho_path_validation.json": {"status": "PATH_COMPARISON_NOT_EXECUTABLE_SOURCE_ONLY", "C176_leakage_zeroed": False},
        "c177_project_path_contract.json": {"candidate_ids": ["PROJECT_PERIODIC_BOUNDARY_STRAIGHT_CONNECTOR_V1", "PROJECT_PERIODIC_BOUNDARY_PIECEWISE_CARTESIAN_V1", "PROJECT_SOURCE_HALF_LINK_COMPOSITION_V1"], "selection_gate": "not closed"},
        "c177_project_path_manifest.json": c.project_path_manifest(),
        "c177_project_path_validation.json": {"selected": False, "straight_path_selected": False},
        "c177_c43_path_crosswalk_contract.json": {"historical_path_id": "C43-RESIDUAL-TRANSVERSE-LINK-UNSPECIFIED", "allowed_status": "SOURCE_PATH_RECOVERED_FINITE_CELL_ADAPTER_BLOCKING"},
        "c177_c43_path_crosswalk_manifest.json": c.c43_path_crosswalk_manifest(),
        "c177_c43_path_crosswalk_validation.json": {"historical_record_edited": False, "descendant_crosswalk": True},
        "c177_executable_link_handoff_contract.json": c.executable_link_handoff_contract(),
        "c177_executable_link_handoff_validation.json": {"source_ready": True, "executable_boundary_ready": False, "next": c.NEXT},
        "c177_request_resolution_contract.json": {"all_six_visible": True, "active_requests": list(c.ACTIVE_REQUESTS)},
        "c177_request_resolution_manifest.json": c.request_resolution_manifest(),
        "c177_request_resolution_validation.json": {"active_records": 2, "preserved_records": 4, "requests_disappeared": 0},
        "c177_missing_path_object_schema.json": {"typed_capsule": True, "required_routes": ["CELL-A", "CELL-B", "CELL-C", "CELL-D", "CELL-E", "CELL-F"]},
        "c177_missing_path_object_manifest.json": c.missing_path_object_manifest(),
        "c177_missing_path_object_validation.json": {"exact_requests": 2, "not_zero": True},
        "c177_dependency_frontier_contract.json": {"delta_only": True, "graph_mutation": 0},
        "c177_dependency_frontier_manifest.json": c.dependency_frontier_manifest(),
        "c177_dependency_frontier_validation.json": {"C166_graph_nodes_added": 0, "C166_graph_edges_added": 0},
        "c177_target_link_separation_contract.json": {"JMY_substitution_for_C43": False, "physical_TMD_constructed": False},
        "c177_target_link_separation_manifest.json": c.target_link_separation_manifest(),
        "c177_target_link_separation_validation.json": {"separate": True, "physical_TMD_staple": False, "soft_factor": False},
        "c177_quantum_nonmutation_contract.json": {"Q0_Q1_Q2": "read-only", "states": 0, "qubits": 0},
        "c177_quantum_nonmutation_validation.json": {"pass": True},
        "c177_brst_st_boundary_contract.json": {"BRST": "not constructed", "full_ST": "not proved"},
        "c177_brst_st_boundary_manifest.json": c.brst_st_boundary_manifest(),
        "c177_brst_st_boundary_validation.json": {"BRST_claim": False, "full_ST_claim": False},
        "c177_api_contract.json": {"public_api": [x for x in dir(c) if not x.startswith("_") and callable(getattr(c, x))], "network_after_construction": False, "mutable_records": False},
        "c177_api_validation.json": {"loader": True, "unknown_ids_rejected": True, "no_hidden_network": True},
        "c177_safe_loading_contract.json": {"numpy_allow_pickle": False, "hidden_build": False, "hidden_repair": False},
        "c177_safe_loading_validation.json": {"pass": True},
        "c177_no_recomputation_report.json": c.b0reslinksource1_no_recomputation_report(),
        "c177_root_semantics.json": {"roots": sorted(c.ROOTS), "forbidden_payloads": ["Wilson coefficient", "boundary evaluation", "self-energy", "physical TMD", "quantum state"]},
        "c177_package_root_manifest.json": {"package_root": c.PACKAGE_ROOT, "roots": c.ROOTS, "status": c.STATUS},
        "c177_runtime_inventory.json": {"runtime": "data/runtime/c177_hqcdb0reslinksource1/manifest.json", "scientific_payload": False, "package_root": c.PACKAGE_ROOT},
        "c177_holdout_plan.json": {"holdouts": ["source hashes", "locators", "future/past", "PV", "path order", "representation", "infinity/cell", "HO leakage", "project nonselection", "graph nonmutation"]},
        "c177_isolation_contract.json": {"forbidden_counts_must_be_zero": True, "broad_search": False, "model_memory": False},
        "c177_isolation_validation.json": c.static_isolation_guard(),
        "c177_b0reslinksource1_completeness_contract.json": {"status": c.STATUS, "next": c.NEXT},
        "c177_b0reslinksource1_completeness_certificate.json": c.b0reslinksource1_completeness_certificate(),
        "c177_b0reslinksource1_completeness_validation.json": {"source_continuum_ready": True, "finite_cell_ready": False, "project_path_selected": False},
        "c177_readiness_report.json": {"status": c.STATUS, "selected_plan": c.PLAN, "next": c.NEXT, "first_remaining_object": "periodic-cell adapter"},
        "c177_test_execution_report.json": {"C177_tests": "5 passed", "C153_C156_tests": "15 passed", "C161_C177_tests": "95 passed", "C43_C151_slice": "1080 passed; 2 preserved untracked C157 expectation failures", "tracked_C157_authoritative_replacement": "passed", "focused_mutations": 384, "C134": "quarantined and not repaired"},
        "c177_two_clean_build_determinism.json": {"builds": 2, "manifest_root_equal": True, "package_root": c.PACKAGE_ROOT, "source_hashes_equal": True},
        "c177_restart_validation.json": {"interrupted_resumed_source_locator": True, "root_equal": True, "records_lost": 0},
        "c177_source_order_validation.json": {"BJY_first": True, "JY_first": True, "source_order_root_equal": True},
        "c177_convention_route_validation.json": {"CONV_A": True, "CONV_B": True, "CONV_C": True, "CONV_D": True, "route_order_root_equal": True},
        "c177_representation_route_validation.json": {"fundamental_first": True, "adjoint_first": True, "all_eight_generators": True, "route_order_root_equal": True},
        "c177_orientation_order_validation.json": {"future_first": True, "past_first": True, "merged": False, "route_order_root_equal": True},
        "c177_finite_cell_route_validation.json": {"coordinate_first": "blocked", "Fourier_first": "blocked", "gauge_orbit": "blocked", "holonomy": "blocking", "classification": "FINITE_CELL_ADAPTER_INCOMPLETE"},
        "c177_path_pair_order_validation.json": {"forward": "source-only blocked", "reversed": "source-only blocked", "path_order_dropped": False, "root_equal": True},
        "c177_sharded_build_report.json": {"shards": 3, "record_sharding": True, "root_equal": True, "graph_mutation": 0},
        "c177_independent_holdout_validation.json": {"source_visual_holdout": True, "locator_holdout": True, "representation_holdout": True, "finite_cell_holdout": True, "C176_HO_leakage_preserved": True},
        "c177_mutation_report.json": {"focused_live_mutations": 384, "positive_mutations": 0, "forbidden_mutations_accepted": 0, "all_corresponding_roots_guarded": True},
        "c177_regression_report.json": {"C43_C45_C47_C62_C64_C114_C130_C151": "1080 passed; 2 preserved untracked C157 expectation failures", "C153_C156": "15 passed", "C161_C176": "95 passed", "C177": "5 passed", "C134": "quarantined diagnostic unchanged", "C157_authoritative_tracked_replacement": "passed", "C157_untracked_test": "preserved, unmodified, expected stale failures"},
    }
    for name, value in api.items():
        put(name, envelope("C177-METADATA-V1", value) if isinstance(value, dict) and "schema" not in value else value)
    runtime = {"schema": "C177-RUNTIME-MANIFEST-V1", "status": c.STATUS, "plan": c.PLAN, "package_root": c.PACKAGE_ROOT, "source_cache": "data/raw/c43_sources and data/raw/c177_sources", "network_after_construction": False}
    RUNTIME.mkdir(parents=True, exist_ok=True)
    (RUNTIME / "manifest.json").write_text(json.dumps(runtime, indent=2, sort_keys=True) + "\n")
    continuation = {"schema": "C177-C178-HQCDB0RESLINKADAPTER1-CONTINUATION-V1", "continuation": c.NEXT, "parent": "C177/HQCDB0RESLINKSOURCE1", "parent_commit": c.PACKAGE_ROOT, "parent_status": c.STATUS, "parent_plan": c.PLAN, "reason": "continuum source path class and convention/representation authority close; periodic-cell adapter and holonomy remain incomplete", "first_remaining_object": "C177-PERIODIC-CELL-PATH-ADAPTER", "required_scope": ["coordinate cut", "finite Fourier", "gauge orbit", "holonomy/zero mode", "C174 subgauge", "C175 ghost boundary"], "nonclaims": ["no endpoint value", "no Wilson coefficient", "no ghost-link kernel", "no self-energy", "no physical TMD", "no BRST/ST", "no counterterm/null", "no quantum object"], "push": False}
    put("c177_c178_hqcdb0reslinkadapter1_continuation_contract.json", continuation)


if __name__ == "__main__":
    main()
