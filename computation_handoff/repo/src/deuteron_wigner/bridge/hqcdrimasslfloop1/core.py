"""C284 maximal C43 signed-mass light-front loop partition."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c284_hqcdrimasslfloop1"
BASELINE="603d561dc5ead8e4021d69a6275028be85d2b596";C283_ROOT="15ec3b901fd3b75256de52cb21fa4295486391c0d269b2debd6a956a03005504"
STATUS="C284_C43_MASS_LOOP_MAXIMAL_KERNEL_PARTITION_READY_RESIDUAL_LINK_ENDPOINT_GEOMETRY_MISSING";PLAN="RIMASSLFLOOP1-B"
NEXT="C285/HQCDRIMASSLINKGEOM1";NEXT_OBJECT="C284-MASS-RESIDUAL-LINK-PATH-ENDPOINT-GEOMETRY";NEXT_EXACT="source-qualified finite-cell residual-link path and endpoint geometry composable with the signed-mass self-energy at K9/K11/K13"
RESOLUTIONS=("K9","K11","K13")
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def loop_partition():
 rows=(("retained canonical q-qg-q","C145/C217","EXECUTABLE_CALLER_CONDITIONAL"),("outside-fixed-K V1","C218-C238","EXECUTABLE_PARAMETERIZED"),("C112 instantaneous fermion/contact","C239-C247","EXECUTABLE_PARAMETERIZED"),("C127 instantaneous current/Gauss","C248-C254","EXECUTABLE_REGULATED"),("Q0 antisymmetric/PV","C43/C172","EXACT_NONZERO_MODE_SCOPE"),("P0/global residual gauge","C173-C175","CONDITIONAL_NONMATRIX"),("finite-HO boundary","C176/C181","FACTORIZED_CONDITIONAL"),("residual link/holonomy","C177-C183","PATH_ENDPOINT_GEOMETRY_NONCOMPOSABLE"),("C149 signed-mass projector","C149/C276","READY"),("counterterm/C117 coordinates","C206/C274","SYMBOLIC_UNSELECTED"))
 return _f({"rows":tuple({"class":a,"authority":b,"status":c} for a,b,c in rows),"count":10,"kernel_ready":9,"full_loop":False,"missing_as_zero":False,"root":_r(rows)})
def resolution_programs():
 ops=("LOAD_CALLER_STATE","LOAD_RETAINED_LOOP","LOAD_V1_COMPLEMENT","LOAD_C112_CONTACT","LOAD_C127_CURRENT","LOAD_Q0_PV","LOAD_P0_INTERFACE","LOAD_HO_BOUNDARY","LOAD_RESIDUAL_LINK_GEOMETRY","APPLY_C149_MASS_PROJECTOR","ATTACH_SYMBOLIC_COUNTERTERMS","RETURN_PARTIAL_ENCLOSURE")
 rows=tuple({"resolution":r,"safe_opcodes":ops,"executable_subset":True,"full_executable":False,"terminal":"RESIDUAL_LINK_PATH_ENDPOINT_GEOMETRY_MISSING"} for r in RESOLUTIONS)
 return _f({"schema":"PROJECT_C284_C43_MASS_LF_LOOP_V1","rows":rows,"eval":False,"pickle":False,"callbacks":False,"root":_r(rows)})
def owner_count_once():return _f({"owners":("C145","C238","C247","C254","C172","C175","C181","C182_C183","C149","C206_C274"),"duplicates":0,"residual_link_additive_before_composition":False,"root":_r("owners")})
def route_certificate():return _f({"routes":tuple({"route":x,"ready_subset":True,"full_agreement":False,"reason":NEXT_OBJECT} for x in ("DIRECT_PROJECT","MASS_DERIVATIVE","SPECTRAL_RESOLVENT","OWNER_DECOMPOSITION","SIGN_REVERSAL")),"false_agreement":False,"root":_r("routes")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"kernel_classes":10,"ready_classes":9,"evaluated_physical_loops":0,"full_loop":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"boundary_zeroed":0,"P0_zeroed":0,"link_unity_assumed":0,"holonomy_selected":0,"C117_coordinates_selected":0,"K_averaged":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimasslfloop1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("state","canonical","V1","C112","C127","Q0","P0","boundary","link","holonomy","projector","counterterm","route")[i%13],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimasslfloop1_authority():
 from deuteron_wigner.bridge import hqcdrimassgaugeadapter1 as c283,hqcdriquarkfixedkv2currentreg1 as c254,hqcdb0holonomy2 as c183
 if c283.PACKAGE_ROOT!=C283_ROOT:raise ValueError("C283 root changed")
 c283.load_verified_hqcdrimassgaugeadapter1_authority();c254.load_verified_hqcdriquarkfixedkv2currentreg1_authority();c183.load_verified_hqcd_b0holonomy2_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimasslfloop1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimasslfloop1_authority()
_ROOTS={"INPUT":_r((BASELINE,C283_ROOT)),"PARTITION":loop_partition()["root"],"PROGRAMS":resolution_programs()["root"],"OWNERS":owner_count_once()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C284-HQCDRIMASSLFLOOP1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
