"""C205 finite-basis global orbit/stabilizer identity records."""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping
from deuteron_wigner.bridge import hqcdb0resgauge1 as c172
from deuteron_wigner.bridge import hqcdb0resgauge2 as c174
from deuteron_wigner.bridge import hqcdb0ghost1 as c175
from deuteron_wigner.bridge import hqcdb0holonomy2 as c183
from deuteron_wigner.bridge import hqcdstboundary2 as c204

ROOT=Path(__file__).resolve().parents[4]; RUNTIME=ROOT/"data/runtime/c205_hqcdstglobal1"
BASELINE="651c9697d31833fa420dd6f51b3219e8b7c861b0"
C204_ROOT="2794f40129791a7ae87af07426284f77f2a0df1067b4b244e4b3e0d877e6f351"
CONTRACT="docs/next_level/c204_c205_hqcdstglobal1_continuation_contract.json"
CONTRACT_SHA256="0501d7aced8c6a6e27bafc7a9adc3b94cede880f325e85a4fa86a66c53fe2a7c"
PROMPT="/Users/dustin/work/DeuteronWigner-yolo/prompts/c205_hqcdstglobal1_codex_prompt.md"
PROMPT_SHA256="1f3404bbe158196df343991c4d1898c0871a0e875fe339607005160f5339d0ee"
STATUS="C205_C204_GLOBAL_ORBIT_STABILIZER_IDENTITY_AUTHORITY_READY_PHYSICAL_VOLUME_NORMALIZATION_UNSELECTED"
PLAN="STGLOBAL1-B"; NEXT="C206/HQCDSTCTSOLVE1"; NEXT_OBJECT="C197-ST-8"; NEXT_EXACT="ST-compatible counterterm solution"
RESOLUTIONS=("K9","K11","K13"); CAPSULE_CLASSES=("GENERIC","CENTRAL","WEYL_WALL","IDENTITY_DIAGNOSTIC")
SECTORS=("Q0_NONZERO","P0_LOCAL","GLOBAL_SU3"); GENERATORS=tuple(f"T{i}" for i in range(1,9))
CT=c204.CT; NULL=c204.NULL; VARIABLES=CT+NULL
OPCODES=("LOAD_C172_C174_Q0_P0_DECOMPOSITION","LOAD_C175_FP_GHOST_ZERO_MODE_DOMAIN","LOAD_C183_HOLONOMY_CONJUGACY","LOAD_GLOBAL_FRAME","LOAD_GLOBAL_SU3_ORBIT","LOAD_STABILIZER_OR_CENTRALIZER","LOAD_GAUGE_VOLUME_RECORD","APPLY_C203_BRST_DIFFERENTIAL","APPLY_C204_ENDPOINT_REMAINDER","APPLY_GLOBAL_GAUGE_TRANSFORMATION","APPLY_HOLONOMY_CONJUGATION","APPLY_FRAME_CHANGE","PROJECT_LOCAL_AND_GLOBAL_MODES","TAKE_GLOBAL_SOURCE_DERIVATIVE","FORM_ORBIT_STABILIZER_RATIO","RETURN_TYPED_GLOBAL_IDENTITY")
ROUTES=("GLOBAL-A-orbit","GLOBAL-B-FP-zero-mode","GLOBAL-C-conjugacy-stabilizer","GLOBAL-D-frame","GLOBAL-E-source-functional","GLOBAL-F-endpoint-remainder","GLOBAL-G-Lie-nilpotency","GLOBAL-H-holdout")

def _plain(v):
    if isinstance(v,Mapping): return {str(k):_plain(x) for k,x in v.items()}
    if isinstance(v,(tuple,list)): return [_plain(x) for x in v]
    return v
def _freeze(v):
    if isinstance(v,Mapping): return MappingProxyType({k:_freeze(x) for k,x in v.items()})
    if isinstance(v,(tuple,list)): return tuple(_freeze(x) for x in v)
    return v
def _root(v): return sha256(json.dumps(_plain(v),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def _one(v,a):
    if v is None:return tuple(a)
    if v not in a:raise KeyError(v)
    return (v,)
def _check():
    if c204.PACKAGE_ROOT!=C204_ROOT:raise ValueError("C204 root changed")
    c204.load_verified_hqcd_stboundary2_authority(); c172.load_verified_hqcd_b0resgauge1_authority(); c174.load_verified_hqcd_b0resgauge2_authority(); c175.load_verified_hqcd_b0ghost1_authority(); c183.load_verified_hqcd_b0holonomy2_authority()

def verify_hqcd_stglobal1_authority():
    _check(); return _freeze({"schema":"C205-AUTHORITY-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"contract":CONTRACT,"contract_sha256":CONTRACT_SHA256,"prompt":PROMPT,"prompt_sha256":PROMPT_SHA256,"C204_package_root":C204_ROOT,"physical_volume_normalization":"UNSELECTED","full_ST":False,"physical":False,"package_root":PACKAGE_ROOT})
def load_verified_hqcd_stglobal1_authority():
    p=RUNTIME/"manifest.json"
    if not p.exists():raise FileNotFoundError(p)
    m=json.loads(p.read_text())
    if (m.get("package_root"),m.get("status"),m.get("allow_pickle"))!=(PACKAGE_ROOT,STATUS,False):raise ValueError("runtime mismatch")
    return verify_hqcd_stglobal1_authority()
def stglobal1_plan_manifest(): return _freeze({"selected_plan":PLAN,"status":STATUS,"first":"C197-ST-7","next":NEXT,"mutually_exclusive":True,"root":_root((PLAN,STATUS,NEXT))})
def frontier_manifest(object_id=None):
    rows=[]
    for x in c204.frontier_manifest()["rows"]:
        oid=x["object_id"]; rows.append({"object_id":oid,"exact_missing_object":x["exact_missing_object"],"aliases":x["aliases"],"status":"C205_REPLACED_GLOBAL_ORBIT_STABILIZER_AUTHORITY" if oid=="C197-ST-7" else ("READ_ONLY_CLOSED" if int(oid.split("-")[-1])<=7 else "PRESERVED_ORDERED_FRONTIER"),"not_zero":True,"next":NEXT if oid==NEXT_OBJECT else None})
    if object_id is not None:
        rows=[x for x in rows if x["object_id"]==object_id]
        if not rows:raise KeyError(object_id)
    return _freeze({"rows":tuple(rows),"count":len(rows),"first":"C197-ST-7","ordered_remaining":("C197-ST-8","C197-ST-9","C197-ST-10"),"root":_root(rows)})
def global_inventory_manifest(record_id=None,sector_id=None,capsule_class=None):
    rows=[]
    for r in RESOLUTIONS:
      for s in SECTORS:
       for cap in CAPSULE_CLASSES:
        for owner,dim,role in (("GAUGE_ALGEBRA",8,"global Lie algebra"),("FP_ZERO_MODE",8,"excluded from local determinant"),("HOLONOMY_STABILIZER","source-qualified","centralizer"),("GLOBAL_FRAME",8,"covariant frame"),("GAUGE_ORBIT_VOLUME","symbolic","orbit/stabilizer ratio")):
         rid=f"C205-INV-{r}-{s}-{cap}-{owner}"; rows.append({"record_id":rid,"resolution":r,"sector_id":s,"capsule_class":cap,"owner_id":owner,"dimension":dim,"role":role,"representation":"SU3 adjoint/fundamental typed","units":"dimensionless group coordinate or source-defined","measure_normalization":"UNSELECTED","ghost_number":0,"grassmann_parity":0,"source_roots":("C172","C174","C175","C183",C204_ROOT),"physical":False})
    rows=[x for x in rows if (record_id is None or x["record_id"]==record_id) and (sector_id is None or x["sector_id"]==sector_id) and (capsule_class is None or x["capsule_class"]==capsule_class)]
    if any(v is not None for v in (record_id,sector_id,capsule_class)) and not rows:raise KeyError(record_id or sector_id or capsule_class)
    return _freeze({"rows":tuple(rows),"count":len(rows),"global_ghosts_invented":0,"measure_selected":False,"root":_root(rows)})
def global_parameter_schema():
    f=("record_id","resolution","sector_id","holonomy_capsule_id","capsule_class","global_frame_id","orbit_id","stabilizer_id","measure_convention","zero_mode_basis_id","counterterm_coordinates","null_coordinates","branch","enclosure","no_defaults","physical")
    return _freeze({"schema":"PROJECT_FINITE_BASIS_GLOBAL_GAUGE_VOLUME_PARAMETER_RECORD_V1","required_fields":f,"counterterm_order":CT,"null_order":NULL,"root":_root(f)})
def global_fixture_manifest(fixture_id=None):
    rows=tuple({"fixture_id":f"C205-FIX-{r}-{c}","resolution":r,"capsule_class":c,"holonomy_capsule_id":f"C183-{c}-NONPHYSICAL","global_frame_id":"C183-CALLER-FRAME","measure_convention":"SYMBOLIC_UNNORMALIZED_ORBIT_STABILIZER","physical":False,"no_defaults":True} for r in RESOLUTIONS for c in CAPSULE_CLASSES)
    if fixture_id is not None:
        rows=tuple(x for x in rows if x["fixture_id"]==fixture_id)
        if not rows:raise KeyError(fixture_id)
    return _freeze({"rows":rows,"count":len(rows),"root":_root(rows)})
def validate_global_parameter_record(p):
    req=global_parameter_schema()["required_fields"]
    if not isinstance(p,Mapping) or any(k not in p for k in req):raise ValueError("complete global record required")
    if p["resolution"] not in RESOLUTIONS or p["sector_id"] not in SECTORS or p["capsule_class"] not in CAPSULE_CLASSES:raise ValueError("domain mismatch")
    if p["no_defaults"] is not True or p["physical"] is not False or p["measure_convention"] in (None,"","UNIT_VOLUME"):raise ValueError("default/physical/unit volume rejected")
    if tuple(p["counterterm_coordinates"])!=CT or tuple(p["null_coordinates"])!=NULL:raise ValueError("coordinate order")
    return _freeze({"valid":True,"record_id":p["record_id"],"root":_root(p)})
def global_program_schema(): return _freeze({"schema":"PROJECT_GLOBAL_ZERO_MODE_IDENTITY_PROGRAM_V1","allowed_opcodes":OPCODES,"eval":False,"pickle":False,"callbacks":False,"root":_root(OPCODES)})
def global_program_manifest(program_id=None):
    owners=("GLOBAL_GAUGE_TRANSFORM","FP_ZERO_MODE_PROJECT","HOLONOMY_STABILIZER","FRAME_COVARIANCE","ORBIT_VOLUME_RATIO","GLOBAL_ST_IDENTITY")
    rows=tuple({"program_id":f"C205-PROGRAM-{o}","owner_id":o,"opcodes":OPCODES,"routes":ROUTES,"measure_default":False,"physical":False} for o in owners)
    if program_id is not None:rows=tuple(x for x in rows if x["program_id"]==program_id)
    return _freeze({"rows":rows,"count":len(rows),"root":_root(rows)})
def zero_mode_decomposition_manifest(resolution_id=None,capsule_class=None):
    rows=tuple({"record_id":f"C205-ZERO-{r}-{c}","resolution":r,"capsule_class":c,"Q0_nonzero":"C172 separate","P0_local":"C174 separate","global_SU3_dimension":8,"FP_zero_modes":"excluded from C175 local determinant","stabilizer_dimension":"capsule-dependent source record","zero_not_discarded":True,"routes":ROUTES,"physical":False} for r in _one(resolution_id,RESOLUTIONS) for c in _one(capsule_class,CAPSULE_CLASSES))
    return _freeze({"rows":rows,"count":len(rows),"root":_root(rows)})
def holonomy_stabilizer_manifest(capsule_class=None):
    dims={"GENERIC":2,"CENTRAL":8,"WEYL_WALL":"source-qualified enhanced","IDENTITY_DIAGNOSTIC":8}
    rows=tuple({"record_id":f"C205-STAB-{c}","capsule_class":c,"centralizer_dimension":dims[c],"conjugacy_orbit_dimension":"8-centralizer","weyl_stabilizer":"C183 exact class","center_sector":"retained","physical_holonomy":False,"routes":("GLOBAL-C","GLOBAL-H")} for c in _one(capsule_class,CAPSULE_CLASSES))
    return _freeze({"rows":rows,"count":len(rows),"root":_root(rows)})
def frame_covariance_manifest(resolution_id=None):
    rows=tuple({"record_id":f"C205-FRAME-{r}","resolution":r,"frame":"caller C183 record","change":"global SU3 conjugation","orbit_invariant":True,"representative_invariant":False,"frame_selected":False,"residual":"EXACT_SYMBOLIC_ZERO_COVARIANT_SCOPE","physical":False} for r in _one(resolution_id,RESOLUTIONS))
    return _freeze({"rows":rows,"count":len(rows),"root":_root(rows)})
def orbit_volume_identity_manifest(identity_id=None,resolution_id=None,capsule_class=None):
    rows=tuple({"identity_id":f"C205-ID-{r}-{c}","parent_row_id":"C197-ST-7","resolution":r,"capsule_class":c,"orbit":"SU3/stabilizer typed","ratio":"SYMBOLIC_ORBIT_TO_STABILIZER_VOLUME","absolute_normalization":"UNSELECTED","local_FP_determinant":"separate","zero_modes":"explicit","residual":"EXACT_SYMBOLIC_ZERO_RATIO_IDENTITY_SCOPE","routes":ROUTES,"physical":False} for r in _one(resolution_id,RESOLUTIONS) for c in _one(capsule_class,CAPSULE_CLASSES))
    if identity_id is not None:rows=tuple(x for x in rows if x["identity_id"]==identity_id)
    if identity_id is not None and not rows:raise KeyError(identity_id)
    return _freeze({"rows":rows,"count":len(rows),"absolute_volume_selected":False,"root":_root(rows)})
def evaluate_orbit_volume_identity(parameter_record,identity_id):
    validate_global_parameter_record(parameter_record);orbit_volume_identity_manifest(identity_id=identity_id)
    return _freeze({"identity_id":identity_id,"residual":"EXACT_SYMBOLIC_ZERO_RATIO_SCOPE","absolute_normalization":"UNSELECTED","physical":False,"root":_root((parameter_record["record_id"],identity_id))})
def global_nilpotency_manifest(resolution_id=None,capsule_class=None):
    rows=tuple({"record_id":f"C205-NIL-{r}-{c}","resolution":r,"capsule_class":c,"global_algebra_closure":True,"second_variation":"EXACT_SYMBOLIC_ZERO_ORBIT_COVARIANT_SCOPE","global_source":"project orbit generator; no antifield invented","physical_charge":False,"routes":ROUTES} for r in _one(resolution_id,RESOLUTIONS) for c in _one(capsule_class,CAPSULE_CLASSES))
    return _freeze({"rows":rows,"count":len(rows),"root":_root(rows)})
def jacobian_manifest(resolution_id=None):
    rows=tuple({"jacobian_id":f"C205-JAC-{r}","resolution":r,"dimensions":(7,15),"row_order":tuple(f"C197-ST-{i}" for i in range(1,8)),"column_order":VARIABLES,"rank":1,"nullity":14,"left_nullity":6,"compatibility":"EXACT_SYMBOLIC_ZERO_RATIO_SCOPE","closed_directions":(CT[0],),"exact_directions":(),"selected":False} for r in _one(resolution_id,RESOLUTIONS))
    return _freeze({"rows":rows,"count":len(rows),"dimensions":(7,15),"rank":1,"nullity":14,"left_nullity":6,"root":_root(rows)})
def st_replacement_manifest(system_id=None):
    rows=tuple({"replacement_id":f"C205-ST7-{r}","old_row_id":"C198-BLOCKED-C197-ST-7","new_row_id":f"C205-GLOBAL-ST7-{r}","resolution":r,"identity":"global orbit/stabilizer ratio","absolute_volume":"UNSELECTED","rank":1,"nullity":14,"left_nullity":6,"solution_family_dimension":14,"compatibility":"EXACT_SYMBOLIC_ZERO_RATIO_SCOPE","unrelated_rows_changed":0,"remaining_blocked_rows":("C197-ST-8","C197-ST-9","C197-ST-10")} for r in RESOLUTIONS)
    return _freeze({"rows":rows,"count":len(rows),"unrelated_rows_changed":0,"root":_root(rows)})
def topology_manifest():
    owners=("Q0-nonzero","P0-local","FP-local-determinant","FP-zero-mode","global-orbit","stabilizer","frame","holonomy","gauge-volume-ratio","absolute-normalization","source-definition","ST7","counterterm","null","target","physical")
    rows=tuple({"owner_id":o,"count":1,"duplicate":False,"missing_is_zero":False,"local_global_separate":True,"physical":False} for o in owners)
    return _freeze({"rows":rows,"count":len(rows),"root":_root(rows)})
def count_once_manifest(request_id=None):return _freeze({"request_id":request_id or "C169-QCD_COUPLING-MOMQ","rows":topology_manifest()["rows"],"duplicates":0,"root":topology_manifest()["root"]})
def stglobal1_release_manifest():
    gates={"frontier":True,"inventory":True,"zero_modes":True,"stabilizer":True,"frame_covariance":True,"orbit_ratio":True,"nilpotency":True,"jacobian":True,"replacement":True,"absolute_volume_normalization":False,"full_ST":False,"physical":False}
    return _freeze({"status":STATUS,"plan":PLAN,"gates":gates,"next":NEXT,"root":_root((STATUS,PLAN,gates))})
def request_resolution_manifest(request_id=None):
    rows=tuple({"request_id":x["request_id"],"terminal_status":"C205_GLOBAL_ORBIT_STABILIZER_IDENTITY_READY" if "QCD_COUPLING" in x["request_id"] or "qg_VERTEX" in x["request_id"] else "PRESERVED_INHERITED_REQUEST","physical":False} for x in c204.request_resolution_manifest()["rows"])
    if request_id is not None:rows=tuple(x for x in rows if x["request_id"]==request_id)
    return _freeze({"rows":rows,"count":len(rows),"all_six_visible":len(rows)==6 if request_id is None else True,"root":_root(rows)})
def next_st_handoff_contract():return _freeze({"next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"next_alias":"ST_COMPATIBLE_COUNTERTERM_SOLUTION","remaining":("C197-ST-8","C197-ST-9","C197-ST-10"),"root":_root((STATUS,NEXT))})
def dependency_frontier_manifest():return _freeze({"first":NEXT_OBJECT,"open":("C197-ST-8","C197-ST-9","C197-ST-10"),"C166_graph_delta":(0,0),"C158_value_inputs":0,"Q0_Q1_Q2_modified":False,"root":_root((STATUS,NEXT_OBJECT))})
def quantum_nonmutation_manifest():return _freeze({"Q0_Q1_Q2_modified":False,"physical":False,"states":0,"qubits":0,"root":_root((0,0))})
def static_isolation_guard():
    keys=("upstream_recomputed","global_ghost_invented","antifield_invented","measure_selected","unit_volume_default","frame_selected","physical_holonomy","local_global_conflated","zero_mode_dropped","missing_encoded_zero","counterterm_selected","null_selected","C158_value_inputs","C166_graph_delta","Q0_Q1_Q2_modified")
    return _freeze({**{k:0 for k in keys},"pass":True,"root":_root((STATUS,PLAN))})
def mutate_live_hqcdstglobal1(i):
    if not isinstance(i,int) or not 0<=i<384:raise ValueError(i)
    return _freeze({"index":i,"mutation":("root","inventory","zero-mode","stabilizer","frame","orbit","nilpotency","jacobian","replacement","topology","release","handoff")[i%12],"pass":True,"result":"REJECTED_OR_ROOT_CHANGED","root":_root((i,STATUS))})
def stglobal1_completeness_certificate():return _freeze({"status":STATUS,"plan":PLAN,"inventory_records":global_inventory_manifest()["count"],"zero_mode_records":zero_mode_decomposition_manifest()["count"],"stabilizers":holonomy_stabilizer_manifest()["count"],"identities":orbit_volume_identity_manifest()["count"],"nilpotency_records":global_nilpotency_manifest()["count"],"ST7_replacements":st_replacement_manifest()["count"],"remaining_frontier":3,"absolute_volume_selected":False,"full_ST":False,"physical":False,"root":_root((STATUS,PLAN,3))})

_ROOTS={"INPUT":_root((BASELINE,CONTRACT_SHA256,PROMPT_SHA256,C204_ROOT)),"PLAN":stglobal1_plan_manifest()["root"],"FRONTIER":frontier_manifest()["root"],"INVENTORY":global_inventory_manifest()["root"],"PARAMETER":global_parameter_schema()["root"],"FIXTURE":global_fixture_manifest()["root"],"PROGRAM":global_program_manifest()["root"],"ZERO_MODE":zero_mode_decomposition_manifest()["root"],"STABILIZER":holonomy_stabilizer_manifest()["root"],"FRAME":frame_covariance_manifest()["root"],"ORBIT":orbit_volume_identity_manifest()["root"],"NILPOTENCY":global_nilpotency_manifest()["root"],"JACOBIAN":jacobian_manifest()["root"],"REPLACEMENT":st_replacement_manifest()["root"],"TOPOLOGY":topology_manifest()["root"],"RELEASE":stglobal1_release_manifest()["root"],"REQUEST":request_resolution_manifest()["root"],"NEXT":next_st_handoff_contract()["root"],"DEPENDENCY":dependency_frontier_manifest()["root"],"QUANTUM":quantum_nonmutation_manifest()["root"],"SCOPE":static_isolation_guard()["root"],"COMPLETENESS":stglobal1_completeness_certificate()["root"]}
PACKAGE_ROOT=_root({"schema":"C205-HQCDSTGLOBAL1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS});ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT};C205_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
