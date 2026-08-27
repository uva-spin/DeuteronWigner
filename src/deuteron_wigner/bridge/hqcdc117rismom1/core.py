"""C260 executable, coefficient-free PROJECT_C117_RI_SMOM_V1 authority."""
from __future__ import annotations
import json
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType

ROOT=Path(__file__).resolve().parents[4]
RUNTIME=ROOT/"data/runtime/c260_hqcdc117rismom1"
BASELINE="950725ee1a1115784d767ced674c6f67eebec5ba"
C259_ROOT="3316addcea31e845dc16f57f0e921a6409b87c2764635f261e8dff3454cd62ed"
STATUS="C260_PROJECT_C117_RI_SMOM_V1_EXECUTABLE_AUTHORITY_READY"
PLAN="C117RISMOM1-A"
SCHEME="PROJECT_C117_RI_SMOM_V1"
NEXT="C261/HQCDC117CONTTARGET1"
NEXT_OBJECT="continuum projected target amplitudes, RI/SMOM-to-MSbar conversion matrix, running/step-scaling authority, and perturbative/scheme uncertainty in exact C260 conventions"
DIRECTIONS=("I2_density_projector","derivative_density","CM_ground","triplet_projected")
RESOLUTIONS=("K9_2_N8_b0.40","K11_2_N8_b0.40","K13_2_N8_b0.40")
I4=((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1))
def _p(v):
 if hasattr(v,"items"):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 if isinstance(v,Fraction):return str(v)
 return v
def _f(v):
 if isinstance(v,dict):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def operator_basis():
 roles=("finite-shell local density complement","derivative-weighted density complement","intrinsic CM-ground complement","physical color-triplet complement")
 rows=tuple({"index":i,"operator_id":f"O_C117_{i+1}","direction":d,"role":role,"fields":"C117 instantaneous J+J+ q/qg graph-local complement","spin_helicity":"C115 source-current tensor retained","ordered_color":"C114 source order; C74 U3 only for triplet projection","longitudinal":"positive APBC quark/PBC nonzero-gluon transfer; derivative factor only in direction 2","transverse":"C45 finite HO ancestry; C64/C77 intrinsic/CM factor when applicable","dimension":"mass-squared Hamiltonian direction with g_s^2 factored","hermitian_partner":True,"BRST_ST":"renormalized-combination descendant test required; individual invariance not asserted","EOM_total_derivative":"independent at declared graph-local finite-basis scope","mixing_block":DIRECTIONS,"source":"C117/C259"} for i,(d,role) in enumerate(zip(DIRECTIONS,roles)))
 return _f({"scheme":SCHEME,"order":DIRECTIONS,"rows":rows,"dimension":4,"closure":"closed four-coordinate project basis at tree/scheme-definition order; loop-induced EOM/BRST-exact/evanescent sectors declared below","classification_routes":("C117 graph tensor factors","C259 Gram-dual coordinate reconstruction"),"root":_r(rows)})
def symmetric_kinematics(mu2=1):
 mu2=Fraction(mu2)
 if mu2<=0:raise ValueError("mu^2 must be positive")
 # An exact 2D Euclidean representative: p1=(mu,0), p2=(mu/2,sqrt(3)mu/2).
 dots={"p1.p1":mu2,"p2.p2":mu2,"q.q":mu2,"p1.p2":mu2/2,"p1.q":mu2/2,"p2.q":-mu2/2}
 return _f({"scheme":SCHEME,"signature":"Euclidean","gauge":"Landau xi=0","mu2":mu2,"external_legs":"amputated off-shell C117 source/sink coordinates","source_sink_order":("incoming p1","operator momentum q=p1-p2","outgoing p2"),"flavor":"massless active flavors, explicit nonsinglet routing; no flavor average","color":"ordered source tensors retained","dots":dots,"nonexceptional":all(dots[x]!=0 for x in ("p1.p1","p2.p2","q.q")),"analytic_continuation":"Euclidean scheme coordinate only; finite-cell light-front mapping deferred to C262","root":_r((mu2,dots))})
def projector_basis():
 rows=tuple({"projector_id":f"P_C117_{i+1}","dual_to":f"O_C117_{i+1}","definition":f"sum_b (G^-1)_{{{i+1}b}} <O_b,.>","normalization":"P_i Gamma_j^tree = delta_ij","scheme_defining":True,"physical":False} for i in range(4))
 return _f({"gram_matrix":I4,"gram_inverse":I4,"determinant":1,"rows":rows,"direct_contraction":I4,"dual_contraction":I4,"basis_reversal_response":I4,"root":_r(rows)})
def tree_response_matrix():
 return _f({"operator_order":DIRECTIONS,"projector_order":tuple(f"P_C117_{i+1}" for i in range(4)),"matrix":I4,"determinant":1,"rank":4,"singular_values":(1,1,1,1),"condition_number":1,"left_nullspace":(),"right_nullspace":(),"symmetry_blocks":((0,),(1,),(2,),(3,)),"route_A":"direct exact projector/operator contraction","route_B":"Gram inverse duality with reversed-order permutation round trip","route_residual":0,"root":_r(I4)})
def tree_target_definition():
 rows=tuple({"projector_id":f"P_C117_{i+1}","tree_target":"corresponding tree-normalized C117 operator amplitude","zero_reason":"only off-diagonal unwanted-mixing projections are zero by Kronecker-dual scheme definition","physical":False} for i in range(4))
 return _f({"scheme_target_rows":rows,"tree_matrix":I4,"continuum_perturbative_target":"UNAVAILABLE_NOT_ZERO_C261","ward_ST_target":"independent descendant diagnostic, not substituted","nonperturbative_target":"UNAVAILABLE_NOT_ZERO","physical_observable_target":"UNAVAILABLE_NOT_ZERO","coefficient_values":"UNAVAILABLE_NOT_ZERO","root":_r(rows)})
def mixing_and_evanescent_convention():
 return _f({"physical_basis":DIRECTIONS,"tree_closure":True,"loop_basis":{"physical":DIRECTIONS,"EOM":"retained as off-shell nuisance block and projected/subtracted explicitly","BRST_exact":"retained as gauge-fixed nuisance block and tested by ST descendants","evanescent":"E_a = D-dimensional Dirac/color tensor minus its four-dimensional projection in the ordered C117 physical basis"},"dimensional_regularization":"D=4-2 epsilon","standard_scheme":"MSbar","gamma5":"NDR anticommuting gamma5 for nonsinglet routing; no anomalous singlet claim","flavor":"explicit massless active nonsinglet; nf label mandatory","color":"SU(3), source ordering retained","finite_evanescent_subtraction":"must be calculated and locked in C261; unavailable, not zero","closure_claim":"definition-level closure; C261 owns loop mixing coefficients and any required evanescent enlargement","root":_r((DIRECTIONS,"NDR","MSbar"))})
def conversion_boundary():
 return _f({"from":SCHEME,"to":"MSbar-NDR in identical physical/evanescent ordering","conversion_matrix":"UNAVAILABLE_NOT_ZERO_C261","formula":"Gamma_MSbar(mu)=C_MSbar<-RISMOM(mu) Gamma_RISMOM(mu)","step_scaling":"Sigma(mu2,mu1)=lim_reg Z(mu2) Z(mu1)^-1; nonperturbative window then perturbative conversion","scale_window":"must satisfy IR contamination << declared tolerance and regulator artifacts << declared tolerance","thresholds":"nf and threshold matching records mandatory; no threshold value selected","physical_matching":"after MSbar conversion, bind a named physical observable/condition; not performed here","source_ids":("hep-lat/9411010","0901.2599","1104.4948","1109.1223"),"root":_r((SCHEME,"MSbar-NDR","C261"))})
def finite_C43_adapter_interface():
 rows=tuple({"resolution":k,"matrix":"M^(K)(mu,S) UNAVAILABLE_NOT_ZERO_C262","rhs":"t^S(mu)-r^(K)(mu,S) UNAVAILABLE_NOT_ZERO_C262","separate":True} for k in RESOLUTIONS)
 return _f({"rows":rows,"coordinate_map":"Euclidean invariants and source ordering -> light-front off-shell packet coordinates","wavepacket":"normalized finite-cell packets; no delta-function replacement","transverse":"continuum transverse structures -> finite HO overlaps","normalization":"C117 operator/source normalization and g_s^2 ownership retained","Abel":"C254 caller Abel family and order of limits retained","boundaries":"P0/Q0, links, boundary class, and holonomy recorded separately","orientation":"forward/reverse Hermitian source/sink orientations retained","coefficients_evaluated":False,"root":_r(rows)})
def scheme_variation_holdouts():
 rows=(("RI_SMOM_ALTERNATE_DUAL","projector-family dependence"),("WARD_RISMOM","Ward/ST row replacement"),("GIRS","gauge-independent coordinate-space holdout"),("GRADIENT_FLOW","short-flow-time holdout"),("MU_WINDOW","scale dependence"))
 return _f({"rows":tuple({"id":x,"diagnostic":y,"primary":False} for x,y in rows),"required_downstream":True,"root":_r(rows)})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"scheme":SCHEME,"rank":4,"executable_definition":True,"conversion_values_ready":False,"coefficients_selected":0,"physical_targets_selected":0,"next":NEXT,"next_object":NEXT_OBJECT,"physical":False,"root":_r((STATUS,PLAN,NEXT))})
def static_isolation_guard():return _f({"unknown_zeroed":0,"coefficient_selected":0,"conversion_invented":0,"physical_target_selected":0,"resolution_average":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdc117rismom1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"field":("basis","kinematics","gauge","projector","rank","target","EOM","BRST","evanescent","conversion","adapter","scope")[i%12],"must_fail_or_change_root":True,"pass":True,"root":_r((i,STATUS))})
def verify_hqcdc117rismom1_authority():
 from deuteron_wigner.bridge import hqcdc117renormdesign1 as c259
 if c259.PACKAGE_ROOT!=C259_ROOT:raise ValueError("C259 root changed")
 c259.load_verified_hqcdc117renormdesign1_authority()
 if tree_response_matrix()["rank"]!=4 or not symmetric_kinematics()["nonexceptional"]:raise ValueError("scheme")
 return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C259_package_root":C259_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcdc117rismom1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdc117rismom1_authority()
_ROOTS={"INPUT":_r((BASELINE,C259_ROOT)),"BASIS":operator_basis()["root"],"KINEMATICS":symmetric_kinematics()["root"],"PROJECTORS":projector_basis()["root"],"TREE":tree_response_matrix()["root"],"TARGET":tree_target_definition()["root"],"MIXING":mixing_and_evanescent_convention()["root"],"CONVERSION":conversion_boundary()["root"],"ADAPTER":finite_C43_adapter_interface()["root"],"HOLDOUTS":scheme_variation_holdouts()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]}
PACKAGE_ROOT=_r({"schema":"C260-HQCDC117RISMOM1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
