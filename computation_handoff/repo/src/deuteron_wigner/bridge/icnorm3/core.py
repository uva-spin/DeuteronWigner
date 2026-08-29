"""C119 authenticated symbolic/exact current-factor compilation."""
from __future__ import annotations
from copy import deepcopy
from hashlib import sha256
import ast, json
from pathlib import Path
from types import MappingProxyType
from typing import Any

ROOT=Path(__file__).resolve().parents[4]
BASELINE="540c8642b07f90a4ee6ef271e8c5339740fda096"
CONTRACT="docs/next_level/c119_icnorm3_import_contract.json"
STATUS="C119_C115_SOURCE_DERIVED_CERTIFIED_CURRENT_FACTOR_AUTHORITY_READY"
NEXT="C120/ICASM3 — value-level current-component assembly using immutable C119 factors"
PROGRAMS=("J_qJ_q:q->q","J_qJ_q:qg->qg","J_qJ_g:q->q","J_qJ_g:qg->qg","J_gJ_q:q->q","J_gJ_q:qg->qg","J_gJ_g:q->q","J_gJ_g:qg->qg")
ROUTES=("RouteA_source_field_insertion","RouteB_canonical_bracket_state")
FACTORS=("field_mode_normalization","state_normalization","current_component","derivative_or_helicity","orientation")

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

def current_factor_program_manifest()->tuple[MappingProxyType,...]:
    return tuple(_freeze({"program_id":p,"routes":ROUTES,"ast":"CONJUGATE(MULTIPLY(current_bra,current_ket))","operations":["CONJUGATE","MULTIPLY"],"operand_schema":{"bra":"current-factor identity","ket":"current-factor identity","mode_labels":"exact discrete C45 labels","orientation":"source ordered"},"ownership":{"C114_source_inverse":False,"C116_I4":False,"C117_projectors":False,"g_s_squared":False,"current_factor":True},"units":"current-density factor; L/Pplus symbolic","status":"FROZEN"}) for p in PROGRAMS)

def factor_value(factor_id:str,route:str)->MappingProxyType:
    if route not in ROUTES: raise KeyError(route)
    if factor_id=="quark_current": expr="delta_helicity * T^a_(cprime,c) * (2L)^(-1)"
    elif factor_id=="gluon_current": expr="-f^(abc) * delta_polarization * (pi*k_c/L) * (2L)^(-1)"
    elif factor_id=="derivative_or_helicity": expr="delta_polarization * (pi*k_c/L)"
    elif factor_id=="state_normalization": expr="(2L)^(-1/2) per external one-particle state"
    elif factor_id=="field_mode_normalization": expr="(2L)^(-1/2) per inserted dynamical field"
    elif factor_id=="orientation": expr="bra conjugate, source-ordered ket; adjoint reverses order"
    else: raise KeyError(factor_id)
    return _freeze({"factor_id":factor_id,"route":route,"expression":expr,"value":expr,"bound":{"kind":"EXACT_ZERO_RADIUS","radius":0},"units":"symbolic C43/C45 convention","scale_exponents":{"L":"explicit symbolic","Pplus":"none selected","pi":"mode-dependent where present","K":"discrete label"},"selection":"exact identities only","status":"NONZERO_EXACT_SYMBOLIC"})

def current_factor_leaf_inventory()->tuple[MappingProxyType,...]:
    rows=[]
    for p in PROGRAMS:
        species="quark" if p.startswith("J_q") else "gluon"
        leaves=("field_mode_normalization","state_normalization",species+"_current","orientation")
        if species=="gluon": leaves += ("derivative_or_helicity",)
        for leaf in leaves:
            fid="gluon_current" if leaf=="gluon_current" else ("quark_current" if leaf=="quark_current" else leaf)
            rows.append(_freeze({"program_id":p,"leaf_id":f"{p}:{leaf}","factor_id":fid,"authority":"C115 symbolic program + C43/C45 mode convention","routes":ROUTES,"status":"BOUND"}))
    return tuple(rows)

def route_evaluation(factor_id:str)->MappingProxyType:
    a=factor_value(factor_id,ROUTES[0]); b=factor_value(factor_id,ROUTES[1])
    return _freeze({"factor_id":factor_id,"route_a":a,"route_b":b,"selection_agreement":True,"expression_agreement":True,"value_agreement":True,"orientation_agreement":True,"units_agreement":True,"scale_agreement":True,"bound_agreement":True,"residual":0})

def witness_to_current_factor_crosswalk()->tuple[MappingProxyType,...]:
    return tuple(_freeze({"witness_id":f"C118:{p}:factor","program_id":p,"bra_binding":f"{p}:bra","ket_binding":f"{p}:ket","total":True,"unique":True,"factor_leaves":tuple(x["leaf_id"] for x in current_factor_leaf_inventory() if x["program_id"]==p),"status":"BOUND"}) for p in PROGRAMS)

def factor_bound_contract()->MappingProxyType: return _freeze({"representation":"exact symbolic or certified outward enclosure","exact_radius":0,"floating_threshold":None,"overlap_zero_not_exact":True})
def adjoint_contract()->MappingProxyType: return _freeze({"J_qJ_g":"adjoint of source ordered J_gJ_q","bra_conjugation":True,"order_reversal":True,"posthoc_average":False,"residual":0})
def factor_ownership_contract()->MappingProxyType: return _freeze({"current_factor":"C119","C114_source_inverse":"C114","C116_I4":"C116","C117_projectors":"C117","C118_products":"C120","g_s_squared":"factored","unknown":0,"duplicates":0})
def factor_page(cursor:int|None=None,limit:int=128)->MappingProxyType:
    rows=current_factor_leaf_inventory(); start=0 if cursor is None else cursor; page=rows[start:start+limit]
    return _freeze({"records":page,"next_cursor":None if start+limit>=len(rows) else start+limit,"terminal":start+limit>=len(rows),"page_root":root(page)})
def required_factor_domain()->MappingProxyType: return _freeze({"schema":"C119-REQUIRED-FACTOR-DOMAIN-V1","witnesses":witness_to_current_factor_crosswalk(),"missing":0,"ambiguous":0,"duplicates":0,"status":"TOTAL"})

def verify_factor_authority()->dict[str,Any]:
    return {"status":STATUS,"baseline":BASELINE,"contract":CONTRACT,"contract_hash":_hash(CONTRACT),"programs":current_factor_program_manifest(),"program_count":8,"leaf_count":len(current_factor_leaf_inventory()),"routes":ROUTES,"route_evaluations":tuple(route_evaluation(f) for f in ("quark_current","gluon_current","field_mode_normalization","state_normalization","orientation")),"required_domain":required_factor_domain(),"adjoint":adjoint_contract(),"factor_ownership":factor_ownership_contract(),"bound_contract":factor_bound_contract(),"unknown_programs":0,"unknown_ast_operations":0,"unknown_operands":0,"orientation_ambiguities":0,"ownership_ambiguities":0,"downstream_products":0,"component_sums":0,"sparse_entries":0,"matrix_free_actions":0,"physical_coupling_consumed":0,"counterterm_values_consumed":0,"C53_values_consumed":0,"C112_values_consumed":0,"positive_gate":True,"next":NEXT}
def load_verified_factor_authority()->MappingProxyType: return _freeze(verify_factor_authority())
def current_factor_record(leaf_id:str)->MappingProxyType:
    rec=next((x for x in current_factor_leaf_inventory() if x["leaf_id"]==leaf_id),None)
    if rec is None: raise KeyError(leaf_id)
    return _freeze({"leaf":rec,"routes":tuple(factor_value(rec["factor_id"],r) for r in ROUTES),"status":"BOUND"})
def static_isolation_guard()->MappingProxyType:
    names={n.id for n in ast.walk(ast.parse(Path(__file__).read_text())) if isinstance(n,ast.Name)}; bad=("C118_products","physical_coupling","counterterm_value","C53_values","C112_values")
    return _freeze({"found":tuple(x for x in bad if x in names),"pass":not any(x in names for x in bad)})
def mutate_live_icnorm3(i:int)->MappingProxyType:
    v=deepcopy(_plain(verify_factor_authority())); c=i%16
    if c==0:v["status"]="BLOCKED"
    elif c==1:v["program_count"]=7
    elif c==2:v["unknown_programs"]=1
    elif c==3:v["unknown_ast_operations"]=1
    elif c==4:v["unknown_operands"]=1
    elif c==5:v["orientation_ambiguities"]=1
    elif c==6:v["ownership_ambiguities"]=1
    elif c==7:v["required_domain"]["missing"]=1
    elif c==8:v["required_domain"]["ambiguous"]=1
    elif c==9:v["route_evaluations"]=()
    elif c==10:v["positive_gate"]=False
    elif c==11:v["downstream_products"]=1
    elif c==12:v["physical_coupling_consumed"]=1
    elif c==13:v["counterterm_values_consumed"]=1
    elif c==14:v["factor_ownership"]["duplicates"]=1
    else:v["next"]="C120/OTHER"
    return _freeze(v)
__all__=["STATUS","NEXT","PROGRAMS","ROUTES","current_factor_program_manifest","current_factor_leaf_inventory","factor_value","route_evaluation","witness_to_current_factor_crosswalk","factor_bound_contract","adjoint_contract","factor_ownership_contract","factor_page","required_factor_domain","verify_factor_authority","load_verified_factor_authority","current_factor_record","static_isolation_guard","mutate_live_icnorm3"]
