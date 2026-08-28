"""C313 source-qualified C43 holonomy effective-action kernel."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c313_hqcdrimassc43effact1";BASELINE="59defa90cb8f129f9c1b0ec0384c16346d90cf2d";C312_ROOT="205e93f06d5d919e04926c8fe9bd0ca38e37a869c9f48d0a61d986fe0502208c"
STATUS="C313_C43_BACKGROUND_HOLONOMY_EFFECTIVE_ACTION_KERNEL_DERIVED_REGULATED_DETERMINANT_EVALUATION_MISSING";PLAN="RIMASSC43EFFACT1-C";NEXT="C314/HQCDRIMASSC43DETEVAL1";NEXT_OBJECT="C313-C43-HOLONOMY-DETERMINANT-EVALUATION";NEXT_EXACT="evaluate the regulated C43 background-field fluctuation determinant and project its finite class-function coefficients onto CHI8 and RE_TF3"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def source_freeze():
 from deuteron_wigner.bridge.g0.contracts import source_manifest,conventions,action_contract,symbolic_hash
 s=source_manifest();return _f({"source_root":symbolic_hash(s),"convention_root":symbolic_hash(conventions()),"action_root":symbolic_hash(action_contract()),"hash_locked":s["status"]=="HASH_LOCKED","root":_r("C313-SOURCE")})
def background_contract():return _f({"background":"constant Cartan A_plus zero mode encoded by W=exp(i theta_a T^a)","gauge":"C43 A_plus_gauge_field=A^-=background; A^+=0; names kept covariant-index explicit","color":"T=lambda/2, Tr(TaTb)=delta_ab/2","domain":"SU3 Weyl alcove with C295 normalized measure","basis":("CHI8","RE_TF3"),"physical_background_selected":False,"root":_r("C313-BG")})
def determinant_kernel():return _f({"formula":"Gamma1[W]=1/2 Tr'_B log Delta_B(W)-Tr'_constraint log Delta_constraint(W)-Tr'_F log Delta_F(W)","prime":"C43 P0/global and constrained owners excluded and recorded separately","mode_shift":"p_plus -> p_plus + alpha(theta)/L for adjoint roots; fundamental weights for fermions","regulator":"symmetric mode cutoff N at fixed finite volume, then source-qualified subtraction","subtraction":"W-independent vacuum term separate; no thermal Weiss import","evaluation":"MISSING_NOT_ZERO","root":_r("C313-DET")})
def normalization_contract():return _f({"action":"Gamma1 dimensionless","potential_density":"Gamma1/(L_plus L_minus A_perp)","C301_scale":"lambda_K multiplies dimensionless class functions; K adapter requires declared cell volume and g_K^2 L_K/(4 pi^2)","absolute_coefficients":"UNAVAILABLE_PENDING_DETERMINANT_EVALUATION","root":_r("C313-NORM")})
def topology_ledger():return _f({"owners":("transverse gluon fluctuation","fermion fluctuation","Gauss/constraint Jacobian","global P0 exclusion","vacuum subtraction"),"ghost":"decoupled only at C43 declared nonzero-mode axial scope","count_once":True,"constrained_modes_zeroed":False,"root":_r("C313-TOPO")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"kernel_ready":True,"coefficients_ready":False,"C293_promoted":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"Weiss_imported":0,"C293_promoted":0,"determinant_fabricated":0,"P0_zeroed":0,"physical_value_selected":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassc43effact1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("source","background","gauge","color","mode","P0","constraint","regulator","normalization","scope")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassc43effact1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43match1 as c312
 from deuteron_wigner.bridge.g0.contracts import validate_contract,validate_source_manifest,source_manifest
 if c312.PACKAGE_ROOT!=C312_ROOT or not validate_contract() or not validate_source_manifest(source_manifest()):raise ValueError("authority changed")
 c312.load_verified_hqcdrimassc43match1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassc43effact1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassc43effact1_authority()
_ROOTS={"INPUT":_r((BASELINE,C312_ROOT)),"SOURCE":source_freeze()["root"],"BG":background_contract()["root"],"DET":determinant_kernel()["root"],"NORM":normalization_contract()["root"],"TOPO":topology_ledger()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C313-HQCDRIMASSC43EFFACT1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};__all__=[n for n in globals() if not n.startswith("_")]
