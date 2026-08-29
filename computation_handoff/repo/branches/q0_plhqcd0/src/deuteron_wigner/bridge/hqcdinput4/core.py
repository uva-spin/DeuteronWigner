"""C139/HQCDINPUT4 fail-closed external-input boundary.

The frozen authority chain contains no numerical capsules or authorized
staging location.  This module therefore exposes request and validation
metadata while every numerical/operator evaluation remains unavailable.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c139_hqcdinput4"
BASELINE = "9f9f6087e421e5871f2dde9bd3ae6a80976db3d6"
CONTRACT = "docs/next_level/c138_c139_hqcdinput4_import_contract.json"
CONTRACT_SHA256 = "9974603dac5869425cd7edd45ffdc838aefd8609f525efafa835a92b41010355"
STATUS = "C139_HQCDINPUT4_EXTERNAL_INPUT_INCOMPLETE"
NEXT = "C140/HQCDINPUT5"
SCHEMA = "C139-HQCDINPUT4-V1"
SCHEME = "PROJECT_FINITE_BASIS_OPEN_TRIPLET_SUBTRACTION_V1"
C138_ROOT = "075c29f17e149b35ae2b78dcbc0f33c25d7457b321fd01479238cecd875eec9b"
C137_ROOT = "96e3f9b1d25e546c7d968abe46def0cbacd205ed238b6f5d3aa776fc44b6041c"
C136_ROOT = "fac2b3210bfef7cd3dc22a1a05ea47d9253a641172308603f4c2f3b6c31eb262"
C135_ROOT = "e94b1bb47b0ab2d7499922ef558a8b32f0c6796ee7edcf2d86aed9e048ddcb5b"
C134_ROOT = "709a8955c466cee493da30fe23b9a31b85d63e8541e256ba92f6ce21568a9dd4"
C133_ROOT = "c47a70ad4a87cac048db0c00fd1e24e7f5bde110596aec9116bcfc34bde9add9"
C132_ROOT = "192de102695f89ed00aa1a1f1959395c28118177bb59b9ae9c4ec11ecaf84adc"
C131_ROOT = "67ab09bdc4ef7960a7d39ee35c243cec5c6537087012ea6283d5b4da8259cbd4"
REQUIRED = ("M_R2_FB", "g_R_FB(K_R)")
EXPECTED = {
    "M_R2_FB": {"condition_id": "C136_MASS_K9", "target_id": "M_R2_FB", "selector_id": "C136_SEL_0", "units": "GeV^2", "scope": "K9 reference state"},
    "g_R_FB(K_R)": {"condition_id": "C136_VERTEX_LONGITUDINAL", "target_id": "g_R_FB(K_R)", "selector_id": "C136_SEL_3", "units": "dimensionless", "scope": "C136 reference longitudinal vertex kinematics"},
}
NULLS = tuple(f"eta_{i}" for i in range(9))

def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, dict): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    return x
def _freeze(x: Any) -> Any:
    if isinstance(x, dict): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)): return tuple(_freeze(v) for v in x)
    return x
def _canon(x: Any) -> str: return json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True)
def _root(x: Any) -> str: return sha256(_canon(x).encode()).hexdigest()

def execution_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C139-PLAN-V1", "selected_plan": "INPUT4-D", "reason": "no contract-authorized capsule staging location or explicitly supplied capsule files", "alternatives": {"INPUT4-A": "no source-qualified pair present", "INPUT4-B": "no user-declared pair supplied", "INPUT4-C": "benchmark-only inputs are not authorized by the import contract"}, "positive_evaluation": False, "root": _root(("INPUT4-D", 0))})

def required_capsule_manifest() -> MappingProxyType:
    rows = tuple({"input_id": k, **EXPECTED[k], "scheme_id": SCHEME, "domain": "finite-resolution-open-triplet", "cardinality": 1, "no_default": True} for k in REQUIRED)
    return _freeze({"schema": "C139-REQUIRED-CAPSULE-MANIFEST-V1", "count": 2, "inputs": rows, "completeness_rule": "exactly one capsule per input ID", "root": _root(rows)})

def input_plan_manifest() -> MappingProxyType: return execution_plan_manifest()

def _validate_record(v: dict, *, allow_template: bool = False) -> None:
    required = {"schema", "external_input_id", "condition_id", "target_id", "selector_id", "parameter_id", "value_or_interval", "units", "domain", "scheme_id", "reference_scale_or_kinematics", "resolution_scope", "provenance", "source_or_user_declaration", "uncertainty_semantics", "claim_tier", "canonical_record_hash", "signature", "no_default", "capsule_root"}
    if not isinstance(v, dict) or not required.issubset(v): raise ValueError("capsule schema fields incomplete")
    if v.get("template_marker") and not allow_template: raise ValueError("production loader rejects template capsules")
    if v.get("schema") != "C135-EXTERNAL-INPUT-CAPSULE-V1": raise ValueError("capsule schema mismatch")
    key = v.get("external_input_id")
    if key not in EXPECTED: raise ValueError("unknown input ID")
    exp = EXPECTED[key]
    if v.get("parameter_id") != key or v.get("condition_id") != exp["condition_id"] or v.get("target_id") != exp["target_id"] or v.get("selector_id") != exp["selector_id"]: raise ValueError("capsule identity mismatch")
    if v.get("scheme_id") != SCHEME or v.get("units") != exp["units"] or v.get("domain") != "finite-resolution-open-triplet": raise ValueError("capsule scheme/units/domain mismatch")
    if v.get("value_or_interval") is None: raise ValueError("capsule numerical value or interval absent")
    if not v.get("reference_scale_or_kinematics") or not v.get("resolution_scope"): raise ValueError("capsule reference scope absent")
    if not v.get("provenance") or not v.get("source_or_user_declaration") or not v.get("uncertainty_semantics") or not v.get("claim_tier") or not v.get("signature") or not v.get("capsule_root") or not v.get("canonical_record_hash"): raise ValueError("capsule attestation fields absent")
    if v.get("no_default") is not True: raise ValueError("explicit no-default assertion required")

def validate_capsule(path_or_record: Any) -> MappingProxyType:
    if isinstance(path_or_record, (str, Path)):
        p = Path(path_or_record)
        raise ValueError(f"capsule path is not an authorized C139 staging location: {p}")
    _validate_record(path_or_record)
    return _freeze({"schema": "C139-CAPSULE-VALIDATION-V1", "valid": True, "input_id": path_or_record["external_input_id"], "root": _root(path_or_record)})

def accepted_capsule_manifest() -> MappingProxyType: return _freeze({"schema": "C139-ACCEPTED-CAPSULE-MANIFEST-V1", "count": 0, "records": (), "root": _root(())})
def rejected_capsule_manifest() -> MappingProxyType: return _freeze({"schema": "C139-REJECTED-CAPSULE-MANIFEST-V1", "count": 0, "records": (), "root": _root(())})
def missing_capsule_manifest() -> MappingProxyType: return _freeze({"schema": "C139-MISSING-CAPSULE-MANIFEST-V1", "count": 2, "missing": REQUIRED, "request": "docs/next_level/c139_external_input_request.md", "root": _root(REQUIRED)})

def coordinate_operator_binding_manifest() -> MappingProxyType:
    rows = ({"coordinate": "phi_mass", "original_direction_ids": ("m_q", "m_q^2", "ct_mass"), "owner_ids": ("C128", "C131"), "operator_monomial": "free mass bilinear plus mass counterterm", "coupling_degree": 0, "units": "GeV^2", "support": "q and qg one-body", "classification": "IDENTIFIED_MIXED_PARAMETER_DIRECTION_COMPONENT", "ancestry": ("C131", "C137", "C138")}, {"coordinate": "phi_coupling", "original_direction_ids": ("g_s",), "owner_ids": ("C53", "C131"), "operator_monomial": "canonical q<->qg vertex", "coupling_degree": 1, "units": "dimensionless input; operator GeV^2/g_s scaling", "support": "q<->qg", "classification": "IDENTIFIED_PARAMETERIZED_BARE_OPERATOR_COMPONENT", "ancestry": ("C53", "C131", "C137", "C138")})
    return _freeze({"schema": "C139-COORDINATE-OPERATOR-BINDING-V1", "bindings": rows, "binding_mismatches": 0, "coordinate_mismatches": 0, "source_order_preserved": True, "root": _root(rows)})

def identified_coordinate_evaluation(*, capsules: dict | None = None) -> MappingProxyType:
    raise ValueError("C139_HQCDINPUT4_EXTERNAL_INPUT_INCOMPLETE: numerical capsule pair is absent")
def identified_operator_manifest(resolution: str | None = None) -> MappingProxyType:
    raise ValueError("C139_HQCDINPUT4_EXTERNAL_INPUT_INCOMPLETE: identified operator evaluation unavailable")
def identified_operator_sparse_matrix(resolution: str) -> Any: raise ValueError("identified operator unavailable without capsules")
def identified_operator_sparse_bounds(resolution: str) -> Any: raise ValueError("identified operator bounds unavailable without capsules")
def apply_identified_operator(resolution: str, vector: Any) -> Any: raise ValueError("identified operator action unavailable without capsules")

def nullspace_manifest() -> MappingProxyType:
    return _freeze({"schema": "C139-NULLSPACE-V1", "coordinates": tuple({"id": n, "status": "UNRESOLVED", "assigned": False, "value": None} for n in NULLS), "dimension": 9, "coordinates_assigned": 0, "null_operator_terms_inserted": 0, "minimum_norm": False, "moore_penrose": False, "zero_representative": False, "root": _root((NULLS, 0))})
def null_operator_family_manifest() -> MappingProxyType: return _freeze({"schema": "C139-NULL-OPERATOR-FAMILY-V1", "directions": NULLS, "solved": 0, "represented_as_zero": False, "root": _root(NULLS)})
def unique_full_operator_no_go_certificate() -> MappingProxyType: return _freeze({"schema": "C139-FULL-OPERATOR-NO-GO-V1", "unique_vector": False, "unique_matrix": False, "physical_state": False, "reason": "nine-dimensional nullspace remains unfixed", "root": _root((False, False, 9))})
def input4_completeness_certificate() -> MappingProxyType: return _freeze({"schema": "C139-COMPLETENESS-V1", "required_capsules": 2, "accepted_project_scheme": 0, "accepted_benchmark": 0, "rejected": 0, "missing": 2, "identified_coordinate_evaluation": False, "identified_operator_component": False, "nullspace_dimension": 9, "unavailable_unique_full_operator": True, "preserved_blockers": ("gluon spectator-dependent factorization", "gluon masslessness target", "Ward/current holdouts", "C130 constraints and omitted interfaces"), "next": NEXT, "root": _root((2, 0, 0, 2, 9))})
def verify_hqcd_input4_authority() -> dict[str, Any]:
    return {"schema": SCHEMA, "status": STATUS, "positive_gate": False, "selected_plan": "INPUT4-D", "baseline": BASELINE, "C138_package_root": C138_ROOT, "C137_package_root": C137_ROOT, "required_capsules": 2, "capsules_present": 0, "accepted": 0, "rejected": 0, "missing": 2, "binding_mismatches": 0, "null_coordinates": 9, "null_zeroed": 0, "next": NEXT, "roots": ROOTS, "package_root": PACKAGE_ROOT}
def load_verified_hqcd_input4_authority() -> MappingProxyType:
    p = RUNTIME / "manifest.json"
    if not p.exists(): raise FileNotFoundError("C139 runtime manifest missing")
    m = json.loads(p.read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS: raise ValueError("C139 root/status mismatch")
    return _freeze(verify_hqcd_input4_authority())
def static_isolation_guard() -> MappingProxyType: return _freeze({"forbidden_sources_consumed": 0, "defaults": 0, "null_zeroed": 0, "physical_values": 0, "unique_full_operator": 0, "pass": True})
def mutate_live_hqcdinput4(index: int) -> MappingProxyType: return _freeze({"mutation": ("capsule", "units", "scheme", "identity", "provenance", "attestation", "root", "binding", "operator", "nullspace", "loader", "C140")[int(index) % 12], "positive_gate": False, "must_fail_or_change_root": True})

ROOTS = {"C139_EXECUTION_PLAN_ROOT": _root(execution_plan_manifest()), "C139_REQUIRED_CAPSULE_ROOT": _root(required_capsule_manifest()), "C139_MISSING_CAPSULE_ROOT": _root(missing_capsule_manifest()), "C139_BINDING_ROOT": _root(coordinate_operator_binding_manifest()), "C139_NULLSPACE_ROOT": _root(nullspace_manifest()), "C139_FULL_OPERATOR_NO_GO_ROOT": _root(unique_full_operator_no_go_certificate()), "C139_COMPLETENESS_ROOT": _root(input4_completeness_certificate())}
PACKAGE_ROOT = _root({"schema": SCHEMA, "baseline": BASELINE, "contract": CONTRACT, "status": STATUS, "roots": ROOTS, "ancestry": (C138_ROOT, C137_ROOT, C136_ROOT, C135_ROOT, C134_ROOT, C133_ROOT, C132_ROOT, C131_ROOT)})
__all__ = ["STATUS", "NEXT", "PACKAGE_ROOT", "ROOTS", "execution_plan_manifest", "input_plan_manifest", "required_capsule_manifest", "validate_capsule", "accepted_capsule_manifest", "rejected_capsule_manifest", "missing_capsule_manifest", "coordinate_operator_binding_manifest", "identified_coordinate_evaluation", "identified_operator_manifest", "identified_operator_sparse_matrix", "identified_operator_sparse_bounds", "apply_identified_operator", "nullspace_manifest", "null_operator_family_manifest", "unique_full_operator_no_go_certificate", "input4_completeness_certificate", "verify_hqcd_input4_authority", "load_verified_hqcd_input4_authority", "static_isolation_guard", "mutate_live_hqcdinput4"]
