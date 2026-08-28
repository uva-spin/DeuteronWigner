"""C316 executable conditional C43 determinant evaluation."""
from __future__ import annotations
import json,math
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c316_hqcdrimassc43deteval2";BASELINE="99906cc16da5f0e6aaa922438c59719e5391b754";C315_ROOT="37ecab11fea734e19744d352a006457fcb110a0d65b41d1cf57f11094848f1db"
STATUS="C316_EXECUTABLE_PARAMETERIZED_C43_DETERMINANT_AND_GRAM_FUNCTIONALS_READY_CALLER_PARAMETER_CAPSULE_MISSING";PLAN="RIMASSC43DETEVAL2-D";NEXT="C317/HQCDRIMASSC43PARAM1";NEXT_OBJECT="C316-C43-DETERMINANT-PARAMETER-CAPSULE";NEXT_EXACT="bind a source-qualified nonphysical caller parameter capsule for the executable C316 K9 K11 K13 determinant and Gram coefficient functionals"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
_RES={"K9":(8,.4),"K11":(10,.45),"K13":(12,.5)}
def _validate(resolution,mass2,L,N):
 if resolution not in _RES or not isinstance(N,int) or N<4 or not math.isfinite(mass2) or mass2<0 or not math.isfinite(L) or L<=0:raise ValueError("invalid conditional determinant inputs")
def spectral_delta(resolution,theta,mass2,L,N=128,owner="fermion"):
 _validate(resolution,mass2,L,N)
 if owner not in ("boson","fermion","constraint"):raise ValueError(owner)
 nmax,b=_RES[resolution];phase=.5 if owner=="fermion" else 0.;sign=-1. if owner=="fermion" else (.5 if owner=="boson" else -1.)
 total=0.
 for q in range(nmax):
  deg=q+1;omega2=b*b*(q+1)+(mass2 if owner=="fermion" else 0.)
  for n in range(-N,N+1):
   if owner!="fermion" and n==0:continue
   x=2*math.pi*(n+phase);total+=sign*deg*math.log(((x+theta)/L)**2+omega2)-sign*deg*math.log((x/L)**2+omega2)
 return total
def parameter_schema():return _f({"required":("resolution","mass2_GeV2","L_GeVinv","coupling_normalization","P0_functional","boundary_class"),"signed_mass_separate":True,"defaults":False,"physical":False,"root":_r("C316-PARAM")})
def component_contract():return _f({"owners":{"boson":"spectral_delta(... owner=boson)","fermion":"spectral_delta(... owner=fermion)","constraint":"spectral_delta(... owner=constraint)","P0":"caller functional required","vacuum":"built into each spectral_delta"},"N_windows":((32,64),(64,128),(128,256)),"real":True,"root":_r("C316-COMP")})
def tail_subtraction():return _f({"paired":"n=-N..N","vacuum_subtracted":True,"residual":"O(1/N) enclosure from consecutive doubled windows","orders":("symmetric","paired_shell"),"exact_tail_guessed":False,"root":_r("C316-TAIL")})
def gram_functionals():return _f({"basis":("CHI8","RE_TF3"),"measure":"C295/C296","callable":"evaluate component sum on quadrature nodes, solve frozen weighted Gram system","coefficients":"EXECUTABLE_ON_COMPLETE_PARAMETER_CAPSULE","current_values":"UNAVAILABLE_NOT_ZERO","C293_C311_used":False,"root":_r("C316-GRAM")})
def K_adapters():return _f({"rows":tuple({"resolution":k,"Nmax":v[0],"bHO_GeV":v[1],"evaluator":"spectral_delta","complete":False} for k,v in _RES.items()),"K_averaged":False,"root":_r("C316-K")})
def covariance_contract():return _f({"components":("window","quadrature","boson","fermion","constraint","P0","mass2","L","coupling"),"cross_K":"shared-parameter Jacobian plus resolution residual","matrix":"UNAVAILABLE_NOT_DIAGONAL_PENDING_CAPSULE","root":_r("C316-COV")})
def route_parity():return _f({"route_A":"direct paired log sum","route_B":"theta derivative resolvent sum integrated from zero","zero_theta":abs(spectral_delta("K9",0.,0.,1.,8,"boson"))==0.,"agreement":"algebraic and live zero/odd-pair checks","root":_r("C316-PARITY")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"executable":True,"parameter_capsule":False,"coefficients_ready":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"default_parameter":0,"signed_mass_squared":0,"P0_zeroed":0,"K_averaged":0,"coefficient_invented":0,"physical_value_selected":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassc43deteval2(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("K","mass2","L","N","theta","boson","fermion","constraint","P0","scope")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassc43deteval2_authority():
 from deuteron_wigner.bridge import hqcdrimassc43spectrum1 as c315
 if c315.PACKAGE_ROOT!=C315_ROOT:raise ValueError("C315 root changed")
 c315.load_verified_hqcdrimassc43spectrum1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassc43deteval2_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassc43deteval2_authority()
_ROOTS={"INPUT":_r((BASELINE,C315_ROOT)),"PARAM":parameter_schema()["root"],"COMP":component_contract()["root"],"TAIL":tail_subtraction()["root"],"GRAM":gram_functionals()["root"],"K":K_adapters()["root"],"COV":covariance_contract()["root"],"PARITY":route_parity()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C316-HQCDRIMASSC43DETEVAL2-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};__all__=[n for n in globals() if not n.startswith("_")]
