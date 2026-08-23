"""C176 fail-closed residual-link boundary package.

The authenticated C43 public contract supplies gauge/action/convention and
residual-link role records, but no executable path geometry.  This package
therefore refuses to invent a path or endpoint.  The independent C174
finite-HO raising-shell boundary is exposed in factorized form, while every
path-dependent, endpoint-dependent, Wilson, ghost-link, and link-kernel
object carries an explicit blocking status rather than a numerical zero.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

import numpy as np

from deuteron_wigner.bridge import hqcdb0ghostsector1 as c175
from deuteron_wigner.bridge import hqcdb0resgauge2 as c174
from deuteron_wigner.bridge.modes.core import gell_mann
from deuteron_wigner.bridge.g0 import contracts as c43

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c176_hqcdb0reslink1"
BASELINE = "854098ef8fbeeff7a4f47c7c2268f371a9b5c8a0"
PROMPT = "/Users/dustin/Downloads/c176_hqcdb0reslink1_codex_prompt.md"
PROMPT_SHA256 = "b779723d61e2685fe345b7128c4f661fd1520664b5efe20641eb7c4d126c6eb7"
CONTRACT = "docs/next_level/c175_c176_hqcdb0reslink1_continuation_contract.json"
CONTRACT_SHA256 = "34457964822712019148ba83e7d73426a6042cc756cf55678117516713b4753c"
CONTRACT_PRESENT = True
STATUS = "C176_HQCDB0RESLINK1_PATH_GEOMETRY_INCOMPLETE"
PLAN = "B0RESLINK1-D"
NEXT = "C177/HQCDB0RESLINKSOURCE1"
SCHEME = "PROJECT_FINITE_CELL_P0_TRANSVERSE_SUBGAUGE_V1"
PATH_ID = "C43-RESIDUAL-TRANSVERSE-LINK-UNSPECIFIED"
RESOLUTIONS = ("K9", "K11", "K13")
COLORS = tuple(range(8))
COUPLING_DEGREES = (0, 1, 2)
SECTORS = ("C170-B0-G", "C170-B0-QQBAR-ADJOINT", "C170-B0-GG-ADJOINT-D", "C170-B0-GG-ADJOINT-F", "C151-ONE-GLUON")
ACTIVE_REQUESTS = (
    "C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-TRANSVERSE_GLUON_FIELD-MOMQ-2",
    "C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-QCD_COUPLING-MOMQ-2",
)


def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, Mapping): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    if isinstance(x, np.ndarray): return x.tolist()
    if isinstance(x, complex): return {"real": float(x.real), "imaginary": float(x.imag)}
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


def _c43_records() -> dict[str, Any]:
    source = c43.source_manifest()
    conventions = c43.conventions()
    action = c43.action_contract()
    c43.validate_contract(action)
    return {"source_manifest": source, "conventions": conventions, "action": action,
            "source_root": c43.symbolic_hash(source), "conventions_root": c43.symbolic_hash(conventions),
            "action_root": c43.symbolic_hash(action)}


def _c174_leakage(resolution_id: str) -> np.ndarray:
    row = c174.gradient_manifest(resolution_id=resolution_id)["rows"][0]
    payload = row["finite_shell_leakage"]["matrix"]
    return np.asarray([[complex(z[0], z[1]) for z in line] for line in payload], dtype=np.complex128)


def _scalar_rows(resolution_id: str) -> tuple[Mapping[str, Any], ...]:
    return tuple(c174.scalar_parameter_manifest(resolution_id=resolution_id)["rows"])


def _vector_rows(resolution_id: str) -> tuple[Mapping[str, Any], ...]:
    return tuple(c174.p0_vector_field_manifest(resolution_id=resolution_id)["rows"])


def _all_upstream_roots() -> Mapping[str, str]:
    return {"C175_PACKAGE_ROOT": c175.PACKAGE_ROOT, "C174_PACKAGE_ROOT": c174.PACKAGE_ROOT,
            "C174_SCALAR_ROOT": c174.ROOTS["C174_SCALAR_ROOT"], "C174_VECTOR_ROOT": c174.ROOTS["C174_VECTOR_ROOT"],
            "C174_GRADIENT_ROOT": c174.ROOTS["C174_GRADIENT_ROOT"], "C174_BOUNDARY_ROOT": c174.ROOTS["C174_BOUNDARY_ROOT"],
            "C174_LINK_ROOT": c174.ROOTS["C174_LINK_ROOT"], "C174_FP_ROOT": c174.ROOTS["C174_FP_ROOT"],
            "C175_DOMAIN_ROOT": c175.ROOTS["C175_GHOST_DOMAIN_ROOT"], "C175_SUPPORT_ROOT": c175.ROOTS["C175_LONGITUDINAL_SUPPORT_ROOT"],
            "C175_LINK_ROOT": c175.ROOTS["C175_BOUNDARY_LINK_ROOT"], "C175_DETERMINANT_ROOT": c175.ROOTS["C175_DETERMINANT_ROOT"],
            "C175_LOOP_ROOT": c175.ROOTS["C175_GHOST_LOOP_ROOT"]}


def verify_hqcd_b0reslink1_authority() -> MappingProxyType:
    c43r = _c43_records()
    return _freeze({"schema": "C176-HQCDB0RESLINK1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN,
        "next": NEXT, "contract": CONTRACT, "contract_sha256": CONTRACT_SHA256, "contract_present": CONTRACT_PRESENT,
        "prompt": PROMPT, "prompt_sha256": PROMPT_SHA256, "contract_provenance_fail_closed": False,
        "C175_package_root": c175.PACKAGE_ROOT, "C174_package_root": c174.PACKAGE_ROOT,
        "upstream_roots": _all_upstream_roots(), "C43_source_root": c43r["source_root"],
        "C43_conventions_root": c43r["conventions_root"], "C43_action_root": c43r["action_root"],
        "path_geometry_loaded": False, "path_inferred": False, "new_source_acquisitions": 0,
        "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "C171_b0_rebuilt": 0,
        "C174_gauge_rebuilt": 0, "C175_ghost_rebuilt": 0, "B1_mutations": 0,
        "C158_value_inputs": 0, "quantum_objects_modified": 0, "package_root": PACKAGE_ROOT})


def load_verified_hqcd_b0reslink1_authority() -> MappingProxyType:
    record = json.loads((RUNTIME / "manifest.json").read_text())
    if record.get("package_root") != PACKAGE_ROOT or record.get("status") != STATUS: raise ValueError("C176 runtime mismatch")
    contract_path = ROOT / CONTRACT
    if sha256(contract_path.read_bytes()).hexdigest() != CONTRACT_SHA256: raise ValueError("C175-C176 contract hash mismatch")
    return verify_hqcd_b0reslink1_authority()


def b0reslink1_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C176-PLAN-MANIFEST-V1", "selected_plan": PLAN, "status": STATUS,
        "reason": "C43 public action/convention authority has no executable path ID, endpoint geometry, transverse parameterization, or orientation; no path is inferred", "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})


def residual_link_handoff_freeze() -> MappingProxyType:
    c43r = _c43_records()
    return _freeze({"schema": "C176-RESIDUAL-LINK-HANDOFF-FREEZE-V1", "C175_status": c175.STATUS,
        "C175_plan": c175.PLAN, "C175_package_root": c175.PACKAGE_ROOT, "C175_blocker": "C175-RESIDUAL-LINK-BOUNDARY-OPERATOR",
        "C174_scheme": SCHEME, "C174_project_root": c174.ROOTS["C174_PROJECT_ROOT"], "C174_fp_root": c174.ROOTS["C174_FP_ROOT"],
        "C174_boundary_root": c174.ROOTS["C174_BOUNDARY_ROOT"], "C174_link_root": c174.ROOTS["C174_LINK_ROOT"],
        "C175_bulk_support_root": c175.ROOTS["C175_LONGITUDINAL_SUPPORT_ROOT"], "C175_ghost_link_root": c175.ROOTS["C175_BOUNDARY_LINK_ROOT"],
        "C43_path_source_root": c43r["source_root"], "C43_path_status": "ROLE_RECORD_ONLY_NO_EXECUTABLE_PATH",
        "records_rebuilt": 0, "root": _root((c175.PACKAGE_ROOT, c174.PACKAGE_ROOT, c43r["source_root"], False))})


def boundary_layer_separation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C176-BOUNDARY-LAYER-SEPARATION-V1", "spacetime_residual_transverse_link": {"owner": "C176-RESIDUAL-LINK", "status": "PATH_GEOMETRY_INCOMPLETE"}, "finite_HO_raising_shell": {"owner": "C176-HO-BOUNDARY", "status": "AVAILABLE_EXECUTABLE_FACTORISED"}, "finite_longitudinal_endpoint": {"owner": "C43/C172", "status": "separate P0/Q0 interface"}, "P0_zero_mode": {"owner": "C172/C174/C175", "status": "separate"}, "omitted_Fock_sector": {"owner": "C170/C171", "status": "separate"}, "link_HO_relation": "NONCOMPOSABLE_NONMATRIX_INTERFACE", "conflated": False, "root": _root(("link", "HO", "separate", False))})


def path_geometry_manifest(path_id: str | None = None) -> MappingProxyType:
    if path_id is not None and path_id != PATH_ID: raise KeyError(path_id)
    c43r = _c43_records()
    row = {"path_id": PATH_ID, "scientific_role": "C43 residual transverse Wilson closure for finite-cell open-adjoint probe", "representation": "not executable; C43 source role is retained but path representation is absent", "basepoint": None, "endpoint": None, "finite_cell_longitudinal_boundary": "not supplied", "periodic_identification": "not promoted to a transverse endpoint identity", "transverse_parameterization": None, "orientation": None, "path_ordering": None, "source_color_action": "open-adjoint covariance required", "sink_color_action": "open-adjoint covariance required", "C43_source_root": c43r["source_root"], "C43_action_root": c43r["action_root"], "C174_scheme": SCHEME, "status": "PATH_GEOMETRY_INCOMPLETE", "missing_object": "exact source-qualified path ID, basepoint, endpoint, parameterization, orientation, and path-order convention", "path_inferred": False}
    return _freeze({"schema": "C176-PATH-GEOMETRY-V1", "rows": (row,), "root": _root(row)})


def boundary_evaluation_manifest(mode_id: str | None = None, projector_id: str | None = None, path_id: str | None = None) -> MappingProxyType:
    if path_id is not None and path_id != PATH_ID: raise KeyError(path_id)
    rows = []
    for r in RESOLUTIONS:
        scalar = _scalar_rows(r); vector = _vector_rows(r)
        if mode_id is not None and mode_id not in {x["mode_id"] for x in scalar + vector}: raise KeyError(mode_id)
        rows.append({"resolution": r, "mode_filter": mode_id, "projector_id": projector_id, "path_id": PATH_ID, "P0_dimension": 2 * len(scalar), "Q0_dimension": "retained C151/C171 source dimension caller-bound; not reconstructed", "P0_Q0_separate": True, "incoming_mode_identity": mode_id or "C174/C151 public mode identity", "longitudinal_fourier_mode": {"P0": 0, "Q0": "nonzero retained source"}, "transverse_HO_identity": "C174 vector configuration / C151 source role kept separate", "boundary_coordinate": None, "path_parameter": None, "normalization": "C174/C151 public normalization only; endpoint trace unavailable", "units": "source-qualified; endpoint map unavailable", "phase": "C45 phase retained; endpoint evaluation unavailable", "periodic_endpoint_relation": "unresolved without path geometry", "finite_shell": "C174 leakage retained", "routes": ("EVAL-A direct analytic", "EVAL-B finite Fourier", "EVAL-C recurrence/generating", "EVAL-D bounded quadrature", "EVAL-E operator/source topology"), "route_status": "BLOCKED_BY_PATH_GEOMETRY", "endpoint_value": "UNAVAILABLE_NOT_ZERO", "root": _root((r, mode_id, projector_id, PATH_ID, "blocked"))})
    return _freeze({"schema": "C176-BOUNDARY-EVALUATION-V1", "rows": tuple(rows), "root": _root(rows)})


def path_trace_manifest(path_id: str | None = None) -> MappingProxyType:
    if path_id is not None and path_id != PATH_ID: raise KeyError(path_id)
    return _freeze({"schema": "C176-PATH-TRACE-V1", "path_id": PATH_ID, "T_path": "UNAVAILABLE_NOT_ZERO", "line_measure": None, "transverse_path": None, "P0_trace": "blocked", "Q0_trace": "blocked", "status": "PATH_GEOMETRY_INCOMPLETE", "root": _root((PATH_ID, "trace-blocked"))})


def _structure_constants() -> np.ndarray:
    t = gell_mann(); f = np.zeros((8, 8, 8), dtype=float)
    for a in COLORS:
        for b in COLORS:
            for c in COLORS:
                f[a, b, c] = float((-2j * np.trace((t[a] @ t[b] - t[b] @ t[a]) @ t[c])).real)
    return f


def link_color_manifest() -> MappingProxyType:
    f = _structure_constants()
    rows = tuple({"generator": a, "convention": "[T^a,T^b]=i f^{abc}T^c; T=lambda/2; Tr(TaTb)=delta/2", "adjoint_transport": "(T_adj^a)_{bc}=-i f^{abc}", "source_action": "open-adjoint coordinate retained", "sink_action": "generated by source orientation", "residual": float(np.linalg.norm(f[a] + f[a].T)), "all_eight_generators": True} for a in COLORS)
    return _freeze({"schema": "C176-LINK-COLOR-V1", "rows": rows, "tensor_hash": _array_hash(f), "all_eight_generators": True, "global_volume": "C174 separate", "open_adjoint": True, "singlet_projection": False, "adjoint_dimension_divided": False, "C171_gg_multiplicities": ("d", "f"), "path_dependent_transport": "blocked by path geometry", "root": _root(rows)})


def wilson_link_manifest(path_id: str | None = None, coupling_degree: int | None = None) -> MappingProxyType:
    if path_id is not None and path_id != PATH_ID: raise KeyError(path_id)
    ds = _check(coupling_degree, COUPLING_DEGREES); rows = []
    for d in ds:
        rows.append({"path_id": PATH_ID, "coupling_degree": d, "identity_degree_zero": d == 0, "ordered_insertions": "unavailable for d=1,2 because path measure/orientation absent" if d else "formal identity transport only; no path matrix materialized", "source_sign": "C43 D/U convention not sufficient to bind path orientation", "path_measure": None, "field_normalization": "C43 field convention retained", "endpoint_orientation": None, "color_order": "not evaluated", "units": "unavailable", "finite_shell_status": "separate C176 HO boundary", "routes": ("LINK-A direct path expansion", "LINK-B differential transport", "LINK-C segmented composition", "LINK-D reverse/generated adjoint", "LINK-E covariance"), "route_status": "BLOCKED_BY_PATH_GEOMETRY", "symmetrized": False, "status": "ADJOINT_LINK_EXPANSION_INCOMPLETE", "not_zero": True, "root": _root((PATH_ID, d, "blocked"))})
    return _freeze({"schema": "C176-WILSON-LINK-V1", "rows": tuple(rows), "root": _root(rows)})


def apply_wilson_link_order(path_id: str, coupling_degree: int, field_record: Mapping[str, Any], color_vector: Any) -> MappingProxyType:
    if path_id != PATH_ID: raise KeyError(path_id)
    if coupling_degree not in COUPLING_DEGREES: raise KeyError(coupling_degree)
    return _freeze({"status": "ADJOINT_LINK_EXPANSION_INCOMPLETE", "path_id": PATH_ID, "coupling_degree": coupling_degree, "action": "UNAVAILABLE_NOT_ZERO", "field_record_consumed": False, "color_vector_consumed": False, "reason": "exact path geometry is absent; no link matrix element inferred", "root": _root((PATH_ID, coupling_degree, "no-action"))})


def link_covariance_manifest() -> MappingProxyType:
    return _freeze({"schema": "C176-LINK-COVARIANCE-V1", "identity_path": "blocked", "concatenation": "blocked", "reversal": "blocked", "generated_adjoint": "blocked", "endpoint_transformation": "blocked", "periodic_cell": "longitudinal identity does not imply transverse path identity", "global_covariance": "color tensor closes; path covariance unavailable", "all_eight_generators": True, "status": "PATH_GEOMETRY_INCOMPLETE", "root": _root((PATH_ID, "covariance-blocked"))})


def ho_boundary_manifest(resolution_id: str | None = None, source_mode_id: str | None = None) -> MappingProxyType:
    rs = _check(resolution_id, RESOLUTIONS); rows = []
    for r in rs:
        scalar = _scalar_rows(r); d = len(scalar); leakage = _c174_leakage(r)
        if source_mode_id is not None and source_mode_id not in {x["mode_id"] for x in scalar}: raise KeyError(source_mode_id)
        entries = []
        for component_offset, comp in enumerate(("x", "y")):
            component = leakage[component_offset * leakage.shape[0] // 2:(component_offset + 1) * leakage.shape[0] // 2]
            for target, source in zip(*np.nonzero(np.abs(component) > 0)):
                entries.append({"source_mode_id": scalar[int(source)]["mode_id"], "first_omitted_shell": f"Nmax+1:{comp}:{int(target)}", "derivative_component": comp, "coefficient": (float(component[target, source].real), float(component[target, source].imag)), "phase": "C45 Cartesian derivative phase", "units": "GeV", "orientation": "Q_HO gradient P_HO", "rank": len(entries), "count_once_owner": "C176-HO-BOUNDARY"})
        gradient = c174.gradient_manifest(resolution_id=r)["rows"][0]
        rows.append({"resolution": r, "source_mode_filter": source_mode_id, "retained_dimension": d, "factorized_omitted_dimension": leakage.shape[0], "gradient_boundary_matrix": tuple(entries), "leakage_norm": float(np.linalg.norm(leakage)), "leakage_nonzero_entries": len(entries), "leakage_threshold_pruned": False, "rank": int(np.linalg.matrix_rank(leakage, tol=1e-12)), "units": "GeV", "B_gradient": "factorized Q_HO nabla P_HO", "B_divergence": "factorized adjoint P_HO nabla^dagger Q_HO", "routes": ("HO-BND-A exact ladder leakage", "HO-BND-B analytic derivative integration", "HO-BND-C integration-by-parts defect", "HO-BND-D bounded quadrature holdout", "HO-BND-E adjoint/reversal"), "C174_gradient_root": c174.ROOTS["C174_GRADIENT_ROOT"], "route_status": "AVAILABLE_EXECUTABLE_FACTORISED", "root": _root((r, _array_hash(leakage), gradient["root"]))})
    return _freeze({"schema": "C176-HO-BOUNDARY-V1", "rows": tuple(rows), "root": _root(rows)})


def apply_ho_boundary_operator(resolution_id: str, vector: Any, orientation: str | None = None) -> MappingProxyType:
    _check(resolution_id, RESOLUTIONS); orientation = orientation or "gradient"
    if orientation not in ("gradient", "divergence"): raise KeyError(orientation)
    leak = _c174_leakage(resolution_id); v = np.asarray(vector, dtype=np.complex128)
    if orientation == "gradient":
        if v.ndim != 1 or v.size != leak.shape[1]: raise ValueError("retained vector dimension")
        out = leak @ v; adj = leak.conj().T @ out
        return _freeze({"resolution": resolution_id, "orientation": orientation, "action": tuple((float(z.real), float(z.imag)) for z in out), "adjoint_roundtrip_residual": float(np.linalg.norm(adj - leak.conj().T @ (leak @ v))), "omitted_space_materialized": False, "root": _root((resolution_id, orientation, _array_hash(out)))})
    if v.ndim != 1 or v.size != leak.shape[0]: raise ValueError("factorized omitted vector dimension")
    out = leak.conj().T @ v
    return _freeze({"resolution": resolution_id, "orientation": orientation, "action": tuple((float(z.real), float(z.imag)) for z in out), "omitted_space_materialized": False, "root": _root((resolution_id, orientation, _array_hash(out)))})


def integration_by_parts_defect_manifest(resolution_id: str | None = None) -> MappingProxyType:
    rs = _check(resolution_id, RESOLUTIONS); rows = []
    for r in rs:
        leak = _c174_leakage(r); rows.append({"resolution": r, "defect_operator": "B_div = B_gradient^dagger on factorized first-omitted image", "shape": leak.shape, "rank": int(np.linalg.matrix_rank(leak, tol=1e-12)), "norm": float(np.linalg.norm(leak)), "defect_nonzero": bool(np.linalg.norm(leak) > 0), "formula": "<P phi, div Q psi>-<grad P phi,Q psi>=boundary defect", "routes": ("analytic ladder", "integration by parts", "quadrature holdout"), "threshold_pruned": False, "root": _root((r, _array_hash(leak)))})
    return _freeze({"schema": "C176-INTEGRATION-BY-PARTS-DEFECT-V1", "rows": tuple(rows), "root": _root(rows)})


def boundary_relation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C176-BOUNDARY-RELATION-V1", "link_owner": "C176-RESIDUAL-LINK", "ho_owner": "C176-HO-BOUNDARY", "shared_source_target_space": False, "composition_order": None, "coupling_degree": None, "units": "separate", "sign": None, "count_once": True, "relation": "NONCOMPOSABLE_NONMATRIX_INTERFACE", "reason": "HO factorized leakage is executable, spacetime link is path-blocked; no cancellation inferred", "root": _root(("link", "HO", "noncomposable"))})


def link_variation_manifest(residual_parameter_id: str | None = None, path_id: str | None = None) -> MappingProxyType:
    if path_id is not None and path_id != PATH_ID: raise KeyError(path_id)
    return _freeze({"schema": "C176-LINK-VARIATION-V1", "residual_parameter_id": residual_parameter_id, "path_id": PATH_ID, "endpoint_action": "UNAVAILABLE_NOT_ZERO", "bulk_path_action": "UNAVAILABLE_NOT_ZERO", "global_color_kernel": "C174 global SU3 outside local chart", "P0_Q0": "separate", "path_ordering": None, "representation": "open-adjoint required", "boundary_HO_interface": "separate", "routes": ("VAR-LINK-A endpoint", "VAR-LINK-B ordered expansion", "VAR-LINK-C transport equation", "VAR-LINK-D reverse/generated adjoint"), "status": "PATH_GEOMETRY_INCOMPLETE", "BRST": False, "root": _root((PATH_ID, residual_parameter_id, "variation-blocked"))})


def ghost_link_manifest(resolution_id: str | None = None, path_id: str | None = None) -> MappingProxyType:
    rs = _check(resolution_id, RESOLUTIONS)
    if path_id is not None and path_id != PATH_ID: raise KeyError(path_id)
    rows = tuple({"resolution": r, "path_id": PATH_ID, "ghost_domain_root": c175.ROOTS["C175_GHOST_DOMAIN_ROOT"], "antighost_domain_root": c175.ROOTS["C175_GHOST_DOMAIN_ROOT"], "C174_scheme": SCHEME, "C175_free_root": c175.ROOTS["C175_FREE_GHOST_ROOT"], "C175_interaction_root": c175.ROOTS["C175_GHOST_INTERACTION_ROOT"], "coupling_degree": 1, "Grassmann_order": "bar_c -> link -> c", "color_tensor": "adjoint f tensor; open color retained", "path_orientation": None, "P0_Q0_support": "endpoint support incomplete", "HO_boundary_dependence": "separate factorized interface", "count_once_owner": "C176-LINK-GHOST", "routes": ("GHOST-LINK-A", "GHOST-LINK-B", "GHOST-LINK-C", "GHOST-LINK-D", "GHOST-LINK-E"), "status": "GHOST_LINK_INCOMPLETE", "not_zero": True, "root": _root((r, PATH_ID, "ghost-link-blocked"))} for r in rs)
    return _freeze({"schema": "C176-GHOST-LINK-V1", "rows": rows, "root": _root(rows)})


def endpoint_support_manifest(external_sector_id: str | None = None, path_id: str | None = None, coupling_degree: int | None = None) -> MappingProxyType:
    if external_sector_id is not None and external_sector_id not in SECTORS: raise KeyError(external_sector_id)
    if path_id is not None and path_id != PATH_ID: raise KeyError(path_id)
    ds = _check(coupling_degree, COUPLING_DEGREES); sectors = (external_sector_id,) if external_sector_id else SECTORS
    rows = tuple({"external_sector_id": sector, "path_id": PATH_ID, "coupling_degree": d, "P0_endpoint": "UNAVAILABLE_NOT_ZERO", "Q0_endpoint": "UNAVAILABLE_NOT_ZERO", "analytic_route": "blocked", "Fourier_route": "blocked", "one_link_route": "blocked", "two_link_route": "blocked", "ghost_link_route": "blocked", "source_topology_route": "retained source identity known; path contraction unavailable", "HO_boundary_exception": "separate nonzero factorized leakage", "classification": "SUPPORT_INCOMPLETE", "orthogonality_assumed": False, "nonzero_assumed": False, "root": _root((sector, PATH_ID, d, "support-incomplete"))} for sector in sectors for d in ds)
    return _freeze({"schema": "C176-ENDPOINT-SUPPORT-V1", "rows": rows, "root": _root(rows)})


def link_kernel_manifest(request_id: str | None = None, path_id: str | None = None, coupling_degree: int | None = None) -> MappingProxyType:
    if request_id is not None and request_id not in ACTIVE_REQUESTS: raise KeyError(request_id)
    if path_id is not None and path_id != PATH_ID: raise KeyError(path_id)
    ds = _check(coupling_degree, COUPLING_DEGREES); reqs = (request_id,) if request_id else ACTIVE_REQUESTS
    rows = tuple({"request_id": rid, "path_id": PATH_ID, "coupling_degree": d, "external_source": "C151/C171 retained open-adjoint source", "boundary_field": "unavailable path-boundary identity", "source_order": "external source -> ordered link insertions", "color_order": "not evaluated", "path_orientation": None, "transverse_HO_trace": "unavailable", "P0_Q0_support": "SUPPORT_INCOMPLETE", "finite_shell_remainder": "explicit C176-HO-BOUNDARY owner", "units": "unavailable", "status": "PATH_GEOMETRY_INCOMPLETE", "enclosure": "UNAVAILABLE_NOT_ZERO", "routes": ("LKERNEL-A", "LKERNEL-B", "LKERNEL-C", "LKERNEL-D", "LKERNEL-E", "LKERNEL-F", "LKERNEL-G"), "complete_self_energy": False, "root": _root((rid, PATH_ID, d, "kernel-blocked"))} for rid in reqs for d in ds)
    return _freeze({"schema": "C176-LINK-KERNEL-V1", "rows": rows, "root": _root(rows)})


def open_color_manifest() -> MappingProxyType:
    return _freeze({"schema": "C176-OPEN-COLOR-V1", "open_adjoint": True, "global_volume": "C174 separate", "singlet_projection": False, "adjoint_dimension_divided": False, "gg_multiplicities": ("d", "f"), "all_eight_generators": True, "link_path_transport": "blocked; color algebra retained", "root": _root((True, False, False, "d", "f"))})


def link_reality_manifest() -> MappingProxyType:
    return _freeze({"schema": "C176-LINK-REALITY-V1", "source_orientation": "C43 source -> sink open-adjoint", "link_adjoint": "generated reverse path; unavailable until path closes", "reverse_path": "not independently fitted", "complex_conjugation": "source orientation reversal", "one_link": "blocked", "two_link_order": "ordered, not symmetrized", "ghost_link_orientation": "bar_c -> link -> c", "physical_positivity": False, "root": _root((PATH_ID, "ordered", False))})


def boundary_count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    if request_id is not None and request_id not in ACTIVE_REQUESTS: raise KeyError(request_id)
    rows = ({"owner": "C172-Q0-DETERMINANT", "status": "separate"}, {"owner": "C175-BULK-P0-GHOST-DETERMINANT", "status": "imported read-only; not recomputed"}, {"owner": "C176-RESIDUAL-LINK", "status": "path-blocked; not zero"}, {"owner": "C176-LINK-GHOST", "status": "path-blocked; not zero"}, {"owner": "C176-HO-BOUNDARY", "status": "factorized executable leakage"}, {"owner": "C43-FINITE-LONGITUDINAL-BOUNDARY", "status": "separate"}, {"owner": "C174-GLOBAL-VOLUME", "status": "separate"}, {"owner": "C130-GAUSS-INSTANTANEOUS", "status": "separate"}, {"owner": "C111-C112-C127-C129", "status": "separate"}, {"owner": "C170-C171-QBARQ-GG", "status": "separate"}, {"owner": "TARGET-LINK-GHOST", "status": "target-side only"})
    return _freeze({"schema": "C176-BOUNDARY-COUNT-ONCE-V1", "request_id": request_id, "rows": rows, "duplicate_owners": 0, "missing_as_zero": 0, "link_HO_conflated": False, "root": _root((request_id, rows))})


def target_link_separation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C176-TARGET-LINK-SEPARATION-V1", "C43_residual_link": "finite-cell open-adjoint matching probe; path geometry incomplete", "physical_TMD_staple": "PHYSICAL_TMD_LINK_NOT_CONSTRUCTED", "soft_subtraction": "SOFT_SUBTRACTION_NOT_CONSTRUCTED", "target_MOMq_RI_SMOM": "separate target-side", "target_ghost_link_imported": False, "adapter": False, "root": _root((PATH_ID, False, False, False))})


def brst_st_boundary_manifest() -> MappingProxyType:
    return _freeze({"schema": "C176-BRST-ST-BOUNDARY-V1", "BRST": "BRST_NOT_CONSTRUCTED", "full_ST": "FULL_ST_NOT_PROVED", "coupling_renormalization": "COUPLING_RENORMALIZATION_NOT_AUTHORIZED", "link_covariance_is_BRST": False, "root": _root(("no-BRST", "no-ST", False))})


def b0_release_manifest() -> MappingProxyType:
    return _freeze({"schema": "C176-B0-RELEASE-V1", "decision": "B0_NOT_RELEASED_PATH_GEOMETRY_INCOMPLETE", "C174_scheme": SCHEME, "C175_bulk_support": "preserved exact bulk orthogonality", "path_geometry": "incomplete", "boundary_evaluation": "blocked", "wilson_link": "blocked", "ho_boundary": "independent factorized authority ready", "link_HO_relation": "noncomposable nonmatrix interface", "ghost_link": "blocked", "endpoint_support": "incomplete", "open_color": "separate retained", "count_once": "structural closed", "target_link": "separate", "BRST_ST": "not proved", "counterterm_null": "unselected", "exact_scope": "finite-HO leakage operator only; no path or link coefficient released", "next": NEXT, "root": _root((STATUS, PLAN, NEXT, False))})


def _inherited_requests() -> tuple[Mapping[str, Any], ...]:
    return tuple(c175.request_resolution_manifest()["rows"])


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = []
    for row in _inherited_requests():
        active = row["request_id"] in ACTIVE_REQUESTS
        rows.append({"request_id": row["request_id"], "C168_capsule_id": row["C168_capsule_id"], "C169_status": row["C169_status"], "C170_status": row["C170_status"], "C171_status": row["C171_status"], "C172_status": row["C172_status"], "C173_status": row["C173_status"], "C174_status": row["C174_status"], "C175_status": row["C175_terminal_status"], "path_status": "PATH_GEOMETRY_INCOMPLETE" if active else "PRESERVED_INHERITED_REQUEST", "boundary_evaluation_status": "BOUNDARY_EVALUATION_INCOMPLETE" if active else "PRESERVED_INHERITED_REQUEST", "link_expansion_status": "ADJOINT_LINK_EXPANSION_INCOMPLETE" if active else "PRESERVED_INHERITED_REQUEST", "HO_boundary_status": "AVAILABLE_EXECUTABLE_FACTORISED" if active else "PRESERVED_INHERITED_REQUEST", "ghost_link_status": "GHOST_LINK_INCOMPLETE" if active else "PRESERVED_INHERITED_REQUEST", "endpoint_support_status": "ENDPOINT_SUPPORT_INCOMPLETE" if active else "PRESERVED_INHERITED_REQUEST", "B0_release_status": b0_release_manifest()["decision"] if active else "PRESERVED_INHERITED_REQUEST", "C176_terminal_status": "PATH_GEOMETRY_INCOMPLETE" if active else "PRESERVED_INHERITED_REQUEST", "next_object": NEXT if active else "unchanged"})
    if request_id is not None:
        rows = [row for row in rows if row["request_id"] == request_id]
        if not rows: raise KeyError(request_id)
    return _freeze({"schema": "C176-REQUEST-RESOLUTION-V1", "rows": tuple(rows), "count": len(rows), "all_six_visible": len(rows) == 6 if request_id is None else True, "root": _root(rows)})


def missing_boundary_object_manifest(request_id: str | None = None) -> MappingProxyType:
    if request_id is not None and request_id not in ACTIVE_REQUESTS: raise KeyError(request_id)
    reqs = (request_id,) if request_id else ACTIVE_REQUESTS
    rows = tuple({"request_id": rid, "object_id": "C176-C43-RESIDUAL-LINK-PATH-GEOMETRY", "parent_C169_request": rid, "C171_sectors": ("C170-B0-G", "C170-B0-QQBAR-ADJOINT", "C170-B0-GG-ADJOINT-D", "C170-B0-GG-ADJOINT-F"), "C172_scheme": "Q0/P0 projectors and antisymmetric/PV", "C173_scheme": "continuum-source/nonidentity preserved", "C174_scheme": SCHEME, "C175_ghost_support": c175.ROOTS["C175_LONGITUDINAL_SUPPORT_ROOT"], "path_id": PATH_ID, "endpoint_geometry": "required exact source object", "P0_Q0": "endpoint support blocked", "boundary_condition": "finite-cell endpoint and transverse closure semantics required", "PV": "antisymmetric/PV unchanged", "representation": "open adjoint with source/sink action", "open_color": True, "coupling_degree": (0, 1, 2), "required_routes": ("path source", "endpoint map", "finite Fourier", "ordered link", "ghost-link", "support"), "holdouts": ("no inferred path", "no endpoint zero", "no link unity", "no degree-two symmetrization"), "nonclaims": ("no physical TMD staple", "no soft factor", "no physical boundary loop", "no self-energy", "no adapter", "no BRST/ST"), "status": "REQUIRES_C177_HQCDB0RESLINKSOURCE1", "not_zero": True} for rid in reqs)
    return _freeze({"schema": "C176-MISSING-BOUNDARY-OBJECT-V1", "rows": rows, "root": _root(rows)})


def calculation_resumption_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C176-CALCULATION-HANDOFF-V1", "status": STATUS, "plan": PLAN, "C171_B0_read_only": True, "C174_scheme": SCHEME, "roots": ROOTS if "ROOTS" in globals() else {}, "B0_release": b0_release_manifest()["decision"], "remaining": "C43 executable residual-link path and endpoint geometry", "next": NEXT, "no_self_energy": True, "no_adapter": True, "root": _root((STATUS, PLAN, NEXT, "read-only"))})


def dependency_frontier_manifest() -> MappingProxyType:
    rows = ({"frontier_id": "C167-RI-SMOM", "status": "PRESERVED_TWO_SOURCE_RESOLVED_LEAVES"}, {"frontier_id": "C168-C169-REQUESTS", "status": "SIX_VISIBLE_TWO_ACTIVE"}, {"frontier_id": "C163-LOCATORS", "status": "SIX_PRESERVED"}, {"frontier_id": "C171-B0", "status": "READ_ONLY"}, {"frontier_id": "C172-Q0", "status": "CLOSED_DECLARED_SCOPE"}, {"frontier_id": "C173-NONIDENTITY", "status": "PRESERVED"}, {"frontier_id": "C174-P0", "status": "PROJECT_SCHEME_PRESERVED"}, {"frontier_id": "C175-GHOST", "status": "LOCAL_READY_BULK_ORTHOGONAL_PRESERVED"}, {"frontier_id": "C176-RESLINK", "status": "PATH_GEOMETRY_INCOMPLETE"}, {"frontier_id": "C170-B1-QGG", "status": "PRESERVED"}, {"frontier_id": "C170-B1-QQBARQ", "status": "PRESERVED"}, {"frontier_id": "C155-COUNTERTERM", "status": "PRESERVED"})
    return _freeze({"schema": "C176-DEPENDENCY-FRONTIER-V1", "rows": rows, "delta_only": True, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "root": _root(rows)})


def quantum_boundary_handoff() -> MappingProxyType:
    return _freeze({"schema": "C176-QUANTUM-BOUNDARY-HANDOFF-V1", "Q0_Q1_Q2_modified": False, "boundary_link_qubits": 0, "production_QubitUnitary": 0, "states_created": 0, "TMD_objects_created": 0, "root": _root((False, 0, 0, 0))})


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"new_source_acquisitions": 0, "web_search": 0, "model_memory_formulas": 0, "retrospective_contracts_invented": 0, "path_inferred": 0, "endpoint_zero_from_bulk": 0, "endpoint_nonzero_assumed": 0, "link_staple_conflations": 0, "link_HO_conflations": 0, "Abelianized_degree_two": 0, "threshold_pruned_leakage": 0, "target_link_imports": 0, "target_ghost_imports": 0, "C175_rebuilt": 0, "C174_rebuilt": 0, "B1_mutations": 0, "global_color_local_matrix": 0, "C158_value_inputs": 0, "private_upstream_builder_calls": 0, "missing_values_set_zero": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "counterterms_selected": 0, "null_coordinates_selected": 0, "quantum_objects_modified": 0, "pass": True, "root": _root((STATUS, PLAN, 0))})


def b0reslink1_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C176-HQCDB0RESLINK1-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, "contract_hash_verified": True, "path_geometry_ready": False, "boundary_evaluation_ready": False, "wilson_link_ready": False, "ho_boundary_ready": True, "integration_by_parts_defect_ready": True, "link_HO_relation": "NONCOMPOSABLE_NONMATRIX_INTERFACE", "ghost_link_ready": False, "endpoint_support_ready": False, "link_kernels_ready": False, "open_color": True, "count_once": True, "C175_preserved": True, "C174_preserved": True, "C171_b0_rebuilt": 0, "B1_mutations": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "C158_value_inputs": 0, "quantum_objects_modified": 0, "next": NEXT, "root": _root((STATUS, PLAN, NEXT, False, True))})


def mutate_live_hqcdb0reslink1(index: int) -> MappingProxyType:
    fields = ("C175_root", "C174_root", "C43_path", "path_id", "endpoint", "P0_map", "Q0_map", "trace", "color", "degree_zero", "degree_one", "degree_two", "order", "reversal", "composition", "adjoint", "HO_leakage", "IBP_defect", "relation", "variation", "ghost_link", "support", "kernel", "open_color", "count_once", "target_link", "BRST", "request", "frontier", "package_root")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False, "must_fail_or_change_root": True})


ROOTS = {
    "C176_INPUT_ROOT": _root((BASELINE, CONTRACT_SHA256, PROMPT_SHA256, c175.PACKAGE_ROOT)),
    "C176_REGRESSION_BOUNDARY_ROOT": _root(("C134-quarantine", "C157-preserved", 0)),
    "C176_CONTRACT_PROVENANCE_ROOT": _root((CONTRACT, CONTRACT_SHA256, True, "C170/C171/C172/C173/C174/C175-prompt-only")),
    "C176_PLAN_ROOT": b0reslink1_plan_manifest()["root"], "C176_HANDOFF_FREEZE_ROOT": residual_link_handoff_freeze()["root"],
    "C176_BOUNDARY_LAYER_ROOT": boundary_layer_separation_manifest()["root"], "C176_PATH_GEOMETRY_ROOT": path_geometry_manifest()["root"],
    "C176_BOUNDARY_EVALUATION_ROOT": boundary_evaluation_manifest()["root"], "C176_PATH_TRACE_ROOT": path_trace_manifest()["root"],
    "C176_LINK_COLOR_ROOT": link_color_manifest()["root"], "C176_WILSON_LINK_ROOT": wilson_link_manifest()["root"],
    "C176_LINK_COVARIANCE_ROOT": link_covariance_manifest()["root"], "C176_HO_BOUNDARY_ROOT": ho_boundary_manifest()["root"],
    "C176_INTEGRATION_BY_PARTS_DEFECT_ROOT": integration_by_parts_defect_manifest()["root"], "C176_BOUNDARY_RELATION_ROOT": boundary_relation_manifest()["root"],
    "C176_LINK_VARIATION_ROOT": link_variation_manifest()["root"], "C176_GHOST_LINK_ROOT": ghost_link_manifest()["root"],
    "C176_ENDPOINT_SUPPORT_ROOT": endpoint_support_manifest()["root"], "C176_LINK_KERNEL_ROOT": link_kernel_manifest()["root"],
    "C176_OPEN_COLOR_ROOT": open_color_manifest()["root"], "C176_LINK_REALITY_ROOT": link_reality_manifest()["root"],
    "C176_COUNT_ONCE_ROOT": boundary_count_once_manifest()["root"], "C176_TARGET_LINK_SEPARATION_ROOT": target_link_separation_manifest()["root"],
    "C176_BRST_ST_BOUNDARY_ROOT": brst_st_boundary_manifest()["root"], "C176_B0_RELEASE_ROOT": b0_release_manifest()["root"],
    "C176_REQUEST_RESOLUTION_ROOT": request_resolution_manifest()["root"], "C176_MISSING_OBJECT_ROOT": missing_boundary_object_manifest()["root"],
    "C176_DEPENDENCY_FRONTIER_ROOT": dependency_frontier_manifest()["root"], "C176_QUANTUM_HANDOFF_ROOT": quantum_boundary_handoff()["root"],
    "C176_SCOPE_ROOT": _root((STATUS, "no-physical-link", "no-self-energy", "no-TMD", "no-quantum")), "C176_COMPLETENESS_ROOT": b0reslink1_completeness_certificate()["root"]
}
ROOTS["C176_CALCULATION_HANDOFF_ROOT"] = calculation_resumption_handoff_contract()["root"]
PACKAGE_ROOT = _root({"schema": "C176-HQCDB0RESLINK1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": ROOTS})


__all__ = [name for name in globals() if not name.startswith("_")]
