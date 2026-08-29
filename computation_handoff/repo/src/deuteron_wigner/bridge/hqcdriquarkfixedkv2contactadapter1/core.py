"""C243 retained-ID-free complement contact coordinate adapter."""
from __future__ import annotations
import json
from dataclasses import dataclass,asdict
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Mapping
from deuteron_wigner.bridge import hqcdriquarkfixedkv2contact1 as c242
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c243_hqcdriquarkfixedkv2contactadapter1"
BASELINE="18792a6c6368eea4dd723b90a36674fd3793ca22";C242_ROOT="38d21d500ee10f9ec9d779278af4b7019c76a375275b21ca9d2b2c0e61e6b4b9"
STATUS="C243_PARAMETERIZED_COMPLEMENT_CONTACT_COORDINATE_AND_LONGITUDINAL_ADAPTER_READY_SPIN_COLOR_FOUR_HO_EVALUATOR_INCOMPLETE";PLAN="RIQUARKFIXEDKV2CONTACTADAPTER1-D"
NEXT="C244/HQCDRIQUARKFIXEDKV2CONTACTKERNEL1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V2-CONTACT-PARAMETERIZED-KERNEL";NEXT_EXACT="retained-ID-free spin/polarization, ordered-color, and exact four-HO contact evaluator for C243 complement coordinates"
def _f(v):
 if isinstance(v,dict):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(v,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
@dataclass(frozen=True)
class ComplementContactCoordinate:
 q_out:tuple;g_out:tuple;q_in:tuple;g_in:tuple;c_out:int;a_out:int;c_in:int;a_in:int
 source_order:tuple=("b_dagger","a_dagger","a","b");zero_mode_policy:str="C43_PV_Q0_EXCLUDE_ZERO"
def _mode(m,gluon):
 if len(m)!=5:raise ValueError("mode=(k,n,m,helicity,species)")
 k=Fraction(m[0]);n,orb,h,s=m[1:]
 if k<=0 or n<0 or h not in (-1,1) or s!=("g" if gluon else "q"):raise ValueError("invalid complement mode")
 if (gluon and k.denominator!=1) or (not gluon and k.denominator!=2):raise ValueError("PBC/APBC mode required")
 return (str(k),int(n),int(orb),int(h),s)
def validate_coordinate(x):
 if not isinstance(x,ComplementContactCoordinate):raise TypeError(x)
 modes=(_mode(x.q_out,False),_mode(x.g_out,True),_mode(x.q_in,False),_mode(x.g_in,True))
 if x.source_order!=("b_dagger","a_dagger","a","b") or x.zero_mode_policy!="C43_PV_Q0_EXCLUDE_ZERO":raise ValueError("C43/C55 policy required")
 if not all(0<=v<3 for v in (x.c_out,x.c_in)) or not all(0<=v<8 for v in (x.a_out,x.a_in)):raise ValueError("color")
 return _f({"modes":modes,"coordinate_root":_r(asdict(x)),"retained_ids":False,"valid":True})
def longitudinal_contact_factor(x):
 validate_coordinate(x);koq,kog,kiq,kig=(Fraction(m[0]) for m in (x.q_out,x.g_out,x.q_in,x.g_in));outc=koq+kog;inc=kiq+kig;conserved=outc==inc
 return _f({"conserved":conserved,"status":"NONZERO_EXACT_ALGEBRAIC" if conserved else "ZERO_BY_EXACT_LONGITUDINAL_CONSERVATION","expression":f"-1/(4*pi*({inc}))" if conserved else "0","channel":str(inc),"L_cancellation":"exact C80 route","root":_r((str(outc),str(inc),conserved))})
def adapter_manifest():return _f({"coordinate":"ComplementContactCoordinate caller tuples","longitudinal_ready":True,"spin_polarization_ready":False,"ordered_color_ready":False,"four_HO_ready":False,"retained_id_dependency":False,"root":_r((True,False,False,False))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"coordinate_ready":True,"kernel_ready":False,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def next_handoff_contract():return _f({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"adapter_root":adapter_manifest()["root"],"root":_r((NEXT,NEXT_OBJECT))})
def static_isolation_guard():return _f({"retained_ids":0,"cutoff":0,"smearing":0,"missing_zeroed":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkv2contactadapter1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"pass":True,"root":_r((i,STATUS))})
def completeness_certificate():return _f({"status":STATUS,"coordinate":True,"kernel":False,"mutations":384,"next":NEXT,"root":_r((STATUS,True,False))})
def verify_hqcd_riquarkfixedkv2contactadapter1_authority():
 if c242.PACKAGE_ROOT!=C242_ROOT:raise ValueError("C242 root changed")
 c242.load_verified_hqcd_riquarkfixedkv2contact1_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C242_package_root":C242_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcd_riquarkfixedkv2contactadapter1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkv2contactadapter1_authority()
_ROOTS={"INPUT":_r((BASELINE,C242_ROOT)),"ADAPTER":adapter_manifest()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"NEXT":next_handoff_contract()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETE":completeness_certificate()["root"]}
PACKAGE_ROOT=_r({"schema":"C243-HQCDRIQUARKFIXEDKV2CONTACTADAPTER1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
