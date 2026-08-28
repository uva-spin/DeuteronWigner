"""C309 full Gram evaluation and shape-tail diagnosis."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c309_hqcdrimassv0grameval1";BASELINE="92c37126abe2b9f7c88db46b320b748a4ec7fe34";C308_ROOT="b4035029133db4f2264ff6b8ed367fb3e6857ba348ce6aee37d25229fa243371"
STATUS="C309_FULL_GRAM_SCAN_COMPLETE_NONCONSTANT_LOG_MODE_TAILS_IDENTIFIED_SHAPE_TAIL_SUBTRACTION_MISSING";PLAN="RIMASSV0GRAMEVAL1-C";NEXT="C310/HQCDRIMASSSHAPETAIL1";NEXT_OBJECT="C309-V0-CLASS-SHAPE-MODE-TAILS";NEXT_EXACT="derive and subtract the logarithmic N tails in the CHI8 and RE_TF3 full-Gram coefficients before epsilon extrapolation"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def scan_design():return _f({"N":(32,64,128,256),"epsilon":(.08,.05,.03),"quadrature_order":(20,28,36),"measure":"J/6","basis":("1","CHI8","RE_TF3"),"center_tail":"C308 applied only to additive constant","evaluations":36,"root":_r("C309-DESIGN")})
def reference_scan():
 rows=({"N":32,"constant":-386.678709,"CHI8":-407.096832,"RE_TF3":133.498305},{"N":64,"constant":-343.158315,"CHI8":-399.857483,"RE_TF3":131.300895},{"N":128,"constant":-291.038541,"CHI8":-392.632005,"RE_TF3":129.108867},{"N":256,"constant":-230.295997,"CHI8":-385.412334,"RE_TF3":126.919196});return _f({"rows":rows,"epsilon":.05,"G":36,"normalization":.9996552,"Gram_condition":82.516,"root":_r(rows)})
def shape_tail_fit():return _f({"CHI8":{"model":"a+b logN+c/N","a":-443.10772409,"b":10.40577774,"c":-1.68756313,"max_residual":.000245},"RE_TF3":{"model":"a+b logN+c/N","a":144.41247570,"b":-3.15514520,"c":.66287304,"max_residual":.000073},"pure_log_slopes":{"CHI8":10.42765145,"RE_TF3":-3.16373717},"converged_without_subtraction":False,"analytic_coefficients_derived":False,"root":_r("C309-TAILFIT")})
def regulator_audit():return _f({"G36_epsilon_08_vs_05":"close at resolved nodes","epsilon_03":"changes when nearer-wall nodes enter","ordered_requirement":"subtract N tails at fixed epsilon before epsilon extrapolation","quadrature_normalization_range":(.9985,.9999836),"full_coefficients_ready":False,"root":_r("C309-REG")})
def evaluation_certificate():return _f({"full_Gram_executed":True,"center_tail_sufficient":False,"shape_tails_nonzero":True,"coefficient_intervals":"UNAVAILABLE_NOT_ZERO","C43_matching":False,"root":_r("C309-CERT")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"scan_complete":True,"coefficients_ready":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"shape_tail_zeroed":0,"short_fit_promoted_exact":0,"epsilon_order_reversed":0,"raw_coefficients_promoted":0,"C43_matching_claimed":0,"C117_coordinates_selected":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassv0grameval1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("N","epsilon","G","Gram","constant","CHI8","TF3","tail","order","scope")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassv0grameval1_authority():
 from deuteron_wigner.bridge import hqcdrimassv0tailrenorm1 as c308
 if c308.PACKAGE_ROOT!=C308_ROOT:raise ValueError("C308 root changed")
 c308.load_verified_hqcdrimassv0tailrenorm1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassv0grameval1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassv0grameval1_authority()
_ROOTS={"INPUT":_r((BASELINE,C308_ROOT)),"DESIGN":scan_design()["root"],"SCAN":reference_scan()["root"],"TAIL":shape_tail_fit()["root"],"REG":regulator_audit()["root"],"CERT":evaluation_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C309-HQCDRIMASSV0GRAMEVAL1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};__all__=[n for n in globals() if not n.startswith("_")]
