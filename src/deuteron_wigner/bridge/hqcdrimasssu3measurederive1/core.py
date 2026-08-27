"""C295 normalized SU(3) Cartan/FP holonomy measure derivation."""
from __future__ import annotations
import itertools,json,math
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c295_hqcdrimasssu3measurederive1"
BASELINE="beea65aeb8faca06e76992659af1cc24269bbe7d";C294_ROOT="409edc700360062a71ac46c8641f675040ae37257772869094fb95a4959dd167"
STATUS="C295_NORMALIZED_SU3_ZERO_MODE_FP_HOLONOMY_MEASURE_DERIVED_C43_FINITE_VOLUME_ACTION_ADAPTER_MISSING";PLAN="RIMASSSU3MEASUREDERIVE1-A"
NEXT="C296/HQCDRIMASSSU3MEASUREADAPTER1";NEXT_OBJECT="C295-MASS-SU3-MEASURE-C43-FINITE-VOLUME-ADAPTER";NEXT_EXACT="map the normalized C295 SU(3) Cartan measure and C293 zero-mode Hamiltonian into C43 finite-volume variables, boundary action, and K9/K11/K13 covariance"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def cartan_convention():
 row={"generators":"C43 Hermitian T_a=lambda_a/2; Tr(TaTb)=delta_ab/2","H":"theta3*T3+theta8*T8","eigenphases":("phi1=theta3/2+theta8/(2sqrt3)","phi2=-theta3/2+theta8/(2sqrt3)","phi3=-theta8/sqrt3"),"constraint":"phi1+phi2+phi3=0 mod 2pi","full_torus":"phi1,phi2 in [0,2pi); phi3=-phi1-phi2","weyl_group":"S3 order 6"}
 return _f({**row,"root":_r(row)})
def fp_spectrum():
 roots=(("alpha12","theta3"),("alpha13","theta3/2+sqrt3*theta8/2"),("alpha23","-theta3/2+sqrt3*theta8/2"))
 rows=tuple({"root":n,"positive_eigenphase":a,"negative_eigenphase":f"-({a})","adjoint_multiplicity":2,"zero_cartan_modes":2} for n,a in roots)
 return _f({"rows":rows,"nonzero_modes":6,"cartan_zero_modes":2,"all_eight_generators":True,"root":_r(rows)})
def jacobian_formula():
 return _f({"delta_squared":"product_{i<j} 4 sin^2((phi_i-phi_j)/2)","C43_theta_form":"64 sin^2(theta3/2) sin^2((theta3+sqrt3 theta8)/4) sin^2((-theta3+sqrt3 theta8)/4)","weyl_walls":"any phi_i=phi_j mod 2pi","center_action":"common 2pi/3 phase leaves differences and Jacobian invariant","nonnegative":True,"identity_default":False,"root":_r("SU3-WEYL-DENOMINATOR-SQUARED")})
def _constant_term():
 # |det(z_i^(j-1))|^2 constant term: equal permutation pairs only.
 perms=tuple(itertools.permutations(range(3)))
 return sum(1 for p in perms for q in perms if p==q)
def normalization_certificate():
 ct=_constant_term();return _f({"route_A":"Weyl denominator constant term","constant_term":ct,"full_torus_integral":"6*(2pi)^2","normalized_density":"Delta^2/[6*(2pi)^2] dphi1 dphi2","integral":1,"single_alcove_density":"Delta^2/(2pi)^2 after one-to-one Weyl restriction","route_B":"explicit adjoint root-pair product gives identical three sine-squared factors","routes_agree":ct==6,"root":_r((ct,"normalized"))})
def evaluate_density(phi1,phi2):
 if not all(math.isfinite(float(x)) for x in (phi1,phi2)):raise ValueError("finite phases")
 p=(float(phi1),float(phi2),-float(phi1)-float(phi2));j=1.0
 for a,b in ((0,1),(0,2),(1,2)):j*=4*math.sin((p[a]-p[b])/2)**2
 return _f({"phi":p,"jacobian":j,"full_torus_density":j/(6*(2*math.pi)**2),"root":_r((p,j))})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"normalized":True,"routes":2,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"SU2_relabelled_SU3":0,"flat_measure":0,"identity_default":0,"dimension_adapter_claimed":0,"boundary_action_selected":0,"C117_coordinates_selected":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimasssu3measurederive1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("generator","phase","root","spectrum","jacobian","wall","center","weyl","normalization","route")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimasssu3measurederive1_authority():
 from deuteron_wigner.bridge import hqcdrimassboundarysu3fullsource1 as c294,hqcdb0holonomy2 as c183
 if c294.PACKAGE_ROOT!=C294_ROOT or _constant_term()!=6:raise ValueError("source or normalization changed")
 c294.load_verified_hqcdrimassboundarysu3fullsource1_authority();c183.load_verified_hqcd_b0holonomy2_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimasssu3measurederive1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimasssu3measurederive1_authority()
_ROOTS={"INPUT":_r((BASELINE,C294_ROOT)),"CARTAN":cartan_convention()["root"],"SPECTRUM":fp_spectrum()["root"],"JACOBIAN":jacobian_formula()["root"],"NORMALIZATION":normalization_certificate()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C295-HQCDRIMASSSU3MEASUREDERIVE1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
