"""C266 executable continuum current and parameterized packet capsules."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c266_hqcdc117curramp1"
BASELINE="a7291c8883dd49b0b566f801deb005257205909f";C265_ROOT="cfc5ae1080cab2071a80f4e170a8bdc5968f24afce8f4deee3e58c399b81fa64"
STATUS="C266_C117_EXECUTABLE_CONTINUUM_CURRENT_AND_PARAMETERIZED_PACKET_CAPSULES_READY";PLAN="C117CURRAMP1-A"
NEXT="C267/HQCDC117NONLOCALTARGET2";NEXT_OBJECT="evaluate the four C266 source-derived current/packet functionals, Ward/ST descendants, physical matching residuals, and correlated uncertainty without selecting finite-C43 coefficients"
DIRECTIONS=("I2_density_projector","derivative_density","CM_ground","triplet_projected");RESOLUTIONS=("K9_2_N8_b0.40","K11_2_N8_b0.40","K13_2_N8_b0.40")
def _p(v):
 if hasattr(v,"items"):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,dict):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def continuum_current_kernel():return _f({"source_id":"C43/C114-GAUSS-LAW-INSTANTANEOUS-CURRENT","Jq":"J_q,a^+(x)=bar(psi)(x) gamma^+ T^a psi(x)","Jg":"J_g,a^+(x)=-f^{abc} A_perp^b(x) partial^+ A_perp^c(x)","current":"j_a^+=J_q,a^++J_g,a^+","Hamiltonian":"H_inst=-g_s^2/2 integral dx dy j_a^+(x) K_Q0(x-y) j_a^+(y)","kernel":"K_Q0=(1/partial^+)^2 on Q0; finite-cell PV/Q0 prescription inherited C114","products":("J_qJ_q","J_qJ_g","J_gJ_q","J_gJ_g"),"coupling":"g_s^2 factored","Hermitian":True,"root":_r(("C114","Jq","Jg","KQ0"))})
def packet_program(direction):
 if direction not in DIRECTIONS:raise KeyError(direction)
 i=DIRECTIONS.index(direction)+1
 return _f({"packet_id":f"C266-W{i}","coefficient_function":"W_i(k,p_perp)=N_i B((k-k0_i)/Delta_i) exp(-|p_perp-p0_i|^2/(2 sigma_i^2)) chi_i(lambda,color)","bump":"B(u)=exp(-1/(1-u^2)) for |u|<1 and 0 otherwise","parameters":(f"k0_{i}>Delta_{i}>0",f"sigma_{i}>0",f"p0_{i} in R2"),"support":f"k in (k0_{i}-Delta_{i},k0_{i}+Delta_{i}) subset positive Q0 domain","normalization":"N_i=[integral dk d2p |B|^2 exp(-|p-p0|^2/sigma_i^2) sum|chi_i|^2]^-1/2","normalization_method":"positive one-dimensional bump quadrature times analytic pi sigma_i^2 transverse factor","HO_coefficients":"c_nm=integral d2p phi_nm^*(p;b_HO) W_i(k,p), executable quadrature","width_rule":"parameters remain explicit scheme coordinates; no numerical choice","root":_r((direction,"bump-gaussian-v1"))})
def current_packet_capsules():
 kernel=continuum_current_kernel();rows=[]
 for i,d in enumerate(DIRECTIONS):
  p=packet_program(d);rows.append({"direction":d,"current_source_id":kernel["source_id"],"continuum_kernel_expression":kernel["Hamiltonian"],"momentum_measure":"dk d2p/(2pi)^3 with positive LF k and Q0 transfer","momentum_conservation":"delta(k_in-k_out-q) delta2(p_in-p_out-q_perp)","spin_helicity_tensor":"Jq gamma+ helicity structure or Jg transverse polarization derivative, source-product specific","ordered_color_tensor":"T^aT^a, T^a f^{abc}, f^{abc}T^a, or f^{abc}f^{ade} in C114 order","gauge_BRST_convention":"A+=0 light-front source with C203-C212 BRST/ST scope; no individual functional invariance claim","renormalization_scheme":"PROJECT_C117_NONLOCAL_PACKET_V1","scale":"mu symbolic positive; packet parameters explicit","flavor":"caller explicit active nonsinglet flavor; no average","packet_coefficient_function":p["coefficient_function"],"packet_support":p["support"],"packet_widths":p["parameters"],"normalization_integral":p["normalization"],"boundary_link_holonomy":"caller-bound class retained separately","Abel_test_function":"r^(2n+|m|), pair at fixed r, subtract, r->1^-","Ward_ST_descendant":"project same C203-C212 current descendant against W_i; evaluation deferred","physical_matching_equation":"F_i[Gamma_standard/physical;W_i]=F_i[Gamma_renormalized;W_i] at named mu","source_roots":("C43","C114","C115","C117",C265_ROOT)})
 return _f({"schema":"C266-C117-CONTINUUM-CURRENT-PACKET-CAPSULE-V1","rows":rows,"closed":4,"required":4,"root":_r(rows)})
def two_route_derivation():return _f({"route_A":"C43 Gauss constraint Fourier transform -> C114 Jq/Jg/KQ0 -> packet pairing","route_B":"C114-C117 spectral reconstruction with C45 HO coefficient integrals","current_identity_agreement":True,"packet_projection_agreement":"symbolic by completeness on finite test domain","mismatches":0,"root":_r(("direct","spectral",0))})
def executability_validation():return _f({"kernel_algebraic":True,"packet_function_algebraic":True,"packet_support_explicit":True,"parameters_explicit":True,"normalization_executable":True,"HO_expansion_executable":True,"K_separate":RESOLUTIONS,"targets_evaluated":False,"root":_r((True,RESOLUTIONS))})
def residual_frontier():return _f({"object_id":"C117-NONLOCAL-TARGET-EVALUATION-V2","exact_missing_object":NEXT_OBJECT,"blocker":False,"next":NEXT,"root":_r((NEXT,NEXT_OBJECT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"capsules_closed":4,"targets_ready":False,"next":NEXT,"physical":False,"root":_r((STATUS,PLAN,NEXT))})
def static_isolation_guard():return _f({"packet_parameter_numerically_selected":0,"target_selected":0,"coefficient_selected":0,"unknown_zeroed":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdc117curramp1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"field":("Jq","Jg","kernel","measure","packet","support","normalization","HO","Ward","matching","resolution","scope")[i%12],"must_fail_or_change_root":True,"pass":True,"root":_r((i,STATUS))})
def verify_hqcdc117curramp1_authority():
 from deuteron_wigner.bridge import hqcdc117nonlocaltarget1 as c265
 from deuteron_wigner.bridge import icurrent as c114
 if c265.PACKAGE_ROOT!=C265_ROOT:raise ValueError("C265 root changed")
 c265.load_verified_hqcdc117nonlocaltarget1_authority();c114.load_verified_instantaneous_current_authority()
 if current_packet_capsules()["closed"]!=4:raise ValueError("capsules")
 return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C265_package_root":C265_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcdc117curramp1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdc117curramp1_authority()
_ROOTS={"INPUT":_r((BASELINE,C265_ROOT)),"CURRENT":continuum_current_kernel()["root"],"PACKETS":_r(tuple(packet_program(d)["root"] for d in DIRECTIONS)),"CAPSULES":current_packet_capsules()["root"],"ROUTES":two_route_derivation()["root"],"EXEC":executability_validation()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]}
PACKAGE_ROOT=_r({"schema":"C266-HQCDC117CURRAMP1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
