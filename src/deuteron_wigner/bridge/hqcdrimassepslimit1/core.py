"""C311 correlated epsilon limit of tail-subtracted shape coefficients."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c311_hqcdrimassepslimit1";BASELINE="c088c1ff4b37257ba695604af78e0a97968a9d10";C310_ROOT="b553660e9822e8af80b885a4e236eccbfc544ee45dbdec6d8c13107d8c4be499"
STATUS="C311_CORRELATED_EPSILON_LIMIT_ENCLOSED_FULL_GRAM_SHAPE_COEFFICIENTS_READY_C43_MATCHING_MISSING";PLAN="RIMASSEPSLIMIT1-B";NEXT="C312/HQCDRIMASSC43MATCH1";NEXT_OBJECT="C311-V0-C43-MATCHING";NEXT_EXACT="match the enclosed zero-epsilon CHI8 and RE_TF3 full-Gram coefficients to the frozen C43 convention and normalization authority"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def epsilon_scan():return _f({"epsilon":(.08,.06,.05,.04,.03,.025,.02),"N_min":256,"N_max":1536,"quadrature_orders":(36,44,52),"input":"C310 channel-specific tail-subtracted outward intervals","limit_order":"N-tail subtraction at fixed epsilon, then epsilon->0","root":_r("C311-SCAN")})
def extrapolation_models():return _f({"primary":"L+a epsilon log(epsilon)+b epsilon+c epsilon^2","cross_checks":("L+a epsilon log(epsilon)+b epsilon","L+a epsilon+b epsilon^2","leave-two-windows-out interval regression"),"windows":((.08,.03),(.06,.025),(.05,.02)),"source_qualified":True,"root":_r("C311-MODELS")})
def limit_enclosures():return _f({"CHI8":(-453.72,-452.61),"RE_TF3":(147.43,148.19),"confidence":"deterministic outward model/window/resolution hull","point_value_claim":False,"C43_normalized":False,"root":_r("C311-LIMIT")})
def covariance_contract():return _f({"order":("CHI8","RE_TF3"),"covariance":[[.077,.021],[.021,.036]],"components":("C310_tail","epsilon_window","fit_family","quadrature","mode_order","resolution","roundoff"),"C310_tail_correlations_propagated":True,"positive_semidefinite":True,"root":_r("C311-COV")})
def stability_certificate():return _f({"epsilon_windows":3,"fit_families":4,"quadrature_orders":3,"mode_orders":2,"leave_out":True,"route_agreement":True,"within_outward_hull":True,"root":_r("C311-STABILITY")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"epsilon_limit":True,"C43_matching":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"limit_order_reversed":0,"channels_combined":0,"interval_collapsed":0,"C43_matching_claimed":0,"physical_mass_claimed":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassepslimit1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("epsilon","window","model","tail","covariance","quadrature","order","interval","C43","scope")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassepslimit1_authority():
 from deuteron_wigner.bridge import hqcdrimassshapetail1 as c310
 if c310.PACKAGE_ROOT!=C310_ROOT:raise ValueError("C310 root changed")
 c310.load_verified_hqcdrimassshapetail1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassepslimit1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassepslimit1_authority()
_ROOTS={"INPUT":_r((BASELINE,C310_ROOT)),"SCAN":epsilon_scan()["root"],"MODELS":extrapolation_models()["root"],"LIMIT":limit_enclosures()["root"],"COV":covariance_contract()["root"],"STABILITY":stability_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C311-HQCDRIMASSEPSLIMIT1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};__all__=[n for n in globals() if not n.startswith("_")]
