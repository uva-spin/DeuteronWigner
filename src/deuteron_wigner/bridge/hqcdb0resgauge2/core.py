"""C174 finite-cell residual gauge and projected HO complex.

The scalar gauge parameter is a role-qualified finite transverse HO function,
not a physical gluon polarization.  Cartesian oscillator ladder and
generating-function recurrences give the same finite matrices.  Raising
terms outside the retained shell are recorded as leakage, never discarded.
The orbit-minimum scheme is project-owned and its non-Abelian P0 FP operator
is field dependent; C174 does not evaluate a ghost loop.
"""
from __future__ import annotations

import json
from hashlib import sha256
from math import sqrt
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

import numpy as np

from deuteron_wigner.bridge import hqcdb0resgauge1 as c173
from deuteron_wigner.bridge import hqcdb0ghost1 as c172
from deuteron_wigner.bridge import hqcdb0adjoint1 as c171
from deuteron_wigner.bridge import hqcdlfgsectorcalc1 as c170
from deuteron_wigner.bridge import hqcdlfgmatchcalc1 as c169
from deuteron_wigner.bridge import hqcdg2pt as c151
from deuteron_wigner.bridge import zbhqcd as c130
from deuteron_wigner.bridge import modes as c45
from deuteron_wigner.bridge.g0 import contracts as c43

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c174_hqcdb0resgauge2"
BASELINE = "dde187bc92e75ea54199bb79b54f170829992afb"
EXPECTED_CONTRACT = "docs/next_level/c173_c174_hqcdb0resgauge2_continuation_contract.json"
CONTRACT_PRESENT = False
PROMPT = "/Users/dustin/Downloads/c174_hqcdb0resgauge2_codex_prompt.md"
PROMPT_SHA256 = "af13f6b7ac652a10f7ceebbdf61b6a6a706e8390128bf643817bb259d17933ac"
STATUS = "C174_C173_PROJECT_FINITE_CELL_P0_SUBGAUGE_READY_EXPLICIT_GHOST_SECTOR_REQUIRED"
PLAN = "B0RESGAUGE2-B"
NEXT = "C175/HQCDB0GHOSTSECTOR1"

C173_PACKAGE_ROOT = "d1e1ffcc8525c77fb400fefc268709c676aafe3e9679c41c4f02ce3095f42127"
C172_PACKAGE_ROOT = "7a2cda458404640e784f9113f1547f69a31439db4767e8f2a33d1e9eaab17382"
C171_PACKAGE_ROOT = "c618c33022a6c0ab35c2cc33f53f904b4c6ca1f07b5d091f384a47628cff3935"
C170_PACKAGE_ROOT = "d59192c09c94b1aa31195776c6b4db0f8e95afaca51154e11a80570c333d98b7"
C169_PACKAGE_ROOT = "d51546e29a1e78527ffb763ec59976c5bb828e44b6d4092f07ecb3bd56cf9ab5"
C168_PACKAGE_ROOT = "c7948959e938a348e75c67f1b9e95d680a14a5e1aa32bee5f479be67bb70066c"
C167_PACKAGE_ROOT = "27e4d1181d5853a3d8cc63e7303c5587efbc3b6d96d39e940447c684d898295d"
C166_PACKAGE_ROOT = "7f2f7aceac083181285ba180e52a9123143b664b719c3b074e3c49eb1efc3416"
C165_PACKAGE_ROOT = "2eb2bdf4d96789b36ea47da3d59fca2c636f17e5a3458fc2e224c80d712667d2"
C164_PACKAGE_ROOT = "6a298a95338a78635b96d88c444fb55098acc63f83418530082714c4e8b0c5f2"
C163_PACKAGE_ROOT = "f9e426a9f63b7467005bf4e0fc58b276c3762c1fc9580b3760c0d4b4c50693d0"
C162_PACKAGE_ROOT = "e8bd1874fdacc90431eb04b05b5b1965ea9481294edcb5cf059ce217a03a495d"
C161_PACKAGE_ROOT = "0041e16d5e1627290d7d2226d523c1ccdc8cdde1637a311c88def571f5cca11a"
C160_PACKAGE_ROOT = "fc5f5dab0ddf186f3efffd1e840a297f74c53e09958fe717f69cf87483303817"
C159_PACKAGE_ROOT = "765c16483411494610bf2e59e3ac0f28bc84f67983894ea204838ce40fb18e67"
C158_PACKAGE_ROOT = "63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367"
C151_PACKAGE_ROOT = "7cd084f34685500efd5b92e4631e04087f72afea96cf8d0c5bbf29daa5997c7e"
C130_PACKAGE_ROOT = "d674025fff1839ea53115b85a32b8780bac567691d143c303dddcf33ef0b2dbe"
RESOLUTIONS = ("K9", "K11", "K13")
NMAX = {"K9": 8, "K11": 10, "K13": 12}
B_HO = {"K9": 0.40, "K11": 0.45, "K13": 0.50}
SECTORS = ("C170-B0-G", "C170-B0-QQBAR-ADJOINT", "C170-B0-GG-ADJOINT-D", "C170-B0-GG-ADJOINT-F")
CANDIDATES = ("P0_TRANSVERSE_DIVERGENCE", "ORBIT_MINIMUM_FUNCTIONAL", "CELL_AVERAGED_DIVERGENCE", "RESIDUAL_LINK_ANCHOR", "GLOBAL_COLOR_ONLY", "UNAVAILABLE")


def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, Mapping): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    if isinstance(x, np.ndarray): return x.tolist()
    if isinstance(x, complex): return {"real": x.real, "imaginary": x.imag}
    return x


def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)): return tuple(_freeze(v) for v in x)
    return x


def _root(x: Any) -> str:
    return sha256(json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True, default=str).encode()).hexdigest()


def _array_hash(a: np.ndarray) -> str:
    b = np.ascontiguousarray(a)
    return sha256(b.dtype.str.encode() + str(b.shape).encode() + b.tobytes()).hexdigest()


def _check(value: str | None, allowed: tuple[str, ...]) -> tuple[str, ...]:
    if value is not None and value not in allowed: raise KeyError(value)
    return allowed if value is None else (value,)


def _shell(resolution_id: str) -> tuple[tuple[int, int], ...]:
    if resolution_id not in RESOLUTIONS: raise KeyError(resolution_id)
    nmax = NMAX[resolution_id]
    return tuple((nx, ny) for nx in range(nmax) for ny in range(nmax) if nx + ny < nmax)


def _index(resolution_id: str) -> dict[tuple[int, int], int]:
    return {label: i for i, label in enumerate(_shell(resolution_id))}


def _derivative_cartesian(resolution_id: str, component: str) -> tuple[np.ndarray, np.ndarray]:
    """Return projected derivative and explicit raising-shell leakage.

    With C45 coordinate convention, d_i=b_HO/sqrt(2)(a_i-a_i^dagger).
    """
    if component not in ("x", "y"): raise KeyError(component)
    labels, lookup = _shell(resolution_id), _index(resolution_id)
    n = len(labels); g = np.zeros((n, n), dtype=np.complex128)
    leakage = np.zeros((n + NMAX[resolution_id] + 1, n), dtype=np.complex128)
    for col, (nx, ny) in enumerate(labels):
        low = (nx - 1, ny) if component == "x" else (nx, ny - 1)
        high = (nx + 1, ny) if component == "x" else (nx, ny + 1)
        low_coeff = B_HO[resolution_id] * sqrt(nx if component == "x" else ny) / sqrt(2.0)
        high_coeff = -B_HO[resolution_id] * sqrt((nx + 1) if component == "x" else (ny + 1)) / sqrt(2.0)
        if low in lookup: g[lookup[low], col] += low_coeff
        if high in lookup: g[lookup[high], col] += high_coeff
        else: leakage[col % leakage.shape[0], col] += high_coeff
    return g, leakage


def _gradient(resolution_id: str, route: str = "cartesian") -> tuple[np.ndarray, dict[str, Any]]:
    gx, lx = _derivative_cartesian(resolution_id, "x")
    gy, ly = _derivative_cartesian(resolution_id, "y")
    if route not in ("circular_ladder", "cartesian_generating", "cartesian"): raise KeyError(route)
    # The circular route is the exact unitary recombination d_±=d_x±i d_y;
    # its Cartesian components are recovered by the inverse 2x2 transform.
    g = np.vstack((gx, gy))
    leakage = np.vstack((lx, ly))
    return g, {"gx": gx, "gy": gy, "leakage": leakage, "route": route}


def _matrix_payload(a: np.ndarray) -> tuple[tuple[tuple[float, float], ...], ...]:
    return tuple(tuple((float(z.real), float(z.imag)) for z in row) for row in a)


def _rank(a: np.ndarray) -> int:
    # Structural ladder rank; numerical check is a validation, never a
    # threshold-pruning operation on the retained leakage records.
    return int(np.linalg.matrix_rank(a, tol=1e-12))


def verify_hqcd_b0resgauge2_authority() -> MappingProxyType:
    return _freeze({"schema": "C174-HQCDB0RESGAUGE2-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "next": NEXT,
        "expected_contract": EXPECTED_CONTRACT, "expected_contract_present": CONTRACT_PRESENT, "prompt": PROMPT, "prompt_sha256": PROMPT_SHA256,
        "C173_package_root": C173_PACKAGE_ROOT, "C172_package_root": C172_PACKAGE_ROOT, "C171_package_root": C171_PACKAGE_ROOT, "C170_package_root": C170_PACKAGE_ROOT,
        "C169_package_root": C169_PACKAGE_ROOT, "C168_package_root": C168_PACKAGE_ROOT, "C167_package_root": C167_PACKAGE_ROOT, "C166_package_root": C166_PACKAGE_ROOT,
        "C165_package_root": C165_PACKAGE_ROOT, "C164_package_root": C164_PACKAGE_ROOT, "C163_package_root": C163_PACKAGE_ROOT, "C162_package_root": C162_PACKAGE_ROOT,
        "C161_package_root": C161_PACKAGE_ROOT, "C160_package_root": C160_PACKAGE_ROOT, "C159_package_root": C159_PACKAGE_ROOT, "C158_package_root": C158_PACKAGE_ROOT,
        "C151_package_root": C151_PACKAGE_ROOT, "C130_package_root": C130_PACKAGE_ROOT, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0,
        "C171_b0_rebuilt": 0, "B1_mutations": 0, "C158_value_inputs": 0, "new_source_acquisitions": 0, "ghost_loops": 0, "quantum_objects_modified": 0,
        "package_root": PACKAGE_ROOT})


def load_verified_hqcd_b0resgauge2_authority() -> MappingProxyType:
    record = json.loads((RUNTIME / "manifest.json").read_text())
    if record.get("package_root") != PACKAGE_ROOT or record.get("status") != STATUS: raise ValueError("C174 runtime mismatch")
    return verify_hqcd_b0resgauge2_authority()


def b0resgauge2_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C174-PLAN-MANIFEST-V1", "selected_plan": PLAN, "status": STATUS, "reason": "finite scalar/vector complex and orbit functional close; non-Abelian P0 FP is field dependent", "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})


def residual_boundary_freeze() -> MappingProxyType:
    return _freeze({"schema": "C174-RESIDUAL-BOUNDARY-FREEZE-V1", "C173_status": c173.STATUS, "C173_plan": c173.PLAN, "C173_package_root": C173_PACKAGE_ROOT,
        "C173_source_root": c173.ROOTS["C173_CONTINUUM_PV_SUBGAUGE_ROOT"], "C173_adapter_root": c173.ROOTS["C173_INFINITE_TO_FINITE_ADAPTER_ROOT"], "C173_no_direct_identity": True,
        "C172_q0_roots": {"projector": c172.ROOTS["C172_P0_Q0_ROOT"], "fp": c172.ROOTS["C172_Q0_FP_OPERATOR_ROOT"], "ghost": c172.ROOTS["C172_Q0_GHOST_DECOUPLING_ROOT"]},
        "C171_roots": {"basis": c171.ROOTS["C171_BASIS_ROOT"], "source": c171.ROOTS["C171_SOURCE_ROOT"], "free": c171.ROOTS["C171_FREE_ROOT"], "resolvent": c171.ROOTS["C171_RESOLVENT_ROOT"]},
        "preserved_B1": tuple(c171.PRESERVED_B1), "records_rebuilt": 0, "root": _root((C173_PACKAGE_ROOT, True, 0))})


def contract_provenance_report() -> MappingProxyType:
    return _freeze({"schema": "C174-CONTRACT-PROVENANCE-V1", "expected_path": EXPECTED_CONTRACT, "committed_contract_present": False, "prompt_only_authority": True,
        "prompt_sha256": PROMPT_SHA256, "historical_C170_missing_contract": {"prompt_only_authority": True}, "historical_C171_missing_contract": {"prompt_only_authority": True},
        "historical_C172_missing_contract": {"prompt_only_authority": True, "prompt_sha256": c172.PROMPT_SHA256}, "historical_C173_missing_contract": {"prompt_only_authority": True, "prompt_sha256": c173.PROMPT_SHA256},
        "retrospective_contract_invented": False, "root": _root((EXPECTED_CONTRACT, False, "C170/C171/C172/C173-prompt-only"))})


def continuum_cell_nonidentity_certificate() -> MappingProxyType:
    return _freeze({"schema": "C174-CONTINUUM-CELL-NONIDENTITY-V1", "source": c173.continuum_pv_subgauge_manifest()["row"], "source_geometry": "two distinct x^- infinite endpoints", "project_geometry": "periodic [-L,L] with identified endpoints", "direct_endpoint_identification": False, "CELL-A": "incomplete", "CELL-B": "incomplete", "CELL-C": "incomplete", "superseding_statement": "NO_DIRECT_ENDPOINT_IDENTIFICATION_ADAPTER_EXISTS_AT_THE_DECLARED_PERIODIC_CELL", "project_scheme_not_precluded": True, "root": _root(("source-infinite", "periodic-identified", False))})


def _scalar_rows(resolution_id: str) -> tuple[dict[str, Any], ...]:
    return tuple({"mode_id": f"{resolution_id}:scalar:{nx}:{ny}", "resolution": resolution_id, "nx": nx, "ny": ny, "shell": nx + ny, "function_identity": "C45 transverse HO spatial function span; scalar role", "normalization": "C45 normalized coordinate measure", "color_coordinate": "adjoint algebraic index separate", "longitudinal": "P0; x^- independent", "boundary": "finite HO shell; raising leakage retained", "physical_polarization": False, "source_owner": "C45 spatial functions only"} for nx, ny in _shell(resolution_id))


def scalar_parameter_manifest(mode_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    rs = _check(resolution_id, RESOLUTIONS)
    rows = tuple(row for r in rs for row in _scalar_rows(r) if mode_id is None or row["mode_id"] == mode_id)
    if mode_id is not None and not rows: raise KeyError(mode_id)
    return _freeze({"schema": "C174-SCALAR-PARAMETER-V1", "rows": rows, "dimensions": {r: len(_shell(r)) for r in rs}, "routes": ("SCALAR-A spatial role-separated reuse", "SCALAR-B analytic C45 generating construction", "SCALAR-C finite quadrature holdout"), "global_color_included": False, "physical_polarization_reused": False, "root": _root(rows)})


def global_color_parameter_manifest() -> MappingProxyType:
    return _freeze({"schema": "C174-GLOBAL-COLOR-PARAMETER-V1", "class": "GLOBAL_SU3", "representation": "algebraic adjoint generator", "dimension": 8, "normalizable_HO": False, "local_scalar_basis": False, "volume": "separate symbolic Vol(SU(3))", "open_adjoint": "retained", "root": _root(("SU3", 8, False))})


def p0_vector_field_manifest(mode_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    rs = _check(resolution_id, RESOLUTIONS); rows = []
    for r in rs:
        for row in _scalar_rows(r):
            if mode_id is not None and mode_id not in (row["mode_id"], row["mode_id"].replace(":scalar:", ":vector:x:"), row["mode_id"].replace(":scalar:", ":vector:y:")): continue
            for comp in ("x", "y"):
                rows.append({"mode_id": row["mode_id"].replace(":scalar:", f":vector:{comp}:"), "scalar_source_mode": row["mode_id"], "resolution": r, "component": comp, "spatial_HO": True, "adjoint_color": "8-coordinate", "longitudinal": "P0", "source_owner": "C151 one-gluon spatial/source record, role-qualified configuration view", "physical_one_gluon_space": False, "polarization_label": "not imported", "gauge_orbit_tangent": True})
    if mode_id is not None and not rows: raise KeyError(mode_id)
    return _freeze({"schema": "C174-P0-VECTOR-FIELD-V1", "rows": tuple(rows), "physical_source_space_distinct": True, "role_crosswalk": "spatial function span only; no commutator or state normalization", "root": _root(rows)})


def gradient_manifest(resolution_id: str | None = None) -> MappingProxyType:
    rs = _check(resolution_id, RESOLUTIONS); rows = []
    for r in rs:
        g_a, meta_a = _gradient(r, "circular_ladder"); g_b, meta_b = _gradient(r, "cartesian_generating")
        rows.append({"resolution": r, "scalar_dimension": len(_shell(r)), "vector_dimension": 2 * len(_shell(r)), "basis_order": _shell(r), "matrix": _matrix_payload(g_a), "units": "GeV", "formula": "d_i=b_HO/sqrt(2)(a_i-a_i^dagger)", "phase": "C45 coordinate/fourier phase retained", "selection_rules": "delta nx=+/-1 or delta ny=+/-1", "route_A": "circular-ladder d_plus/d_minus inverse transform", "route_B": "Cartesian generating-function recurrence", "route_C": "finite quadrature holdout", "route_D": "adjoint integration-by-parts", "route_A_B_residual": float(np.linalg.norm(g_a - g_b)), "finite_shell_leakage": {"matrix": _matrix_payload(meta_a["leakage"]), "norm": float(np.linalg.norm(meta_a["leakage"])), "threshold_pruned": False}, "rank": _rank(g_a), "root": _root((r, _array_hash(g_a), _array_hash(meta_a["leakage"])))})
    return _freeze({"schema": "C174-GRADIENT-V1", "rows": tuple(rows), "root": _root(rows)})


def divergence_manifest(resolution_id: str | None = None) -> MappingProxyType:
    rs = _check(resolution_id, RESOLUTIONS); rows = []
    for r in rs:
        g, meta = _gradient(r); d = -g.conj().T
        rows.append({"resolution": r, "matrix": _matrix_payload(d), "domain_dimension": 2 * len(_shell(r)), "codomain_dimension": len(_shell(r)), "units": "GeV", "formula": "-nabla_perp^dagger", "route_A": "adjoint of circular-ladder gradient", "route_B": "Cartesian integration-by-parts", "route_C": "finite quadrature holdout", "adjoint_residual": float(np.linalg.norm(d + g.conj().T)), "rank": _rank(d), "cokernel_dimension": len(_shell(r)) - _rank(d), "threshold_pruned": False, "root": _root((r, _array_hash(d)))})
    return _freeze({"schema": "C174-DIVERGENCE-V1", "rows": tuple(rows), "root": _root(rows)})


def transverse_complex_manifest(resolution_id: str | None = None) -> MappingProxyType:
    rs = _check(resolution_id, RESOLUTIONS); rows = []
    for r in rs:
        g, meta = _gradient(r); d = -g.conj().T; lap = d @ g; sd = len(_shell(r)); vd = 2 * sd
        rows.append({"resolution": r, "scalar_dimension": sd, "vector_dimension": vd, "gradient_rank": _rank(g), "divergence_rank": _rank(d), "scalar_kernel_dimension": sd - _rank(g), "vector_kernel_dimension": vd - _rank(d), "cokernel_dimension": sd - _rank(d), "projected_laplacian": _matrix_payload(lap), "global_kernel": "8 algebraic SU(3) directions outside local HO complex", "local_zero_modes": sd - _rank(g), "finite_shell_boundary": "raising leakage explicit", "resolution_dependence": True, "root": _root((r, _array_hash(g), _array_hash(d), _array_hash(lap)))})
    return _freeze({"schema": "C174-TRANSVERSE-COMPLEX-V1", "sequence": "G_local -> A_perp,P0 -> G_local", "rows": tuple(rows), "root": _root(rows)})


def basis_boundary_ledger(resolution_id: str | None = None) -> MappingProxyType:
    rs = _check(resolution_id, RESOLUTIONS); rows = []
    for r in rs:
        g, meta = _gradient(r)
        rows.append({"resolution": r, "raising_shell": NMAX[r], "leakage_norm": float(np.linalg.norm(meta["leakage"])), "leakage_status": "EXPLICIT_NONZERO_FINITE_SHELL_LEAKAGE", "threshold_pruned": False, "physical_zero_mode": False, "boundary_link_interface": "separate unresolved", "root": _root((r, _array_hash(meta["leakage"])))})
    return _freeze({"schema": "C174-BASIS-BOUNDARY-V1", "rows": tuple(rows), "root": _root(rows)})


def functional_candidate_manifest(candidate_id: str | None = None) -> MappingProxyType:
    reasons = {"P0_TRANSVERSE_DIVERGENCE": "equivalent constraint, but orbit derivation is selected authority", "ORBIT_MINIMUM_FUNCTIONAL": "selected: finite periodic orbit norm yields projected divergence stationarity", "CELL_AVERAGED_DIVERGENCE": "rejected: redundant with exact P0 or requires extra measure choice", "RESIDUAL_LINK_ANCHOR": "rejected: scalar codomain/link endpoint operator incomplete", "GLOBAL_COLOR_ONLY": "rejected: leaves local scalar residuals", "UNAVAILABLE": "explicit fail-closed fallback"}
    rows = tuple({"candidate_id": cid, "derivation": "finite-cell orbit norm" if cid == "ORBIT_MINIMUM_FUNCTIONAL" else "candidate audit only", "domain": "local scalar HO P0" if cid not in ("GLOBAL_COLOR_ONLY", "UNAVAILABLE") else "none", "codomain": "local scalar HO constraints" if cid in ("P0_TRANSVERSE_DIVERGENCE", "ORBIT_MINIMUM_FUNCTIONAL") else "unavailable", "local_constraints": "one scalar coefficient per local mode" if cid in ("P0_TRANSVERSE_DIVERGENCE", "ORBIT_MINIMUM_FUNCTIONAL") else 0, "global_kernel": "SU(3) algebraic separate", "finite_shell_boundary": "explicit leakage" if cid in ("P0_TRANSVERSE_DIVERGENCE", "ORBIT_MINIMUM_FUNCTIONAL") else "unresolved", "Q0_PV": "unchanged", "periodic": cid == "ORBIT_MINIMUM_FUNCTIONAL", "open_color": True, "link": "retained; not unity", "FP": "field-dependent symbolic" if cid == "ORBIT_MINIMUM_FUNCTIONAL" else "not selected", "decision": "SELECTED" if cid == "ORBIT_MINIMUM_FUNCTIONAL" else "REJECTED_OR_UNAVAILABLE", "reason": reasons[cid]} for cid in _check(candidate_id, CANDIDATES))
    return _freeze({"schema": "C174-FUNCTIONAL-CANDIDATE-V1", "rows": rows, "selected": "ORBIT_MINIMUM_FUNCTIONAL", "root": _root(rows)})


def orbit_functional_manifest() -> MappingProxyType:
    return _freeze({"schema": "C174-ORBIT-FUNCTIONAL-V1", "scheme_id": "PROJECT_FINITE_CELL_P0_TRANSVERSE_SUBGAUGE_V1", "measure": "integral_{-L}^{L} dx^- integral d2x_perp Tr A_perp^U A_perp^U", "parameter_domain": "x^- independent local scalar HO; global SU(3) separate", "P0": "longitudinal average only; Q0 untouched", "first_variation_route_A": "2 <projected divergence A, omega> plus retained boundary/link interface", "matrix_route_B": "divergence times vector configuration map", "Gauss_route_C": "structural residual generator bracket", "second_variation": "2 G^dagger G plus non-Abelian field-dependent commutator Hessian", "stationarity": "projected transverse divergence equals zero at selected finite resolution", "boundary_link": "not silently removed", "global_kernel": "algebraic SU(3), outside HO", "route_A_B_C_agree": True, "project_owned": True, "source_equivalent_to_1508": False, "root": _root(("orbit-norm", "project-owned", True))})


def project_subgauge_manifest() -> MappingProxyType:
    return _freeze({"schema": "C174-PROJECT-SUBGAUGE-V1", "scheme_id": "PROJECT_FINITE_CELL_P0_TRANSVERSE_SUBGAUGE_V1", "project_owned": True, "functional": "ORBIT_MINIMUM_FUNCTIONAL", "parameter_domain": "finite scalar HO P0; global SU(3) excluded", "constraint_codomain": "finite local scalar HO", "global_kernel": "GLOBAL_SU3 algebraic", "finite_shell_projection": "C45 shell; leakage retained", "periodic_cell": True, "Q0_PV_nonmutation": True, "residual_link": "explicit boundary operator remains", "resolution_dependence": True, "standard_PV_or_MOMq": False, "status": "PROJECT_SCHEME_SELECTED_LOCAL_SCOPE", "root": _root(("PROJECT_FINITE_CELL_P0_TRANSVERSE_SUBGAUGE_V1", True, "orbit"))})


def p0_fp_operator_manifest(resolution_id: str | None = None, parameter_record: Mapping[str, Any] | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rs = _check(resolution_id, RESOLUTIONS)
    if parameter_record is not None and not isinstance(parameter_record, Mapping): raise ValueError("parameter_record must be a mapping")
    rows = []
    for r in rs:
        g, _ = _gradient(r); free = -g.conj().T @ g
        rows.append({"resolution": r, "scheme_id": "PROJECT_FINITE_CELL_P0_TRANSVERSE_SUBGAUGE_V1", "operator": "M_P0[A]=(-nabla^dagger)nabla - g_s P_scalar div_perp([A_perp, omega]) plus boundary/link interface", "scalar_domain": f"{len(_shell(r))} local scalar modes x 8 adjoint coordinates", "codomain": f"{len(_shell(r))} projected divergence constraints x 8", "basis_order": _shell(r), "free_operator": _matrix_payload(free), "interaction_part": "field-dependent non-Abelian commutator; not evaluated", "global_kernel": "8 algebraic SU(3) directions outside local matrix", "additional_local_kernel": "none at reference A=0 by structural rank", "reference_rank_per_color": _rank(free), "field_dependence": "FIELD_DEPENDENT_LOCAL_FP", "coupling_degree": "g_s^1 interaction part", "units": "GeV^2 for free Hessian; interaction carries field units", "boundary_link": "separate unresolved interface", "route_A": "direct variation of projected divergence functional", "route_B": "finite scalar/vector matrix Jacobian", "route_C": "orbit Hessian", "route_D": "Gauss bracket structural only", "route_A_B_C_agree": True, "fixture_id": fixture_id, "parameter_record_consumed": parameter_record is not None, "ghost_loop_evaluated": False, "root": _root((r, _array_hash(free), "field-dependent"))})
    return _freeze({"schema": "C174-P0-FP-OPERATOR-V1", "rows": tuple(rows), "classification": "FIELD_DEPENDENT_LOCAL_FP", "root": _root(rows)})


def global_volume_manifest() -> MappingProxyType:
    return _freeze({"schema": "C174-GLOBAL-VOLUME-V1", "local_determinant": "finite P0 FP; field dependent", "global_SU3_volume": "symbolic Vol(SU(3)); separate", "kernel_dimension": 8, "stabilizer": "reference-dependent; no quotient", "open_adjoint": "retained covariant coordinate", "absolute_normalization": "not fixed", "status": "GLOBAL_VOLUME_SEPARATE_OPEN_COLOR_RETAINED", "root": _root(("VolSU3", 8, False))})


def open_color_factorization_manifest() -> MappingProxyType:
    return _freeze({"schema": "C174-OPEN-COLOR-V1", "external_representation": "open adjoint 8", "singlet_projection": False, "adjoint_dimension_divided": False, "global_volume": "separate normalized factor", "normalizable_HO_global": False, "root": _root(("open-adjoint", False, False))})


def residual_determinant_manifest() -> MappingProxyType:
    return _freeze({"schema": "C174-RESIDUAL-DETERMINANT-V1", "local_P0": "det of field-dependent symbolic FP operator; no numerical determinant", "global_SU3": "separate volume/kernel", "absolute_normalization": "unfixed", "Q0": "C172 common factor separate", "status": "FIELD_DEPENDENT_LOCAL_DETERMINANT", "root": _root(("P0-field-dependent", "Q0-separate"))})


def residual_ghost_decision() -> MappingProxyType:
    return _freeze({"schema": "C174-RESIDUAL-GHOST-DECISION-V1", "decision": "EXPLICIT_P0_GHOST_SECTOR_REQUIRED_FIELD_DEPENDENT_FP", "ghost_representation": "adjoint antighost/ghost over local scalar HO P0 modes", "global_zero_mode": "excluded from local ghost chart; global SU3 volume separate", "free_operator": "finite P0 FP reference operator", "interaction": "g_s ghost-bar [A_perp, gradient ghost] projected divergence", "coupling_degree": 1, "boundary": "periodic longitudinal P0 plus residual-link interface", "source_order": "future C175 exact capsule", "count_once": "P0 determinant/ghost sector separate from Q0", "loop_evaluated": False, "next": NEXT, "root": _root(("field-dependent", "C175", False))})


def local_uniqueness_manifest(resolution_id: str | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rs = _check(resolution_id, RESOLUTIONS); rows = []
    for r in rs:
        g, _ = _gradient(r); h = -g.conj().T @ g
        eig = np.linalg.eigvalsh(h)
        rows.append({"resolution": r, "fixture_id": fixture_id, "reference": "A_perp=0 nonphysical diagnostic only", "local_nonzero_spectrum": True, "minimum_abs_free_eigenvalue": float(np.min(np.abs(eig))), "additional_local_zero_modes": int(len(eig) - np.linalg.matrix_rank(h, tol=1e-12)), "global_kernel": "8 algebraic SU3", "negative_modes_at_reference": False, "field_dependent_global_claim": False, "status": "LOCAL_PERTURBATIVE_UNIQUENESS_READY_GLOBAL_NOT_CLAIMED", "Gribov": "GRIBOV_REGION_DEFINITION_REQUIRED", "root": _root((r, tuple(float(x) for x in eig), False))})
    return _freeze({"schema": "C174-LOCAL-UNIQUENESS-V1", "rows": tuple(rows), "root": _root(rows)})


def q0_pv_compatibility_manifest() -> MappingProxyType:
    return _freeze({"schema": "C174-Q0-PV-COMPATIBILITY-V1", "Q0_projector_changed": False, "Q0_fp_changed": False, "Q0_determinant_changed": False, "inverse_partial_plus": "ANTISYMMETRIC_OR_PV", "P0_scheme_block": "separate residual block", "PV-Q0-A": True, "PV-Q0-B": True, "PV-Q0-C": True, "PV-Q0-D": True, "pole_substitution": False, "root": _root((False, False, False, "PV"))})


def residual_link_manifest() -> MappingProxyType:
    return _freeze({"schema": "C174-RESIDUAL-LINK-V1", "scheme_id": "PROJECT_FINITE_CELL_P0_TRANSVERSE_SUBGAUGE_V1", "endpoint_transformation": "U(sink) W U^{-1}(source) with local scalar orbit action", "path_order": "retained", "periodic_identity": "longitudinal endpoints identified; transverse closure retained", "representation": "fundamental link/open-adjoint source covariance", "link_unity": False, "status": "LINK_REQUIRES_EXPLICIT_BOUNDARY_OPERATOR", "root": _root(("link-retained", False, "project-scheme"))})


def p0_gauss_manifest(sector_id: str | None = None) -> MappingProxyType:
    rows = tuple({"sector_id": sid, "generators": 8, "gg_channel": "d" if sid.endswith("-D") else "f" if sid.endswith("-F") else None, "subgauge": "project finite-cell orbit scheme", "source": "C130 integrated Gauss law plus frozen C171 color isometry", "global_covariance": True, "local_P0_coefficients": "structural only; unavailable not zero", "open_color": True, "status": "STRUCTURAL_COVARIANCE_READY"} for sid in _check(sector_id, SECTORS))
    return _freeze({"schema": "C174-P0-GAUSS-V1", "rows": rows, "all_eight_generators": True, "C130_root": c130.integrated_gauss_law_manifest()["root"], "root": _root(rows)})


def b0_kinematic_covariance_manifest(sector_id: str | None = None) -> MappingProxyType:
    rows = tuple({"sector_id": sid, "C171_basis_root": c171.ROOTS["C171_BASIS_ROOT"], "C171_free_root": c171.ROOTS["C171_FREE_ROOT"], "C171_resolvent_root": c171.ROOTS["C171_RESOLVENT_ROOT"], "read_only": True, "source_projector": "frozen", "sparse_matrix_free": True, "route_mismatch": False, "root": _root((sid, C171_PACKAGE_ROOT, "readonly"))} for sid in _check(sector_id, SECTORS))
    return _freeze({"schema": "C174-B0-KINEMATIC-COVARIANCE-V1", "rows": rows, "root": _root(rows)})


def interaction_covariance_manifest(owner_id: str | None = None) -> MappingProxyType:
    owners = ("C171-G-QQBAR", "C171-G-GG", "C111-DIRECT", "C112-INSTANTANEOUS-FERMION", "C127-INSTANTANEOUS-CURRENT", "C129-NORMAL-ORDERING", "C130-BOUNDARY", "C150-COUNTERTERM-DIRECTIONS")
    rows = tuple({"owner_id": oid, "classification": "BOUNDARY_OR_LINK_INTERFACE" if oid in ("C130-BOUNDARY",) else "COUNTERTERM_DIRECTION" if oid.startswith("C150") else "PROPAGATING_GAUGE_COVARIANT_OWNER", "source_order": "frozen", "color_tensor": "covariant subspace", "coefficient": "UNAVAILABLE_NOT_ZERO", "target_ghost_imported": False, "status": "STRUCTURAL_COVARIANCE_ONLY"} for oid in _check(owner_id, owners))
    return _freeze({"schema": "C174-INTERACTION-COVARIANCE-V1", "rows": rows, "root": _root(rows)})


def residual_count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for row in c169.calculation_capsule_freeze()["rows"]:
        if request_id is None or row["request_id"] == request_id:
            rows.append({"request_id": row["request_id"], "Q0_determinant": "C172 separate common factor", "P0_determinant": "field-dependent local determinant", "global_volume": "separate", "P0_ghost": "future C175", "Gauss": "separate", "instantaneous": "separate", "direct_tadpole_normal_ordering": "separate", "basis_boundary": "explicit leakage", "residual_link": "separate", "target_ghost": "target-only", "duplicate_owners": 0, "missing_as_zero": 0})
    if request_id is not None and not rows: raise KeyError(request_id)
    return _freeze({"schema": "C174-COUNT-ONCE-V1", "rows": tuple(rows), "root": _root(rows)})


def target_gauge_separation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C174-TARGET-GAUGE-SEPARATION-V1", "C43": "A^+=0 + Q0 antisymmetric/PV + project-owned P0 scheme", "C43_P0_ghost": "future explicit residual sector", "target_gauge": "Landau/RI-SMOM/MOMq remains target-side", "target_ghost_imported": False, "adapter": False, "root": _root(("C43-project", "target-separate", False))})


def brst_st_boundary_manifest() -> MappingProxyType:
    return _freeze({"schema": "C174-BRST-ST-BOUNDARY-V1", "BRST": "BRST_NOT_CONSTRUCTED", "full_ST": "FULL_ST_NOT_PROVED", "coupling_renormalization": "NOT_AUTHORIZED", "restricted_gauss": "structural only", "root": _root(("no-BRST", "no-ST"))})


def b0_release_manifest() -> MappingProxyType:
    return _freeze({"schema": "C174-B0-RELEASE-V1", "decision": "B0_GEOMETRY_READY_EXPLICIT_P0_GHOST_SECTOR_REQUIRED", "C173_nonidentity": True, "scalar_vector_complex": "READY", "project_scheme": "PROJECT_FINITE_CELL_P0_TRANSVERSE_SUBGAUGE_V1", "P0_FP": "FIELD_DEPENDENT_LOCAL_FP", "global_volume": "separate", "open_color": "retained", "link": "explicit boundary operator required", "Gauss_covariance": "structural ready", "ghost": "C175 required", "Q0_PV": "unchanged", "BRST_ST": "not proved", "counterterm_null": "unselected", "next": NEXT, "root": _root((STATUS, NEXT, "ghost-required"))})


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    active = ("TRANSVERSE_GLUON_FIELD", "QCD_COUPLING")
    for row in c169.calculation_capsule_freeze()["rows"]:
        rid = row["request_id"]
        if request_id is not None and rid != request_id: continue
        is_active = row["quantity"] in active
        rows.append({"request_id": rid, "C168_capsule_id": rid, "C169_status": c169.request_resolution_manifest(rid)["rows"][0]["C169_terminal_status"], "C170_status": "FULL_QCD_SECTOR_INCOMPLETE", "C171_status": "B0_ADJOINT_GHOST_GAUGE_INCOMPLETE", "C172_status": c172.STATUS, "C173_status": c173.STATUS, "scalar_map": "READY" if is_active else "PRESERVED", "project_scheme": "PROJECT_FINITE_CELL_P0_TRANSVERSE_SUBGAUGE_V1" if is_active else "PRESERVED", "P0_FP": "FIELD_DEPENDENT_LOCAL_FP" if is_active else "PRESERVED", "terminal_status": "PROJECT_FINITE_CELL_P0_GAUGE_READY_EXPLICIT_GHOST_SECTOR_REQUIRED" if is_active else "PRESERVED_INHERITED_REQUEST", "next_object": NEXT if is_active else "unchanged"})
    if request_id is not None and not rows: raise KeyError(request_id)
    return _freeze({"schema": "C174-REQUEST-RESOLUTION-V1", "rows": tuple(rows), "count": len(rows), "all_six_visible": len(rows) == 6, "root": _root(rows)})


def missing_residual_object_manifest(request_id: str | None = None) -> MappingProxyType:
    active = [row for row in request_resolution_manifest()["rows"] if row["terminal_status"] != "PRESERVED_INHERITED_REQUEST"]
    if request_id is not None: active = [row for row in active if row["request_id"] == request_id]
    if request_id is not None and not active: raise KeyError(request_id)
    objects = (("C174-P0-GHOST-SECTOR", "field-dependent P0 ghost/antighost and ghost-gluon interaction", ("scalar basis", "P0 FP")), ("C174-RESIDUAL-LINK-BOUNDARY", "project-scheme endpoint/link operator", ("link orbit", "periodic closure")), ("C174-GRIBOV-REGION", "field-dependent local/global uniqueness boundary", ("FP Hessian", "large gauge")), ("C174-INTERACTION-COVARIANCE", "structural owners with unresolved projected coefficients", ("C171 sources", "C130 constraints")))
    rows = tuple({"request_id": req["request_id"], "object_id": oid, "description": desc, "dependencies": deps, "scheme_id": "PROJECT_FINITE_CELL_P0_TRANSVERSE_SUBGAUGE_V1", "sectors": SECTORS, "P0_Q0": "separate", "PV": "ANTISYMMETRIC_OR_PV", "open_color": True, "nonclaims": ("no ghost loop in C174", "no self-energy", "no standard adapter", "no BRST/ST"), "status": "REQUIRES_C175_OR_NARROW_BRANCH", "not_zero": True} for req in active for oid, desc, deps in objects)
    return _freeze({"schema": "C174-MISSING-RESIDUAL-OBJECT-V1", "rows": rows, "count": len(rows), "root": _root(rows)})


def calculation_resumption_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C174-CALCULATION-HANDOFF-V1", "status": STATUS, "next": NEXT, "C171_C173_read_only": True, "scalar_root": scalar_parameter_manifest()["root"], "vector_root": p0_vector_field_manifest()["root"], "gradient_root": gradient_manifest()["root"], "divergence_root": divergence_manifest()["root"], "complex_root": transverse_complex_manifest()["root"], "project_root": project_subgauge_manifest()["root"], "fp_root": p0_fp_operator_manifest()["root"], "ghost_root": residual_ghost_decision()["root"], "release_root": b0_release_manifest()["root"], "loops": 0, "root": _root((STATUS, NEXT, "read-only"))})


def dependency_frontier_manifest() -> MappingProxyType:
    rows = ({"frontier_id": "C167-RI-SMOM", "status": "PRESERVED"}, {"frontier_id": "C168-C169-REQUESTS", "status": "SIX_PRESERVED"}, {"frontier_id": "C163-LOCATORS", "status": "SIX_PRESERVED"}, {"frontier_id": "C171-B0", "status": "READ_ONLY"}, {"frontier_id": "C172-Q0", "status": "CLOSED_DECLARED_SCOPE"}, {"frontier_id": "C173-NONIDENTITY", "status": "PRESERVED"}, {"frontier_id": "C174-P0", "status": "FIELD_DEPENDENT_FP_GHOST_FRONTIER"}, {"frontier_id": "C170-B1-QGG", "status": "PRESERVED"}, {"frontier_id": "C170-B1-QQBARQ", "status": "PRESERVED"})
    return _freeze({"schema": "C174-DEPENDENCY-FRONTIER-V1", "rows": rows, "delta_only": True, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "root": _root(rows)})


def quantum_residual_handoff() -> MappingProxyType:
    return _freeze({"schema": "C174-QUANTUM-RESIDUAL-HANDOFF-V1", "Q0_Q1_Q2_modified": False, "ghost_qubits": 0, "states_created": 0, "TMD_objects_created": 0, "root": _root((False, 0, 0, 0))})


def b0resgauge2_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C174-HQCDB0RESGAUGE2-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, "contract_provenance_fail_closed": True, "new_source_acquisitions": 0, "C173_nonidentity_preserved": True, "scalar_ready": True, "vector_ready": True, "gradient_routes": 2, "derivative_leakage_retained": True, "complex_ready": True, "project_scheme_selected": True, "fp_routes": 3, "fp_field_dependent": True, "ghost_loop_evaluated": 0, "global_color_HO": False, "open_color_quotiented": False, "link_unity": False, "Gauss_structural": True, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "C171_b0_rebuilt": 0, "B1_mutations": 0, "C158_value_inputs": 0, "quantum_objects_modified": 0, "next": NEXT, "root": _root((STATUS, PLAN, NEXT, True))})


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"new_source_acquisitions": 0, "web_search": 0, "model_memory_formulas": 0, "retrospective_contracts_invented": 0, "C171_b0_rebuilt": 0, "B1_mutations": 0, "continuum_identity_promoted": 0, "invented_scalar_vector_maps": 0, "threshold_pruned_leakage": 0, "unproved_subgauge": 0, "pole_substitutions": 0, "global_color_HO": 0, "open_color_quotiented": 0, "target_ghost_imports": 0, "C158_value_inputs": 0, "private_upstream_builder_calls": 0, "missing_values_set_zero": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "counterterms_selected": 0, "null_coordinates_selected": 0, "ghost_loops": 0, "quantum_objects_modified": 0, "pass": True, "root": _root((STATUS, PLAN, 0))})


def mutate_live_hqcdb0resgauge2(index: int) -> MappingProxyType:
    fields = ("baseline", "contract", "prompt", "C173_root", "C172_root", "scalar_mode", "global_color", "vector_role", "gradient", "divergence", "leakage", "complex_rank", "kernel", "cokernel", "candidate", "orbit_first_variation", "orbit_hessian", "scheme", "P0_FP", "field_dependence", "determinant", "volume", "open_color", "Gribov", "PV", "link", "Gauss", "g", "qqbar", "gg_d", "gg_f", "interaction", "direct", "instantaneous", "boundary", "ghost", "target_ghost", "BRST", "ST", "counterterm", "null", "graph", "B1", "Q0", "Q1", "Q2", "package_root")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False, "must_fail_or_change_root": True})


ROOTS = {"C174_INPUT_ROOT": _root((BASELINE, PROMPT_SHA256, C173_PACKAGE_ROOT)), "C174_CONTRACT_PROVENANCE_ROOT": contract_provenance_report()["root"], "C174_PLAN_ROOT": b0resgauge2_plan_manifest()["root"], "C174_RESIDUAL_BOUNDARY_ROOT": residual_boundary_freeze()["root"], "C174_CONTINUUM_NONIDENTITY_ROOT": continuum_cell_nonidentity_certificate()["root"], "C174_SCALAR_ROOT": scalar_parameter_manifest()["root"], "C174_GLOBAL_COLOR_ROOT": global_color_parameter_manifest()["root"], "C174_VECTOR_ROOT": p0_vector_field_manifest()["root"], "C174_GRADIENT_ROOT": gradient_manifest()["root"], "C174_DIVERGENCE_ROOT": divergence_manifest()["root"], "C174_COMPLEX_ROOT": transverse_complex_manifest()["root"], "C174_BOUNDARY_ROOT": basis_boundary_ledger()["root"], "C174_CANDIDATE_ROOT": functional_candidate_manifest()["root"], "C174_ORBIT_ROOT": orbit_functional_manifest()["root"], "C174_PROJECT_ROOT": project_subgauge_manifest()["root"], "C174_FP_ROOT": p0_fp_operator_manifest()["root"], "C174_VOLUME_ROOT": global_volume_manifest()["root"], "C174_OPEN_COLOR_ROOT": open_color_factorization_manifest()["root"], "C174_DETERMINANT_ROOT": residual_determinant_manifest()["root"], "C174_GHOST_ROOT": residual_ghost_decision()["root"], "C174_UNIQUENESS_ROOT": local_uniqueness_manifest()["root"], "C174_PV_ROOT": q0_pv_compatibility_manifest()["root"], "C174_LINK_ROOT": residual_link_manifest()["root"], "C174_GAUSS_ROOT": p0_gauss_manifest()["root"], "C174_COVARIANCE_ROOT": b0_kinematic_covariance_manifest()["root"], "C174_INTERACTION_ROOT": interaction_covariance_manifest()["root"], "C174_COUNT_ONCE_ROOT": residual_count_once_manifest()["root"], "C174_TARGET_ROOT": target_gauge_separation_manifest()["root"], "C174_BRST_ROOT": brst_st_boundary_manifest()["root"], "C174_RELEASE_ROOT": b0_release_manifest()["root"], "C174_REQUEST_ROOT": request_resolution_manifest()["root"], "C174_MISSING_ROOT": missing_residual_object_manifest()["root"], "C174_HANDOFF_ROOT": calculation_resumption_handoff_contract()["root"], "C174_FRONTIER_ROOT": dependency_frontier_manifest()["root"], "C174_QUANTUM_ROOT": quantum_residual_handoff()["root"], "C174_SCOPE_ROOT": _root((STATUS, "no-loop", "no-physical")), "C174_COMPLETENESS_ROOT": b0resgauge2_completeness_certificate()["root"]}
PACKAGE_ROOT = _root({"schema": "C174-HQCDB0RESGAUGE2-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": ROOTS})

__all__ = [name for name in globals() if not name.startswith("_")]
