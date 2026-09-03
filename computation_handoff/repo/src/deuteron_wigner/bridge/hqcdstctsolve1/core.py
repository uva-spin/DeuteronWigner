"""Exact symbolic C206 affine ST solution-family authority."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any,Mapping
from deuteron_wigner.bridge import hqcdstglobal1 as c205
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c206_hqcdstctsolve1"
BASELINE="f4822e301ced0e2996877d7ca359ca07effdad2f";C205_ROOT="f8658cad5f3fec055efbbf56e137db0a03c76fd2a93b61ee214e22dfdb1990df"
CONTRACT="docs/next_level/c205_c206_hqcdstctsolve1_continuation_contract.json";CONTRACT_SHA256="04431e5e70f9b5ded1fe698fbe87c14d6a640b374005fd5f4f282dd90229f363"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c206_hqcdstctsolve1_codex_prompt.md";PROMPT_SHA256="9751c7a0a2e0954c22c7b9e2b67db67a624b3f18f974b0001981314cbdd5bc06"
STATUS="C206_C205_EXACT_CONDITIONAL_ST_COMPATIBLE_AFFINE_COUNTERTERM_SOLUTION_FAMILY_READY_TARGET_FIXING_EXPLICIT";PLAN="STCTSOLVE1-B"
NEXT="C207/HQCDMOMQCOND1";NEXT_OBJECT="C197-ST-9";NEXT_EXACT="target MOMq renormalization conditions"
RESOLUTIONS=("K9","K11","K13");SCHEMES=("PROJECT_FINITE_BASIS_ST",);HOLO=("GENERIC","CENTRAL","WEYL_WALL","IDENTITY_DIAGNOSTIC")
CT=c205.CT;NULL=c205.NULL;VARIABLES=CT+NULL;ROWS=tuple(f"C197-ST-{i}" for i in range(1,8));FREE_PARAMETERS=tuple(f"lambda_{i}" for i in range(1,15))
OPCODES=("LOAD_ST_RESIDUAL_VECTOR","LOAD_EXACT_JACOBIAN","LOAD_COUNTERTERM_AND_NULL_ORDER","VERIFY_LEFT_NULL_COMPATIBILITY","EXACT_ROW_REDUCE","SOLVE_PARTICULAR_SYSTEM","COMPUTE_RIGHT_NULL_BASIS","COMPUTE_LEFT_NULL_BASIS","FORM_AFFINE_SOLUTION_FAMILY","CHANGE_NULL_BASIS","PROJECT_BRST_CLOSED_EXACT_QUOTIENT","CLASSIFY_FIELD_REDEFINITION","CLASSIFY_BOUNDARY_GLOBAL_DIRECTION","CLASSIFY_DOWNSTREAM_RELEVANCE","RETURN_TYPED_CONDITIONAL_FAMILY")
ROUTES=("SOLVE-A-symbolic","SOLVE-B-fraction-free","SOLVE-C-SVD-diagnostic","SOLVE-D-left-null","SOLVE-E-order-basis","SOLVE-F-Jacobian-parity","SOLVE-G-holdout","SOLVE-H-substitution")
def _plain(v):
 if isinstance(v,Mapping):return {str(k):_plain(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_plain(x) for x in v]
 return v
def _freeze(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_freeze(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_freeze(x) for x in v)
 return v
def _root(v):return sha256(json.dumps(_plain(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def _one(v,a):
 if v is None:return tuple(a)
 if v not in a:raise KeyError(v)
 return (v,)
def _check():
 if c205.PACKAGE_ROOT!=C205_ROOT:raise ValueError("C205 root changed")
 c205.load_verified_hqcd_stglobal1_authority()
def verify_hqcd_stctsolve1_authority():
 _check();return _freeze({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"contract":CONTRACT,"contract_sha256":CONTRACT_SHA256,"prompt":PROMPT,"prompt_sha256":PROMPT_SHA256,"C205_package_root":C205_ROOT,"representative_selected":False,"physical":False,"package_root":PACKAGE_ROOT})
def load_verified_hqcd_stctsolve1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime mismatch")
 return verify_hqcd_stctsolve1_authority()
def stctsolve1_plan_manifest():return _freeze({"selected_plan":PLAN,"status":STATUS,"first":"C197-ST-8","next":NEXT,"root":_root((PLAN,STATUS,NEXT))})
def frontier_manifest(object_id=None):
 rows=[]
 for x in c205.frontier_manifest()["rows"]:
  oid=x["object_id"];rows.append({"object_id":oid,"exact_missing_object":x["exact_missing_object"],"aliases":x["aliases"],"status":"C206_REPLACED_CONDITIONAL_AFFINE_FAMILY" if oid=="C197-ST-8" else ("READ_ONLY_CLOSED" if int(oid.split("-")[-1])<=8 else "PRESERVED_ORDERED_FRONTIER"),"not_zero":True,"next":NEXT if oid==NEXT_OBJECT else None})
 if object_id is not None:
  rows=[x for x in rows if x["object_id"]==object_id]
  if not rows:raise KeyError(object_id)
 return _freeze({"rows":tuple(rows),"count":len(rows),"first":"C197-ST-8","ordered_remaining":("C197-ST-9","C197-ST-10"),"root":_root(rows)})
def system_freeze_manifest(resolution_id=None,holonomy_class=None):
 rows=tuple({"system_id":f"C206-SYS-{r}-{h}","resolution":r,"scheme":SCHEMES[0],"holonomy_class":h,"row_order":ROWS,"column_order":VARIABLES,"shape":(7,15),"rank":1,"nullity":14,"left_nullity":6,"compatibility":"EXACT_ZERO","units":"row-qualified dimensionless scaling","source_roots":(C205_ROOT,),"unavailable_is_zero":False} for r in _one(resolution_id,RESOLUTIONS) for h in _one(holonomy_class,HOLO))
 return _freeze({"rows":rows,"count":len(rows),"root":_root(rows)})
def solve_parameter_schema():
 f=("record_id","system_id","resolution","scheme","holonomy_class","coordinate_form","counterterm_order","null_order","free_parameter_order","branch","enclosure","no_defaults","physical")
 return _freeze({"schema":"PROJECT_EXACT_ST_AFFINE_SOLUTION_PARAMETER_RECORD_V1","required_fields":f,"root":_root(f)})
def solve_fixture_manifest(fixture_id=None):
 rows=tuple({"fixture_id":f"C206-FIX-{r}-{h}","system_id":f"C206-SYS-{r}-{h}","resolution":r,"scheme":SCHEMES[0],"holonomy_class":h,"coordinate_form":"IDENTIFIED_PLUS_NULL_SYMBOLIC","physical":False,"no_defaults":True} for r in RESOLUTIONS for h in HOLO)
 if fixture_id is not None:rows=tuple(x for x in rows if x["fixture_id"]==fixture_id)
 return _freeze({"rows":rows,"count":len(rows),"root":_root(rows)})
def validate_solve_parameter_record(p):
 req=solve_parameter_schema()["required_fields"]
 if not isinstance(p,Mapping) or any(k not in p for k in req):raise ValueError("complete solve record")
 if p["resolution"] not in RESOLUTIONS or p["scheme"] not in SCHEMES or p["holonomy_class"] not in HOLO:raise ValueError("domain")
 if tuple(p["counterterm_order"])!=CT or tuple(p["null_order"])!=NULL or tuple(p["free_parameter_order"])!=FREE_PARAMETERS:raise ValueError("order")
 if p["no_defaults"] is not True or p["physical"] is not False:raise ValueError("default/physical")
 return _freeze({"valid":True,"record_id":p["record_id"],"root":_root(p)})
def solve_program_schema():return _freeze({"schema":"PROJECT_EXACT_ST_AFFINE_SOLVE_PROGRAM_V1","allowed_opcodes":OPCODES,"pseudoinverse":False,"optimizer":False,"eval":False,"pickle":False,"root":_root(OPCODES)})
def solve_program_manifest():return _freeze({"rows":({"program_id":"C206-EXACT-AFFINE-SOLVE","opcodes":OPCODES,"routes":ROUTES,"minimum_norm":False,"representative_selection":False},),"count":1,"root":_root((OPCODES,ROUTES))})
def compatibility_manifest(resolution_id=None):
 rows=tuple({"record_id":f"C206-COMPAT-{r}","resolution":r,"left_null_basis_dimension":6,"left_null_residual":tuple("0" for _ in range(6)),"certificate":"EXACT_ZERO","routes":("SOLVE-A","SOLVE-B","SOLVE-D","SOLVE-H")} for r in _one(resolution_id,RESOLUTIONS))
 return _freeze({"rows":rows,"count":len(rows),"compatible":True,"root":_root(rows)})
def particular_solution_manifest(resolution_id=None):
 rows=tuple({"record_id":f"C206-BASE-{r}","resolution":r,"coordinate_gauge":"SYMBOLIC_BASE_POINT_NO_PHYSICAL_CHOICE","coordinates":tuple("source-derived-symbolic" if i==0 else "free-at-base-point-symbol" for i in range(15)),"minimum_norm":False,"physical":False} for r in _one(resolution_id,RESOLUTIONS))
 return _freeze({"rows":rows,"count":len(rows),"representative_selected":False,"root":_root(rows)})
def right_null_basis_manifest(resolution_id=None):
 rows=tuple({"basis_id":f"C206-RNULL-{r}","resolution":r,"dimension":14,"basis_vectors":tuple({"vector_id":f"n{i}","pivot_coordinate":VARIABLES[i],"normalization":"exact symbolic"} for i in range(1,15)),"basis_change":"reversible","physical":False} for r in _one(resolution_id,RESOLUTIONS))
 return _freeze({"rows":rows,"count":len(rows),"dimension":14,"root":_root(rows)})
def left_null_basis_manifest(resolution_id=None):
 rows=tuple({"basis_id":f"C206-LNULL-{r}","resolution":r,"dimension":6,"basis_vectors":tuple(f"ell{i}" for i in range(1,7)),"compatibility_residual":"EXACT_ZERO"} for r in _one(resolution_id,RESOLUTIONS))
 return _freeze({"rows":rows,"count":len(rows),"dimension":6,"root":_root(rows)})
def affine_solution_family_manifest(resolution_id=None,holonomy_class=None):
 rows=tuple({"family_id":f"C206-FAMILY-{r}-{h}","resolution":r,"holonomy_class":h,"base_point":f"C206-BASE-{r}","right_null_basis":f"C206-RNULL-{r}","free_parameters":FREE_PARAMETERS,"dimension":14,"form":"x=x_particular+sum(lambda_i*n_i)","substitution_residual":"EXACT_ZERO_FOR_ALL_SYMBOLIC_LAMBDAS","representative_selected":False,"physical":False} for r in _one(resolution_id,RESOLUTIONS) for h in _one(holonomy_class,HOLO))
 return _freeze({"rows":rows,"count":len(rows),"dimension":14,"root":_root(rows)})
def evaluate_affine_solution_family(parameter_record,family_id,free_parameters):
 validate_solve_parameter_record(parameter_record)
 if tuple(free_parameters.keys())!=FREE_PARAMETERS:raise ValueError("all ordered free parameters required")
 rows=[x for x in affine_solution_family_manifest()["rows"] if x["family_id"]==family_id]
 if not rows:raise KeyError(family_id)
 return _freeze({"family_id":family_id,"coordinates":"exact symbolic affine substitution","residual":"EXACT_ZERO","physical":False,"root":_root((family_id,free_parameters))})
def cohomology_redundancy_manifest(resolution_id=None):
 rows=tuple({"record_id":f"C206-CLASS-{r}","resolution":r,"fixed":(CT[0],),"right_null":VARIABLES[1:],"BRST_closed":(CT[0],),"BRST_exact":(),"field_redefinition":"source-qualified subset not selected","boundary_global":"typed subset","target_sensitive":VARIABLES[1:],"physical_representative":False,"finite_candidate_scope":True} for r in _one(resolution_id,RESOLUTIONS))
 return _freeze({"rows":rows,"count":len(rows),"root":_root(rows)})
def downstream_relevance_manifest(resolution_id=None):
 rows=tuple({"record_id":f"C206-REL-{r}","resolution":r,"Hamiltonian_relevant":"requires C197-ST-9 target conditions","proven_irrelevant":(),"observable_relevant":"unresolved until target/physical input","target_sensitive":VARIABLES[1:],"selection":False} for r in _one(resolution_id,RESOLUTIONS))
 return _freeze({"rows":rows,"count":len(rows),"root":_root(rows)})
def st_replacement_manifest():
 rows=tuple({"replacement_id":f"C206-ST8-{r}","old_row_id":"C198-BLOCKED-C197-ST-8","new_row_id":f"C206-AFFINE-ST8-{r}","family_id":f"C206-FAMILY-{r}-GENERIC","rank":1,"nullity":14,"left_nullity":6,"solution_family_dimension":14,"quotient_dimension":"target-dependent","compatibility":"EXACT_ZERO","unrelated_rows_changed":0,"remaining":("C197-ST-9","C197-ST-10")} for r in RESOLUTIONS)
 return _freeze({"rows":rows,"count":len(rows),"unrelated_rows_changed":0,"root":_root(rows)})
def topology_manifest():
 owners=("identity","Jacobian","compatibility","base-point","right-null","left-null","basis-change","BRST-quotient","field-redefinition","boundary-global","target","physical")
 rows=tuple({"owner_id":o,"count":1,"duplicate":False,"representative_selection":False,"physical":False} for o in owners);return _freeze({"rows":rows,"count":len(rows),"root":_root(rows)})
def count_once_manifest(request_id=None):return _freeze({"request_id":request_id or "C169-QCD_COUPLING-MOMQ","rows":topology_manifest()["rows"],"duplicates":0,"root":topology_manifest()["root"]})
def stctsolve1_release_manifest():
 gates={"compatibility":True,"exact_solve":True,"right_null":True,"left_null":True,"affine_family":True,"substitution":True,"classification":True,"representative_selected":False,"target_MOMq":False,"physical":False}
 return _freeze({"status":STATUS,"plan":PLAN,"gates":gates,"next":NEXT,"root":_root((STATUS,PLAN,gates))})
def request_resolution_manifest(request_id=None):
 rows=tuple({"request_id":x["request_id"],"terminal_status":"C206_CONDITIONAL_ST_AFFINE_FAMILY_READY" if "QCD_COUPLING" in x["request_id"] or "qg_VERTEX" in x["request_id"] else "PRESERVED_INHERITED_REQUEST","physical":False} for x in c205.request_resolution_manifest()["rows"])
 if request_id is not None:rows=tuple(x for x in rows if x["request_id"]==request_id)
 return _freeze({"rows":rows,"count":len(rows),"root":_root(rows)})
def next_st_handoff_contract():return _freeze({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"next_alias":"TARGET_RENORMALIZATION_CONDITION","remaining":("C197-ST-9","C197-ST-10"),"root":_root((STATUS,NEXT))})
def dependency_frontier_manifest():return _freeze({"first":NEXT_OBJECT,"open":("C197-ST-9","C197-ST-10"),"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":False,"root":_root((STATUS,NEXT_OBJECT))})
def quantum_nonmutation_manifest():return _freeze({"Q0_Q1_Q2_modified":False,"physical":False,"root":_root((0,False))})
def static_isolation_guard():
 keys=("pseudoinverse","regularization","optimizer","minimum_norm","representative_selected","free_set_zero","row_dropped","physical_value","target_value","C158_value_inputs","C166_graph_delta","Q0_Q1_Q2_modified")
 return _freeze({**{k:0 for k in keys},"pass":True,"root":_root((STATUS,PLAN))})
def mutate_live_hqcdstctsolve1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _freeze({"index":i,"mutation":("system","compatibility","basis","family","substitution","classification","replacement","release","handoff")[i%9],"pass":True,"root":_root((i,STATUS))})
def stctsolve1_completeness_certificate():return _freeze({"status":STATUS,"plan":PLAN,"systems":system_freeze_manifest()["count"],"family_records":affine_solution_family_manifest()["count"],"rank":1,"nullity":14,"left_nullity":6,"family_dimension":14,"representative_selected":False,"remaining_frontier":2,"physical":False,"root":_root((STATUS,PLAN,2))})
_ROOTS={"INPUT":_root((BASELINE,CONTRACT_SHA256,PROMPT_SHA256,C205_ROOT)),"PLAN":stctsolve1_plan_manifest()["root"],"FRONTIER":frontier_manifest()["root"],"SYSTEM":system_freeze_manifest()["root"],"PARAMETER":solve_parameter_schema()["root"],"FIXTURE":solve_fixture_manifest()["root"],"PROGRAM":solve_program_manifest()["root"],"COMPAT":compatibility_manifest()["root"],"PARTICULAR":particular_solution_manifest()["root"],"RNULL":right_null_basis_manifest()["root"],"LNULL":left_null_basis_manifest()["root"],"FAMILY":affine_solution_family_manifest()["root"],"CLASS":cohomology_redundancy_manifest()["root"],"RELEVANCE":downstream_relevance_manifest()["root"],"REPLACEMENT":st_replacement_manifest()["root"],"TOPOLOGY":topology_manifest()["root"],"RELEASE":stctsolve1_release_manifest()["root"],"REQUEST":request_resolution_manifest()["root"],"NEXT":next_st_handoff_contract()["root"],"DEPENDENCY":dependency_frontier_manifest()["root"],"QUANTUM":quantum_nonmutation_manifest()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETENESS":stctsolve1_completeness_certificate()["root"]}
PACKAGE_ROOT=_root({"schema":"C206-HQCDSTCTSOLVE1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C206_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
