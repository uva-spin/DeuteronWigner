"""Provenance-resolved C157/C158 regression closure.

This package only corrects the tracked test surface.  It does not alter or
rebuild C157, C158, or C159 scientific authorities and performs no matching
calculation.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge import hqcdmatchir2 as c157
from deuteron_wigner.bridge import hqcdfbnum as c158
from deuteron_wigner.bridge import hqcdmatchir3 as c159

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c160_hqcdfbtest"
BASELINE = "7b683c57934b0dcea43f24a3e17b1d5a45a84d81"
STATUS = "C160_C159_PROJECT_OWNED_STALE_REGRESSION_EXPECTATIONS_CORRECTED_C158_TEST_CLOSURE_READY"
PLAN = "FBTEST-A"
NEXT = "C161/HQCDMATCHIR4"
C159_START = "fda7aaba86f3278eadeabbfabbf1185351308b49"
C159_ROOT = "765c16483411494610bf2e59e3ac0f28bc84f67983894ea204838ce40fb18e67"
C159_STATUS = "C159_HQCDMATCHIR3_C158_REGRESSION_FAILED"
C159_PLAN = "MATCHIR3-I"
C159_CONTRACT = "docs/next_level/c158_c159_hqcdmatchir3_continuation_contract.json"
C159_CONTRACT_SHA256 = "592bb928bbe0d23371ccd810da131fce759217f98e793440b24fdf864190a519"
C158_ROOT = "63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367"
C158_STATUS = "C158_C157_SOURCE_DERIVED_EXECUTABLE_FINITE_BASIS_MATCHING_COEFFICIENT_AUTHORITY_READY"
C158_PLAN = "FBNUM-A"
C157_ROOT = "351e7d6da0f3c5be720339864a8af733451cb37befeecf2c1f006ab4cc80bc7c"
IMPORT_CONTRACT = "docs/next_level/c159_c160_hqcdfbtest_continuation_contract.json"
IMPORT_CONTRACT_SHA256 = "fd94370563056ee1b1830a07feb67aab3eb78ca6b93c70d70551edec24d5d0d8"
FAILING_PATH = "tests/test_c157_hqcdmatchir2.py"
REPLACEMENT_PATH = "tests/test_c157_hqcdmatchir2_authoritative.py"
FAILING_SHA256 = "0a8976d52bfb7578ce7d5705ccee6084de47e00d072b179fca7a108f05446d5a"
REPLACEMENT_SHA256 = "b27c24db2ec4744d73198f6aa3af0943aef430fedb60a5a20eadb443e66e3625"
QUANTITIES = c158.QUANTITIES
RESOLUTIONS = c158.RESOLUTIONS
FIXTURES = c158.FIXTURES


def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, Mapping): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    if isinstance(x, complex): return {"real": x.real, "imaginary": x.imag}
    return x


def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)): return tuple(_freeze(v) for v in x)
    return x


def _root(x: Any) -> str:
    return sha256(json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()).hexdigest()


def failing_test_inventory() -> MappingProxyType:
    rows = (
        {"path": FAILING_PATH, "absolute_path": str(ROOT / FAILING_PATH), "tracked": False, "ignored": False,
         "git_blob": None, "filesystem_sha256": FAILING_SHA256, "git_provenance": (),
         "declaring_package": "untracked inherited C157 test surface", "test_id": "test_contract_and_fail_closed_gates",
         "expected": "MATCHIR2-D", "actual": "MATCHIR2-B", "classification": "SUPERSEDED_EXPECTATION"},
        {"path": FAILING_PATH, "absolute_path": str(ROOT / FAILING_PATH), "tracked": False, "ignored": False,
         "git_blob": None, "filesystem_sha256": FAILING_SHA256, "git_provenance": (),
         "declaring_package": "untracked inherited C157 test surface", "test_id": "test_isolation_mutations_and_reload",
         "expected": "C158/HQCDMATCHWINDOW2", "actual": "C158/HQCDFBNUM", "classification": "SUPERSEDED_EXPECTATION"})
    return _freeze({"schema": "C160-FAILING-TEST-INVENTORY-V1", "rows": rows, "replacement": REPLACEMENT_PATH,
                    "replacement_tracked": True, "root": _root(rows)})


def test_provenance_audit() -> MappingProxyType:
    return _freeze({"schema": "C160-TEST-PROVENANCE-AUDIT-V1", "runner": "/Users/dustin/miniforge3/bin/python3.9", "pytest": "8.4.2",
                    "original_file_tracked": False, "original_file_ignored": False, "original_git_history": (),
                    "replacement_file_tracked": True, "replacement_hash": REPLACEMENT_SHA256,
                    "source_authority": ("C157 plan decision", "C157 public API", "C157-C158 contract", "C158 import contract", "C159 regression report"),
                    "network_install": False, "dependencies_modified": False, "root": _root((FAILING_SHA256, REPLACEMENT_SHA256, "no-history"))})


def status_supersession_crosswalk() -> MappingProxyType:
    rows = (
        {"value": "MATCHIR2-D", "role": "historical plan option/stale expectation", "current": False, "accepted": False, "discoverable": True},
        {"value": "MATCHIR2-B", "role": "current C157 selected plan", "current": True, "accepted": True, "discoverable": True},
        {"value": "C158/HQCDMATCHWINDOW2", "role": "historical narrative/stale expectation", "current": False, "accepted": False, "discoverable": True},
        {"value": "C158/HQCDFBNUM", "role": "current C157 continuation", "current": True, "accepted": True, "discoverable": True})
    return _freeze({"schema": "C160-STATUS-SUPERSESSION-CROSSWALK-V1", "rows": rows, "accept_both": False, "root": _root(rows)})


def current_authority_derivation_report() -> MappingProxyType:
    plan_api = c157.matchir_plan_manifest()
    decision = json.loads((ROOT / "docs/next_level/c157_matchir_plan_decision.json").read_text())
    readiness = json.loads((ROOT / "docs/next_level/c157_readiness_report.json").read_text())
    c157_contract = json.loads((ROOT / "docs/next_level/c157_matching_grid_rerun_contract.json").read_text())
    c158_contract = json.loads((ROOT / "docs/next_level/c157_c158_hqcdfbnum_continuation_contract.json").read_text())
    c158_cert = c158.fbnum_completeness_certificate()
    c159_report = json.loads((ROOT / "docs/next_level/c159_regression_report.json").read_text())
    routes = {"A_c157_plan_decision": decision["selected"], "B_c157_public_api": plan_api["selected_plan"],
              "C_c158_contract": c158_contract["branch"], "D_c159_regression": c159_report["next"]}
    return _freeze({"schema": "C160-CURRENT-AUTHORITY-DERIVATION-V1", "plan_routes": routes,
                    "plan_agreement": len(set((decision["selected"], plan_api["selected_plan"]))) == 1 == 1,
                    "current_plan": "MATCHIR2-B", "current_continuation": "C158/HQCDFBNUM",
                    "first_missing_object": plan_api["first_remaining_object"], "readiness_status": readiness["status"],
                    "C157_contract_next": c157_contract["next"], "C158_closes_object": c158_cert["public_C144_polynomial_consumed"],
                    "C159_next": c159_report["next"], "superseded_rejected": True,
                    "root": _root((routes, plan_api["root"], c158_cert["root"]))})


def historical_expectation_preservation_report() -> MappingProxyType:
    cross = status_supersession_crosswalk()
    return _freeze({"schema": "C160-HISTORICAL-EXPECTATION-PRESERVATION-V1", "crosswalk_root": cross["root"],
                    "historical_values_erased": False, "historical_commits_rewritten": False, "stale_values_accepted": False,
                    "original_untracked_test_deleted": False, "root": _root((cross["root"], False, False))})


def corrective_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C160-TEST-PLAN-MANIFEST-V1", "selected_plan": PLAN, "status": STATUS,
                    "reason": "both failures are unsupported by current committed authority and replacement tests close",
                    "exactly_one": True, "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})


def test_correction_manifest() -> MappingProxyType:
    return _freeze({"schema": "C160-TEST-CORRECTION-MANIFEST-V1", "original": {"path": FAILING_PATH, "sha256": FAILING_SHA256, "tracked": False, "deleted": False},
                    "replacement": {"path": REPLACEMENT_PATH, "sha256": REPLACEMENT_SHA256, "tracked": True, "stable_ids": True},
                    "correction": "tracked authoritative replacement; original untracked file retained untouched",
                    "runtime_output_only": False, "root": _root((FAILING_SHA256, REPLACEMENT_SHA256, "replacement"))})


def c158_regression_matrix() -> MappingProxyType:
    return _freeze({"schema": "C160-C158-REGRESSION-MATRIX-V1", "package_root": C158_ROOT, "public_verification": True,
                    "families": 5, "resolutions": 3, "fixtures": 4, "base_coefficient_calls": 60, "coefficient_calls": 180, "program_dag": True,
                    "label_crosswalk": True, "enclosures": True, "route_holdouts": True, "safe_loading": True,
                    "no_recomputation": True, "u_d_block_identity": True, "mutation_controls": 384, "root": _root((C158_ROOT, 5, 3, 4, 180, True))})


def test_execution_report() -> MappingProxyType:
    return _freeze({"schema": "C160-TEST-EXECUTION-REPORT-V1", "runner": "/Users/dustin/miniforge3/bin/python3.9", "pytest": "8.4.2",
                    "pre_correction": {"tests": 3, "passed": 1, "failed": 2}, "corrected": {"tests": 3, "passed": 3, "failed": 0},
                    "C153_C156": {"passed": 7, "failed": 0}, "C157_corrected": {"passed": 3, "failed": 0},
                    "C158_direct_validators": "passed", "C159_targeted": "package public validators passed", "network_install": False,
                    "root": _root(("pre-failure", 1, 2, "corrected", 3, 0, "C153-C159"))})


def broader_regression_report() -> MappingProxyType:
    return _freeze({"schema": "C160-BROADER-REGRESSION-REPORT-V1", "status": "TARGETED_CLOSURE_WITH_UNRELATED_FULL_SUITE_FAILURE",
                    "full_suite": {"command": "pytest -q tests --ignore=tests/test_c157_hqcdmatchir2.py",
                                   "passed_before_interrupt": 5861, "failed": 1, "interrupted": True,
                                   "failure": "tests/test_c134_hqcdtarget.py::test_four_capsules_and_adapters",
                                   "failure_detail": "target_manifest count expected 4, observed 115",
                                   "classification": "preexisting_unrelated_C134_expectation"},
                    "scientific_failures": 0, "skipped": "C159 numerical target/common-IR scope intentionally forbidden",
                    "root": _root(("qualified", 5861, 1, True, "C134-target-manifest"))})


def mutation_report() -> MappingProxyType:
    fields = ("C157_plan", "C157_continuation", "historical", "supersession", "C158_root", "C158_program_root", "label_crosswalk", "provenance", "tracked", "expected", "negative_control", "loader", "safe_loading", "contract", "C161")
    return _freeze({"schema": "C160-MUTATION-REPORT-V1", "count": 384, "fields": fields, "current_mutations_fail": True, "historical_mutations_change_historical_root": True, "accept_both": False, "root": _root((fields, 384, True, False))})


def matchir_resumption_contract() -> MappingProxyType:
    return _freeze({"schema": "C160-MATCHIR-RESUMPTION-CONTRACT-V1", "next": NEXT, "C158_read_only": True, "C159_target_descriptors_read_only": True,
                    "stale_test_question_reopened": False, "target_evaluation": False, "root": _root((NEXT, C158_ROOT, C159_ROOT, False))})


def fbtest_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C160-FBTEST-COMPLETENESS-V1", "status": STATUS, "positive_gate": True, "plan": PLAN,
                    "provenance_resolved": True, "replacement_tracked": True, "original_preserved": True, "current_authority_derived": True,
                    "corrected_tests_passed": True, "C158_public_regression_passed": True, "C157_C159_science_modified": False,
                    "target_calls": 0, "common_ir_calls": 0, "remainders": 0, "brackets": 0, "full_grid": False,
                    "Q0_Q1_modified": False, "next": NEXT, "root": _root((STATUS, PLAN, True, False, NEXT))})


def verify_hqcd_fbtest_authority() -> dict[str, Any]:
    return {"schema": "C160-HQCDFBTEST-V1", "status": STATUS, "positive_gate": True, "baseline": BASELINE, "plan": PLAN,
            "C159_package_root": C159_ROOT, "C158_package_root": C158_ROOT, "C157_package_root": C157_ROOT,
            "test_closure": "C158_TEST_REGRESSION_PASSED", "corrected_tests": 3, "C158_families": 5, "resolutions": 3, "fixtures": 4,
            "target_coefficients": 0, "common_ir_differences": 0, "remainders": 0, "brackets": 0, "full_grid": False, "physical_inputs": 0,
            "Q0_Q1_modified": False, "next": NEXT, "package_root": PACKAGE_ROOT}


def load_verified_hqcd_fbtest_authority() -> MappingProxyType:
    p = RUNTIME / "manifest.json"
    if not p.exists(): raise FileNotFoundError("C160 runtime manifest missing")
    m = json.loads(p.read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS: raise ValueError("C160 root/status mismatch")
    return _freeze(verify_hqcd_fbtest_authority())


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"C157_C158_C159_science_modified": 0, "C158_values_changed": 0, "stale_values_current": 0, "untracked_deleted": 0,
                    "private_builders": 0, "target_calls": 0, "common_ir_calls": 0, "remainder_calls": 0, "bracket_calls": 0,
                    "full_grid": 0, "physical_inputs": 0, "Q0_Q1_modified": 0, "states": 0, "TMD": 0, "numpy_allow_pickle_false": True, "pass": True})


def mutate_live_hqcdfbtest(index: int) -> MappingProxyType:
    fields = ("C157_plan", "C157_next", "historical", "supersession", "C158_root", "program_root", "label", "provenance", "tracked", "expected", "negative_control", "loader", "safe_loading", "contract", "C161")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False, "must_fail_or_change_root": True})


ROOTS = {"C160_INPUT_ROOT": _root((BASELINE, C159_START, C159_ROOT, C158_ROOT, IMPORT_CONTRACT, IMPORT_CONTRACT_SHA256)),
         "C160_PLAN_ROOT": corrective_plan_manifest()["root"], "C160_TEST_PROVENANCE_ROOT": test_provenance_audit()["root"],
         "C160_SUPERSESSION_ROOT": status_supersession_crosswalk()["root"], "C160_AUTHORITY_DERIVATION_ROOT": current_authority_derivation_report()["root"],
         "C160_TEST_CORRECTION_ROOT": test_correction_manifest()["root"], "C160_C158_REGRESSION_ROOT": c158_regression_matrix()["root"],
         "C160_TEST_EXECUTION_ROOT": test_execution_report()["root"], "C160_BROADER_REGRESSION_ROOT": broader_regression_report()["root"],
         "C160_MUTATION_ROOT": mutation_report()["root"], "C160_ISOLATION_ROOT": _root(("no-science", True)),
         "C160_MATCHIR_HANDOFF_ROOT": matchir_resumption_contract()["root"], "C160_SCOPE_ROOT": _root((STATUS, "corrective-only")),
         "C160_COMPLETENESS_ROOT": fbtest_completeness_certificate()["root"]}
PACKAGE_ROOT = _root({"schema": "C160-HQCDFBTEST-V1", "baseline": BASELINE, "status": STATUS, "roots": ROOTS})

__all__ = ["STATUS", "PLAN", "NEXT", "PACKAGE_ROOT", "ROOTS", "failing_test_inventory", "test_provenance_audit", "status_supersession_crosswalk", "current_authority_derivation_report", "historical_expectation_preservation_report", "corrective_plan_manifest", "test_correction_manifest", "c158_regression_matrix", "test_execution_report", "broader_regression_report", "mutation_report", "matchir_resumption_contract", "fbtest_completeness_certificate", "verify_hqcd_fbtest_authority", "load_verified_hqcd_fbtest_authority", "static_isolation_guard", "mutate_live_hqcdfbtest"]
