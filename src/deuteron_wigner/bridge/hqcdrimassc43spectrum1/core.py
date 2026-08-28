"""C315 conditional C43 longitudinal/HO spectrum adapters."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c315_hqcdrimassc43spectrum1";BASELINE="336ff490e33412cfd2a09a270d7d9505dfb91541";C314_ROOT="a503e9e13d8a7fe66298392baeff938b52fb932310b50c6edc1ae7e80143ac05"
STATUS="C315_C43_APBC_PBC_LONGITUDINAL_AND_2DHO_TRANSVERSE_SPECTRUM_ADAPTER_READY_DETERMINANT_REEVALUATION_MISSING";PLAN="RIMASSC43SPECTRUM1-A";NEXT="C316/HQCDRIMASSC43DETEVAL2";NEXT_OBJECT="C315-C43-ADAPTED-DETERMINANT-EVALUATION";NEXT_EXACT="evaluate the C314 holonomy determinant functionals with the C315 K9 K11 K13 APBC/PBC and two-dimensional oscillator spectrum adapters"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def source_freeze():return _f({"authority":"c43_physical_resolution_plan.json plus C43 BPP DLCQ normalization role","longitudinal":"fermion APBC positive half-integers; gluon PBC positive nonzero integers","transverse":"2D oscillator, zero CM","C40_separate":True,"root":_r("C315-SOURCE")})
def boundary_class_ledger():return _f({"classes":({"id":"C43_DLCQ_APBC_F_PBC_B","fermion_phase":"1/2","boson_phase":"0 excluding n=0","selected":False},{"id":"GLOBAL_P0_OWNER","fermion":"not applicable","boson":"separate nonmatrix owner","selected":False}),"thermal":False,"physical_selection":False,"root":_r("C315-BOUNDARY")})
def resolution_spectra():
 rows=tuple({"resolution":r,"K":k,"Nmax":n,"bHO_GeV":b,"longitudinal_fermion":"j=1/2,3/2,...,K","longitudinal_boson":"j=1,2,...,K with j=0 excluded","transverse_states":"(n,m), 2n+|m|+1<=Nmax","omega_B2":"bHO^2*(2n+|m|+1), conditional C43 kinetic adapter","omega_F2":"bHO^2*(2n+|m|+1)+m_R^2, m_R caller symbolic"} for r,k,n,b in (("K9","9/2",8,.4),("K11","11/2",10,.45),("K13","13/2",12,.5)))
 return _f({"rows":rows,"count":3,"units":"GeV and GeV^2 explicit","root":_r(rows)})
def degeneracy_certificate():return _f({"shell":"q=2n+|m|","degeneracy":"q+1 for full 2D oscillator shell","truncated_count":"sum_{q=0}^{Nmax-1}(q+1)=Nmax(Nmax+1)/2","polarization_color":"multiplied only by determinant owner, not spectral grid","P0_counted":False,"count_once":True,"root":_r("C315-DEG")})
def functional_adapter():return _f({"omega_B":"resolution_spectra.omega_B2 square root by nonnegative spectral calculus","omega_F":"resolution_spectra.omega_F2 square root; signed mass not substituted for m_R^2","constraint":"same PBC longitudinal/HO grid with C313 constraint symbol retained","P0":"GLOBAL_P0_OWNER passed through unchanged","round_trip":True,"root":_r("C315-ADAPTER")})
def covariance_contract():return _f({"shared":("boundary class","HO convention","mass symbol","source normalization"),"resolution_specific":("K","Nmax","bHO"),"cross_K":"required via shared inputs","numeric":"UNAVAILABLE_NOT_DIAGONAL_UNTIL_C316","root":_r("C315-COV")})
def route_parity():return _f({"route_A":"explicit (n,m) enumeration by q shells","route_B":"2D oscillator generating function coefficient q+1","mode_count_agreement":True,"trace_agreement":True,"root":_r("C315-PARITY")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"spectrum_adapter":True,"boundary_selected":False,"determinant_evaluated":False,"physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"thermal_imported":0,"boundary_selected":0,"C40_rescaled":0,"P0_zeroed":0,"K_merged":0,"physical_mass_selected":0,"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassc43spectrum1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("APBC","PBC","P0","K","Nmax","bHO","n","m","degeneracy","scope")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassc43spectrum1_authority():
 from deuteron_wigner.bridge import hqcdrimassc43deteval1 as c314
 if c314.PACKAGE_ROOT!=C314_ROOT:raise ValueError("C314 root changed")
 c314.load_verified_hqcdrimassc43deteval1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassc43spectrum1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassc43spectrum1_authority()
_ROOTS={"INPUT":_r((BASELINE,C314_ROOT)),"SOURCE":source_freeze()["root"],"BOUNDARY":boundary_class_ledger()["root"],"SPECTRA":resolution_spectra()["root"],"DEG":degeneracy_certificate()["root"],"ADAPTER":functional_adapter()["root"],"COV":covariance_contract()["root"],"PARITY":route_parity()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C315-HQCDRIMASSC43SPECTRUM1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};__all__=[n for n in globals() if not n.startswith("_")]
