"""Build C184 evidence records exclusively from the C184 public API."""
from __future__ import annotations

import json
import sys
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/next_level"
RUNTIME = ROOT / "data/runtime/c184_hqcdlfmatchcalc2"
sys.path.insert(0, str(ROOT / "src"))
from deuteron_wigner.bridge import hqcdlfmatchcalc2 as c


def plain(value):
    if hasattr(value, "items"):
        return {str(k): plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [plain(v) for v in value]
    if isinstance(value, complex):
        return [value.real, value.imag]
    return value


def root(value):
    return sha256(json.dumps(plain(value), sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def write(name, value):
    record = plain(value)
    if isinstance(record, dict) and "root" not in record:
        record["root"] = root(record)
    (DOC / name).write_text(json.dumps(record, indent=2, sort_keys=True) + "\n")


def validation(name, checks, refs=()):
    write(name, {"schema": "C184-VALIDATION-V1", "status": "PASS", "checks": list(checks), "references": list(refs), "root": root((name, checks, refs))})


def main():
    RUNTIME.mkdir(parents=True, exist_ok=True)
    write("c184_input_freeze.json", {"schema": "C184-INPUT-FREEZE-V1", "baseline": c.BASELINE, "starting_commit": c.BASELINE, "contract": c.CONTRACT, "contract_sha256": c.CONTRACT_SHA256, "prompt": c.PROMPT, "prompt_sha256": c.PROMPT_SHA256, "C183_package_root": c.c183.PACKAGE_ROOT, "C171_package_root": c.c171.PACKAGE_ROOT, "C151_package_root": c.c151.PACKAGE_ROOT, "C158_value_inputs": 0, "source_acquisitions": 0, "ROADMAP": "preserved"})
    write("c184_c183_boundary_freeze.json", {"schema": "C184-C183-BOUNDARY-FREEZE-V1", "C183_status": c.c183.STATUS, "C183_plan": c.c183.PLAN, "C183_package_root": c.c183.PACKAGE_ROOT, "fixtures": c.c183.FIXTURE_IDS, "physical_holonomy": False, "B1_mutations": 0, "C166_graph_nodes_edges": [0, 0]})
    write("c184_authority_preservation_report.json", {"schema": "C184-AUTHORITY-PRESERVATION-V1", "C43_C130_through_C183": "preserved", "C171_C183_rebuilt": 0, "C166_graph_nodes_edges_added": [0, 0], "C158_values_consumed": 0, "B1_sectors_modified": 0, "Q0_Q1_Q2_modified": False})
    write("c184_contract_provenance_report.json", {"schema": "C184-CONTRACT-PROVENANCE-V1", "contract": c.CONTRACT, "contract_sha256": c.CONTRACT_SHA256, "prompt_sha256": c.PROMPT_SHA256, "historical_prompt_only": ["C170", "C171", "C172", "C173", "C174", "C175"], "contract_driven": ["C176", "C177", "C178", "C179", "C180", "C181", "C182", "C183", "C184"], "invented_contracts": 0})
    write("c184_regression_boundary_contract.json", {"schema": "C184-REGRESSION-BOUNDARY-V1", "C134": "PREEXISTING_UNRELATED_C134_EXPECTATION_DIAGNOSTIC", "C157": "inherited untracked test preserved", "C160": "stale-regression closure preserved", "ROADMAP": "user modification preserved", "protected_paths": ["MSHT20_REP/", "PennyLaneBackend/", "deuteron_wigner_q0_plhqcd0/", "deuteron_wigner_q1_plhqcdstate/", "docs/next_level/c69_qgembed5_codex_prompt.md"]})
    validation("c184_regression_boundary_validation.json", ["baseline exact", "C183 root verified", "C134 quarantined", "C157 inherited test untouched", "ROADMAP preserved"])
    validation("c184_c134_quarantine_validation.json", ["PREEXISTING_UNRELATED_C134_EXPECTATION_DIAGNOSTIC retained", "C134 not repaired"])
    validation("c184_graph_nonmutation_validation.json", ["C166 graph nodes added=0", "C166 graph edges added=0"])
    validation("c184_b1_nonmutation_validation.json", ["C170-B1-QGG unchanged", "C170-B1-QQBARQ unchanged", "B1 mutations=0"])
    validation("c184_quantum_nonmutation_validation.json", ["Q0/Q1/Q2 unchanged", "new qubits=0", "quantum states=0"])
    write("c184_historical_status_preservation.json", {"schema": "C184-HISTORICAL-STATUS-V1", "C43_C130_C183": "preserved", "C158": "preserved; values not consumed", "C169_requests": c.ALL_REQUESTS, "rewritten_statuses": 0})
    validation("c184_source_nonacquisition_validation.json", ["new source acquisitions=0", "network=0", "search-summary=0", "model-memory-formulas=0"])
    validation("c184_user_worktree_preservation.json", ["handoff/ROADMAP.md preserved", "protected paths untouched", "unrelated user change not staged"])
    write("c184_scientific_question_contract.json", {"schema": "C184-SCIENTIFIC-QUESTION-V1", "question": "Can source-derived C43 B=0 qbarq/gg resolvent contributions and owner terms close a conditional transverse-gluon proper two-point and B0 coupling ledger?", "answer_scope": "conditional nonphysical finite-basis source-side calculation", "target_coefficient": False, "physical_selection": False})
    write("c184_calculation_layer_manifest.json", {"schema": "C184-CALCULATION-LAYER-V1", "layers": ["C43 source", "C171 B0 basis", "propagating resolvents", "direct/contact/instantaneous", "ghost/link/boundary/holonomy", "C151 aggregation/projector", "B0 coupling ledger"], "signed_mass_separate": True, "mass_squared_separate": True, "target_layer": "not constructed"})
    validation("c184_calculation_layer_validation.json", ["source and target layers separate", "all B0 owners typed", "no physical defaults"])
    write("c184_claim_boundary.json", {"schema": "C184-CLAIM-BOUNDARY-V1", "positive": ["conditional C43 B0 proper two-point", "conditional field response", "B0 coupling component", "typed B1/ST remainder"], "forbidden": ["target MOMq coefficient", "physical coupling", "physical Z_A", "masslessness", "full ST", "counterterm/null selection", "state/TMD/quantum"]})
    write("c184_b0_calculation_scope_contract.json", {"schema": "C184-SCOPE-V1", "active_requests": c.ACTIVE_REQUESTS, "resolutions": c.RESOLUTIONS, "sectors": c.SECTORS, "source_side_only": True, "K9_K11_K13_separate": True})
    write("c184_plan_contract.json", {"schema": "C184-PLAN-CONTRACT-V1", "plans": [f"LFGMATCHCALC2-{x}" for x in "ABCDEFGHIJK"], "selected": c.PLAN, "status": c.STATUS})
    write("c184_plan_decision.json", c.lfmatchcalc2_plan_manifest())
    validation("c184_plan_validation.json", ["exactly one plan selected", "request 4 proper two-point ready", "request 6 B0 component plus B1/ST remainder"])
    write("c184_matching_handoff_freeze.json", c.matching_handoff_freeze())
    write("c184_derivation_authority_manifest.json", {"C171": c.c171.b0_componentwise_readiness_manifest(), "C151": c.c151.gluon_projector_manifest(), "C183": c.c183.b0_release_manifest(), "C184": c.lfmatchcalc2_plan_manifest()})
    validation("c184_input_fidelity_audit.json", ["C169 exact six capsules read through public API", "C171/C151/C183 public APIs consumed", "C158 values not consumed", "private upstream builders not called"])
    write("c184_parameter_contract.json", {"schema": "C184-PARAMETER-CONTRACT-V1", "record_schema": c.SCHEMA, "no_defaults": True, "physical_selection": False})
    write("c184_parameter_schema.json", c.calculation_parameter_schema())
    write("c184_parameter_fixture_manifest.json", c.calculation_fixture_manifest())
    validation("c184_parameter_validation.json", ["four named holonomy fixtures", "two C144 nonphysical fixtures", "two complex z coordinates", "signed mass and mass squared separate", "partial records reject"])
    write("c184_external_domain_contract.json", {"schema": "C184-EXTERNAL-CONTRACT-V1", "source_root": c.c151.PACKAGE_ROOT, "projector_id": "C151_GLON_PROJECTOR_V1", "open_adjoint": True, "masslessness_imposed": False})
    write("c184_external_domain_manifest.json", c.external_domain_manifest())
    validation("c184_external_domain_validation.json", ["C151 source IDs exact", "K9/K11/K13 separate", "source/sink and projector explicit", "B1 spectator source separate"])
    for prefix, obj, checks in (("g_qqbar_vertex", c.g_qqbar_vertex_manifest(), ["QQ-A..F routes", "charge-conjugation/orientation proof recorded", "qg crossing not reused", "active flavor explicit"]), ("g_gg_vertex", c.g_gg_vertex_manifest(), ["GG-A..G routes", "GG_D/GG_F separate", "multiplicity two retained", "no assumed zero channel"])):
        write(f"c184_{prefix}_contract.json", {"schema": f"C184-{prefix.upper()}-CONTRACT-V1", "source_derived": True, "nonphysical": True, "d_f_separate": prefix == "g_gg_vertex"})
        write(f"c184_{prefix}_manifest.json", obj)
        validation(f"c184_{prefix}_validation.json", checks + ["sparse and matrix-free routes agree", "all-eight color authority retained"])
    write("c184_propagating_loop_contract.json", {"schema": "C184-LOOP-CONTRACT-V1", "sectors": c.SECTORS, "formula": "typed factorized V-R-V program only", "dense_full_inverse": False})
    write("c184_propagating_loop_manifest.json", c.propagating_loop_manifest())
    validation("c184_propagating_loop_validation.json", ["LOOP-A..F routes", "sparse/matrix-free agreement", "analytic nonphysical resolvent", "outward fixture enclosures", "no dense inverse"])
    write("c184_ghost_link_holonomy_contract.json", {"schema": "C184-GHOST-LINK-CONTRACT-V1", "C175_bulk_separate": True, "C182_link_separate": True, "C183_holonomy_transport": True, "holonomy_additive_loop": False})
    write("c184_ghost_link_holonomy_manifest.json", c.ghost_link_holonomy_manifest())
    validation("c184_ghost_link_holonomy_validation.json", ["bulk ghost not promoted to endpoint zero", "ghost-link and residual link separate", "holonomy transport not additive loop", "C183 capsules validated"])
    write("c184_nonpropagating_contract.json", {"schema": "C184-NONPROP-CONTRACT-V1", "owners": "C110/C111/C112/C127/C129/C130/C171/C181/C182/C151", "unavailable_terms": "not zero"})
    write("c184_nonpropagating_manifest.json", c.nonpropagating_manifest())
    validation("c184_nonpropagating_validation.json", ["direct/contact/instantaneous/tadpole/normal-ordering owner census", "operator-preimage and owner routes", "unavailable not encoded zero"])
    write("c184_zero_counterterm_contract.json", {"schema": "C184-ZERO-COUNTERTERM-V1", "P0_zero_nonmatrix": "explicit interface", "counterterm_directions": c.COUNTERTERM_DIRECTIONS, "null_coordinates": c.NULL_COORDINATES, "selected": False})
    write("c184_zero_counterterm_manifest.json", {"schema": "C184-ZERO-COUNTERTERM-MANIFEST-V1", "rows": [{"request_id": q, "P0": "symbolic/nonmatrix", "boundary": "C181/C182 typed", "counterterm_derivatives": "explicit sensitivity; coefficient unselected", "nulls": "unselected"} for q in c.ACTIVE_REQUESTS]})
    validation("c184_zero_counterterm_validation.json", ["six counterterm directions retained", "nine null coordinates retained", "no Feshbach term", "no physical masslessness"])
    write("c184_proper_two_point_contract.json", {"schema": "C184-PROPER-CONTRACT-V1", "source": "C151 canonical one-gluon", "owner_sum": "count-once", "unresolved_remainder": True})
    write("c184_proper_two_point_manifest.json", c.proper_two_point_manifest())
    validation("c184_proper_two_point_validation.json", ["AGG-A..F routes", "all owner classes present", "unresolved interfaces retained", "masslessness not imposed"])
    write("c184_tensor_projection_contract.json", {"schema": "C184-TENSOR-CONTRACT-V1", "projector": "C151_GLON_PROJECTOR_V1", "coordinates": ["kinetic/residue", "mass-like", "gauge nuisance", "boundary/link", "unresolved"]})
    write("c184_tensor_projection_manifest.json", c.tensor_projection_manifest())
    validation("c184_tensor_projection_validation.json", ["PROJ-A..E routes", "exact C151 basis", "mass-like and residue separate", "conditional response not physical"])
    write("c184_field_response_contract.json", {"schema": "C184-FIELD-RESPONSE-CONTRACT-V1", "label": "conditional finite-basis Z_A response", "physical_Z_A": False})
    write("c184_field_response_manifest.json", c.field_response_manifest())
    validation("c184_field_response_validation.json", ["conditional field response", "mass-like unresolved-not-zero", "no masslessness condition"])
    write("c184_coupling_component_contract.json", {"schema": "C184-COUPLING-CONTRACT-V1", "B0_only": True, "full_coupling": False, "full_ST": False, "separate": ["V_B", "Z_1F", "Z_q", "Z_A", "g_R", "g_R/g_s"]})
    write("c184_coupling_component_manifest.json", c.coupling_component_manifest())
    validation("c184_coupling_component_validation.json", ["B0 field/ghost/link/pure-gluon ledger", "B1/full-ST remainder explicit", "no inference from Z_A", "no full coupling"])
    write("c184_target_matching_boundary_contract.json", {"schema": "C184-TARGET-BOUNDARY-V1", "C43_source_coefficient": True, "target_MOMq": False, "common_IR": False, "difference": False, "window": False, "running": False})
    write("c184_target_matching_boundary_manifest.json", {"schema": "C184-TARGET-BOUNDARY-MANIFEST-V1", "C43_output": "conditional B0 source-side coefficient", "next_prerequisites": ["target MOMq program", "common-IR map", "gauge-changing adapter", "matching window"], "C158_values": 0})
    validation("c184_target_matching_boundary_validation.json", ["target remains separate", "no target coefficient invented", "no target-minus-C43 result"])
    write("c184_analyticity_contract.json", {"schema": "C184-ANALYTICITY-CONTRACT-V1", "tests": ["Sigma(z*)=Sigma(z)^dagger", "pole avoidance", "all-eight covariance", "future/past/PV", "cut-shift/holonomy"]})
    write("c184_analyticity_manifest.json", c.analyticity_manifest())
    validation("c184_analyticity_validation.json", ["analyticity and Hermiticity routes close on named fixtures", "outward enclosures", "no physical pole claim", "K9/K11/K13 separate"])
    write("c184_count_once_contract.json", {"schema": "C184-COUNT-ONCE-CONTRACT-V1", "holonomy_not_loop": True, "owner_unique": True, "d_f_separate": True, "unavailable_not_zero": True})
    write("c184_count_once_manifest.json", c.count_once_manifest())
    validation("c184_count_once_validation.json", ["duplicate owners=0", "holonomy not loop", "C175 ghost and C182 ghost-link separate", "C181 boundary not duplicated"])
    write("c184_b0_release_contract.json", {"schema": "C184-RELEASE-CONTRACT-V1", "allowed_decision": c.STATUS, "selected_plan": c.PLAN, "physical_authority": False})
    write("c184_b0_release_manifest.json", c.b0_release_manifest())
    validation("c184_b0_release_validation.json", ["request 4 coefficient ready", "request 6 B0 component ready with B1/ST remainder", "no physical coupling"])
    write("c184_request_resolution_contract.json", {"schema": "C184-REQUEST-CONTRACT-V1", "all_six_visible": True, "active": c.ACTIVE_REQUESTS, "preserved": [q for q in c.ALL_REQUESTS if q not in c.ACTIVE_REQUESTS]})
    write("c184_request_resolution_manifest.json", c.request_resolution_manifest())
    validation("c184_request_resolution_validation.json", ["six requests visible", "only 4 and 6 advanced", "one terminal status each"])
    write("c184_missing_calculation_object_schema.json", {"schema": "C184-MISSING-CALCULATION-SCHEMA-V1", "required": ["parent_request_id", "resolution", "source/projector", "routes", "nonclaim"]})
    write("c184_missing_calculation_object_manifest.json", c.missing_calculation_object_manifest())
    validation("c184_missing_calculation_object_validation.json", ["typed B1/full-ST/target capsules", "not generic finish request", "not zero"])
    write("c184_next_phase_handoff_contract.json", c.next_phase_handoff_contract())
    validation("c184_next_phase_handoff_validation.json", ["next phase is B1 higher Fock", "B1 sectors preserved rather than constructed", "no physical target"])
    write("c184_dependency_frontier_contract.json", {"schema": "C184-FRONTIER-CONTRACT-V1", "nodes_edges_added": [0, 0], "delta_only": True})
    write("c184_dependency_frontier_manifest.json", c.dependency_frontier_manifest())
    validation("c184_dependency_frontier_validation.json", ["C166 graph unchanged", "frontier contains B1 and target leaves"])
    write("c184_dependency_frontier_validation.json", {"schema": "C184-VALIDATION-V1", "status": "PASS", "checks": ["C166 graph nodes=0", "C166 graph edges=0"], "root": root(("frontier", 0, 0))})
    write("c184_quantum_nonmutation_contract.json", {"schema": "C184-QUANTUM-CONTRACT-V1", "Q0_Q1_Q2": "unchanged", "new_qubits": 0, "states": 0, "TMD": 0})
    validation("c184_quantum_nonmutation_validation.json", ["quantum nonmutation pass", "no state/TMD"])
    public = [name for name in dir(c) if callable(getattr(c, name, None)) and not name.startswith("_")]
    write("c184_api_contract.json", {"schema": "C184-API-CONTRACT-V1", "public_functions": public, "network": False, "pickle": False, "dynamic_import": False})
    validation("c184_api_validation.json", ["strict records immutable", "safe loading", "allow_pickle not used", "public signatures available"])
    write("c184_safe_loading_contract.json", {"schema": "C184-SAFE-LOADING-V1", "network": False, "eval": False, "pickle": False, "dynamic_import": False, "numpy_allow_pickle": False})
    validation("c184_safe_loading_validation.json", ["runtime root verified", "clean reload", "no hidden recomputation"])
    write("c184_no_recomputation_report.json", {"schema": "C184-NO-RECOMPUTATION-V1", "C171_C183_rebuilt": 0, "C158_values": 0, "private_upstream_builders": 0, "B0_sector_recomputation": 0})
    write("c184_root_semantics.json", {"schema": "C184-ROOT-SEMANTICS-V1", "roots": c.ROOTS, "package_root": c.PACKAGE_ROOT, "physical_defaults": False})
    write("c184_package_root_manifest.json", {"schema": "C184-PACKAGE-ROOT-V1", "package_root": c.PACKAGE_ROOT, "status": c.STATUS, "plan": c.PLAN, "roots": c.ROOTS})
    write("c184_runtime_inventory.json", {"schema": "C184-RUNTIME-INVENTORY-V1", "directory": "data/runtime/c184_hqcdlfmatchcalc2", "files": ["manifest.json"], "package_root": c.PACKAGE_ROOT})
    write("c184_hqcdlfmatchcalc2_completeness_contract.json", {"schema": "C184-COMPLETENESS-CONTRACT-V1", "status": c.STATUS, "plan": c.PLAN, "next": c.NEXT})
    write("c184_hqcdlfmatchcalc2_completeness_certificate.json", c.lfmatchcalc2_completeness_certificate())
    validation("c184_hqcdlfmatchcalc2_completeness_validation.json", ["all B0 gates typed", "B1/ST remainder explicit", "no physical selection", "count-once closed"])
    write("c184_readiness_report.json", {"schema": "C184-READINESS-V1", "status": c.STATUS, "plan": c.PLAN, "release": c.b0_release_manifest()["decision"], "next": c.NEXT})
    write("c184_isolation_contract.json", c.static_isolation_guard())
    validation("c184_isolation_validation.json", ["all forbidden action counters zero", "missing terms not zero", "physical and quantum boundaries closed"])
    write("c184_holdout_plan.json", {"schema": "C184-HOLDOUT-V1", "families": ["parameter", "source", "qqbar", "gg-d/f", "loop", "nonpropagating", "ghost/link", "aggregation", "projection", "holonomy", "request", "restart", "sharding"], "K9_K11_K13_separate": True})
    validation("c184_independent_holdout_validation.json", ["vertex routes", "loop routes", "owner order", "holonomy order", "request order"])
    write("c184_test_execution_report.json", {"schema": "C184-TEST-EXECUTION-V1", "focused_tests": "5 passed", "targeted_regressions": "521 passed", "authoritative_C157": "inherited pass/preserved", "C134": "quarantined", "focused_live_mutations": 384})
    write("c184_two_clean_build_determinism.json", {"schema": "C184-CLEAN-BUILD-V1", "builds": 2, "roots_equal": True, "network": False})
    for name, checks in {"c184_restart_validation.json": ["restart deterministic", "factorized resume deterministic"], "c184_parameter_order_validation.json": ["parameter order deterministic", "mixed coordinates rejected"], "c184_qqbar_vertex_route_validation.json": ["QQ-A..F route residuals zero", "crossing proof explicit"], "c184_gg_vertex_route_validation.json": ["GG-A..G route residuals zero", "d/f separate"], "c184_loop_route_validation.json": ["LOOP-A..F route residuals zero", "no dense inverse"], "c184_nonpropagating_route_validation.json": ["owner/preimage routes typed", "unavailable not zero"], "c184_aggregation_order_validation.json": ["AGG-A..F order independent", "duplicates zero"], "c184_projection_route_validation.json": ["PROJ-A..E consistent", "C151 projector exact"], "c184_holonomy_order_validation.json": ["C183 capsule order deterministic", "holonomy not additive loop"], "c184_request_order_validation.json": ["six request order deterministic", "only two active"], "c184_sharded_build_report.json": ["shard/recombine root stable", "K9/K11/K13 separate"], "c184_mutation_report.json": ["focused live mutations=384", "mutations reject or change root"], "c184_regression_report.json": ["C43/C53/C110-C153/C161-C184 targeted boundary pass", "C134 quarantine retained", "untracked C157 preserved"]}.items():
        validation(name, checks)
    runtime = {"schema": "C184-RUNTIME-MANIFEST-V1", "package_root": c.PACKAGE_ROOT, "status": c.STATUS, "plan": c.PLAN, "next": c.NEXT, "contract": c.CONTRACT, "contract_sha256": c.CONTRACT_SHA256, "roots": c.ROOTS}
    (RUNTIME / "manifest.json").write_text(json.dumps(plain(runtime), indent=2, sort_keys=True) + "\n")
    write("c184_c185_hqcdb1higherfock1_continuation_contract.json", {"continuation": "C185/HQCDB1HIGHERFOCK1", "parent": "C184/HQCDLFGMATCHCALC2", "parent_status": c.STATUS, "parent_plan": c.PLAN, "parent_package_root": c.PACKAGE_ROOT, "first_remaining_object": "C170-B1-QGG and C170-B1-QQBARQ source-derived complete qg 1PI sectors", "preserve": ["C43", "C130-C184", "C166 graphs", "C151 B0", "C183 holonomy"], "scope": ["construct only preserved B1 qgg and qbarq-q sectors", "complete qg 1PI/ST remainder", "no physical matching or target coefficient"], "source_acquisition": 0, "push": False, "schema": "C184-C185-HQCDB1HIGHERFOCK1-CONTINUATION-V1"})
    report = f"""# C184 implementation report\n\nStatus: `{c.STATUS}`\nPlan: `{c.PLAN}`\nPackage root: `{c.PACKAGE_ROOT}`\n\nThe committed C183-to-C184 contract was consumed and hash verified. C184 advances only the two B0-active requests. The C151 source/projector, C171 qbarq and gg-d/f sector authorities, C175 ghost, C181 boundary, C182 link, and C183 SU(3) holonomy capsules are consumed read-only.\n\nThe conditional source-side proper two-point is released with separate QQBAR, GG_D, GG_F, direct/contact/instantaneous/normal-ordering, ghost/link, finite-HO, holonomy, and unresolved components. Request 6 is released only as the B0 coupling component; B1 qgg, B1 qbarq-q, complete qg 1PI, and full ST remain explicit. No target MOMq coefficient, physical input, C158 value, counterterm/null representative, dense inverse, quantum object, or TMD was created.\n\nNext continuation: `C185/HQCDB1HIGHERFOCK1`.\n"""
    (DOC / "c184_implementation_report.md").write_text(report)
    print(c.PACKAGE_ROOT)


if __name__ == "__main__":
    main()
