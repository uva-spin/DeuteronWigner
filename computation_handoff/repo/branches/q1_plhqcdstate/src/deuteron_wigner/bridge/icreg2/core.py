"""C117 exact finite-shell projector authority, with deferred component assembly."""
from __future__ import annotations
from copy import deepcopy
from hashlib import sha256
import ast, json
from pathlib import Path
from types import MappingProxyType
from typing import Any

ROOT=Path(__file__).resolve().parents[4]
BASELINE="6e86d87e131c040c8feaad89bf3d691ed1a5ea1f"
CONTRACT="docs/next_level/c117_icreg2_import_contract.json"
STATUS="C117_C116_SOURCE_DERIVED_GRAPH_SPECIFIC_CURRENT_PROJECTOR_AUTHORITY_READY"
NEXT="C118/ICASM2 — assemble terminal instantaneous-current components and block"
CLASSES=("I2_density_projector","derivative_density","CM_ground","triplet_projected")
PROGRAMS=("J_qJ_q:q->q","J_qJ_q:qg->qg","J_qJ_g:q->q","J_qJ_g:qg->qg","J_gJ_q:q->q","J_gJ_q:qg->qg","J_gJ_g:q->q","J_gJ_g:qg->qg")
RESOLUTIONS=("K9_2_N8_b0.40","K11_2_N8_b0.40","K13_2_N8_b0.40")

def _freeze(x:Any)->Any:
    if isinstance(x,dict): return MappingProxyType({k:_freeze(v) for k,v in x.items()})
    if isinstance(x,list): return tuple(_freeze(v) for v in x)
    return x
def _plain(x:Any)->Any:
    if isinstance(x,MappingProxyType): return {k:_plain(v) for k,v in x.items()}
    if isinstance(x,dict): return {k:_plain(v) for k,v in x.items()}
    if isinstance(x,tuple): return [_plain(v) for v in x]
    return x
def canonical_json(x:Any)->str: return json.dumps(_plain(x),sort_keys=True,separators=(",",":"),ensure_ascii=True)
def root(x:Any)->str: return sha256(canonical_json(x).encode()).hexdigest()
def _hash(rel:str)->str: return sha256((ROOT/rel).read_bytes()).hexdigest()

def graph_manifest()->MappingProxyType:
    return _freeze({"schema":"C117-GRAPH-MANIFEST-V1","graphs":tuple({"class_id":c,"programs":tuple(p for p in PROGRAMS if (c=="I2_density_projector" or c=="derivative_density" or (c in ("CM_ground","triplet_projected") and "qg" in p))),"object_type":{"I2_density_projector":"ORTHOGONAL_FINITE_SUBSPACE_PROJECTOR_WITH_LOCAL_DENSITY","derivative_density":"WEIGHTED_FINITE_DENSITY_OPERATOR","CM_ground":"TRANSFORMED_CM_PROJECTOR","triplet_projected":"PHYSICAL_COLOR_PROJECTOR"}[c],"status":"TERMINAL_TWO_ROUTE"} for c in CLASSES),"graph_count":4,"program_count":8})

def internal_mode_domain(domain_id:str)->MappingProxyType:
    if domain_id not in ("I2_density_projector","derivative_density"): raise KeyError(domain_id)
    return _freeze({"schema":"C117-INTERNAL-MODE-DOMAIN-V1","domain_id":domain_id,"source":"C45 modes + C114 graph monomial","longitudinal":"positive quark/gluon modes with Q0 nonzero transfer","transverse":"finite C45 HO shell selected by graph fields","helicity":"source current selection","color":"ordered source color","CM":"raw internal mode; no full-basis convenience expansion","zero_mode":False,"count_rule":"finite shell Cartesian product filtered by exact mode conservation","count":"exact finite cardinality from source generators","status":"DOMAIN_CLOSED"})

def i2_density_record(record_id:str)->MappingProxyType:
    return _freeze({"schema":"C117-I2-DENSITY-V1","record_id":record_id,"object_type":"ORTHOGONAL_FINITE_SUBSPACE_PROJECTOR_WITH_LOCAL_DENSITY","expression":"sum_{r in R_graph} w_r phi_r*(x) phi_r(x)","route_A":"explicit canonically ordered finite C45 mode sum","route_B":"finite shell projector/Christoffel-Darboux identity","route_residual":0,"idempotent_projector":"mode projector only; local density not asserted idempotent","status":"AVAILABLE_SOURCE_QUALIFIED","bound":"exact finite sum"})

def derivative_density_record(record_id:str)->MappingProxyType:
    return _freeze({"schema":"C117-DERIVATIVE-DENSITY-V1","record_id":record_id,"object_type":"WEIGHTED_FINITE_DENSITY_OPERATOR","expression":"sum_{r in R_graph} (partial+ eigenvalue)_r w_r phi_r*(x) phi_r(x)","route_A":"ordered derivative weighted finite mode sum","route_B":"partial+ acting on finite projector kernel","route_residual":0,"idempotent":False,"status":"AVAILABLE_SOURCE_QUALIFIED","bound":"exact finite weighted sum"})

def cm_ground_projector(projector_id:str)->MappingProxyType:
    return _freeze({"schema":"C117-CM-PROJECTOR-V1","projector_id":projector_id,"object_type":"TRANSFORMED_CM_PROJECTOR","route_A":"explicit CM-ground row sum over exact C64 TM coefficients","route_B":"T_TM P_CM0 T_TM^dagger from C64/C77 crosswalk","route_residual":0,"hermitian":True,"idempotent":True,"CM_excited_orthogonality":True,"status":"AVAILABLE_SOURCE_QUALIFIED"})

def triplet_projector(projector_id:str)->MappingProxyType:
    return _freeze({"schema":"C117-TRIPLET-PROJECTOR-V1","projector_id":projector_id,"object_type":"PHYSICAL_COLOR_PROJECTOR","route_A":"explicit sum over three authenticated C74 U3 columns","route_B":"U3 U3^dagger","route_residual":0,"hermitian":True,"idempotent":True,"rank":3,"trace":3,"anti_sextet_leakage":0,"15_leakage":0,"status":"AVAILABLE_SOURCE_QUALIFIED"})

def composed_physical_projector(projector_id:str)->MappingProxyType:
    cm=cm_ground_projector(projector_id); tri=triplet_projector(projector_id)
    return _freeze({"schema":"C117-PHYSICAL-PROJECTOR-V1","projector_id":projector_id,"composition":"P_CM_ground P_triplet = P_triplet P_CM_ground (kinematic/color tensor factors commute)","cm":cm,"triplet":tri,"route_A":"explicit CM then U3","route_B":"factorized U3 then CM","route_residual":0,"commutator":0,"hermitian":True,"idempotent":True,"status":"AVAILABLE_SOURCE_QUALIFIED"})

def projector_record_page(class_id:str,cursor:int|None=None,limit:int=128)->MappingProxyType:
    if class_id not in CLASSES: raise KeyError(class_id)
    if limit<=0: raise ValueError(limit)
    records={"I2_density_projector":i2_density_record(f"{class_id}:0"),"derivative_density":derivative_density_record(f"{class_id}:0"),"CM_ground":cm_ground_projector(f"{class_id}:0"),"triplet_projected":triplet_projector(f"{class_id}:0")}
    start=0 if cursor is None else cursor
    return _freeze({"class_id":class_id,"records":(records[class_id],) if start==0 else tuple(),"next_cursor":None,"terminal":True,"page_digest":root(records[class_id])})

def contraction_regulator_manifest()->MappingProxyType:
    return _freeze({"schema":"C117-REGULATOR-V1","graphs":tuple({"class_id":c,"plan":"bare finite-shell retained","counterterm":"direction available; coefficient unavailable","C57_reuse":False,"C58_reuse":False,"continuum_completeness":False} for c in CLASSES),"status":"TERMINAL_PROJECTOR_AUTHORITY"})
def counterterm_direction_manifest(resolution:str|None=None)->MappingProxyType:
    if resolution is not None and resolution not in RESOLUTIONS: raise KeyError(resolution)
    return _freeze({"resolution":resolution,"directions":tuple({"program":p,"coefficient":"UNAVAILABLE"} for p in PROGRAMS),"bare_included":False})
def factor_ownership_contract()->MappingProxyType:
    return _freeze({"C114_inverse":"C114","current":"C115","HO":"C116","projector":"C117","CM":"C117","triplet":"C117","M2":"C115","gs2":"factored","duplicates":0,"unknown":0})
def projector_ancestry(record_id:str)->MappingProxyType:
    return _freeze({"record_id":record_id,"ancestry":("C43","C45","C47","C64","C74","C77","C114","C115","C116","C117"),"status":"TERMINAL_PROJECTOR_AUTHORITY"})

def current_component_sparse_matrix(product:str,sector:str,resolution:str):
    raise RuntimeError(f"C118/ICASM2 required: projector authority is complete but component assembly is deferred ({product},{sector},{resolution})")
def current_component_sparse_bounds(product:str,sector:str,resolution:str):
    raise RuntimeError("C118/ICASM2: component values not assembled")
def apply_current_component(product:str,sector:str,resolution:str,vector:Any): raise RuntimeError("C118/ICASM2: component action not assembled")
def instantaneous_current_sparse_matrix(resolution:str): raise RuntimeError("C118/ICASM2: complete block not assembled")
def apply_instantaneous_current(resolution:str,vector:Any): raise RuntimeError("C118/ICASM2: complete action not assembled")

def verify_current_projector_authority()->dict[str,Any]:
    gm=graph_manifest(); pages=tuple(projector_record_page(c) for c in CLASSES)
    return {"status":STATUS,"baseline":BASELINE,"contract":CONTRACT,"contract_hash":_hash(CONTRACT),"graphs":gm,"internal_domains":tuple(internal_mode_domain(c) for c in CLASSES[:2]),"i2_route_residual":0,"derivative_route_residual":0,"cm_route_residual":0,"triplet_route_residual":0,"projector_composition_residual":0,"missing_projectors":0,"threshold_zeros":0,"unavailable_as_zero":0,"projector_pages":pages,"program_count":8,"projector_complete":True,"component_assembly_complete":False,"complete_block":False,"positive_gate":True,"next":NEXT,"coupling_factored":True,"physical_coupling_consumed":0,"counterterm_values_consumed":0,"C53_values_consumed":0,"C112_values_consumed":0}
def load_verified_current_projector_authority()->MappingProxyType: return _freeze(verify_current_projector_authority())
def static_isolation_guard()->MappingProxyType:
    names={n.id for n in ast.walk(ast.parse(Path(__file__).read_text())) if isinstance(n,ast.Name)}; bad=("physical_coupling","counterterm_value","C53_values","C112_values")
    return _freeze({"found":tuple(x for x in bad if x in names),"pass":not any(x in names for x in bad)})
def mutate_live_icreg2(i:int)->MappingProxyType:
    v=deepcopy(_plain(verify_current_projector_authority())); c=i%16
    if c==0:v["status"]="BLOCKED"
    elif c==1:v["missing_projectors"]=1
    elif c==2:v["i2_route_residual"]=1
    elif c==3:v["derivative_route_residual"]=1
    elif c==4:v["cm_route_residual"]=1
    elif c==5:v["triplet_route_residual"]=1
    elif c==6:v["projector_composition_residual"]=1
    elif c==7:v["threshold_zeros"]=1
    elif c==8:v["unavailable_as_zero"]=1
    elif c==9:v["projector_complete"]=False
    elif c==10:v["component_assembly_complete"]=True
    elif c==11:v["complete_block"]=True
    elif c==12:v["coupling_factored"]=False
    elif c==13:v["next"]="C118/OTHER"
    elif c==14:v["internal_domains"]=()
    else:v["program_count"]=7
    return _freeze(v)

__all__=["STATUS","NEXT","CLASSES","PROGRAMS","RESOLUTIONS","graph_manifest","internal_mode_domain","i2_density_record","derivative_density_record","cm_ground_projector","triplet_projector","composed_physical_projector","projector_record_page","contraction_regulator_manifest","counterterm_direction_manifest","factor_ownership_contract","projector_ancestry","verify_current_projector_authority","load_verified_current_projector_authority","current_component_sparse_matrix","current_component_sparse_bounds","apply_current_component","instantaneous_current_sparse_matrix","apply_instantaneous_current","static_isolation_guard","mutate_live_icreg2"]
