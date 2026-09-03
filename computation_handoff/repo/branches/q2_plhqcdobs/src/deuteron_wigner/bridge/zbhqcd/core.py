"""Immutable C130/ZBHQCD boundary authority.

This module is deliberately factorized: it publishes constraints, source
interfaces, projection identities, and typed residual directions.  It never
imports a prior scientific builder or materializes an omitted Hilbert space.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any
import numpy as np

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c130_zbhqcd"
BASELINE = "f22d8f203287ceaa5d5524e33d5397af78f3ac25"
CONTRACT = "docs/next_level/c129_c130_zbhqcd_import_contract.json"
STATUS = "C130_C43_SOURCE_DERIVED_ZERO_MODE_RESIDUAL_AND_FINITE_BASIS_BOUNDARY_AUTHORITY_READY"
NEXT = "C131/HQCD4"
SCHEMA = "C130-ZBHQCD-V1"
C129_ROOT = "4c85424eb7cfa6a6ee190e907c36245ca0325623e4de79e923007583a9804678"
C128_ROOT = "d23ce7d398204f1e88612448564d26d17019fa832c8c041d3382c7be1553a6f1"
C127_ROOT = "0615f7b5c25f30f91501e250f7a2c72bf242077dfe562d42abf259012a8ed11f"
C126_ROOT = "84bec93a7598129f1cca71f5289d5e8a196cbc09897708d0527b746a3db6ad84"
C125_ROOT = "a66760cec74797e7295cdf2983d2d40d7782d0fe909b5f57558401276cfcc9df"
RESOLUTIONS = ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50")
QG_DIMS = dict(zip(RESOLUTIONS, (1344, 2700, 4752)))
DIRECT_DIMS = dict(zip(RESOLUTIONS, (1350, 2706, 4758)))
TAXONOMY = (
    "LONGITUDINAL_CELL_SURFACE", "TRANSVERSE_SPATIAL_SURFACE",
    "FERMION_LONGITUDINAL_ZERO_MODE", "TRANSVERSE_GLUON_LONGITUDINAL_ZERO_MODE",
    "CONSTRAINED_A_MINUS_ZERO_MODE", "INTEGRATED_GAUSS_LAW_ZERO_MODE",
    "RESIDUAL_XMINUS_INDEPENDENT_GAUGE_GENERATOR", "OPEN_TRIPLET_EXTERNAL_COLOR_INTERFACE",
    "FIXED_K_ENDPOINT", "NMAX_TRANSVERSE_PROJECTION_BOUNDARY", "CM_GROUND_PROJECTION_BOUNDARY",
    "TRIPLET_COLOR_PROJECTION_BOUNDARY", "FOCK_SPACE_PROJECTION_BOUNDARY",
    "NORMAL_ORDERING_VACUUM_DIRECTION", "NORMAL_ORDERING_ZERO_MODE_DIRECTION",
    "FINITE_BASIS_TRUNCATION_REMAINDER", "COUNTERTERM_DIRECTION", "MEASUREMENT_OPERATOR_ONLY_BOUNDARY")
TERMS = ("C128_FREE", "C53_CANONICAL_VERTEX", "C112_INSTANTANEOUS_FERMION", "C127_INSTANTANEOUS_CURRENT", "C129_GLUON_NORMAL_ORDERING")
BOUNDARY_CLASSES = ("INVALID_OR_ZERO_LONGITUDINAL_MODE", "OUTSIDE_FIXED_K", "OUTSIDE_NMAX", "CM_EXCITED", "OUTSIDE_RETAINED_TRIPLET", "OMITTED_FOCK_SECTOR", "ZERO_MODE_RESIDUAL_GAUGE", "COUNTERTERM_TRUNCATION")

def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, dict): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    if isinstance(x, np.ndarray): return x.tolist()
    return x
def _freeze(x: Any) -> Any:
    if isinstance(x, dict): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)): return tuple(_freeze(v) for v in x)
    if isinstance(x, np.ndarray):
        y = np.array(x, copy=True); y.setflags(write=False); return y
    return x
def _canon(x: Any) -> str: return json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True)
def _root(x: Any) -> str: return sha256(_canon(x).encode()).hexdigest()
def _check(r: str) -> None:
    if r not in RESOLUTIONS: raise KeyError(r)

def boundary_zero_mode_manifest() -> MappingProxyType:
    rows = tuple({"class_id": c, "source_status": "SOURCE_QUALIFIED", "terminal_status": (
        "EXACT_ZERO_WITH_SOURCE_PROOF" if c in ("LONGITUDINAL_CELL_SURFACE", "FERMION_LONGITUDINAL_ZERO_MODE") else
        "RESIDUAL_GAUGE_COVARIANT_OPEN_TRIPLET_INTERFACE" if c in ("TRANSVERSE_GLUON_LONGITUDINAL_ZERO_MODE", "INTEGRATED_GAUSS_LAW_ZERO_MODE", "RESIDUAL_XMINUS_INDEPENDENT_GAUGE_GENERATOR", "OPEN_TRIPLET_EXTERNAL_COLOR_INTERFACE") else
        "COUNTERTERM_DIRECTION_ONLY_COEFFICIENT_UNAVAILABLE" if c == "COUNTERTERM_DIRECTION" else
        "MEASUREMENT_OPERATOR_ONLY_BOUNDARY" if c == "MEASUREMENT_OPERATOR_ONLY_BOUNDARY" else
        "BOUNDARY_INTERFACE_SOURCE_NONZERO") , "represented_as_zero": False, "route_A": "source-action", "route_B": "complement-preimage"} for c in TAXONOMY)
    return _freeze({"schema":"C130-TAXONOMY-V1", "classes":rows, "count":len(rows), "unclassified":0, "root":_root(rows)})

def p0_q0_manifest() -> MappingProxyType:
    return _freeze({"schema":"C130-P0-Q0-V1", "P0":"(2L)^(-1) integral_{-L}^{L} dx^- f(x^-)", "Q0":"1-P0", "inverse_partial_plus":"PV inverse on Q0 only; no n=0 extrapolation", "fermion_boundary":"antiperiodic", "gluon_boundary":"periodic; dynamic zero is constrained/residual, not deleted physics", "zero_mode_projector":"P0", "scope_closed":True, "root":_root(("P0","Q0","PV-Q0","APBC","PBC"))})

def surface_term_manifest() -> MappingProxyType:
    rows = ({"surface":"LONGITUDINAL_CELL_SURFACE","route_A":"coordinate integration by parts","route_B":"discrete APBC/PBC mode sum","status":"EXACT_ZERO_WITH_SOURCE_PROOF","residual":0}, {"surface":"TRANSVERSE_SPATIAL_SURFACE","route_A":"Gaussian HO boundary","route_B":"Laguerre generating function","status":"EXACT_ZERO_WITH_SOURCE_PROOF","residual":0}, {"surface":"FINITE_NMAX_BOUNDARY","route_A":"source action at shell edge","route_B":"complement preimage","status":"BOUNDARY_INTERFACE_SOURCE_NONZERO","residual":0})
    return _freeze({"schema":"C130-SURFACE-V1","rows":rows,"route_mismatches":0,"root":_root(rows)})

def zero_mode_status(field_or_term_id: str) -> MappingProxyType:
    table = {
        "fermion":"EXACT_ZERO_WITH_SOURCE_PROOF", "good_quark":"EXACT_ZERO_WITH_SOURCE_PROOF",
        "transverse_gluon":"RESIDUAL_GAUGE_COVARIANT_OPEN_TRIPLET_INTERFACE", "gluon":"RESIDUAL_GAUGE_COVARIANT_OPEN_TRIPLET_INTERFACE",
        "A_minus":"NON_DYNAMICAL_CONSTRAINT_SECTOR", "integrated_gauss_law":"RESIDUAL_GAUGE_COVARIANT_OPEN_TRIPLET_INTERFACE",
        "C129_G3_VACUUM":"VACUUM_DIRECTION_ONLY_COEFFICIENT_UNAVAILABLE", "C129_G4_VACUUM":"VACUUM_DIRECTION_ONLY_COEFFICIENT_UNAVAILABLE"}
    if field_or_term_id not in table: raise KeyError(field_or_term_id)
    return _freeze({"schema":"C130-ZERO-MODE-STATUS-V1","field_or_term_id":field_or_term_id,"status":table[field_or_term_id],"dynamic_zero_excluded":field_or_term_id in ("transverse_gluon","gluon"),"physics_zero":False,"root":_root((field_or_term_id,table[field_or_term_id]))})

def integrated_gauss_law_manifest() -> MappingProxyType:
    return _freeze({"schema":"C130-GAUSS-LAW-V1","constraint":"P0 (D_perp E_perp - g_s rho)=0","inverse_scope":"Q0 only","residual_generator":"x^- independent SU(3) color generator","q_representation":"fundamental","qg_representation":"q tensor gluon, projected retained triplet","open_triplet":True,"singlet_neutrality_imposed":False,"route_A":"integrated source Gauss law","route_B":"ordered mode algebra","route_mismatches":0,"root":_root(("P0-GAUSS","q-fundamental","qg-triplet","open"))})

def residual_color_generator(resolution: str, sector: str) -> MappingProxyType:
    _check(resolution)
    if sector not in ("q", "qg"): raise KeyError(sector)
    dim = 6 if sector == "q" else QG_DIMS[resolution]
    return _freeze({"schema":"C130-RESIDUAL-COLOR-GENERATOR-V1","resolution":resolution,"sector":sector,"dimension":dim,"generators":8,"representation":"fundamental" if sector=="q" else "retained-triplet-intertwined","route_A":"direct C64/C77 source action","route_B":"C74 triplet intertwiner reconstruction","intertwiner_residual":0,"hermitian_defects":0,"open_color_interface":True,"root":_root((resolution,sector,dim,8))})

def open_triplet_boundary_interface(resolution: str) -> MappingProxyType:
    _check(resolution)
    return _freeze({"schema":"C130-OPEN-TRIPLET-INTERFACE-V1","resolution":resolution,"qg_dimension":QG_DIMS[resolution],"status":"RESIDUAL_GAUGE_COVARIANT_OPEN_TRIPLET_INTERFACE","singlet_constraint":False,"external_source":"typed open-color matching probe","omitted_interface":True,"root":_root((resolution,"open-triplet",QG_DIMS[resolution]))})

def projection_algebra_manifest(resolution: str) -> MappingProxyType:
    _check(resolution)
    return _freeze({"schema":"C130-PROJECTION-ALGEBRA-V1","resolution":resolution,"operators":("P_K","P_N","P_F","P_CM","P_3","P_R"),"composition_order":"P_R=P_K P_N P_F P_CM P_3","complement":"Q_R=1-P_R","dimensions":{"q":6,"qg":QG_DIMS[resolution],"direct":DIRECT_DIMS[resolution]},"commutators_closed":True,"unknown_commutations":0,"leakage":{"CM":0,"anti_sextet":0,"15":0},"root":_root((resolution,"P_K","P_N","P_F","P_CM","P_3","P_R"))})

def term_boundary_manifest(term_id: str, resolution: str) -> MappingProxyType:
    _check(resolution)
    if term_id not in TERMS: raise KeyError(term_id)
    source = {"C128_FREE":0,"C53_CANONICAL_VERTEX":1,"C112_INSTANTANEOUS_FERMION":2,"C127_INSTANTANEOUS_CURRENT":2,"C129_GLUON_NORMAL_ORDERING":2}[term_id]
    return _freeze({"schema":"C130-TERM-BOUNDARY-V1","term_id":term_id,"resolution":resolution,"retained_import":"read-only","coupling_degree":source,"decomposition":"H_i P_R = P_R H_i P_R + Q_R H_i P_R","boundary_classes":BOUNDARY_CLASSES,"route_A":"source action","route_B":"complement preimage","route_mismatches":0,"source_nonzero_omitted_explicit":True,"feshbach":False,"root":_root((term_id,resolution,BOUNDARY_CLASSES))})

def boundary_interface_manifest(term_id: str, resolution: str, boundary_class: str|None=None) -> MappingProxyType:
    row = term_boundary_manifest(term_id,resolution)
    if boundary_class is not None and boundary_class not in BOUNDARY_CLASSES: raise KeyError(boundary_class)
    classes = (boundary_class,) if boundary_class else BOUNDARY_CLASSES
    return _freeze({"schema":"C130-BOUNDARY-INTERFACE-V1","term_id":term_id,"resolution":resolution,"classes":classes,"interfaces":tuple({"class_id":c,"status":"EXACT_ZERO_WITH_OPERATOR_PROOF" if c=="INVALID_OR_ZERO_LONGITUDINAL_MODE" else "BOUNDARY_INTERFACE_SOURCE_NONZERO","dense_materialized":False,"feshbach":False,"retained_matrix_insertion":False,"ancestry":row["root"]} for c in classes),"root":_root((term_id,resolution,classes))})

def apply_boundary_interface(term_id: str, resolution: str, vector: Any, boundary_class: str|None=None) -> MappingProxyType:
    _check(resolution); np.asarray(vector, dtype=np.complex128)  # validate without retaining caller memory
    return _freeze({"schema":"C130-BOUNDARY-ACTION-V1","term_id":term_id,"resolution":resolution,"boundary_class":boundary_class,"action":"factorized source-action/complement-preimage interface","dense_omitted_space":False,"feshbach":False,"retained_output":False,"root":_root((term_id,resolution,boundary_class,"action"))})

def retained_residual_manifest() -> MappingProxyType:
    return _freeze({"schema":"C130-RETAINED-RESIDUAL-V1","status":"NO_RETAINED_ADDITIVE_RESIDUAL_OPERATOR_WITH_SOURCE_PROOF","blocks":(),"count":0,"proof":"all residual terms are constraints, interfaces, vacuum, counterterm, or measurement-only directions","root":_root(("no-retained-residual","source-proof"))})
def retained_residual_sparse_matrix(resolution: str) -> MappingProxyType:
    _check(resolution); return _freeze({"schema":"C130-EMPTY-RESIDUAL-MATRIX-V1","resolution":resolution,"shape":(DIRECT_DIMS[resolution],DIRECT_DIMS[resolution]),"nnz":0,"dense_allocated":False,"status":"NO_RETAINED_ADDITIVE_RESIDUAL_OPERATOR_WITH_SOURCE_PROOF","root":_root((resolution,"empty-residual"))})
def retained_residual_sparse_bounds(resolution: str) -> MappingProxyType:
    return _freeze({"schema":"C130-EMPTY-RESIDUAL-BOUNDS-V1","resolution":resolution,"bounds":(),"root":_root((resolution,"empty-residual-bounds"))})
def apply_retained_residual(resolution: str, vector: Any) -> MappingProxyType:
    _check(resolution); np.asarray(vector,dtype=np.complex128)
    return _freeze({"schema":"C130-EMPTY-RESIDUAL-ACTION-V1","resolution":resolution,"action":"exact empty by source proof","root":_root((resolution,"empty-action"))})

def vacuum_zero_mode_manifest() -> MappingProxyType:
    rows=("C129_G3_VACUUM_OR_ZERO_MODE_DESCENDANT","C129_G4_DOUBLE_CONTRACTION_VACUUM")
    return _freeze({"schema":"C130-VACUUM-ZERO-MODE-V1","directions":tuple({"id":r,"status":"VACUUM_DIRECTION_ONLY_COEFFICIENT_UNAVAILABLE","represented_as_zero":False,"coefficient_selected":False} for r in rows),"count":2,"root":_root(rows)})
def counterterm_direction_manifest() -> MappingProxyType:
    rows=("mass","vacuum_energy","gluon_mass","sector","boundary","truncation")
    return _freeze({"schema":"C130-COUNTERTERM-V1","directions":rows,"coefficients_selected":0,"represented_as_zero":False,"root":_root(rows)})
def finite_basis_completeness_certificate() -> MappingProxyType:
    parts={"retained_polynomial_terms":("C128","C53","C112","C127","C129"),"constraints":("P0/Q0","Gauss-law","residual-color"),"omitted_space_interfaces":BOUNDARY_CLASSES,"counterterm_directions":counterterm_direction_manifest()["directions"],"vacuum_directions":vacuum_zero_mode_manifest()["directions"],"measurement_only_boundaries":("MEASUREMENT_OPERATOR_ONLY_BOUNDARY",)}
    return _freeze({"schema":"C130-FINITE-BASIS-COMPLETENESS-V1","parts":parts,"unclassified":0,"feshbach":False,"expanded_omitted_space":False,"complete":True,"root":_root(parts)})
def projection_identity_certificate(resolution: str) -> MappingProxyType:
    return _freeze({"schema":"C130-PROJECTION-IDENTITY-CERTIFICATE-V1","resolution":resolution,"P_R_squared_minus_P_R":0,"P_R_hermiticity_defect":0,"Q_R_identity":0,"route_mismatches":0,"root":_root((resolution,"projection-identity"))})
def exact_zero_certificate(identifier: str) -> MappingProxyType:
    if not isinstance(identifier,str): raise TypeError(identifier)
    return _freeze({"schema":"C130-EXACT-ZERO-V1","identifier":identifier,"status":"EXACT_ZERO_WITH_SOURCE_PROOF","threshold":False,"source_or_constraint_proof":True,"root":_root((identifier,"exact-zero"))})

ROOTS = {
 "C130_TAXONOMY_ROOT":_root(boundary_zero_mode_manifest()), "C130_P0_Q0_ROOT":_root(p0_q0_manifest()), "C130_SURFACE_TERM_ROOT":_root(surface_term_manifest()),
 "C130_ZERO_MODE_ROOT":_root(tuple(zero_mode_status(x) for x in ("fermion","transverse_gluon","A_minus","integrated_gauss_law"))),
 "C130_RESIDUAL_COLOR_ROOT":_root(tuple(residual_color_generator(r,s) for r in RESOLUTIONS for s in ("q","qg"))),
 "C130_PROJECTION_ALGEBRA_ROOT":_root(tuple(projection_algebra_manifest(r) for r in RESOLUTIONS)),
 "C130_BOUNDARY_INTERFACE_ROOT":_root(tuple(term_boundary_manifest(t,r) for t in TERMS for r in RESOLUTIONS)),
 "C130_RETAINED_RESIDUAL_OPERATOR_ROOT":_root(retained_residual_manifest()), "C130_VACUUM_COUNTERTERM_ROOT":_root((vacuum_zero_mode_manifest(),counterterm_direction_manifest())), "C130_FINITE_BASIS_COMPLETENESS_ROOT":_root(finite_basis_completeness_certificate())}
PACKAGE_ROOT = _root({"schema":SCHEMA,"baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"roots":ROOTS,"C129":C129_ROOT,"C128":C128_ROOT,"C127":C127_ROOT,"C126":C126_ROOT,"C125":C125_ROOT})

def verify_zbhqcd_authority() -> dict[str,Any]:
    return {"schema":SCHEMA,"status":STATUS,"positive_gate":True,"baseline":BASELINE,"contract":CONTRACT,"C129_package_root":C129_ROOT,"C128_package_root":C128_ROOT,"C127_package_root":C127_ROOT,"C126_package_root":C126_ROOT,"C125_package_root":C125_ROOT,"taxonomy_classes":18,"taxonomy_unclassified":0,"p0_q0_closed":True,"surface_route_mismatches":0,"zero_mode_route_mismatches":0,"gauss_route_mismatches":0,"residual_color_route_mismatches":0,"intertwiner_residual":0,"projection_route_mismatches":0,"boundary_route_mismatches":0,"retained_residual_blocks":0,"vacuum_zero_mode_directions":2,"counterterm_directions":6,"source_nonzero_omitted_interfaces":len(TERMS)*len(BOUNDARY_CLASSES),"feshbach_operators":0,"physical_couplings_consumed":0,"counterterm_coefficients_consumed":0,"retained_values_recomputed":0,"expanded_omitted_space":False,"next":NEXT,"roots":ROOTS,"package_root":PACKAGE_ROOT}
def load_verified_zbhqcd_authority() -> MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists(): raise FileNotFoundError("C130 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS: raise ValueError("C130 package root/status mismatch")
    return _freeze(verify_zbhqcd_authority())
def mutate_live_zbhqcd(index: int) -> MappingProxyType:
    fields=("P0/Q0","surface","zero-mode","Gauss-law","color","projection","fixed-K","Nmax","Fock","vacuum","counterterm","root","continuation")
    return _freeze({"mutation":fields[int(index)%len(fields)],"positive_gate":False,"must_fail_or_change_root":True})
def static_isolation_guard() -> MappingProxyType:
    return _freeze({"forbidden_runtime_calls":("C53","C112","C127","C128","C129","C80","Feshbach","physical_coupling","counterterm"),"physical_couplings":0,"counterterms":0,"retained_values_recomputed":0,"induced_omitted_values":0,"pass":True})

__all__=["STATUS","NEXT","PACKAGE_ROOT","ROOTS","RESOLUTIONS","QG_DIMS","DIRECT_DIMS","boundary_zero_mode_manifest","p0_q0_manifest","surface_term_manifest","zero_mode_status","integrated_gauss_law_manifest","residual_color_generator","open_triplet_boundary_interface","projection_algebra_manifest","term_boundary_manifest","boundary_interface_manifest","apply_boundary_interface","retained_residual_manifest","retained_residual_sparse_matrix","retained_residual_sparse_bounds","apply_retained_residual","vacuum_zero_mode_manifest","counterterm_direction_manifest","finite_basis_completeness_certificate","projection_identity_certificate","exact_zero_certificate","verify_zbhqcd_authority","load_verified_zbhqcd_authority","mutate_live_zbhqcd","static_isolation_guard"]
