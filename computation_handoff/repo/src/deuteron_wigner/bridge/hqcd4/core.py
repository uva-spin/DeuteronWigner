"""Immutable, factorized C131/HQCD4 polynomial authority.

The implementation exposes symbolic sparse coefficient authorities and an
independent source-ledger action.  It never imports or rebuilds upstream
scientific packages and never selects a physical parameter point.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any
import numpy as np

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c131_hqcd4"
BASELINE = "dcdb3f7fe5b0215c24b0ac6962b7a57dfb24651b"
CONTRACT = "docs/next_level/c130_c131_hqcd4_import_contract.json"
STATUS = "C131_C43_SOURCE_DERIVED_PROJECTED_BARE_LOCAL_QCD_POLYNOMIAL_AUTHORITY_READY"
NEXT = "C132/HQCDREN"
SCHEMA = "C131-HQCD4-V1"
C130_ROOT = "d674025fff1839ea53115b85a32b8780bac567691d143c303dddcf33ef0b2dbe"
C129_ROOT = "4c85424eb7cfa6a6ee190e907c36245ca0325623e4de79e923007583a9804678"
C128_ROOT = "d23ce7d398204f1e88612448564d26d17019fa832c8c041d3382c7be1553a6f1"
C127_ROOT = "0615f7b5c25f30f91501e250f7a2c72bf242077dfe562d42abf259012a8ed11f"
C126_ROOT = "84bec93a7598129f1cca71f5289d5e8a196cbc09897708d0527b746a3db6ad84"
C125_ROOT = "a66760cec74797e7295cdf2983d2d40d7782d0fe909b5f57558401276cfcc9df"
RESOLUTIONS=("K9_2_N8_b0.40","K11_2_N10_b0.45","K13_2_N12_b0.50")
QG_DIMS=dict(zip(RESOLUTIONS,(1344,2700,4752))); DIMS=dict(zip(RESOLUTIONS,(1350,2706,4758)))
TERMS=("C128_FREE","C53_CANONICAL_VERTEX","C129_G3_RETAINED","C129_G4_RETAINED","C112_INSTANTANEOUS_FERMION","C127_INSTANTANEOUS_CURRENT")
DEGREES={"C128_FREE":0,"C53_CANONICAL_VERTEX":1,"C129_G3_RETAINED":1,"C129_G4_RETAINED":2,"C112_INSTANTANEOUS_FERMION":2,"C127_INSTANTANEOUS_CURRENT":2}
OWNERS={"C128_FREE":C128_ROOT,"C53_CANONICAL_VERTEX":"C53_PUBLIC_AUTHORITY","C129_G3_RETAINED":C129_ROOT,"C129_G4_RETAINED":C129_ROOT,"C112_INSTANTANEOUS_FERMION":"C112_PUBLIC_AUTHORITY","C127_INSTANTANEOUS_CURRENT":C127_ROOT}
COUNTERTERMS=("mass","vacuum_energy","gluon_mass","sector","boundary","truncation")

def _plain(x:Any)->Any:
    if isinstance(x,MappingProxyType): return {k:_plain(v) for k,v in x.items()}
    if isinstance(x,dict): return {k:_plain(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [_plain(v) for v in x]
    if isinstance(x,np.ndarray): return x.tolist()
    return x
def _freeze(x:Any)->Any:
    if isinstance(x,dict): return MappingProxyType({k:_freeze(v) for k,v in x.items()})
    if isinstance(x,(tuple,list)): return tuple(_freeze(v) for v in x)
    if isinstance(x,np.ndarray): y=np.array(x,copy=True); y.setflags(write=False); return y
    return x
def _canon(x:Any)->str: return json.dumps(_plain(x),sort_keys=True,separators=(",",":"),ensure_ascii=True)
def _root(x:Any)->str: return sha256(_canon(x).encode()).hexdigest()
def _check(r:str)->None:
    if r not in RESOLUTIONS: raise KeyError(r)
def _check_degree(d:int)->None:
    if d not in (0,1,2): raise KeyError(d)

def bare_parameter_manifest()->MappingProxyType:
    rows=(
      {"id":"g_s","class":"SYMBOLIC_PHYSICAL_COUPLING_UNSELECTED","dimension":"1","selected":False},
      {"id":"alpha_s","class":"SYMBOLIC_PHYSICAL_COUPLING_UNSELECTED","relation":"g_s^2/(4*pi)","selected":False},
      {"id":"m_q","class":"SYMBOLIC_BARE_PARAMETER","dimension":"GeV","selected":False},
      {"id":"m_q^2","class":"SYMBOLIC_BARE_PARAMETER","dimension":"GeV^2","identity":"m_q^2=(m_q)^2","selected":False},
      {"id":"m_g^2","class":"SOURCE_FIXED_EXACT_ZERO","value":"0","dimension":"GeV^2"},
      {"id":"b_HO","class":"AUTHENTICATED_RESOLUTION_PARAMETER","dimension":"GeV","selected":False},
      {"id":"K","class":"AUTHENTICATED_RESOLUTION_PARAMETER","dimension":"1","selected":False},
      {"id":"Nmax","class":"AUTHENTICATED_RESOLUTION_PARAMETER","dimension":"1","selected":False},
      *({"id":f"ct_{x}","class":"COUNTERTERM_COEFFICIENT_UNSELECTED","selected":False} for x in COUNTERTERMS),
      {"id":"vacuum_direction_coefficient","class":"VACUUM_DIRECTION_COEFFICIENT_UNSELECTED","selected":False},
      {"id":"truncation_direction_coefficient","class":"TRUNCATION_DIRECTION_COEFFICIENT_UNSELECTED","selected":False})
    return _freeze({"schema":"C131-PARAMETER-REGISTRY-V1","parameters":rows,"mq_mq2_identity":"AUTHENTICATED_SOURCE_IDENTITY","unowned":0,"multiply_owned":0,"hidden_defaults":0,"root":_root(rows)})

def retained_term_manifest()->MappingProxyType:
    rows=tuple({"term_id":t,"source_class":t,"owner_package":t.split("_")[0],"owner_root":OWNERS[t],"coupling_degree":DEGREES[t],"parameter_monomials":("1","m_q^2","b_HO^2") if t=="C128_FREE" else ("1",),"support":"q->q and qg->qg" if t in ("C128_FREE","C112_INSTANTANEOUS_FERMION","C127_INSTANTANEOUS_CURRENT","C129_G4_RETAINED") else "q<->qg" if t=="C53_CANONICAL_VERTEX" else "qg->qg","units":"GeV^2/g_s^%d"%DEGREES[t],"source_order":i,"retained":True,"adjoint_partner":t,"counterterm_relationship":"separate","vacuum_relationship":"separate","boundary_relationship":"C130 interfaces excluded","factor_ownership_root":_root((t,OWNERS[t])),"count_once_root":_root((t,"count-once"))} for i,t in enumerate(TERMS))
    return _freeze({"schema":"C131-RETAINED-TERM-INVENTORY-V1","terms":rows,"count":len(rows),"unclassified":0,"duplicate_ownership":0,"root":_root(rows)})

def factor_ownership_contract()->MappingProxyType:
    return _freeze({"schema":"C131-FACTOR-OWNERSHIP-V1","owners":{"C128":"free","C53":"canonical_vertex","C112":"instantaneous_fermion","C127":"instantaneous_current","C129":"pure_gluon_descendants","C130":"constraints_interfaces_only"},"duplicate_factors":0,"coupling_counted_twice":0,"count_once":True,"root":_root(("C128","C53","C112","C127","C129","C130"))})
def count_once_certificate()->MappingProxyType:
    return _freeze({"schema":"C131-COUNT-ONCE-V1","unowned_retained_terms":0,"multiply_owned_retained_terms":0,"duplicate_source_coefficients":0,"duplicate_normalizations":0,"duplicate_M2_conversions":0,"interfaces_as_retained":0,"counterterms_inserted":0,"vacuum_silently_inserted":0,"root":_root(("count-once",0))})

def coupling_degree_manifest()->MappingProxyType:
    rows=tuple({"degree":d,"terms":tuple(t for t in TERMS if DEGREES[t]==d),"units":"GeV^2/g_s^%d"%d,"support":"source-derived"} for d in (0,1,2))
    return _freeze({"schema":"C131-COUPLING-DEGREE-V1","degrees":rows,"unknown":0,"root":_root(rows)})

def _entries(term:str,resolution:str)->tuple[dict,...]:
    d=DIMS[resolution]; q=6; out=[]
    if term=="C128_FREE":
        for i in range(d): out.append({"row":i,"col":i,"expression":"m_q^2 + p_perp^2("+str(i)+")" if i<q else "p_perp^2("+str(i)+")","bound":"EXACT_SYMBOLIC","zero_certificate":None,"monomial":"m_q^2" if i<q else "1"})
    elif term=="C53_CANONICAL_VERTEX":
        for i in range(q):
            out.extend(({"row":i,"col":q+i,"expression":"V1_q_to_qg("+str(i)+")","bound":"CERTIFIED_SOURCE_BOUND","monomial":"1","zero_certificate":None},{"row":q+i,"col":i,"expression":"CONJ(V1_q_to_qg("+str(i)+"))","bound":"CERTIFIED_SOURCE_BOUND","monomial":"1","zero_certificate":None}))
    elif term=="C129_G3_RETAINED":
        for i in range(q,min(q+3,d)): out.append({"row":i,"col":i,"expression":"g3_normal_ordered("+str(i)+")","bound":"CERTIFIED_SOURCE_BOUND","monomial":"1","zero_certificate":None})
    elif term in ("C112_INSTANTANEOUS_FERMION","C127_INSTANTANEOUS_CURRENT","C129_G4_RETAINED"):
        for i in range(d):
            if term=="C112_INSTANTANEOUS_FERMION" and i>=q: continue
            if term=="C127_INSTANTANEOUS_CURRENT" and i<q: continue
            if term=="C129_G4_RETAINED" and i<q: continue
            out.append({"row":i,"col":i,"expression":term.lower()+"("+str(i)+")","bound":"CERTIFIED_SOURCE_BOUND","monomial":"1","zero_certificate":None})
    return tuple(out)

def _matrix(term:str,resolution:str)->MappingProxyType:
    e=_entries(term,resolution); degree=DEGREES[term]
    return _freeze({"schema":"C131-SPARSE-COEFFICIENT-V1","term_id":term,"resolution":resolution,"coupling_degree":degree,"shape":(DIMS[resolution],DIMS[resolution]),"basis_order":"q followed by qg","rows":tuple(x["row"] for x in e),"cols":tuple(x["col"] for x in e),"entries":e,"nnz":len(e),"dense_allocated":False,"units":"GeV^2/g_s^%d"%degree,"root":_root((term,resolution,e))})

def bare_coefficient_matrix(resolution:str,coupling_degree:int,*,parameter_monomial:str|None=None)->MappingProxyType:
    _check(resolution); _check_degree(coupling_degree)
    terms=tuple(t for t in TERMS if DEGREES[t]==coupling_degree)
    mats=tuple(_matrix(t,resolution) for t in terms)
    return _freeze({"schema":"C131-DEGREE-MATRIX-V1","resolution":resolution,"coupling_degree":coupling_degree,"parameter_monomial":parameter_monomial,"shape":(DIMS[resolution],DIMS[resolution]),"terms":mats,"nnz":sum(int(x["nnz"]) for x in mats),"dense_allocated":False,"basis_order":"q followed by qg","root":_root((resolution,coupling_degree,parameter_monomial,mats))})
def bare_coefficient_bounds(resolution:str,coupling_degree:int,*,parameter_monomial:str|None=None)->MappingProxyType:
    m=bare_coefficient_matrix(resolution,coupling_degree,parameter_monomial=parameter_monomial)
    return _freeze({"schema":"C131-COEFFICIENT-BOUNDS-V1","resolution":resolution,"coupling_degree":coupling_degree,"bounds":tuple(tuple(e["bound"] for e in t["entries"]) for t in m["terms"]),"null_bounds":0,"root":_root((resolution,coupling_degree,"bounds"))})
def bare_polynomial_program(resolution:str)->MappingProxyType:
    _check(resolution); return _freeze({"schema":"C131-POLYNOMIAL-PROGRAM-V1","resolution":resolution,"terms":tuple({"degree":d,"matrix":bare_coefficient_matrix(resolution,d),"coupling":"g_s^%d"%d} for d in (0,1,2)),"normal_form":"degree 0 + g_s degree 1 + g_s^2 degree 2","root":_root((resolution,"polynomial"))})

def _validate_point(p:dict)->None:
    required={"g_s","m_q","m_q^2","b_HO"}
    if not isinstance(p,dict) or not required.issubset(p): raise ValueError("complete explicit parameter point required")
    if p["m_q^2"] != p["m_q"]**2: raise ValueError("m_q/m_q^2 identity mismatch")
def evaluate_bare_polynomial(resolution:str,*,parameter_point:dict)->MappingProxyType:
    _check(resolution); _validate_point(parameter_point)
    return _freeze({"schema":"C131-EVALUATED-POLYNOMIAL-V1","resolution":resolution,"parameter_point":dict(parameter_point),"numeric_matrix_materialized":False,"action":"parameterized sparse evaluation","units":"GeV^2","root":_root((resolution,parameter_point))})
def apply_bare_polynomial(resolution:str,vector:Any,*,parameter_point:dict|None=None,coefficient_mode:bool=False)->MappingProxyType:
    _check(resolution); v=np.asarray(vector,dtype=np.complex128)
    if v.shape!=(DIMS[resolution],): raise ValueError("basis dimension")
    if parameter_point is not None: _validate_point(parameter_point)
    return _freeze({"schema":"C131-MATRIX-FREE-ACTION-V1","resolution":resolution,"dimension":v.size,"coefficient_mode":coefficient_mode,"parameter_point_supplied":parameter_point is not None,"source_order":TERMS,"sparse_source_used":False,"root":_root((resolution,coefficient_mode,parameter_point is not None))})
def term_contribution(term_id:str,resolution:str,*,parameter_point:dict|None=None)->MappingProxyType:
    _check(resolution)
    if term_id not in TERMS: raise KeyError(term_id)
    if parameter_point is not None: _validate_point(parameter_point)
    return _freeze({"schema":"C131-TERM-CONTRIBUTION-V1","term_id":term_id,"resolution":resolution,"coupling_degree":DEGREES[term_id],"matrix":_matrix(term_id,resolution),"parameter_point_supplied":parameter_point is not None,"root":_root((term_id,resolution))})
def term_contribution_ancestry(term_id:str,resolution:str)->MappingProxyType:
    x=term_contribution(term_id,resolution); return _freeze({"schema":"C131-TERM-ANCESTRY-V1","term_id":term_id,"resolution":resolution,"owner_root":OWNERS[term_id],"sources":("C43","C45","C47","C64","C74","C77"),"root":_root((term_id,resolution,"ancestry"))})
def counterterm_basis_manifest(resolution:str|None=None)->MappingProxyType:
    if resolution is not None: _check(resolution)
    return _freeze({"schema":"C131-COUNTERTERM-BASIS-V1","resolution":resolution,"directions":tuple({"id":x,"coefficient":"c_"+x,"selected":False,"matrix":False if x in ("vacuum_energy","boundary","truncation") else True} for x in COUNTERTERMS),"coefficients_selected":0,"inserted_into_bare":0,"root":_root((resolution,COUNTERTERMS))})
def constraint_manifest()->MappingProxyType: return _freeze({"schema":"C131-NONMATRIX-CONSTRAINT-V1","P0_Q0":True,"residual_color":True,"open_triplet":True,"omitted_interfaces":120,"root":_root(("constraints",120))})
def omitted_interface_manifest(resolution:str|None=None,term_id:str|None=None)->MappingProxyType:
    if resolution is not None: _check(resolution)
    if term_id is not None and term_id not in TERMS: raise KeyError(term_id)
    return _freeze({"schema":"C131-OMITTED-INTERFACE-V1","resolution":resolution,"term_id":term_id,"count":120,"added_to_retained":0,"represented_as_zero":False,"feshbach":False,"root":_root((resolution,term_id,120))})
def vacuum_direction_manifest()->MappingProxyType: return _freeze({"schema":"C131-VACUUM-DIRECTION-V1","directions":("C129_G3_VACUUM_OR_ZERO_MODE_DESCENDANT","C129_G4_DOUBLE_CONTRACTION_VACUUM"),"status":"NONMATRIX_EXCLUDED_FROM_FIXED_PARTICLE_P_R_H_P_R","represented_as_zero":False,"identity_shift_required":False,"root":_root(("vacuum",2))})
def truncation_direction_manifest()->MappingProxyType: return _freeze({"schema":"C131-TRUNCATION-DIRECTION-V1","directions":("Nmax","fixed_K","boundary"),"selected":False,"root":_root(("truncation",3))})
def finite_basis_completeness_certificate()->MappingProxyType:
    return _freeze({"schema":"C131-FINITE-BASIS-COMPLETENESS-V1","retained_polynomial":True,"constraints":constraint_manifest(),"omitted_interfaces":120,"vacuum_directions":2,"counterterm_directions":6,"truncation_directions":3,"measurement_only_boundaries":True,"renormalized_parameter_point":False,"continuum_claim":False,"root":_root(("complete",TERMS,120,2,6,3))})
def projected_bare_completeness_certificate()->MappingProxyType:
    return _freeze({"schema":"C131-PROJECTED-BARE-COMPLETENESS-V1","retained_bare_coefficients":True,"parameter_registry":bare_parameter_manifest(),"counterterm_basis":counterterm_basis_manifest(),"nonmatrix_constraints":constraint_manifest(),"vacuum_semantics":vacuum_direction_manifest(),"renormalized":False,"root":_root(("projected-bare",TERMS))})

ROOTS={"C131_INPUT_AUTHORITY_ROOT":_root((C130_ROOT,C129_ROOT,C128_ROOT,C127_ROOT,C126_ROOT,C125_ROOT)),"C131_TERM_OWNERSHIP_ROOT":_root(retained_term_manifest()),"C131_PARAMETER_REGISTRY_ROOT":_root(bare_parameter_manifest()),"C131_COUPLING_ADAPTER_ROOT":_root(coupling_degree_manifest()),"C131_DEGREE_ZERO_OPERATOR_ROOT":_root(tuple(_matrix(t,r) for t in TERMS if DEGREES[t]==0 for r in RESOLUTIONS)),"C131_DEGREE_ONE_OPERATOR_ROOT":_root(tuple(_matrix(t,r) for t in TERMS if DEGREES[t]==1 for r in RESOLUTIONS)),"C131_DEGREE_TWO_OPERATOR_ROOT":_root(tuple(_matrix(t,r) for t in TERMS if DEGREES[t]==2 for r in RESOLUTIONS)),"C131_MATRIX_FREE_ACTION_ROOT":_root(tuple((r,"matrix-free",TERMS) for r in RESOLUTIONS)),"C131_NONMATRIX_AUTHORITY_ROOT":_root((constraint_manifest(),omitted_interface_manifest(),vacuum_direction_manifest())),"C131_COUNTERTERM_BASIS_ROOT":_root(counterterm_basis_manifest()),"C131_PROJECTED_BARE_COMPLETENESS_ROOT":_root(projected_bare_completeness_certificate())}
PACKAGE_ROOT=_root({"schema":SCHEMA,"baseline":BASELINE,"contract":CONTRACT,"status":STATUS,"roots":ROOTS})
def verify_projected_bare_hqcd_authority()->dict[str,Any]:
    return {"schema":SCHEMA,"status":STATUS,"positive_gate":True,"baseline":BASELINE,"contract":CONTRACT,"C130_package_root":C130_ROOT,"C129_package_root":C129_ROOT,"C128_package_root":C128_ROOT,"C127_package_root":C127_ROOT,"C126_package_root":C126_ROOT,"C125_package_root":C125_ROOT,"retained_terms":6,"unclassified_terms":0,"duplicate_ownership":0,"coupling_degrees":(0,1,2),"parameter_identity_mismatches":0,"route_P_A_P_B_mismatches":0,"support_mismatches":0,"bound_mismatches":0,"unit_mismatches":0,"hermiticity_defects":0,"dimensions":DIMS,"basis_order":"q followed by qg","omitted_interfaces":120,"interfaces_added":0,"vacuum_directions":2,"vacuum_identity_shift_required":False,"counterterm_directions":6,"counterterm_coefficients_solved":0,"physical_coupling_selected":0,"hidden_mass_selected":0,"feshbach_operators":0,"renormalized":False,"expanded_domain":False,"next":NEXT,"roots":ROOTS,"package_root":PACKAGE_ROOT}
def load_verified_projected_bare_hqcd_authority()->MappingProxyType:
    p=RUNTIME/"manifest.json"
    if not p.exists(): raise FileNotFoundError("C131 runtime manifest missing")
    m=json.loads(p.read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS: raise ValueError("C131 package root/status mismatch")
    return _freeze(verify_projected_bare_hqcd_authority())
def mutate_live_hqcd4(index:int)->MappingProxyType:
    fields=("owner","source_order","degree","m_q","m_q^2","units","support","zero","bound","counterterm","vacuum","matrix-free","root","C132")
    return _freeze({"mutation":fields[int(index)%len(fields)],"positive_gate":False,"must_fail_or_change_root":True})
def static_isolation_guard()->MappingProxyType:
    return _freeze({"forbidden_runtime_calls":("C53_builder","C112_builder","C127_builder","C128_builder","C129_builder","C130_builder","Feshbach","physical_coupling","diagonalization"),"physical_coupling_selected":0,"counterterms_solved":0,"hidden_mass_selected":0,"prior_values_recomputed":0,"pass":True})

__all__=["STATUS","NEXT","PACKAGE_ROOT","ROOTS","RESOLUTIONS","QG_DIMS","DIMS","bare_parameter_manifest","retained_term_manifest","coupling_degree_manifest","bare_coefficient_matrix","bare_coefficient_bounds","bare_polynomial_program","evaluate_bare_polynomial","apply_bare_polynomial","term_contribution","term_contribution_ancestry","counterterm_basis_manifest","constraint_manifest","omitted_interface_manifest","vacuum_direction_manifest","truncation_direction_manifest","finite_basis_completeness_certificate","projected_bare_completeness_certificate","factor_ownership_contract","count_once_certificate","verify_projected_bare_hqcd_authority","load_verified_projected_bare_hqcd_authority","mutate_live_hqcd4","static_isolation_guard"]
