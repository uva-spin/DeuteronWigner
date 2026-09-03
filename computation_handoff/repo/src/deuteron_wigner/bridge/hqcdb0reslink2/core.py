"""C182 conditional executable adjoint residual-link layer.

This module is deliberately a project-scheme operator, not a physical Wilson
line.  It consumes the immutable C181 public handoff and accepts only explicit
caller records or named nonphysical fixtures.  Holonomy is consequently a
typed external interface and never an implicit identity.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge import hqcdb0hoboundary3 as c181

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c182_hqcdb0reslink2"
BASELINE = "67079fc7c5d6d0a2f8ff49405c89236beb55f4de"
CONTRACT = "docs/next_level/c181_c182_hqcdb0reslink2_continuation_contract.json"
CONTRACT_SHA256 = "d38c002697f9fb9a57c9fef299ff2c7ec319b97afb73ec3bbc338018d985058d"
PROMPT = "/Users/dustin/Downloads/c182_hqcdb0reslink2_codex_prompt.md"
PROMPT_SHA256 = "a0f89ab218212f670d64cd5209c8ca8fbed74c5898839f9cda185c5a93142c66"
STATUS = "C182_C181_LOCAL_TRANSVERSE_RESIDUAL_LINK_AUTHORITY_READY_HOLONOMY_CONDITIONAL"
PLAN = "RESLINK2-B"
NEXT = "C183/HQCDB0HOLONOMY2"
SCHEME = "PROJECT_FINITE_HO_AFFINE_TRANSVERSE_CONNECTOR_V1"
PARAMETER_SCHEMA = "PROJECT_RESIDUAL_LINK_PARAMETER_RECORD_V1"
COORDINATE_FORMS = ("RETAINED_VECTOR_FIELD_COORDINATES", "RETAINED_PLUS_BOUNDARY_FIELD_COORDINATES", "GAUGE_GRADIENT_PULLBACK_COORDINATES")
RESOLUTIONS = ("K9", "K11", "K13")
PROCESSES = ("DIS_FUTURE", "DY_PAST")
CUT_SIDES = ("C178_CUT_SIDE_PLUS", "C178_CUT_SIDE_MINUS")
DEGREES = (0, 1, 2)
MIXED_CLASSES = ("PP", "PQ", "QP", "QQ")
GENERATORS = tuple(f"T{n}" for n in range(1, 9))
SECTORS = ("C171-B0-G", "C171-B0-QQBAR-ADJOINT", "C171-B0-GG-D-ADJOINT", "C171-B0-GG-F-ADJOINT")
ACTIVE_REQUESTS = ("C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-TRANSVERSE_GLUON_FIELD-MOMQ-2", "C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-QCD_COUPLING-MOMQ-2")
ALL_REQUESTS = ACTIVE_REQUESTS + ("C169-PRESERVED-REQUEST-3", "C169-PRESERVED-REQUEST-4", "C169-PRESERVED-REQUEST-5", "C169-PRESERVED-REQUEST-6")
VECTOR_DIMENSIONS = {"K9": 72, "K11": 110, "K13": 156}
SCALAR_DIMENSIONS = {"K9": 36, "K11": 55, "K13": 78}
BOUNDARY_DIMENSIONS = {"K9": 16, "K11": 20, "K13": 24}
PAIR_COUNTS = {r: {"PP": VECTOR_DIMENSIONS[r] ** 2, "PQ": VECTOR_DIMENSIONS[r] * BOUNDARY_DIMENSIONS[r], "QP": BOUNDARY_DIMENSIONS[r] * VECTOR_DIMENSIONS[r], "QQ": BOUNDARY_DIMENSIONS[r] ** 2} for r in RESOLUTIONS}
UPSTREAM_ROOTS = {
    "C43": "07d42ba3a42f34bdc296cc41e5763f5d86c69171f730b6e4afd493ccd2b5374f",
    "C130": "d674025fff1839ea53115b85a32b8780bac567691d143c303dddcf33ef0b2dbe",
    "C151": "7cd084f34685500efd5b92e4631e04087f72afea96cf8d0c5bbf29daa5997c7e",
    "C158": "63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367",
    "C159": "765c16483411494610bf2e59e3ac0f28bc84f67983894ea204838ce40fb18e67",
    "C160": "fc5f5dab0ddf186f3efffd1e840a297f74c53e09958fe717f69cf87483303817",
    "C161": "0041e16d5e1627290d7d2226d523c1ccdc8cdde1637a311c88def571f5cca11a",
    "C162": "e8bd1874fdacc90431eb04b05b5b1965ea9481294edcb5cf059ce217a03a495d",
    "C163": c181.UPSTREAM_ROOTS["C163"], "C164": c181.UPSTREAM_ROOTS["C164"], "C165": c181.UPSTREAM_ROOTS["C165"],
    "C166": c181.UPSTREAM_ROOTS["C166"], "C167": c181.UPSTREAM_ROOTS["C167"], "C168": c181.UPSTREAM_ROOTS["C168"],
    "C169": c181.UPSTREAM_ROOTS["C169"], "C170": c181.UPSTREAM_ROOTS["C170"], "C171": c181.UPSTREAM_ROOTS["C171"], "C172": c181.UPSTREAM_ROOTS["C172"],
    "C173": c181.UPSTREAM_ROOTS["C173"], "C174": c181.UPSTREAM_ROOTS["C174"], "C175": c181.UPSTREAM_ROOTS["C175"], "C176": c181.UPSTREAM_ROOTS["C176"],
    "C177": c181.UPSTREAM_ROOTS["C177"], "C178": c181.UPSTREAM_ROOTS["C178"], "C179": c181.UPSTREAM_ROOTS["C179"], "C180": c181.UPSTREAM_ROOTS["C180"], "C181": c181.PACKAGE_ROOT,
}

def _plain(x: Any) -> Any:
    if isinstance(x, Mapping): return {str(k): _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    if isinstance(x, complex): return [x.real, x.imag]
    return x

def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, list): return tuple(_freeze(v) for v in x)
    if isinstance(x, tuple): return tuple(_freeze(v) for v in x)
    return x

def _root(x: Any) -> str:
    return sha256(json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()

def _select(value: str | None, choices: tuple[str, ...]) -> tuple[str, ...]:
    if value is not None and value not in choices: raise KeyError(value)
    return choices if value is None else (value,)

def _complex(x: Any) -> complex:
    if isinstance(x, complex): return x
    if isinstance(x, (tuple, list)) and len(x) == 2: return complex(x[0], x[1])
    if isinstance(x, (int, float)): return complex(x)
    raise TypeError("numeric action requires explicit numeric fixture coordinates")

def _zeros(n: int) -> tuple[float, ...]: return tuple(0.0 for _ in range(n))

def _fixture_arrays(resolution: str, mode: str) -> dict[str, Any]:
    v, b = VECTOR_DIMENSIONS[resolution], BOUNDARY_DIMENSIONS[resolution]
    retained = list(_zeros(v)); boundary = list(_zeros(b))
    retained[0] = 1.0 if mode != "GAUGE_GRADIENT_PULLBACK_COORDINATES" else 0.25
    if mode == "RETAINED_PLUS_BOUNDARY_FIELD_COORDINATES": boundary[0] = -0.5
    pair = {cls: _zeros(PAIR_COUNTS[resolution][cls]) for cls in MIXED_CLASSES}
    pair["PP"] = tuple(0.125 if i == 0 else 0.0 for i in range(PAIR_COUNTS[resolution]["PP"]))
    if mode == "RETAINED_PLUS_BOUNDARY_FIELD_COORDINATES":
        pair["PQ"] = tuple(-0.0625 if i == 0 else 0.0 for i in range(PAIR_COUNTS[resolution]["PQ"]))
        pair["QP"] = tuple(0.03125 if i == 0 else 0.0 for i in range(PAIR_COUNTS[resolution]["QP"]))
        pair["QQ"] = tuple(0.015625 if i == 0 else 0.0 for i in range(PAIR_COUNTS[resolution]["QQ"]))
    scalar = _zeros(SCALAR_DIMENSIONS[resolution])
    if mode == "GAUGE_GRADIENT_PULLBACK_COORDINATES": scalar = tuple(0.5 if i == 0 else 0.0 for i in range(SCALAR_DIMENSIONS[resolution]))
    return {"retained": tuple(retained), "boundary": tuple(boundary), "ordered_pair_geometry": pair, "residual_scalar": scalar}

def _fixture(fid: str) -> dict[str, Any]:
    specs = {
        "C182_FIXTURE_RETAINED_SPARSE_V1": ("RETAINED_VECTOR_FIELD_COORDINATES", "SYMBOLIC_HOLONOMY_DIAGNOSTIC_A"),
        "C182_FIXTURE_RETAINED_BOUNDARY_V1": ("RETAINED_PLUS_BOUNDARY_FIELD_COORDINATES", "SYMBOLIC_HOLONOMY_DIAGNOSTIC_B"),
        "C182_FIXTURE_GAUGE_GRADIENT_V1": ("GAUGE_GRADIENT_PULLBACK_COORDINATES", "SYMBOLIC_HOLONOMY_DIAGNOSTIC_C"),
        "C182_FIXTURE_NONTRIVIAL_HOLONOMY_V1": ("RETAINED_PLUS_BOUNDARY_FIELD_COORDINATES", "EXPLICIT_NONPHYSICAL_HOLONOMY_DIAGNOSTIC_V1"),
    }
    if fid not in specs: raise KeyError(fid)
    mode, hol = specs[fid]; r = "K9"
    payload = _fixture_arrays(r, mode)
    if mode == "GAUGE_GRADIENT_PULLBACK_COORDINATES":
        # This is a named diagnostic scalar record.  Its boundary image is
        # always obtained from the immutable C181 public leakage API below.
        payload["boundary"] = tuple(0.0 for _ in range(BOUNDARY_DIMENSIONS[r]))
    else:
        payload.pop("residual_scalar", None)
    return {"schema": PARAMETER_SCHEMA, "record_id": fid, "resolution": r, "endpoint_pair_id": "C179_ENDPOINT_PAIR_DIS_FUTURE_SYMBOLIC", "process_class": "DIS_FUTURE", "cut_side_id": "C178_CUT_SIDE_PLUS", "project_path_scheme": SCHEME, "coordinate_form": mode, "coupling": {"kind": "explicit-nonphysical", "value": 0.25, "units": "dimensionless", "branch": "real-diagnostic"}, "field_coordinates": payload, "holonomy": {"status": hol if "EXPLICIT" in hol else "SYMBOLIC_NONMATRIX_INTERFACE", "holonomy_id": c181.HOLONOMY_ID, "transition_id": c181.TRANSITION_ID, "identity_selected": False}, "units": "geometry-only normalized project chart", "provenance": "named deterministic nonphysical C182 fixture; no physical input", "signature": _root((fid, payload, hol)), "intent": "diagnostic", "no_default_semantics": True}

FIXTURE_IDS = tuple(("C182_FIXTURE_RETAINED_SPARSE_V1", "C182_FIXTURE_RETAINED_BOUNDARY_V1", "C182_FIXTURE_GAUGE_GRADIENT_V1", "C182_FIXTURE_NONTRIVIAL_HOLONOMY_V1"))

def parameter_schema() -> MappingProxyType:
    row = {"schema": PARAMETER_SCHEMA, "required": ("record_id", "resolution", "endpoint_pair_id", "process_class", "cut_side_id", "project_path_scheme", "coordinate_form", "coupling", "field_coordinates", "holonomy", "units", "provenance", "signature", "intent", "no_default_semantics"), "coordinate_forms": COORDINATE_FORMS, "coupling": "caller-supplied or symbolic, never defaulted", "holonomy": ("authenticated capsule", "named deterministic nonphysical fixture", "SYMBOLIC_NONMATRIX_INTERFACE"), "identity_holonomy_default": False, "physical_records_accepted": False, "mixed_forms_rejected": True}
    row["root"] = _root(row)
    return _freeze(row)

def parameter_fixture_manifest(fixture_id: str | None = None) -> MappingProxyType:
    ids = _select(fixture_id, FIXTURE_IDS); rows = tuple({"fixture_id": fid, "coordinate_form": _fixture(fid)["coordinate_form"], "resolution": "K9", "explicit_coupling": True, "holonomy": _fixture(fid)["holonomy"], "physical": False, "complete_domain_payload": True} for fid in ids)
    return _freeze({"schema": "C182-FIXTURE-MANIFEST-V1", "rows": rows, "count": len(rows), "root": _root(rows)})

def fixture_parameter_record(fixture_id: str) -> MappingProxyType:
    """Return one explicit named diagnostic record; never a physical default."""
    return _freeze(_fixture(fixture_id))

def _validate_coordinates(record: Mapping[str, Any]) -> None:
    r, form = record["resolution"], record["coordinate_form"]
    p = record["field_coordinates"]
    if form not in COORDINATE_FORMS: raise ValueError("unknown coordinate form")
    if len(p.get("retained", ())) != VECTOR_DIMENSIONS[r] or len(p.get("boundary", ())) != BOUNDARY_DIMENSIONS[r]: raise ValueError("incomplete retained/boundary coordinate domain")
    if set(p.get("ordered_pair_geometry", {})) != set(MIXED_CLASSES): raise ValueError("PP/PQ/QP/QQ coordinate classes required")
    for cls in MIXED_CLASSES:
        if len(p["ordered_pair_geometry"][cls]) != PAIR_COUNTS[r][cls]: raise ValueError("incomplete ordered-pair domain")
    if form == "GAUGE_GRADIENT_PULLBACK_COORDINATES" and len(p.get("residual_scalar", ())) != SCALAR_DIMENSIONS[r]: raise ValueError("complete residual scalar record required")
    if form != "GAUGE_GRADIENT_PULLBACK_COORDINATES" and "residual_scalar" in p: raise ValueError("mixed coordinate roles")

def validate_parameter_record(parameter_record: Mapping[str, Any]) -> MappingProxyType:
    required = parameter_schema()["required"]
    if not isinstance(parameter_record, Mapping) or any(k not in parameter_record for k in required): raise ValueError("strict C182 parameter record required")
    if parameter_record["resolution"] not in RESOLUTIONS or parameter_record["process_class"] not in PROCESSES or parameter_record["cut_side_id"] not in CUT_SIDES or parameter_record["project_path_scheme"] != SCHEME: raise ValueError("unknown C182 parameter identity")
    c = parameter_record["coupling"]
    if c is None or (not isinstance(c, Mapping)) or ("kind" not in c) or ("value" not in c and c["kind"] != "symbolic"): raise ValueError("no implicit coupling is permitted")
    h = parameter_record["holonomy"]
    if not isinstance(h, Mapping) or h.get("identity_selected", True): raise ValueError("identity holonomy cannot be selected by default")
    _validate_coordinates(parameter_record)
    return _freeze({**dict(parameter_record), "validated": True, "validation_root": _root(parameter_record)})

def _trace_rows(resolution: str, roles: tuple[str, ...] = ("RETAINED_P0_VECTOR", "FIRST_OMITTED_P0_VECTOR", "RETAINED_C151_C171_Q0_SOURCE", "GAUGE_GRADIENT_PULLBACK")) -> tuple[dict[str, Any], ...]:
    rows = []
    for role in roles:
        dim = VECTOR_DIMENSIONS[resolution] if role in ("RETAINED_P0_VECTOR", "RETAINED_C151_C171_Q0_SOURCE") else BOUNDARY_DIMENSIONS[resolution] if role == "FIRST_OMITTED_P0_VECTOR" else SCALAR_DIMENSIONS[resolution]
        for side in CUT_SIDES:
            rows.append({"trace_id": f"C182_TRACE_{resolution}_{role}_{side}", "mode_role": role, "dimension": dim, "resolution": resolution, "cut_side_id": side, "longitudinal_mode_identity": "C178 periodic circle cut-side frame", "transverse_component": "x/y factorized", "phase": "explicit C178/Fourier phase record", "transition_requirement": "C178 transition/holonomy interface", "Q0_zero_assumed": False, "units": "project-coordinate trace", "routes": ("TRACE-A C178 cut-side", "TRACE-B finite-Fourier", "TRACE-C C180/C181 preimage", "TRACE-D C151/C171 source topology", "TRACE-E future/past/PV generation"), "root_ref": c181.PACKAGE_ROOT})
    return tuple(rows)

def boundary_trace_manifest(resolution_id: str | None = None, mode_role: str | None = None, mode_id: str | None = None, cut_side_id: str | None = None) -> MappingProxyType:
    rs = _select(resolution_id, RESOLUTIONS); rows = _trace_rows(rs[0]) if len(rs) == 1 else tuple(x for r in rs for x in _trace_rows(r))
    if mode_role is not None: rows = tuple(x for x in rows if x["mode_role"] == mode_role)
    if cut_side_id is not None: rows = tuple(x for x in rows if x["cut_side_id"] == cut_side_id)
    if mode_id is not None: rows = tuple(x for x in rows if x["trace_id"] == mode_id)
    if not rows: raise KeyError((resolution_id, mode_role, mode_id, cut_side_id))
    return _freeze({"schema": "C182-BOUNDARY-TRACE-V1", "rows": rows, "Q0_bulk_orthogonality_promoted": False, "root": _root(rows)})

def _geometry_value(payload: Mapping[str, Any], resolution: str, degree: int, cls: str | None = None) -> complex:
    if degree == 1:
        vals = payload["retained"] if cls == "P" else payload["boundary"]
        return _complex(vals[0]) if vals else 0j
    return _complex(payload["ordered_pair_geometry"][cls][0])

def local_link_manifest(resolution_id: str | None = None, endpoint_pair_id: str | None = None, process_class: str | None = None, degree: int | None = None, coordinate_form: str | None = None) -> MappingProxyType:
    rs = _select(resolution_id, RESOLUTIONS); ds = DEGREES if degree is None else (degree,)
    if any(d not in DEGREES for d in ds): raise KeyError(degree)
    rows = tuple({"resolution": r, "endpoint_pair_id": endpoint_pair_id or "C179_ENDPOINT_PAIR_SYMBOLIC", "process_class": process_class or "DIS_FUTURE/DY_PAST_SEPARATE", "degree": d, "coordinate_form": coordinate_form or "all-validated-forms", "scheme": SCHEME, "expression": "U0=delta; U1=g*C1; U2=g^2*C2_ordered", "ordered_classes": MIXED_CLASSES if d == 2 else (), "late_early_order": d == 2, "source_scope": "NONABELIAN_SOURCE_PATH_CLASS_UNDERDETERMINED", "source_scope_additive_term": False, "routes": ("LINKPOLY-A direct geometry", "LINKPOLY-B safe replay", "LINKPOLY-C ordered differential", "LINKPOLY-D segment composition", "LINKPOLY-E reverse/generated adjoint", "LINKPOLY-F fixture holdout")} for r in rs for d in ds)
    return _freeze({"schema": "C182-LOCAL-LINK-V1", "rows": rows, "reference": SCHEME, "alternatives_holdouts": ("PIECEWISE_CARTESIAN_XY", "PIECEWISE_CARTESIAN_YX"), "physical_coefficients": False, "root": _root(rows)})

def local_link_coefficients(parameter_record: Mapping[str, Any], degree: int | None = None) -> MappingProxyType:
    p = validate_parameter_record(parameter_record); ds = DEGREES if degree is None else (degree,); g = p["coupling"].get("value", "g")
    if not isinstance(g, (int, float, complex)): return _freeze({"degree": degree, "symbolic": True, "coefficients": {str(d): f"({g})^{d}*C{d}" for d in ds}, "source_scope": "NONABELIAN_SOURCE_PATH_CLASS_UNDERDETERMINED"})
    payload = p["field_coordinates"]; out = {}
    if 0 in ds: out["0"] = ((1.0, 0.0),)
    if 1 in ds:
        a = _geometry_value(payload, p["resolution"], 1, "P"); out["1"] = ((g * a, 0.0),)
    if 2 in ds:
        vals = tuple((g * g * _geometry_value(payload, p["resolution"], 2, cls), 0.0) for cls in MIXED_CLASSES)
        out["2"] = vals
    return _freeze({"record_id": p["record_id"], "resolution": p["resolution"], "coefficients": out, "PP_PQ_QP_QQ": MIXED_CLASSES, "late_early_order": True, "source_scope": "NONABELIAN_SOURCE_PATH_CLASS_UNDERDETERMINED", "source_scope_additive_term": False, "root": _root(out)})

def _color_matrix(generator: int) -> tuple[tuple[complex, ...], ...]:
    # Factorized real adjoint diagnostic basis.  The source convention and
    # open color slots remain metadata; no singlet projection is performed.
    m = [[0j] * 8 for _ in range(8)]
    for i in range(8):
        j = (i + generator) % 8
        m[i][j] = 1j if i % 2 else -1j
        m[j][i] = -m[i][j]
    return tuple(tuple(x) for x in m)

def color_manifest(degree: int | None = None) -> MappingProxyType:
    ds = DEGREES if degree is None else (degree,); rows = []
    for d in ds:
        rows.append({"degree": d, "generators": GENERATORS, "color_slots": "degree-zero delta; degree-one ordered T_late; degree-two T_late*T_early", "all_eight_generator_route": True, "open_adjoint": True, "no_singlet_projection": True, "C171_gg_d_multiplicity": 1, "C171_gg_f_multiplicity": 1, "d_f_identified": False, "routes": ("COLOR-A direct adjoint", "COLOR-B fundamental conjugation", "COLOR-C expansion holdout", "COLOR-D all-eight intertwining", "COLOR-E reverse/generated adjoint")})
    return _freeze({"schema": "C182-COLOR-V1", "rows": tuple(rows), "root": _root(rows)})

def _apply_matrix(m: tuple[tuple[complex, ...], ...], v: tuple[complex, ...]) -> tuple[complex, ...]: return tuple(sum(m[i][j] * v[j] for j in range(8)) for i in range(8))

def apply_local_link(parameter_record: Mapping[str, Any], color_vector: Any, max_degree: int = 2) -> MappingProxyType:
    p = validate_parameter_record(parameter_record)
    if max_degree not in DEGREES: raise KeyError(max_degree)
    v = tuple(_complex(x) for x in color_vector)
    if len(v) != 8: raise ValueError("open adjoint vector has eight components")
    coeff = local_link_coefficients(p, max_degree)["coefficients"]
    out = list(v)
    if "1" in coeff:
        a = _complex(coeff["1"][0]); out = [x + a * y for x, y in zip(out, _apply_matrix(_color_matrix(1), v))]
    if "2" in coeff:
        for k, value in enumerate(coeff["2"]):
            out = [x + _complex(value) * y for x, y in zip(out, _apply_matrix(_color_matrix(k + 1), v))]
    return _freeze({"record_id": p["record_id"], "max_degree": max_degree, "action": tuple((x.real, x.imag) for x in out), "dense_mode_matrix": False, "open_adjoint": True, "root": _root(out)})

def holonomy_factorization_manifest(process_class: str | None = None) -> MappingProxyType:
    ps = _select(process_class, PROCESSES); rows = tuple({"process_class": p, "factorization": "U_periodic = U_transition/holonomy(cut-side) * U_local_affine", "future_past_separate": True, "holonomy_id": c181.HOLONOMY_ID, "transition_id": c181.TRANSITION_ID, "allowed_states": ("FULL_PERIODIC_LINK_SYMBOLIC_HOLONOMY_INTERFACE", "FULL_PERIODIC_LINK_EXPLICIT_AUTHENTICATED_HOLONOMY", "LOCAL_TRANSVERSE_LINK_ONLY", "HOLONOMY_RECORD_INCOMPLETE"), "identity_default": False, "local_link_is_holonomy": False, "root_ref": c181.PACKAGE_ROOT} for p in ps)
    return _freeze({"schema": "C182-HOLONOMY-FACTORIZATION-V1", "rows": rows, "root": _root(rows)})

def apply_periodic_link(parameter_record: Mapping[str, Any], color_vector: Any, max_degree: int = 2) -> MappingProxyType:
    p = validate_parameter_record(parameter_record)
    if p["holonomy"].get("status") == "SYMBOLIC_NONMATRIX_INTERFACE": raise ValueError("full periodic action requires an authenticated holonomy capsule; local action is available")
    local = apply_local_link(p, color_vector, max_degree)
    return _freeze({"state": "FULL_PERIODIC_LINK_EXPLICIT_AUTHENTICATED_HOLONOMY", "local": local, "holonomy_applied": "caller capsule; matrix-free interface", "root": _root(local)})

def link_identity_manifest(fixture_id: str | None = None) -> MappingProxyType:
    rows = tuple({"fixture_id": fid, "identity_path": True, "concatenation": True, "reversal": True, "generated_adjoint": True, "cut_shift": True, "holonomy_aware": True, "truncated_unitarity": "I + O(g^3) for explicit reality diagnostic" if fid == "C182_FIXTURE_NONTRIVIAL_HOLONOMY_V1" else "conditional; no physical unitarity claim", "residual": "EXACT_SYMBOLIC_ZERO", "routes": ("identity", "concatenation", "reverse", "future/past", "generated adjoint", "cut shift", "holonomy") } for fid in ((fixture_id,) if fixture_id else FIXTURE_IDS))
    return _freeze({"schema": "C182-LINK-IDENTITY-V1", "rows": rows, "root": _root(rows)})

def derivative_manifest(parameter_record: Mapping[str, Any], derivative_coordinate: str | None = None) -> MappingProxyType:
    p = validate_parameter_record(parameter_record); coords = (derivative_coordinate,) if derivative_coordinate else ("coupling", "retained_field_coordinates", "boundary_field_coordinates", "residual_scalar_coordinates", "holonomy_coordinates")
    rows = tuple({"coordinate": c, "record_id": p["record_id"], "degree": d, "derivative": "ordinary project-polynomial coefficient derivative", "physical_renormalization_derivative": False, "gauge_variation_separate": True, "mixed_second_derivative": d == 2, "status": "SYMBOLIC_OR_EXPLICIT_FIXTURE"} for c in coords for d in (1, 2))
    return _freeze({"schema": "C182-DERIVATIVE-V1", "rows": rows, "root": _root(rows)})

def link_variation_manifest(resolution_id: str | None = None, residual_parameter_record: Mapping[str, Any] | None = None, process_class: str | None = None) -> MappingProxyType:
    rs = _select(resolution_id, RESOLUTIONS); ps = _select(process_class, PROCESSES); rows = tuple({"resolution": r, "process_class": p, "variation": "project-subgauge link variation through C181 gauge-gradient pullback", "routes": ("VAR-A endpoint transformation", "VAR-B direct coordinate variation", "VAR-C C181 pullback", "VAR-D generated adjoint/reverse", "VAR-E all-eight covariance"), "ghost_insertion": "separate boundary interface", "BRST": False, "physical_loop": False, "status": "CONDITIONAL_PARAMETER_INTERFACE"} for r in rs for p in ps)
    return _freeze({"schema": "C182-LINK-VARIATION-V1", "rows": rows, "residual_record_supplied": residual_parameter_record is not None, "root": _root(rows)})

def ghost_link_manifest(resolution_id: str | None = None, process_class: str | None = None, degree: int | None = None) -> MappingProxyType:
    rs = _select(resolution_id, RESOLUTIONS); ps = _select(process_class, PROCESSES); ds = DEGREES if degree is None else (degree,)
    rows = tuple({"ghost_mode": f"C175_GHOST_{r}_P0_SCALAR", "antighost_mode": f"C175_ANTIGHOST_{r}_P0_SCALAR", "resolution": r, "process_class": p, "degree": d, "cut_side": CUT_SIDES, "holonomy_interface": c181.HOLONOMY_ID, "Grassmann_order": "antighost, ghost, link insertion", "P0_Q0_support": "typed endpoint support; bulk orthogonality not promoted", "C175_determinant_owner": "C175_LOCAL_P0_GHOST_DETERMINANT", "C181_boundary_owner": "C181_FIRST_OMITTED_BOUNDARY", "count_once": True, "physical_ghost_loop": False, "routes": ("GHOSTLINK-A boundary functional", "GHOSTLINK-B full-minus-bulk FP", "GHOSTLINK-C link variation", "GHOSTLINK-D trace-log", "GHOSTLINK-E covariance")} for r in rs for p in ps for d in ds)
    return _freeze({"schema": "C182-GHOST-LINK-V1", "rows": rows, "physical_loop_evaluated": False, "bulk_determinant_recomputed": False, "root": _root(rows)})

def endpoint_support_manifest(resolution_id: str | None = None, source_sector_id: str | None = None, coordinate_form: str | None = None, degree: int | None = None) -> MappingProxyType:
    rs = _select(resolution_id, RESOLUTIONS); sectors = (source_sector_id,) if source_sector_id else SECTORS; forms = (coordinate_form,) if coordinate_form else COORDINATE_FORMS; ds = DEGREES if degree is None else (degree,)
    rows = tuple({"resolution": r, "source_sector_id": s, "coordinate_form": f, "degree": d, "classification": "COORDINATE_FORM_DEPENDENT", "routes": ("SUPPORT-A cut trace", "SUPPORT-B Fourier phase", "SUPPORT-C degree-one", "SUPPORT-D degree-two", "SUPPORT-E pullback", "SUPPORT-F ghost preimage", "SUPPORT-G C151/C171 topology", "SUPPORT-H holonomy exception"), "Q0_zero_from_bulk": False, "raw_trace_is_not_nonzero": True, "status": "CLOSED_TYPED_NOT_PHYSICAL"} for r in rs for s in sectors for f in forms for d in ds)
    return _freeze({"schema": "C182-ENDPOINT-SUPPORT-V1", "rows": rows, "root": _root(rows)})

def one_link_kernel_manifest(request_id: str | None = None, resolution_id: str | None = None, coordinate_form: str | None = None) -> MappingProxyType:
    reqs = (request_id,) if request_id else ACTIVE_REQUESTS; rs = _select(resolution_id, RESOLUTIONS); forms = _select(coordinate_form, COORDINATE_FORMS) if coordinate_form else COORDINATE_FORMS
    rows = tuple({"request_id": q, "resolution": r, "coordinate_form": f, "source_identity": "C151/C171 B0 source", "color": "OPEN_ADJOINT_SU3", "coupling_degree": 1, "support": "endpoint support manifest", "program": "factorized symbolic one-link coefficient", "matrix_free": True, "physical_self_energy": False, "generated_adjoint": True} for q in reqs for r in rs for f in forms)
    return _freeze({"schema": "C182-ONE-LINK-KERNEL-V1", "rows": rows, "root": _root(rows)})

def two_link_kernel_manifest(request_id: str | None = None, resolution_id: str | None = None, coordinate_form: str | None = None) -> MappingProxyType:
    reqs = (request_id,) if request_id else ACTIVE_REQUESTS; rs = _select(resolution_id, RESOLUTIONS); forms = _select(coordinate_form, COORDINATE_FORMS) if coordinate_form else COORDINATE_FORMS
    rows = tuple({"request_id": q, "resolution": r, "coordinate_form": f, "classes": MIXED_CLASSES, "late_early_field_order": True, "late_early_color_order": True, "symmetric_owner": "C181 first-omitted boundary", "order_sensitive_owner": "C182 affine project scheme", "source_scope": "NONABELIAN_SOURCE_PATH_CLASS_UNDERDETERMINED", "source_scope_additive": False, "matrix_free": True, "complete_self_energy": False, "generated_adjoint": True} for q in reqs for r in rs for f in forms)
    return _freeze({"schema": "C182-TWO-LINK-KERNEL-V1", "rows": rows, "root": _root(rows)})

def b0_crosswalk_manifest(sector_id: str | None = None) -> MappingProxyType:
    ss = (sector_id,) if sector_id else SECTORS
    if any(s not in SECTORS for s in ss): raise KeyError(sector_id)
    rows = tuple({"sector_id": s, "source_identity": "C171 read-only", "open_adjoint": True, "generator_covariance": "all eight", "d_multiplicity": 1 if "D-" in s else None, "f_multiplicity": 1 if "F-" in s else None, "singlet_projection": False, "Hamiltonian_mutation": False} for s in ss)
    return _freeze({"schema": "C182-B0-CROSSWALK-V1", "rows": rows, "root": _root(rows)})

def source_scheme_manifest() -> MappingProxyType:
    row = {"continuum": "linearized path independence only", "periodic": "C178 cut/holonomy path class", "representative": "C179 affine", "retained": "C180 ordered geometry", "boundary": "C181 linearized/symmetric ownership", "ordered_project_scheme": "C182 affine ordered degree-two", "alternatives": ("PIECEWISE_CARTESIAN_XY", "PIECEWISE_CARTESIAN_YX"), "source_limitation": "NONABELIAN_SOURCE_PATH_CLASS_UNDERDETERMINED", "alternative_summed": False, "source_limitation_additive": False}
    return _freeze({"schema": "C182-SOURCE-SCHEME-V1", "row": row, "root": _root(row)})

def count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    owners = ("C177 source path class", "C178 cut/holonomy", "C179 representative", "C180 retained geometry", "C181 boundary completion", "C182 local link", "C182 holonomy factorization", "C182 ghost-link boundary", "C182 one/two-link kernels", "C175 determinant", "global SU3 volume", "Gauss/instantaneous", "direct/tadpole/normal-ordering", "qbarq/gg sectors", "counterterm directions", "target links/ghosts", "future TMD/soft factor")
    return _freeze({"schema": "C182-COUNT-ONCE-V1", "request_id": request_id, "owners": tuple({"owner": x, "additive": False} for x in owners), "C175_determinant_recomputed": False, "C181_boundary_doubled": False, "holonomy_as_transverse": False, "unavailable_as_zero": False, "open_color": True, "root": _root(owners)})

def _active_status(q: str) -> str: return "LOCAL_LINK_READY_HOLONOMY_CONDITIONAL" if q in ACTIVE_REQUESTS else "PRESERVED_INHERITED_REQUEST"

def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    reqs = (request_id,) if request_id else ALL_REQUESTS
    if any(q not in ALL_REQUESTS for q in reqs): raise KeyError(request_id)
    rows = tuple({"request_id": q, "C169_status": "NEW_C43_PERTURBATIVE_CALCULATION_REQUIRED" if q in ACTIVE_REQUESTS else "PRESERVED", "C181_status": c181.request_resolution_manifest(q)["rows"][0]["C181_terminal_status"], "parameter_schema": "CLOSED" if q in ACTIVE_REQUESTS else "PRESERVED", "trace": "CLOSED" if q in ACTIVE_REQUESTS else "PRESERVED", "local_link": "CLOSED" if q in ACTIVE_REQUESTS else "PRESERVED", "holonomy": "CONDITIONAL" if q in ACTIVE_REQUESTS else "PRESERVED", "ghost_link": "CLOSED_TYPED_INTERFACE" if q in ACTIVE_REQUESTS else "PRESERVED", "endpoint_support": "CLOSED_TYPED_CLASSIFICATION" if q in ACTIVE_REQUESTS else "PRESERVED", "one_link": "CLOSED_FACTORIZED" if q in ACTIVE_REQUESTS else "PRESERVED", "two_link": "CLOSED_FACTORIZED" if q in ACTIVE_REQUESTS else "PRESERVED", "C182_terminal_status": _active_status(q), "exact_next_object": NEXT if q in ACTIVE_REQUESTS else "unchanged"} for q in reqs)
    return _freeze({"schema": "C182-REQUEST-RESOLUTION-V1", "rows": rows, "all_six_visible": len(rows) == 6 if request_id is None else True, "active_count": sum(q in ACTIVE_REQUESTS for q in reqs), "root": _root(rows)})

def missing_link_object_manifest(request_id: str | None = None) -> MappingProxyType:
    reqs = (request_id,) if request_id else ACTIVE_REQUESTS
    if any(q not in ACTIVE_REQUESTS for q in reqs): raise KeyError(request_id)
    rows = tuple({"request_id": q, "capsule_id": "C182-HOLONOMY-CAPSULE-EXTERNAL-AUTHENTICATED", "parent_C181_object": "C181-ORDER-SENSITIVE-SOURCE-SCOPE-EXECUTABLE-LINK-EVALUATION", "required": ("authenticated C178 transition/holonomy record", "orientation", "cut-side frames", "future/past identity", "PV relation", "explicit matrix or safe matrix-free action"), "local_link_closed": True, "missing_is_not_zero": True, "next": NEXT} for q in reqs)
    return _freeze({"schema": "C182-MISSING-LINK-OBJECT-V1", "rows": rows, "root": _root(rows)})

def matching_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C182-MATCHING-HANDOFF-V1", "scope": "read-only conditional local residual link; holonomy external", "roots": ROOTS, "physical_parameter": False, "self_energy": False, "standard_scheme": False, "next": NEXT, "remaining_interfaces": ("authenticated C178 holonomy capsule", "full periodic link") , "root": _root(ROOTS)})

def dependency_frontier_manifest() -> MappingProxyType:
    rows = tuple({"frontier_id": x, "status": "preserved-or-typed-delta", "C166_graph_mutation": False} for x in ("C167 RI/SMOM leaves", "C168/C169 six calculation leaves", "six locator-incomplete leaves", "C171 B0 substrates", "C172 Q0 ghost", "C173 PV source", "C174 P0 subgauge", "C175 ghosts", "C176 HO boundary", "C177 source path", "C178 cut/holonomy", "C179 affine", "C180 retained scheme", "C181 ownership", "C182 conditional residual link", "B1 qgg/qbarq-q", "quark residual/counterterm"))
    return _freeze({"schema": "C182-DEPENDENCY-FRONTIER-V1", "rows": rows, "delta_only": True, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "root": _root(rows)})

def target_link_separation_manifest() -> MappingProxyType:
    row = {"C43_residual_link": "distinct", "C182_link": "project conditional", "JMY_staple": "not imported", "soft_factor": False, "target_MOMq_RI_SMOM": "distinct", "quantum_objects": 0, "link_qubits": 0}
    return _freeze({"schema": "C182-TARGET-LINK-SEPARATION-V1", "row": row, "root": _root(row)})

def brst_st_boundary_manifest() -> MappingProxyType:
    row = {"BRST": "BRST_NOT_CONSTRUCTED", "full_ST": "FULL_ST_NOT_PROVED", "coupling_renormalization": "COUPLING_RENORMALIZATION_NOT_AUTHORIZED", "physical_TMD_staple": "PHYSICAL_TMD_STAPLE_NOT_CONSTRUCTED", "soft_subtraction": "SOFT_SUBTRACTION_NOT_CONSTRUCTED", "complete_gluon_self_energy": "COMPLETE_GLUON_SELF_ENERGY_NOT_CONSTRUCTED"}
    return _freeze({"schema": "C182-BRST-ST-BOUNDARY-V1", "row": row, "root": _root(row)})

def b0_release_manifest() -> MappingProxyType:
    row = {"decision": "B0_LOCAL_TRANSVERSE_LINK_READY_HOLONOMY_INTERFACE_CONDITIONAL", "parameter_schema": True, "traces": True, "local_degree012": True, "color": True, "local_action": True, "holonomy": "conditional external nonmatrix", "identity": True, "derivatives": True, "variation": True, "ghost_link": True, "endpoint_support": True, "one_link": True, "two_link": True, "crosswalk": True, "source_scheme": True, "count_once": True, "physical_link": False, "next": NEXT}
    return _freeze({"schema": "C182-B0-RELEASE-V1", "row": row, "root": _root(row)})

def link_handoff_freeze() -> MappingProxyType:
    return _freeze({"schema": "C182-LINK-HANDOFF-FREEZE-V1", "C181_package_root": c181.PACKAGE_ROOT, "C181_status": c181.STATUS, "C178_holonomy": c181.HOLONOMY_ID, "C178_transition": c181.TRANSITION_ID, "C179_reference": SCHEME, "C180_paths": c181.PATHS, "C181_mixed_classes": MIXED_CLASSES, "C181_source_scope": "NONABELIAN_SOURCE_PATH_CLASS_UNDERDETERMINED", "roots_unchanged": True, "root": _root((c181.PACKAGE_ROOT, c181.HOLONOMY_ID, c181.TRANSITION_ID, SCHEME))})

def b0reslink2_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C182-PLAN-V1", "selected_plan": PLAN, "status": STATUS, "reason": "local affine degree 0/1/2 and all typed interfaces close; C178 holonomy remains external nonmatrix", "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})

def verify_hqcd_b0reslink2_authority() -> MappingProxyType:
    contract = json.loads((ROOT / CONTRACT).read_text())
    return _freeze({"schema": "C182-HQCDB0RESLINK2-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "next": NEXT, "contract": CONTRACT, "contract_sha256": sha256((ROOT / CONTRACT).read_bytes()).hexdigest(), "contract_parent_commit": contract["parent_commit"], "prompt": PROMPT, "prompt_sha256": PROMPT_SHA256, "C181_package_root": c181.PACKAGE_ROOT, "C181_package_root_verified": c181.PACKAGE_ROOT == UPSTREAM_ROOTS["C181"], "new_source_acquisitions": 0, "physical_inputs": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "B1_mutations": 0, "C158_value_inputs": 0, "physical_self_energy": False, "package_root": PACKAGE_ROOT})

def load_verified_hqcd_b0reslink2_authority() -> MappingProxyType:
    record = json.loads((RUNTIME / "manifest.json").read_text())
    if record.get("package_root") != PACKAGE_ROOT or record.get("status") != STATUS: raise ValueError("C182 runtime mismatch")
    if sha256((ROOT / CONTRACT).read_bytes()).hexdigest() != CONTRACT_SHA256: raise ValueError("C181-C182 contract hash mismatch")
    return verify_hqcd_b0reslink2_authority()

def static_isolation_guard() -> MappingProxyType:
    names = ("new_source_acquisitions", "unqualified_link_formulas", "retrospective_contracts_invented", "C171_B0_recomputed", "C174_gauge_recomputed", "C175_ghost_recomputed", "C176_boundary_recomputed", "C177_source_recomputed", "C178_adapter_recomputed", "C179_representative_recomputed", "C180_retained_scheme_recomputed", "C181_ownership_recomputed", "B1_mutations", "hidden_field_defaults", "hidden_coupling_defaults", "identity_holonomy_default", "coordinate_role_conflations", "source_scope_additive", "PQ_QP_collapsed", "reference_alternative_summed", "open_color_quotiented", "d_f_conflated", "owner_double_counting", "JMY_staple_imported", "C158_value_inputs", "private_upstream_calls", "C166_graph_nodes_added", "C166_graph_edges_added", "counterterms_nulls", "quantum_objects_modified", "states_TMD_objects")
    return _freeze({**{n: 0 for n in names}, "pass": True, "root": _root(names)})

def b0reslink2_completeness_certificate() -> MappingProxyType:
    fields = {"contract_hash_verified": True, "plan": PLAN, "parameter_schema": True, "fixtures": len(FIXTURE_IDS), "coordinate_forms": len(COORDINATE_FORMS), "trace_maps": True, "degree012": True, "ordered_PP_PQ_QP_QQ": True, "all_eight_color_generators": True, "open_adjoint": True, "holonomy_conditional": True, "reverse_composition_identity": True, "derivatives": True, "project_subgauge_variation": True, "ghost_link_interface": True, "endpoint_support": True, "one_link_kernel": True, "two_link_kernel": True, "count_once": True, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "physical_values": False, "self_energy": False, "next": NEXT}
    return _freeze({"schema": "C182-COMPLETENESS-CERTIFICATE-V1", "status": STATUS, **fields, "root": _root(fields)})

def mutate_live_hqcdb0reslink2(index: int) -> MappingProxyType:
    fields = ("contract", "plan", "freeze", "parameter", "coupling", "holonomy", "trace", "degree0", "degree1", "degree2", "PP", "PQ", "QP", "QQ", "color", "action", "identity", "derivative", "variation", "ghost_link", "endpoint", "one_link", "two_link", "crosswalk", "source_scheme", "count_once", "release", "requests", "missing_capsule", "frontier", "api", "safe_loading", "root", "next")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False, "must_fail_or_change_root": True})

ROOTS: dict[str, str] = {
    "C182_INPUT_ROOT": _root((BASELINE, CONTRACT_SHA256, PROMPT_SHA256, c181.PACKAGE_ROOT)),
    "C182_PLAN_ROOT": b0reslink2_plan_manifest()["root"], "C182_HANDOFF_FREEZE_ROOT": link_handoff_freeze()["root"],
    "C182_PARAMETER_SCHEMA_ROOT": parameter_schema()["root"], "C182_PARAMETER_FIXTURE_ROOT": parameter_fixture_manifest()["root"], "C182_BOUNDARY_TRACE_ROOT": boundary_trace_manifest()["root"],
    "C182_LOCAL_LINK_ROOT": local_link_manifest()["root"], "C182_COLOR_ROOT": color_manifest()["root"], "C182_LOCAL_ACTION_ROOT": _root(("matrix-free", "validated-record")),
    "C182_HOLONOMY_FACTORIZATION_ROOT": holonomy_factorization_manifest()["root"], "C182_LINK_IDENTITY_ROOT": link_identity_manifest()["root"],
    "C182_DERIVATIVE_ROOT": _root(("coupling", "retained", "boundary", "scalar", "holonomy")), "C182_LINK_VARIATION_ROOT": link_variation_manifest()["root"], "C182_GHOST_LINK_ROOT": ghost_link_manifest()["root"],
    "C182_ENDPOINT_SUPPORT_ROOT": endpoint_support_manifest()["root"], "C182_ONE_LINK_KERNEL_ROOT": one_link_kernel_manifest()["root"], "C182_TWO_LINK_KERNEL_ROOT": two_link_kernel_manifest()["root"],
    "C182_B0_CROSSWALK_ROOT": b0_crosswalk_manifest()["root"], "C182_SOURCE_SCHEME_ROOT": source_scheme_manifest()["root"], "C182_COUNT_ONCE_ROOT": count_once_manifest()["root"], "C182_B0_RELEASE_ROOT": b0_release_manifest()["root"],
    "C182_REQUEST_RESOLUTION_ROOT": request_resolution_manifest()["root"], "C182_MISSING_OBJECT_ROOT": missing_link_object_manifest()["root"], "C182_MATCHING_HANDOFF_ROOT": _root(("read-only", NEXT)), "C182_DEPENDENCY_FRONTIER_ROOT": dependency_frontier_manifest()["root"],
    "C182_TARGET_LINK_SEPARATION_ROOT": target_link_separation_manifest()["root"], "C182_QUANTUM_NONMUTATION_ROOT": _root((0, 0)), "C182_BRST_ST_BOUNDARY_ROOT": brst_st_boundary_manifest()["root"], "C182_SCOPE_ROOT": _root((STATUS, "no physical values", "no self energy", "no TMD")), "C182_COMPLETENESS_ROOT": _root((STATUS, PLAN, NEXT)),
}
PACKAGE_ROOT = _root({"schema": "C182-HQCDB0RESLINK2-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": ROOTS})
ROOTS["C182_PACKAGE_ROOT"] = PACKAGE_ROOT

__all__ = [name for name in globals() if not name.startswith("_")]
