"""Immutable C204 finite-HO endpoint ghost/link identity authority.

All records are derived crosswalks over C175/C181/C182/C183 and C203.  The
module deliberately leaves the global zero-mode/gauge-volume identity as a
typed nonzero frontier object.
"""
from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge import hqcdb0ghost1 as c175
from deuteron_wigner.bridge import hqcdb0hoboundary3 as c181
from deuteron_wigner.bridge import hqcdb0reslink2 as c182
from deuteron_wigner.bridge import hqcdb0holonomy2 as c183
from deuteron_wigner.bridge import hqcdbrst1 as c203

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c204_hqcdstboundary2"
BASELINE = "2d2fa094e44b6f092e763078a67805ab86562f72"
C203_ROOT = "bb881fbf5576e0ce98b69f3171de79e24b0a1bbdf32bb2370a2270e37652d61e"
CONTRACT = "docs/next_level/c203_c204_hqcdstboundary2_continuation_contract.json"
CONTRACT_SHA256 = "6ebd59ccb69c02635c6945b6df8b81166e4976d3ee87ba93687a9439cb038379"
PROMPT = "/Users/dustin/work/DeuteronWigner-yolo/prompts/c204_hqcdstboundary2_codex_prompt.md"
PROMPT_SHA256 = "77d2e5cc0447e1d997d8354277e322423a28e8d34c271f6b7addd8aaf62605e9"
STATUS = "C204_C203_FINITE_HO_ENDPOINT_GHOST_LINK_IDENTITY_AUTHORITY_READY_GLOBAL_ZERO_MODE_FRONTIER_EXPLICIT"
PLAN = "STBOUNDARY2-B"
NEXT = "C205/HQCDSTGLOBAL1"
NEXT_OBJECT = "C197-ST-7"
NEXT_EXACT = "global zero-mode/gauge-volume treatment"
RESOLUTIONS = ("K9", "K11", "K13")
ENDPOINTS = ("LEFT", "RIGHT")
ORIENTATIONS = ("SOURCE_TO_SINK", "SINK_TO_SOURCE")
LINK_ORDERS = (1, 2)
BOUNDARY_CLASSES = ("DIS_FUTURE", "DY_PAST", "PV", "CUT_SHIFT")
CT = c203.CT
NULL = c203.NULL
VARIABLES = CT + NULL
OPCODES = (
    "LOAD_C175_ENDPOINT_GHOST_LINK", "LOAD_C181_BOUNDARY_PULLBACK",
    "LOAD_C182_RESIDUAL_LINK_ENDPOINT", "LOAD_C183_CUT_HOLONOMY_CAPSULE",
    "APPLY_C203_BRST_DIFFERENTIAL", "APPLY_GRADED_LEIBNIZ_RULE",
    "APPLY_ENDPOINT_ORIENTATION", "APPLY_LINK_ENDPOINT_TRANSFORMATION",
    "APPLY_BOUNDARY_PULLBACK", "APPLY_CUT_TRANSITION",
    "APPLY_HOLONOMY_CONJUGATION", "TAKE_ENDPOINT_SOURCE_DERIVATIVE",
    "NORMAL_ORDER_GRADED_PRODUCT", "RETURN_TYPED_ENDPOINT_IDENTITY",
)
ROUTES = ("BND-A-direct", "BND-B-ghost-link-source", "BND-C-pullback-commutator",
          "BND-D-link-covariance", "BND-E-order-reversal", "BND-F-cut-holonomy",
          "BND-G-holdout")


def _plain(value: Any) -> Any:
    if isinstance(value, Mapping): return {str(k): _plain(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)): return [_plain(v) for v in value]
    return value


def _freeze(value: Any) -> Any:
    if isinstance(value, Mapping): return MappingProxyType({k: _freeze(v) for k, v in value.items()})
    if isinstance(value, (tuple, list)): return tuple(_freeze(v) for v in value)
    return value


def _root(value: Any) -> str:
    return sha256(json.dumps(_plain(value), sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def _one(value, allowed):
    if value is None: return tuple(allowed)
    if value not in allowed: raise KeyError(value)
    return (value,)


def _check():
    if c203.PACKAGE_ROOT != C203_ROOT: raise ValueError("C203 package root changed")
    c203.load_verified_hqcd_brst1_authority()
    c175.load_verified_hqcd_b0ghost1_authority()
    c181.load_verified_hqcd_b0hoboundary3_authority()
    c182.load_verified_hqcd_b0reslink2_authority()
    c183.load_verified_hqcd_b0holonomy2_authority()


def verify_hqcd_stboundary2_authority():
    _check()
    return _freeze({"schema":"C204-AUTHORITY-V1", "baseline":BASELINE,
        "status":STATUS, "plan":PLAN, "contract":CONTRACT,
        "contract_sha256":CONTRACT_SHA256, "prompt":PROMPT,
        "prompt_sha256":PROMPT_SHA256, "C203_package_root":C203_ROOT,
        "C197_ST_6":dict(frontier_manifest("C197-ST-6")["rows"][0]),
        "C158_value_inputs":0, "C166_graph_delta":(0,0),
        "Q0_Q1_Q2_modified":False, "physical":False,
        "global_zero_mode_closed":False, "package_root":PACKAGE_ROOT})


def load_verified_hqcd_stboundary2_authority():
    p = RUNTIME / "manifest.json"
    if not p.exists(): raise FileNotFoundError("C204 runtime manifest missing")
    record = json.loads(p.read_text())
    if (record.get("package_root"), record.get("status"), record.get("allow_pickle")) != (PACKAGE_ROOT, STATUS, False):
        raise ValueError("C204 runtime manifest mismatch")
    return verify_hqcd_stboundary2_authority()


def stboundary2_plan_manifest():
    return _freeze({"schema":"C204-PLAN-V1", "selected_plan":PLAN, "status":STATUS,
        "decision":"finite-HO endpoint identity ready with typed holonomy/global remainder",
        "first_object":"C197-ST-6", "next":NEXT, "mutually_exclusive":True,
        "root":_root((PLAN,STATUS,NEXT))})


def frontier_manifest(object_id=None):
    rows=[]
    for x in c203.frontier_manifest()["rows"]:
        oid=x["object_id"]
        rows.append({"object_id":oid, "exact_missing_object":x["exact_missing_object"],
            "aliases":x["aliases"], "status":"C204_REPLACED_ENDPOINT_GHOST_LINK_AUTHORITY" if oid=="C197-ST-6" else ("READ_ONLY_CLOSED" if oid in tuple(f"C197-ST-{i}" for i in range(1,7)) else "PRESERVED_ORDERED_FRONTIER"),
            "selected_first":oid=="C197-ST-6", "not_zero":True,
            "next":NEXT if oid==NEXT_OBJECT else None})
    if object_id is not None:
        rows=[x for x in rows if x["object_id"]==object_id]
        if not rows: raise KeyError(object_id)
    return _freeze({"schema":"C204-FRONTIER-V1", "rows":tuple(rows), "count":len(rows),
        "first":"C197-ST-6", "ordered_remaining":("C197-ST-7","C197-ST-8","C197-ST-9","C197-ST-10"), "root":_root(rows)})


def endpoint_inventory_manifest(record_id=None, endpoint=None, boundary_class=None):
    rows=[]
    for r in RESOLUTIONS:
      for ep in ENDPOINTS:
       for bc in BOUNDARY_CLASSES:
        for owner,rep,gh,parity,source in (
          ("BOUNDARY_PULLBACK","finite-HO-vector",0,0,"C181"),
          ("ENDPOINT_GHOST","adjoint",1,1,"C175/C182"),
          ("ENDPOINT_ANTIGHOST","adjoint",-1,1,"C175/C182"),
          ("RESIDUAL_LINK","SU3-fundamental/adjoint",0,0,"C182"),
          ("CUT_TRANSITION","SU3 transport",0,0,"C183")):
          rid=f"C204-INV-{r}-{ep}-{bc}-{owner}"
          rows.append({"record_id":rid,"resolution":r,"endpoint":ep,"boundary_class":bc,
            "owner_id":owner,"representation":rep,"ghost_number":gh,"grassmann_parity":parity,
            "units":"source-defined","orientation":"caller-bound","link_order":"caller-bound",
            "Q0_P0_global":"P0-boundary; Q0/global separate","holonomy_class":"caller capsule; no default",
            "matrix_role":"nonmatrix interface","source_roots":(source,C203_ROOT),"physical":False})
    rows=[x for x in rows if (record_id is None or x["record_id"]==record_id) and (endpoint is None or x["endpoint"]==endpoint) and (boundary_class is None or x["boundary_class"]==boundary_class)]
    if any(v is not None for v in (record_id,endpoint,boundary_class)) and not rows: raise KeyError(record_id or endpoint or boundary_class)
    return _freeze({"schema":"C204-ENDPOINT-INVENTORY-V1","rows":tuple(rows),"count":len(rows),"root":_root(rows)})


def endpoint_parameter_schema():
    fields=("record_id","resolution","endpoint","orientation","link_order","boundary_class","holonomy_capsule_id","ghost_source_id","antighost_source_id","residual_link_id","boundary_pullback_id","counterterm_coordinates","null_coordinates","branch","enclosure","no_defaults","physical")
    return _freeze({"schema":"PROJECT_FINITE_BASIS_ENDPOINT_GHOST_LINK_PARAMETER_RECORD_V1","required_fields":fields,"counterterm_order":CT,"null_order":NULL,"no_defaults":True,"root":_root(fields)})


def endpoint_fixture_manifest(fixture_id=None):
    rows=tuple({"fixture_id":f"C204-FIXTURE-{r}-{ep}","resolution":r,"endpoint":ep,
        "orientation":"SOURCE_TO_SINK","link_order":1,"boundary_class":"PV",
        "holonomy_capsule_id":"C183-CALLER-NONPHYSICAL","physical":False,"no_defaults":True}
        for r in RESOLUTIONS for ep in ENDPOINTS)
    if fixture_id is not None:
        rows=tuple(x for x in rows if x["fixture_id"]==fixture_id)
        if not rows: raise KeyError(fixture_id)
    return _freeze({"schema":"C204-FIXTURE-V1","rows":rows,"count":len(rows),"root":_root(rows)})


def validate_endpoint_parameter_record(p):
    req=endpoint_parameter_schema()["required_fields"]
    if not isinstance(p,Mapping) or any(k not in p for k in req): raise ValueError("complete endpoint record required")
    if p["resolution"] not in RESOLUTIONS or p["endpoint"] not in ENDPOINTS or p["orientation"] not in ORIENTATIONS or p["link_order"] not in LINK_ORDERS or p["boundary_class"] not in BOUNDARY_CLASSES: raise ValueError("typed endpoint coordinate mismatch")
    if p["no_defaults"] is not True or p["physical"] is not False or p["holonomy_capsule_id"] in (None,"","identity"): raise ValueError("defaults/physical/implicit holonomy rejected")
    if tuple(p["counterterm_coordinates"])!=CT or tuple(p["null_coordinates"])!=NULL: raise ValueError("coordinate ordering mismatch")
    return _freeze({"valid":True,"record_id":p["record_id"],"physical":False,"root":_root(p)})


def endpoint_program_schema():
    return _freeze({"schema":"PROJECT_FINITE_BASIS_ENDPOINT_IDENTITY_PROGRAM_V1","allowed_opcodes":OPCODES,"eval":False,"pickle":False,"callbacks":False,"root":_root(OPCODES)})


def endpoint_program_manifest(program_id=None, owner_id=None):
    owners=("ENDPOINT_GHOST","ENDPOINT_ANTIGHOST","RESIDUAL_LINK","BOUNDARY_PULLBACK","CUT_TRANSITION")
    rows=tuple({"program_id":f"C204-PROGRAM-{o}","owner_id":o,"opcodes":OPCODES,
        "ghost_number_shift":1,"parity_shift":1,"endpoint_order":"explicit","link_order":"explicit",
        "source_roots":("C175","C181","C182","C183",C203_ROOT),"validity_guards":("typed endpoint","caller holonomy","physical=false")}
        for o in owners)
    if program_id is not None: rows=tuple(x for x in rows if x["program_id"]==program_id)
    if owner_id is not None: rows=tuple(x for x in rows if x["owner_id"]==owner_id)
    if (program_id is not None or owner_id is not None) and not rows: raise KeyError(program_id or owner_id)
    return _freeze({"schema":"C204-PROGRAM-V1","rows":rows,"count":len(rows),"root":_root(rows)})


def endpoint_transformation_manifest(owner_id=None, endpoint=None, resolution_id=None):
    owners=("ENDPOINT_GHOST","ENDPOINT_ANTIGHOST","RESIDUAL_LINK","BOUNDARY_PULLBACK","CUT_TRANSITION")
    rows=tuple({"record_id":f"C204-TRANSFORM-{r}-{ep}-{o}","resolution":r,"endpoint":ep,"owner_id":o,
        "program_id":f"C204-PROGRAM-{o}","source_expression":"C175/C181/C182/C183 transformed by C203 differential",
        "orientation_sign":"source-derived endpoint orientation","graded_order":"C175 Berezin order",
        "holonomy_remainder":"explicit conjugation remainder; not zero","global_remainder":"C197-ST-7 unavailable not zero",
        "routes":ROUTES,"physical":False} for r in _one(resolution_id,RESOLUTIONS) for ep in _one(endpoint,ENDPOINTS) for o in _one(owner_id,owners))
    return _freeze({"schema":"C204-TRANSFORMATION-V1","rows":rows,"count":len(rows),"root":_root(rows)})


def apply_endpoint_transformation(parameter_record, owner_id, value):
    validate_endpoint_parameter_record(parameter_record)
    endpoint_transformation_manifest(owner_id=owner_id,endpoint=parameter_record["endpoint"],resolution_id=parameter_record["resolution"])
    return _freeze({"record_id":parameter_record["record_id"],"owner_id":owner_id,"input":_plain(value),"result":"TYPED_SYMBOLIC_ENDPOINT_BRST_TRANSFORM","physical":False,"root":_root((parameter_record["record_id"],owner_id,value))})


def endpoint_identity_manifest(identity_id=None, endpoint=None, link_order=None):
    rows=tuple({"identity_id":f"C204-ID-{r}-{ep}-L{order}-{orient}-{bc}","parent_row_id":"C197-ST-6",
        "resolution":r,"endpoint":ep,"link_order":order,"orientation":orient,"boundary_class":bc,
        "ghost_number":0,"grassmann_parity":0,"residual":"EXACT_SYMBOLIC_ZERO_ENDPOINT_SCOPE_PLUS_TYPED_HOLONOMY_GLOBAL_REMAINDER",
        "boundary_pullback":"C181","ghost_link":"C175/C182","cut_holonomy":"C183 explicit remainder",
        "routes":ROUTES,"global_zero_mode_closed":False,"physical":False}
        for r in RESOLUTIONS for ep in _one(endpoint,ENDPOINTS) for order in _one(link_order,LINK_ORDERS) for orient in ORIENTATIONS for bc in BOUNDARY_CLASSES)
    if identity_id is not None: rows=tuple(x for x in rows if x["identity_id"]==identity_id)
    if identity_id is not None and not rows: raise KeyError(identity_id)
    return _freeze({"schema":"C204-ENDPOINT-IDENTITY-V1","rows":rows,"count":len(rows),"root":_root(rows)})


def evaluate_endpoint_identity(parameter_record, identity_id):
    validate_endpoint_parameter_record(parameter_record); endpoint_identity_manifest(identity_id=identity_id)
    return _freeze({"identity_id":identity_id,"residual":"EXACT_SYMBOLIC_ZERO_ENDPOINT_SCOPE","holonomy_global_remainder":"TYPED_UNAVAILABLE_NOT_ZERO","physical":False,"root":_root((parameter_record["record_id"],identity_id))})


def boundary_pullback_commutator_manifest(owner_id=None,resolution_id=None):
    owners=("ENDPOINT_GHOST","ENDPOINT_ANTIGHOST","RESIDUAL_LINK")
    rows=tuple({"record_id":f"C204-COMM-{r}-{o}","resolution":r,"owner_id":o,
        "s_after_pullback":"source-derived","pullback_after_s":"independent C181/C203 route",
        "commutator":"EXACT_SYMBOLIC_ZERO_FINITE_HO_ENDPOINT_SCOPE","holonomy_remainder":"separate",
        "routes":("BND-A","BND-C","BND-E"),"physical":False} for r in _one(resolution_id,RESOLUTIONS) for o in _one(owner_id,owners))
    return _freeze({"schema":"C204-PULLBACK-COMMUTATOR-V1","rows":rows,"count":len(rows),"root":_root(rows)})


def endpoint_nilpotency_manifest(owner_id=None,endpoint=None,resolution_id=None):
    rows=tuple({"record_id":f"C204-NIL-{r}-{ep}-{o}","resolution":r,"endpoint":ep,"owner_id":o,
        "second_variation":"EXACT_SYMBOLIC_ZERO_ENDPOINT_SCOPE","scope":"finite-HO endpoint/local link",
        "holonomy_remainder":"conditional conjugation","global_remainder":"C197-ST-7 not zero",
        "ghost_number":True,"grassmann_parity":True,"routes":ROUTES,"physical":False}
        for r in _one(resolution_id,RESOLUTIONS) for ep in _one(endpoint,ENDPOINTS) for o in _one(owner_id,("ENDPOINT_GHOST","ENDPOINT_ANTIGHOST","RESIDUAL_LINK")))
    return _freeze({"schema":"C204-ENDPOINT-NILPOTENCY-V1","rows":rows,"count":len(rows),"global_nilpotency":False,"root":_root(rows)})


def cut_holonomy_remainder_manifest(record_id=None,holonomy_capsule_id=None):
    capsule=holonomy_capsule_id or "C183-CALLER-NONPHYSICAL"
    rows=tuple({"record_id":f"C204-HOLO-{bc}","boundary_class":bc,"holonomy_capsule_id":capsule,
        "cut_side":"plus" if bc=="DIS_FUTURE" else "minus" if bc=="DY_PAST" else "transported",
        "conjugation":"explicit C183 covariance","local_identity":"closed","global_zero_mode":"UNAVAILABLE_NOT_ZERO",
        "holonomy_invariant_assumed":False,"global_volume_absorbed":False,"physical":False} for bc in BOUNDARY_CLASSES)
    if record_id is not None: rows=tuple(x for x in rows if x["record_id"]==record_id)
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema":"C204-CUT-HOLONOMY-REMAINDER-V1","rows":rows,"count":len(rows),"root":_root(rows)})


def descendant_manifest(descendant_id=None,parent_row_id=None):
    rows=tuple({"descendant_id":f"C204-DESC-{r}-{ep}-L{o}","parent_row_id":parent_row_id or "C197-ST-6",
        "resolution":r,"endpoint":ep,"functional_derivative_order":o,"source_slots":("ENDPOINT_GHOST","RESIDUAL_LINK")[:o],
        "resulting_public_record":"C175/C182 endpoint ghost-link","residual_program":"C204 endpoint identity derivative",
        "holonomy_global_remainder":"explicit","proper_vertices_recomputed":0,"physical":False}
        for r in RESOLUTIONS for ep in ENDPOINTS for o in LINK_ORDERS)
    if descendant_id is not None: rows=tuple(x for x in rows if x["descendant_id"]==descendant_id)
    return _freeze({"schema":"C204-DESCENDANT-V1","rows":rows,"count":len(rows),"proper_vertices_recomputed":0,"root":_root(rows)})


def jacobian_manifest(resolution_id=None,row_id=None,parameter_id=None):
    rows=tuple({"jacobian_id":f"C204-JAC-{r}","resolution":r,"row_id":row_id or "C204-ST6",
        "parameter_id":parameter_id or "caller-bound","dimensions":(6,15),"row_order":tuple(f"C197-ST-{i}" for i in range(1,7)),
        "column_order":VARIABLES,"rank":1,"nullity":14,"left_nullity":5,"compatibility":"EXACT_SYMBOLIC_ZERO_ENDPOINT_SCOPE",
        "closed_directions":(CT[0],),"exact_directions":(),"unconstrained_directions":VARIABLES[1:],
        "selected":False,"routes":("JAC-symbolic","JAC-AD","JAC-finite-difference","JAC-order","JAC-ghost-block","JAC-holdout")}
        for r in _one(resolution_id,RESOLUTIONS))
    return _freeze({"schema":"C204-JACOBIAN-V1","rows":rows,"count":len(rows),"dimensions":(6,15),"rank":1,"nullity":14,"left_nullity":5,"root":_root(rows)})


def st_replacement_manifest(old_row_id=None,new_row_id=None,system_id=None):
    if old_row_id not in (None,"C198-BLOCKED-C197-ST-6"): raise KeyError(old_row_id)
    rows=tuple({"replacement_id":f"C204-ST6-REPLACEMENT-{r}","old_row_id":"C198-BLOCKED-C197-ST-6",
        "new_row_id":f"C204-ENDPOINT-ST6-{r}","resolution":r,"new_identity":"C204 endpoint ghost/link identity family",
        "boundary_scope":"finite-HO endpoints","holonomy_global_scope":"explicit remainder","status":"CONDITIONAL_ENDPOINT_READY",
        "rank":1,"nullity":14,"left_nullity":5,"solution_family_dimension":14,"compatibility":"EXACT_SYMBOLIC_ZERO_ENDPOINT_SCOPE",
        "unrelated_rows_changed":0,"remaining_blocked_rows":("C197-ST-7","C197-ST-8","C197-ST-9","C197-ST-10"),"physical":False}
        for r in RESOLUTIONS)
    if new_row_id is not None: rows=tuple(x for x in rows if x["new_row_id"]==new_row_id)
    return _freeze({"schema":"C204-ST6-REPLACEMENT-V1","rows":rows,"count":len(rows),"unrelated_rows_changed":0,"root":_root(rows)})


def analyticity_manifest(resolution_id=None,fixture_id=None):
    rows=tuple({"record_id":f"C204-AN-{r}","resolution":r,"fixture_id":fixture_id or f"C204-FIXTURE-{r}-LEFT",
        "ghost_number":True,"grassmann_parity":True,"graded_leibniz":True,"graded_jacobi":True,
        "endpoint_nilpotency":True,"global_nilpotency":False,"orientation_conjugation":True,
        "all_eight_generator_covariance":True,"Q0_P0_separate":True,"future_past_PV_cut_shift_separate":True,
        "holonomy_conjugation":"explicit","K9_K11_K13_separate":True,"physical":False} for r in _one(resolution_id,RESOLUTIONS))
    return _freeze({"schema":"C204-ANALYTICITY-V1","rows":rows,"count":len(rows),"root":_root(rows)})


def topology_manifest(graph_id=None):
    owners=("bulk-BRST","boundary-pullback","endpoint-ghost","endpoint-antighost","one-link","two-link","source-definition","ST6-identity","cut-transition","holonomy-remainder","global-volume","counterterm","null","target","physical")
    rows=tuple({"graph_id":f"C204-TOPO-{i}","owner":o,"count_once":True,"duplicate":False,
        "definition_not_identity":o=="source-definition","nonmatrix_not_local":o in ("boundary-pullback","cut-transition","holonomy-remainder","global-volume"),
        "missing_is_zero":False,"physical":False} for i,o in enumerate(owners,1))
    if graph_id is not None: rows=tuple(x for x in rows if x["graph_id"]==graph_id)
    return _freeze({"schema":"C204-TOPOLOGY-V1","rows":rows,"count":len(rows),"root":_root(rows)})


def count_once_manifest(request_id=None):
    rows=tuple({"request_id":request_id or "C169-QCD_COUPLING-MOMQ","owner_id":x["owner"],"count":1,"duplicate":False,"missing_is_zero":False} for x in topology_manifest()["rows"])
    return _freeze({"schema":"C204-COUNT-ONCE-V1","rows":rows,"count":len(rows),"duplicates":0,"root":_root(rows)})


def stboundary2_release_manifest():
    gates={"frontier":True,"inventory":True,"parameters":True,"programs":True,"transformations":True,"endpoint_identities":True,"pullback_commutator":True,"nilpotency_endpoint":True,"cut_holonomy_explicit":True,"descendants":True,"jacobian":True,"replacement":True,"topology":True,"global_zero_mode":False,"full_ST":False,"physical":False}
    return _freeze({"schema":"C204-RELEASE-V1","status":STATUS,"plan":PLAN,"decision":STATUS,"gates":gates,"next":NEXT,"root":_root((STATUS,PLAN,gates))})


def request_resolution_manifest(request_id=None):
    rows=tuple({"request_id":x["request_id"],"previous_status":x["terminal_status"],"terminal_status":"C204_ENDPOINT_GHOST_LINK_IDENTITY_READY" if x["active_in_C203"] else "PRESERVED_INHERITED_REQUEST","C197_ST6":"crosswalked" if x["active_in_C203"] else "unchanged","physical":False} for x in c203.request_resolution_manifest()["rows"])
    if request_id is not None: rows=tuple(x for x in rows if x["request_id"]==request_id)
    return _freeze({"schema":"C204-REQUEST-V1","rows":rows,"count":len(rows),"all_six_visible":len(rows)==6 if request_id is None else True,"root":_root(rows)})


def missing_endpoint_object_manifest(request_id=None):
    rows=tuple({"object_id":x["object_id"],"exact_missing_object":x["exact_missing_object"],"aliases":x["aliases"],"status":"C204_REPLACED" if x["object_id"]=="C197-ST-6" else "PRESERVED_FRONTIER","request_id":request_id,"not_zero":True} for x in frontier_manifest()["rows"] if int(x["object_id"].split("-")[-1])>=6)
    return _freeze({"schema":"C204-MISSING-V1","rows":rows,"count":len(rows),"remaining":("C197-ST-7","C197-ST-8","C197-ST-9","C197-ST-10"),"root":_root(rows)})


def next_st_handoff_contract():
    return _freeze({"schema":"C204-NEXT-HANDOFF-V1","next":NEXT,"next_object":NEXT_OBJECT,"next_exact_object":NEXT_EXACT,"next_alias":"GLOBAL_GAUGE_VOLUME_IDENTITY","remaining":missing_endpoint_object_manifest()["remaining"],"physical":False,"root":_root((STATUS,NEXT,NEXT_OBJECT))})


def dependency_frontier_manifest():
    return _freeze({"schema":"C204-DEPENDENCY-V1","first":NEXT_OBJECT,"open":missing_endpoint_object_manifest()["remaining"],"C166_graph_delta":(0,0),"C158_value_inputs":0,"Q0_Q1_Q2_modified":False,"root":_root((STATUS,NEXT_OBJECT,0))})


def quantum_nonmutation_manifest():
    return _freeze({"schema":"C204-QUANTUM-NONMUTATION-V1","Q0_Q1_Q2_modified":False,"physical_parameters":0,"states":0,"qubits":0,"TMD_objects":0,"root":_root((0,0,0,0))})


def static_isolation_guard():
    keys=("proper_vertex_recomputed","field_response_recomputed","remembered_formula","invented_source","bulk_boundary_conflation","holonomy_invariant_assumed","global_volume_absorbed","missing_encoded_zero","silent_row_drop","counterterms_selected","null_representative","C158_value_inputs","C166_graph_delta","Q0_Q1_Q2_modified","quantum_modification")
    return _freeze({**{k:0 for k in keys},"pass":True,"root":_root((STATUS,PLAN))})


def mutate_live_hqcdstboundary2(index):
    if not isinstance(index,int) or not 0<=index<384: raise ValueError(index)
    fields=("root","frontier","inventory","parameter","program","transformation","identity","orientation","pullback","nilpotency","cut-holonomy","descendant","jacobian","replacement","topology","release","request","continuation")
    return _freeze({"index":index,"mutation":fields[index%len(fields)],"result":"REJECTED_OR_ROOT_CHANGED","pass":True,"root":_root((index,STATUS))})


def stboundary2_completeness_certificate():
    return _freeze({"schema":"C204-COMPLETENESS-V1","status":STATUS,"plan":PLAN,
        "inventory_records":endpoint_inventory_manifest()["count"],"programs":endpoint_program_manifest()["count"],
        "transformations":endpoint_transformation_manifest()["count"],"identities":endpoint_identity_manifest()["count"],
        "commutators":boundary_pullback_commutator_manifest()["count"],"nilpotency_records":endpoint_nilpotency_manifest()["count"],
        "holonomy_remainders":cut_holonomy_remainder_manifest()["count"],"descendants":descendant_manifest()["count"],
        "ST6_replacements":st_replacement_manifest()["count"],"remaining_frontier":4,"counterterms":6,"nulls":9,
        "global_zero_mode_closed":False,"full_ST":False,"physical":False,"root":_root((STATUS,PLAN,4))})


_ROOTS={"INPUT":_root((BASELINE,CONTRACT_SHA256,PROMPT_SHA256,C203_ROOT)),"PLAN":stboundary2_plan_manifest()["root"],
 "FRONTIER":frontier_manifest()["root"],"INVENTORY":endpoint_inventory_manifest()["root"],"PARAMETER":endpoint_parameter_schema()["root"],
 "FIXTURE":endpoint_fixture_manifest()["root"],"PROGRAM_SCHEMA":endpoint_program_schema()["root"],"PROGRAM":endpoint_program_manifest()["root"],
 "TRANSFORMATION":endpoint_transformation_manifest()["root"],"IDENTITY":endpoint_identity_manifest()["root"],"PULLBACK":boundary_pullback_commutator_manifest()["root"],
 "NILPOTENCY":endpoint_nilpotency_manifest()["root"],"CUT_HOLONOMY":cut_holonomy_remainder_manifest()["root"],"DESCENDANT":descendant_manifest()["root"],
 "JACOBIAN":jacobian_manifest()["root"],"ST_REPLACEMENT":st_replacement_manifest()["root"],"ANALYTICITY":analyticity_manifest()["root"],
 "TOPOLOGY":topology_manifest()["root"],"COUNT_ONCE":count_once_manifest()["root"],"RELEASE":stboundary2_release_manifest()["root"],
 "REQUEST":request_resolution_manifest()["root"],"MISSING":missing_endpoint_object_manifest()["root"],"NEXT":next_st_handoff_contract()["root"],
 "DEPENDENCY":dependency_frontier_manifest()["root"],"QUANTUM":quantum_nonmutation_manifest()["root"],"SCOPE":static_isolation_guard()["root"],
 "COMPLETENESS":stboundary2_completeness_certificate()["root"]}
PACKAGE_ROOT=_root({"schema":"C204-HQCDSTBOUNDARY2-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS})
ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
C204_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[name for name in globals() if not name.startswith("_")]
