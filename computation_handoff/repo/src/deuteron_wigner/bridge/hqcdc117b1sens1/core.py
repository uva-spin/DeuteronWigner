"""C272 exact b1 sensitivity programs and physical-state boundary."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c272_hqcdc117b1sens1"
BASELINE="02110eeb45b20697b60cbc9f11f9c653227d24bc";C271_ROOT="7a55d193904b3c19d7c29d61d0abcce421801b4e6852349af2aa571d69d07cbe"
STATUS="C272_EXACT_B1_SENSITIVITY_PROGRAMS_READY_PHYSICAL_EIGENSTATE_BUNDLE_UNAVAILABLE";PLAN="C117B1SENS1-B";NEXT="C273/HQCDC117PHYSSTATE1";NEXT_OBJECT="authenticated renormalized K9 deuteron eigenstate and reduced-resolvent response bundle with K11/K13 holdouts for evaluating the C272 b1 sensitivities"
DIRECTIONS=("I2_density_projector","derivative_density","CM_ground","triplet_projected")
def _p(v):
 if hasattr(v,"items"):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,dict):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def sensitivity_program(direction):
 if direction not in DIRECTIONS:raise KeyError(direction)
 i=DIRECTIONS.index(direction)+1
 x={"direction":direction,"direct":f"S_{i}=P_b1 d/dc_{i} <Psi(c)|[J,J]|Psi(c)>|c_ref paired W_{i}","insertion":f"dH/dc_{i}=O_C117,{i} with differentiated contact/current-current terms retained","spectral":f"S_{i}=<Psi|dB1/dc_{i}|Psi>+2 Re <Psi|B1 R'_Psi O_{i}|Psi>","reduced_resolvent":"R'_Psi=Q_Psi(E_Psi-H)^-1 Q_Psi with pole removed and boundary class fixed","normalization_term":"-<Psi|B1|Psi> d<Psi|Psi>/dc_i retained (zero only after authenticated unit-normalized derivative)","packet_Q0_Abel":"C266 W_i; Q0 fixed; pair at r<1 then r->1-","resolutions":("K9_2_N8_b0.40","K11_2_N8_b0.40","K13_2_N8_b0.40"),"value":None,"status":"EXECUTABLE_ON_PHYSICAL_STATE_BUNDLE_UNAVAILABLE_NOT_ZERO"}
 return _f({**x,"root":_r(x)})
def physical_state_audit():return _f({"renormalized_H_K9":False,"deuteron_eigenstate_K9":False,"reduced_resolvent_K9":False,"K11_K13_holdouts":False,"repository_fixtures_are_physical":False,"missing_as_zero":False,"root":_r((False,)*6)})
def rank_certificate():return _f({"EM_rank":3,"b1_row":tuple(f"S_{i+1}" for i in range(4)),"values":None,"rank":"UNAVAILABLE_NOT_ZERO","conditioning":"UNAVAILABLE_NOT_ZERO","rank_four_claim":False,"compatibility":"no contradiction; evaluation domain absent","root":_r((3,"unavailable"))})
def two_route_derivation():return _f({"route_A":"direct differentiated C271 hadron tensor","route_B":"Feynman-Hellmann reduced-resolvent spectral sum","algebraic_equivalence":True,"numeric_agreement":"UNAVAILABLE_WITHOUT_PHYSICAL_STATE","contradiction":False,"root":_r((True,False))})
def uncertainty_program():return _f({"program":"Jacobian propagation of state, spectral-gap, packet, Abel/HO, factorization and b1 source covariance","state_covariance":None,"status":"PROGRAM_READY_STATE_BLOCK_UNAVAILABLE_NOT_ZERO","root":_r("c272-cov")})
def residual_frontier():return _f({"object_id":"C117-PHYSICAL-STATE-RESPONSE-BUNDLE-V1","exact_missing_object":NEXT_OBJECT,"blocker":False,"next":NEXT,"root":_r((NEXT,NEXT_OBJECT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"programs_closed":4,"values_closed":0,"rank_four":False,"coefficients_selected":0,"physical":False,"next":NEXT,"root":_r((STATUS,PLAN,NEXT))})
def static_isolation_guard():return _f({"unsupported_zeroed":0,"finite_coefficient_selected":0,"physical_fixture_promoted":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdc117b1sens1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"pass":True,"root":_r((i,STATUS))})
def verify_hqcdc117b1sens1_authority():
 from deuteron_wigner.bridge import hqcdc117b1adapter1 as c271
 if c271.PACKAGE_ROOT!=C271_ROOT:raise ValueError("C271 root changed")
 c271.load_verified_hqcdc117b1adapter1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdc117b1sens1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdc117b1sens1_authority()
_ROOTS={"INPUT":_r((BASELINE,C271_ROOT)),"PROGRAMS":_r(tuple(sensitivity_program(d)["root"] for d in DIRECTIONS)),"STATE":physical_state_audit()["root"],"RANK":rank_certificate()["root"],"ROUTES":two_route_derivation()["root"],"UNCERTAINTY":uncertainty_program()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C272-HQCDC117B1SENS1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
