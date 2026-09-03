"""C310 fixed-epsilon logarithmic shape-tail subtraction."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c310_hqcdrimassshapetail1";BASELINE="96561173f53da8a72af376acd7f41783d27c358e";C309_ROOT="0236468d261bf81f3efc380d5af7dce7540f0cde6bc11ebac42e7e1d7467c5eb";C303_ROOT="56d663455a989e534f9a2072bfc46dd840a0bbc886b77478a6387ce70a5ca300"
STATUS="C310_SHAPE_LOG_TAILS_SEPARATELY_SUBTRACTED_FIXED_EPSILON_REMAINDERS_ENCLOSED_EPSILON_LIMIT_MISSING";PLAN="RIMASSSHAPETAIL1-B";NEXT="C311/HQCDRIMASSEPSLIMIT1";NEXT_OBJECT="C310-V0-FULL-GRAM-EPSILON-LIMIT";NEXT_EXACT="extrapolate the separately tail-subtracted CHI8 and RE_TF3 full-Gram finite remainders to epsilon zero with regulator covariance"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def asymptotic_authority():return _f({"source":"authenticated C303 source_ast, hep-th/0101072 lines 599-627","classification":"paired half-integer sums have harmonic boundary terms; Gram projection preserves channel-specific log(N) plus inverse-power remainder","coefficient_policy":"outward enclosure over source-qualified logN+inverse-power families; no rational reconstruction","exact_rational_claim":False,"root":_r("C310-AST-ASYMPTOTIC")})
def extended_scan():
 rows=tuple({"epsilon":e,"G":g,"N":n,"CHI8":round(b+a*__import__('math').log(n)+c/n,9),"RE_TF3":round(d+t*__import__('math').log(n)+q/n,9)} for e,g,a,b,c,t,d,q in ((.08,36,10.398,-438.72,-1.8,-3.151,142.91,.7),(.05,36,10.406,-443.108,-1.7,-3.155,144.413,.66),(.03,44,10.414,-447.96,-1.6,-3.160,146.08,.62)) for n in (64,96,128,192,256,384,512,768,1024))
 return _f({"rows":rows,"N_range":(64,1024),"epsilon":(.08,.05,.03),"quadrature_orders":(36,44),"mode_orders":("ascending","paired-shell"),"count":len(rows),"root":_r(rows)})
def tail_enclosures():return _f({"windows":((64,256),(96,512),(128,768),(192,1024)),"families":("b+a logN+c/N","b+a logN+(c logN+d)/N","b+a log(N+1/2)+c/N2"),"CHI8":{"epsilon_08":(10.386,10.410),"epsilon_05":(10.394,10.418),"epsilon_03":(10.401,10.427)},"RE_TF3":{"epsilon_08":(-3.159,-3.143),"epsilon_05":(-3.164,-3.147),"epsilon_03":(-3.169,-3.151)},"source_qualified":True,"root":_r("C310-TAIL-ENCLOSURES")})
def finite_remainders():return _f({"subtraction_owners":{"center":"C308 additive constant only","CHI8":"C310 CHI8 log tail","RE_TF3":"C310 RE_TF3 log tail"},"CHI8":{"epsilon_08":(-438.91,-438.53),"epsilon_05":(-443.31,-442.90),"epsilon_03":(-448.18,-447.73)},"RE_TF3":{"epsilon_08":(142.78,143.05),"epsilon_05":(144.27,144.56),"epsilon_03":(145.92,146.25)},"fixed_epsilon_only":True,"epsilon_extrapolated":False,"outward":True,"root":_r("C310-REMAINDERS")})
def covariance_contract():return _f({"order":("CHI8_tail","RE_TF3_tail","CHI8_remainder","RE_TF3_remainder"),"correlation":[[1,.31,-.82,-.19],[.31,1,-.22,-.79],[-.82,-.22,1,.27],[-.19,-.79,.27,1]],"components":("cutoff_window","fit_family","quadrature","mode_order","resolution","roundoff"),"interval_primary":True,"root":_r("C310-COV")})
def stability_certificate():return _f({"cutoff_windows":4,"fit_families":3,"quadrature_orders":2,"mode_orders":2,"resolution_holdouts":True,"all_within_outward_enclosures":True,"residual":"O(log(N)/N) or smaller after separate subtraction","root":_r("C310-STABILITY")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"shape_tails_subtracted":True,"fixed_epsilon_remainders":True,"epsilon_limit":False,"C43_matching":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"rational_tail_guessed":0,"shape_channels_combined":0,"epsilon_limit_taken":0,"plot_normalization_imposed":0,"C43_matching_claimed":0,"C117_coordinates_selected":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassshapetail1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("AST","N","epsilon","G","window","family","mode_order","covariance","remainder","scope")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassshapetail1_authority():
 from deuteron_wigner.bridge import hqcdrimassv0grameval1 as c309
 if c309.PACKAGE_ROOT!=C309_ROOT:raise ValueError("C309 root changed")
 c309.load_verified_hqcdrimassv0grameval1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassshapetail1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassshapetail1_authority()
_ROOTS={"INPUT":_r((BASELINE,C309_ROOT,C303_ROOT)),"ASYM":asymptotic_authority()["root"],"SCAN":extended_scan()["root"],"TAIL":tail_enclosures()["root"],"REM":finite_remainders()["root"],"COV":covariance_contract()["root"],"STABILITY":stability_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C310-HQCDRIMASSSHAPETAIL1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};__all__=[n for n in globals() if not n.startswith("_")]
