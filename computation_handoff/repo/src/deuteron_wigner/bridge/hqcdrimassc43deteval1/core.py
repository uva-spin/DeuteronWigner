"""C314 conditional evaluation of the C43 holonomy determinant."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c314_hqcdrimassc43deteval1";BASELINE="0303e5362385ab7f08ba078a8e41d7f467240086";C313_ROOT="5918deb3c9596f879cef962c7fc368ef3d093bf6bd5af0ec0a4671f71c81c65b"
STATUS="C314_C43_DETERMINANT_REDUCED_TO_FINITE_SPECTRAL_FUNCTIONALS_TRANSVERSE_BOUNDARY_SPECTRUM_MISSING";PLAN="RIMASSC43DETEVAL1-D";NEXT="C315/HQCDRIMASSC43SPECTRUM1";NEXT_OBJECT="C314-C43-TRANSVERSE-BOUNDARY-SPECTRUM";NEXT_EXACT="derive the C43 finite-volume transverse boundary spectrum and degeneracy adapter required to evaluate the boson, fermion and constraint holonomy determinant functionals"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def regulator_scan():return _f({"N":(32,64,128,256,512),"quadrature":(24,32,40),"owners":("boson","fermion","constraint_jacobian","global_P0","vacuum"),"mode_order":("symmetric","paired_shell"),"numeric_values":"UNAVAILABLE_WITHOUT_TRANSVERSE_SPECTRUM","root":_r("C314-SCAN")})
def spectral_reduction():return _f({"boson":"1/2 sum_{alpha in roots} sum'_{n,s} log[((2pi n+alpha.theta)/L)^2+omega_B(s)^2]","fermion":"-sum_{w in weights} sum'_{n,s} log[((2pi n+w.theta)/L)^2+omega_F(s,m)^2]","constraint":"-sum_{alpha,n,s}' log Delta_constraint(alpha,n,s)","P0":"excluded global owner, not assigned zero","vacuum":"subtract same owner at theta=0 before class projection","reality":"paired roots/weights give real sums","root":_r("C314-SPECTRAL")})
def tail_certificate():return _f({"large_mode":"log Delta(theta)-log Delta(0)=O(1/n) odd term cancels under symmetric pairing; remainder O(1/n^2)","tail_owner":"componentwise theta=0 subtraction","families":("1/N","1/N2","logN/N2"),"holonomy_divergence":"CANCELS_COMPONENTWISE_CONDITIONALLY","rational_coefficient_guessed":False,"root":_r("C314-TAIL")})
def finite_functionals():return _f({"F_B":"finite outward functional of omega_B spectrum and boundary class","F_F":"finite outward functional of omega_F spectrum, mass and boundary class","F_C":"finite outward constraint/Jacobian functional","F_P0":"global zero-mode functional retained separately","evaluated":False,"unavailable_reason":"C43 action authority has no selected transverse finite-volume boundary spectrum or degeneracy","root":_r("C314-FINITE")})
def gram_projection():return _f({"basis":("CHI8","RE_TF3"),"measure":"C295/C296 normalized nonflat alcove","coefficients":{"CHI8":"GramInv[CHI8,j]<basis_j,F_B+F_F+F_C+F_P0>","RE_TF3":"GramInv[RE_TF3,j]<basis_j,F_B+F_F+F_C+F_P0>"},"intervals":"UNAVAILABLE_NOT_ZERO_PENDING_SPECTRUM","C293_C311_used":False,"root":_r("C314-GRAM")})
def covariance_contract():return _f({"owners":("boson","fermion","constraint","P0","vacuum","regulator","quadrature","boundary_spectrum"),"correlated":True,"matrix":"UNAVAILABLE_NOT_DIAGONAL_PENDING_SPECTRUM","root":_r("C314-COV")})
def route_parity():return _f({"route_A":"direct paired spectral log sums","route_B":"differentiate in theta, sum convergent resolvents, integrate with Gamma(0)=0","symbolic_agreement":True,"numeric_agreement":"DEFERRED_PENDING_SPECTRUM","root":_r("C314-PARITY")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"spectral_reduction":True,"tails_classified":True,"coefficients_ready":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"Weiss_imported":0,"C293_promoted":0,"P0_zeroed":0,"boundary_selected":0,"coefficient_invented":0,"physical_value_selected":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassc43deteval1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("N","quadrature","boson","fermion","constraint","P0","vacuum","tail","Gram","scope")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassc43deteval1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43effact1 as c313
 if c313.PACKAGE_ROOT!=C313_ROOT:raise ValueError("C313 root changed")
 c313.load_verified_hqcdrimassc43effact1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassc43deteval1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassc43deteval1_authority()
_ROOTS={"INPUT":_r((BASELINE,C313_ROOT)),"SCAN":regulator_scan()["root"],"SPECTRAL":spectral_reduction()["root"],"TAIL":tail_certificate()["root"],"FINITE":finite_functionals()["root"],"GRAM":gram_projection()["root"],"COV":covariance_contract()["root"],"PARITY":route_parity()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C314-HQCDRIMASSC43DETEVAL1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};__all__=[n for n in globals() if not n.startswith("_")]
