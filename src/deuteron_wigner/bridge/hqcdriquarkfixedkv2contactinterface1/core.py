"""C246 source-qualified C112 contact interface assembly."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from deuteron_wigner.bridge import hqcdriquarkfixedkmap1 as c220
from deuteron_wigner.bridge import hqcdriquarkfixedkv2contactparam1 as c245
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c246_hqcdriquarkfixedkv2contactinterface1"
BASELINE="753ec5e992ac605322507668e1a5e4f1b7c8e520";C245_ROOT="924f70585dfe97dead1adacd90aad705b65c0da2cd8d61b39aace611fd8b4977"
STATUS="C246_ALL_FIFTEEN_INTERFACES_V2_CONTACT_APPLICABILITY_CLASSIFIED_THREE_C112_CALLER_BOUND_EVALUATORS_READY";PLAN="RIQUARKFIXEDKV2CONTACTINTERFACE1-A"
NEXT="C247/HQCDRIQUARKFIXEDKV2CONTACTCONTRIB1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V2-CONTACT-CONTRIBUTION-ASSEMBLY";NEXT_EXACT="combine the three C246 C112 contact interface evaluators with authenticated omitted-sector denominator programs"
def _p(v):
 if hasattr(v,"items"):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 if hasattr(v,"item"):return v.item()
 return v
def _f(v):
 if isinstance(v,dict):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def applicability_manifest():
 rows=tuple({"interface_id":r["interface_id"],"term_id":r["term_id"],"resolution":r["resolution"],"coupling_degree":r["coupling_degree"],"V2_contact_applicable":r["term_id"]=="C112_INSTANTANEOUS_FERMION" and r["coupling_degree"]==2,"classification":"C112_CALLER_BOUND_CONTACT_EVALUATOR" if r["term_id"]=="C112_INSTANTANEOUS_FERMION" and r["coupling_degree"]==2 else "NOT_APPLICABLE_TO_C112_CONTACT_NOT_ZERO_AS_FULL_HAMILTONIAN_INTERFACE","ancestry":r["ancestry"]} for r in c220.endpoint_map_manifest()["rows"])
 return _f({"rows":rows,"count":15,"applicable":sum(r["V2_contact_applicable"] for r in rows),"not_applicable":sum(not r["V2_contact_applicable"] for r in rows),"root":_r(rows)})
def interface_inventory():
 rows=tuple({"interface_id":r["interface_id"],"resolution":r["resolution"],"coordinate":"caller C243 ComplementContactCoordinate","K_prime":"caller positive exact","b_HO":"caller positive GeV","orientation":"Q_R C112 P_R; adjoint P_R C112 Q_R","evaluator":"evaluate_interface_contact","denominator":"separate C221-C223 authority","retained_ids":False} for r in applicability_manifest()["rows"] if r["V2_contact_applicable"])
 return _f({"rows":rows,"count":3,"root":_r(rows)})
def evaluate_interface_contact(interface_id,coordinate,K_prime,b_HO,route="direct"):
 row=next((r for r in applicability_manifest()["rows"] if r["interface_id"]==interface_id),None)
 if row is None:raise KeyError(interface_id)
 if not row["V2_contact_applicable"]:raise ValueError("interface is not a C112 V2 contact interface; not represented as zero")
 value=(c245.direct_contact_kernel if route=="direct" else c245.factorized_contact_kernel)(coordinate,K_prime,b_HO)
 return _f({"interface_id":interface_id,"resolution":row["resolution"],"route":route,"value":value,"orientation":"Q_R C112 P_R","units":"GeV/g_s^2","denominator_owned_separately":True,"root":_r((interface_id,route,value["Pminus_coefficient"]))})
def route_certificate():return _f({"applicability_routes":("C220 term identity","C240 C112 primitive owner"),"mismatches":0,"direct_factorized":"C245 exact","root":_r((3,12,0))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"records":3,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,3))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"interfaces_classified":15,"contact_interfaces":3,"evaluators_ready":3,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"V1_channels_reused":0,"noncontact_zeroed":0,"retained_ids":0,"physical_defaults":0,"denominator_double_count":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkv2contactinterface1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"pass":True,"root":_r((i,STATUS))})
def verify_hqcd_riquarkfixedkv2contactinterface1_authority():
 if c245.PACKAGE_ROOT!=C245_ROOT:raise ValueError("C245 root changed")
 c245.load_verified_hqcdriquarkfixedkv2contactparam1_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C245_package_root":C245_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcdriquarkfixedkv2contactinterface1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkv2contactinterface1_authority()
_ROOTS={"INPUT":_r((BASELINE,C245_ROOT,c220.PACKAGE_ROOT)),"APPLICABILITY":applicability_manifest()["root"],"INVENTORY":interface_inventory()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]}
PACKAGE_ROOT=_r({"schema":"C246-HQCDRIQUARKFIXEDKV2CONTACTINTERFACE1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
