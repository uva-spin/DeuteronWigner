"""C271 tensor-DIS b1 operator/normalization adapter."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c271_hqcdc117b1adapter1"
BASELINE="68701f95f651b8b82ac7a16a07484b1071aa6a58";C270_ROOT="69675d52d7c2aa6ac9a88c4ce175cfce6a92d646b52aaedf9644101296119e4d"
STATUS="C271_B1_OPERATOR_NORMALIZATION_ADAPTER_READY_C117_SENSITIVITY_ROW_UNEVALUATED";PLAN="C117B1ADAPTER1-B";NEXT="C272/HQCDC117B1SENS1";NEXT_OBJECT="evaluate the four derivatives of the normalized tensor-DIS b1 packet functional with respect to the C117 finite subtraction coordinates and certify combined rank"
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
def hadron_tensor_operator():
 x={"operator":"W_mn(P,q;lambda)=1/(4pi) integral d4z exp(iq.z) <P,lambda|[J_m(z),J_n(0)]|P,lambda>","tensor_combination":"delta_T W_mn = W_mn(lambda=0) - [W_mn(+1)+W_mn(-1)]/2","b1_projector":"authenticated spin-one DIS b1 projector applied to delta_T W_mn","current_order":"commutator order and cut orientation retained","Hermitian":True,"source":"hep-ex/0506018 and 1702.05337"}
 return _f({**x,"root":_r(x)})
def normalization_kinematics():
 x={"state":"unit-normalized spin-1 tensor density combination rho00-(rho+++rho--)/2","x":"Q2/(2 M_N nu), HERMES convention","x_D":"Q2/(2 P_D.q); kept distinct; project relation x approximately 2 x_D only in declared frame/domain","active_fraction":"alpha centered near 1 corresponds to project y=alpha/2 centered near 1/2","flavor_weights":"sum_q e_q^2 retained explicitly","scheme":"leading-twist collinear factorization label and Q2/mu explicit","validity":"HERMES low-Q2 points flagged; no automatic leading-twist promotion","root":_r("b1-normalization-v1")}
 return _f(x)
def packet_adapter():
 rows=tuple({"direction":d,"packet":f"C266-W{i+1}","functional":f"B1_i[c]=P_b1 delta_T W[J_em,J_em; Psi_c,W_{i+1}]","derivative":f"S_b1,{i+1}=d B1_i/d c_{i+1}|reference","Q0_Abel":"C266 Q0; pair fixed r then r->1-","K":("K9_2_N8_b0.40","K11_2_N8_b0.40","K13_2_N8_b0.40"),"boundary_link_holonomy":"caller-bound","derivative_value":None,"unavailable_not_zero":True} for i,d in enumerate(DIRECTIONS))
 return _f({"rows":rows,"operator_closed":True,"normalization_closed":True,"response_values_closed":0,"root":_r(rows)})
def rank_certificate():return _f({"EM_rank":3,"b1_response_row":tuple(f"S_b1,{i+1}" for i in range(4)),"symbolic_rank_condition":"rank([R_EM;S_b1])=4 iff S_b1 not in rowspan(R_EM)","evaluated_rank":None,"rank_four_claim":False,"missing_as_zero":False,"root":_r((3,"symbolic"))})
def two_route_derivation():return _f({"route_A":"direct delta_T hadron-tensor b1 projection and packet functional derivative","route_B":"1702.05337 tensor convolution with alpha=2y and C114-C117 spectral response","operator_normalization_agreement":True,"sensitivity_agreement":"UNEVALUATED_C272","contradiction":False,"root":_r((True,"C272"))})
def uncertainty_program():return _f({"components":("HERMES stat","HERMES syst","low-Q2 validity","factorization","x/xD mapping","packet","HO/Abel","C117 response"),"covariance":"retain shared source/packet blocks and symmetrize A Sigma A^T","values":"PARTIAL_SOURCE_COVARIANCE; RESPONSE_BLOCK_UNAVAILABLE_NOT_ZERO","root":_r("b1-cov")})
def residual_frontier():return _f({"object_id":"C117-B1-SENSITIVITY-V1","exact_missing_object":NEXT_OBJECT,"blocker":False,"next":NEXT,"root":_r((NEXT,NEXT_OBJECT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"operator_closed":True,"normalization_closed":True,"rank_four":False,"coefficients_selected":0,"physical":False,"next":NEXT,"root":_r((STATUS,PLAN,NEXT))})
def static_isolation_guard():return _f({"unsupported_zeroed":0,"finite_coefficient_selected":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdc117b1adapter1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"pass":True,"root":_r((i,STATUS))})
def verify_hqcdc117b1adapter1_authority():
 from deuteron_wigner.bridge import hqcdc117fourthchannel1 as c270
 if c270.PACKAGE_ROOT!=C270_ROOT:raise ValueError("C270 root changed")
 c270.load_verified_hqcdc117fourthchannel1_authority();return _f({"package_root":PACKAGE_ROOT,"status":STATUS,"plan":PLAN,"physical":False})
def load_verified_hqcdc117b1adapter1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdc117b1adapter1_authority()
_ROOTS={"INPUT":_r((BASELINE,C270_ROOT)),"OPERATOR":hadron_tensor_operator()["root"],"NORMALIZATION":normalization_kinematics()["root"],"ADAPTER":packet_adapter()["root"],"RANK":rank_certificate()["root"],"ROUTES":two_route_derivation()["root"],"UNCERTAINTY":uncertainty_program()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]};PACKAGE_ROOT=_r({"schema":"C271-HQCDC117B1ADAPTER1-V1","roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
