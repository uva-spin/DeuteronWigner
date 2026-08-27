"""C286 conditional project-path selection map for the C43 mass loop."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c286_hqcdrimasspathselect1"
BASELINE="bbac87363a32d12436456b55630c69f0ff17a2e4";C285_ROOT="43ed36b295be408e42a8c518e73b37fdf8a087876ff0a798fe56c07d484b4639";C179_ROOT="7cc1089eb36fffac5240666b7e6b03bf5bf3feca6a422c6644689f218fa836d2"
STATUS="C286_PROJECT_AFFINE_PATH_AND_CONDITIONAL_PROCESS_MAP_READY_PHYSICAL_PROCESS_HOLONOMY_CAPSULE_MISSING";PLAN="RIMASSPATHSELECT1-B"
NEXT="C287/HQCDRIMASSPROCESS1";NEXT_OBJECT="C286-MASS-PHYSICAL-PROCESS-HOLONOMY-CAPSULE";NEXT_EXACT="authenticated signed-mass self-energy process classification selecting DIS-future or DY-past cut side and a physical SU(3) holonomy sector at K9/K11/K13"
RESOLUTIONS=("K9","K11","K13");REPRESENTATIVE="PROJECT_FINITE_HO_AFFINE_TRANSVERSE_CONNECTOR_V1"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def project_path_selection():
 row={"representative":REPRESENTATIVE,"candidate":"DIRECT_AFFINE_CONNECTOR","authority":"C179 project representative","path_shape_selected":True,"unique_continuum_path_claim":False,"degree_two_scheme_dependence":"NONZERO_RETAINED","alternatives_summed":False}
 return _f({**row,"root":_r(row)})
def conditional_process_map():
 rows=tuple({"resolution":k,"branches":({"process":"DIS_FUTURE","cut_side":"C178_CUT_SIDE_PLUS","orientation":"SOURCE_TO_SINK_FUTURE"},{"process":"DY_PAST","cut_side":"C178_CUT_SIDE_MINUS","orientation":"SOURCE_TO_SINK_PAST"}),"endpoint_pair":"C179 symbolic process endpoint pair","transition":"C178_TRANSITION_C0_NONTRIVIAL_INTERFACE","holonomy":"CALLER_PHYSICAL_CAPSULE_REQUIRED"} for k in RESOLUTIONS)
 return _f({"rows":rows,"conditional_executable":True,"physical_branch_selected":False,"branches_merged":False,"root":_r(rows)})
def selection_gate():return _f({"path_shape":True,"cut_chart":True,"symbolic_endpoints":True,"representation":True,"ordered_transport":True,"process":False,"physical_holonomy":False,"identity_fixture_allowed":False,"full_composition":False,"root":_r((STATUS,PLAN))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"path_representative":REPRESENTATIVE,"conditional_branches":2,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"future_selected":0,"past_selected":0,"identity_fixture_promoted":0,"holonomy_selected":0,"link_unity_assumed":0,"endpoint_equated":0,"C117_coordinates_selected":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimasspathselect1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("representative","branch","cut","endpoint","orientation","representation","transition","holonomy","resolution","composition")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimasspathselect1_authority():
 from deuteron_wigner.bridge import hqcdrimasslinkgeom1 as c285,hqcdb0reslinkpath1 as c179
 if c285.PACKAGE_ROOT!=C285_ROOT or c179.PACKAGE_ROOT!=C179_ROOT or c179.PROJECT_REPRESENTATIVE!=REPRESENTATIVE:raise ValueError("upstream root or representative changed")
 c285.load_verified_hqcdrimasslinkgeom1_authority();c179.load_verified_hqcd_b0reslinkpath1_authority()
 return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimasspathselect1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimasspathselect1_authority()
_ROOTS={"INPUT":_r((BASELINE,C285_ROOT,C179_ROOT)),"PATH":project_path_selection()["root"],"MAP":conditional_process_map()["root"],"GATE":selection_gate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C286-HQCDRIMASSPATHSELECT1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
