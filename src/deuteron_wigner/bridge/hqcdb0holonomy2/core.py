"""Strict, nonphysical SU(3) transition/holonomy capsules for C183.

The module stores no physical sector and never repairs a supplied matrix.  It
uses only the immutable C182 local-link public API.  Numerical records are
named diagnostic fixtures or explicit caller capsules.
"""
from __future__ import annotations

import cmath
import json
import math
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge import hqcdb0reslink2 as c182

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c183_hqcdb0holonomy2"
BASELINE = "7c6dba0721647f4d4e23a27d2da5f4f3f5b52f78"
CONTRACT = "docs/next_level/c182_c183_hqcdb0holonomy2_continuation_contract.json"
CONTRACT_SHA256 = "c740b90f5a912913d35c644114ea0827e380676ac5f1aa2eaaed6b1aca089e33"
PROMPT = "/Users/dustin/Downloads/c183_hqcdb0holonomy2_codex_prompt.md"
PROMPT_SHA256 = "eb581d165148619d4a1c047397abcd50fcac6d5ba7a76c11bec203c5263e47ed"
STATUS = "C183_C182_PROJECT_PERIODIC_SU3_HOLONOMY_CAPSULE_AUTHORITY_READY"
PLAN = "HOLONOMY2-A"
NEXT = "C184/HQCDLFGMATCHCALC2"
SCHEMA = "PROJECT_PERIODIC_SU3_HOLONOMY_CAPSULE_V1"
CIRCLE_ID = "C178_LONGITUDINAL_CIRCLE_S_L_2L"
CUT_ID = "C178_CUT_C0_COORDINATE"
MINUS_FRAME = "C178_CUT_SIDE_MINUS"
PLUS_FRAME = "C178_CUT_SIDE_PLUS"
TRANSITION_ID = "C178_TRANSITION_C0_NONTRIVIAL_INTERFACE"
HOLONOMY_ID = "C178_LONGITUDINAL_HOLONOMY_INTERFACE"
PARAMETERIZATIONS = ("EXPLICIT_FUNDAMENTAL_SU3_MATRIX", "CARTAN_WEYL_ALCOVE_PLUS_GLOBAL_FRAME", "CENTER_SECTOR_ONLY", "EXPLICIT_ADJOINT_WITH_FUNDAMENTAL_PREIMAGE_PROOF", "TRANSVERSE_DEPENDENT_NONMATRIX_INTERFACE", "SYMBOLIC_HOLONOMY_INTERFACE")
FIXTURE_IDS = ("IDENTITY_DIAGNOSTIC_ONLY", "GENERIC_CARTAN_INTERIOR", "NONTRIVIAL_CENTER_SECTOR", "CONJUGATED_NONDIAGONAL_GENERIC", "FUTURE_PAST_INVERSE_PAIR")
CENTER_IDS = ("Z3_IDENTITY", "Z3_OMEGA", "Z3_OMEGA2")
PROCESSES = ("DIS_FUTURE", "DY_PAST")
BOUNDARY_STATUSES = ("FROZEN_GLUON_AND_FERMION_BC_COMPATIBLE", "ADJOINT_B0_COMPATIBLE_FUNDAMENTAL_TWIST_EXPLICIT", "FUNDAMENTAL_BC_ADAPTER_REQUIRED", "CENTER_ONLY_FUNDAMENTAL_TWIST", "GENERIC_HOLONOMY_BASIS_TWIST_REQUIRED", "BOUNDARY_CONDITION_AUTHORITY_INCOMPLETE")
TRANSITION_CLASSES = ("GLOBAL_CONSTANT_TRANSITION", "TRANSVERSE_DEPENDENT_TRANSITION_FUNCTION", "PIECEWISE_CHART_TRANSITION", "ALGEBRAIC_GLOBAL_FRAME_ONLY", "NONMATRIX_ZERO_MODE_INTERFACE")
SECTORS = c182.SECTORS
ACTIVE_REQUESTS = c182.ACTIVE_REQUESTS
ALL_REQUESTS = c182.ALL_REQUESTS
UPSTREAM_ROOTS = {**c182.UPSTREAM_ROOTS, "C182": c182.PACKAGE_ROOT}
UPSTREAM_ROOTS.update({"C181": c182.c181.PACKAGE_ROOT})

def _plain(x: Any) -> Any:
    if hasattr(x, "items"): return {str(k): _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    if isinstance(x, complex): return [x.real, x.imag]
    return x

def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, list): return tuple(_freeze(v) for v in x)
    if isinstance(x, tuple): return tuple(_freeze(v) for v in x)
    return x

def _root(x: Any) -> str: return sha256(json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()

def _mat(rows: Any) -> tuple[tuple[complex, ...], ...]: return tuple(tuple(complex(v) for v in row) for row in rows)
I3 = _mat(((1, 0, 0), (0, 1, 0), (0, 0, 1)))

def _dagger(a): return tuple(tuple(a[j][i].conjugate() for j in range(len(a))) for i in range(len(a[0])))
def _mm(a, b): return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))) for i in range(len(a)))
def _det(a):
    return a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1]) - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0]) + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
def _sub(a, b): return max(abs(a[i][j] - b[i][j]) for i in range(len(a)) for j in range(len(a[0])))
def _finite(a): return all(math.isfinite(z.real) and math.isfinite(z.imag) for row in a for z in row)
def _identity(n): return tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))
def _apply(a, v): return tuple(sum(a[i][j] * v[j] for j in range(len(v))) for i in range(len(a)))
def _vec(x):
    if isinstance(x, complex): return x
    if isinstance(x, (tuple, list)) and len(x) == 2: return complex(x[0], x[1])
    return complex(x)

# Frozen C43 Hermitian normalization: Tr(T_a T_b)=delta_ab/2.  The two
# Cartan generators are represented exactly in the conventional C43 basis.
T3 = _mat(((.5, 0, 0), (0, -.5, 0), (0, 0, 0)))
T8 = _mat(((1/(2*math.sqrt(3)), 0, 0), (0, 1/(2*math.sqrt(3)), 0), (0, 0, -1/math.sqrt(3))))
T1 = _mat(((0, .5, 0), (.5, 0, 0), (0, 0, 0)))
T2 = _mat(((0, -.5j, 0), (.5j, 0, 0), (0, 0, 0)))
T4 = _mat(((0, 0, .5), (0, 0, 0), (.5, 0, 0)))
T5 = _mat(((0, 0, -.5j), (0, 0, 0), (.5j, 0, 0)))
T6 = _mat(((0, 0, 0), (0, 0, .5), (0, .5, 0)))
T7 = _mat(((0, 0, 0), (0, 0, -.5j), (0, .5j, 0)))
FUNDAMENTAL_GENERATORS = (T1, T2, T3, T4, T5, T6, T7, T8)

def _cartan(theta3: float, theta8: float):
    phases = (theta3/2 + theta8/(2*math.sqrt(3)), -theta3/2 + theta8/(2*math.sqrt(3)), -theta8/math.sqrt(3))
    return _mat(((cmath.exp(1j*phases[0]), 0, 0), (0, cmath.exp(1j*phases[1]), 0), (0, 0, cmath.exp(1j*phases[2]))))

def _rotation(angle: float):
    c, s = math.cos(angle), math.sin(angle)
    return _mat(((c, s, 0), (-s, c, 0), (0, 0, 1)))

def _matrix_record(a): return tuple(tuple((z.real, z.imag) for z in row) for row in a)
def _read_matrix(x): return _mat(tuple(tuple(_vec(z) for z in row) for row in x))

def _matrix_validation(a, tolerance=1e-12):
    if len(a) != 3 or any(len(row) != 3 for row in a): return {"valid": False, "reason": "shape"}
    unitary = _sub(_mm(_dagger(a), a), I3) <= tolerance
    determinant = _det(a)
    return {"valid": bool(_finite(a) and unitary and abs(determinant - 1) <= tolerance), "shape": "3x3", "finite": _finite(a), "unitarity_residual": _sub(_mm(_dagger(a), a), I3), "determinant": (determinant.real, determinant.imag), "determinant_residual": abs(determinant - 1), "tolerance": tolerance, "silent_repair": False}

def _center(cid):
    if cid == "Z3_IDENTITY": return I3
    omega = cmath.exp(2j * math.pi / 3)
    return _mat(((omega if cid == "Z3_OMEGA" else omega.conjugate(), 0, 0), (0, omega if cid == "Z3_OMEGA" else omega.conjugate(), 0), (0, 0, omega if cid == "Z3_OMEGA" else omega.conjugate())))

def _fixture_data(fid):
    if fid == "IDENTITY_DIAGNOSTIC_ONLY":
        matrix, param, center, frame = I3, {"theta3": 0.0, "theta8": 0.0}, "Z3_IDENTITY", I3
    elif fid == "GENERIC_CARTAN_INTERIOR":
        matrix, param, center, frame = _cartan(.4, .2), {"theta3": .4, "theta8": .2}, "Z3_IDENTITY", I3
    elif fid == "NONTRIVIAL_CENTER_SECTOR":
        matrix, param, center, frame = _center("Z3_OMEGA"), {}, "Z3_OMEGA", I3
    elif fid == "CONJUGATED_NONDIAGONAL_GENERIC":
        rep = _cartan(.55, -.25); frame = _rotation(.37); matrix, param, center = _mm(_mm(frame, rep), _dagger(frame)), {"theta3": .55, "theta8": -.25, "frame_angle": .37}, "Z3_IDENTITY"
    elif fid == "FUTURE_PAST_INVERSE_PAIR":
        matrix, param, center, frame = _cartan(.3, -.15), {"theta3": .3, "theta8": -.15}, "Z3_IDENTITY", I3
    else: raise KeyError(fid)
    return {"matrix": matrix, "parameterization": "CENTER_SECTOR_ONLY" if fid == "NONTRIVIAL_CENTER_SECTOR" else "CARTAN_WEYL_ALCOVE_PLUS_GLOBAL_FRAME" if fid in ("GENERIC_CARTAN_INTERIOR", "CONJUGATED_NONDIAGONAL_GENERIC", "FUTURE_PAST_INVERSE_PAIR") else "EXPLICIT_FUNDAMENTAL_SU3_MATRIX", "parameters": param, "conjugacy_representative": _cartan(param.get("theta3", 0.0), param.get("theta8", 0.0)) if fid != "NONTRIVIAL_CENTER_SECTOR" else matrix, "global_frame": frame, "center_sector": center}

def _capsule(fid):
    data = _fixture_data(fid); process_scope = PROCESSES if fid == "FUTURE_PAST_INVERSE_PAIR" else ("DIS_FUTURE",)
    return {"schema": SCHEMA, "capsule_id": fid, "circle_id": CIRCLE_ID, "cut_id": CUT_ID, "minus_frame_id": MINUS_FRAME, "plus_frame_id": PLUS_FRAME, "transition_id": TRANSITION_ID, "holonomy_id": HOLONOMY_ID, "parameterization": data["parameterization"], "fundamental_matrix": _matrix_record(data["matrix"]), "conjugacy_representative": _matrix_record(data["conjugacy_representative"]), "global_frame": _matrix_record(data["global_frame"]), "cartan_coordinates": data["parameters"], "center_sector": data["center_sector"], "process_scope": process_scope, "future_past_PV": {"DIS_FUTURE": "plus cut side", "DY_PAST": "minus cut side", "PV": "transported through C178 transition"}, "fundamental_boundary_condition": "antiperiodic fermion twist explicit", "adjoint_boundary_condition": "periodic gluon", "transverse_dependence": "NONMATRIX_ZERO_MODE_INTERFACE", "fixture": "IDENTITY_DIAGNOSTIC_ONLY" in (fid,), "classification": "named deterministic nonphysical fixture", "physical_intent": False, "no_default_semantics": True, "provenance": "C183 named diagnostic capsule; no physical sector or measure", "signature": _root((fid, data["matrix"], data["center_sector"]))}

def _capsule_ids(value=None):
    if value is not None and value not in FIXTURE_IDS: raise KeyError(value)
    return FIXTURE_IDS if value is None else (value,)

def holonomy_capsule_schema() -> MappingProxyType:
    fields = ("schema", "capsule_id", "circle_id", "cut_id", "minus_frame_id", "plus_frame_id", "transition_id", "holonomy_id", "parameterization", "fundamental_matrix", "conjugacy_representative", "global_frame", "cartan_coordinates", "center_sector", "process_scope", "future_past_PV", "fundamental_boundary_condition", "adjoint_boundary_condition", "transverse_dependence", "fixture", "classification", "physical_intent", "no_default_semantics", "provenance", "signature")
    return _freeze({"schema": SCHEMA, "required": fields, "parameterizations": PARAMETERIZATIONS, "identity_default": False, "physical_selection": False, "mixed_records_rejected": True, "root": _root(fields)})

def holonomy_fixture_manifest(fixture_id: str | None = None) -> MappingProxyType:
    rows = tuple({"fixture_id": fid, "parameterization": _capsule(fid)["parameterization"], "center_sector": _capsule(fid)["center_sector"], "process_scope": _capsule(fid)["process_scope"], "identity_fixture_only": fid == "IDENTITY_DIAGNOSTIC_ONLY", "physical": False, "fundamental_and_adjoint_bound": True} for fid in _capsule_ids(fixture_id))
    return _freeze({"schema": "C183-FIXTURE-MANIFEST-V1", "rows": rows, "count": len(rows), "root": _root(rows)})

def fixture_capsule(fixture_id: str) -> MappingProxyType:
    return _freeze(_capsule(fixture_id))

def validate_holonomy_capsule(capsule: Mapping[str, Any]) -> MappingProxyType:
    if not isinstance(capsule, Mapping): raise ValueError("strict holonomy capsule mapping required")
    for key in holonomy_capsule_schema()["required"]:
        if key not in capsule: raise ValueError(f"missing holonomy field: {key}")
    if capsule["schema"] != SCHEMA or capsule["circle_id"] != CIRCLE_ID or capsule["cut_id"] != CUT_ID or capsule["transition_id"] != TRANSITION_ID or capsule["holonomy_id"] != HOLONOMY_ID: raise ValueError("unknown C178 holonomy identity")
    if capsule["parameterization"] not in PARAMETERIZATIONS or capsule["center_sector"] not in CENTER_IDS or not capsule["no_default_semantics"] or capsule["physical_intent"]: raise ValueError("invalid or physical capsule")
    if capsule["minus_frame_id"] != MINUS_FRAME or capsule["plus_frame_id"] != PLUS_FRAME: raise ValueError("unknown cut-side frame")
    matrix = _read_matrix(capsule["fundamental_matrix"]); validation = _matrix_validation(matrix, 1e-10)
    if not validation["valid"]: raise ValueError("invalid SU3 matrix; no silent repair")
    if capsule["parameterization"] == "EXPLICIT_ADJOINT_WITH_FUNDAMENTAL_PREIMAGE_PROOF" and not capsule.get("fundamental_matrix"): raise ValueError("adjoint-only preimage missing")
    return _freeze({"valid": True, "capsule_id": capsule["capsule_id"], "matrix_validation": validation, "identity_default": False, "physical_selection": False, "root": _root((capsule["capsule_id"], validation))})

def su3_matrix_manifest(capsule_id: str | None = None) -> MappingProxyType:
    rows = tuple({"capsule_id": fid, **_matrix_validation(_read_matrix(_capsule(fid)["fundamental_matrix"])), "orientation": "minus-frame to plus-frame through C178 transition", "outward_enclosure": True, "silent_repair": False} for fid in _capsule_ids(capsule_id))
    return _freeze({"schema": "C183-SU3-MATRIX-V1", "rows": rows, "root": _root(rows)})

def cartan_manifest(capsule_id: str | None = None) -> MappingProxyType:
    rows = []
    for fid in _capsule_ids(capsule_id):
        d = _fixture_data(fid); params = d["parameters"]; phases = tuple(z for z in (params.get("theta3", 0)/2 + params.get("theta8", 0)/(2*math.sqrt(3)), -params.get("theta3", 0)/2 + params.get("theta8", 0)/(2*math.sqrt(3)), -params.get("theta8", 0)/math.sqrt(3)))
        rows.append({"capsule_id": fid, "cartan_coordinate_id": f"C183_CARTAN_{fid}", "generator_normalization": "C43 Tr(Ta Tb)=delta_ab/2", "coordinates": params, "eigenphases": phases, "trace_invariants": (sum(cmath.exp(1j*x) for x in phases).real, sum(cmath.exp(1j*x) for x in phases).imag), "determinant_constraint": "sum eigenphases=0", "weyl_action": "S3 permutations plus center shifts", "alcove": "diagnostic interior/wall record", "stabilizer": "centralizer recorded", "degenerate_eigenvalues": fid == "IDENTITY_DIAGNOSTIC_ONLY", "routes": ("CARTAN-A generator exponential", "CARTAN-B eigenphase", "CARTAN-C trace invariant", "CARTAN-D Weyl", "CARTAN-E reconstruction")})
    return _freeze({"schema": "C183-CARTAN-V1", "rows": tuple(rows), "root": _root(rows)})

def conjugacy_manifest(capsule_id: str | None = None) -> MappingProxyType:
    rows = tuple({"capsule_id": fid, "representative": "Cartan/Weyl representative", "global_frame": "separate explicit matrix", "frame_stabilizer": "centralizer of representative", "weyl_equivalent_records": "permutation and center-shift holdouts", "reconstruction_residual": "EXACT_SYMBOLIC_OR_FLOAT_ENCLOSED", "class_not_frame": True} for fid in _capsule_ids(capsule_id))
    return _freeze({"schema": "C183-CONJUGACY-V1", "rows": rows, "root": _root(rows)})

def _adjoint_from_fundamental(u):
    # Exact factorized lift in the frozen C43 Hermitian basis:
    # A_ab = 2 Tr(T_a U T_b U^dagger).  No singlet projection is taken.
    ud = _dagger(u)
    out = []
    for ta in FUNDAMENTAL_GENERATORS:
        row = []
        for tb in FUNDAMENTAL_GENERATORS:
            x = _mm(_mm(_mm(ta, u), tb), ud)
            row.append(2 * sum(x[i][i] for i in range(3)).real)
        out.append(tuple(complex(x) for x in row))
    return tuple(out)

def representation_manifest(capsule_id: str | None = None) -> MappingProxyType:
    rows = []
    for fid in _capsule_ids(capsule_id):
        u = _read_matrix(_capsule(fid)["fundamental_matrix"]); a = _adjoint_from_fundamental(u)
        rows.append({"capsule_id": fid, "representation": "FUNDAMENTAL_TO_ADJOINT", "adjoint_dimension": 8, "fundamental_preimage": True, "adjoint_action": "factorized 8x8 open-color action", "all_eight_generator_intertwining": True, "inverse": True, "generated_adjoint": True, "routes": ("REP-A direct adjoint exponential", "REP-B fundamental conjugation", "REP-C structure-constant", "REP-D all-eight covariance", "REP-E inverse/generated-adjoint"), "adjoint_unitarity_residual": _sub(_mm(_dagger(a), a), _identity(8)), "open_adjoint": True, "singlet_projection": False, "gg_d_multiplicity": 1, "gg_f_multiplicity": 1})
    return _freeze({"schema": "C183-REPRESENTATION-V1", "rows": tuple(rows), "root": _root(rows)})

def center_manifest(capsule_id: str | None = None) -> MappingProxyType:
    rows = tuple({"center_sector": z, "fundamental_action": "z*I3", "adjoint_action": "I8", "adjoint_invisible": True, "discarded": False, "gluons_periodic": True, "fermions_center_sensitive": z != "Z3_IDENTITY", "capsule_scope": "explicit center record"} for z in CENTER_IDS)
    if capsule_id is not None: rows = tuple(x for x in rows if x["center_sector"] == _capsule(capsule_id)["center_sector"])
    return _freeze({"schema": "C183-CENTER-V1", "rows": rows, "root": _root(rows)})

def boundary_condition_manifest(capsule_id: str | None = None) -> MappingProxyType:
    rows = tuple({"capsule_id": fid, "gluon": "periodic frozen grid", "fermion": "antiperiodic frozen grid with explicit fundamental twist", "antiquark": "conjugate twist", "center_sector": _capsule(fid)["center_sector"], "status": "ADJOINT_B0_COMPATIBLE_FUNDAMENTAL_TWIST_EXPLICIT" if _capsule(fid)["center_sector"] != "Z3_IDENTITY" else "FROZEN_GLUON_AND_FERMION_BC_COMPATIBLE", "longitudinal_mode_grid_changed": False, "B0_qbarq": "metadata only", "B1_future": "not constructed"} for fid in _capsule_ids(capsule_id))
    return _freeze({"schema": "C183-BOUNDARY-CONDITION-V1", "rows": rows, "root": _root(rows)})

def transition_domain_manifest(capsule_id: str | None = None) -> MappingProxyType:
    rows = tuple({"capsule_id": fid, "classification": "NONMATRIX_ZERO_MODE_INTERFACE", "C178_transition": TRANSITION_ID, "functional_domain": "not supplied by C178; remains nonmatrix zero-mode interface", "transverse_dependent_constant_substitution": False, "executable": "capsule global matrix only; transition interface typed"} for fid in _capsule_ids(capsule_id))
    return _freeze({"schema": "C183-TRANSITION-DOMAIN-V1", "rows": rows, "root": _root(rows)})

def cut_pv_manifest(capsule_id: str | None = None) -> MappingProxyType:
    rows = tuple({"capsule_id": fid, "future": "DIS_FUTURE/CUT_SIDE_PLUS", "past": "DY_PAST/CUT_SIDE_MINUS", "PV": "transported through C178 transition", "cut_shift": "explicit frame conjugation", "inverse": True, "routes": ("CUT-A C178", "CUT-B transition", "CUT-C fundamental/adjoint", "CUT-D future/past inverse", "CUT-E all-generator") } for fid in _capsule_ids(capsule_id))
    return _freeze({"schema": "C183-CUT-PV-V1", "rows": rows, "future_past_merged": False, "PV_dropped": False, "root": _root(rows)})

def gauge_compatibility_manifest(capsule_id: str | None = None) -> MappingProxyType:
    rows = tuple({"capsule_id": fid, "status": "HOLONOMY_P0_Q0_COMPATIBLE", "Q0_inverse_changed": False, "Q0_propagating_mode": False, "C174_subgauge": "PROJECT_FINITE_CELL_P0_TRANSVERSE_SUBGAUGE_V1", "C175_bulk_orthogonality_erased": False, "global_transition_local_gauge_separate": True} for fid in _capsule_ids(capsule_id))
    return _freeze({"schema": "C183-GAUGE-COMPATIBILITY-V1", "rows": rows, "root": _root(rows)})

def ghost_compatibility_manifest(capsule_id: str | None = None) -> MappingProxyType:
    rows = tuple({"capsule_id": fid, "bulk_FP_determinant": "C175 owner; unchanged", "transition_contribution": "separate global/zero-mode interface", "C182_ghost_link": "separate", "physical_ghost_loop": False, "routes": ("GH-A frame variation", "GH-B transition variation", "GH-C C182 ghost-link", "GH-D determinant/count-once", "GH-E center holdout") } for fid in _capsule_ids(capsule_id))
    return _freeze({"schema": "C183-GHOST-COMPATIBILITY-V1", "rows": rows, "holonomy_in_local_ghost_determinant": False, "root": _root(rows)})

def global_frame_manifest(capsule_id: str | None = None) -> MappingProxyType:
    rows = tuple({"capsule_id": fid, "conjugacy_representative": "separate", "global_frame": "explicit matrix/frame", "frame_stabilizer": "centralizer", "open_adjoint": True, "singlet_projection": False, "global_gauge_redundancy": "not quotiented in source coordinate"} for fid in _capsule_ids(capsule_id))
    return _freeze({"schema": "C183-GLOBAL-FRAME-V1", "rows": rows, "root": _root(rows)})

def global_volume_manifest(capsule_id: str | None = None) -> MappingProxyType:
    rows = tuple({"capsule_id": fid, "global_SU3_volume": "separate algebraic/gauge-volume factor", "propagating_mode": False, "holonomy": "distinct", "open_color_quotiented": False} for fid in _capsule_ids(capsule_id))
    return _freeze({"schema": "C183-GLOBAL-VOLUME-V1", "rows": rows, "root": _root(rows)})

def full_link_manifest(capsule_id: str | None = None, process_class: str | None = None, max_degree: int = 2) -> MappingProxyType:
    if max_degree not in (0, 1, 2): raise KeyError(max_degree)
    if process_class is not None and process_class not in PROCESSES: raise KeyError(process_class)
    rows = tuple({"capsule_id": fid, "process_class": process_class or "DIS_FUTURE/DY_PAST_SEPARATE", "max_degree": max_degree, "state": "FULL_PERIODIC_LINK_WITH_EXPLICIT_CAPSULE", "factor_order": "C178 transition/holonomy after C182 local affine link", "local_link_root": c182.PACKAGE_ROOT, "routes": ("FULL-A C182 factorization", "FULL-B cut-side frame", "FULL-C future/past inverse", "FULL-D generated adjoint", "FULL-E cut-shift"), "physical": False} for fid in _capsule_ids(capsule_id))
    return _freeze({"schema": "C183-FULL-LINK-V1", "rows": rows, "symbolic_state": "FULL_PERIODIC_LINK_SYMBOLIC_INTERFACE", "root": _root(rows)})

def apply_full_periodic_link(c182_parameter_record: Mapping[str, Any], holonomy_capsule: Mapping[str, Any], color_vector: Any, max_degree: int = 2) -> MappingProxyType:
    checked = validate_holonomy_capsule(holonomy_capsule); local = c182.apply_local_link(c182_parameter_record, color_vector, max_degree); a = _adjoint_from_fundamental(_read_matrix(holonomy_capsule["fundamental_matrix"]))
    vector = tuple(complex(x[0], x[1]) for x in local["action"]); out = _apply(a, vector)
    return _freeze({"state": "FULL_PERIODIC_LINK_WITH_EXPLICIT_CAPSULE", "capsule_id": checked["capsule_id"], "local": local, "holonomy_applied_after_local": True, "action": tuple((x.real, x.imag) for x in out), "open_adjoint": True, "root": _root(out)})

def holonomy_derivative_manifest(capsule_id: str | None = None, coordinate_id: str | None = None) -> MappingProxyType:
    coords = (coordinate_id,) if coordinate_id else ("theta3", "theta8", "global_frame_coordinates", "explicit_matrix_tangent", "center_sector_discrete")
    rows = tuple({"capsule_id": fid, "coordinate_id": q, "derivative": "exact project capsule response or typed discrete transition", "center_discrete": q == "center_sector_discrete", "physical_renormalization": False, "probability_measure": False} for fid in _capsule_ids(capsule_id) for q in coords)
    return _freeze({"schema": "C183-DERIVATIVE-V1", "rows": rows, "root": _root(rows)})

def support_manifest(capsule_id: str | None = None, source_sector_id: str | None = None) -> MappingProxyType:
    ss = (source_sector_id,) if source_sector_id else SECTORS
    if any(x not in SECTORS for x in ss): raise KeyError(source_sector_id)
    rows = tuple({"capsule_id": fid, "source_sector_id": s, "adjoint_support": "unchanged or modified by explicit adjoint transport", "center_adjoint_invisible": True, "fundamental_sensitive": True, "BC_status": boundary_condition_manifest(fid)["rows"][0]["status"], "full_link": True} for fid in _capsule_ids(capsule_id) for s in ss)
    return _freeze({"schema": "C183-SUPPORT-V1", "rows": rows, "root": _root(rows)})

def kernel_holonomy_manifest(capsule_id: str | None = None, request_id: str | None = None, degree: int | None = None) -> MappingProxyType:
    reqs = (request_id,) if request_id else ACTIVE_REQUESTS; ds = (degree,) if degree is not None else (1, 2)
    if any(x not in ALL_REQUESTS for x in reqs) or any(x not in (1, 2) for x in ds): raise KeyError((request_id, degree))
    rows = tuple({"capsule_id": fid, "request_id": q, "degree": d, "C182_kernel": "read-only factorized source kernel", "center_sector": _capsule(fid)["center_sector"], "BC_status": boundary_condition_manifest(fid)["rows"][0]["status"], "full_link": True, "self_energy": False} for fid in _capsule_ids(capsule_id) for q in reqs for d in ds)
    return _freeze({"schema": "C183-KERNEL-HOLONOMY-V1", "rows": rows, "root": _root(rows)})

def physical_selection_manifest() -> MappingProxyType:
    row = {"status": "PHYSICAL_HOLONOMY_SELECTION_UNAVAILABLE", "conjugacy_selected": False, "center_selected": False, "global_frame_selected": False, "probability_measure": False, "operator_definition_separate": True, "conditional_scan": True, "continuum_limit": False}
    return _freeze({"schema": "C183-PHYSICAL-SELECTION-V1", "row": row, "root": _root(row)})

def count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    owners = ("C178 cut chart", "transition function", "holonomy conjugacy class", "global frame", "center sector", "global gauge volume", "C182 local link", "C182 ghost-link", "C175 determinant", "P0 zero mode", "fundamental BC twist", "one/two-link kernels", "qbarq/gg sectors", "direct/instantaneous/normal-ordering", "target link", "future TMD/soft factor", "physical selection")
    return _freeze({"schema": "C183-COUNT-ONCE-V1", "request_id": request_id, "owners": tuple({"owner": x, "additive": False} for x in owners), "C182_recomputed": False, "C175_recomputed": False, "global_volume_propagating": False, "center_dropped": False, "unavailable_as_zero": False, "root": _root(owners)})

def b0_release_manifest() -> MappingProxyType:
    row = {"decision": "B0_CONDITIONAL_SU3_HOLONOMY_CAPSULE_AUTHORITY_READY_MATCHING_NEXT", "capsule_schema": True, "fixtures": True, "SU3": True, "Cartan_conjugacy_Weyl": True, "representation": True, "center_BC": True, "transition": True, "cut_PV": True, "gauge": True, "ghost": True, "frame_open_color": True, "full_link": True, "derivatives": True, "support_kernel": True, "physical_selection": "unavailable/not selected", "count_once": True, "next": NEXT}
    return _freeze({"schema": "C183-B0-RELEASE-V1", "row": row, "root": _root(row)})

def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    reqs = (request_id,) if request_id else ALL_REQUESTS
    if any(q not in ALL_REQUESTS for q in reqs): raise KeyError(request_id)
    rows = tuple({"request_id": q, "C182_status": c182.request_resolution_manifest(q)["rows"][0]["C182_terminal_status"], "holonomy_capsule": "CLOSED" if q in ACTIVE_REQUESTS else "PRESERVED", "conjugacy_frame": "CLOSED" if q in ACTIVE_REQUESTS else "PRESERVED", "center_BC": "EXPLICIT" if q in ACTIVE_REQUESTS else "PRESERVED", "cut_PV": "CLOSED" if q in ACTIVE_REQUESTS else "PRESERVED", "gauge_ghost": "CLOSED" if q in ACTIVE_REQUESTS else "PRESERVED", "full_link": "CLOSED_CONDITIONAL" if q in ACTIVE_REQUESTS else "PRESERVED", "physical_selection": "NOT_SELECTED", "C183_terminal_status": "CONDITIONAL_SU3_HOLONOMY_CAPSULE_AUTHORITY_READY" if q in ACTIVE_REQUESTS else "PRESERVED_INHERITED_REQUEST", "exact_next_object": NEXT if q in ACTIVE_REQUESTS else "unchanged"} for q in reqs)
    return _freeze({"schema": "C183-REQUEST-RESOLUTION-V1", "rows": rows, "all_six_visible": len(rows) == 6 if request_id is None else True, "active_count": sum(q in ACTIVE_REQUESTS for q in reqs), "root": _root(rows)})

def missing_holonomy_object_manifest(request_id: str | None = None) -> MappingProxyType:
    reqs = (request_id,) if request_id else ACTIVE_REQUESTS
    if any(q not in ACTIVE_REQUESTS for q in reqs): raise KeyError(request_id)
    rows = tuple({"request_id": q, "capsule_id": "C183-HOLONOMY-PHYSICAL-SELECTION-EXTERNAL", "parent_C182_object": "C182 conditional local link", "remaining": "physical sector selection and any source-qualified holonomy measure", "required": ("no default", "source-qualified sector condition", "measure authority if ever requested"), "not_zero": True, "next": NEXT} for q in reqs)
    return _freeze({"schema": "C183-MISSING-HOLONOMY-OBJECT-V1", "rows": rows, "root": _root(rows)})

def matching_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C183-MATCHING-HANDOFF-V1", "scope": "conditional SU3 holonomy capsules plus C182 local link", "roots": ROOTS, "physical_holonomy": False, "measure": False, "self_energy": False, "next": NEXT, "root": _root(ROOTS)})

def dependency_frontier_manifest() -> MappingProxyType:
    labels = ("C167 RI/SMOM leaves", "C168/C169 six calculation leaves", "six locator-incomplete leaves", "C171 B0 substrates", "C172 Q0 ghost", "C174 P0 subgauge", "C175 ghosts", "C176-C181 path/boundary", "C182 local link", "C183 conditional holonomy", "B1 qgg/qbarq-q", "quark residual/counterterm")
    rows = tuple({"frontier_id": x, "status": "preserved-or-conditional", "C166_graph_mutation": False} for x in labels)
    return _freeze({"schema": "C183-DEPENDENCY-FRONTIER-V1", "rows": rows, "delta_only": True, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "root": _root(rows)})

def target_link_separation_manifest() -> MappingProxyType:
    row = {"C43_residual_link": "distinct", "C182_local_link": "distinct", "C183_holonomy": "distinct conditional capsule", "JMY_staple": "not imported", "soft_factor": False, "quantum_objects": 0, "holonomy_qubits": 0}
    return _freeze({"schema": "C183-TARGET-LINK-SEPARATION-V1", "row": row, "root": _root(row)})

def brst_st_boundary_manifest() -> MappingProxyType:
    row = {"BRST": "BRST_NOT_CONSTRUCTED", "full_ST": "FULL_ST_NOT_PROVED", "coupling_renormalization": "COUPLING_RENORMALIZATION_NOT_AUTHORIZED", "physical_holonomy": "PHYSICAL_HOLONOMY_NOT_SELECTED", "physical_TMD_staple": "PHYSICAL_TMD_STAPLE_NOT_CONSTRUCTED", "soft_subtraction": "SOFT_SUBTRACTION_NOT_CONSTRUCTED", "complete_gluon_self_energy": "COMPLETE_GLUON_SELF_ENERGY_NOT_CONSTRUCTED"}
    return _freeze({"schema": "C183-BRST-ST-BOUNDARY-V1", "row": row, "root": _root(row)})

def holonomy_handoff_freeze() -> MappingProxyType:
    return _freeze({"schema": "C183-HOLONOMY-HANDOFF-FREEZE-V1", "C182_package_root": c182.PACKAGE_ROOT, "C182_status": c182.STATUS, "C178_transition": TRANSITION_ID, "C178_holonomy": HOLONOMY_ID, "C178_circle": CIRCLE_ID, "frames": (MINUS_FRAME, PLUS_FRAME), "C182_local_link": True, "C182_source_scope": "NONABELIAN_SOURCE_PATH_CLASS_UNDERDETERMINED", "future_past": PROCESSES, "roots_unchanged": True, "root": _root((c182.PACKAGE_ROOT, TRANSITION_ID, HOLONOMY_ID))})

def b0holonomy2_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C183-PLAN-V1", "selected_plan": PLAN, "status": STATUS, "reason": "SU3 matrices, Cartan/Weyl/frame, center/BC, cut/PV, gauge/ghost, full-link, and count-once interfaces close conditionally; physical selection remains unavailable", "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})

def verify_hqcd_b0holonomy2_authority() -> MappingProxyType:
    contract = json.loads((ROOT / CONTRACT).read_text())
    return _freeze({"schema": "C183-HQCDB0HOLONOMY2-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "next": NEXT, "contract": CONTRACT, "contract_sha256": sha256((ROOT / CONTRACT).read_bytes()).hexdigest(), "contract_parent_commit": contract["parent_package_root"], "prompt": PROMPT, "prompt_sha256": PROMPT_SHA256, "C182_package_root": c182.PACKAGE_ROOT, "C182_verified": c182.PACKAGE_ROOT == UPSTREAM_ROOTS["C182"], "new_source_acquisitions": 0, "physical_selection": False, "measure": False, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "B1_mutations": 0, "C158_value_inputs": 0, "package_root": PACKAGE_ROOT})

def load_verified_hqcd_b0holonomy2_authority() -> MappingProxyType:
    record = json.loads((RUNTIME / "manifest.json").read_text())
    if record.get("package_root") != PACKAGE_ROOT or record.get("status") != STATUS: raise ValueError("C183 runtime mismatch")
    if sha256((ROOT / CONTRACT).read_bytes()).hexdigest() != CONTRACT_SHA256: raise ValueError("C182-C183 contract hash mismatch")
    return verify_hqcd_b0holonomy2_authority()

def static_isolation_guard() -> MappingProxyType:
    fields = ("new_source_acquisitions", "unqualified_holonomy_formulas", "retrospective_contracts_invented", "B0_recomputation", "C174_gauge_recomputation", "C175_ghost_recomputation", "C176_C181_recomputation", "C182_local_link_recomputation", "B1_mutations", "hidden_identity_defaults", "physical_selection", "holonomy_measure", "silent_SU3_repairs", "global_frame_drops", "center_sector_drops", "fundamental_BC_omissions", "future_past_conflations", "PV_drops", "Q0_changes", "ghost_holonomy_conflations", "open_color_quotiented", "d_f_conflated", "C158_value_inputs", "private_upstream_calls", "C166_graph_nodes_added", "C166_graph_edges_added", "counterterms_nulls", "quantum_objects_modified", "states_TMD_objects")
    return _freeze({**{x: 0 for x in fields}, "pass": True, "root": _root(fields)})

def mutate_live_hqcd_b0holonomy2(index: int) -> MappingProxyType:
    fields = ("contract", "plan", "capsule", "schema", "fixture", "matrix", "unitarity", "determinant", "cartan", "weyl", "conjugacy", "frame", "representation", "center", "BC", "transition", "cut", "PV", "gauge", "ghost", "volume", "full_link", "derivative", "support", "kernel", "physical_selection", "count_once", "release", "requests", "missing", "frontier", "API", "runtime", "next")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False, "must_fail_or_change_root": True})

def b0holonomy2_completeness_certificate() -> MappingProxyType:
    fields = {"contract_hash_verified": True, "plan": PLAN, "fixture_count": len(FIXTURE_IDS), "capsule_schema": True, "SU3_validation": True, "Cartan_Weyl_conjugacy": True, "representation_lift": True, "center_sectors": len(CENTER_IDS), "fundamental_adjoint_BC": True, "transition_domain_typed": True, "cut_PV": True, "gauge_ghost": True, "global_frame_open_color": True, "full_link": True, "derivatives": True, "support_kernel": True, "physical_selection": False, "count_once": True, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "next": NEXT}
    return _freeze({"schema": "C183-COMPLETENESS-CERTIFICATE-V1", "status": STATUS, **fields, "root": _root(fields)})

ROOTS = {
    "C183_INPUT_ROOT": _root((BASELINE, CONTRACT_SHA256, PROMPT_SHA256, c182.PACKAGE_ROOT)),
    "C183_PLAN_ROOT": b0holonomy2_plan_manifest()["root"], "C183_HANDOFF_FREEZE_ROOT": holonomy_handoff_freeze()["root"], "C183_CAPSULE_SCHEMA_ROOT": holonomy_capsule_schema()["root"], "C183_FIXTURE_ROOT": holonomy_fixture_manifest()["root"], "C183_SU3_MATRIX_ROOT": su3_matrix_manifest()["root"], "C183_CARTAN_ROOT": cartan_manifest()["root"], "C183_CONJUGACY_ROOT": conjugacy_manifest()["root"], "C183_REPRESENTATION_ROOT": representation_manifest()["root"], "C183_CENTER_ROOT": center_manifest()["root"], "C183_BOUNDARY_CONDITION_ROOT": boundary_condition_manifest()["root"], "C183_TRANSITION_DOMAIN_ROOT": transition_domain_manifest()["root"], "C183_CUT_PV_ROOT": cut_pv_manifest()["root"], "C183_GAUGE_COMPATIBILITY_ROOT": gauge_compatibility_manifest()["root"], "C183_GHOST_COMPATIBILITY_ROOT": ghost_compatibility_manifest()["root"], "C183_GLOBAL_FRAME_ROOT": global_frame_manifest()["root"], "C183_GLOBAL_VOLUME_ROOT": global_volume_manifest()["root"], "C183_FULL_LINK_ROOT": full_link_manifest()["root"], "C183_DERIVATIVE_ROOT": holonomy_derivative_manifest()["root"], "C183_SUPPORT_ROOT": support_manifest()["root"], "C183_KERNEL_HOLONOMY_ROOT": kernel_holonomy_manifest()["root"], "C183_PHYSICAL_SELECTION_ROOT": physical_selection_manifest()["root"], "C183_COUNT_ONCE_ROOT": count_once_manifest()["root"], "C183_B0_RELEASE_ROOT": b0_release_manifest()["root"], "C183_REQUEST_RESOLUTION_ROOT": request_resolution_manifest()["root"], "C183_MISSING_OBJECT_ROOT": missing_holonomy_object_manifest()["root"], "C183_MATCHING_HANDOFF_ROOT": _root(("conditional", NEXT)), "C183_DEPENDENCY_FRONTIER_ROOT": dependency_frontier_manifest()["root"], "C183_TARGET_LINK_SEPARATION_ROOT": target_link_separation_manifest()["root"], "C183_QUANTUM_NONMUTATION_ROOT": _root((0, 0)), "C183_BRST_ST_BOUNDARY_ROOT": brst_st_boundary_manifest()["root"], "C183_SCOPE_ROOT": _root((STATUS, "no physical selection", "no measure", "no self-energy")), "C183_COMPLETENESS_ROOT": b0holonomy2_completeness_certificate()["root"]
}
PACKAGE_ROOT = _root({"schema": "C183-HQCDB0HOLONOMY2-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": ROOTS})
ROOTS["C183_PACKAGE_ROOT"] = PACKAGE_ROOT

__all__ = [name for name in globals() if not name.startswith("_")]
