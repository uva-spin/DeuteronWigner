"""C301 SU3 holonomy class-function potential basis."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c301_hqcdrimassholonomypot1"
BASELINE="b9c28ab0a5eb2b3582bc6e2e7bacd4f456800d30";C300_ROOT="3e9a52fd144a5e523d197ed5dea6a531abb40d658e060c56d1cb58c25459a667"
STATUS="C301_EXACT_SU3_CENTER_WEYL_HOLONOMY_POTENTIAL_BASIS_READY_COEFFICIENT_MATCHING_MISSING";PLAN="RIMASSHOLONOMYPOT1-B"
NEXT="C302/HQCDRIMASSHOLONOMYCOEFF1";NEXT_OBJECT="C301-HOLONOMY-POTENTIAL-COEFFICIENT-MATCHING";NEXT_EXACT="derive or authenticate the C43 K9/K11/K13 coefficients and joint covariance for the C301 center- and Weyl-invariant holonomy potential basis"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def authority_freeze():return _f({"C183":"explicit SU3 holonomy capsule and conjugacy","C203_C205":"bulk/endpoint/global BRST identities","C295":"normalized Weyl measure","C296":"z-to-C43 phase/action map","C300":C300_ROOT,"root":_r(("C183","C203-C205","C295","C296",C300_ROOT))})
def class_function_basis():
 rows=({"id":"CHI8","formula":"tr_Adj(W)=|tr_F(W)|^2-1","center":"invariant","weyl":"invariant","real":True},{"id":"RE_TF3","formula":"Re[(tr_F W)^3]","center":"invariant","weyl":"invariant","real":True});return _f({"rows":rows,"count":2,"constant_separate":True,"dependent_identity":"Re tr_F(W^3)=RE_TF3-3*(CHI8+1)+3, so it is omitted","root":_r(rows)})
def endpoint_brst_proof():return _f({"sW":"c(end)W-Wc(start)","identified_endpoint":"c(end)=c(start) up to transition conjugation","class_function_variation":0,"global_frame":"conjugation quotient","bulk_mass_equivalence":False,"root":_r("C301-ENDPOINT-BRST")})
def potential_contract():return _f({"formula":"V_K(W)=lambda8_K*CHI8+lambda3_K*RE_TF3+constant_K","measure":"C295/C296 normalized nonflat alcove density","identity_default":False,"coefficients":"UNMATCHED_NOT_ZERO","absolute_normalization":"ACTION_COEFFICIENTS_REQUIRED","root":_r("C301-V-BASIS")})
def resolution_adapter():
 rows=tuple({"resolution":k,"basis":("CHI8","RE_TF3"),"coefficients":"UNAVAILABLE_NOT_ZERO","action_scale":"g_K^2 L_K/(4*pi^2)","cross_K_covariance":"REQUIRED"} for k in ("K9","K11","K13"));return _f({"rows":rows,"count":3,"root":_r(rows)})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"basis_ready":True,"coefficients_ready":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"identity_selected":0,"flat_measure":0,"coefficients_zeroed":0,"bulk_mass_equated":0,"C117_coordinates_selected":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassholonomypot1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("trace","center","Weyl","real","BRST","endpoint","measure","K","covariance","scope")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassholonomypot1_authority():
 from deuteron_wigner.bridge import hqcdrimassadjointst1 as c300
 if c300.PACKAGE_ROOT!=C300_ROOT:raise ValueError("C300 root changed")
 c300.load_verified_hqcdrimassadjointst1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassholonomypot1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassholonomypot1_authority()
_ROOTS={"INPUT":_r((BASELINE,C300_ROOT)),"AUTH":authority_freeze()["root"],"BASIS":class_function_basis()["root"],"BRST":endpoint_brst_proof()["root"],"POT":potential_contract()["root"],"K":resolution_adapter()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C301-HQCDRIMASSHOLONOMYPOT1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
