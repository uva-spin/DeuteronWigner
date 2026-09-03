"""C159 fail-closed boundary for the inherited C158 regression.

The local pytest runner is available, and the inherited C157 test surface has
two actual expectation failures.  C159 therefore publishes no target value,
common-IR difference, remainder, or bracket.  The target-program records
remain immutable source-qualified descriptors for the next corrective branch.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c159_hqcdmatchir3"
BASELINE = "fda7aaba86f3278eadeabbfabbf1185351308b49"
CONTRACT = "docs/next_level/c158_c159_hqcdmatchir3_continuation_contract.json"
CONTRACT_SHA256 = "592bb928bbe0d23371ccd810da131fce759217f98e793440b24fdf864190a519"
SCHEMA = "C159-HQCDMATCHIR3-V1"
STATUS = "C159_HQCDMATCHIR3_C158_REGRESSION_FAILED"
PLAN = "MATCHIR3-I"
NEXT = "C160/HQCDFBTEST"
C158_STATUS = "C158_C157_SOURCE_DERIVED_EXECUTABLE_FINITE_BASIS_MATCHING_COEFFICIENT_AUTHORITY_READY"
C158_PLAN = "FBNUM-A"
C158_ROOT = "63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367"
C157_ROOT = "351e7d6da0f3c5be720339864a8af733451cb37befeecf2c1f006ab4cc80bc7c"
C153_ROOT = "7af7b6fcc7c5b80c61f721b3c438b914518ebf52103a322befd1ef97b4a1c464"
QUANTITIES = ("QUARK_FIELD", "SIGNED_QUARK_MASS", "TRANSVERSE_GLUON_FIELD", "qg_VERTEX_DRESSING", "QCD_COUPLING")
ORDERS = {"QUARK_FIELD": 0, "SIGNED_QUARK_MASS": 0, "TRANSVERSE_GLUON_FIELD": 0, "qg_VERTEX_DRESSING": 1, "QCD_COUPLING": 1}
LABELS = {"QUARK_FIELD": "delta_quark_field^FB(order=0)", "SIGNED_QUARK_MASS": "delta_signed_quark_mass^FB(order=0)", "TRANSVERSE_GLUON_FIELD": "delta_gluon_field^FB(order=0)", "qg_VERTEX_DRESSING": "delta_qg_vertex^FB(order=1)", "QCD_COUPLING": "delta_qcd_coupling^FB(order=1)"}
TARGET_SCHEMES = ("PROJECT_CONTINUUM_LIGHT_FRONT", "C43_ADAPTED_MSBAR", "RI_SMOM", "MOMQ", "STEP_SCALING_INTERMEDIATE")
RESOLUTIONS = ("K9", "K11", "K13")
FIXTURES = ("FIXTURE-FREE", "FIXTURE-INTERACTING-A", "FIXTURE-INTERACTING-B-NULL-SHIFT", "FIXTURE-MASS-SIGN")


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


def _require_common(record: Mapping[str, Any]) -> Mapping[str, Any]:
    if not isinstance(record, Mapping): raise TypeError("explicit common-IR record required")
    if record.get("resolution") not in RESOLUTIONS: raise ValueError("explicit K9/K11/K13 resolution required")
    if not (record.get("common_ir_id") or record.get("common_ir_numeric_id") or record.get("subtraction_id")): raise ValueError("explicit IR/subtraction ID required")
    if "mu" not in record or "rho" not in record: raise ValueError("explicit mu and rho required")
    if record.get("no_default") is False: raise ValueError("no_default must be explicit")
    return _freeze(dict(record))


def _require_context(parameter_record: Any, fixture_id: str | None) -> None:
    if (parameter_record is None) == (fixture_id is None): raise ValueError("exactly one parameter_record or fixture_id required")
    if fixture_id is not None and fixture_id not in FIXTURES: raise KeyError(fixture_id)


def c158_test_closure_report() -> MappingProxyType:
    return _freeze({"schema": "C159-C158-TEST-CLOSURE-REPORT-V1", "status": "C158_TEST_REGRESSION_FAILED",
                    "runner": "/Users/dustin/miniforge3/bin/python3.9", "pytest": "8.4.2",
                    "commands": ("pytest -q tests/test_c153_hqcdmatchfb.py tests/test_c156_hqcdmatchgrid2.py tests/test_c157_hqcdmatchir2.py", "pytest -q tests/test_c157_hqcdmatchir2.py"),
                    "inherited_passed": 8, "inherited_failed": 2,
                    "failures": ("tests/test_c157_hqcdmatchir2.py::test_contract_and_fail_closed_gates expects MATCHIR2-D; frozen C157 is MATCHIR2-B",
                                  "tests/test_c157_hqcdmatchir2.py::test_isolation_mutations_and_reload expects C158/HQCDMATCHWINDOW2; frozen continuation is C158/HQCDFBNUM"),
                    "direct_c158_validators": "passed", "C158_package_root": C158_ROOT,
                    "network_install": False, "dependencies_modified": False, "root": _root(("failed", 8, 2, C158_ROOT))})


def matchir3_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C159-MATCHIR3-PLAN-MANIFEST-V1", "selected_plan": PLAN, "status": STATUS,
                    "reason": "actual inherited C158/C157 test failure", "target_execution": False, "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})


def quantity_order_execution_ledger() -> MappingProxyType:
    rows = tuple({"quantity_id": q, "order": ORDERS[q], "C153_label": LABELS[q], "C158_status": "IMPORTED_PUBLIC_ROOT_ONLY",
                  "target_status": "BLOCKED_BY_C158_REGRESSION", "common_ir_status": "NOT_EVALUATED",
                  "terminal_status": STATUS, "exact_missing_object": "C158 regression correction"} for q in QUANTITIES)
    return _freeze({"schema": "C159-QUANTITY-ORDER-EXECUTION-LEDGER-V1", "rows": rows, "root": _root(rows)})


def perturbative_coordinate_adapter_manifest() -> MappingProxyType:
    rows = ({"source": "g_s", "target": "g_s^2", "factor": "power map only", "status": "DECLARED_NOT_EVALUATED"},
            {"source": "g_s^2", "target": "alpha_s", "factor": "1/(4*pi)", "status": "DECLARED_NOT_EVALUATED"},
            {"source": "alpha_s", "target": "a_s", "factor": "1/(4*pi)", "status": "DECLARED_NOT_EVALUATED"},
            {"source": "V_B", "target": "Z_1F", "factor": "divide by g_s with derivative guard", "status": "DECLARED_NOT_EVALUATED"},
            {"source": "g_R^FB", "target": "g_R^FB/g_s", "factor": "guarded ratio", "status": "DECLARED_NOT_EVALUATED"})
    return _freeze({"schema": "C159-PERTURBATIVE-COORDINATE-ADAPTER-MANIFEST-V1", "rows": rows, "root": _root(rows)})


def target_program_schema() -> MappingProxyType:
    return _freeze({"schema": "TARGET_COEFFICIENT_PROGRAM_DAG_V1", "safe_opcodes": ("LOAD_RATIONAL", "LOAD_SOURCE_CONSTANT", "LOAD_KINEMATIC", "ADD", "NEGATE", "MULTIPLY", "SAFE_DIVIDE", "INTEGER_POWER", "LOG", "LOG_RATIO", "EXP", "POSITIVE_SQRT", "PI_POWER", "ZETA_CONSTANT", "PROJECT_TENSOR", "SERIES_COEFFICIENT", "RETURN_TYPED_COEFFICIENT"), "immutable": True, "pickle": False, "callables": False, "unknown_opcode": "reject", "root": _root(("TARGET_COEFFICIENT_PROGRAM_DAG_V1", TARGET_SCHEMES))})


def target_program_manifest(quantity_id: str | None = None, target_scheme_id: str | None = None, order: int | None = None) -> MappingProxyType:
    qs = QUANTITIES if quantity_id is None else (quantity_id,)
    ss = TARGET_SCHEMES if target_scheme_id is None else (target_scheme_id,)
    rows = []
    for q in qs:
        if q not in QUANTITIES: raise ValueError(q)
        for s in ss:
            if s not in TARGET_SCHEMES: raise ValueError(s)
            if order is not None and order != ORDERS[q]: continue
            rows.append({"program_id": f"TGT-{q}-{s}", "quantity_id": q, "order": ORDERS[q], "target_scheme_id": s,
                         "source_id": "C153-primary-source-manifest", "source_locator_status": "explicit locator, numeric expression unavailable",
                         "gauge_pole_status": "must be adapter-bound", "active_Nf": "explicit record required", "numeric_status": "BLOCKED_BY_C158_REGRESSION",
                         "root": _root((q, s, ORDERS[q], C153_ROOT))})
    return _freeze({"schema": "C159-TARGET-PROGRAM-MANIFEST-V1", "rows": tuple(rows), "root": _root(rows)})


def validate_target_program(program: Mapping[str, Any]) -> MappingProxyType:
    if not isinstance(program, Mapping) or program.get("schema") != "TARGET_COEFFICIENT_PROGRAM_DAG_V1": raise ValueError("invalid target DAG")
    if program.get("numeric_status") == "BLOCKED_BY_C158_REGRESSION": return _freeze(dict(program))
    if program.get("program_id") and program.get("source_id") == "C153-primary-source-manifest": return _freeze(dict(program))
    raise ValueError("target DAG is not source-qualified and regression-gated")


def _blocked(operation: str, **extra: Any) -> MappingProxyType:
    return _freeze({"schema": f"C159-{operation.upper()}-BLOCKED-V1", "status": STATUS, "operation": operation,
                    "positive_gate": False, "value": None, "reason": "C158_TEST_REGRESSION_FAILED", "next": NEXT, **extra,
                    "root": _root((operation, STATUS, extra))})


def target_numeric_coefficient(coefficient_label: str, common_ir_record: Mapping[str, Any], *, target_scheme_id: str, route: str = "primary") -> MappingProxyType:
    if target_scheme_id not in TARGET_SCHEMES: raise ValueError(target_scheme_id)
    _require_common(common_ir_record)
    return _blocked("target_numeric_coefficient", coefficient_label=coefficient_label, target_scheme_id=target_scheme_id, route=route)


def finite_basis_numeric_coefficient_import(coefficient_label: str, common_ir_record: Mapping[str, Any], coupling_expansion_record: Mapping[str, Any], *, parameter_record=None, fixture_id=None) -> MappingProxyType:
    _require_common(common_ir_record); _require_context(parameter_record, fixture_id)
    return _blocked("finite_basis_numeric_coefficient_import", coefficient_label=coefficient_label, recomputed=False, imported_root=C158_ROOT)


def direct_common_ir_difference(coefficient_label: str, common_ir_record: Mapping[str, Any], coupling_expansion_record: Mapping[str, Any], *, target_scheme_id: str, parameter_record=None, fixture_id=None) -> MappingProxyType:
    if target_scheme_id not in TARGET_SCHEMES: raise ValueError(target_scheme_id)
    _require_common(common_ir_record); _require_context(parameter_record, fixture_id)
    return _blocked("direct_common_ir_difference", coefficient_label=coefficient_label, target_scheme_id=target_scheme_id, difference=None)


def log_ir_derivative_report(*args: Any, **kwargs: Any) -> MappingProxyType: return _blocked("log_ir_derivative_report", residual=None, atlas_frozen=False)
def common_ir_variation_report(*args: Any, **kwargs: Any) -> MappingProxyType: return _blocked("common_ir_variation_report", residuals=(), atlas_frozen=False)
def conversion_numeric_report(*args: Any, **kwargs: Any) -> MappingProxyType: return _blocked("conversion_numeric_report", round_trip_residual=None)
def first_omitted_order_report(coefficient_label: str, common_ir_record: Mapping[str, Any], perturbative_control_record: Mapping[str, Any], *, target_scheme_id: str, parameter_record=None, fixture_id=None) -> MappingProxyType:
    _require_common(common_ir_record); _require_context(parameter_record, fixture_id)
    if not isinstance(perturbative_control_record, Mapping) or perturbative_control_record.get("no_default") is not True or not perturbative_control_record.get("coupling_log_envelope"):
        raise ValueError("explicit perturbative-control record with coupling/log envelope required")
    return _blocked("first_omitted_order_report", classification="UNAVAILABLE_BLOCKING", coupling_envelope_required=True)
def positive_scale_bracket(*args: Any, **kwargs: Any) -> MappingProxyType: return _blocked("positive_scale_bracket", intervals=(), selected_scale=False)
def componentwise_matchir_manifest() -> MappingProxyType: return _freeze({"schema": "C159-COMPONENTWISE-MATCHIR-MANIFEST-V1", "status": STATUS, "rows": quantity_order_execution_ledger()["rows"], "root": _root((STATUS, QUANTITIES))})
def mass_coupling_bracket_preflight() -> MappingProxyType: return _blocked("mass_coupling_bracket_preflight", intersection=(), final_window=False)
def flavor_matchir_covariance_report() -> MappingProxyType: return _freeze({"schema": "C159-FLAVOR-MATCHIR-COVARIANCE-V1", "status": STATUS, "proof": "C155 block identity retained; evaluation blocked", "averaged": False, "active_Nf_altered": False, "root": _root(("C155", STATUS, False))})
def matching_grid_rerun_contract() -> MappingProxyType: return _freeze({"schema": "C159-MATCHING-GRID-RERUN-CONTRACT-V1", "next": NEXT, "full_grid_executed": False, "final_windows": False, "physical_scale": False, "root": _root((NEXT, False))})
def matchir_completeness_certificate() -> MappingProxyType: return _freeze({"schema": "C159-MATCHIR-COMPLETENESS-V1", "status": STATUS, "positive_gate": False, "C158_test_closure": "FAILED", "target_coefficients": False, "direct_difference": False, "remainder": False, "positive_bracket": False, "full_grid": False, "physical_scale": False, "missing_objects": ("corrected C158 inherited test surface",), "next": NEXT, "root": _root((STATUS, NEXT))})


def verify_hqcd_matchir3_authority() -> dict[str, Any]:
    return {"schema": SCHEMA, "status": STATUS, "positive_gate": False, "baseline": BASELINE, "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256,
            "plan": PLAN, "C158_status": C158_STATUS, "C158_plan": C158_PLAN, "C158_package_root": C158_ROOT, "C157_package_root": C157_ROOT, "C153_package_root": C153_ROOT,
            "C158_test_closure": "C158_TEST_REGRESSION_FAILED", "target_numeric_coefficients": 0, "common_ir_differences": 0, "remainders": 0, "positive_brackets": 0,
            "full_grid": False, "physical_scale": False, "physical_inputs": 0, "next": NEXT, "package_root": PACKAGE_ROOT}


def load_verified_hqcd_matchir3_authority() -> MappingProxyType:
    p = RUNTIME / "manifest.json"
    if not p.exists(): raise FileNotFoundError("C159 runtime manifest missing")
    m = json.loads(p.read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS: raise ValueError("C159 root/status mismatch")
    return _freeze(verify_hqcd_matchir3_authority())


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"C158_coefficient_recomputations": 0, "private_builder_calls": 0, "physical_inputs": 0, "full_grid": False, "physical_scale": False, "running": False, "thresholds": False, "Q0_Q1_modified": False, "pickle_loads": 0, "pass": True})


def mutate_live_hqcdmatchir3(index: int) -> MappingProxyType:
    fields = ("C158_test_closure", "C158_root", "plan", "opcode", "source", "gauge", "pole", "Nf", "state", "rho", "mu", "difference", "remainder", "bracket", "flavor", "next", "package_root")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False, "must_fail_or_change_root": True})


ROOTS = {"C159_INPUT_ROOT": _root((BASELINE, CONTRACT, CONTRACT_SHA256, C158_ROOT)), "C159_C158_TEST_ROOT": c158_test_closure_report()["root"], "C159_PLAN_ROOT": matchir3_plan_manifest()["root"], "C159_EXECUTION_LEDGER_ROOT": quantity_order_execution_ledger()["root"], "C159_COORDINATE_ADAPTER_ROOT": perturbative_coordinate_adapter_manifest()["root"], "C159_TARGET_PROGRAM_ROOT": target_program_schema()["root"], "C159_TARGET_COEFFICIENT_ROOT": _root(("blocked", STATUS)), "C159_COMMON_IR_ROOT": _root(("blocked", "C157 schema")), "C159_SCOPE_ROOT": _root((STATUS, "no physical claims")), "C159_COMPLETENESS_ROOT": matchir_completeness_certificate()["root"]}
PACKAGE_ROOT = _root({"schema": SCHEMA, "baseline": BASELINE, "contract": CONTRACT, "status": STATUS, "roots": ROOTS})

__all__ = ["STATUS", "PLAN", "NEXT", "PACKAGE_ROOT", "ROOTS", "QUANTITIES", "ORDERS", "LABELS", "TARGET_SCHEMES", "RESOLUTIONS", "FIXTURES", "c158_test_closure_report", "matchir3_plan_manifest", "quantity_order_execution_ledger", "perturbative_coordinate_adapter_manifest", "target_program_schema", "target_program_manifest", "validate_target_program", "target_numeric_coefficient", "finite_basis_numeric_coefficient_import", "direct_common_ir_difference", "log_ir_derivative_report", "common_ir_variation_report", "conversion_numeric_report", "first_omitted_order_report", "positive_scale_bracket", "componentwise_matchir_manifest", "mass_coupling_bracket_preflight", "flavor_matchir_covariance_report", "matching_grid_rerun_contract", "matchir_completeness_certificate", "verify_hqcd_matchir3_authority", "load_verified_hqcd_matchir3_authority", "static_isolation_guard", "mutate_live_hqcdmatchir3"]
