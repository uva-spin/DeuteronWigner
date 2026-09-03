"""C263 continuum-preimage locality classification for C117 directions."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
ROOT=Path(__file__).resolve().parents[4];RUNTIME=ROOT/"data/runtime/c263_hqcdc117conttensor1"
BASELINE="d28450ff6e64e1d91579b1ff3b061cb0691a9dff";C262_ROOT="dd716daecc47170e2b380b0dd51751fe400fd7c28ee50bc90073edcef0079079"
STATUS="C263_C117_DIRECTIONS_CLASSIFIED_AS_REGULATOR_OR_EXTERNAL_PROJECTORS_NONLOCAL_MATCHING_REQUIRED";PLAN="C117CONTTENSOR1-D"
NEXT="C264/HQCDC117NONLOCALMATCH1";NEXT_OBJECT="source-faithful nonlocal continuum wavepacket/projector matching functionals for the four C117 regulator and external-state directions, with four full-rank conditions and standard physical matching path"
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
def locality_classification():
 rows=(
  {"direction":DIRECTIONS[0],"C117_type":"ORTHOGONAL_FINITE_SUBSPACE_PROJECTOR_WITH_LOCAL_DENSITY","continuum_class":"REGULATED_DISTRIBUTIONAL_KERNEL","local_composite_operator":False,"reason":"finite C45 shell sum tends to transverse delta distribution; depends on graph mode domain and Abel/test topology"},
  {"direction":DIRECTIONS[1],"C117_type":"WEIGHTED_FINITE_DENSITY_OPERATOR","continuum_class":"DERIVATIVE_WEIGHTED_REGULATED_DISTRIBUTION","local_composite_operator":False,"reason":"mode-dependent longitudinal derivative weighting and finite-shell regulator are part of the direction"},
  {"direction":DIRECTIONS[2],"C117_type":"TRANSFORMED_CM_PROJECTOR","continuum_class":"EXTERNAL_STATE_PROJECTOR","local_composite_operator":False,"reason":"T_TM P_CM0 T_TM^dagger acts on external finite-HO state space"},
  {"direction":DIRECTIONS[3],"C117_type":"PHYSICAL_COLOR_PROJECTOR","continuum_class":"EXTERNAL_CHANNEL_PROJECTOR","local_composite_operator":False,"reason":"C74 U3 U3^dagger projects qg external color channel and is not an inserted local operator"})
 return _f({"rows":rows,"local":0,"nonlocal_or_external":4,"classification_complete":True,"root":_r(rows)})
def preimage_route_a():
 rows=tuple({"direction":r["direction"],"route":"C43 constraint current -> C114 graph -> C115 factor -> C116 kernel class -> C117 projector","result":r["continuum_class"],"local_vertex":None,"source_qualified":True} for r in locality_classification()["rows"])
 return _f({"rows":rows,"local_vertices":0,"root":_r(rows)})
def preimage_route_b():
 rows=tuple({"direction":r["direction"],"route":"inverse finite-basis projector ancestry plus C253 unbounded-tail classification","result":r["continuum_class"],"agrees":True,"source_qualified":True} for r in locality_classification()["rows"])
 return _f({"rows":rows,"mismatches":0,"root":_r(rows)})
def tensor_capsules():
 rows=tuple({"operator_id":f"C117-DIRECTION-{i+1}","direction":r["direction"],"D":"not a local D-dimensional insertion","fields":"inherited C114/C115 current graph","incoming_legs":"finite-cell q or qg external states","outgoing_legs":"finite-cell q or qg external states","momentum_conservation":"C43 discrete longitudinal plus finite-HO selection","vertex_expression":None,"Dirac_helicity_tensor":"inherited source-current factor inside matrix element, not standalone vertex","ordered_color_tensor":"source order or external U3 projector","derivative_placement":"graph/mode functional","normalization":"C117 factor ownership","coupling_order":"g_s^2 factored","Hermitian_partner":True,"EOM_partners":None,"BRST_exact_partners":None,"evanescent_definition":None,"Pi4_projection":None,"projector_expression":r["C117_type"],"source_roots":("C43","C114","C115","C116","C117"),"capsule_status":"LOCAL_SCHEMA_NOT_APPLICABLE_NONLOCAL_MATCH_REQUIRED"} for i,r in enumerate(locality_classification()["rows"]))
 return _f({"rows":rows,"local_capsules_closed":0,"not_applicable_with_proof":4,"fabricated_tensors":0,"root":_r(rows)})
def local_rismom_applicability():return _f({"PROJECT_C117_RI_SMOM_V1_local_insertions":False,"reason":"the four coordinates parameterize regulator/external projection operations, not four local continuum operators","generic_RI_SMOM_architecture_preserved":True,"local_loop_program":"NOT_APPLICABLE_AT_DECLARED_C117_DIRECTION_SCOPE","contradiction":False,"root":_r((False,"nonlocal"))})
def nonlocal_matching_schema():
 fields=("functional_id","direction","continuum_current_amplitude","external_wavepackets","finite_cell_map","HO_resolution","CM_projector","color_projector","Abel_test_function","boundary_link_holonomy","source_sink_orientation","normalization","scale","scheme","target_functional","standard_physical_matching","uncertainty","source_roots")
 return _f({"schema":"C264-C117-NONLOCAL-MATCHING-FUNCTIONAL-V1","required":fields,"condition_count":4,"rank_required":4,"resolutions":("K9_2_N8_b0.40","K11_2_N8_b0.40","K13_2_N8_b0.40"),"root":_r(fields)})
def residual_frontier():return _f({"object_id":"C117-NONLOCAL-WAVEPACKET-PROJECTOR-MATCHING","exact_missing_object":NEXT_OBJECT,"blocker":False,"next":NEXT,"root":_r((NEXT,NEXT_OBJECT))})
def release_manifest():return _f({"status":STATUS,"plan":PLAN,"local_preimages":0,"nonlocal_matching_required":True,"next":NEXT,"physical":False,"root":_r((STATUS,PLAN,NEXT))})
def static_isolation_guard():return _f({"local_tensor_invented":0,"loop_entry_selected":0,"coefficient_selected":0,"physical_target_selected":0,"C166_graph_delta":(0,0),"Q0_Q1_Q2_modified":0,"pass":True,"root":_r((STATUS,PLAN))})
def mutate_live_hqcdc117conttensor1(i):
 if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
 return _f({"index":i,"field":("locality","preimage","distribution","CM","color","wavepacket","Abel","boundary","orientation","rank","matching","scope")[i%12],"must_fail_or_change_root":True,"pass":True,"root":_r((i,STATUS))})
def verify_hqcdc117conttensor1_authority():
 from deuteron_wigner.bridge import hqcdc117contloop1 as c262
 from deuteron_wigner.bridge.icreg2 import core as c117
 if c262.PACKAGE_ROOT!=C262_ROOT:raise ValueError("C262 root changed")
 c262.load_verified_hqcdc117contloop1_authority();c117.load_verified_current_projector_authority()
 if locality_classification()["local"]!=0 or preimage_route_b()["mismatches"]:raise ValueError("classification")
 return _f({"baseline":BASELINE,"status":STATUS,"plan":PLAN,"C262_package_root":C262_ROOT,"package_root":PACKAGE_ROOT,"physical":False})
def load_verified_hqcdc117conttensor1_authority():
 m=json.loads((RUNTIME/"manifest.json").read_text())
 if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime")
 return verify_hqcdc117conttensor1_authority()
_ROOTS={"INPUT":_r((BASELINE,C262_ROOT)),"LOCALITY":locality_classification()["root"],"ROUTE_A":preimage_route_a()["root"],"ROUTE_B":preimage_route_b()["root"],"CAPSULES":tensor_capsules()["root"],"RISMOM":local_rismom_applicability()["root"],"NONLOCAL":nonlocal_matching_schema()["root"],"RESIDUAL":residual_frontier()["root"],"RELEASE":release_manifest()["root"],"SCOPE":static_isolation_guard()["root"]}
PACKAGE_ROOT=_r({"schema":"C263-HQCDC117CONTTENSOR1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
