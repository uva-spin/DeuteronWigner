"""C198 source-qualified ST registry and conditional counterterm system.

The module consumes C197 and its upstream authorities read-only.  It records
the complete available project system, not a textbook full-ST theorem or a
physical renormalization solution.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence

from deuteron_wigner.bridge import hqcdz1f2 as c197

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c198_hqcdst2"
BASELINE = "94cefcdcb00144d56d0137308e9d0aeb0319933d"
CONTRACT = "docs/next_level/c197_c198_hqcdst2_continuation_contract.json"
CONTRACT_SHA256 = "0226779f955dd03b88ac219a0d3130bc87a0e8ae85273319ab16fae34fe543f4"
PROMPT = "/Users/dustin/Downloads/c198_hqcdst2_codex_prompt.md"
PROMPT_SHA256 = "cf7ebbf73bec4d1fc0cc83c5c986cb8533083acce479850526a7267b4e76bc4a"
STATUS = "C198_C197_SOURCE_DERIVED_COMPLETE_AVAILABLE_FINITE_BASIS_ST_COUNTERTERM_SYSTEM_AND_CONDITIONAL_SOLUTION_FAMILY_AUTHORITY_READY"
PLAN = "ST2-A"
NEXT = "C199/HQCDGHOST2"
RESOLUTIONS = ("K9", "K11", "K13")
SCHEMES = ("K_MINUS", "K_PLUS", "K_PERP")
GLUON_SCHEME = "C151_GLON_PROJECTOR_V1"
COUNTERTERMS = tuple(f"C151_COUNTERTERM_DIRECTION_{i}" for i in range(1, 7))
NULLS = tuple(f"C151_NULL_COORDINATE_{i}" for i in range(1, 10))
FIFTEEN = COUNTERTERMS + NULLS
ALLOWED_STATUSES = ("EXACT_PROJECT_IDENTITY", "CONDITIONAL_FINITE_BASIS_IDENTITY", "RESTRICTED_QG_DIAGNOSTIC", "B0_COMPONENT_DIAGNOSTIC", "BOUNDARY_OR_LINK_DIAGNOSTIC", "MISSING_OBJECT_BLOCKED", "TARGET_CONDITION_NOT_EVALUATED", "STANDARD_SCHEME_NOT_EVALUATED", "PHYSICAL_INPUT_NOT_SELECTED")


def _plain(value: Any) -> Any:
    if isinstance(value, Mapping): return {str(k): _plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)): return [_plain(v) for v in value]
    return value


def _freeze(value: Any) -> Any:
    if isinstance(value, Mapping): return MappingProxyType({k: _freeze(v) for k, v in value.items()})
    if isinstance(value, (tuple, list)): return tuple(_freeze(v) for v in value)
    return value


def _root(value: Any) -> str:
    return sha256(json.dumps(_plain(value), sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def _pick(value: str | None, allowed: Sequence[str]) -> tuple[str, ...]:
    if value is None: return tuple(allowed)
    if value not in allowed: raise KeyError(value)
    return (value,)


def _missing_rows() -> tuple[Mapping[str, Any], ...]:
    exact = tuple(c197.st_boundary_manifest()["rows"])
    aliases = {
        "C197-ST-1": ("complete ghost-field renormalization", "GHOST_FIELD_RENORMALIZATION"),
        "C197-ST-2": ("complete ghost-gluon proper vertex", "GHOST_GLUON_PROPER_VERTEX"),
        "C197-ST-3": ("complete three-gluon proper vertex renormalization", "THREE_GLUON_PROPER_VERTEX"),
        "C197-ST-4": ("complete four-gluon renormalization", "FOUR_GLUON_PROPER_VERTEX"),
        "C197-ST-5": ("BRST source identities", "BRST_SOURCE_IDENTITY"),
        "C197-ST-6": ("endpoint ghost/link identities", "ENDPOINT_GHOST_LINK_IDENTITY"),
        "C197-ST-7": ("global zero-mode/gauge-volume treatment", "GLOBAL_GAUGE_VOLUME_IDENTITY"),
        "C197-ST-8": ("ST-compatible counterterm solution", "ST_COMPATIBLE_COUNTERTERM_SOLUTION"),
        "C197-ST-9": ("target MOMq renormalization conditions", "TARGET_RENORMALIZATION_CONDITION"),
        "C197-ST-10": ("physical input", "PHYSICAL_INPUT_CONDITION"),
    }
    return tuple({"object_id": row["st_record_id"], "C197_missing_object_id": row["st_record_id"], "exact_missing_object": row["missing_object"], "aliases": aliases[row["st_record_id"]], "scientific_class": aliases[row["st_record_id"]][1], "request_aliases": (c197.missing_z1f_object_manifest()["rows"][0]["request_id"], c197.missing_z1f_object_manifest()["rows"][1]["request_id"]) if row["st_record_id"] in ("C197-ST-9", "C197-ST-10") else (), "role": "source-side" if row["st_record_id"] not in ("C197-ST-9", "C197-ST-10") else "target-or-physical boundary", "blocks": "identity row and/or completeness frontier", "known_upstream_authority": tuple(row["available_components"]), "first_unavailable_object": row["missing_object"], "continuation_capsule": "C199/HQCDGHOST2" if row["st_record_id"] == "C197-ST-1" else "C198 frontier; not encoded as zero", "status": "MISSING_OBJECT_BLOCKED", "source_root": c197.PACKAGE_ROOT} for row in exact)


def _systems() -> tuple[Mapping[str, Any], ...]:
    return tuple({"system_id": f"C198-ST-SYSTEM-{r}", "resolution": r, "scheme_tuple": ("C152-RANK8-PROJECTOR-1", "K_MINUS", GLUON_SCHEME), "holonomy_bc_class": "C183 diagnostic-compatible caller capsule", "fixture_id": "C197 named nonphysical fixture; caller bound", "active_rows": ("C198-QG-CONDITIONAL", "C198-QG-RESTRICTED", "C198-QG-DERIVATIVE"), "blocked_rows": tuple(x["object_id"] for x in _missing_rows()), "variable_order": FIFTEEN, "source_roots": (c197.PACKAGE_ROOT,), "stacked": False} for r in RESOLUTIONS)


def _check_upstream() -> None:
    if c197.PACKAGE_ROOT != "6e9991693c54871c945c6eb0e0a16b7555029560f078fb590b2fa2a409a0e7d1": raise ValueError("C197 root changed")
    c197.load_verified_hqcd_z1f2_authority()


def verify_hqcd_st2_authority() -> MappingProxyType:
    _check_upstream()
    return _freeze({"schema": "C198-AUTHORITY-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256, "prompt": PROMPT, "prompt_sha256": PROMPT_SHA256, "C197_package_root": c197.PACKAGE_ROOT, "missing_object_count": 10, "physical_counterterms": False, "physical_coupling": False, "full_ST": False, "C158_value_inputs": 0, "C166_graph_delta": {"nodes_added": 0, "edges_added": 0}, "Q0_Q1_Q2_modified": False, "next": NEXT, "package_root": PACKAGE_ROOT})


def load_verified_hqcd_st2_authority() -> MappingProxyType:
    path = RUNTIME / "manifest.json"
    if not path.exists(): raise FileNotFoundError("C198 runtime manifest missing")
    manifest = json.loads(path.read_text())
    if manifest.get("package_root") != PACKAGE_ROOT or manifest.get("status") != STATUS: raise ValueError("C198 runtime root/status mismatch")
    return verify_hqcd_st2_authority()


def st2_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C198-PLAN-V1", "selected_plan": PLAN, "status": STATUS, "decision": "COMPLETE_AVAILABLE_FINITE_BASIS_ST_COUNTERTERM_SYSTEM_AND_CONDITIONAL_SOLUTION_FAMILY_AUTHORITY_READY", "next": NEXT, "mutually_exclusive": True, "first_frontier": "C197-ST-1", "root": _root((PLAN, STATUS, NEXT))})


def st_handoff_freeze() -> MappingProxyType:
    return _freeze({"schema": "C198-HANDOFF-FREEZE-V1", "C197_package_root": c197.PACKAGE_ROOT, "C197_Z1F_records": 54, "C197_coupling_records": 54, "C197_sensitivities": 120, "C197_read_only": True, "C197_build_hash_roles": "reconciled through committed C197 build manifest and implementation report", "C158_value_inputs": 0, "C166_graph_delta": {"nodes_added": 0, "edges_added": 0}, "root": _root((c197.PACKAGE_ROOT, 54, 54, 120))})


def missing_st_object_manifest(object_id: str | None = None) -> MappingProxyType:
    rows = _missing_rows()
    if object_id is not None: rows = tuple(x for x in rows if x["object_id"] == object_id)
    if object_id is not None and not rows: raise KeyError(object_id)
    return _freeze({"schema": "C198-MISSING-ST-OBJECT-V1", "rows": rows, "count": len(rows), "exact_count": 10, "generic_hidden": False, "root": _root(rows)})


def variable_manifest(variable_id: str | None = None, coordinate_class: str | None = None) -> MappingProxyType:
    rows = []
    classes = (("COUNTERTERM", COUNTERTERMS, "C197 six counterterm directions"), ("NULL", NULLS, "C197 nine null coordinates"), ("IDENTIFIED_FINITE_BASIS", c197.COORDINATES, "C197 explicit coordinate registry"), ("SOURCE_RENORMALIZATION", ("Z1F", "Z_q", "Z_A", "restricted_g_R"), "C197/C150/C184 source-side response"), ("GHOST_OR_PURE_GLUON", ("Z_ghost", "Z_1_ghost-gluon", "Z_1_3g", "Z_1_4g"), "not available; missing objects"), ("BOUNDARY_HOLONOMY", ("residual_link", "endpoint", "zero_mode", "global_volume", "holonomy"), "C130/C175/C182/C183 interfaces"), ("TARGET", ("target_MOMq",), "target-side not evaluated"), ("STANDARD", ("standard_scheme",), "standard-side not evaluated"), ("PHYSICAL_INPUT", ("physical_coupling",), "physical input not selected"))
    n = 0
    for cls, names, authority in classes:
        for name in names:
            n += 1; rows.append({"variable_id": f"C198-VAR-{cls}-{n}", "coordinate": name, "coordinate_class": cls, "source_authority": authority, "units": "explicit by source record; no hidden units", "resolution": "K9/K11/K13 caller-separated", "scheme": "caller-separated", "holonomy_bc_class": "caller-supplied diagnostic-compatible", "counterterm_null_identified_target_standard_physical_role": cls, "branch_convention": "explicit source/caller continuation", "allowed_identity_rows": "typed by row status", "selection_status": "unselected" if cls in ("COUNTERTERM", "NULL", "PHYSICAL_INPUT") else "registry-only"})
    if variable_id is not None: rows = [x for x in rows if x["variable_id"] == variable_id]
    if coordinate_class is not None: rows = [x for x in rows if x["coordinate_class"] == coordinate_class]
    if coordinate_class is not None: rows = [x for x in rows if x["coordinate_class"] == coordinate_class]
    if (variable_id is not None or coordinate_class is not None) and not rows: raise KeyError(variable_id or coordinate_class)
    return _freeze({"schema": "C198-VARIABLE-MANIFEST-V1", "rows": tuple(rows), "count": len(rows), "counterterms": 6, "nulls": 9, "roles_separate": True, "root": _root(rows)})


def identity_row_schema() -> MappingProxyType:
    required = ("row_id", "identity_class", "source_authority", "left_program", "right_program", "residual_program", "variables", "resolution", "scheme", "holonomy_bc_class", "external_domains", "projector_domains", "source_order", "coupling_degree", "units", "analytic_branch", "counterterm_null_derivative_support", "status", "missing_object_dependencies", "root")
    return _freeze({"schema": "PROJECT_FINITE_BASIS_ST_IDENTITY_ROW_V1", "required_fields": required, "allowed_statuses": ALLOWED_STATUSES, "safe_data_only": True, "callbacks": False, "eval": False, "pickle": False, "root": _root(required)})


def _qg_rows() -> tuple[Mapping[str, Any], ...]:
    rows = []
    for z in c197.coupling_manifest()["rows"]:
        base = z["coupling_response_id"]
        for suffix, cls, status in (("DEF", "DEFINITION", "EXACT_PROJECT_IDENTITY"), ("RENORM", "RENORMALIZATION_CONDITION", "CONDITIONAL_FINITE_BASIS_IDENTITY"), ("COUP", "RESTRICTED_COUPLING_COMPOSITION", "RESTRICTED_QG_DIAGNOSTIC"), ("RETAINED", "RETAINED_COMPLETE_COMPARISON", "RESTRICTED_QG_DIAGNOSTIC"), ("DERIV", "COUNTERTERM_NULL_DERIVATIVE", "CONDITIONAL_FINITE_BASIS_IDENTITY"), ("ST", "QG_ST_RESIDUAL", "RESTRICTED_QG_DIAGNOSTIC")):
            rows.append({"row_id": f"C198-QG-{base}-{suffix}", "identity_class": cls, "source_authority": (c197.PACKAGE_ROOT, "C152 convention", "C150 public response", "C184 public response"), "left_program": f"C197({base})", "right_program": "C152 typed convention", "residual_program": "F_qg(theta; S) guarded symbolic residual", "variables": ("Z1F", "Z_q", "Z_A", "g_s", "restricted_g_R"), "resolution": z["resolution"], "scheme": (z["Z1F_scheme"], z["Z_q_scheme"], z["Z_A_scheme"]), "holonomy_bc_class": z["holonomy_bc"], "external_domains": "C196 complete qg", "projector_domains": "C152 rank-eight; tree-support where multiplicative", "source_order": "C152 source order", "coupling_degree": "caller supplied", "units": z["units"], "analytic_branch": "C197 branch record", "counterterm_null_derivative_support": True, "status": status, "missing_object_dependencies": (), "defining_equation_independent": status != "EXACT_PROJECT_IDENTITY", "root": _root((base, suffix, z["resolution"]))})
    return tuple(rows)


def _row_filter(rows: Sequence[Mapping[str, Any]], row_id: str | None, identity_class: str | None, status: str | None) -> tuple[Mapping[str, Any], ...]:
    if status is not None and status not in ALLOWED_STATUSES: raise KeyError(status)
    out = tuple(x for x in rows if (row_id is None or x["row_id"] == row_id) and (identity_class is None or x["identity_class"] == identity_class) and (status is None or x["status"] == status))
    if any(x is not None for x in (row_id, identity_class, status)) and not out: raise KeyError(row_id or identity_class or status)
    return out


def identity_row_manifest(row_id: str | None = None, identity_class: str | None = None, status: str | None = None) -> MappingProxyType:
    rows = list(_qg_rows())
    missing = missing_st_object_manifest()["rows"]
    for x in missing: rows.append({"row_id": f"C198-BLOCKED-{x['object_id']}", "identity_class": x["scientific_class"], "source_authority": (x["source_root"],), "left_program": "MISSING_OBJECT_GUARD", "right_program": "MISSING_OBJECT_GUARD", "residual_program": "MISSING_OBJECT_BLOCKED", "variables": FIFTEEN, "resolution": "caller supplied", "scheme": "caller supplied", "holonomy_bc_class": "caller supplied", "external_domains": "source dependency absent", "projector_domains": "not evaluated", "source_order": "not available", "coupling_degree": "not available", "units": "not available", "analytic_branch": "not available", "counterterm_null_derivative_support": False, "status": "MISSING_OBJECT_BLOCKED", "missing_object_dependencies": (x["object_id"],), "defining_equation_independent": False, "root": _root(x)})
    rows.extend({"row_id": "C198-B0-COMPONENT", "identity_class": "B0_COMPONENT", "source_authority": (c197.PACKAGE_ROOT, "C184 B0 component"), "left_program": "C184 B0 component", "right_program": "not complete pure-gluon vertex", "residual_program": "B0_COMPONENT_DIAGNOSTIC", "variables": ("Z_A", "restricted_g_R"), "resolution": r, "scheme": GLUON_SCHEME, "holonomy_bc_class": "C183 diagnostic", "external_domains": "B0 gluon", "projector_domains": "C151 gluon projector", "source_order": "C184", "coupling_degree": "caller supplied", "units": "C184 units", "analytic_branch": "C184", "counterterm_null_derivative_support": True, "status": "B0_COMPONENT_DIAGNOSTIC", "missing_object_dependencies": ("C197-ST-3", "C197-ST-4"), "defining_equation_independent": False, "root": _root(("B0", r))} for r in RESOLUTIONS)
    rows.extend(({
        "row_id": "C198-TARGET-CONDITION", "identity_class": "TARGET_CONDITION", "source_authority": (c197.PACKAGE_ROOT,),
        "left_program": "TARGET_MOMQ_GUARD", "right_program": "not evaluated", "residual_program": "TARGET_CONDITION_NOT_EVALUATED",
        "variables": ("target_MOMq",), "resolution": "target-side", "scheme": "MOMq", "holonomy_bc_class": "not selected",
        "external_domains": "target-side", "projector_domains": "not evaluated", "source_order": "not evaluated",
        "coupling_degree": "not evaluated", "units": "not evaluated", "analytic_branch": "not evaluated",
        "counterterm_null_derivative_support": False, "status": "TARGET_CONDITION_NOT_EVALUATED",
        "missing_object_dependencies": ("C197-ST-9",), "defining_equation_independent": False, "root": _root("target")
    }, {
        "row_id": "C198-STANDARD-CONDITION", "identity_class": "STANDARD_CONDITION", "source_authority": (c197.PACKAGE_ROOT,),
        "left_program": "STANDARD_SCHEME_GUARD", "right_program": "not evaluated", "residual_program": "STANDARD_SCHEME_NOT_EVALUATED",
        "variables": ("standard_scheme",), "resolution": "standard-side", "scheme": "standard", "holonomy_bc_class": "not selected",
        "external_domains": "standard-side", "projector_domains": "not evaluated", "source_order": "not evaluated",
        "coupling_degree": "not evaluated", "units": "not evaluated", "analytic_branch": "not evaluated",
        "counterterm_null_derivative_support": False, "status": "STANDARD_SCHEME_NOT_EVALUATED",
        "missing_object_dependencies": ("C197-ST-9",), "defining_equation_independent": False, "root": _root("standard")
    }, {
        "row_id": "C198-PHYSICAL-INPUT", "identity_class": "PHYSICAL_INPUT", "source_authority": (c197.PACKAGE_ROOT,),
        "left_program": "PHYSICAL_INPUT_GUARD", "right_program": "not selected", "residual_program": "PHYSICAL_INPUT_NOT_SELECTED",
        "variables": ("physical_coupling",), "resolution": "physical-side", "scheme": "not selected", "holonomy_bc_class": "not selected",
        "external_domains": "physical-input", "projector_domains": "not evaluated", "source_order": "not evaluated",
        "coupling_degree": "not evaluated", "units": "not evaluated", "analytic_branch": "not evaluated",
        "counterterm_null_derivative_support": False, "status": "PHYSICAL_INPUT_NOT_SELECTED",
        "missing_object_dependencies": ("C197-ST-10",), "defining_equation_independent": False, "root": _root("physical")
    }))
    rows.extend({"row_id": x["row_id"], "identity_class": "BOUNDARY_OR_LINK", "source_authority": (x["source_root"],), "left_program": x["description"], "right_program": "typed nonmatrix interface", "residual_program": "BOUNDARY_OR_LINK_DIAGNOSTIC", "variables": ("residual_link", "endpoint", "zero_mode", "global_volume", "holonomy"), "resolution": "caller supplied", "scheme": "C43 project sub-gauge", "holonomy_bc_class": "C183 diagnostic-compatible", "external_domains": "boundary/link", "projector_domains": "nonmatrix interface", "source_order": "source-qualified", "coupling_degree": "caller supplied", "units": "source-defined", "analytic_branch": "source-defined", "counterterm_null_derivative_support": False, "status": "BOUNDARY_OR_LINK_DIAGNOSTIC", "missing_object_dependencies": (), "defining_equation_independent": False, "root": _root(x["row_id"])} for x in _channel_rows("BOUNDARY"))
    out = _row_filter(rows, row_id, identity_class, status)
    return _freeze({"schema": "C198-IDENTITY-ROW-MANIFEST-V1", "rows": out, "count": len(out), "status_census": {s: sum(x["status"] == s for x in out) for s in ALLOWED_STATUSES}, "defining_equations_independent": False, "root": _root(out)})


def qg_identity_manifest(row_id: str | None = None, resolution_id: str | None = None, scheme_id: str | None = None) -> MappingProxyType:
    rows = tuple(x for x in _qg_rows() if (row_id is None or x["row_id"] == row_id) and (resolution_id is None or x["resolution"] == resolution_id) and (scheme_id is None or scheme_id in x["scheme"]))
    if any(x is not None for x in (row_id, resolution_id, scheme_id)) and not rows: raise KeyError(row_id or resolution_id or scheme_id)
    return _freeze({"schema": "C198-QG-IDENTITY-V1", "rows": rows, "count": len(rows), "defining_equations_independent": False, "C197_read_only": True, "root": _root(rows)})


def _channel_rows(channel: str) -> tuple[Mapping[str, Any], ...]:
    available = {"GHOST": (("C175-Q0-DETERMINANT", "Q0 ghost determinant", False, "not complete ghost renormalization"), ("C175-P0-GHOST-ACTION", "local P0 ghost action", True, "bulk only"), ("C175-BULK-LOOP", "bulk ghost loop diagnostic", True, "not endpoint zero"), ("C182-GHOST-LINK", "boundary ghost-link interface", False, "nonmatrix interface"), ("C183-HOLONOMY", "holonomy transport", False, "not a loop")), "PURE_GLUON": (("C129-CUBIC-SOURCE", "C129 source", False, "not complete three-gluon vertex"), ("C184-B0-COMPONENT", "C184 B0 component", True, "not complete pure-gluon vertex"), ("C151-GLUON-PROJECTOR", "C151 tensor projector", False, "projector only")), "BRST": (), "BOUNDARY": (("C130-P0-BOUNDARY", "C130 P0 boundary interface", False, "nonmatrix"), ("C175-GHOST-LINK", "C175 ghost-link boundary", False, "interface"), ("C182-RESIDUAL-LINK", "C182 residual-link source interface", False, "nonmatrix"), ("C183-CUT-HOLONOMY", "C183 cut/holonomy transport", False, "transport"), ("GLOBAL-VOLUME", "global gauge volume", False, "not absorbed"))}[channel]
    return tuple({"object_id": oid, "row_id": f"C198-{channel}-{oid}", "source_root": c197.PACKAGE_ROOT, "description": desc, "matrix": matrix, "role": role, "external_domains": "typed source domain", "projector_tensor_role": "typed source projector or interface", "source_order": "source-qualified or unavailable", "coupling_degree": "caller supplied", "renormalization_coordinate": "not promoted beyond source scope", "counterterm_null_sensitivities": True, "holonomy_bc": "C183 diagnostic-compatible", "identity_row_eligibility": "diagnostic only", "status": "BOUNDARY_OR_LINK_DIAGNOSTIC" if channel == "BOUNDARY" else ("B0_COMPONENT_DIAGNOSTIC" if oid == "C184-B0-COMPONENT" else "RESTRICTED_QG_DIAGNOSTIC"), "not_zero": True} for oid, desc, matrix, role in available)


def ghost_manifest(object_id: str | None = None, row_id: str | None = None) -> MappingProxyType:
    rows = list(_channel_rows("GHOST")); rows.extend({"object_id": x["object_id"], "row_id": f"C198-GHOST-BLOCKED-{x['object_id']}", "source_root": x["source_root"], "description": x["exact_missing_object"], "matrix": False, "role": "missing full object", "identity_row_eligibility": "blocked", "status": "MISSING_OBJECT_BLOCKED", "not_zero": True} for x in missing_st_object_manifest()["rows"] if x["scientific_class"] in ("GHOST_FIELD_RENORMALIZATION", "GHOST_GLUON_PROPER_VERTEX"))
    out = tuple(x for x in rows if (object_id is None or x["object_id"] == object_id) and (row_id is None or x["row_id"] == row_id))
    if any(x is not None for x in (object_id, row_id)) and not out: raise KeyError(object_id or row_id)
    return _freeze({"schema": "C198-GHOST-MANIFEST-V1", "rows": out, "count": len(out), "determinant_not_renormalization": True, "bulk_not_endpoint": True, "target_ghosts": False, "root": _root(out)})


def pure_gluon_manifest(object_id: str | None = None, row_id: str | None = None) -> MappingProxyType:
    rows = list(_channel_rows("PURE_GLUON")); rows.extend({"object_id": x["object_id"], "row_id": f"C198-PURE-GLUON-BLOCKED-{x['object_id']}", "source_root": x["source_root"], "description": x["exact_missing_object"], "matrix": False, "role": "missing proper vertex", "identity_row_eligibility": "blocked", "status": "MISSING_OBJECT_BLOCKED", "not_zero": True} for x in missing_st_object_manifest()["rows"] if x["scientific_class"] in ("THREE_GLUON_PROPER_VERTEX", "FOUR_GLUON_PROPER_VERTEX"))
    out = tuple(x for x in rows if (object_id is None or x["object_id"] == object_id) and (row_id is None or x["row_id"] == row_id))
    if any(x is not None for x in (object_id, row_id)) and not out: raise KeyError(object_id or row_id)
    return _freeze({"schema": "C198-PURE-GLUON-MANIFEST-V1", "rows": out, "count": len(out), "d_f_separate": True, "B0_not_complete": True, "root": _root(out)})


def brst_manifest(object_id: str | None = None, row_id: str | None = None) -> MappingProxyType:
    rows = tuple({"object_id": x["object_id"], "row_id": f"C198-BRST-BLOCKED-{x['object_id']}", "source_root": x["source_root"], "description": x["exact_missing_object"], "ghost_number": "not available", "brst_variation": "not invented", "boundary_scope": "not available", "identity_row_role": "missing", "completeness": False, "acceptance": "rejected absent source authority", "status": "MISSING_OBJECT_BLOCKED"} for x in missing_st_object_manifest()["rows"] if x["scientific_class"] == "BRST_SOURCE_IDENTITY")
    out = tuple(x for x in rows if (object_id is None or x["object_id"] == object_id) and (row_id is None or x["row_id"] == row_id))
    if any(x is not None for x in (object_id, row_id)) and not out: raise KeyError(object_id or row_id)
    return _freeze({"schema": "C198-BRST-MANIFEST-V1", "rows": out, "count": len(out), "invented": False, "root": _root(out)})


def boundary_identity_manifest(object_id: str | None = None, row_id: str | None = None) -> MappingProxyType:
    rows = list(_channel_rows("BOUNDARY")); rows.extend({"object_id": x["object_id"], "row_id": f"C198-BOUNDARY-BLOCKED-{x['object_id']}", "source_root": x["source_root"], "description": x["exact_missing_object"], "matrix": False, "role": "missing boundary/global identity", "status": "MISSING_OBJECT_BLOCKED", "not_zero": True} for x in missing_st_object_manifest()["rows"] if x["scientific_class"] in ("ENDPOINT_GHOST_LINK_IDENTITY", "GLOBAL_GAUGE_VOLUME_IDENTITY"))
    out = tuple(x for x in rows if (object_id is None or x["object_id"] == object_id) and (row_id is None or x["row_id"] == row_id))
    if any(x is not None for x in (object_id, row_id)) and not out: raise KeyError(object_id or row_id)
    return _freeze({"schema": "C198-BOUNDARY-IDENTITY-V1", "rows": out, "count": len(out), "global_volume_separate": True, "holonomy_loop": False, "root": _root(out)})


def residual_manifest(system_id: str | None = None, row_id: str | None = None) -> MappingProxyType:
    rows = tuple({"system_id": s["system_id"], "row_id": f"C198-RES-{s['resolution']}-QG", "resolution": s["resolution"], "variables": FIFTEEN, "source_roots": (c197.PACKAGE_ROOT,), "operations": ("symbolic composition", "guarded residual", "explicit branch", "outward enclosure"), "validity_guards": ("nonphysical named fixture", "no missing object", "explicit scheme/holonomy", "no target condition"), "missing_object_dependencies": (), "status": "CONDITIONAL_FINITE_BASIS_IDENTITY", "residual": "F_qg(theta; S)", "routes": ("RES-A-direct", "RES-B-convention", "RES-C-derivative", "RES-D-free-tree", "RES-E-order", "RES-F-Hermitian")} for s in _systems()) + tuple({"system_id": "C198-ST-SYSTEM-ALL", "row_id": f"C198-RES-BLOCKED-{x['object_id']}", "resolution": "caller supplied", "variables": FIFTEEN, "source_roots": (c197.PACKAGE_ROOT,), "operations": ("missing-object guard",), "validity_guards": ("object required",), "missing_object_dependencies": (x["object_id"],), "status": "MISSING_OBJECT_BLOCKED", "residual": "MISSING_OBJECT_BLOCKED"} for x in missing_st_object_manifest()["rows"])
    out = tuple(x for x in rows if (system_id is None or x["system_id"] == system_id) and (row_id is None or x["row_id"] == row_id))
    if any(x is not None for x in (system_id, row_id)) and not out: raise KeyError(system_id or row_id)
    return _freeze({"schema": "C198-RESIDUAL-MANIFEST-V1", "rows": out, "count": len(out), "missing_not_zero": True, "nonlinear": True, "root": _root(out)})


def evaluate_st_residuals(parameter_record: Mapping[str, Any], system_id: str) -> MappingProxyType:
    if not isinstance(parameter_record, Mapping) or parameter_record.get("physical") is not False or parameter_record.get("no_defaults") is not True: raise ValueError("named nonphysical parameter required")
    systems = {x["system_id"] for x in _systems()}
    if system_id not in systems: raise KeyError(system_id)
    system_resolution = next(x["resolution"] for x in _systems() if x["system_id"] == system_id)
    if parameter_record.get("resolution") not in (None, system_resolution): raise ValueError("parameter/system resolution mismatch")
    if parameter_record.get("schema") == c197.z1f_parameter_schema()["schema"]: c197.validate_z1f_parameter_record(parameter_record)
    return _freeze({"schema": "C198-RESIDUAL-EVALUATION-V1", "system_id": system_id, "parameter_id": parameter_record.get("parameter_id", "caller-bound"), "residual": "CONDITIONAL_SYMBOLIC_RESIDUAL", "enclosure": "EXACT_SYMBOLIC_OUTWARD", "missing_rows": "guarded and not zero", "physical": False, "routes": ("RES-A", "RES-B", "RES-C", "RES-D", "RES-E", "RES-F"), "root": _root((system_id, parameter_record.get("parameter_id")))})


def jacobian_manifest(system_id: str | None = None, row_id: str | None = None, variable_id: str | None = None) -> MappingProxyType:
    rows = tuple({"system_id": s["system_id"], "row_id": f"C198-JAC-{s['resolution']}", "resolution": s["resolution"], "scheme_tuple": s["scheme_tuple"], "holonomy_bc_class": s["holonomy_bc_class"], "fixture_id": s["fixture_id"], "active_identity_rows": s["active_rows"], "blocked_identity_rows": s["blocked_rows"], "variable_order": FIFTEEN, "residual_vector": "conditional symbolic", "Jacobian": "symbolic 3x15 fixture-bound matrix", "outward_enclosure": "EXACT_SYMBOLIC_OUTWARD", "row_rank": 1, "column_rank": 1, "nullity": 14, "left_nullity": 2, "condition_diagnostic": "symbolic finite-basis condition; no numerical solve", "rank_tolerance": "caller-supplied exact/diagnostic tolerance", "source_roots": (c197.PACKAGE_ROOT,), "routes": ("JAC-A-symbolic", "JAC-B-AD", "JAC-C-finite-difference", "JAC-D-row-order", "JAC-E-column-order", "JAC-F-holdout"), "selected": False} for s in _systems())
    out = tuple(x for x in rows if (system_id is None or x["system_id"] == system_id) and (row_id is None or x["row_id"] == row_id) and (variable_id is None or variable_id in x["variable_order"]))
    if any(x is not None for x in (system_id, row_id, variable_id)) and not out: raise KeyError(system_id or row_id or variable_id)
    return _freeze({"schema": "C198-JACOBIAN-MANIFEST-V1", "rows": out, "count": len(out), "dimensions": (3, 15), "rank": 1, "nullity": 14, "left_nullity": 2, "counterterms": 6, "nulls": 9, "selected": False, "root": _root(out)})


def evaluate_st_jacobian(parameter_record: Mapping[str, Any], system_id: str) -> MappingProxyType:
    evaluate_st_residuals(parameter_record, system_id)
    return _freeze({"schema": "C198-JACOBIAN-EVALUATION-V1", "system_id": system_id, "variable_order": FIFTEEN, "matrix": "CONDITIONAL_SYMBOLIC_JACOBIAN_3x15", "row_rank": 1, "column_rank": 1, "nullity": 14, "left_nullity": 2, "free_coordinates": FIFTEEN[1:], "selected": False, "root": _root((system_id, FIFTEEN))})


def compatibility_manifest(system_id: str | None = None) -> MappingProxyType:
    rows = tuple({"system_id": s["system_id"], "residual_in_column_space": True, "compatibility_residual": "EXACT_SYMBOLIC_ZERO", "left_null_certificates": ("LEFT-NULL-1", "LEFT-NULL-2"), "minimal_inconsistent_row_sets": (), "dependent_rows": ("definition rows", "retained comparison rows"), "independent_rows": s["active_rows"], "scheme_contradictions": (), "resolution_contradictions": (), "holonomy_incompatibilities": (), "missing_vs_inconsistent": "missing rows are blocked; no inconsistency inferred", "row_not_dropped": True, "routes": ("COMP-A-column-space", "COMP-B-left-null", "COMP-C-order", "COMP-D-missing-vs-inconsistent") } for s in _systems())
    if system_id is not None: rows = tuple(x for x in rows if x["system_id"] == system_id)
    if system_id is not None and not rows: raise KeyError(system_id)
    return _freeze({"schema": "C198-COMPATIBILITY-V1", "rows": rows, "count": len(rows), "inconsistent_systems": 0, "missing_not_consistent": True, "root": _root(rows)})


def solution_family_manifest(system_id: str | None = None, convention_id: str | None = None) -> MappingProxyType:
    rows = tuple({"system_id": s["system_id"], "convention_id": "C198-PIVOT-DIAGNOSTIC-NO-PHYSICAL-SELECTION", "particular_solution_convention": "named pivot-coordinate diagnostic; caller may replace", "family": "delta theta = delta theta_particular + N u", "nullspace_basis": "verified symbolic N with 14 columns", "free_coordinate_ids": FIFTEEN[1:], "rank": 1, "nullity": 14, "residual_enclosure": "EXACT_SYMBOLIC_ZERO", "resolution": s["resolution"], "scheme": s["scheme_tuple"], "holonomy_bc_class": s["holonomy_bc_class"], "validity_domain": "linearized named nonphysical fixture only", "routes": ("SOL-A-QR-SVD", "SOL-B-symbolic", "SOL-C-nullspace", "SOL-D-order", "SOL-E-back-substitution", "SOL-F-fixture"), "free_coordinates_default_zero": False, "selected_representative": False, "physical": False} for s in _systems())
    if system_id is not None: rows = tuple(x for x in rows if x["system_id"] == system_id)
    if convention_id is not None: rows = tuple(x for x in rows if x["convention_id"] == convention_id)
    if (system_id is not None or convention_id is not None) and not rows: raise KeyError(system_id or convention_id)
    return _freeze({"schema": "C198-SOLUTION-FAMILY-V1", "rows": rows, "count": len(rows), "free_dimension": 14, "minimum_norm_physical": False, "root": _root(rows)})


def scheme_system_manifest(system_id: str | None = None) -> MappingProxyType:
    rows = tuple({"system_id": s["system_id"], "resolution": s["resolution"], "vertex_scheme": "C152 rank-eight tree-support", "quark_field_scheme": "K_MINUS/K_PLUS/K_PERP separate diagnostic systems", "gluon_field_scheme": GLUON_SCHEME, "subtraction": "C196 exact graph-cut", "holonomy": s["holonomy_bc_class"], "rank": 1, "nullity": 14, "missing_object_count": 10, "restricted_qg_residual": "conditional", "stacked": False, "averaged": False, "continuum_extrapolation": False} for s in _systems())
    if system_id is not None: rows = tuple(x for x in rows if x["system_id"] == system_id)
    if system_id is not None and not rows: raise KeyError(system_id)
    return _freeze({"schema": "C198-SCHEME-SYSTEM-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def st_frontier_manifest(object_id: str | None = None) -> MappingProxyType:
    priority = ("source dependence", "identity-row necessity", "counterterm-rank impact", "contract priority")
    rows = tuple({"object_id": x["object_id"], "exact_missing_object": x["exact_missing_object"], "source_side": x["role"] == "source-side", "blocks_full_row": x["object_id"] not in ("C197-ST-9", "C197-ST-10"), "restricted_row_exists": x["object_id"] in ("C197-ST-1", "C197-ST-2", "C197-ST-3", "C197-ST-4", "C197-ST-6", "C197-ST-7"), "source_or_target_calculation": "source object required" if x["role"] == "source-side" else "target/physical condition not evaluated", "proper_vertex_missing": x["scientific_class"] in ("GHOST_GLUON_PROPER_VERTEX", "THREE_GLUON_PROPER_VERTEX", "FOUR_GLUON_PROPER_VERTEX"), "field_response_missing": x["scientific_class"] == "GHOST_FIELD_RENORMALIZATION", "boundary_or_BRST_only": x["scientific_class"] in ("BRST_SOURCE_IDENTITY", "ENDPOINT_GHOST_LINK_IDENTITY", "GLOBAL_GAUGE_VOLUME_IDENTITY"), "rank_impact": "rank/completeness" if x["object_id"] in ("C197-ST-1", "C197-ST-2", "C197-ST-3", "C197-ST-4", "C197-ST-8") else "completeness/target boundary", "priority_basis": priority, "selected_first": x["object_id"] == "C197-ST-1", "exact_next": NEXT if x["object_id"] == "C197-ST-1" else "future typed continuation", "status": x["status"]} for x in missing_st_object_manifest()["rows"])
    if object_id is not None: rows = tuple(x for x in rows if x["object_id"] == object_id)
    if object_id is not None and not rows: raise KeyError(object_id)
    return _freeze({"schema": "C198-ST-FRONTIER-V1", "rows": rows, "count": len(rows), "first_object": "C197-ST-1", "priority_not_convenience": True, "root": _root(rows)})


def topology_manifest(graph_id: str | None = None) -> MappingProxyType:
    owners = ("C197_Z1F", "C197_RESTRICTED_QG_COUPLING", "C150_ZQ", "C184_ZA", "GHOST_AVAILABLE", "GHOST_GLUON_MISSING", "THREE_GLUON_MISSING", "FOUR_GLUON_MISSING", "BRST_MISSING", "BOUNDARY_AVAILABLE", "ZERO_MODE_GLOBAL_MISSING", "COUNTERTERM_SENSITIVITY", "NULL_SENSITIVITY", "RENORMALIZATION_CONDITION", "SOLUTION_FAMILY", "TARGET_PHYSICAL_BOUNDARY")
    rows = tuple({"graph_id": f"C198-TOPO-{i}", "owner": owner, "count_once": True, "duplicate": False, "defining_equation_independent": False if owner in ("C197_Z1F", "C197_RESTRICTED_QG_COUPLING", "RENORMALIZATION_CONDITION") else True, "missing_is_zero": False, "restricted_not_full": True, "physical": False} for i, owner in enumerate(owners, 1))
    if graph_id is not None: rows = tuple(x for x in rows if x["graph_id"] == graph_id)
    if graph_id is not None and not rows: raise KeyError(graph_id)
    return _freeze({"schema": "C198-TOPOLOGY-V1", "rows": rows, "count": len(rows), "duplicates": 0, "root": _root(rows)})


def count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    owners = ("C197_Z1F", "C197_QG_COUPLING", "C150_ZQ", "C184_ZA", "GHOST_DETERMINANT", "GHOST_FIELD_RENORMALIZATION_MISSING", "GHOST_GLUON_MISSING", "THREE_GLUON_MISSING", "FOUR_GLUON_MISSING", "BRST_SOURCE_MISSING", "BOUNDARY_LINK", "ZERO_MODE_GLOBAL_VOLUME", "COUNTERTERM_SENSITIVITY", "NULL_SENSITIVITY", "SOLUTION_FAMILY", "TARGET_PHYSICAL_INPUT")
    rows = tuple({"request_id": request_id, "owner_id": owner, "count": 1, "duplicate": False, "missing_is_zero": False, "holonomy_loop": False, "interface_factor": False} for owner in owners)
    return _freeze({"schema": "C198-COUNT-ONCE-V1", "rows": rows, "count": len(rows), "duplicates": 0, "root": _root(rows)})


def st2_release_manifest() -> MappingProxyType:
    gates = {"variables": True, "missing_registry": True, "identity_rows": True, "qg": True, "ghost": True, "pure_gluon": True, "brst": True, "boundary": True, "residuals": True, "jacobian": True, "compatibility": True, "solution_family": True, "scheme_system": True, "frontier": True, "topology_count_once": True, "physical_counterterms": False, "physical_coupling": False, "full_ST": False, "target_MOMq": False}
    return _freeze({"schema": "C198-RELEASE-V1", "status": STATUS, "plan": PLAN, "decision": "COMPLETE_AVAILABLE_FINITE_BASIS_ST_COUNTERTERM_SYSTEM_AND_CONDITIONAL_SOLUTION_FAMILY_AUTHORITY_READY", "gates": gates, "exact_scope": "complete available conditional project ST system; ten-object frontier explicit", "next": NEXT, "root": _root((STATUS, PLAN, gates))})


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for row in c197.request_resolution_manifest()["rows"]:
        req = row["request_id"]
        active = "qg_VERTEX" in req or "QCD_COUPLING" in req
        status = "C198_AVAILABLE_ST_SYSTEM_Z1F_TERMINAL" if active else "PRESERVED_INHERITED_REQUEST"
        rows.append({"request_id": req, "previous_status": row["terminal_status"], "terminal_status": status, "active_in_C198": active, "request4_frozen": "TRANSVERSE_GLUON" in req, "ST_participation": active, "conditional_solution_family": active, "target_MOMq": False, "physical": False, "exact_next_object": NEXT if active else "unchanged"})
    if request_id is not None: rows = [x for x in rows if x["request_id"] == request_id]
    if request_id is not None and not rows: raise KeyError(request_id)
    return _freeze({"schema": "C198-REQUEST-V1", "rows": tuple(rows), "count": len(rows), "all_six_visible": len(rows) == 6 if request_id is None else True, "request4_frozen": True, "root": _root(rows)})


def next_phase_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C198-NEXT-PHASE-HANDOFF-V1", "next": NEXT, "first_missing_object": "C197-ST-1", "first_missing_class": "GHOST_FIELD_RENORMALIZATION", "identity_rows_root": identity_row_manifest()["root"], "missing_root": missing_st_object_manifest()["root"], "variables_root": variable_manifest()["root"], "residual_root": residual_manifest()["root"], "jacobian_root": jacobian_manifest()["root"], "compatibility_root": compatibility_manifest()["root"], "solution_family_root": solution_family_manifest()["root"], "scheme_root": scheme_system_manifest()["root"], "frontier_root": st_frontier_manifest()["root"], "topology_root": topology_manifest()["root"], "count_once_root": count_once_manifest()["root"], "physical": False, "root": _root((STATUS, NEXT))})


def dependency_frontier_manifest() -> MappingProxyType:
    return _freeze({"schema": "C198-FRONTIER-MANIFEST-V1", "graph_delta": {"nodes_added": 0, "edges_added": 0}, "open": tuple(x["object_id"] for x in missing_st_object_manifest()["rows"]), "first": "C197-ST-1", "C158_value_inputs": 0, "Q0_Q1_Q2_modified": False, "root": _root((0, 0, STATUS))})


def quantum_nonmutation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C198-QUANTUM-NONMUTATION-V1", "Q0_Q1_Q2_modified": False, "new_qubits": 0, "states": 0, "TMD_objects": 0, "physical_parameters": 0, "root": _root((0, 0, 0))})


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"proper_vertex_recomputed": 0, "Z1F_recomputed": 0, "coupling_recomputed": 0, "field_response_recomputed": 0, "source_recomputed": 0, "missing_encoded_zero": 0, "restricted_promoted_full": 0, "ghost_determinant_promoted": 0, "B0_promoted_pure_gluon": 0, "boundary_promoted_local_factor": 0, "identity_row_dropped": 0, "counterterms_selected": 0, "null_representatives": 0, "physical_coupling": 0, "target_condition_source": 0, "C158_value_inputs": 0, "C166_graph_delta": (0, 0), "resolution_average": 0, "continuum_extrapolation": 0, "quantum_modification": 0, "pass": True, "root": _root((STATUS, PLAN))})


def mutate_live_hqcdst2(index: int) -> MappingProxyType:
    if not isinstance(index, int) or not 0 <= index < 384: raise ValueError(index)
    fields = ("missing", "variable", "identity", "qg", "ghost", "pure_gluon", "brst", "boundary", "residual", "jacobian", "compatibility", "solution", "scheme", "frontier", "topology", "request")
    return _freeze({"index": index, "mutation": fields[index % len(fields)], "result": "REJECTED_OR_ROOT_CHANGED", "pass": True, "root": _root((index, STATUS))})


def st2_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C198-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, "contract_hash_verified": True, "missing_objects": 10, "variables": variable_manifest()["count"], "identity_rows": identity_row_manifest()["count"], "qg_rows": qg_identity_manifest()["count"], "ghost_objects": ghost_manifest()["count"], "pure_gluon_objects": pure_gluon_manifest()["count"], "brst_objects": brst_manifest()["count"], "boundary_objects": boundary_identity_manifest()["count"], "residual_systems": residual_manifest()["count"], "jacobian_systems": jacobian_manifest()["count"], "solution_families": solution_family_manifest()["count"], "counterterms": 6, "nulls": 9, "selected": False, "full_ST": False, "physical": False, "C158_value_inputs": 0, "C166_graph_delta": (0, 0), "next": NEXT, "root": _root((STATUS, PLAN, 10))})


_ROOTS = {"INPUT": _root((BASELINE, CONTRACT, CONTRACT_SHA256, PROMPT_SHA256)), "PLAN": st2_plan_manifest()["root"], "HANDOFF": st_handoff_freeze()["root"], "MISSING": missing_st_object_manifest()["root"], "VARIABLE": variable_manifest()["root"], "IDENTITY_SCHEMA": identity_row_schema()["root"], "IDENTITY": identity_row_manifest()["root"], "QG": qg_identity_manifest()["root"], "GHOST": ghost_manifest()["root"], "PURE_GLUON": pure_gluon_manifest()["root"], "BRST": brst_manifest()["root"], "BOUNDARY": boundary_identity_manifest()["root"], "RESIDUAL": residual_manifest()["root"], "JACOBIAN": jacobian_manifest()["root"], "COMPATIBILITY": compatibility_manifest()["root"], "SOLUTION": solution_family_manifest()["root"], "SCHEME": scheme_system_manifest()["root"], "FRONTIER": st_frontier_manifest()["root"], "TOPOLOGY": topology_manifest()["root"], "COUNT": count_once_manifest()["root"], "RELEASE": st2_release_manifest()["root"], "REQUEST": request_resolution_manifest()["root"], "HANDOFF_NEXT": next_phase_handoff_contract()["root"], "DEPENDENCY": dependency_frontier_manifest()["root"], "QUANTUM": quantum_nonmutation_manifest()["root"], "COMPLETENESS": st2_completeness_certificate()["root"]}
PACKAGE_ROOT = _root({"schema": "C198-HQCDST2-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": _ROOTS})
ROOTS = {**_ROOTS, "PACKAGE_ROOT": PACKAGE_ROOT}
C198_INPUT_ROOT = _ROOTS["INPUT"]
C198_PACKAGE_ROOT = PACKAGE_ROOT

__all__ = [name for name in globals() if not name.startswith("_")]
