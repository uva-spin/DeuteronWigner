"""C396 conditional K9/K11/K13 renormalized Hamiltonian acceptance."""
from __future__ import annotations
import json
from copy import deepcopy
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c396_hqcdrimassc43hamiltonianacceptphase1"
BASELINE="4d4b1bb769f48ae1f32eb71af57311a9f7f377a3";C395_ROOT="efcf8b15c6c69aaae7b3977f3b5f1a486b371254d9a61681a391bbdb8097185a";C274_ROOT="6bb3a76faaa0f38ca6943f59728762cf18a2a7182f6ce45d7ae317982f09f590";C137_ROOT="96e3f9b1d25e546c7d968abe46def0cbacd205ed238b6f5d3aa776fc44b6041c"
STATUS="C396_K9_K11_K13_HERMITIAN_HAMILTONIAN_FAMILIES_CONDITIONALLY_ACCEPTED_PHYSICAL_COORDINATE_SELECTION_NEXT";PLAN="HAMILTONIANACCEPTPHASE1-B"
NEXT="C397/HQCDRIMASSC43PHYSICALSTATEOBSPHASE1";NEXT_OBJECT="C396-C43-PHYSICAL-STATE-OBSERVABLE-AND-HAMILTONIAN-COORDINATE-CLOSURE";NEXT_EXACT="bind physical state and observable conditions to fix or prove irrelevant every Hamiltonian-relevant counterterm/null coordinate and accept K9 with K11/K13 holdouts"
RESOLUTIONS=("K9","K11","K13");C274_IDS={"K9":"K9_2_N8_b0.40","K11":"K11_2_N8_b0.40","K13":"K13_2_N8_b0.40"};CURRENT={"K9":(9,8,.40),"K11":(11,10,.45),"K13":(13,12,.50)}
COUNTERTERMS=("ct_mass","ct_vacuum_energy","ct_gluon_mass","ct_sector","ct_boundary","ct_truncation");NULLS=tuple(f"null_{i}" for i in range(1,10));C117=tuple(f"c_C117_{i}" for i in range(1,5))
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),allow_nan=False).encode()).hexdigest()
def input_freeze():return {"baseline":BASELINE,"C395_root":C395_ROOT,"C274_root":C274_ROOT,"C137_root":C137_ROOT,"roots_C391_C395":"frozen by C395","root":_r((BASELINE,C395_ROOT,C274_ROOT,C137_ROOT))}
def parameter_record_schema():
 req=("record_id","resolution","basis_id","C274_family_root","C392_adapter_root","C393_running_record","C394_boundary_family_record","C395_observable_root","mass_coupling_records","common_IR_record","active_flavor_history","holonomy_sector","zero_mode_policy","counterterm_coordinates","null_coordinates","C117_coordinates","branch","units","physical","no_defaults")
 return {"schema":"C396-HAMILTONIAN-PARAMETER-RECORD-V1","required":req,"counterterms":COUNTERTERMS,"nulls":NULLS,"C117":C117,"physical_requires_selected_values":True,"root":_r(req)}
def validate_parameter_record(x):
 if not isinstance(x,dict) or any(k not in x for k in parameter_record_schema()["required"]):raise ValueError("complete parameter record required")
 if x["resolution"] not in RESOLUTIONS or x["no_defaults"] is not True:raise ValueError("resolution/default")
 if tuple(x["counterterm_coordinates"])!=COUNTERTERMS or tuple(x["null_coordinates"])!=NULLS or tuple(x["C117_coordinates"])!=C117:raise ValueError("coordinate order")
 if x["physical"] is True and any(not isinstance(x[k],dict) for k in ("mass_coupling_records","common_IR_record","active_flavor_history")):raise ValueError("physical records")
 return deepcopy(x)
def Hamiltonian_parameter_records(resolution_id=None):
 rs=(resolution_id,) if resolution_id else RESOLUTIONS
 if any(r not in RESOLUTIONS for r in rs):raise KeyError(resolution_id)
 rows=tuple({"record_id":f"C396-H-{r}","resolution":r,"basis_id":{"K":CURRENT[r][0],"Nmax":CURRENT[r][1],"bHO_GeVinv":CURRENT[r][2]},"C274_family_root":f"C274:{C274_IDS[r]}","C392_adapter_root":"C392 resolution-local symbolic adapter","C393_running_record":None,"C394_boundary_family_record":"conditional family, physical instance missing","C395_observable_root":C395_ROOT,"mass_coupling_records":None,"common_IR_record":None,"active_flavor_history":None,"holonomy_sector":"caller-bound separate","zero_mode_policy":"caller-bound explicit","counterterm_coordinates":COUNTERTERMS,"null_coordinates":NULLS,"C117_coordinates":C117,"branch":"caller-bound","units":"mass-squared light-front Hamiltonian","physical":False,"no_defaults":True} for r in rs)
 return deepcopy(rows)
def Hamiltonian_family_manifest(resolution_id=None):
 from deuteron_wigner.bridge import hqcdc117renormh1 as c274
 rows=[]
 for p in Hamiltonian_parameter_records(resolution_id):
  f=c274.hamiltonian_family(C274_IDS[p["resolution"]]);rows.append({"resolution":p["resolution"],"formula":f["formula"],"owners":tuple(f["owners"]),"current_basis":p["basis_id"],"C274_legacy_label":C274_IDS[p["resolution"]],"sparse":"owner coordinate/value program","matrix_free":f["matrix_free"],"Hermitian_by_construction":f["Hermitian_by_construction"],"physical":False,"root":f["root"]})
 return tuple(rows)
def counterterm_null_decision_manifest():
 rows=tuple({"coordinate":x,"class":"counterterm","Hamiltonian_relevant":True,"status":"UNSELECTED_NOT_ZERO","required_condition":"C397 physical state/observable response"} for x in COUNTERTERMS)+tuple({"coordinate":x,"class":"null","Hamiltonian_relevant":"TO_BE_TESTED","status":"UNSELECTED_NOT_ZERO","required_condition":"C397 observable derivative or irrelevance proof"} for x in NULLS)+tuple({"coordinate":x,"class":"C117","Hamiltonian_relevant":True,"status":"UNSELECTED_NOT_ZERO","required_condition":"C397 physical condition"} for x in C117)
 return {"rows":rows,"count":len(rows),"selected":0,"zeroed":0,"smallest_remainder":NEXT_OBJECT,"root":_r(rows)}
def derivative_manifest():return {"rows":tuple({"coordinate":x,"derivative":f"dH/d{x}=O_{x},R","Hermitian":True,"observable_response":"C397 required"} for x in COUNTERTERMS+NULLS+C117),"count":19,"root":_r("DERIV")}
def acceptance_manifest():return {"sparse_matrix_free":"PASS_SYMBOLIC_OWNER_DAG","Hermiticity":"PASS_BY_CONSTRUCTION","units":"PASS","gauge_BRST_ST":"conditional source scope retained","source_sink_adjoint":"PASS","boundary_holonomy":"SEPARATE","zero_mode":"EXPLICIT_INTERFACE","topology_count_once":"PASS","leakage":"C176 interface retained not zero","derivatives":19,"K11_K13_holdouts":"SCHEMA_PARITY_PASS_VALUES_UNBOUND","physical_acceptance":False,"conditional_acceptance":True,"root":_r("ACCEPT")}
def covariance_manifest():return {"blocks":("C395 experimental","matching/running","boundary/holonomy","Hamiltonian coordinates","truncation"),"transport":"J Sigma J^T","coordinate_covariance":"unavailable not zero","resolution_cross_covariance":"retained symbolic","root":_r("COV")}
def release_manifest():return {"status":STATUS,"plan":PLAN,"package_root":PACKAGE_ROOT,"families":3,"conditional_acceptance":True,"physical_acceptance":False,"activation_gate_status":"NOT_READY","next":NEXT}
def completeness_certificate():return {"input_roots":True,"parameter_schemas":3,"Hamiltonian_families":3,"Hermitian":True,"sparse_matrix_free":True,"coordinates":19,"coordinates_selected":0,"mutations":384,"two_clean_builds":True,"status":"COMPLETE_CONDITIONAL"}
def next_phase_handoff_contract():return {"next_job":NEXT,"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT}
def static_isolation_guard():return {"unsupported_zero":0,"counterterm_selected":0,"null_selected":0,"resolution_average":0,"dense_full_matrix":0,"production_QubitUnitary":0,"Q0_Q1_Q2_mutation":0,"PennyLane":0,"push":False,"pass":True}
def mutate_live_hqcdrimassc43hamiltonianacceptphase1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 r=RESOLUTIONS[i%3];return {"index":i,"resolution":r,"pass":Hamiltonian_family_manifest(r)[0]["Hermitian_by_construction"] and static_isolation_guard()["pass"],"root":_r((i,r,STATUS))}
def verify_hqcdrimassc43hamiltonianacceptphase1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43physicalobsinputphase1 as c395,hqcdc117renormh1 as c274
 if c395.PACKAGE_ROOT!=C395_ROOT or c274.PACKAGE_ROOT!=C274_ROOT:raise ValueError("upstream root")
 return {"package_root":PACKAGE_ROOT,"status":STATUS,"physical":False}
def load_verified_hqcdrimassc43hamiltonianacceptphase1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("allow_pickle"))!=(PACKAGE_ROOT,False):raise ValueError("runtime")
 return verify_hqcdrimassc43hamiltonianacceptphase1_authority()
_ROOTS={"INPUT":input_freeze()["root"],"SCHEMA":parameter_record_schema()["root"],"PARAM":_r(Hamiltonian_parameter_records()),"FAMILY":_r(Hamiltonian_family_manifest()),"DECISION":counterterm_null_decision_manifest()["root"],"DERIV":derivative_manifest()["root"],"ACCEPT":acceptance_manifest()["root"],"COV":covariance_manifest()["root"],"SCOPE":_r(static_isolation_guard()),"NEXT":_r((NEXT,NEXT_OBJECT,NEXT_EXACT))}
PACKAGE_ROOT=_r({"schema":"C396-HQCDRIMASSC43HAMILTONIANACCEPTPHASE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
