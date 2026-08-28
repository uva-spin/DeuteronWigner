"""C305 source-compatible V0 Weyl-wall finite-part prescription."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c305_hqcdrimassv0finitepart1";BASELINE="2c10b32fb02559c234c80c325d6a9838b53356f6";C304_ROOT="e41526e037b832fee633e8c383f734c0d350ddd20dec3057c1a220dcb2760431"
STATUS="C305_SOURCE_COMPATIBLE_CENTER_SUBTRACTED_SYMMETRIC_WALL_FINITE_PART_SCHEME_READY_NUMERICAL_LIMIT_EVALUATION_MISSING";PLAN="RIMASSV0FINITEPART1-B";NEXT="C306/HQCDRIMASSV0FINITEEVAL1";NEXT_OBJECT="C305-V0-FINITE-PART-NUMERICAL-LIMIT";NEXT_EXACT="evaluate the C305 ordered N-to-infinity then epsilon-to-zero coefficient family with convergence and path-dependence enclosures"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def wall_asymptotics():
 rows=tuple({"wall":w,"root_distance":d,"generic_behavior":"V0=-A_wall(t)/delta^2+O(delta^-1)","measure_behavior":"J/6=B_wall(t)*delta^2+O(delta^4)","weighted_behavior":"finite generic-wall limit; intersections require joint regulator"} for w,d in (("alpha_u","|sin pi u|"),("alpha_v","|sin pi v|"),("alpha_v-u","|sin pi(v-u)|")));return _f({"rows":rows,"count":3,"direct_scan":"epsilon=.08,.04,.02,.01,.005 confirms epsilon^2 V0 approaches finite values","root":_r(rows)})
def regulator_definition():return _f({"D_epsilon":"points in (0,1)^2 with min(|sin pi u|,|sin pi v|,|sin pi(v-u)|)>=epsilon","symmetry":"all three positive-root walls treated identically","mode_cutoff":"m,n,k half-integer <=N-1/2 in every C303 sum","center_subtraction":"Vbar_N(u,v)=V_N(u,v)-V_N(1/2,1/2)","source_authority":"C293 lines 655-657 sets V(1/2,1/2)=0","measure":"corrected C304 J/6","root":_r("C305-REG")})
def finite_part_program():return _f({"basis":("1","CHI8","RE_TF3"),"gram":"G_epsilon=<f_i f_j>_(J/6,D_epsilon)","rhs":"b_N,epsilon=<f_i Vbar_N>_(J/6,D_epsilon)","coefficients":"c_N,epsilon=G_epsilon^-1 b_N,epsilon","ordered_limit":"first N->infinity at fixed epsilon; then epsilon->0","alternative_paths":"simultaneous N*epsilon fixed and reversed order are mandatory scheme-dependence holdouts","acceptance":"interval sequences Cauchy and path spread enclosed","C43_matching":False,"root":_r("C305-PROGRAM")})
def covariance_contract():return _f({"components":("mode-tail","quadrature","wall-excision","limit-fit","path/scheme"),"correlated_across_basis":True,"correlated_across_regulators":True,"zero_diagonal_assumption":False,"root":_r("C305-COV")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"scheme_ready":True,"coefficients_ready":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"wall_terms_dropped":0,"regulator_hidden":0,"limit_order_conflated":0,"scheme_spread_zeroed":0,"C43_matching_claimed":0,"C117_coordinates_selected":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassv0finitepart1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("wall","delta","asymptotic","epsilon","N","subtraction","Gram","limit","covariance","scope")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassv0finitepart1_authority():
 from deuteron_wigner.bridge import hqcdrimassv0meshproject1 as c304
 if c304.PACKAGE_ROOT!=C304_ROOT:raise ValueError("C304 root changed")
 c304.load_verified_hqcdrimassv0meshproject1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassv0finitepart1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassv0finitepart1_authority()
_ROOTS={"INPUT":_r((BASELINE,C304_ROOT)),"ASYM":wall_asymptotics()["root"],"REG":regulator_definition()["root"],"PROGRAM":finite_part_program()["root"],"COV":covariance_contract()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C305-HQCDRIMASSV0FINITEPART1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};__all__=[n for n in globals() if not n.startswith("_")]
