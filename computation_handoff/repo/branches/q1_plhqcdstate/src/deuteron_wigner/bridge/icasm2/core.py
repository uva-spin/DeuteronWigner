"""C118 certified component assembly boundary; no fabricated values."""
from __future__ import annotations
from copy import deepcopy
from hashlib import sha256
import ast, json
from pathlib import Path
from types import MappingProxyType
from typing import Any

ROOT=Path(__file__).resolve().parents[4]
BASELINE="c8cea55b9ba6de3477461d531420948c838789ee"
CONTRACT="docs/next_level/c118_icasm2_import_contract.json"
STATUS="C118_ICASM2_COMPONENT_EVALUATION_INCOMPLETE"
NEXT="C119/ICNORM3 — executable diagonal current-factor normalization/value authority"
PRODUCTS=("J_qJ_q","J_qJ_g","J_gJ_q","J_gJ_g")
SECTORS=("q->q","qg->qg")
PROGRAMS=tuple(f"{p}:{s}" for p in PRODUCTS for s in SECTORS)
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

def component_program_freeze()->tuple[MappingProxyType,...]:
    return tuple(_freeze({"component":p,"source_order":"C114 left/right current order","factors":("C114_source","C114_inverse_partial_squared","C115_current","C115_state_normalization","C115_spin","C115_color","C116_I4_local","C117_projectors","C115_M2"),"witness_domain":"source-ordered graph-conditioned finite domain","status":STATUS,"missing_factor":"C115 executable current-factor value/bound record"}) for p in PROGRAMS)
def source_witness_domain(component:str)->MappingProxyType:
    if component not in PROGRAMS: raise KeyError(component)
    return _freeze({"schema":"C118-WITNESS-DOMAIN-V1","component":component,"domain":"finite C45/C117 graph-conditioned witnesses","source_order":True,"count_once":True,"missing":0,"ambiguous":0,"status":"DOMAIN_CLOSED","values":"blocked at current-factor evaluation"})
def component_status(product:str,sector:str,resolution:str|None=None)->MappingProxyType:
    if product not in PRODUCTS or sector not in SECTORS: raise KeyError((product,sector))
    if resolution is not None and resolution not in RESOLUTIONS: raise KeyError(resolution)
    return _freeze({"component":f"{product}:{sector}","resolution":resolution,"status":STATUS,"terminal":False,"value":None,"bound":None,"missing_factor":"C115 executable current-factor value/bound record","unavailable_as_zero":False})
def primitive_authority_validation()->MappingProxyType:
    return _freeze({"C114":True,"C115_current_factors":"symbolic only; no executable value/bound","C116_I4":True,"C117_projectors":True,"unknown_primitive_statuses":1,"status":STATUS})
def factor_ownership_contract()->MappingProxyType:
    return _freeze({"owners":{"C114_source_inverse":"C114","current_factors":"C115","I4":"C116","projectors":"C117","M2":"C115","gs2":"factored"},"unknown":1,"duplicates":0,"status":STATUS})
def source_witness_manifest()->MappingProxyType:
    return _freeze({"schema":"C118-WITNESS-MANIFEST-V1","components":PROGRAMS,"all_domains":"closed structurally","missing":0,"ambiguous":0,"value_status":"blocked"})
def component_sparse_matrix(product:str,sector:str,resolution:str): raise RuntimeError(f"{STATUS}: {product}/{sector} lacks executable current-factor value authority")
def component_sparse_bounds(product:str,sector:str,resolution:str): raise RuntimeError(f"{STATUS}: certified bound unavailable")
def apply_component(product:str,sector:str,resolution:str,vector:Any): raise RuntimeError(f"{STATUS}: matrix-free value action unavailable")
def instantaneous_current_sparse_matrix(resolution:str): raise RuntimeError(f"{STATUS}: complete block fail-closed")
def apply_instantaneous_current(resolution:str,vector:Any): raise RuntimeError(f"{STATUS}: complete action fail-closed")
def mixed_current_adjoint()->MappingProxyType: return _freeze({"J_qJ_g":"not assembled","J_gJ_q":"source-adjoint relation frozen","posthoc_average":False,"status":STATUS})
def contraction_regulator_manifest()->MappingProxyType: return _freeze({"graphs":4,"finite_shell":"C117 authority","counterterms":"coefficient unavailable","C57_reuse":False,"C58_reuse":False})
def counterterm_direction_manifest(resolution:str|None=None)->MappingProxyType: return _freeze({"resolution":resolution,"directions":tuple({"component":p,"coefficient":"UNAVAILABLE"} for p in PROGRAMS),"bare_included":False})
def verify_assembly_authority()->dict[str,Any]:
    return {"status":STATUS,"baseline":BASELINE,"contract":CONTRACT,"contract_hash":_hash(CONTRACT),"programs":component_program_freeze(),"program_count":8,"witness_domain":source_witness_manifest(),"primitive_validation":primitive_authority_validation(),"factor_ownership":factor_ownership_contract(),"C114_cross_sector_exact_zeros":8,"diagonal_terminal":0,"diagonal_blocked":8,"missing_value_factor":"C115 executable current-factor value/bound record","product_bound_status":"UNAVAILABLE","M2_units":"GeV^2/g_s^2 required but not terminal","boost_covariance":False,"hermiticity":"not evaluable without values","component_assembly_complete":False,"complete_block":False,"positive_gate":False,"next":NEXT,"physical_coupling_consumed":0,"counterterm_values_consumed":0,"C53_values_consumed":0,"C112_values_consumed":0}
def load_verified_assembly_authority()->MappingProxyType: return _freeze(verify_assembly_authority())
def static_isolation_guard()->MappingProxyType:
    names={n.id for n in ast.walk(ast.parse(Path(__file__).read_text())) if isinstance(n,ast.Name)}; bad=("physical_coupling","counterterm_value","C53_values","C112_values")
    return _freeze({"found":tuple(x for x in bad if x in names),"pass":not any(x in names for x in bad)})
def mutate_live_icasm2(i:int)->MappingProxyType:
    v=deepcopy(_plain(verify_assembly_authority())); c=i%16
    if c==0:v["status"]="READY"
    elif c==1:v["program_count"]=7
    elif c==2:v["diagonal_terminal"]=8
    elif c==3:v["diagonal_blocked"]=0
    elif c==4:v["missing_value_factor"]="none"
    elif c==5:v["product_bound_status"]="CERTIFIED"
    elif c==6:v["M2_units"]="GeV^2"
    elif c==7:v["boost_covariance"]=True
    elif c==8:v["component_assembly_complete"]=True
    elif c==9:v["complete_block"]=True
    elif c==10:v["positive_gate"]=True
    elif c==11:v["witness_domain"]["missing"]=1
    elif c==12:v["factor_ownership"]["duplicates"]=1
    elif c==13:v["physical_coupling_consumed"]=1
    elif c==14:v["counterterm_values_consumed"]=1
    else:v["next"]="C119/OTHER"
    return _freeze(v)
__all__=["STATUS","NEXT","PRODUCTS","SECTORS","PROGRAMS","component_program_freeze","source_witness_domain","component_status","primitive_authority_validation","factor_ownership_contract","source_witness_manifest","component_sparse_matrix","component_sparse_bounds","apply_component","instantaneous_current_sparse_matrix","apply_instantaneous_current","mixed_current_adjoint","contraction_regulator_manifest","counterterm_direction_manifest","verify_assembly_authority","load_verified_assembly_authority","static_isolation_guard","mutate_live_icasm2"]
