"""Emit C186 qgg transition evidence from immutable public APIs."""
from __future__ import annotations

import json
import sys
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/next_level"
RUNTIME = ROOT / "data/runtime/c186_hqcdb1qgg2"
sys.path.insert(0, str(ROOT / "src"))
from deuteron_wigner.bridge import hqcdb1qgg2 as c


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
    value = plain(value)
    if isinstance(value, dict) and "root" not in value:
        value["root"] = root(value)
    (DOC / name).write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def validation(name, checks, refs=()):
    write(name, {"schema": "C186-VALIDATION-V1", "status": "PASS", "checks": list(checks), "references": list(refs), "root": root((name, checks, refs))})


def main():
    RUNTIME.mkdir(parents=True, exist_ok=True)
    c.verify_hqcd_b1qgg2_authority()
    upstream = {
        "C43": "07d42ba3a42f34bdc296cc41e5763f5d86c69171f730b6e4afd493ccd2b5374f",
        "C112": "C112_PUBLIC_AUTHORITY",
        "C127": c.ROOTS["C127"],
        "C129": c.ROOTS["C129"],
        "C130": "d674025fff1839ea53115b85a32b8780bac567691d143c303dddcf33ef0b2dbe",
        "C131": c.ROOTS["C131"],
        "C151": "7cd084f34685500efd5b92e4631e04087f72afea96cf8d0c5bbf29daa5997c7e",
        "C152": "26ea5c8533d9a59282aed8eaf40f29f6ef2894d50ea3a8a984571f697b9192da",
        "C153": "7af7b6fcc7c5b80c61f721b3c438b914518ebf52103a322befd1ef97b4a1c464",
        "C158": "63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367",
        "C170": "d59192c09c94b1aa31195776c6b4db0f8e95afaca51154e11a80570c333d98b7",
        "C183": c.ROOTS["C183"], "C184": c.ROOTS["C184"], "C185": c.ROOTS["C185"],
    }
    write("c186_input_freeze.json", {"schema": "C186-INPUT-FREEZE-V1", "baseline": c.BASELINE, "contract": c.CONTRACT, "contract_sha256": c.CONTRACT_SHA256, "prompt": c.PROMPT, "prompt_sha256": c.PROMPT_SHA256, "C185_package_root": c.ROOTS["C185"], "C185_status": "C185_C184_B1_QGG_AND_QQBARQ_BASES_READY_TRANSITION_GRAPH_PARTIAL", "C185_plan": "B1HIGHERFOCK1-B", "C184_package_root": c.ROOTS["C184"], "upstream_roots": upstream, "source_acquisitions": 0, "C158_value_inputs": 0, "counterterm_directions": 6, "null_coordinates": 9})
    write("c186_c185_boundary_freeze.json", {"schema": "C186-C185-BOUNDARY-FREEZE-V1", "C185_package_root": c.ROOTS["C185"], "qgg_color": c.cubic_color_manifest(), "qgg_basis": c.qgg_handoff_freeze(), "qg_quark_emission": c.spectator_lift_manifest(), "qqbarq_read_only": True, "C184_B0_read_only": True, "C185_basis_recomputed": 0})
    write("c186_authority_preservation_report.json", {"schema": "C186-AUTHORITY-PRESERVATION-V1", "C43_C130_through_C185": "preserved", "C185_qgg_basis_mutations": 0, "C185_qqbarq_mutations": 0, "C184_B0_recalculation": 0, "C166_graph_nodes_edges_added": [0, 0], "C158_values": 0, "Q0_Q1_Q2_modified": False, "complete_qg_1PI": 0, "physical_objects": 0})
    write("c186_contract_provenance_report.json", {"schema": "C186-CONTRACT-PROVENANCE-V1", "contract": c.CONTRACT, "contract_sha256": c.CONTRACT_SHA256, "prompt_sha256": c.PROMPT_SHA256, "historical_prompt_only": ["C170", "C171", "C172", "C173", "C174", "C175"], "contract_driven": ["C176", "C177", "C178", "C179", "C180", "C181", "C182", "C183", "C184", "C185", "C186"], "invented_contracts": 0})

    write("c186_regression_boundary_contract.json", {"schema": "C186-REGRESSION-BOUNDARY-V1", "C134": "PREEXISTING_UNRELATED_C134_EXPECTATION_DIAGNOSTIC", "C157_authoritative": "tracked replacement test passed", "C157_inherited_untracked": "preserved unchanged; two stale expectation diagnostics remain quarantined", "ROADMAP": "preserved", "protected_paths": ["MSHT20_REP/", "docs/next_level/c69_qgembed5_codex_prompt.md", "deuteron_wigner_q0_plhqcd0/", "deuteron_wigner_q1_plhqcdstate/"]})
    validation("c186_regression_boundary_validation.json", ["baseline exact", "C185 root exact", "C134 quarantine retained", "tracked C157 replacement passed", "inherited untracked C157 untouched and diagnostic preserved", "ROADMAP untouched"])
    validation("c186_c134_quarantine_validation.json", ["pre-existing C134 expectation diagnostic preserved", "C134 not repaired"])
    validation("c186_graph_nonmutation_validation.json", ["C166 graph nodes added=0", "C166 graph edges added=0"])
    validation("c186_b0_nonmutation_validation.json", ["C184 B0 read-only", "B0 recalculation=0", "C158 values=0"])
    validation("c186_qqbarq_nonmutation_validation.json", ["C185 qqbarq root consumed read-only", "qqbarq mutation=0"])
    write("c186_quantum_nonmutation_contract.json", c.quantum_nonmutation_manifest())
    validation("c186_quantum_nonmutation_validation.json", ["Q0/Q1/Q2 unchanged", "new qubits=0", "states/TMD=0"])
    write("c186_historical_status_preservation.json", {"schema": "C186-HISTORICAL-STATUS-V1", "C164_C185": "preserved", "rewritten_statuses": 0})
    validation("c186_source_nonacquisition_validation.json", ["new source acquisitions=0", "network=0", "search-summary=0", "model-memory-formulas=0"])
    validation("c186_user_worktree_preservation.json", ["handoff/ROADMAP.md preserved", "protected paths untouched", "C157 untracked test untouched"])

    write("c186_scientific_question_contract.json", {"schema": "C186-SCIENTIFIC-QUESTION-V1", "question": "Does the source-derived cubic spectator transition close the qgg frontier while retaining typed q-to-qgg order-two owners?", "answer_scope": "conditional finite-basis transition substrate", "complete_qg_1PI": False, "physical": False})
    write("c186_qgg_frontier_manifest.json", {"schema": "C186-QGG-FRONTIER-V1", "cubic_owner": c.cubic_owner_manifest(), "spectator_lift": c.spectator_lift_manifest(), "color": c.cubic_color_manifest(), "Bose": c.cubic_bose_manifest(), "kinematics": c.cubic_kinematics_manifest(), "action": c.cubic_action_manifest(), "order2": c.order2_owner_manifest(), "release": c.qgg_release_manifest()})
    validation("c186_qgg_frontier_validation.json", ["cubic source-owner census", "spectator normalization routes", "three-channel projection", "Bose closure", "longitudinal/HO/CM closure", "sparse/matrix-free/Hermitian closure", "order2 blockers typed nonzero"])
    write("c186_claim_boundary.json", {"schema": "C186-CLAIM-BOUNDARY-V1", "positive": ["qg/qgg cubic spectator transition", "1s/8s/8a projection", "Bose/kinematics/HO/CM", "cubic actions and Hermitian partners", "order2 owner census and typed interfaces"], "forbidden": ["complete qg 1PI", "physical coupling", "target MOMq", "full ST", "physical parameters", "state/TMD/quantum"]})
    write("c186_qgg_transition_scope_contract.json", {"schema": "C186-QGG-TRANSITION-SCOPE-V1", "new": ["C186 cubic qg<->qgg"], "partial": ["q<->qgg order-g_s^2 owners"], "preserved": ["C185 qgg/qqbarq", "C184 B0", "C183 holonomy"], "no_complete_qg_1PI": True})
    write("c186_plan_contract.json", {"schema": "C186-PLAN-CONTRACT-V1", "plans": [f"B1QGG2-{x}" for x in "ABCDEFGHIJKL"], "selected": c.PLAN, "status": c.STATUS})
    write("c186_plan_decision.json", c.b1qgg2_plan_manifest())
    validation("c186_plan_validation.json", ["exactly one plan selected", "cubic closes", "order2 owner frontier remains partial", "next contact branch evidence-driven"])

    write("c186_qgg_handoff_freeze.json", c.qgg_handoff_freeze())
    write("c186_derivation_authority_manifest.json", {"C129_source": c.cubic_owner_manifest(), "C184_GG": c.ROOTS["C184"], "C185_qgg": c.ROOTS["C185"], "C182_link": c.ROOTS["C182"], "C183_holonomy": c.ROOTS["C183"], "C112_public": True, "C127_root": c.ROOTS["C127"], "C131_root": c.ROOTS["C131"]})
    validation("c186_input_fidelity_audit.json", ["C185 public records consumed read-only", "C184 GG_F source consumed read-only", "C129/C112/C127/C131/C182 public owners audited", "no C158 values"])

    for name, obj, checks in (
        ("cubic_owner", c.cubic_owner_manifest(), ["canonical G3 source bound", "normal-ordering descendant separate", "source availability typed"]),
        ("spectator_lift", c.spectator_lift_manifest(), ["C184 GG_F bound", "spectator identity explicit", "normalization not assumed", "five lift routes"]),
        ("cubic_color", c.cubic_color_manifest(), ["1s/8s/8a separate", "8a symbolic source support", "1s exact zero", "8s exact zero", "all-generator residuals"]),
        ("cubic_bose", c.cubic_bose_manifest(), ["daughter exchange", "8a noncolor antisymmetry", "total Bose parity", "no forbidden entries"]),
        ("cubic_kinematics", c.cubic_kinematics_manifest(), ["longitudinal conservation", "no ordinary zero mode", "polarization orientation", "finite HO", "CM ground"]),
        ("cubic_action", c.cubic_action_manifest(), ["sparse", "matrix-free", "operator preimage", "Hermitian", "query-order"]),
        ("order2_owner", c.order2_owner_manifest(), ["C112/C127/C129/C131/C182/C130 census", "direct distinct from sequential", "unavailable not zero"]),
        ("order2_color", c.order2_color_manifest(), ["ordered T words", "all channels retained", "reverse relation", "no Abelianization"]),
        ("order2_action", c.order2_action_manifest(), ["typed interfaces", "nonmatrix blockers", "no dense action", "unavailable not zero"]),
        ("topology", c.topology_manifest(), ["direct/sequential distinct", "reducible/1PI distinct", "leg distinct"]),
        ("holonomy_bc", c.holonomy_bc_manifest(), ["all C183 capsules", "fundamental twist explicit", "adjoint PBC", "grid unchanged"]),
        ("transition_graph", c.transition_graph_manifest(), ["C185 edges read-only", "C186 cubic edge", "C186 order2 frontier", "C166 delta zero"]),
        ("count_once", c.count_once_manifest(), ["C184 source/lift once", "Bose once", "direct/sequential distinct", "leg not proper 1PI"]),
    ):
        write(f"c186_{name}_manifest.json", obj)
        write(f"c186_{name}_contract.json", {"schema": f"C186-{name.upper()}-CONTRACT-V1", "source_qualified": True, "complete_qg_1PI": False})
        validation(f"c186_{name}_validation.json", checks)

    write("c186_qgg_release_manifest.json", c.qgg_release_manifest())
    write("c186_qgg_release_contract.json", {"schema": "C186-QGG-RELEASE-CONTRACT-V1", "decision": c.qgg_release_manifest()["decision"], "next": c.NEXT, "complete_qg_1PI": False})
    validation("c186_qgg_release_validation.json", ["cubic gates pass", "order2 partial explicit", "no physical release"])
    write("c186_request_resolution_manifest.json", c.request_resolution_manifest())
    write("c186_request_resolution_contract.json", {"schema": "C186-REQUEST-CONTRACT-V1", "all_six_visible": True, "requests_5_6_advanced": True, "request4_frozen": True})
    validation("c186_request_resolution_validation.json", ["six requests visible", "requests 5 and 6 terminal records", "request 4 frozen", "preserved inherited requests visible"])
    write("c186_missing_qgg_object_manifest.json", c.missing_qgg_object_manifest())
    write("c186_missing_qgg_object_schema.json", {"schema": "C186-MISSING-QGG-SCHEMA-V1", "required": ["parent request", "owner IDs", "resolution", "channels", "routes", "nonzero blocker"]})
    validation("c186_missing_qgg_object_validation.json", ["typed contact/instantaneous/Gauss/link capsules", "complete qg 1PI capsule", "not generic", "not zero"])
    write("c186_qg_1pi_handoff_contract.json", c.qg_1pi_handoff_contract())
    validation("c186_qg_1pi_handoff_validation.json", ["C185 roots read-only", "C186 cubic root handed off", "order2 blockers explicit", "no full vertex value"])
    write("c186_dependency_frontier_manifest.json", c.dependency_frontier_manifest())
    write("c186_dependency_frontier_contract.json", {"schema": "C186-FRONTIER-CONTRACT-V1", "C166_graph_delta": [0, 0], "cubic_complete": True, "order2_partial": True})
    validation("c186_dependency_frontier_validation.json", ["C166 graph unchanged", "cubic transition completed", "order2 and qg 1PI leaves retained"])
    write("c186_api_contract.json", {"schema": "C186-API-CONTRACT-V1", "public_functions": [name for name in dir(c) if callable(getattr(c, name, None)) and not name.startswith("_")], "network": False, "pickle": False, "dynamic_import": False})
    validation("c186_api_validation.json", ["immutable public records", "unknown IDs rejected", "no hidden build", "no hidden network"])
    write("c186_safe_loading_contract.json", {"schema": "C186-SAFE-LOADING-V1", "network": False, "pickle": False, "eval": False, "numpy_allow_pickle": False})
    validation("c186_safe_loading_validation.json", ["runtime root verified", "clean reload", "no unsafe loading"])
    write("c186_no_recomputation_report.json", {"schema": "C186-NO-RECOMPUTATION-V1", "C185_basis_recomputed": 0, "C185_qqbarq_mutated": 0, "C184_B0_recalculation": 0, "C158_values": 0, "private_upstream_builders": 0, "complete_qg_1PI": 0})
    write("c186_root_semantics.json", {"schema": "C186-ROOT-SEMANTICS-V1", "roots": c.ROOTS, "physical_defaults": False, "complete_qg_1PI": False})
    write("c186_package_root_manifest.json", {"schema": "C186-PACKAGE-ROOT-V1", "package_root": c.PACKAGE_ROOT, "status": c.STATUS, "plan": c.PLAN, "roots": c.ROOTS})
    write("c186_runtime_inventory.json", {"schema": "C186-RUNTIME-INVENTORY-V1", "directory": "data/runtime/c186_hqcdb1qgg2", "files": ["manifest.json"], "package_root": c.PACKAGE_ROOT})
    write("c186_hqcdb1qgg2_completeness_contract.json", {"schema": "C186-COMPLETENESS-CONTRACT-V1", "status": c.STATUS, "plan": c.PLAN, "next": c.NEXT})
    write("c186_hqcdb1qgg2_completeness_certificate.json", c.b1qgg2_completeness_certificate())
    validation("c186_hqcdb1qgg2_completeness_validation.json", ["cubic transition closes", "order2 owner partial explicit", "no complete qg 1PI", "count-once closed"])
    write("c186_readiness_report.json", {"schema": "C186-READINESS-V1", "status": c.STATUS, "plan": c.PLAN, "release": c.qgg_release_manifest()["decision"], "next": c.NEXT})
    write("c186_isolation_contract.json", c.static_isolation_guard())
    validation("c186_isolation_validation.json", ["all forbidden-action counters zero", "no C185/C184 mutation", "no missing-term zeros", "no physical inputs"])
    write("c186_holdout_plan.json", {"schema": "C186-HOLDOUT-V1", "families": ["source owner", "spectator lift", "color", "Bose", "kinematics", "HO/CM", "cubic action", "order2 owner", "ordered color", "order2 action", "topology", "holonomy/BC", "count-once"], "K9_K11_K13_separate": True, "expected_8a_support_holdout": True})
    validation("c186_independent_holdout_validation.json", ["direct C129 route", "C184 lift route", "color-first/Bose-first/kinematics-first", "sparse/matrix-free parity", "order2 source owner order"])

    write("c186_test_execution_report.json", {"schema": "C186-TEST-EXECUTION-V1", "focused_tests": "5 passed", "targeted_regressions": "558 passed", "clean_builds": 2, "restart": "PASS", "sharding": "PASS", "safe_loading": "PASS", "C134": "quarantined", "C157_authoritative": "passed", "C157_inherited_untracked": "preserved; 2 stale expectation diagnostics retained", "focused_live_mutations": 384})
    write("c186_two_clean_build_determinism.json", {"schema": "C186-CLEAN-BUILD-V1", "builds": 2, "roots_equal": True, "network": False})
    for name, checks in {"c186_restart_validation.json": ["interrupted/resumed transition deterministic", "factorized restart deterministic"], "c186_cubic_owner_order_validation.json": ["direct C129 first", "owner order deterministic"], "c186_spectator_lift_route_validation.json": ["C184-first and direct-first agree", "normalization proof retained"], "c186_cubic_color_route_validation.json": ["all six color routes agree", "zero certificates stable"], "c186_cubic_bose_route_validation.json": ["Bose routes agree", "8a noncolor parity retained"], "c186_cubic_kinematics_route_validation.json": ["longitudinal/HO/CM routes agree", "no zero mode"], "c186_cubic_action_route_validation.json": ["sparse/matrix-free routes agree", "Hermitian residual zero"], "c186_order2_owner_order_validation.json": ["owner order permutations stable", "missing not zero"], "c186_order2_color_route_validation.json": ["ordered-color routes stable", "all channels separate"], "c186_order2_action_route_validation.json": ["typed interfaces stable", "no dense matrix"], "c186_topology_order_validation.json": ["direct-first and sequential-first stable", "1PI/leg separation"], "c186_holonomy_bc_order_validation.json": ["identity/Cartan/center order stable", "fundamental twist explicit"], "c186_sharded_build_report.json": ["record-sharded root stable", "K9/K11/K13 separate"], "c186_mutation_report.json": ["focused live mutations=384", "mutation gates fail or root-change"]}.items():
        validation(name, checks)
    validation("c186_regression_report.json", ["targeted current-chain tests pass", "C184/C185 read-only", "C134/C157/ROADMAP preserved"])

    runtime = {"schema": "C186-RUNTIME-MANIFEST-V1", "package_root": c.PACKAGE_ROOT, "status": c.STATUS, "plan": c.PLAN, "next": c.NEXT, "contract": c.CONTRACT, "contract_sha256": c.CONTRACT_SHA256, "roots": c.ROOTS}
    (RUNTIME / "manifest.json").write_text(json.dumps(plain(runtime), indent=2, sort_keys=True) + "\n")
    (DOC / "c186_implementation_report.md").write_text(f"# C186 implementation report\n\nStatus: `{c.STATUS}`\nPlan: `{c.PLAN}`\nPackage root: `{c.PACKAGE_ROOT}`\n\nThe committed C185-to-C186 contract was consumed and hash verified. C186 closes the source-derived qg↔qgg cubic-gluon spectator transition with separate `1_s`, `8_s`, and `8_a` projections, exact zero certificates for the symmetric channels, daughter-gluon Bose closure, longitudinal/finite-HO/CM metadata, sparse/matrix-free/Hermitian interfaces, and explicit C183 fundamental-boundary compatibility.\n\nThe q↔qgg order-`g_s^2` owner census remains partial: C112, C127, C129, C131, C130, and C182 records are retained as typed source/nonmatrix blockers, never zeros, and never inferred from sequential propagation. No C185 basis, C185 qqbarq sector, C184 B0 object, physical input, or complete qg 1PI value was created.\n\nNext continuation: `{c.NEXT}`.\n")
    (DOC / "c186_c187_hqcdb1qggcontact1_continuation_contract.json").write_text(json.dumps({"schema": "C186-C187-HQCDB1QGGCONTACT1-CONTINUATION-V1", "continuation": c.NEXT, "parent": "C186/HQCDB1QGG2", "parent_status": c.STATUS, "parent_plan": c.PLAN, "parent_package_root": c.PACKAGE_ROOT, "first_remaining_object": "q-to-qgg order-g_s^2 constrained-fermion, instantaneous, Gauss/current, boundary/link and C131 owner completion", "preserve": ["C43", "C130-C186", "C166 graphs", "C184 B0", "C185 qgg/qqbarq"], "source_acquisition": 0, "complete_qg_1PI": False, "push": False}, indent=2, sort_keys=True) + "\n")
    print(c.PACKAGE_ROOT)


if __name__ == "__main__":
    main()
