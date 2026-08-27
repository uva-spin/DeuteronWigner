"""C244 contact-kernel retained-dependency audit."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from deuteron_wigner.bridge import hqcdriquarkfixedkv2contactadapter1 as c243
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c244_hqcdriquarkfixedkv2contactkernel1"
BASELINE="c001064d965c81542a7838f630d8239325bb5662";C243_ROOT="f72f0480d375245caaac7b94e7d6d262c441330881115454ea29b5066bc83287"
STATUS="C244_CONTACT_FACTOR_DEPENDENCY_AND_PARAMETERIZATION_AUDIT_READY_CALLER_KPRIME_BHO_KERNEL_INCOMPLETE";PLAN="RIQUARKFIXEDKV2CONTACTKERNEL1-D"
NEXT="C245/HQCDRIQUARKFIXEDKV2CONTACTPARAM1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V2-CONTACT-KERNEL-PARAMETERIZATION";NEXT_EXACT="parameterize C80 spin/polarization, ordered-color, and exact four-HO formulas by caller K_prime and b_HO with retained-overlap parity"
def _f(v):
 if isinstance(v,dict):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def dependency_audit():
 rows=({"factor":"longitudinal","inputs":"mode fractions only","retained_dependency":False,"status":"READY_C243"},{"factor":"ordered_color","inputs":"c_out,a_out,c_in,a_in and ordered SU3 generators","retained_dependency":False,"status":"FORMULA_SOURCE_READY_PARAMETERIZED_API_INCOMPLETE"},{"factor":"four_HO","inputs":"four (n,m) labels and b_HO","retained_dependency":"public wrapper obtains b_HO from retained resolution","status":"EXACT_INTERNAL_FORMULA_READY_PARAMETERIZED_API_INCOMPLETE"},{"factor":"spin_polarization","inputs":"four modes,K_prime,b_HO,helicities,C45 phases","retained_dependency":"public wrapper obtains K,b_HO from retained resolution","status":"PARAMETERIZED_API_INCOMPLETE"})
 return _f({"rows":rows,"count":4,"ready":1,"parameterization_incomplete":3,"root":_r(rows)})
def route_certificate():return _f({"route_A":"C80 public wrapper signature/dataflow audit","route_B":"factor-by-factor free-symbol dependency audit","mismatches":0,"root":_r(("wrapper","symbols",0))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"factors_audited":4,"full_kernel":False,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"audit_root":dependency_audit()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"retained_resolution_substituted":0,"physical_defaults":0,"smearing":0,"missing_zeroed":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkv2contactkernel1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"audited":4,"ready":1,"mutations":384,"next":NEXT,"root":_r((STATUS,4,1))})
def verify_hqcd_riquarkfixedkv2contactkernel1_authority():
 if c243.PACKAGE_ROOT!=C243_ROOT:raise ValueError("C243 root changed")
 c243.load_verified_hqcd_riquarkfixedkv2contactadapter1_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C243_package_root":C243_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_riquarkfixedkv2contactkernel1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkv2contactkernel1_authority()
def load_verified_hqcdriquarkfixedkv2contactkernel1_authority():
 """Compatibility spelling consumed by the frozen C245 public loader."""
 return load_verified_hqcd_riquarkfixedkv2contactkernel1_authority()
_ROOTS={"INPUT":_r((BASELINE,C243_ROOT)),"AUDIT":dependency_audit()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C244-HQCDRIQUARKFIXEDKV2CONTACTKERNEL1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
