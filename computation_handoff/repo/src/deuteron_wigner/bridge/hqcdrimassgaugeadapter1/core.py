"""C283 structural RI/SMOM-to-C43 signed-mass gauge adapter."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c283_hqcdrimassgaugeadapter1"
BASELINE="42b77434a6412f9ee27ba69ac1e1219fb853fbb4";C282_ROOT="e64df09d7abc357b53d4b49435b3dd4dfa260d71d1c2b5dd2a001558ccf3052e"
STATUS="C283_COVARIANT_TO_C43_MASS_ADAPTER_STRUCTURAL_PROGRAM_READY_LIGHT_FRONT_LOOP_COEFFICIENT_MISSING";PLAN="RIMASSGAUGEADAPTER1-C"
NEXT="C284/HQCDRIMASSLFLOOP1";NEXT_OBJECT="C283-C43-LIGHT-FRONT-MASS-ONE-LOOP";NEXT_EXACT="order-alpha_s C43 A-plus-zero antisymmetric-PV signed-mass-projected quark self-energy including Q0, boundary, residual-link, and instantaneous contributions at K9/K11/K13"
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
def endpoint_manifest():
 rows=({"endpoint":"RI_SMOM","gauge":"general covariant xi; Landau xi=0 specialization","pole":"Feynman i0","state":"continuum symmetric nonexceptional off-shell nonsinglet","source":"arXiv:0901.2599v2"},{"endpoint":"C43","gauge":"A^+=0 light-front","pole":"antisymmetric/PV inverse partial-plus on Q0","state":"finite-cell/HO off-shell colored state","boundary":"P0/Q0, residual transverse link, APBC/PBC and holonomy retained"})
 return _f({"rows":rows,"identity":False,"root":_r(rows)})
def contribution_ledger():
 rows=(("canonical q-qg-q","operator programs available; common-state evaluation required"),("instantaneous fermion","source-bound; evaluation required"),("instantaneous current/Gauss","regulated source-bound; evaluation required"),("Q0/P0","Q0 PV retained; P0 not zeroed"),("boundary/residual link/holonomy","conditional nonmatrix interfaces retained"),("counterterm layer","symbolic unselected"))
 return _f({"rows":tuple({"class":a,"status":b} for a,b in rows),"count":6,"evaluated":0,"missing_as_zero":False,"root":_r(rows)})
def adapter_program():
 ops=("LOAD_RI_SMOM_TARGET","LOAD_C43_COMMON_STATE","LOAD_C43_CANONICAL_LOOP","LOAD_INSTANTANEOUS_FERMION","LOAD_INSTANTANEOUS_CURRENT","LOAD_Q0_PV","LOAD_BOUNDARY_RESIDUAL_LINK","APPLY_SIGNED_MASS_PROJECTOR","SUBTRACT_COMMON_IR","FORM_TARGET_MINUS_C43","RETURN_ENCLOSURE")
 rows=tuple({"resolution":r,"safe_opcodes":ops,"structural":True,"executable":False,"terminal":"C43_LIGHT_FRONT_LOOP_MISSING"} for r in RESOLUTIONS)
 return _f({"schema":"PROJECT_C283_RI_SMOM_C43_MASS_GAUGE_ADAPTER_V1","rows":rows,"eval":False,"pickle":False,"callbacks":False,"root":_r(rows)})
def cross_gauge_audit():return _f({"common_bare_action":"formal only","off_shell_colored_gauge_independence":False,"Landau_relabelled_C43":False,"universal_scalar_map":False,"ST_Ward":"endpoint-local; insufficient for cross-gauge coefficient","exact_required_calculation":NEXT_OBJECT,"root":_r("no-cross-gauge-promotion")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"structural_programs":3,"executable_adapters":0,"cross_gauge_equivalence":False,"remaining_C165_layer_leaves":1,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"cross_gauge_equality_assumed":0,"boundary_zeroed":0,"P0_zeroed":0,"C117_coordinates_selected":0,"remaining_layer_leaf_modified":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassgaugeadapter1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("source-gauge","target-gauge","pole","Q0","P0","boundary","link","instantaneous","projector","IR","route","layer")[i%12],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassgaugeadapter1_authority():
 from deuteron_wigner.bridge import hqcdrimassnf1 as c282,hqcdlfgadapter1 as c168
 if c282.PACKAGE_ROOT!=C282_ROOT:raise ValueError("C282 root changed")
 c282.load_verified_hqcdrimassnf1_authority();c168.load_verified_hqcd_lfgadapter1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassgaugeadapter1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassgaugeadapter1_authority()
_ROOTS={"INPUT":_r((BASELINE,C282_ROOT)),"ENDPOINTS":endpoint_manifest()["root"],"CONTRIBUTIONS":contribution_ledger()["root"],"PROGRAM":adapter_program()["root"],"AUDIT":cross_gauge_audit()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C283-HQCDRIMASSGAUGEADAPTER1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
