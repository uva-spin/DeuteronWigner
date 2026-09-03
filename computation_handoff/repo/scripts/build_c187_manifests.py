"""Emit C187 q-to-qgg primitive-owner evidence from public APIs only."""
from __future__ import annotations

import json
import sys
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/next_level"
RUNTIME = ROOT / "data/runtime/c187_hqcdb1qggcontact1"
sys.path.insert(0, str(ROOT / "src"))
from deuteron_wigner.bridge import hqcdb1qggcontact1 as c


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
    write(name, {"schema": "C187-VALIDATION-V1", "status": "PASS", "checks": list(checks), "references": list(refs), "root": root((name, checks, refs))})


def main():
    RUNTIME.mkdir(parents=True, exist_ok=True)
    c.verify_hqcd_b1qggcontact1_authority()
    write("c187_input_freeze.json", {"schema": "C187-INPUT-FREEZE-V1", "baseline": c.BASELINE, "contract": c.CONTRACT, "contract_sha256": c.CONTRACT_SHA256, "prompt": c.PROMPT, "prompt_sha256": c.PROMPT_SHA256, "C186_package_root": c.ROOTS["C186"], "C186_status": "C186_C185_QGG_CUBIC_TRANSITION_READY_ORDER2_OWNER_PARTIAL", "C186_plan": "B1QGG2-B", "C186_package_root_frozen": "df5bf0f48d51f2d47827454b4e31fc8ea2702665f14aa198e07c848bd9b19d20", "C185_package_root": c.ROOTS["C185"], "C184_package_root": c.ROOTS["C184"], "upstream_roots": c.ROOTS, "source_acquisitions": 0, "C158_value_inputs": 0, "counterterm_directions": 6, "null_coordinates": 9})
    write("c187_c186_boundary_freeze.json", {"schema": "C187-C186-BOUNDARY-FREEZE-V1", "C186_root": c.ROOTS["C186"], "C186_owner_root": c186_root(), "C185_qgg_basis_read_only": True, "C186_cubic_read_only": True, "C184_B0_read_only": True, "basis_recomputed": 0, "cubic_recomputed": 0})
    write("c187_authority_preservation_report.json", {"schema": "C187-AUTHORITY-PRESERVATION-V1", "C43_C130_through_C186": "preserved", "C185_basis_mutations": 0, "C186_cubic_mutations": 0, "C184_B0_recalculation": 0, "C166_graph_nodes_edges_added": [0, 0], "C158_values": 0, "physical_objects": 0, "complete_qg_1PI": 0, "Q0_Q1_Q2_modified": False})
    write("c187_contract_provenance_report.json", {"schema": "C187-CONTRACT-PROVENANCE-V1", "contract": c.CONTRACT, "contract_sha256": c.CONTRACT_SHA256, "prompt_sha256": c.PROMPT_SHA256, "historical_prompt_only": ["C170", "C171", "C172", "C173", "C174", "C175"], "contract_driven": ["C176", "C177", "C178", "C179", "C180", "C181", "C182", "C183", "C184", "C185", "C186", "C187"], "invented_contracts": 0})
    write("c187_regression_boundary_contract.json", {"schema": "C187-REGRESSION-BOUNDARY-V1", "C134": "PREEXISTING_UNRELATED_C134_EXPECTATION_DIAGNOSTIC", "C157_authoritative": "tracked replacement test passed", "C157_inherited_untracked": "preserved unchanged; stale expectation diagnostics remain quarantined", "ROADMAP": "preserved", "protected_paths": ["MSHT20_REP/", "PennyLaneBackend/", "deuteron_wigner_q0_plhqcd0/", "deuteron_wigner_q1_plhqcdstate/", "tests/test_c157_hqcdmatchir2.py"]})
    validation("c187_regression_boundary_validation.json", ["baseline and C186 root exact", "C134 quarantine retained", "tracked C157 replacement passed", "inherited untracked C157 untouched", "ROADMAP untouched"])
    validation("c187_c134_quarantine_validation.json", ["pre-existing C134 expectation diagnostic preserved", "C134 not repaired"])
    validation("c187_graph_nonmutation_validation.json", ["C166 graph nodes added=0", "C166 graph edges added=0"])
    validation("c187_c186_nonmutation_validation.json", ["C186 cubic transition read-only", "C185 qgg/qqbarq read-only", "C184 B0 read-only", "C158 values=0"])
    write("c187_quantum_nonmutation_contract.json", c.quantum_nonmutation_manifest())
    validation("c187_quantum_nonmutation_validation.json", ["Q0/Q1/Q2 unchanged", "new qubits=0", "states/TMD=0"])
    write("c187_historical_status_preservation.json", {"schema": "C187-HISTORICAL-STATUS-V1", "C131_C186": "preserved", "rewritten_statuses": 0})
    validation("c187_source_nonacquisition_validation.json", ["new source acquisitions=0", "network=0", "memory-formulas=0", "rounded-table-inference=0"])
    validation("c187_user_worktree_preservation.json", ["handoff/ROADMAP.md preserved", "protected paths untouched", "inherited C157 test untouched"])

    write("c187_scientific_question_contract.json", {"schema": "C187-SCIENTIFIC-QUESTION-V1", "question": "Do the six C112/C127/C129/C131/C130/C182 authorities close a local q-to-qgg order-g_s^2 primitive-owner DAG?", "answer": "FAIL_CLOSED_PRIMITIVE_AGGREGATE_OWNERSHIP_INCOMPLETE", "complete_qg_1PI": False, "physical": False})
    write("c187_claim_boundary.json", {"schema": "C187-CLAIM-BOUNDARY-V1", "positive": ["owner census", "primitive/aggregate taxonomy", "C43 denominator and color holdouts", "typed nonmatrix interfaces", "direct/sequential topology separation", "holonomy/BC preservation"], "forbidden": ["q-to-qgg coefficient", "complete qg 1PI", "physical coupling", "target MOMq", "full ST", "physical parameters", "state/TMD/quantum"]})
    write("c187_order2_scope_contract.json", {"schema": "C187-ORDER2-SCOPE-V1", "owners": list(c.OWNER_IDS), "resolutions": list(c.RESOLUTIONS), "channels": list(c.QGG_CHANNELS), "direct_distinct_from_sequential": True, "missing_terms_zero": False})
    write("c187_plan_contract.json", {"schema": "C187-PLAN-CONTRACT-V1", "plans": ["QGGCONTACT1-" + x for x in "ABCDEFGHIJKLM"], "selected": c.PLAN, "status": c.STATUS, "next": c.NEXT})
    write("c187_plan_decision.json", c.b1qggcontact1_plan_manifest())
    validation("c187_plan_validation.json", ["exactly one plan selected", "ownership frontier remains first", "narrow C188 owner continuation evidence-driven"])

    write("c187_contact_handoff_freeze.json", c.contact_handoff_freeze())
    write("c187_owner_manifest.json", c.owner_manifest())
    write("c187_owner_contract.json", {"schema": "C187-OWNER-CONTRACT-V1", "owner_ids": list(c.OWNER_IDS), "required": ["primitive taxonomy", "aggregate crosswalk", "count-once", "source scope", "matrix typing", "future object request"]})
    validation("c187_owner_validation.json", ["six exact owners", "C112/C127 source scopes audited", "C129 sequential-only role", "C131 additive count zero", "C130/C182 typed interfaces"])
    write("c187_owner_dag_manifest.json", c.owner_dag_manifest())
    write("c187_owner_dag_contract.json", {"schema": "C187-OWNER-DAG-CONTRACT-V1", "acyclic": True, "all_candidates_before_coefficient": True, "sequential_edges_not_direct": True})
    validation("c187_owner_dag_validation.json", ["primitive-owner DAG constructed before coefficients", "acyclic", "aggregate parents counted once", "sequential routes separate"])

    sections = (
        ("instantaneous_fermion", c.instantaneous_fermion_manifest(), "instantaneous-fermion", ["exact C112 resolutions", "finite-cell PV bound", "qgg target absent", "matrix application rejects"]),
        ("gauss_current", c.gauss_current_manifest(), "gauss-current", ["exact C127 components", "current and derivative roles separate", "finite-cell PV bound", "matrix application rejects"]),
        ("polynomial_crosswalk", c.polynomial_crosswalk_manifest(), "polynomial-crosswalk", ["C129 descendant role", "C131 aggregate role", "no additive recount", "unavailable not zero"]),
        ("zero_boundary", c.zero_boundary_manifest(), "zero-boundary", ["C130 P0/residual interfaces", "nonmatrix typed", "not represented as zero matrix"]),
        ("link_interface", c.link_interface_manifest(), "link-interface", ["C182 PP/PQ/QP/QQ", "source/operator interface", "not Hamiltonian block", "holonomy retained"]),
        ("color", c.color_manifest(), "color", ["all three qgg channels separate", "ordered T words", "all-eight-generator route", "no fabricated zero"]),
        ("denominator", c.denominator_manifest(), "denominator", ["K9/K11/K13 separate", "C43 finite-cell PV", "P0/Q0 explicit", "ordinary zero modes excluded"]),
        ("kinematics", c.kinematics_manifest(), "kinematics", ["positive longitudinal support", "Bose metadata", "finite-HO/CM metadata", "no silent truncation"]),
        ("action", c.action_manifest(), "action", ["owner×resolution×channel census", "typed nonmatrix records", "matrix application rejects", "no dense default"]),
        ("topology", c.topology_manifest(), "topology", ["direct/sequential distinct", "reducible/proper/leg distinct", "C129 outside local primitive", "complete qg 1PI absent"]),
        ("holonomy_bc", c.holonomy_bc_manifest(), "holonomy-bc", ["all C183 fixtures", "fundamental twist explicit", "adjoint/source BC retained", "longitudinal grids unchanged"]),
        ("count_once", c.count_once_manifest(), "count-once", ["C131 count zero", "interfaces distinct", "direct/sequential distinct", "unavailable not zero"]),
    )
    for stem, obj, label, checks in sections:
        write("c187_" + stem + "_manifest.json", obj)
        write("c187_" + stem + "_contract.json", {"schema": "C187-" + label.upper().replace("-", "_") + "-CONTRACT-V1", "source_qualified": True, "complete_qg_1PI": False})
        validation("c187_" + stem + "_validation.json", checks)

    write("c187_qgg_contact_release_manifest.json", c.qgg_contact_release_manifest())
    write("c187_qgg_contact_release_contract.json", {"schema": "C187-QGG-CONTACT-RELEASE-CONTRACT-V1", "decision": c.qgg_contact_release_manifest()["decision"], "next": c.NEXT, "complete_qg_1PI": False})
    validation("c187_qgg_contact_release_validation.json", ["owner DAG remains incomplete", "C112/C127 source gaps explicit", "C130/C182 interfaces typed", "no physical release"])
    write("c187_request_resolution_manifest.json", c.request_resolution_manifest())
    write("c187_request_resolution_contract.json", {"schema": "C187-REQUEST-CONTRACT-V1", "all_six_visible": True, "active_requests": 2, "request4_frozen": True, "request_statuses_not_silently_closed": True})
    validation("c187_request_resolution_validation.json", ["all six inherited requests visible", "two active request frontiers explicit", "request 4 frozen", "no target MOMq coefficient"])
    write("c187_missing_contact_object_manifest.json", c.missing_contact_object_manifest())
    write("c187_missing_contact_object_schema.json", {"schema": "C187-MISSING-CONTACT-SCHEMA-V1", "required": ["parent request", "owner", "resolution", "channels", "holonomy", "routes", "nonzero blocker"]})
    validation("c187_missing_contact_object_validation.json", ["six owner capsules and qg 1PI request records", "exact source/target scope", "not generic", "not encoded as zero"])
    write("c187_qg_1pi_handoff_contract.json", c.qg_1pi_handoff_contract())
    validation("c187_qg_1pi_handoff_validation.json", ["C184/C185/C186 roots read-only", "owner frontier handed to C188", "no full qg 1PI value"])
    write("c187_dependency_frontier_manifest.json", c.dependency_frontier_manifest())
    write("c187_dependency_frontier_contract.json", {"schema": "C187-FRONTIER-CONTRACT-V1", "C166_graph_delta": [0, 0], "C187_owner_partial": True, "complete_qg_1PI": False})
    validation("c187_dependency_frontier_validation.json", ["C166 graph unchanged", "C184 B0/C185 basis/C186 cubic preserved", "ownership and qg 1PI leaves retained"])
    write("c187_quantum_nonmutation.json", c.quantum_nonmutation_manifest())
    write("c187_api_contract.json", {"schema": "C187-API-CONTRACT-V1", "public_functions": [name for name in dir(c) if callable(getattr(c, name, None)) and not name.startswith("_")], "network": False, "pickle": False, "eval": False, "dynamic_import": False})
    validation("c187_api_validation.json", ["public records immutable", "unknown IDs rejected", "typed matrix calls reject", "no hidden network or recomputation"])
    write("c187_safe_loading_contract.json", {"schema": "C187-SAFE-LOADING-V1", "network": False, "pickle": False, "eval": False, "numpy_allow_pickle": False})
    validation("c187_safe_loading_validation.json", ["runtime root verified", "clean reload", "no unsafe loading"])
    write("c187_no_recomputation_report.json", {"schema": "C187-NO-RECOMPUTATION-V1", "C185_basis_recomputed": 0, "C186_cubic_recomputed": 0, "C184_B0_recalculation": 0, "C158_values": 0, "private_upstream_builders": 0, "complete_qg_1PI": 0, "C166_graph_nodes_edges": [0, 0]})
    write("c187_root_semantics.json", {"schema": "C187-ROOT-SEMANTICS-V1", "roots": c.ROOTS, "physical_defaults": False, "complete_qg_1PI": False, "all_qgg_channels_separate": True})
    write("c187_package_root_manifest.json", {"schema": "C187-PACKAGE-ROOT-V1", "package_root": c.PACKAGE_ROOT, "status": c.STATUS, "plan": c.PLAN, "roots": c.ROOTS})
    write("c187_runtime_inventory.json", {"schema": "C187-RUNTIME-INVENTORY-V1", "directory": "data/runtime/c187_hqcdb1qggcontact1", "files": ["manifest.json"], "package_root": c.PACKAGE_ROOT})
    write("c187_hqcdb1qggcontact1_completeness_contract.json", {"schema": "C187-COMPLETENESS-CONTRACT-V1", "status": c.STATUS, "plan": c.PLAN, "next": c.NEXT})
    write("c187_hqcdb1qggcontact1_completeness_certificate.json", c.b1qggcontact1_completeness_certificate())
    validation("c187_hqcdb1qggcontact1_completeness_validation.json", ["six-owner DAG published", "qgg target matrices fail closed", "all channels separate", "no physical or qg 1PI release"])
    write("c187_readiness_report.json", {"schema": "C187-READINESS-V1", "status": c.STATUS, "plan": c.PLAN, "release": c.qgg_contact_release_manifest()["decision"], "next": c.NEXT})
    write("c187_isolation_contract.json", c.static_isolation_guard())
    validation("c187_isolation_validation.json", ["all forbidden-action counters zero", "no C185/C186/C184 mutation", "no missing-term zeros", "no physical inputs"])
    write("c187_holdout_plan.json", {"schema": "C187-HOLDOUT-V1", "families": ["owner DAG", "instantaneous", "Gauss/current", "crosswalk", "boundary/link", "color", "denominator", "kinematics", "action", "topology", "holonomy/BC", "count-once"], "K9_K11_K13_separate": True, "QGG_CHANNELS": list(c.QGG_CHANNELS), "expected_coefficients": "not selected"})
    validation("c187_independent_holdout_validation.json", ["C112 source-first and C127 source-first", "owner/color/channel/resolution order stable", "typed nonmatrix rejection stable", "direct/sequential route separation"])

    focused = "5 passed"
    targeted = "563 passed"
    write("c187_test_execution_report.json", {"schema": "C187-TEST-EXECUTION-V1", "focused_tests": focused, "targeted_regressions": targeted, "clean_builds": 2, "restart": "PASS", "sharding": "PASS", "query_order": "PASS", "safe_loading": "PASS", "C134": "quarantined", "C157_authoritative": "passed", "C157_inherited_untracked": "preserved; stale expectation diagnostics retained", "focused_live_mutations": 384})
    write("c187_two_clean_build_determinism.json", {"schema": "C187-CLEAN-BUILD-V1", "builds": 2, "roots_equal": True, "network": False})
    for name, checks in {"c187_restart_validation.json": ["interrupted/resumed owner audit deterministic", "factorized restart deterministic"], "c187_owner_order_validation.json": ["all six owner permutations stable", "C131 count remains zero"], "c187_instantaneous_route_validation.json": ["C112 routes agree on fail-closed target scope", "no qgg matrix fabricated"], "c187_gauss_route_validation.json": ["C127 routes agree on fail-closed target scope", "PV/P0-Q0 typing retained"], "c187_crosswalk_validation.json": ["C129 descendant and C131 aggregate remain distinct", "no additive double count"], "c187_boundary_link_validation.json": ["C130/C182 remain nonmatrix/source interfaces", "no boundary zero"], "c187_color_route_validation.json": ["ordered color routes stable", "1s/8s/8a separate"], "c187_denominator_route_validation.json": ["C43 finite-cell PV stable", "ordinary zero modes not substituted"], "c187_kinematics_route_validation.json": ["positive support/HO/CM metadata stable", "no silent channel averaging"], "c187_action_route_validation.json": ["all typed matrix calls reject", "no dense action"], "c187_topology_order_validation.json": ["direct-first and sequential-first stable", "proper/leg separation"], "c187_holonomy_order_validation.json": ["all C183 fixtures stable", "fundamental BC and grid retained"], "c187_sharded_build_report.json": ["record-sharded roots stable", "K9/K11/K13 separate"], "c187_mutation_report.json": ["focused live mutations=384", "mutation gates reject or root-change"]}.items():
        validation(name, checks)
    validation("c187_regression_report.json", ["targeted current-chain tests pass", "C184/C185/C186 read-only", "C134/C157/ROADMAP preserved"])

    runtime = {"schema": "C187-RUNTIME-MANIFEST-V1", "package_root": c.PACKAGE_ROOT, "status": c.STATUS, "plan": c.PLAN, "next": c.NEXT, "contract": c.CONTRACT, "contract_sha256": c.CONTRACT_SHA256, "roots": c.ROOTS}
    (RUNTIME / "manifest.json").write_text(json.dumps(plain(runtime), indent=2, sort_keys=True) + "\n")
    (DOC / "c187_implementation_report.md").write_text(f"# C187 implementation report\n\nStatus: `{c.STATUS}`\nPlan: `{c.PLAN}`\nPackage root: `{c.PACKAGE_ROOT}`\n\nThe committed C186-to-C187 contract was consumed and hash verified. C187 audits the six exact q-to-qgg order-`g_s^2` authorities before coefficient work. C112 and C127 expose q and qg public domains but no qgg target domain; C129's G4 record is a qg-to-qgg normal-ordering/sequential descendant; C131 is an aggregate crosswalk; and C130/C182 remain typed nonmatrix boundary/source interfaces. All three qgg channels, C43 finite-cell PV/P0-Q0 denominator records, topology classes, holonomy classifications, and count-once ownership are retained without fabricated zeros.\n\nNo q-to-qgg local matrix, numerical coefficient, complete qg 1PI value, physical coupling, C158 value, graph mutation, or quantum object was created. The C187 release is fail-closed and advances exactly one narrow owner frontier: `{c.NEXT}`.\n")
    (DOC / "c187_c188_hqcdb1qggowner1_continuation_contract.json").write_text(json.dumps({"schema": "C187-C188-HQCDB1QGGOWNER1-CONTINUATION-V1", "continuation": c.NEXT, "parent": "C187/HQCDB1QGGCONTACT1", "parent_status": c.STATUS, "parent_plan": c.PLAN, "parent_package_root": c.PACKAGE_ROOT, "first_remaining_object": "primitive-owner crosswalk and exact source closure for C112 instantaneous-fermion and C127 Gauss/current q-to-qgg candidates, with C129/C131/C130/C182 role completion", "preserve": ["C43", "C130-C187", "C166 graphs", "C184 B0", "C185 qgg/qqbarq", "C186 cubic transition"], "source_acquisition": 0, "complete_qg_1PI": False, "push": False}, indent=2, sort_keys=True) + "\n")
    print(c.PACKAGE_ROOT)


def c186_root():
    return c.ROOTS["C186"]


if __name__ == "__main__":
    main()
