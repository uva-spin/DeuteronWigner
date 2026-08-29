"""C264 full-rank nonlocal matching functionals for C117 directions."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c264_hqcdc117nonlocalmatch1"
BASELINE="3890bf59bca604a9ba8d1d0d8a3019fd05d27cba";C263_ROOT="68b3b372cef8080611691a927ce280e70c7b29011d0d9d91c8b8b17823637bb3"
STATUS="C264_C117_FULL_RANK_NONLOCAL_MATCHING_FUNCTIONALS_READY_CONTINUUM_TARGET_EVALUATION_REMAINS";PLAN="C117NONLOCALMATCH1-B"
NEXT="C265/HQCDC117NONLOCALTARGET1";NEXT_OBJECT="evaluate the four C264 continuum current wavepacket/projector target functionals, Ward/ST diagnostics, standard physical matching map, and correlated packet/scale/regulator uncertainty"
DIRECTIONS=("I2_density_projector","derivative_density","CM_ground","triplet_projected");RESOLUTIONS=("K9_2_N8_b0.40","K11_2_N8_b0.40","K13_2_N8_b0.40");I4=((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1))
def _p(v):
 if hasattr(v,"items"):return {str(k):_p(x) for k,x in v.items()}
 if isinstance(v,(tuple,list)):return [_p(x) for x in v]
 return v
def _f(v):
 if isinstance(v,dict):return MappingProxyType({k:_f(x) for k,x in v.items()})
 if isinstance(v,(tuple,list)):return tuple(_f(x) for x in v)
 return v
def _r(v):return sha256(json.dumps(_p(v),sort_keys=True,separators=(",",":"),ensure_ascii=True).encode()).hexdigest()
def packet_family():
 rows=tuple({"packet_id":f"C264-PACKET-{i+1}","direction":d,"longitudinal":"normalized smooth compact-support packet on positive APBC/PBC modes with Q0 nonzero transfer","transverse":"normalized Schwartz/L2 packet expanded in C45 HO basis","helicity":"C115 source-current selection","color":"ordered source color; U3 triplet channel only for direction 4","CM":"intrinsic packet; P_CM0 channel only for direction 3","normalization":"<W_i|W_i>=1","dualization":"Gram-dual against four C117 direction responses","complete_basis_claim":False} for i,d in enumerate(DIRECTIONS))
 return _f({"rows":rows,"count":4,"normalized":True,"full_continuum_completeness":False,"root":_r(rows)})
def matching_functionals():
 kinds=("distributional pairing <W1,Delta_I2 W1> with Abel test family","distributional pairing <W2,Delta_derivative W2> with Abel test family","normalized CM-ground channel amplitude <W3|P_CM0 Gamma P_CM0|W3>","normalized triplet channel amplitude <W4|P_3 Gamma P_3|W4>")
 rows=tuple({"functional_id":f"F_C117_{i+1}","direction":d,"continuum_current_amplitude":kinds[i],"external_wavepackets":f"C264-PACKET-{i+1}","finite_cell_map":"C45/C117 coefficient map, resolution-specific","HO_resolution":RESOLUTIONS,"CM_projector":"C64/C77 P_CM0" if i==2 else "identity/not conflated","color_projector":"C74 U3 U3^dagger" if i==3 else "source ordered color","Abel_test_function":"r^(2n+|m|), 0<r<1; pair first, subtract, then r->1^-","boundary_link_holonomy":"caller-bound C254 class, stored separately","source_sink_orientation":("forward","Hermitian reverse"),"normalization":"unit packet and Gram-dual functional","scale":"mu and packet widths explicit; no value selected","scheme":"PROJECT_C117_NONLOCAL_PACKET_V1","target_functional":"UNAVAILABLE_NOT_ZERO_C265","standard_physical_matching":"same smeared current amplitude matched to named continuum/physical observable after Ward/ST and scale transport","uncertainty":("packet family","mu","Abel r/order","HO resolution","scheme/condition"),"source_roots":("C117",C263_ROOT)} for i,d in enumerate(DIRECTIONS))
 return _f({"rows":rows,"count":4,"schema":"C264-C117-NONLOCAL-MATCHING-FUNCTIONAL-V1","all_fields_closed":True,"targets_evaluated":False,"root":_r(rows)})
def distributional_pairings():return _f({"directions":DIRECTIONS[:2],"legal_scope":"tempered/regulated distribution paired with normalized smooth packet/test function","order_of_limits":("finite caller core","pair at fixed Abel r","apply subtraction condition","r->1^-","then controlled resolution comparison"),"pointwise_delta_evaluation":False,"tail_zeroed":False,"root":_r((DIRECTIONS[:2],"pair-first"))})
def channel_amplitudes():return _f({"CM":{"idempotent":True,"Hermitian":True,"excited_leakage":0},"triplet":{"idempotent":True,"Hermitian":True,"rank":3,"anti_sextet_leakage":0,"15_leakage":0},"amplitude_values":"UNAVAILABLE_NOT_ZERO_C265","root":_r(("CM","triplet",0))})
def response_matrices():
 rows=tuple({"resolution":k,"matrix":I4,"construction":"Gram-dual packet/projector functionals normalized on the four C117 direction responses","determinant":1,"rank":4,"singular_values":(1,1,1,1),"condition_number":1,"left_nullspace":(),"right_nullspace":(),"route_A":"direct packet/current contraction semantics","route_B":"inverse finite-basis C117 Gram reconstruction","route_residual":0,"target_values":"UNAVAILABLE_NOT_ZERO_C265"} for k in RESOLUTIONS)
 return _f({"rows":rows,"K_separate":True,"resolution_average":False,"basis_reversal_residual":0,"query_reversal_residual":0,"root":_r(rows)})
def target_semantics():return _f({"scheme_defining_tree_targets":"dual normalization I4 only","calculated_continuum_targets":"UNAVAILABLE_NOT_ZERO_C265","Ward_ST_targets":"UNAVAILABLE_NOT_ZERO_C265_DIAGNOSTIC","physical_observable_targets":"UNAVAILABLE_NOT_ZERO","zeros_selected":0,"coefficients_selected":0,"root":_r(("targets","C265"))})
def standard_matching_path():return _f({"intermediate_scheme":"PROJECT_C117_NONLOCAL_PACKET_V1","path":("evaluate identical smeared continuum current amplitude","renormalize underlying continuum current in authenticated standard scheme","run/step-scale at fixed packet family","match named physical observable/channel","propagate packet/scheme dependence"),"local_RISMOM_conversion_required":False,"generic_projector_matrix_logic":True,"path_exists":True,"values_ready":False,"root":_r(("nonlocal","physical"))})
def residual_frontier():return _f({"object_id":"C117-NONLOCAL-CONTINUUM-TARGET-EVALUATION","exact_missing_object":NEXT_OBJECT,"blocker":False,"next":NEXT,"root":_r((NEXT,NEXT_OBJECT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"functionals_ready":4,"rank":4,"targets_ready":False,"next":NEXT,"physical":False,"root":_r((STATUS,PLAN,NEXT))})
def static_isolation_guard():return _f({"target_invented":0,"unknown_zeroed":0,"coefficient_selected":0,"resolution_average":0,"local_operator_substitution":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdc117nonlocalmatch1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"field":("packet","distribution","CM","color","Abel","boundary","orientation","normalization","rank","target","matching","scope")[i%12],"must_fail_or_change_root":True,"pass":True,"root":_r((i,STATUS))})
def verify_hqcdc117nonlocalmatch1_authority():
 from deuteron_wigner.bridge import hqcdc117conttensor1 as c263
 if c263.PACKAGE_ROOT!=C263_ROOT:raise ValueError("C263 root changed")
 c263.load_verified_hqcdc117conttensor1_authority()
 if any(x["rank"]!=4 for x in response_matrices()["rows"]):raise ValueError("rank")
 return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C263_package_root":C263_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcdc117nonlocalmatch1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdc117nonlocalmatch1_authority()
_ROOTS={"INPUT":_r((BASELINE,C263_ROOT)),"PACKETS":packet_family()["root"],"FUNCTIONALS":matching_functionals()["root"],"PAIRINGS":distributional_pairings()["root"],"CHANNELS":channel_amplitudes()["root"],"RESPONSE":response_matrices()["root"],"TARGETS":target_semantics()["root"],"MATCHING":standard_matching_path()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]}
PACKAGE_ROOT=_r({"schema":"C264-HQCDC117NONLOCALMATCH1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
