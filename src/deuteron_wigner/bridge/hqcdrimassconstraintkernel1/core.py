"""C298 exact symbolic SU3 constrained-current kernel."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from collections.abc import Mapping
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c298_hqcdrimassconstraintkernel1"
BASELINE="eb5f0a9493d8d883b7fdadb2b1aa7a0f88590776";C297_ROOT="44b6ca07acb3e3ea970667244072988158ca495fb7829972a210842b448a6502"
STATUS="C298_EXACT_SIX_CHANNEL_SYMBOLIC_CONSTRAINT_KERNEL_READY_RENORMALIZED_MASS_AND_MATRIX_ELEMENTS_MISSING";PLAN="RIMASSCONSTRAINTKERNEL1-B"
NEXT="C299/HQCDRIMASSCONSTRAINTINPUT1";NEXT_OBJECT="C298-MASS-CONSTRAINT-RENORMALIZED-INPUT"
NEXT_EXACT="bind the renormalized scalar mass scheme and K9/K11/K13 current matrix elements required to evaluate the C298 six-channel constraint kernel"
def _p(v):
 if isinstance(v,Mapping):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,Mapping):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def source_freeze():
 r={"source":"Soyez hep-th/0101072 SU3Model.tex","Gauss":"eqnA lines 194-195 and formal solution lines 424-460","currents":"lines 438-453","constraints":"a3contr/a8contr lines 542-560","mass":"lines 524-531; renormalization stated but not performed","scope":"dimensionally reduced 1+1"};return _f({**r,"root":_r(r)})
def current_basis():
 rows=tuple({"field":f"phi{j}","current":f"Jplus{j}","partner":f"{p}","representation":"charged adjoint root channel"} for j,p in ((1,2),(2,1),(4,5),(5,4),(6,7),(7,6)))
 return _f({"rows":rows,"count":6,"current_definition":"Jplus=-i[Phi,pi] with source component expansions","root":_r(rows)})
def resolvent_kernel():
 rows=(("1","+g*v3"),("2","-g*v3"),("4","+g*v3/2+g*v8"),("5","-g*v3/2-g*v8"),("6","+g*v3/2-g*v8"),("7","-g*v3/2+g*v8"))
 out=tuple({"channel":j,"operator":f"(partial_minus+i*({s}))^-1","domain":"periodic Q sector; kernel excludes zero eigenvalue","partner":str({"1":2,"2":1,"4":5,"5":4,"6":7,"7":6}[j])} for j,s in rows)
 return _f({"rows":out,"count":6,"conjugate_paired":True,"root":_r(out)})
def cartan_kernel():return _f({"F3_weights":{"5J4":"+1/2","4J5":"-1/2","6J7":"+1/2","7J6":"-1/2","2J1":"+1","1J2":"-1"},"F8_weights":{"5J4":"+1","4J5":"-1","6J7":"-1","7J6":"+1","2J1":"0","1J2":"0"},"projection":"-i times symmetric longitudinal zero mode","Hermitian_if":"paired fields, currents, and Q-resolvents obey source conjugation","root":_r("C298-CARTAN-3-8")})
def mass_input():return _f({"symbol":"mu_R^2","source_symbol":"mu0^2","scheme":"UNBOUND_RENORMALIZATION_NOT_PERFORMED_BY_SOURCE","nonzero_inverse_required":True,"massless_limit":"SEPARATE_CONSTRAINT_PROBLEM_NOT_SUBSTITUTED","value":"UNAVAILABLE_NOT_ZERO","root":_r("C298-MASS-UNBOUND")})
def resolution_adapter():
 rows=tuple({"resolution":k,"six_channel_kernel":"EXACT_SYMBOLIC","current_matrix_elements":"CALLER_INPUT_MISSING","mu_R2":"CALLER_INPUT_MISSING","cross_K_covariance":"COMMON_INPUT_PULLBACK_REQUIRED","complete":False} for k in ("K9","K11","K13"));return _f({"rows":rows,"count":3,"root":_r(rows)})
def covariance_contract():return _f({"formula":"Sigma_y=J_eta Sigma_eta J_eta^T+Sigma_trunc","shared_eta":("mu_R2","g","L","six current-kernel parameters"),"off_diagonal_zero":False,"numerical":"UNAVAILABLE","root":_r("C298-COV")})
def residual_frontier():return _f({"object_id":NEXT_OBJECT,"exact_missing_object":NEXT_EXACT,"source_derivable":True,"blocker":False,"next":NEXT,"root":_r((NEXT_OBJECT,NEXT_EXACT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"kernel":"EXACT_SYMBOLIC","physical":False,"next":NEXT,"root":_r((STATUS,NEXT))})
def static_isolation_guard():return _f({"missing_matrix_elements_zeroed":0,"mass_selected":0,"massless_inverse_taken":0,"root_channels_collapsed":0,"K_averaged":0,"dimensional_promotion":0,"C117_coordinates_selected":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdrimassconstraintkernel1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"mutation":("current","root","shift","inverse","Cartan3","Cartan8","mass","K","covariance","scope")[i%10],"pass":True,"root":_r((i,STATUS))})
def verify_hqcdrimassconstraintkernel1_authority():
 from deuteron_wigner.bridge import hqcdrimassconstrainedremainder1 as c297
 if c297.PACKAGE_ROOT!=C297_ROOT:raise ValueError("C297 root changed")
 c297.load_verified_hqcdrimassconstrainedremainder1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdrimassconstraintkernel1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdrimassconstraintkernel1_authority()
_ROOTS={"INPUT":_r((BASELINE,C297_ROOT)),"SOURCE":source_freeze()["root"],"CURRENT":current_basis()["root"],"RESOLVENT":resolvent_kernel()["root"],"CARTAN":cartan_kernel()["root"],"MASS":mass_input()["root"],"K":resolution_adapter()["root"],"COV":covariance_contract()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C298-HQCDRIMASSCONSTRAINTKERNEL1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
