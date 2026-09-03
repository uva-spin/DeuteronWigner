"""C115 ICHO: typed diagonal programs, fail-closed until HO authority closes."""
from __future__ import annotations
from copy import deepcopy
from hashlib import sha256
import ast, json
from pathlib import Path
from types import MappingProxyType
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
BASELINE = "05ac97122c8bc86838454709bbad1cb255ec6213"
CONTRACT = "docs/next_level/c115_icho_import_contract.json"
STATUS = "C115_ICHO_TRANSVERSE_KERNEL_INCOMPLETE"
NEXT = "C116/ICHO2 — unresolved instantaneous-current transverse-HO kernel class"
PRODUCTS = ("J_qJ_q", "J_qJ_g", "J_gJ_q", "J_gJ_g")
SECTORS = ("q->q", "qg->qg")
RESOLUTIONS = ("K9_2_N8_b0.40", "K11_2_N8_b0.40", "K13_2_N8_b0.40")

def _freeze(x: Any) -> Any:
    if isinstance(x, dict): return MappingProxyType({k: _freeze(v) for k,v in x.items()})
    if isinstance(x, list): return tuple(_freeze(v) for v in x)
    return x
def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType): return {k:_plain(v) for k,v in x.items()}
    if isinstance(x, dict): return {k:_plain(v) for k,v in x.items()}
    if isinstance(x, tuple): return [_plain(v) for v in x]
    return x
def canonical_json(x: Any) -> str: return json.dumps(_plain(x), sort_keys=True, separators=(",",":"), ensure_ascii=True)
def root(x: Any) -> str: return sha256(canonical_json(x).encode()).hexdigest()
def _hash(rel: str) -> str: return sha256((ROOT/rel).read_bytes()).hexdigest()

def _program(product: str, sector: str) -> MappingProxyType:
    contracted = product != "J_qJ_q"
    return _freeze({
        "id": f"{product}:{sector}", "product": product, "sector": sector,
        "source_monomials": (f"{product}:direct", f"{product}:normal_ordered", f"{product}:contractions"),
        "normal_order": "source-ordered then fermion/gluon contractions",
        "fermion_sign": "C43 current order", "gluon_commutator": "canonical transverse commutator",
        "external_fields": "q current" if product.startswith("J_q") else "transverse-gluon current",
        "contracted_fields": "none" if not contracted else "graph-selected gluon/fermion density",
        "longitudinal_transfer": "n != 0; Q0; L^2/(pi^2*n^2)",
        "ho_class": "I4_local" if not contracted else "I2_density_projector",
        "spin_rule": "delta_helicity for Jq; polarization derivative rule for Jg",
        "color_rule": {"J_qJ_q":"ordered T^a T^a","J_qJ_g":"T^a f^{abc}","J_gJ_q":"f^{abc} T^a","J_gJ_g":"f^{abc}f^{ade}"}[product],
        "projection": "C64 TM/CM-ground then C74 triplet U3 for qg",
        "normalization": "C43/C45 states; C110 only exact two-external-gluon proof",
        "regulator": "C115 graph-specific finite-HO projector required" if contracted else "none",
        "conversion": "M^2=2*(pi*K/L)*P^- - P_perp^2; L symbolic",
        "counterterm": "direction available; coefficient unavailable" if contracted else "none selected",
        "support": "source ordered; no threshold", "ancestry": ("C43","C114","C115"),
        "status": STATUS, "value": None, "bound": None,
    })

def diagonal_component_manifest() -> tuple[MappingProxyType,...]:
    return tuple(_program(p,s) for p in PRODUCTS for s in SECTORS)

def current_programs() -> tuple[MappingProxyType,...]: return diagonal_component_manifest()

def quark_current_derivation() -> MappingProxyType:
    route_a={"current":"bar psi gamma+ T^a psi","helicity":"delta_{lambda',lambda}","color":"T^a_{c'c}","longitudinal":"source mode insertion"}
    route_b={"current":"canonical good-component anticommutator","helicity":"delta_{lambda',lambda}","color":"T^a_{c'c}","longitudinal":"normalized one-quark state"}
    return _freeze({"route_a":route_a,"route_b":route_b,"agreement":True,"units":"current density; overall projection unavailable","status":"SYMBOLIC_FACTOR_CLOSED"})

def gluon_current_derivation() -> MappingProxyType:
    route_a={"current":"-f^{abc} A^b_perp partial+ A^c_perp","derivative":"acts on ordered c field","polarization":"epsilon'^* dot epsilon","color":"-f^{abc}"}
    route_b={"current":"canonical transverse commutator","derivative":"same ordered c-field k^+","polarization":"epsilon'^* dot epsilon","color":"-f^{abc}"}
    return _freeze({"route_a":route_a,"route_b":route_b,"agreement":True,"units":"current density; overall projection unavailable","status":"SYMBOLIC_FACTOR_CLOSED"})

def ho_kernel_manifest() -> MappingProxyType:
    return _freeze({"classes":("I4_local","I2_density_projector","derivative_density","CM_ground","triplet_projected"),"exact_classes":0,"status":"UNAVAILABLE_BLOCKING","threshold":None,"quadrature_primary":False,"C80_reuse":"NOT_PROVED_OPERATOR_IDENTICAL"})

def contraction_projector_manifest() -> tuple[MappingProxyType,...]:
    return tuple(_freeze({"id":f"{p}:projector","product":p,"species":"graph-dependent","longitudinal":"Q0 nonzero modes","transverse":"C45 finite shell required","CM":"physical qg only","regulator":"not inherited from C57/C58","status":"UNAVAILABLE_BLOCKING","counterterm":"COEFFICIENT_UNAVAILABLE"}) for p in PRODUCTS)

def physical_projection_manifest() -> MappingProxyType:
    return _freeze({"routes":("raw->TM->CM-ground->U3","endpoint-component recomposition"),"C64":True,"C74":True,"C77":True,"CM_leakage":None,"antisextet_leakage":None,"15_leakage":None,"status":"UNAVAILABLE_BLOCKING"})

def component_status(product: str, sector: str, resolution: str | None = None) -> MappingProxyType:
    if product not in PRODUCTS or sector not in SECTORS: raise KeyError((product,sector))
    if resolution is not None and resolution not in RESOLUTIONS: raise KeyError(resolution)
    p=next(x for x in diagonal_component_manifest() if x["product"]==product and x["sector"]==sector)
    return _freeze({"schema":"C115-COMPONENT-STATUS-V1","resolution":resolution,"program":p,"status":STATUS,"terminal":False,"value":None,"bound":None})

def factor_ownership_contract() -> MappingProxyType:
    return _freeze({"schema":"C115-FACTOR-OWNERSHIP-V1","owners":{"C114_inverse_kernel":"C114","current_factor":"C115","HO":"C115","spin":"C115","color":"C115","state_normalization":"C115","M2_conversion":"C115","g_s_squared":"factored source only"},"duplicates":0,"unknown":0})

def counterterm_direction_manifest(resolution: str|None=None) -> MappingProxyType:
    if resolution is not None and resolution not in RESOLUTIONS: raise KeyError(resolution)
    return _freeze({"resolution":resolution,"directions":tuple({"product":p,"coefficient":"UNAVAILABLE"} for p in PRODUCTS),"bare_included":False})

def current_component_sparse_matrix(product: str, sector: str, resolution: str):
    raise RuntimeError(f"{STATUS}: {product}/{sector} has no terminal HO kernel")
def current_component_sparse_bounds(product: str, sector: str, resolution: str):
    raise RuntimeError(f"{STATUS}: certified bound unavailable until HO projection closes")
def apply_current_component(product: str, sector: str, resolution: str, vector: Any):
    raise RuntimeError(f"{STATUS}: matrix-free action unavailable")
def instantaneous_current_sparse_matrix(resolution: str):
    raise RuntimeError(f"{STATUS}: complete block unavailable; no missing component is zero")
def apply_instantaneous_current(resolution: str, vector: Any):
    raise RuntimeError(f"{STATUS}: complete action unavailable")

def verify_current_ho_projection_authority() -> dict[str,Any]:
    programs=diagonal_component_manifest(); q=quark_current_derivation(); g=gluon_current_derivation(); h=ho_kernel_manifest()
    return {"status":STATUS,"baseline":BASELINE,"contract":CONTRACT,"contract_hash":_hash(CONTRACT),"programs":programs,"program_count":8,"quark_route_agreement":q["agreement"],"gluon_route_agreement":g["agreement"],"ho":h,"physical_projection":physical_projection_manifest(),"contraction_projectors":contraction_projector_manifest(),"factor_ownership":factor_ownership_contract(),"available_components":0,"blocked_components":8,"complete_block":False,"positive_gate":False,"no_zero_substitution":True,"C80_spatial_reuse":False,"C57_C58_regulator_reuse":False,"C110_scope_limited":True,"coupling_factored":True}
def load_verified_current_ho_projection_authority() -> MappingProxyType: return _freeze(verify_current_ho_projection_authority())
def current_ho_kernel_record(kernel_id: str) -> MappingProxyType:
    if kernel_id not in ("I4_local","I2_density_projector","derivative_density","CM_ground","triplet_projected"): raise KeyError(kernel_id)
    return _freeze({"kernel_id":kernel_id,"status":"UNAVAILABLE_BLOCKING","value":None,"bound":None})
def current_contraction_record(contraction_id: str) -> MappingProxyType:
    if contraction_id not in tuple(f"{p}:projector" for p in PRODUCTS): raise KeyError(contraction_id)
    return next(x for x in contraction_projector_manifest() if x["id"]==contraction_id)
def current_projection_ancestry(record_id: str) -> MappingProxyType:
    return _freeze({"record_id":record_id,"ancestry":("C43","C45","C47","C64","C74","C77","C114","C115"),"status":STATUS})
def static_isolation_guard() -> MappingProxyType:
    tree=ast.parse(Path(__file__).read_text()); names={n.id for n in ast.walk(tree) if isinstance(n,ast.Name)}; forbidden=("C53","C112","C80","physical_coupling","counterterm_value")
    return _freeze({"found":tuple(x for x in forbidden if x in names),"pass":not any(x in names for x in forbidden)})
def mutate_live_icho(fault_id: int) -> MappingProxyType:
    v=deepcopy(_plain(verify_current_ho_projection_authority())); c=fault_id%16
    if c==0:v["status"]="READY"
    elif c==1:v["program_count"]=7
    elif c==2:v["quark_route_agreement"]=False
    elif c==3:v["gluon_route_agreement"]=False
    elif c==4:v["ho"]["status"]="READY"
    elif c==5:v["available_components"]=8
    elif c==6:v["blocked_components"]=0
    elif c==7:v["complete_block"]=True
    elif c==8:v["positive_gate"]=True
    elif c==9:v["no_zero_substitution"]=False
    elif c==10:v["C80_spatial_reuse"]=True
    elif c==11:v["C57_C58_regulator_reuse"]=True
    elif c==12:v["factor_ownership"]["duplicates"]=1
    elif c==13:v["factor_ownership"]["unknown"]=1
    elif c==14:v["physical_projection"]["status"]="READY"
    else:v["C110_scope_limited"]=False
    return _freeze(v)

__all__=["STATUS","NEXT","PRODUCTS","SECTORS","RESOLUTIONS","load_verified_current_ho_projection_authority","verify_current_ho_projection_authority","diagonal_component_manifest","current_programs","component_status","current_ho_kernel_record","current_contraction_record","current_component_sparse_matrix","current_component_sparse_bounds","apply_current_component","instantaneous_current_sparse_matrix","apply_instantaneous_current","counterterm_direction_manifest","current_projection_ancestry","factor_ownership_contract","quark_current_derivation","gluon_current_derivation","ho_kernel_manifest","contraction_projector_manifest","physical_projection_manifest","static_isolation_guard","mutate_live_icho"]
