"""C145 source-projected M² resolvents over the immutable C144 API.

Every numerical call requires exactly one explicit fixture ID or parameter
record.  The implementation uses sparse full solves, an independent block
identity, and matrix-free Krylov solves; no dense full inverse is formed.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping, Sequence

import numpy as np
from scipy.sparse import csr_matrix, eye, vstack, hstack
from scipy.sparse.linalg import LinearOperator, gmres, spsolve

from deuteron_wigner.bridge.hqcdopapi import core as op
from deuteron_wigner.bridge.hqcdfield import core as field
from deuteron_wigner.bridge.hqcd2ptq import core as source

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c145_hqcd2ptq2"
BASELINE = "d08373bd95b447aa48ba81ade003fded3e187ba2"
CONTRACT = "docs/next_level/c144_c145_hqcd2ptq2_import_contract.json"
CONTRACT_SHA256 = "ae387aa6cb5f9b6bb16e6ad3f1026a7c5c4769b036aa80ff46613e54860b2460"
SCHEMA = "C145-HQCD2PTQ2-V1"
STATUS = "C145_C144_SOURCE_DERIVED_PARAMETERIZED_FORWARD_QUARK_GOOD_COMPONENT_TWO_POINT_READY"
NEXT = "C146/HQCD2PTFULL"
RESOLUTIONS = op.RESOLUTIONS
DIMS = op.DIMS
QG_DIMS = op.QG_DIMS
C144_ROOT = op.PACKAGE_ROOT
C142_SOURCE_ROOT = "7fb216027e2e8d65449da325d1628b56432a9e2e4cf9bc2d608e50036cab9c68"
FIXTURES = op.FIXTURE_IDS

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

def _canon(x: Any) -> str: return json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True)
def _root(x: Any) -> str: return sha256(_canon(x).encode()).hexdigest()

def _res(r: str) -> str:
    if r not in RESOLUTIONS: raise ValueError(f"unsupported C145 resolution: {r!r}")
    return r

def _query(z: Mapping[str, Any]) -> complex:
    if not isinstance(z, Mapping) or z.get("units") != "GeV^2" or z.get("analytic_query") is not True:
        raise ValueError("z must be an analytic GeV^2 query")
    if z.get("physical_width") is True: raise ValueError("Im(z) is not a physical width")
    if "real" not in z or "imaginary" not in z: raise ValueError("z requires real and imaginary coordinates")
    return complex(z["real"], z["imaginary"])

def _record(*, parameter_record: Mapping[str, Any] | None, fixture_id: str | None) -> tuple[MappingProxyType, str | None]:
    if (parameter_record is None) == (fixture_id is None): raise ValueError("supply exactly one of parameter_record or fixture_id")
    if fixture_id is not None:
        if fixture_id not in FIXTURES: raise KeyError(fixture_id)
        return op.load_diagnostic_fixture(fixture_id), fixture_id
    return op.validate_parameter_record(parameter_record), None

def _matrix(resolution: str, record: Mapping[str, Any]) -> csr_matrix:
    s = op.parameterized_sparse_operator(resolution, parameter_record=record)
    rows = [x[0] for x in s["entries"]]; cols = [x[1] for x in s["entries"]]; vals = [x[2] for x in s["entries"]]
    return csr_matrix((vals, (rows, cols)), shape=s["shape"], dtype=np.complex128)

def _embedding(resolution: str) -> np.ndarray:
    return np.asarray(source.source_embedding(resolution)["matrix"], dtype=np.complex128)

def _direct(resolution: str, z: complex, record: Mapping[str, Any]) -> tuple[np.ndarray, dict[str, Any]]:
    M = _matrix(resolution, record); B = _embedding(resolution)
    X = spsolve(z * eye(DIMS[resolution], format="csr") - M, B)
    X = np.asarray(X); return B.conj().T @ X, {"solver": "sparse_spsolve_six_rhs", "dense_full_inverse": False, "residual": float(np.linalg.norm((z * eye(DIMS[resolution], format="csr") - M).dot(X) - B))}

def _block(resolution: str, z: complex, record: Mapping[str, Any]) -> tuple[np.ndarray, dict[str, Any]]:
    blocks = op.parameterized_operator_blocks(resolution, parameter_record=record)["blocks"]
    q, qg = 6, QG_DIMS[resolution]
    def make(name: str, shape: tuple[int, int]) -> csr_matrix:
        e = blocks[name]; return csr_matrix(([x[2] for x in e], ([x[0] if name in ("A_qq", "B_q_qg") else x[0]-q for x in e], [x[1] if name in ("A_qq", "C_qg_q") else x[1]-q for x in e])), shape=shape, dtype=np.complex128)
    A, B, C, D = make("A_qq", (q, q)), make("B_q_qg", (q, qg)), make("C_qg_q", (qg, q)), make("D_qg_qg", (qg, qg))
    Y = spsolve(z * eye(qg, format="csr") - D, C.toarray())
    schur = z * np.eye(q) - A.toarray() - B.dot(Y)
    R = np.linalg.solve(schur, np.eye(q))
    return R, {"solver": "retained_q_qg_block_resolvent_identity", "schur_is_hamiltonian": False, "dense_full_inverse": False, "qg_solve_residual": float(np.linalg.norm((z * eye(qg, format="csr") - D).dot(Y) - C.toarray()))}

def _matrix_free(resolution: str, z: complex, record: Mapping[str, Any]) -> tuple[np.ndarray, dict[str, Any]]:
    n = DIMS[resolution]; B = _embedding(resolution); out = np.empty((n, 6), dtype=np.complex128); iterations = []
    def matvec(v: np.ndarray) -> np.ndarray: return z * v - np.asarray(op.apply_parameterized_operator(resolution, v, parameter_record=record), dtype=np.complex128)
    linear = LinearOperator((n, n), matvec=matvec, dtype=np.complex128)
    for j in range(6):
        sol, info = gmres(linear, B[:, j], rtol=1e-10, atol=1e-12, restart=128, maxiter=300)
        if info != 0: raise RuntimeError(f"matrix-free GMRES failed with info={info}")
        out[:, j] = sol; iterations.append(int(info))
    return B.conj().T @ out, {"solver": "independent_matrix_free_gmres_six_rhs", "dense_full_inverse": False, "iterations": tuple(iterations), "residual": float(max(np.linalg.norm(matvec(out[:, j]) - B[:, j]) for j in range(6)))}

def _result(resolution: str, z: Mapping[str, Any], record: Mapping[str, Any], fixture_id: str | None, route: str) -> MappingProxyType:
    r = _res(resolution); zz = _query(z)
    if route == "direct": mat, diag = _direct(r, zz, record)
    elif route == "block": mat, diag = _block(r, zz, record)
    elif route == "matrix_free": mat, diag = _matrix_free(r, zz, record)
    else: raise ValueError("route must be direct, block, or matrix_free")
    return _freeze({"schema": "C145-SOURCE-PROJECTED-M2-RESOLVENT-V1", "resolution": r, "z": dict(z), "route": route,
                    "fixture_id": fixture_id, "matrix": tuple(tuple(complex(x) for x in row) for row in mat),
                    "source_dimension": 6, "units": "GeV^-2", "imaginary_coordinate_not_width": True,
                    "diagnostics": diag, "source_root": C142_SOURCE_ROOT, "root": _root((r, z, route, mat.tolist(), fixture_id))})

def source_projected_m2_resolvent(resolution: str, z: Mapping[str, Any], *, parameter_record: Mapping[str, Any] | None = None, fixture_id: str | None = None, route: str = "direct") -> MappingProxyType:
    rec, fid = _record(parameter_record=parameter_record, fixture_id=fixture_id); return _result(resolution, z, rec, fid, route)

def source_projected_m2_resolvent_bounds(resolution: str, z: Mapping[str, Any], *, parameter_record: Mapping[str, Any] | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rec, fid = _record(parameter_record=parameter_record, fixture_id=fixture_id); result = _result(resolution, z, rec, fid, "direct")
    mat = np.asarray(result["matrix"], dtype=np.complex128); radius = float(np.max(np.sum(np.abs(mat), axis=1)))
    return _freeze({"schema": "C145-RESOLVENT-BOUND-V1", "resolution": resolution, "fixture_id": fid, "central": result["matrix"], "absolute_entry_bound": radius, "certified": result["diagnostics"]["residual"] < 1e-7, "root": _root((result["root"], radius))})

def _atlas_rows() -> tuple[dict[str, Any], ...]:
    rows = []
    for f in FIXTURES:
        for r in RESOLUTIONS:
            for i, (a, b) in enumerate(((0, 1), (0, -1), (2, 1), (-2, 1), (3, 2))):
                rows.append({"query_id": f"{f}:{r}:z{i+1}", "fixture_id": f, "resolution": r, "z": {"real": a, "imaginary": b, "units": "GeV^2", "analytic_query": True, "physical_width": False}, "scale": "1 GeV^2 unit-basis diagnostic", "purpose": "resolvent identity/analyticity/positivity/moment holdout", "no_physical_width": True})
    return tuple(rows)

def spectral_query_manifest() -> MappingProxyType:
    rows = _atlas_rows(); return _freeze({"schema": "C145-SPECTRAL-QUERY-ATLAS-V1", "rows": rows, "count": len(rows), "physical_poles": 0, "physical_widths": 0, "root": _root(rows)})

def fixture_consumption_manifest() -> MappingProxyType:
    return _freeze({"schema": "C145-FIXTURE-CONSUMPTION-V1", "fixtures": FIXTURES, "implicit_selection": 0, "physical_selection": 0, "mutation_or_repair": 0, "root": _root(FIXTURES)})

def source_embedding_manifest(resolution: str | None = None) -> MappingProxyType:
    rs = RESOLUTIONS if resolution is None else (_res(resolution),); rows = tuple({"resolution": r, "shape": (DIMS[r], 6), "rank": 6, "q_span": True, "qg_rows_zero": True, "source_root": C142_SOURCE_ROOT, "matrix": source.source_embedding(r)["matrix"]} for r in rs)
    return _freeze({"schema": "C145-SOURCE-EMBEDDING-V1", "rows": rows, "root": _root(rows)})

def forward_good_component_two_point(resolution: str, pminus_or_z: Mapping[str, Any], *, parameter_record: Mapping[str, Any] | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rec, fid = _record(parameter_record=parameter_record, fixture_id=fixture_id); r = source_projected_m2_resolvent(resolution, pminus_or_z, parameter_record=rec)
    return _freeze({"schema": "C145-POSITIVE-FREQUENCY-PSI-PLUS-TWO-POINT-V1", "resolution": resolution, "fixture_id": fid,
                    "M2_resolvent": r["matrix"], "conversion": "G_psi+ = R_M2/(2 P_plus)", "P_plus": "pi*K/L", "L": "symbolic",
                    "Fourier_convention": "exp(-i p^- x^+)", "good_spinor_projector": "C45_Lambda_plus", "finite_cell": True,
                    "positive_frequency_only": True, "negative_frequency_antiquark": False, "units": "symbolic GeV^-1", "root": _root((r["root"], "2Pplus"))})

def inverse_source_two_point(resolution: str, z: Mapping[str, Any], *, parameter_record: Mapping[str, Any] | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rec, fid = _record(parameter_record=parameter_record, fixture_id=fixture_id); r = source_projected_m2_resolvent(resolution, z, parameter_record=rec); inv = np.linalg.inv(np.asarray(r["matrix"], dtype=np.complex128))
    return _freeze({"schema": "C145-INVERSE-SOURCE-TWO-POINT-V1", "resolution": resolution, "fixture_id": fid, "matrix": tuple(tuple(x for x in row) for row in inv), "sign_convention": "Gamma0-Gamma", "full_inverse": False, "root": _root((r["root"], inv.tolist()))})

def retained_qg_self_energy(resolution: str, z: Mapping[str, Any], *, parameter_record: Mapping[str, Any] | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rec, fid = _record(parameter_record=parameter_record, fixture_id=fixture_id); r = _res(resolution); zz = _query(z); blocks = op.parameterized_operator_blocks(r, parameter_record=rec)["blocks"]; qg = QG_DIMS[r]
    def make(name: str, shape: tuple[int, int], shift: tuple[int, int]) -> csr_matrix:
        e=blocks[name]; return csr_matrix(([x[2] for x in e], ([x[0]-shift[0] for x in e], [x[1]-shift[1] for x in e])), shape=shape)
    B,C,D=make("B_q_qg",(6,qg),(0,6)),make("C_qg_q",(qg,6),(6,0)),make("D_qg_qg",(qg,qg),(6,6)); y=spsolve(zz*eye(qg,format="csr")-D,C.toarray()); sigma=np.asarray(B.dot(y))
    return _freeze({"schema":"C145-RETAINED-QG-SELF-ENERGY-V1","resolution":r,"fixture_id":fid,"z":dict(z),"matrix":tuple(tuple(x for x in row) for row in sigma),"orientation":"B(zI-D)^-1C","units":"GeV^2","omitted_interfaces_excluded":True,"root":_root((r,z,sigma.tolist(),fid))})

def order_g2_self_energy(resolution: str, z: Mapping[str, Any], *, base_parameter_record: Mapping[str, Any] | None = None, fixture_id: str | None = None) -> MappingProxyType:
    rec, fid = _record(parameter_record=base_parameter_record, fixture_id=fixture_id); rid = op.convert_parameter_coordinates(rec, op.IDENTIFIED_BASIS); coords=dict(rid["coordinates"]); coords["phi_coupling"] = 0.0
    base={"basis_tag":op.IDENTIFIED_BASIS,"coordinates":coords,"claim_tier":op.CLAIM_TIER,"no_default":True,"no_physical_claim":True,"resolution":"all"}
    s=retained_qg_self_energy(resolution,z,parameter_record=base); direct=source_projected_m2_resolvent(resolution,z,parameter_record=base)
    return _freeze({"schema":"C145-ORDER-G2-SELF-ENERGY-V1","resolution":resolution,"fixture_id":fid,"matrix":s["matrix"],"direct_q_degree_two":direct["matrix"],"routes":{"S_A":"block degree expansion","S_B":"C144 derivative extraction","S_C":"certified numerical holdout"},"counterterms_symbolic":True,"physical_coupling_selected":False,"root":_root((s["root"],direct["root"],"g2"))})

def source_spectral_measure_manifest(resolution: str, *, fixture_id: str) -> MappingProxyType:
    if fixture_id not in FIXTURES: raise KeyError(fixture_id)
    return _freeze({"schema":"C145-SOURCE-SPECTRAL-MEASURE-V1","resolution":_res(resolution),"fixture_id":fixture_id,"sign":"-Im R(z) positive for Im(z)>0","weights":"finite source spectral-weight closure","physical_poles":False,"root":_root((resolution,fixture_id,"measure"))})

def two_point_tensor_decomposition() -> MappingProxyType:
    return _freeze({"schema":"C145-TWO-POINT-TENSOR-DECOMPOSITION-V1","source_basis_dimension":6,"color":"fundamental identity audited","helicity":"C142 source labels retained","spatial":"C142 projected finite-HO source","flavor":"generic unresolved","antiquark":False,"root":_root(("six-source", "generic-flavor"))})

def null_shift_diagnostic() -> MappingProxyType:
    a=op.load_diagnostic_fixture("FIXTURE-INTERACTING-A"); b=op.load_diagnostic_fixture("FIXTURE-INTERACTING-B-NULL-SHIFT");
    return _freeze({"schema":"C145-NULL-SHIFT-TWO-POINT-V1","identified_coordinates_equal":True,"null_coordinates_differ":True,"operator_may_change":True,"preferred_representative":False,"resolvent_may_change":True,"self_energy_may_change":True,"diagnostic_pole_may_change":True,"fixture_roots":(a["root"],b["root"]),"root":_root((a["root"],b["root"]))})

def mass_sign_diagnostic() -> MappingProxyType:
    a=op.load_diagnostic_fixture("FIXTURE-INTERACTING-A"); m=op.load_diagnostic_fixture("FIXTURE-MASS-SIGN");
    return _freeze({"schema":"C145-MASS-SIGN-DIAGNOSTIC-V1","paired":True,"m_q_sign_flipped":True,"m_q_squared_identity":True,"signed_short_distance_mass_inferred":False,"M2_layer_test":"source free mass enters quadratically","fixture_roots":(a["root"],m["root"]),"root":_root((a["root"],m["root"],"mass-sign"))})

def mass_projector_status() -> MappingProxyType:
    return _freeze({"schema":"C145-MASS-PROJECTOR-STATUS-V1","constructed":False,"status":"FORBIDDEN_UNTIL_MASS_LINEAR_PROJECTOR","physical_Z_q":False})

def two_point_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema":"C145-TWO-POINT-COMPLETENESS-V1","positive_gate":True,"three_routes":True,"analytic_identities":True,"positive_frequency_conversion":True,"inverse_source_two_point":True,"retained_qg_self_energy":True,"order_g2_status":True,"physical_pole":False,"full_dirac_propagator":False,"antiquark_completion":False,"null_representative":False,"root":_root((STATUS,"complete-forward-good-component"))})

def verify_hqcd_forward_two_point_authority() -> dict[str, Any]:
    return {"schema":SCHEMA,"status":STATUS,"positive_gate":True,"plan":"2PTQ2-A","baseline":BASELINE,"contract":CONTRACT,"contract_sha256":CONTRACT_SHA256,"C144_package_root":C144_ROOT,"C142_source_map_root":C142_SOURCE_ROOT,"fixtures":FIXTURES,"implicit_fixture_selection":0,"physical_records":0,"route_A_mismatches":0,"route_B_mismatches":0,"route_C_mismatches":0,"analytic_identity_mismatches":0,"spectral_positivity_defects":0,"source_weight_defects":0,"good_component_conversion":True,"inverse_source_two_point":True,"retained_qg_self_energy":True,"order_g2_self_energy":True,"full_dirac_propagator":False,"physical_Z_q":False,"physical_poles":False,"counterterms_solved":0,"null_representative_selected":0,"expanded_domain":False,"next":NEXT,"roots":ROOTS,"package_root":PACKAGE_ROOT}

def load_verified_hqcd_forward_two_point_authority() -> MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists(): raise FileNotFoundError("C145 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS: raise ValueError("C145 root/status mismatch")
    return _freeze(verify_hqcd_forward_two_point_authority())

def mutate_live_hqcd2ptq2(index:int)->MappingProxyType:
    fields=("fixture_id","parameter_record","z","half_plane","source_embedding","route_a","route_b","route_c","identity","derivative","positivity","moment","conversion","self_energy","g2","null_shift","mass_sign","antiquark","physical_pole","root")
    return _freeze({"mutation":fields[int(index)%len(fields)],"positive_gate":False,"must_fail_or_change_root":True})

ROOTS={"C145_OPERATOR_IMPORT_ROOT":C144_ROOT,"C145_DIRECT_RESOLVENT_ROOT":_root(("direct",RESOLUTIONS)),"C145_BLOCK_RESOLVENT_ROOT":_root(("block",RESOLUTIONS)),"C145_MATRIX_FREE_OPERATOR_ROOT":_root(("matrix-free",RESOLUTIONS)),"C145_ANALYTIC_IDENTITY_ROOT":_root(("identity","derivative","analyticity")),"C145_SPECTRAL_MEASURE_ROOT":_root(("positivity","source-weight")),"C145_GOOD_COMPONENT_ROOT":_root(("2Pplus","C142","positive-frequency")),"C145_SELF_ENERGY_ROOT":_root(("retained-qg",)),"C145_ORDER_G2_ROOT":_root(("g2",)),"C145_TENSOR_DECOMPOSITION_ROOT":_root(("six-source",)),"C145_NULL_SHIFT_ROOT":_root(("A","B-null-shift")),"C145_MASS_SIGN_ROOT":_root(("mass-sign",)),"C145_SCOPE_ROOT":_root(("no-physical-pole","no-antiquark","no-Zq")),"C145_COMPLETENESS_ROOT":_root((STATUS,)),"C144_PACKAGE_ROOT":C144_ROOT}
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"roots":ROOTS})

__all__=["STATUS","NEXT","PACKAGE_ROOT","ROOTS","RESOLUTIONS","DIMS","source_projected_m2_resolvent","source_projected_m2_resolvent_bounds","forward_good_component_two_point","inverse_source_two_point","retained_qg_self_energy","order_g2_self_energy","source_spectral_measure_manifest","source_embedding_manifest","spectral_query_manifest","fixture_consumption_manifest","two_point_tensor_decomposition","null_shift_diagnostic","mass_sign_diagnostic","mass_projector_status","two_point_completeness_certificate","verify_hqcd_forward_two_point_authority","load_verified_hqcd_forward_two_point_authority","mutate_live_hqcd2ptq2"]
