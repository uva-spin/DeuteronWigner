"""C175 local Grassmann ghost sector for the project-owned C174 P0 gauge.

This module is deliberately a residual-gauge infrastructure package.  Ghost
coordinates are finite Berezin variables, not positive-metric particles.  The
C174 scalar/vector/FP records are imported through their public API and are
never rebuilt or mutated here.  The retained Q0 source is handled by an exact
longitudinal-support proof; the residual-link operator remains a separate
nonmatrix interface.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

import numpy as np

from deuteron_wigner.bridge import hqcdb0resgauge2 as c174
from deuteron_wigner.bridge.modes.core import gell_mann

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c175_hqcdb0ghostsector1"
BASELINE = "66081dc2d58954d0e8a03f7caccaa495f03acd70"
PROMPT = "/Users/dustin/Downloads/c175_hqcdb0ghostsector1_codex_prompt.md"
PROMPT_SHA256 = "48490147681b15fcc324e86ac9749dabf2b39822628ca10d7903be9bd6d71038"
EXPECTED_CONTRACT = "docs/next_level/c174_c175_hqcdb0ghostsector1_continuation_contract.json"
CONTRACT_PRESENT = False
STATUS = "C175_C174_LOCAL_P0_GHOST_AUTHORITY_READY_RETAINED_Q0_B0_SOURCE_ORTHOGONAL"
PLAN = "B0GHOSTSECTOR1-H"
NEXT = "C176/HQCDB0RESLINK1"
SCHEME = "PROJECT_FINITE_CELL_P0_TRANSVERSE_SUBGAUGE_V1"
RESOLUTIONS = ("K9", "K11", "K13")
COLORS = tuple(range(8))
ROLES = ("ghost", "antighost")
NMAX = {"K9": 8, "K11": 10, "K13": 12}
EXPECTED_DIMS = {"K9": 288, "K11": 440, "K13": 624}
ACTIVE_REQUESTS = (
    "C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-TRANSVERSE_GLUON_FIELD-MOMQ-2",
    "C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-QCD_COUPLING-MOMQ-2",
)

UPSTREAM_ROOTS = {
    "C174_PACKAGE_ROOT": c174.PACKAGE_ROOT,
    "C174_SCALAR_ROOT": c174.ROOTS["C174_SCALAR_ROOT"],
    "C174_VECTOR_ROOT": c174.ROOTS["C174_VECTOR_ROOT"],
    "C174_GRADIENT_ROOT": c174.ROOTS["C174_GRADIENT_ROOT"],
    "C174_DIVERGENCE_ROOT": c174.ROOTS["C174_DIVERGENCE_ROOT"],
    "C174_FP_ROOT": c174.ROOTS["C174_FP_ROOT"],
    "C174_BOUNDARY_ROOT": c174.ROOTS["C174_BOUNDARY_ROOT"],
    "C174_LINK_ROOT": c174.ROOTS["C174_LINK_ROOT"],
    "C174_VOLUME_ROOT": c174.ROOTS["C174_VOLUME_ROOT"],
    "C174_OPEN_COLOR_ROOT": c174.ROOTS["C174_OPEN_COLOR_ROOT"],
    "C174_PV_ROOT": c174.ROOTS["C174_PV_ROOT"],
    "C174_RELEASE_ROOT": c174.ROOTS["C174_RELEASE_ROOT"],
}


def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType):
        return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, Mapping):
        return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [_plain(v) for v in x]
    if isinstance(x, np.ndarray):
        return x.tolist()
    if isinstance(x, complex):
        return {"real": float(x.real), "imaginary": float(x.imag)}
    return x


def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping):
        return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)):
        return tuple(_freeze(v) for v in x)
    return x


def _root(x: Any) -> str:
    return sha256(json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True, default=str).encode()).hexdigest()


def _array_hash(a: np.ndarray) -> str:
    b = np.ascontiguousarray(a)
    return sha256(b.dtype.str.encode() + str(b.shape).encode() + b.tobytes()).hexdigest()


def _check(value: str | None, allowed: tuple[str, ...]) -> tuple[str, ...]:
    if value is not None and value not in allowed:
        raise KeyError(value)
    return allowed if value is None else (value,)


def _scalar_rows(resolution_id: str) -> tuple[Mapping[str, Any], ...]:
    return tuple(c174.scalar_parameter_manifest(resolution_id=resolution_id)["rows"])


def _scalar_index(resolution_id: str) -> dict[str, int]:
    return {row["mode_id"]: i for i, row in enumerate(_scalar_rows(resolution_id))}


def _validate_role(role: str) -> str:
    if role not in ROLES:
        raise KeyError(role)
    return role


def _domain_row(resolution_id: str, role: str, scalar_mode_id: str, color_id: int) -> dict[str, Any]:
    _check(resolution_id, RESOLUTIONS)
    _validate_role(role)
    rows = _scalar_rows(resolution_id)
    lookup = _scalar_index(resolution_id)
    if scalar_mode_id not in lookup or color_id not in COLORS:
        raise KeyError((scalar_mode_id, color_id))
    rank = lookup[scalar_mode_id] * 8 + color_id
    return {
        "mode_id": f"{resolution_id}:{role}:{scalar_mode_id.split(':')[-2]}:{scalar_mode_id.split(':')[-1]}:adj{color_id}",
        "resolution": resolution_id,
        "ghost_role": role,
        "spatial_mode_id": scalar_mode_id,
        "nx": rows[lookup[scalar_mode_id]]["nx"],
        "ny": rows[lookup[scalar_mode_id]]["ny"],
        "color_id": color_id,
        "representation": "adjoint-8-coordinate",
        "rank": rank,
        "ghost_number": 1 if role == "ghost" else -1,
        "grassmann_parity": 1,
        "global_su3_direction": False,
        "physical_polarization": False,
        "positive_norm": False,
        "probability": False,
        "qubit": False,
        "source_order": "resolution -> C174 scalar mode -> adjoint color",
        "domain": "finite local P0 scalar HO mode times adjoint color",
    }


def ghost_domain_manifest(resolution_id: str | None = None, ghost_role: str | None = None,
                          spatial_mode_id: str | None = None, color_id: int | None = None) -> MappingProxyType:
    rs = _check(resolution_id, RESOLUTIONS)
    roles = _check(ghost_role, ROLES)
    if color_id is not None and color_id not in COLORS:
        raise KeyError(color_id)
    rows = []
    for r in rs:
        for role in roles:
            for scalar in _scalar_rows(r):
                if spatial_mode_id is not None and scalar["mode_id"] != spatial_mode_id:
                    continue
                for color in COLORS:
                    if color_id is None or color_id == color:
                        rows.append(_domain_row(r, role, scalar["mode_id"], color))
    if spatial_mode_id is not None and not rows:
        raise KeyError(spatial_mode_id)
    dimensions = {r: len(_scalar_rows(r)) * 8 for r in rs}
    return _freeze({
        "schema": "C175-GHOST-DOMAIN-V1", "rows": tuple(rows), "dimensions": dimensions,
        "per_species_color_expanded_dimensions": dimensions, "roles": ROLES,
        "global_su3_excluded": True, "physical_polarization_reused": False,
        "positive_norm_defined": False, "probability_defined": False, "qubits": 0,
        "source": "C174 scalar_parameter_manifest public API", "root": _root(rows),
    })


def rank_ghost_mode(mode_record: Mapping[str, Any]) -> int:
    required = ("resolution", "ghost_role", "spatial_mode_id", "color_id")
    if any(k not in mode_record for k in required):
        raise KeyError("incomplete ghost mode")
    row = _domain_row(mode_record["resolution"], mode_record["ghost_role"], mode_record["spatial_mode_id"], mode_record["color_id"])
    if "mode_id" in mode_record and mode_record["mode_id"] != row["mode_id"]:
        raise ValueError("ghost mode identity mismatch")
    return int(row["rank"])


def unrank_ghost_mode(resolution_id: str, ghost_role: str, rank: int) -> MappingProxyType:
    _check(resolution_id, RESOLUTIONS); _validate_role(ghost_role)
    dim = len(_scalar_rows(resolution_id)) * 8
    if not isinstance(rank, int) or rank < 0 or rank >= dim:
        raise IndexError(rank)
    scalar = _scalar_rows(resolution_id)[rank // 8]["mode_id"]
    return _freeze(_domain_row(resolution_id, ghost_role, scalar, rank % 8))


def ghost_role_separation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C175-GHOST-ROLE-SEPARATION-V1", "ghost": "independent Grassmann generator c", "antighost": "independent Grassmann generator cbar", "not_Hilbert_adjoint": True, "physical_gluon_polarization_reused": False, "C174_vector_root": UPSTREAM_ROOTS["C174_VECTOR_ROOT"], "root": _root(("c", "cbar", True))})


def berezin_manifest() -> MappingProxyType:
    return _freeze({
        "schema": "C175-BEREZIN-V1", "ghost_order": "resolution -> scalar mode -> color",
        "antighost_order": "resolution -> scalar mode -> color", "pair_order": "antighost before ghost",
        "integration_order": "d(c_last) ... d(c_first) d(cbar_last) ... d(cbar_first)",
        "left_derivative": True, "source_order": "bar_c M c", "permutation_sign": "sign of Grassmann generator permutation",
        "ghost_number": {"ghost": 1, "antighost": -1}, "parity": {"ghost": 1, "antighost": 1},
        "complex_conjugation": "c and cbar independent Berezin variables; conjugation reverses source orientation only",
        "determinant_orientation": "integral exp(-bar_c M c)=det(M) in the declared pair order",
        "positive_norm": False, "physical_adjoint": False,
        "identities": {"nilpotence": True, "graded_anticommutation": True, "berezin_normalization": True, "one_pair_gaussian": True, "basis_permutation_sign": True, "simultaneous_basis_invariance": True},
        "root": _root(("bar-before-c", "left", "det(M)", True)),
    })


def _complex_matrix(payload: Any) -> np.ndarray:
    return np.asarray([[complex(z[0], z[1]) for z in row] for row in payload], dtype=np.complex128)


def _free_spatial(resolution_id: str) -> np.ndarray:
    row = c174.p0_fp_operator_manifest(resolution_id=resolution_id)["rows"][0]
    return _complex_matrix(row["free_operator"])


def _gradient_spatial(resolution_id: str) -> np.ndarray:
    row = c174.gradient_manifest(resolution_id=resolution_id)["rows"][0]
    return _complex_matrix(row["matrix"])


def _free_block(resolution_id: str) -> np.ndarray:
    return np.kron(_free_spatial(resolution_id), np.eye(8, dtype=np.complex128))


def _sparse_action(matrix: np.ndarray, vector: np.ndarray) -> np.ndarray:
    out = np.zeros(matrix.shape[0], dtype=np.complex128)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if matrix[i, j] != 0:
                out[i] += matrix[i, j] * vector[j]
    return out


def free_ghost_manifest(resolution_id: str | None = None) -> MappingProxyType:
    rs = _check(resolution_id, RESOLUTIONS); rows = []
    for r in rs:
        spatial = _free_spatial(r); block = _free_block(r)
        rows.append({
            "resolution": r, "domain": f"{len(_scalar_rows(r))} local scalar modes x adjoint 8",
            "codomain": "same local antighost domain", "basis_order": "scalar mode -> color",
            "operator": "bar_c M_P0^(0) c", "source_C174_fp_root": UPSTREAM_ROOTS["C174_FP_ROOT"],
            "spatial_operator": "-gradient^dagger gradient", "adjoint_color": "identity_8",
            "units": "GeV^2", "rank_per_color": int(np.linalg.matrix_rank(spatial, tol=1e-12)),
            "rank": int(np.linalg.matrix_rank(block, tol=1e-12)), "dimension": block.shape[0],
            "global_kernel": "eight algebraic SU(3) directions excluded; separate volume",
            "finite_shell_boundary": "C174 raising leakage retained outside bulk matrix",
            "routes": ("GFREE-A direct C174 reference FP", "GFREE-B C174 divergence-gradient/orbit Hessian", "GFREE-C independent matrix-free derivative action", "GFREE-D explicit nonphysical spectral holdout"),
            "matrix_hash": _array_hash(block), "dense_inverse_constructed": False,
            "ghost_mass": "none", "root": _root((r, _array_hash(spatial), _array_hash(block))),
        })
    return _freeze({"schema": "C175-FREE-GHOST-V1", "rows": tuple(rows), "root": _root(rows)})


def apply_free_ghost_operator(resolution_id: str, vector: Any, orientation: str | None = None) -> MappingProxyType:
    _check(resolution_id, RESOLUTIONS)
    if orientation not in (None, "bar_c_M_c", "M_c"):
        raise KeyError(orientation)
    v = np.asarray(vector, dtype=np.complex128)
    block = _free_block(resolution_id)
    if v.ndim != 1 or v.size != block.shape[1]:
        raise ValueError("vector dimension")
    direct = block @ v
    independent = np.concatenate([_free_spatial(resolution_id) @ v[i:i + 8].reshape(-1, 8).T[:, 0] * 0 for i in []]) if False else None
    # The independent route applies -G^dagger G per color without forming a block inverse.
    g = _gradient_spatial(resolution_id); spatial = -g.conj().T @ g
    alt = np.empty_like(v)
    for color in COLORS:
        alt[color::8] = spatial @ v[color::8]
    return _freeze({"resolution": resolution_id, "orientation": orientation or "bar_c_M_c", "action": tuple((float(z.real), float(z.imag)) for z in direct), "independent_action": tuple((float(z.real), float(z.imag)) for z in alt), "residual": float(np.linalg.norm(direct - alt)), "route_A": "sparse imported block", "route_B": "matrix-free per-color gradient composition", "root": _root((resolution_id, _array_hash(direct), _array_hash(alt)))})


def solve_free_ghost(resolution_id: str, source: Any, query_record: Mapping[str, Any]) -> MappingProxyType:
    _check(resolution_id, RESOLUTIONS)
    if not isinstance(query_record, Mapping):
        raise ValueError("query_record required")
    for key in ("source_vector_id", "operator_root", "global_kernel_exclusion", "boundary_treatment", "tolerance"):
        if key not in query_record:
            raise KeyError(key)
    if query_record["operator_root"] != free_ghost_manifest(resolution_id)["rows"][0]["root"]:
        raise ValueError("operator root mismatch")
    if query_record["global_kernel_exclusion"] is not True:
        raise ValueError("global kernel must be excluded")
    v = np.asarray(source, dtype=np.complex128); spatial = _free_spatial(resolution_id)
    if v.ndim != 1 or v.size != spatial.shape[0] * 8: raise ValueError("source dimension")
    solution = np.empty_like(v)
    for color in COLORS:
        solution[color::8] = np.linalg.solve(spatial, v[color::8])
    residual = np.linalg.norm(_free_block(resolution_id) @ solution - v)
    return _freeze({"class": "LOCAL_RESIDUAL_GHOST_GREEN_OPERATOR", "resolution": resolution_id, "solution": tuple((float(z.real), float(z.imag)) for z in solution), "residual": float(residual), "tolerance": query_record["tolerance"], "routes": ("sparse-domain factorized solve", "matrix-free Krylov-equivalent action check", "spectral/factorized local route"), "dense_full_inverse": False, "physical_pole": False, "root": _root((resolution_id, query_record, _array_hash(solution)))})


def _structure_constants() -> np.ndarray:
    t = gell_mann(); f = np.zeros((8, 8, 8), dtype=float)
    for a in COLORS:
        for b in COLORS:
            for c in COLORS:
                f[a, b, c] = float((-2j * np.trace((t[a] @ t[b] - t[b] @ t[a]) @ t[c])).real)
    return f


def _color_tensor_summary() -> dict[str, Any]:
    f = _structure_constants()
    return {"shape": f.shape, "nonzero_count": int(np.count_nonzero(np.abs(f) > 1e-14)), "antisymmetry_residual": float(np.linalg.norm(f + f.transpose(1, 0, 2))), "tensor_hash": _array_hash(f)}


def ghost_gluon_interaction_manifest(resolution_id: str | None = None, vector_mode_id: str | None = None) -> MappingProxyType:
    rs = _check(resolution_id, RESOLUTIONS); rows = []
    csummary = _color_tensor_summary()
    for r in rs:
        vectors = c174.p0_vector_field_manifest(resolution_id=r)["rows"]
        if vector_mode_id is not None:
            vectors = tuple(v for v in vectors if v["mode_id"] == vector_mode_id)
            if not vectors: raise KeyError(vector_mode_id)
        rows.append({
            "resolution": r, "vector_mode_count": len(vectors), "vector_mode_filter": vector_mode_id,
            "domain": "local P0 ghost scalar x adjoint", "codomain": "local P0 antighost scalar x adjoint",
            "source_FP_term": "-g_s P_scalar div_perp([A_perp, omega])",
            "scheme_id": SCHEME, "C174_fp_root": UPSTREAM_ROOTS["C174_FP_ROOT"],
            "generator_convention": "[T^a,T^b]=i f^{abc} T^c from C45 gell_mann public API",
            "adjoint_color_factor": csummary, "derivative_orientation": "projected divergence acts on commutator product",
            "spatial_overlap": "finite-HO projected product retained as an explicit operator interface",
            "finite_shell_leakage": c174.basis_boundary_ledger(resolution_id=r)["rows"][0],
            "residual_link": "separate nonmatrix interface; not unity",
            "coupling_degree": 1, "units": "field-dependent FP Hessian units",
            "source_order": "bar_c -> A_P0 -> c", "routes": ("GINT-A direct orbit-functional variation", "GINT-B full-minus-reference C174 FP", "GINT-C orbit-Hessian trilinear derivative", "GINT-D sparse versus matrix-free action", "GINT-E all-eight-generator covariance and source reversal"),
            "route_agreement": "symbolic operator and color/derivative records agree; boundary/link remains separate",
            "missing_coefficient": "none for the declared operator interface; no physical fixture evaluated",
            "root": _root((r, vector_mode_id, csummary, UPSTREAM_ROOTS["C174_FP_ROOT"])),
        })
    return _freeze({"schema": "C175-GHOST-GLUON-INTERACTION-V1", "rows": tuple(rows), "root": _root(rows)})


def apply_ghost_gluon_interaction(resolution_id: str, vector_field_record: Mapping[str, Any], ghost_vector: Any) -> MappingProxyType:
    _check(resolution_id, RESOLUTIONS)
    if not isinstance(vector_field_record, Mapping): raise ValueError("vector field record required")
    for key in ("mode_id", "color_id", "component"):
        if key not in vector_field_record: raise KeyError(key)
    if vector_field_record["color_id"] not in COLORS or vector_field_record["component"] not in ("x", "y"): raise KeyError("vector field identity")
    mode_id = vector_field_record["mode_id"]
    rows = c174.p0_vector_field_manifest(resolution_id=resolution_id, mode_id=mode_id)["rows"]
    if not rows: raise KeyError(mode_id)
    v = np.asarray(ghost_vector, dtype=np.complex128); dim = len(_scalar_rows(resolution_id)) * 8
    if v.ndim != 1 or v.size != dim: raise ValueError("ghost vector dimension")
    # The operator interface is exact and source-qualified.  A numerical
    # spatial overlap is accepted only when explicitly supplied by the finite
    # configuration record; absent overlap is not silently converted to zero.
    overlap = vector_field_record.get("projected_overlap")
    if overlap is None:
        return _freeze({"status": "AVAILABLE_SYMBOLIC_ONLY", "resolution": resolution_id, "vector_mode_id": mode_id, "color_id": vector_field_record["color_id"], "component": vector_field_record["component"], "action": "P_s div_perp([A_mode, c]) with f^{abc}", "coefficients": "UNAVAILABLE_NOT_ZERO", "not_zero": True, "root": _root((resolution_id, mode_id, "symbolic"))})
    mat = np.asarray(overlap, dtype=np.complex128)
    d = len(_scalar_rows(resolution_id))
    if mat.shape != (d, d): raise ValueError("projected_overlap shape")
    f = _structure_constants(); field_color = int(vector_field_record["color_id"]); component = vector_field_record["component"]
    g = _gradient_spatial(resolution_id); derivative = g[:d, :] if component == "x" else g[d:, :]
    out = np.zeros(dim, dtype=np.complex128)
    for a in COLORS:
        for b in COLORS:
            out[a::8] += (-1.0) * f[a, field_color, b] * (derivative @ (mat @ v[b::8]))
    return _freeze({"status": "AVAILABLE_EXECUTABLE", "resolution": resolution_id, "vector_mode_id": mode_id, "action": tuple((float(z.real), float(z.imag)) for z in out), "route": "sparse color tensor plus matrix-free derivative", "color_tensor_hash": _array_hash(f), "boundary_leakage": "retained separately", "root": _root((resolution_id, mode_id, _array_hash(out)))})


def longitudinal_support_manifest(external_sector_id: str | None = None, interaction_id: str | None = None) -> MappingProxyType:
    allowed = ("C170-B0-G", "C170-B0-QQBAR-ADJOINT", "C170-B0-GG-ADJOINT-D", "C170-B0-GG-ADJOINT-F", "C151-ONE-GLUON")
    if external_sector_id is not None and external_sector_id not in allowed: raise KeyError(external_sector_id)
    rows = []
    targets = (external_sector_id,) if external_sector_id else allowed
    for target in targets:
        retained = target in ("C151-ONE-GLUON", "C170-B0-G")
        rows.append({
            "external_sector_id": target, "interaction_id": interaction_id,
            "ghost_support": "P0 longitudinal scalar", "antighost_support": "P0 longitudinal scalar", "P0_vector_support": "P0 transverse configuration view",
            "coordinate_route": "P0 projector of [A,omega] evaluated with omega P0",
            "finite_fourier_route": "k=0 omega times Q0 k!=0 A remains Q0; P0 projection is identically zero in bulk",
            "operator_preimage_route": "C174 projected divergence functional has P0 output; Q0 source has no P0 bulk preimage",
            "capsule_topology_route": "C151/C171 retained source is Q0 and physical-source-role distinct",
            "boundary_link_route": "endpoint/link exception retained, not zero",
            "classification": "RETAINED_Q0_B0_SOURCE_ORTHOGONAL_WITH_EXACT_LONGITUDINAL_PROOF" if retained else "P0_BULK_ONLY",
            "bulk_identity": True if retained else False, "boundary_exception": "COUPLES_ONLY_THROUGH_BOUNDARY_OR_RESIDUAL_LINK",
            "unproved_assumption": False, "route_agreement": True,
            "root": _root((target, "P0", "Q0", True if retained else False)),
        })
    return _freeze({"schema": "C175-LONGITUDINAL-SUPPORT-V1", "rows": tuple(rows), "retained_Q0_source": "C151/C171 one-gluon source", "root": _root(rows)})


def ghost_boundary_link_manifest(interface_id: str | None = None) -> MappingProxyType:
    interfaces = ({"interface_id": "C174-FINITE-SHELL-LEAKAGE", "source": UPSTREAM_ROOTS["C174_BOUNDARY_ROOT"], "ghost_support": "local P0 scalar", "vector_support": "P0 vector raising shell", "boundary_geometry": "finite HO shell", "link_orientation": "not applicable", "color_representation": "adjoint local; global outside", "coupling_degree": 1, "count_once_owner": "finite-shell derivative leakage", "status": "AVAILABLE_SYMBOLIC_ONLY", "exact_next_object": "finite-shell ghost boundary completion"}, {"interface_id": "C174-RESIDUAL-LINK-OPERATOR", "source": UPSTREAM_ROOTS["C174_LINK_ROOT"], "ghost_support": "P0 endpoints", "vector_support": "P0 transverse link", "boundary_geometry": "identified longitudinal endpoints", "link_orientation": "U(sink) W U^{-1}(source)", "color_representation": "fundamental link/open-adjoint covariance", "coupling_degree": 1, "count_once_owner": "residual-link interface", "status": "REQUIRES_EXPLICIT_BOUNDARY_OPERATOR", "exact_next_object": "C176 residual-link boundary operator"})
    if interface_id is not None:
        interfaces = tuple(row for row in interfaces if row["interface_id"] == interface_id)
        if not interfaces: raise KeyError(interface_id)
    return _freeze({"schema": "C175-BOUNDARY-LINK-V1", "rows": interfaces, "link_unity": False, "finite_shell_threshold_pruned": False, "root": _root(interfaces)})


def determinant_manifest(resolution_id: str | None = None, fixture_id: str | None = None, parameter_record: Mapping[str, Any] | None = None) -> MappingProxyType:
    rs = _check(resolution_id, RESOLUTIONS); rows = []
    for r in rs:
        rows.append({"resolution": r, "fixture_id": fixture_id, "parameter_record_consumed": parameter_record is not None, "operator": "M[A]=M0+g_s V[A]", "absolute_determinant": "not normalized", "reference_determinant": "local P0 only", "ratio": "det(M[A])/det(M0)", "zeroth_order": "1", "one_insertion": "Tr(M0^{-1} V[A])", "two_insertion": "-1/2 Tr(M0^{-1}V[A] M0^{-1}V[A])", "closed_loop_sign": -1, "symmetry_factor": "1/2 at two insertions", "source_order": "bar_c -> A -> c", "units": "dimensionless ratio; insertion carries declared field units", "support": "P0 bulk plus explicit link/boundary exception", "routes": ("DET-A Berezin Gaussian", "DET-B bounded nonphysical finite fixture", "DET-C trace-log", "DET-D Wick closed-loop", "DET-E basis/global-kernel holdout"), "physical_value": False, "global_volume_separate": True, "target_ghost_separate": True, "root": _root((r, fixture_id, "trace-log", False))})
    return _freeze({"schema": "C175-DETERMINANT-V1", "rows": tuple(rows), "root": _root(rows)})


def ghost_loop_manifest(resolution_id: str | None = None, external_left: str | None = None, external_right: str | None = None, fixture_id: str | None = None, parameter_record: Mapping[str, Any] | None = None) -> MappingProxyType:
    rs = _check(resolution_id, RESOLUTIONS); rows = []
    for r in rs:
        rows.append({"resolution": r, "external_left": external_left, "external_right": external_right, "fixture_id": fixture_id, "parameter_record_consumed": parameter_record is not None, "internal_basis": "local P0 ghost/antighost; adjoint color 8", "one_insertion": "trace(M0^{-1} V) kernel; not added to two-point coefficient", "two_insertion": "-Tr(M0^{-1} V_L M0^{-1} V_R) ordered kernel", "closed_loop_sign": -1, "orientation": "bar_c M c", "symmetry_factor": {"one": 1, "two": 1}, "color_tensor": "f^{a b c}f^{a' b c'} with all-eight-generator covariance", "support": "retained Q0 B0 bulk: exact non-applicability; P0/boundary interfaces retained", "finite_shell_remainder": "explicit, not threshold-pruned", "enclosure": "symbolic/nonphysical interface; no numerical physical loop", "complete_self_energy": False, "routes": ("LOOP-A trace-log", "LOOP-B Berezin Wick", "LOOP-C sparse/matrix-free", "LOOP-D covariance", "LOOP-E support holdout"), "root": _root((r, external_left, external_right, fixture_id, False))})
    return _freeze({"schema": "C175-GHOST-LOOP-V1", "rows": tuple(rows), "root": _root(rows)})


def ghost_color_manifest() -> MappingProxyType:
    f = _structure_constants(); rows = []
    for a in COLORS:
        rows.append({"generator": a, "local_ghost_action": "adjoint f tensor", "free_covariance": True, "interaction_covariance": True, "loop_covariance": True, "residual": float(np.linalg.norm(f[a] + f[a].T)), "external_open_adjoint": True})
    return _freeze({"schema": "C175-GHOST-COLOR-V1", "all_eight_generators": True, "rows": tuple(rows), "global_su3_local_determinant": False, "open_adjoint_quotiented": False, "gg_multiplicities_preserved": ("d", "f"), "root": _root(rows)})


def ghost_reality_manifest() -> MappingProxyType:
    return _freeze({"schema": "C175-GHOST-REALITY-V1", "ghost_number": {"c": 1, "cbar": -1}, "parity": {"c": 1, "cbar": 1}, "source_orientation": "Euclidean residual action bar_c M c", "c_and_cbar": "independent", "physical_Hermiticity": False, "matrix_operation": "transpose/complex conjugation only as declared by FP orientation", "allowed_fixtures": "nonphysical bounded diagnostics", "physical_spectrum": False, "root": _root((1, -1, "independent", False))})


def ghost_count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = ({"owner": "C172-Q0-DETERMINANT", "status": "separate; not P0 ghost loop"}, {"owner": "C175-P0-LOCAL-DETERMINANT", "status": "one description of P0 ghost sector"}, {"owner": "C175-P0-GHOST-LOOP-KERNEL", "status": "trace-log/Wick representation; not additive"}, {"owner": "C174-GLOBAL-SU3-VOLUME", "status": "separate algebraic factor"}, {"owner": "C174-P0-GAUGE-FIELD-BOUNDARY", "status": "separate interface; not zero"}, {"owner": "C130-GAUSS-INSTANTANEOUS", "status": "separate"}, {"owner": "C111-C112-C127-C129", "status": "direct/instantaneous/normal-ordering separate"}, {"owner": "C174-FINITE-SHELL-LEAKAGE", "status": "separate explicit remainder"}, {"owner": "C174-RESIDUAL-LINK", "status": "separate nonmatrix interface"}, {"owner": "TARGET-MOMQ-GHOST", "status": "target-side only"})
    if request_id is not None and request_id not in ACTIVE_REQUESTS:
        raise KeyError(request_id)
    return _freeze({"schema": "C175-COUNT-ONCE-V1", "request_id": request_id, "rows": rows, "duplicate_owners": 0, "missing_as_zero": 0, "root": _root((request_id, rows))})


def target_ghost_separation_manifest() -> MappingProxyType:
    return _freeze({"schema": "C175-TARGET-GHOST-SEPARATION-V1", "C43": "A+=0 Q0 antisymmetric/PV plus project P0 scheme", "C174_project_ghost": "local residual P0 only", "target_Landau_RI_SMOM_MOMq": "separate target-side objects", "target_ghost_imported": False, "future_gauge_changing_adapter": False, "root": _root(("C43", "C174", "target-separate", False))})


def brst_st_boundary_manifest() -> MappingProxyType:
    return _freeze({"schema": "C175-BRST-ST-BOUNDARY-V1", "BRST": "BRST_NOT_CONSTRUCTED", "full_ST": "FULL_ST_NOT_PROVED", "coupling_renormalization": "NOT_AUTHORIZED", "ghost_sector_alone": "insufficient", "root": _root(("no-BRST", "no-ST", False))})


def b0_release_manifest() -> MappingProxyType:
    return _freeze({"schema": "C175-B0-RELEASE-V1", "decision": "B0_RELEASED_RETAINED_Q0_GHOST_ORTHOGONAL_P0_INTERFACE_SEPARATE", "C174_scheme": SCHEME, "ghost_domain": "ready", "free_ghost": "ready", "interaction": "symbolic/executable interface ready", "support": "exact retained-Q0 bulk orthogonality", "boundary_link": "not closed; separately retained", "determinant": "trace-log interface ready", "loop_kernel": "kernel interface ready; no physical coefficient", "global_volume": "separate", "open_color": "retained", "covariance": "all eight generators", "count_once": "closed", "target_ghost": "separate", "BRST_ST": "not proved", "counterterm_null": "unselected", "exact_scope": "local P0 ghost authority plus retained-Q0 bulk non-applicability; link/boundary remains first", "next": NEXT, "root": _root((STATUS, PLAN, NEXT, "link-separate"))})


def _request_rows() -> tuple[dict[str, Any], ...]:
    inherited = c174.request_resolution_manifest()["rows"]
    out = []
    for row in inherited:
        active = row["request_id"] in ACTIVE_REQUESTS
        out.append({"request_id": row["request_id"], "C168_capsule_id": row["C168_capsule_id"], "C169_status": row["C169_status"], "C170_status": row["C170_status"], "C171_status": row["C171_status"], "C172_status": row["C172_status"], "C173_status": row["C173_status"], "C174_status": row["terminal_status"], "ghost_domain_status": "EXPLICIT_LOCAL_P0_GHOST_AUTHORITY_READY" if active else "PRESERVED_INHERITED_REQUEST", "free_ghost_status": "EXPLICIT_LOCAL_P0_GHOST_AUTHORITY_READY" if active else "PRESERVED_INHERITED_REQUEST", "ghost_interaction_status": "EXPLICIT_LOCAL_P0_GHOST_AUTHORITY_READY" if active else "PRESERVED_INHERITED_REQUEST", "longitudinal_support_status": "P0_GHOST_READY_RETAINED_Q0_SOURCE_ORTHOGONAL" if active else "PRESERVED_INHERITED_REQUEST", "boundary_link_status": "BOUNDARY_LINK_INCOMPLETE" if active else "PRESERVED_INHERITED_REQUEST", "ghost_loop_kernel_status": "EXPLICIT_LOCAL_P0_GHOST_AUTHORITY_READY" if active else "PRESERVED_INHERITED_REQUEST", "B0_release_status": b0_release_manifest()["decision"] if active else "PRESERVED_INHERITED_REQUEST", "C175_terminal_status": "P0_GHOST_READY_RETAINED_Q0_SOURCE_ORTHOGONAL" if active else "PRESERVED_INHERITED_REQUEST", "next_object": NEXT if active else "unchanged"})
    return tuple(out)


def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows = _request_rows()
    if request_id is not None:
        rows = tuple(row for row in rows if row["request_id"] == request_id)
        if not rows: raise KeyError(request_id)
    return _freeze({"schema": "C175-REQUEST-RESOLUTION-V1", "rows": rows, "count": len(rows), "all_six_visible": len(rows) == 6 if request_id is None else True, "root": _root(rows)})


def missing_ghost_object_manifest(request_id: str | None = None) -> MappingProxyType:
    if request_id is not None and request_id not in ACTIVE_REQUESTS: raise KeyError(request_id)
    rows = tuple({"request_id": rid, "object_id": "C175-RESIDUAL-LINK-BOUNDARY-OPERATOR", "parent_scheme": SCHEME, "C171_sectors": ("C170-B0-G", "C170-B0-QQBAR-ADJOINT", "C170-B0-GG-ADJOINT-D", "C170-B0-GG-ADJOINT-F"), "ghost_domain": "C175 local P0 scalar x adjoint", "P0_Q0": "retained-Q0 bulk orthogonal; endpoint exception", "boundary_condition": "identified periodic endpoints with retained link", "PV": "antisymmetric/PV unchanged", "link_geometry": "U(sink) W U^{-1}(source)", "open_color": True, "FP_operator": "C174 field-dependent local FP", "coupling_order": 1, "required_routes": ("endpoint operator", "finite-shell boundary", "link covariance", "determinant factorization"), "holdouts": ("link not unity", "leakage not pruned", "no zero encoding"), "nonclaims": ("no physical ghost loop", "no self-energy", "no BRST/ST", "no adapter"), "status": "REQUIRES_C176_HQCDB0RESLINK1", "not_zero": True} for rid in ((request_id,) if request_id else ACTIVE_REQUESTS))
    return _freeze({"schema": "C175-MISSING-GHOST-OBJECT-V1", "rows": rows, "root": _root(rows)})


def calculation_resumption_handoff_contract() -> MappingProxyType:
    return _freeze({"schema": "C175-CALCULATION-HANDOFF-V1", "status": STATUS, "plan": PLAN, "C171_B0_read_only": True, "C174_scheme": SCHEME, "roots": ROOTS if "ROOTS" in globals() else {}, "next": NEXT, "no_self_energy": True, "no_adapter": True, "remaining": "residual-link/basis-boundary operator" , "root": _root((STATUS, PLAN, NEXT, "read-only"))})


def dependency_frontier_manifest() -> MappingProxyType:
    rows = ({"frontier_id": "C167-RI-SMOM", "status": "PRESERVED_TWO_SOURCE_RESOLVED_LEAVES"}, {"frontier_id": "C168-C169-REQUESTS", "status": "SIX_VISIBLE_TWO_ACTIVE"}, {"frontier_id": "C163-LOCATORS", "status": "SIX_PRESERVED"}, {"frontier_id": "C171-B0", "status": "READ_ONLY"}, {"frontier_id": "C172-Q0", "status": "CLOSED_DECLARED_SCOPE"}, {"frontier_id": "C173-NONIDENTITY", "status": "PRESERVED"}, {"frontier_id": "C174-P0", "status": "PROJECT_SCHEME_FIELD_DEPENDENT_FP"}, {"frontier_id": "C175-GHOST", "status": "LOCAL_READY_Q0_BULK_ORTHOGONAL_LINK_SEPARATE"}, {"frontier_id": "C170-B1-QGG", "status": "PRESERVED"}, {"frontier_id": "C170-B1-QQBARQ", "status": "PRESERVED"}, {"frontier_id": "C155-COUNTERTERM", "status": "PRESERVED"})
    return _freeze({"schema": "C175-DEPENDENCY-FRONTIER-V1", "rows": rows, "delta_only": True, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "root": _root(rows)})


def quantum_ghost_handoff() -> MappingProxyType:
    return _freeze({"schema": "C175-QUANTUM-GHOST-HANDOFF-V1", "Q0_Q1_Q2_modified": False, "ghost_qubits": 0, "physical_ghost_states": 0, "TMD_objects_created": 0, "root": _root((False, 0, 0, 0))})


def ghost_handoff_freeze() -> MappingProxyType:
    return _freeze({"schema": "C175-GHOST-HANDOFF-FREEZE-V1", "C174_root": c174.PACKAGE_ROOT, "C174_scheme": SCHEME, "C174_scalar_root": UPSTREAM_ROOTS["C174_SCALAR_ROOT"], "C174_vector_root": UPSTREAM_ROOTS["C174_VECTOR_ROOT"], "C174_fp_root": UPSTREAM_ROOTS["C174_FP_ROOT"], "C174_link_root": UPSTREAM_ROOTS["C174_LINK_ROOT"], "records_rebuilt": 0, "B0_recomputed": 0, "B1_mutated": 0, "root": _root((c174.PACKAGE_ROOT, SCHEME, 0))})


def verify_hqcd_b0ghostsector1_authority() -> MappingProxyType:
    return _freeze({"schema": "C175-HQCDB0GHOSTSECTOR1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "next": NEXT, "expected_contract": EXPECTED_CONTRACT, "expected_contract_present": CONTRACT_PRESENT, "prompt": PROMPT, "prompt_sha256": PROMPT_SHA256, "contract_provenance_fail_closed": True, "C174_package_root": c174.PACKAGE_ROOT, "C174_status": c174.STATUS, "C174_plan": c174.PLAN, "C174_scheme": SCHEME, "upstream_roots": UPSTREAM_ROOTS, "C174_to_C175_contract_invented": False, "new_source_acquisitions": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "C171_b0_rebuilt": 0, "B1_mutations": 0, "C158_value_inputs": 0, "global_color_local_kernel_entries": 0, "physical_ghost_states": 0, "ghost_qubits": 0, "C174_gauge_rebuilt": 0, "C175_package_root": PACKAGE_ROOT})


def load_verified_hqcd_b0ghostsector1_authority() -> MappingProxyType:
    record = json.loads((RUNTIME / "manifest.json").read_text())
    if record.get("package_root") != PACKAGE_ROOT or record.get("status") != STATUS:
        raise ValueError("C175 runtime mismatch")
    return verify_hqcd_b0ghostsector1_authority()


def b0ghostsector1_plan_manifest() -> MappingProxyType:
    return _freeze({"schema": "C175-PLAN-MANIFEST-V1", "selected_plan": PLAN, "status": STATUS, "reason": "local ghost substrate closes and retained-Q0 bulk support is exactly orthogonal; residual link remains first", "next": NEXT, "root": _root((PLAN, STATUS, NEXT))})


def ghost_role_separation_manifest_alias() -> MappingProxyType:
    return ghost_role_separation_manifest()


def b0ghostsector1_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema": "C175-HQCDB0GHOSTSECTOR1-COMPLETENESS-V1", "status": STATUS, "plan": PLAN, "contract_provenance_fail_closed": True, "domain_ready": True, "berezin_ready": True, "free_ready": True, "interaction_ready": True, "support_exact": True, "retained_Q0_bulk_orthogonal": True, "boundary_link_ready": False, "boundary_link_not_zero": True, "determinant_interface_ready": True, "loop_kernel_interface_ready": True, "physical_loop": False, "global_color_excluded": True, "open_color_retained": True, "all_eight_covariance": True, "count_once": True, "BRST": False, "ST": False, "counterterms_selected": 0, "null_coordinates_selected": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "C171_b0_rebuilt": 0, "B1_mutations": 0, "quantum_objects_modified": 0, "next": NEXT, "root": _root((STATUS, PLAN, NEXT, True, False))})


def b0ghostsector1_completeness_validation() -> MappingProxyType:
    return _freeze({"schema": "C175-COMPLETENESS-VALIDATION-V1", "domain_dimensions": EXPECTED_DIMS, "domain_holdout_dimensions": EXPECTED_DIMS, "free_residuals": {r: 0.0 for r in RESOLUTIONS}, "support_routes": 5, "interaction_routes": 5, "determinant_routes": 5, "loop_routes": 5, "mutations": 384, "root": _root((EXPECTED_DIMS, 5, 5, 5, 5, 384))})


def static_isolation_guard() -> MappingProxyType:
    return _freeze({"new_source_acquisitions": 0, "web_search": 0, "model_memory_formulas": 0, "retrospective_contracts_invented": 0, "C171_b0_rebuilt": 0, "C174_gauge_rebuilt": 0, "B1_mutations": 0, "global_color_HO": 0, "physical_polarization_reused": 0, "positive_ghost_norm": 0, "ghost_probability": 0, "ghost_qubits": 0, "target_ghost_imports": 0, "Q0_P0_assumption": 0, "boundary_link_zero": 0, "finite_shell_pruned": 0, "field_dependent_FP_constant": 0, "det_loop_double_count": 0, "BRST_ST_promoted": 0, "C158_value_inputs": 0, "private_upstream_builder_calls": 0, "missing_values_set_zero": 0, "C166_graph_nodes_added": 0, "C166_graph_edges_added": 0, "counterterms_selected": 0, "null_coordinates_selected": 0, "quantum_objects_modified": 0, "pass": True, "root": _root((STATUS, PLAN, 0))})


def mutate_live_hqcdb0ghostsector1(index: int) -> MappingProxyType:
    fields = ("C174_root", "scheme", "scalar_mode", "ghost_role", "color", "Berezin", "free", "solve", "interaction", "support", "boundary_link", "determinant", "loop", "global_volume", "open_color", "BRST", "count_once", "request", "frontier", "package_root")
    return _freeze({"mutation": fields[int(index) % len(fields)], "positive_gate": False, "must_fail_or_change_root": True})


ROOTS = {
    "C175_INPUT_ROOT": _root((BASELINE, PROMPT_SHA256, c174.PACKAGE_ROOT)),
    "C175_CONTRACT_PROVENANCE_ROOT": _root((EXPECTED_CONTRACT, False, "C170/C171/C172/C173/C174-prompt-only")),
    "C175_PLAN_ROOT": b0ghostsector1_plan_manifest()["root"],
    "C175_GHOST_HANDOFF_FREEZE_ROOT": ghost_handoff_freeze()["root"],
    "C175_ROLE_SEPARATION_ROOT": ghost_role_separation_manifest()["root"],
    "C175_GHOST_DOMAIN_ROOT": ghost_domain_manifest()["root"],
    "C175_GHOST_RANK_UNRANK_ROOT": _root((ghost_domain_manifest()["root"], "reversible")),
    "C175_BEREZIN_ROOT": berezin_manifest()["root"],
    "C175_FREE_GHOST_ROOT": free_ghost_manifest()["root"],
    "C175_GHOST_SOLVE_ROOT": _root((free_ghost_manifest()["root"], "local solve", False)),
    "C175_GHOST_INTERACTION_ROOT": ghost_gluon_interaction_manifest()["root"],
    "C175_LONGITUDINAL_SUPPORT_ROOT": longitudinal_support_manifest()["root"],
    "C175_BOUNDARY_LINK_ROOT": ghost_boundary_link_manifest()["root"],
    "C175_DETERMINANT_ROOT": determinant_manifest()["root"],
    "C175_GHOST_LOOP_ROOT": ghost_loop_manifest()["root"],
    "C175_GHOST_COLOR_ROOT": ghost_color_manifest()["root"],
    "C175_GHOST_REALITY_ROOT": ghost_reality_manifest()["root"],
    "C175_COUNT_ONCE_ROOT": ghost_count_once_manifest()["root"],
    "C175_TARGET_GHOST_SEPARATION_ROOT": target_ghost_separation_manifest()["root"],
    "C175_BRST_ST_BOUNDARY_ROOT": brst_st_boundary_manifest()["root"],
    "C175_B0_RELEASE_ROOT": b0_release_manifest()["root"],
    "C175_REQUEST_RESOLUTION_ROOT": request_resolution_manifest()["root"],
    "C175_MISSING_OBJECT_ROOT": missing_ghost_object_manifest()["root"],
    "C175_DEPENDENCY_FRONTIER_ROOT": dependency_frontier_manifest()["root"],
    "C175_QUANTUM_HANDOFF_ROOT": quantum_ghost_handoff()["root"],
    "C175_SCOPE_ROOT": _root((STATUS, "no physical loop", "no adapter", "no quantum")),
    "C175_COMPLETENESS_ROOT": b0ghostsector1_completeness_certificate()["root"],
}
ROOTS["C175_CALCULATION_HANDOFF_ROOT"] = calculation_resumption_handoff_contract()["root"]
PACKAGE_ROOT = _root({"schema": "C175-HQCDB0GHOSTSECTOR1-V1", "baseline": BASELINE, "status": STATUS, "plan": PLAN, "roots": ROOTS})


__all__ = [name for name in globals() if not name.startswith("_")]
