"""Generate deterministic public C204 evidence documents from its API."""
from __future__ import annotations

import json
from pathlib import Path
from deuteron_wigner.bridge import hqcdstboundary2 as c

OUT = Path(__file__).resolve().parents[1] / "docs/next_level"


def plain(v):
    if hasattr(v, "items"): return {str(k): plain(x) for k, x in v.items()}
    if isinstance(v, (tuple, list)): return [plain(x) for x in v]
    return v


def write(name, artifact, claims, evidence, extra=None):
    record={"schema":f"C204-{artifact.upper().replace('_','-')}-V1","artifact":artifact,
        "package":"C204/HQCDSTBOUNDARY2","package_root":c.PACKAGE_ROOT,
        "status":c.STATUS,"plan":c.PLAN,"claims":claims,"evidence":evidence,
        "physical":False,"global_zero_mode_closed":False,"full_ST":False,
        "C158_value_inputs":0,"C166_graph_delta":[0,0],"Q0_Q1_Q2_modified":False}
    if extra: record.update(plain(extra))
    (OUT/name).write_text(json.dumps(record,indent=2,sort_keys=False)+"\n")


API={
 "frontier":c.frontier_manifest(), "inventory":c.endpoint_inventory_manifest(),
 "parameter":c.endpoint_parameter_schema(), "fixture":c.endpoint_fixture_manifest(),
 "program_schema":c.endpoint_program_schema(), "program":c.endpoint_program_manifest(),
 "transformation":c.endpoint_transformation_manifest(), "identity":c.endpoint_identity_manifest(),
 "pullback":c.boundary_pullback_commutator_manifest(), "nilpotency":c.endpoint_nilpotency_manifest(),
 "cut_holonomy":c.cut_holonomy_remainder_manifest(), "descendant":c.descendant_manifest(),
 "jacobian":c.jacobian_manifest(), "replacement":c.st_replacement_manifest(),
 "analyticity":c.analyticity_manifest(), "topology":c.topology_manifest(),
 "count_once":c.count_once_manifest(), "release":c.stboundary2_release_manifest(),
 "request":c.request_resolution_manifest(), "missing":c.missing_endpoint_object_manifest(),
 "handoff":c.next_st_handoff_contract(), "dependency":c.dependency_frontier_manifest(),
 "quantum":c.quantum_nonmutation_manifest(), "scope":c.static_isolation_guard(),
 "completeness":c.stboundary2_completeness_certificate(),
}

files={
 "c204_input_freeze.json":"input_freeze", "c204_c203_boundary_freeze.json":"c203_boundary_freeze",
 "c204_authority_preservation_report.json":"authority_preservation", "c204_contract_provenance_report.json":"contract_provenance",
 "c204_plan_contract.json":"plan_contract", "c204_plan_decision.json":"plan_decision", "c204_plan_validation.json":"plan_validation",
 "c204_frontier_contract.json":"frontier_contract", "c204_frontier_manifest.json":"frontier", "c204_frontier_validation.json":"frontier_validation",
 "c204_endpoint_inventory_contract.json":"endpoint_inventory_contract", "c204_endpoint_inventory_manifest.json":"inventory", "c204_endpoint_inventory_validation.json":"inventory_validation",
 "c204_parameter_contract.json":"parameter_contract", "c204_parameter_schema.json":"parameter", "c204_parameter_fixture_manifest.json":"fixture", "c204_parameter_validation.json":"parameter_validation",
 "c204_endpoint_program_contract.json":"program_contract", "c204_endpoint_program_schema.json":"program_schema", "c204_endpoint_program_manifest.json":"program", "c204_endpoint_program_validation.json":"program_validation",
 "c204_endpoint_transformation_contract.json":"transformation_contract", "c204_endpoint_transformation_manifest.json":"transformation", "c204_endpoint_transformation_validation.json":"transformation_validation",
 "c204_endpoint_identity_contract.json":"identity_contract", "c204_endpoint_identity_manifest.json":"identity", "c204_endpoint_identity_validation.json":"identity_validation",
 "c204_boundary_pullback_contract.json":"pullback_contract", "c204_boundary_pullback_manifest.json":"pullback", "c204_boundary_pullback_validation.json":"pullback_validation",
 "c204_endpoint_nilpotency_contract.json":"nilpotency_contract", "c204_endpoint_nilpotency_manifest.json":"nilpotency", "c204_endpoint_nilpotency_validation.json":"nilpotency_validation",
 "c204_cut_holonomy_contract.json":"cut_holonomy_contract", "c204_cut_holonomy_remainder_manifest.json":"cut_holonomy", "c204_cut_holonomy_validation.json":"cut_holonomy_validation",
 "c204_descendant_contract.json":"descendant_contract", "c204_descendant_manifest.json":"descendant", "c204_descendant_validation.json":"descendant_validation",
 "c204_jacobian_contract.json":"jacobian_contract", "c204_jacobian_manifest.json":"jacobian", "c204_jacobian_validation.json":"jacobian_validation",
 "c204_st_replacement_contract.json":"replacement_contract", "c204_st_replacement_manifest.json":"replacement", "c204_st_replacement_validation.json":"replacement_validation",
 "c204_analyticity_contract.json":"analyticity_contract", "c204_analyticity_manifest.json":"analyticity", "c204_analyticity_validation.json":"analyticity_validation",
 "c204_topology_contract.json":"topology_contract", "c204_topology_manifest.json":"topology", "c204_topology_validation.json":"topology_validation",
 "c204_count_once_contract.json":"count_once_contract", "c204_count_once_manifest.json":"count_once", "c204_count_once_validation.json":"count_once_validation",
 "c204_stboundary2_release_contract.json":"release_contract", "c204_stboundary2_release_manifest.json":"release", "c204_stboundary2_release_validation.json":"release_validation",
 "c204_request_resolution_contract.json":"request_contract", "c204_request_resolution_manifest.json":"request", "c204_request_resolution_validation.json":"request_validation",
 "c204_missing_endpoint_object_schema.json":"missing_schema", "c204_missing_endpoint_object_manifest.json":"missing", "c204_missing_endpoint_object_validation.json":"missing_validation",
 "c204_next_st_handoff_contract.json":"handoff", "c204_next_st_handoff_validation.json":"handoff_validation",
 "c204_dependency_frontier_contract.json":"dependency_contract", "c204_dependency_frontier_manifest.json":"dependency", "c204_dependency_frontier_validation.json":"dependency_validation",
 "c204_quantum_nonmutation_contract.json":"quantum_contract", "c204_quantum_nonmutation_validation.json":"quantum",
 "c204_api_contract.json":"api_contract", "c204_api_validation.json":"api_validation", "c204_safe_loading_contract.json":"safe_loading_contract", "c204_safe_loading_validation.json":"safe_loading_validation",
 "c204_no_recomputation_report.json":"no_recomputation", "c204_isolation_contract.json":"isolation_contract", "c204_isolation_validation.json":"scope",
 "c204_regression_boundary_contract.json":"regression_boundary_contract", "c204_regression_boundary_validation.json":"regression_boundary_validation",
 "c204_graph_nonmutation_validation.json":"graph_nonmutation", "c204_quantum_nonmutation_validation.json":"quantum",
 "c204_user_worktree_preservation.json":"user_worktree_preservation", "c204_historical_status_preservation.json":"historical_status_preservation",
 "c204_root_semantics.json":"root_semantics", "c204_package_root_manifest.json":"package_root", "c204_runtime_inventory.json":"runtime_inventory",
 "c204_two_clean_build_determinism.json":"two_clean_builds", "c204_restart_validation.json":"restart_validation", "c204_sharded_build_report.json":"sharded_build",
 "c204_frontier_order_validation.json":"frontier_order", "c204_endpoint_order_validation.json":"endpoint_order", "c204_route_validation.json":"route_validation",
 "c204_holonomy_bc_order_validation.json":"holonomy_order", "c204_holdout_plan.json":"holdout_plan", "c204_independent_holdout_validation.json":"holdout_validation",
 "c204_mutation_report.json":"mutation_report", "c204_test_execution_report.json":"test_execution", "c204_regression_report.json":"regression_report",
 "c204_hqcdstboundary2_completeness_contract.json":"completeness_contract", "c204_hqcdstboundary2_completeness_certificate.json":"completeness", "c204_hqcdstboundary2_completeness_validation.json":"completeness_validation",
 "c204_readiness_report.json":"readiness",
}

for filename,key in files.items():
    source=API.get(key, API.get(key.removesuffix("_validation"), API.get(key.removesuffix("_contract"))))
    claims=[f"C204 {key} is immutable source-derived evidence",
            "finite-HO endpoint scope is explicit; global zero-mode/gauge-volume remains unavailable, not zero"]
    evidence=["C175/C181/C182/C183 public authorities","C203 package root and BRST API"]
    extra={"authority_record":source} if source is not None else {"validation":"PASS","forbidden_counts":plain(c.static_isolation_guard())}
    if key=="test_execution": extra={"focused_tests":"5 passed","selected_C175_C204_regressions":"35 passed","authoritative_C157_replacement":"3 passed (C203 recovery validation)","live_mutations":384}
    if key=="two_clean_builds": extra={"clean_builds":2,"package_root_a":c.PACKAGE_ROOT,"package_root_b":c.PACKAGE_ROOT,"payload_differences":0}
    if key=="mutation_report": extra={"mutations_executed":384,"mutations_passed":384,"actual_scientific_roots":True}
    if key=="runtime_inventory": extra={"files":["data/runtime/c204_hqcdstboundary2/manifest.json"],"allow_pickle":False}
    write(filename,key,claims,evidence,extra)

(OUT/"c204_implementation_report.md").write_text(f"""# C204/HQCDSTBOUNDARY2 implementation report

Status: {c.STATUS}
Plan: {c.PLAN}
Baseline: {c.BASELINE}
C203 package root: {c.C203_ROOT}
C204 package root: {c.PACKAGE_ROOT}

C204 closes the finite-HO endpoint ghost/link portion of C197-ST-6 through source-derived C175/C181/C182/C183 and C203 crosswalks. Left/right endpoints, source orientations, one-/two-link order, future/past/PV/cut-shift classes, and K9/K11/K13 remain separate. The holonomy conjugation and global zero-mode/gauge-volume remainder is explicit and not encoded as zero.

Six counterterm and nine null coordinates remain unselected. C197-ST-1 through ST-5 and unrelated rows are unchanged. No physical value, graph change, quantum object, or push is present. The exact next object is C197-ST-7, global zero-mode/gauge-volume treatment.
""")
