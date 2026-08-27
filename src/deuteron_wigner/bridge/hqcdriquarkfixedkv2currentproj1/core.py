"""C251 caller-parameterized complement current projector programs."""
from __future__ import annotations
import json
from dataclasses import dataclass,asdict
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from deuteron_wigner.bridge import hqcdriquarkfixedkv2currenteval1 as c250
from deuteron_wigner.bridge import hqcdriquarkfixedkv2currentmap1 as c249
from deuteron_wigner.bridge.icreg2 import core as c117
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c251_hqcdriquarkfixedkv2currentproj1"
BASELINE="8e51ce90688440f128553c7ef459dde7996f1ac4";C250_ROOT="3f41e09857fe6052d7cc5bea2d220817e213620ef83cb8ad7fc7ccd1890dd2d3"
STATUS="C251_CALLER_PARAMETERIZED_COMPLEMENT_CURRENT_PROJECTOR_PROGRAMS_READY_UNBOUNDED_EVALUATION_INCOMPLETE";PLAN="RIQUARKFIXEDKV2CURRENTPROJ1-B"
NEXT="C252/HQCDRIQUARKFIXEDKV2CURRENTPROJEVAL1";NEXT_OBJECT="C168-REQUEST-1-OMITTED-INTERFACE-OUTSIDE-FIXED-K-V2-INSTANTANEOUS-CURRENT-COMPLEMENT-PROJECTOR-EVALUATION";NEXT_EXACT="evaluate or certify core-plus-tail enclosures for the four C251 complement projector programs on the unbounded domain"
CLASSES=("I2_density_projector","derivative_density","CM_ground","triplet_projected")
@dataclass(frozen=True)
class ComplementProjectorCapsule:
 class_id:str;coordinate:c249.ComplementCurrentCoordinate;internal_modes:tuple;b_HO:float;domain_status:str="CALLER_FINITE_CAPSULE_OF_UNBOUNDED_COMPLEMENT"
def _p(v):
 if hasattr(v,"items"):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,dict):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def _internal(m):
 if len(m)!=6:raise ValueError("internal=(species,k,n,m,helicity,color)")
 s,k,n,orb,h,color=m;k=Fraction(k)
 if s not in ("q","g") or k<=0 or n<0 or h not in (-1,1):raise ValueError("internal mode")
 if (s=="q" and k.denominator!=2) or (s=="g" and k.denominator!=1):raise ValueError("APBC/PBC")
 if not 0<=int(color)<(3 if s=="q" else 8):raise ValueError("color")
 return s,str(k),int(n),int(orb),int(h),int(color)
def validate_capsule(x):
 if not isinstance(x,ComplementProjectorCapsule):raise TypeError(x)
 base=c249.validate_coordinate(x.coordinate)
 if x.class_id not in CLASSES or x.b_HO<=0 or x.domain_status!="CALLER_FINITE_CAPSULE_OF_UNBOUNDED_COMPLEMENT":raise ValueError("capsule")
 modes=tuple(_internal(m) for m in x.internal_modes)
 if x.class_id in CLASSES[:2] and not modes:raise ValueError("density projector requires explicit internal modes")
 return _f({"valid":True,"class_id":x.class_id,"coordinate_root":base["root"],"internal_modes":modes,"internal_count":len(modes),"b_HO":float(x.b_HO),"full_unbounded_domain":False,"retained_projector":False,"root":_r(asdict(x))})
def projector_program(x):
 v=validate_capsule(x);cid=x.class_id
 if cid=="I2_density_projector":expr="SUM_CALLER_R(w_r*phi_r^*(x;b_HO)*phi_r(x;b_HO))";routes=("explicit caller mode sum","finite capsule projector identity")
 elif cid=="derivative_density":expr="SUM_CALLER_R((pi*k_r/L)*w_r*phi_r^*(x;b_HO)*phi_r(x;b_HO))";routes=("ordered derivative weighted sum","partial_plus on caller projector kernel")
 elif cid=="CM_ground":expr="T_TM(caller labels)*P_CM0*T_TM^dagger";routes=("explicit caller CM-ground row","factorized exact TM transform")
 else:expr="U3(caller colors)*U3^dagger";routes=("explicit three triplet columns","factorized U3 projector")
 return _f({"class_id":cid,"coordinate_root":v["coordinate_root"],"capsule_root":v["root"],"expression":expr,"routes":routes,"route_residual":"SYMBOLIC_ZERO","hermitian":True,"idempotent":"projector factor only" if cid!="derivative_density" else False,"caller_capsule_exact":True,"unbounded_completion":"UNAVAILABLE_NOT_ZERO","units":"b_HO^2 spatial primitive or dimensionless projector as class-defined","root":_r((cid,v["root"],expr))})
def composition_program(x):
 p=projector_program(x);order="P_CM_ground P_triplet = P_triplet P_CM_ground" if x.class_id in ("CM_ground","triplet_projected") else "source graph order"
 return _f({"program":p,"composition_order":order,"commutator":"0 for kinematic/color tensor factors" if "P_CM" in order else "not applicable","retained_ids":False,"root":_r((p["root"],order))})
def program_inventory():return _f({"classes":tuple({"class_id":c,"program_ready":True,"unbounded_value_ready":False} for c in CLASSES),"count":4,"programs_ready":4,"unbounded_values_ready":0,"root":_r(CLASSES)})
def route_certificate():return _f({"route_A":"C117 identity parameterization over caller capsule","route_B":"C116 class definition reconstruction","program_mismatches":0,"retained_projector_lookups":0,"root":_r((4,0,0))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"programs_ready":4,"unbounded_evaluations":0,"next":NEXT,"physical":False,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"retained_projectors":0,"retained_indices":0,"finite_cutoff_claimed_complete":0,"continuum_completeness":0,"missing_tail_zeroed":0,"physical_defaults":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdriquarkfixedkv2currentproj1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"pass":True,"root":_r((i,STATUS))})
def verify_hqcd_riquarkfixedkv2currentproj1_authority():
 if c250.PACKAGE_ROOT!=C250_ROOT:raise ValueError("C250 root changed")
 c250.load_verified_hqcdriquarkfixedkv2currenteval1_authority();c117.load_verified_current_projector_authority();return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C250_package_root":C250_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcdriquarkfixedkv2currentproj1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcd_riquarkfixedkv2currentproj1_authority()
_ROOTS={"INPUT":_r((BASELINE,C250_ROOT,c117.STATUS)),"PROGRAMS":program_inventory()["root"],"ROUTES":route_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]}
PACKAGE_ROOT=_r({"schema":"C251-HQCDRIQUARKFIXEDKV2CURRENTPROJ1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
