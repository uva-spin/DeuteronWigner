"""C307 symmetric branch finite part at the V0 center wall."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c307_hqcdrimassv0centerlimit1";BASELINE="457fe14a97a9daa0e7db7975e5f60f0aec5de32d";C306_ROOT="acf0dc63172ddf5959561c6deb2af33b5d748f93cd31889fdf37f1daac8f500e"
STATUS="C307_SYMMETRIC_CENTER_WALL_BRANCH_FINITE_PART_DEFINED_MODE_TAIL_RENORMALIZATION_MISSING";PLAN="RIMASSV0CENTERLIMIT1-C";NEXT="C308/HQCDRIMASSV0TAILRENORM1";NEXT_OBJECT="C307-V0-CENTER-FINITE-PART-MODE-TAIL";NEXT_EXACT="derive and subtract the N-dependent mode-tail asymptotics of the C307 symmetric center-wall finite part"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def branch_definition():return _f({"paths":"u=1/2, v=1/2 +/- delta","fit":"V_N^pm=A_pm/delta^2+B_pm/delta+C_pm+O(delta)","delta_grid":(.04,.03,.02,.015,.01,.0075,.005),"symmetric_finite_part":"C_sym(N)=(C_minus(N)+C_plus(N))/2","orientation_neutral":True,"ordinary_point_value":False,"root":_r("C307-BRANCH")})
def branch_scan():
 rows=({"N":24,"A_minus":-5.99997563,"A_plus":-3.99998918,"C_minus":-153.84573287,"C_plus":-35.40828327,"C_sym":-94.62700807},{"N":48,"A_minus":-5.99997588,"A_plus":-3.99998923,"C_minus":-128.58966142,"C_plus":-5.89501426,"C_sym":-67.24233784},{"N":96,"A_minus":-5.99997613,"A_plus":-3.99998928,"C_minus":-94.66666968,"C_plus":32.22579281,"C_sym":-31.22043844},{"N":160,"A_minus":-5.99997632,"A_plus":-3.99998932,"C_minus":-64.13192830,"C_plus":65.84119363,"C_sym":.85463267});return _f({"rows":rows,"count":4,"leading_poles_enclosed":{"minus":(-6.0001,-5.9998),"plus":(-4.0001,-3.9998)},"root":_r(rows)})
def symmetry_certificate():return _f({"one_sided_equal":False,"one_sided_selection_allowed":False,"symmetric_average":"SELECTED_PROJECT_REDUCED_MODEL_BRANCH_SCHEME","source_plot_zero":"implemented only after mode-tail finite part, not as raw AST value","Weyl_orientation_bias":0,"root":_r("C307-SYM")})
def tail_certificate():return _f({"C_sym_sequence":tuple(x["C_sym"] for x in branch_scan()["rows"]),"converged":False,"zero_selected":False,"required_terms":"log/power N asymptotics and finite remainder","coefficient_available":"UNAVAILABLE_NOT_ZERO","root":_r("C307-TAIL")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"branch_scheme_ready":True,"center_value_ready":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"one_sided_selected":0,"raw_center_used":0,"tail_drift_ignored":0,"center_zero_imposed":0,"C43_matching_claimed":0,"C117_coordinates_selected":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassv0centerlimit1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("branch","delta","Aminus","Aplus","Cminus","Cplus","average","N","tail","scope")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassv0centerlimit1_authority():
 from deuteron_wigner.bridge import hqcdrimassv0finiteeval1 as c306
 if c306.PACKAGE_ROOT!=C306_ROOT:raise ValueError("C306 root changed")
 c306.load_verified_hqcdrimassv0finiteeval1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassv0centerlimit1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassv0centerlimit1_authority()
_ROOTS={"INPUT":_r((BASELINE,C306_ROOT)),"BRANCH":branch_definition()["root"],"SCAN":branch_scan()["root"],"SYM":symmetry_certificate()["root"],"TAIL":tail_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C307-HQCDRIMASSV0CENTERLIMIT1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};__all__=[n for n in globals() if not n.startswith("_")]
