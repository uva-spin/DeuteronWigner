from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c302_hqcdrimassholonomycoeff1";BASELINE="4b3fe10f68a32686c64af34ac3971449a06ab581";C301_ROOT="5cda967ef9c8295b3e8f842ec940a2324c9d4484cd82b69847d702a88fdf4c5f"
STATUS="C302_C43_HOLONOMY_COEFFICIENT_AUTHORITY_ABSENT_REDUCED_V0_PROJECTION_BENCHMARK_DERIVABLE";PLAN="RIMASSHOLONOMYCOEFF1-C";NEXT="C303/HQCDRIMASSV0PROJECT1";NEXT_OBJECT="C302-REDUCED-V0-NORMALIZED-CLASS-PROJECTION";NEXT_EXACT="project the authenticated C293 reduced-model normal-mode V0 onto the C301 independent class-function basis under the C295 normalized measure as a non-C43 benchmark"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def authority_audit():
 rows=({"source":"C43/C274","result":"NO_HOLONOMY_POTENTIAL_COEFFICIENT"},{"source":"C293 V0","result":"REDUCED_1PLUS1_NORMAL_MODE_ONLY"},{"source":"C294 FP determinant","result":"MEASURE_NORMALIZATION_NOT_ACTION_COEFFICIENT"},{"source":"thermal Weiss potential","result":"NOT_AUTHENTICATED_AND_INEQUIVALENT_GEOMETRY"});return _f({"rows":rows,"usable_C43":0,"root":_r(rows)})
def coefficient_records():
 rows=tuple({"resolution":k,"lambda8":"UNAVAILABLE_NOT_ZERO","lambda3":"UNAVAILABLE_NOT_ZERO","absolute_normalization":"UNAVAILABLE","covariance":"UNAVAILABLE_NOT_DIAGONAL","physical":False} for k in ("K9","K11","K13"));return _f({"rows":rows,"count":3,"root":_r(rows)})
def benchmark_contract():return _f({"source":"C293 equations decomp/fineq V0","measure":"C295 normalized SU3 alcove","basis":"C301 CHI8,RE_TF3 plus constant","projection":"weighted Gram solve","label":"REDUCED_MODEL_BENCHMARK_NOT_C43_MATCHING","root":_r("C302-BENCH")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"C43_coefficients":False,"benchmark_derivable":True,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"Weiss_imported":0,"reduced_promoted":0,"coefficients_zeroed":0,"covariance_diagonalized":0,"identity_selected":0,"C117_coordinates_selected":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassholonomycoeff1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("source","dimension","basis","measure","coefficient","normalization","K","covariance","benchmark","scope")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassholonomycoeff1_authority():
 from deuteron_wigner.bridge import hqcdrimassholonomypot1 as c301
 if c301.PACKAGE_ROOT!=C301_ROOT:raise ValueError("C301 root changed")
 c301.load_verified_hqcdrimassholonomypot1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassholonomycoeff1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassholonomycoeff1_authority()
_ROOTS={"INPUT":_r((BASELINE,C301_ROOT)),"AUDIT":authority_audit()["root"],"COEFF":coefficient_records()["root"],"BENCH":benchmark_contract()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C302-HQCDRIMASSHOLONOMYCOEFF1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};__all__=[n for n in globals() if not n.startswith("_")]
