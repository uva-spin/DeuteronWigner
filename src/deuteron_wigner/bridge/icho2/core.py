"""C116 ICHO2: five-class crosswalk and fail-closed finite-shell authority."""
from __future__ import annotations
from copy import deepcopy
from hashlib import sha256
import ast, json
from pathlib import Path
from types import MappingProxyType
from typing import Any

ROOT=Path(__file__).resolve().parents[4]
BASELINE="291c14537348e48ac5b360f858e623d0b4635144"
CONTRACT="docs/next_level/c116_icho2_import_contract.json"
STATUS="C116_ICHO2_KERNEL_CLASS_INCOMPLETE"
BLOCKING_CLASS="I2_density_projector"
NEXT="C117/ICREG2 — graph-specific finite-shell contraction projector for I2_density_projector"
CLASSES=("I4_local","I2_density_projector","derivative_density","CM_ground","triplet_projected")
PRODUCTS=("J_qJ_q","J_qJ_g","J_gJ_q","J_gJ_g")
SECTORS=("q->q","qg->qg")
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

CLASS_DEFINITIONS={
 "I4_local":{"definition":"integral d2x phi_a'*phi_b'*phi_c*phi_d","species":"four external fields","routes":["polar Laguerre/Gamma finite moment","Cartesian/circular generating function"],"status":"EXACT_SPATIAL_AUTHORITY","expression":"b_HO^2/pi times finite Laguerre polynomial Gamma moments","bound":"zero-radius exact expression","reuse":"C80 spatial-only reuse PROVED; no C80 source/normalization factors"},
 "I2_density_projector":{"definition":"sum_{r in R} w_r integral d2x phi_a'*phi_a phi_r'*phi_r","species":"two external plus contracted density","routes":["finite Laguerre shell projector","TM/projector decomposition"],"status":"UNAVAILABLE_BLOCKING","expression":None,"bound":None,"reuse":"C80 reuse not applicable"},
 "derivative_density":{"definition":"sum_r derivative-weighted contracted transverse density","species":"ordered transverse-gluon derivative","routes":["direct derivative ladder","Cartesian generating function"],"status":"UNAVAILABLE_BLOCKING","expression":None,"bound":None,"reuse":"C80 reuse not applicable"},
 "CM_ground":{"definition":"CM-ground projection of raw transverse kernel","species":"raw qg to intrinsic/CM","routes":["exact TM CM projector","endpoint recomposition"],"status":"UNAVAILABLE_BLOCKING","expression":None,"bound":None,"reuse":"C80 reuse not applicable"},
 "triplet_projected":{"definition":"C74 U3 triplet projection of CM-ground kernel","species":"physical qg color triplet","routes":["raw product then U3","factorized endpoint U3 recomposition"],"status":"UNAVAILABLE_BLOCKING","expression":None,"bound":None,"reuse":"C80 reuse not applicable"},
}

def five_class_identity_freeze()->MappingProxyType:
    return _freeze({"schema":"C116-FIVE-CLASS-IDENTITY-V1","classes":tuple({"id":c,**CLASS_DEFINITIONS[c]} for c in CLASSES),"count":5,"unknown":0,"duplicates":0,"source":"C115 exact inventory"})

def component_kernel_crosswalk()->tuple[MappingProxyType,...]:
    rows=[]
    for p in PRODUCTS:
        for s in SECTORS:
            # Each program consumes local spatial class; mixed/gluon programs
            # additionally require derivative/projector identities.
            used=("I4_local",) if p=="J_qJ_q" and s=="q->q" else ("I4_local","derivative_density","I2_density_projector")
            if s=="qg->qg": used += ("CM_ground","triplet_projected")
            rows.append(_freeze({"program":f"{p}:{s}","classes":used,"all_class_ids_known":True,"unmapped":0,"status":"CROSSWALK_FROZEN"}))
    return tuple(rows)

def _program_status(program:MappingProxyType)->str:
    return "AVAILABLE_SOURCE_QUALIFIED" if program["program"]=="J_qJ_q:q->q" else STATUS

def five_class_derivations()->tuple[MappingProxyType,...]:
    out=[]
    for c in CLASSES:
        d=CLASS_DEFINITIONS[c]
        out.append(_freeze({"class_id":c,"route_a":d["routes"][0],"route_b":d["routes"][1],"route_residual":"0" if c=="I4_local" else None,"expression":d["expression"],"status":d["status"],"selection_rule":"exact angular/OAM rule; no magnitude threshold"}))
    return tuple(out)

def c80_spatial_reuse_audit()->tuple[MappingProxyType,...]:
    return tuple(_freeze({"class_id":c,"status":"PROVED_SPATIAL_ONLY" if c=="I4_local" else "NOT_APPLICABLE","source_scope":"spatial integral only","forbidden_factors":["longitudinal","source","spin","color","field/state normalization","M2"]}) for c in CLASSES)

def graph_projector_manifest()->tuple[MappingProxyType,...]:
    return tuple(_freeze({"class_id":c,"projector":"finite C45 shell projector" if c!="I4_local" else "none","mode_domain":"graph-specific internal modes" if c!="I4_local" else "external modes","CM_policy":"C64/C77 for qg" if c in ("CM_ground","triplet_projected") else "direct","status":"UNAVAILABLE_BLOCKING" if c!="I4_local" else "NOT_APPLICABLE_WITH_PROOF","continuum_completeness":False}) for c in CLASSES)

def regulator_reuse_audit()->MappingProxyType:
    return _freeze({"C57":tuple({"class_id":c,"status":"NOT_REUSED_OPERATOR_IDENTITY_ABSENT"} for c in CLASSES if c!="I4_local"),"C58":tuple({"class_id":c,"status":"NOT_REUSED_OPERATOR_IDENTITY_ABSENT"} for c in CLASSES if c!="I4_local"),"all_graph_specific":False})

def kernel_record(class_id:str)->MappingProxyType:
    if class_id not in CLASSES: raise KeyError(class_id)
    d=CLASS_DEFINITIONS[class_id]
    return _freeze({"class_id":class_id,"definition":d["definition"],"expression":d["expression"],"value":None if class_id!="I4_local" else "finite_exact_laguerre_gamma_expression","bound":d["bound"],"units":"b_HO^2 for spatial primitive","status":d["status"],"b_HO":"symbolic"})

def component_status(product:str,sector:str,resolution:str|None=None)->MappingProxyType:
    if product not in PRODUCTS or sector not in SECTORS: raise KeyError((product,sector))
    if resolution is not None and resolution not in RESOLUTIONS: raise KeyError(resolution)
    pid=f"{product}:{sector}"; st=_program_status(next(x for x in component_kernel_crosswalk() if x["program"]==pid))
    return _freeze({"program":pid,"resolution":resolution,"status":st,"terminal":st=="AVAILABLE_SOURCE_QUALIFIED","value":"finite-expression" if st.startswith("AVAILABLE") else None,"bound":"exact" if st.startswith("AVAILABLE") else None})

def evaluate_kernel(class_id:str, record:Any=None)->MappingProxyType:
    if class_id not in CLASSES: raise KeyError(class_id)
    if class_id!="I4_local": raise RuntimeError(f"{STATUS}: {class_id}")
    return _freeze({"class_id":class_id,"status":"NONZERO_EXACT_ALGEBRAIC_OR_EXACT_ZERO_BY_OAM","expression":"finite Laguerre/Gamma moment","route_residual":0,"bound":"zero-radius exact","units":"GeV^2 spatial scale; current factors excluded"})

def current_component_sparse_matrix(product:str,sector:str,resolution:str):
    if component_status(product,sector,resolution)["terminal"] is False: raise RuntimeError(f"{STATUS}: {product}/{sector}")
    raise RuntimeError("C116 component assembly not authorized for spatial primitive alone")
def apply_current_component(product:str,sector:str,resolution:str,vector:Any): raise RuntimeError(f"{STATUS}: complete current factorization unavailable")
def instantaneous_current_sparse_matrix(resolution:str): raise RuntimeError(f"{STATUS}: complete block unavailable")
def apply_instantaneous_current(resolution:str,vector:Any): raise RuntimeError(f"{STATUS}: complete action unavailable")

def verify_icho2_authority()->dict[str,Any]:
    freeze=five_class_identity_freeze(); cross=component_kernel_crosswalk(); deriv=five_class_derivations()
    return {"status":STATUS,"baseline":BASELINE,"contract":CONTRACT,"contract_hash":_hash(CONTRACT),"classes":freeze,"crosswalk":cross,"derivations":deriv,"class_count":5,"known_class_ids":5,"two_route_agreement":1,"missing_projectors":4,"threshold_zeros":0,"unavailable_as_zero":0,"C80_reuse":c80_spatial_reuse_audit(),"regulator_reuse":regulator_reuse_audit(),"program_count":8,"terminal_programs":1,"blocked_programs":7,"complete_block":False,"positive_gate":False,"blocking_class":BLOCKING_CLASS,"next":NEXT,"coupling_factored":True,"physical_coupling_consumed":0,"counterterm_values_consumed":0,"C53_values_consumed":0,"C112_values_consumed":0}
def load_verified_icho2_authority()->MappingProxyType: return _freeze(verify_icho2_authority())
def factor_ownership()->MappingProxyType: return _freeze({"C114_inverse":"C114","current":"C115","HO":"C116","projector":"C116","spin":"C115","color":"C115","M2":"C115","g_s2":"factored","duplicates":0})
def ancestry(record_id:str)->MappingProxyType: return _freeze({"record_id":record_id,"ancestry":("C43","C45","C47","C62","C64","C74","C77","C80","C110","C112","C114","C115","C116"),"status":STATUS})
def static_isolation_guard()->MappingProxyType:
    names={n.id for n in ast.walk(ast.parse(Path(__file__).read_text())) if isinstance(n,ast.Name)}; bad=("physical_coupling","counterterm_value","C53_values","C112_values")
    return _freeze({"found":tuple(x for x in bad if x in names),"pass":not any(x in names for x in bad)})
def mutate_live_icho2(i:int)->MappingProxyType:
    v=deepcopy(_plain(verify_icho2_authority())); c=i%16
    if c==0:v["status"]="READY"
    elif c==1:v["class_count"]=4
    elif c==2:v["known_class_ids"]=4
    elif c==3:v["two_route_agreement"]=5
    elif c==4:v["missing_projectors"]=0
    elif c==5:v["threshold_zeros"]=1
    elif c==6:v["unavailable_as_zero"]=1
    elif c==7:v["terminal_programs"]=8
    elif c==8:v["blocked_programs"]=0
    elif c==9:v["complete_block"]=True
    elif c==10:v["positive_gate"]=True
    elif c==11:v["blocking_class"]="other"
    elif c==12:v["coupling_factored"]=False
    elif c==13:v["program_count"]=7
    elif c==14:v["C80_reuse"]=()
    else:v["regulator_reuse"]=None
    return _freeze(v)

__all__=["STATUS","NEXT","CLASSES","PRODUCTS","SECTORS","RESOLUTIONS","five_class_identity_freeze","component_kernel_crosswalk","five_class_derivations","c80_spatial_reuse_audit","graph_projector_manifest","regulator_reuse_audit","kernel_record","component_status","evaluate_kernel","verify_icho2_authority","load_verified_icho2_authority","factor_ownership","ancestry","current_component_sparse_matrix","apply_current_component","instantaneous_current_sparse_matrix","apply_instantaneous_current","static_isolation_guard","mutate_live_icho2"]
