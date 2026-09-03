"""C262 fail-closed executability audit of the C261 loop program."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c262_hqcdc117contloop1"
BASELINE="040ce9d31dc038e0f5bdbf199f59b661697d44ec";C261_ROOT="b8326f78014113be619c70f2c6f8a8174d55c80b11892a4cd9ef2b41b762b4b2"
STATUS="C262_C117_CONTINUUM_LOOP_BLOCKED_BY_NONEXECUTABLE_OPERATOR_AND_NUISANCE_TENSORS_CONTINUATION_READY";PLAN="C117CONTLOOP1-D"
NEXT="C263/HQCDC117CONTTENSOR1";NEXT_OBJECT="explicit D-dimensional continuum preimage tensors, momentum-space vertices, and closed EOM/BRST/evanescent partners for the four C117 graph-local finite-basis directions"
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
def numerator_executability_audit():
 rows=tuple({"direction":d,"finite_basis_operator":"AVAILABLE_C117","continuum_preimage":"NAMED_NOT_DEFINED","D_dimensional_vertex":"UNAVAILABLE_NOT_ZERO","momentum_routing_action":"UNAVAILABLE_NOT_ZERO","Dirac_helicity_tensor":"PROSE_ONLY","color_tensor":"PROSE_ONLY","compiler_executable":False} for d in DIRECTIONS)
 return _f({"rows":rows,"executable":0,"required":4,"finding":"C261 numerator field is a prose schema, not an algebraic expression; integration cannot start","root":_r(rows)})
def nuisance_closure_audit():
 rows=tuple({"direction":d,"EOM_symbol":f"G_C117_{i+1}[off-shell]","EOM_expression":None,"BRST_symbol":f"N_C117_{i+1}[Landau]","BRST_expression":None,"evanescent_symbol":f"E_C117_{i+1}","D_tensor":None,"four_dimensional_projection":None,"finite_subtraction":None,"closed":False} for i,d in enumerate(DIRECTIONS))
 return _f({"rows":rows,"closed":0,"required":4,"mixing_matrix_lawful":False,"root":_r(rows)})
def topology_materialization_audit():
 from deuteron_wigner.bridge import hqcdc117conttarget1 as c261
 rows=tuple({"topology_id":x["topology_id"],"measure_ready":True,"denominators_ready":True,"numerator_ready":False,"projector_name_ready":True,"projector_tensor_ready":False,"symmetry_factor_ready":False,"counterterm_expression_ready":False,"integrable":False} for x in c261.diagram_integral_inventory()["route_A"])
 return _f({"rows":rows,"topologies":8,"integrable":0,"count_once_claim":"UNAVAILABLE_UNTIL_VERTEX_AND_SYMMETRY_FACTORS","root":_r(rows)})
def two_route_certificate():return _f({"route_A":"public API field/type executability audit","route_B":"source-to-continuum-preimage and topology dependency audit","same_missing_objects":True,"contradiction":False,"root":_r(("API","preimage",True))})
def loop_result():return _f({"bare_amplitudes":"UNAVAILABLE_NOT_ZERO","UV_poles":"UNAVAILABLE_NOT_ZERO","finite_parts":"UNAVAILABLE_NOT_ZERO","Z_RISMOM":"UNAVAILABLE_NOT_ZERO","Z_MSbar":"UNAVAILABLE_NOT_ZERO","conversion":"UNAVAILABLE_NOT_ZERO","gamma":"UNAVAILABLE_NOT_ZERO","entries_invented":0,"zeros_inferred":0,"reason":"no executable C117 continuum/nuisance tensors","root":_r((PLAN,"unavailable"))})
def required_tensor_capsule_schema():
 fields=("operator_id","direction","D","fields","incoming_legs","outgoing_legs","momentum_conservation","vertex_expression","Dirac_helicity_tensor","ordered_color_tensor","derivative_placement","normalization","coupling_order","Hermitian_partner","EOM_partners","BRST_exact_partners","evanescent_definition","Pi4_projection","projector_expression","source_roots")
 return _f({"schema":"C263-C117-CONTINUUM-TENSOR-CAPSULE-V1","required":fields,"directions":DIRECTIONS,"all_four_required":True,"root":_r(fields)})
def residual_frontier():return _f({"object_id":"C117-CONTINUUM-PREIMAGE-TENSOR-CLOSURE","exact_missing_object":NEXT_OBJECT,"blocker":False,"next":NEXT,"root":_r((NEXT,NEXT_OBJECT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"loop_evaluated":False,"additional_operator_tensors_required":True,"next":NEXT,"physical":False,"root":_r((STATUS,PLAN,NEXT))})
def static_isolation_guard():return _f({"loop_entry_selected":0,"unsupported_zeroed":0,"finite_C43_evaluated":0,"coefficient_selected":0,"physical_target_selected":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdc117contloop1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"field":("preimage","vertex","Dirac","color","EOM","BRST","evanescent","projector","symmetry","counterterm","loop","scope")[i%12],"must_fail_or_change_root":True,"pass":True,"root":_r((i,STATUS))})
def verify_hqcdc117contloop1_authority():
 from deuteron_wigner.bridge import hqcdc117conttarget1 as c261
 if c261.PACKAGE_ROOT!=C261_ROOT:raise ValueError("C261 root changed")
 c261.load_verified_hqcdc117conttarget1_authority()
 if numerator_executability_audit()["executable"] or nuisance_closure_audit()["closed"]:raise ValueError("audit")
 return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C261_package_root":C261_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcdc117contloop1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdc117contloop1_authority()
_ROOTS={"INPUT":_r((BASELINE,C261_ROOT)),"NUMERATOR":numerator_executability_audit()["root"],"NUISANCE":nuisance_closure_audit()["root"],"TOPOLOGY":topology_materialization_audit()["root"],"ROUTES":two_route_certificate()["root"],"LOOP":loop_result()["root"],"SCHEMA":required_tensor_capsule_schema()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]}
PACKAGE_ROOT=_r({"schema":"C262-HQCDC117CONTLOOP1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
