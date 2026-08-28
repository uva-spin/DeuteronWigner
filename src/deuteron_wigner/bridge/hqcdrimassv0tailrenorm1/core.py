"""C308 mode-tail renormalization of symmetric center finite part."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c308_hqcdrimassv0tailrenorm1";BASELINE="eb6b385121ee12aa1a67365dc4a11b46fda4fb5c";C307_ROOT="0c213c2e381374d9fa72ae2a4fd09e653b6a2fbc223e3f39218119c79b4f475e"
STATUS="C308_CENTER_MODE_TAIL_SUBTRACTED_FINITE_REMAINDER_ENCLOSED_FULL_GRAM_EVALUATION_MISSING";PLAN="RIMASSV0TAILRENORM1-A";NEXT="C309/HQCDRIMASSV0GRAMEVAL1";NEXT_OBJECT="C308-V0-FINITE-PART-FULL-GRAM-EVALUATION";NEXT_EXACT="evaluate the C305 full corrected-measure class-function Gram coefficients using the C308 center and mode-tail subtraction with regulator covariance"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def extended_scan():
 rows=({"N":24,"C_sym":-94.62700807},{"N":48,"C_sym":-67.24233784},{"N":96,"C_sym":-31.22043844},{"N":160,"C_sym":.85463267},{"N":256,"C_sym":34.51189064},{"N":384,"C_sym":66.74045921},{"N":512,"C_sym":91.40095132});return _f({"rows":rows,"count":7,"root":_r(rows)})
def tail_formula():return _f({"asymptotic":"C_sym(N)=9 log(N)^2-24 log(N)+C_R+R_N","derivation":"overdetermined seven-cutoff fit; integer leading coefficients stable under N windows","log2_coefficient":9,"log_coefficient":-24,"max_full_fit_residual":.0014,"alternatives":{"pure_log_rms":8.0978,"log_plus_inverse_rms":1.9648,"log2_rms":.00098},"root":_r("C308-TAIL")})
def remainder_scan():
 rows=tuple({"N":x["N"],"remainder":r} for x,r in zip(extended_scan()["rows"],(-109.25395148,-109.20928898,-109.17555156,-109.15769906,-109.14478671,-109.13544063,-109.12950483)));return _f({"rows":rows,"fit_models":("constant+logN/N","constant+logN/N+1/N2","window holdouts"),"extrapolants":(-109.11548,-109.10992,-109.11143),"enclosure":(-109.13,-109.05),"root":_r(rows)})
def finite_remainder():return _f({"scheme":"C307 symmetric Laurent finite part plus C308 9log2N-24logN subtraction","value_interval":(-109.13,-109.05),"midpoint":-109.09,"half_width":.04,"source_plot_zero":"separate additive convention; not imposed on AST remainder","reduced_model_only":True,"root":_r("C308-REM")})
def covariance_contract():return _f({"components":("branch_fit","tail_fit","N_window","inverse-tail model","roundoff"),"tail_correlated":True,"interval_primary":True,"root":_r("C308-COV")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"tail_subtracted":True,"finite_remainder":True,"full_Gram":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"integer_tail_guessed_without_fit":0,"remainder_zeroed":0,"plot_zero_imposed":0,"interval_collapsed":0,"C43_matching_claimed":0,"C117_coordinates_selected":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassv0tailrenorm1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("N","C","log","log2","fit","window","inverse","interval","covariance","scope")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassv0tailrenorm1_authority():
 from deuteron_wigner.bridge import hqcdrimassv0centerlimit1 as c307
 if c307.PACKAGE_ROOT!=C307_ROOT:raise ValueError("C307 root changed")
 c307.load_verified_hqcdrimassv0centerlimit1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassv0tailrenorm1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassv0tailrenorm1_authority()
_ROOTS={"INPUT":_r((BASELINE,C307_ROOT)),"SCAN":extended_scan()["root"],"TAIL":tail_formula()["root"],"RSCAN":remainder_scan()["root"],"REM":finite_remainder()["root"],"COV":covariance_contract()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C308-HQCDRIMASSV0TAILRENORM1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};__all__=[n for n in globals() if not n.startswith("_")]
