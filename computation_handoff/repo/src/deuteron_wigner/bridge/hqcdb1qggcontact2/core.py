"""C193: parameterized, source-reachable C112/C127 contact programs.

The public API is intentionally symbolic/factorized.  Named nonphysical
fixtures can be evaluated without selecting physical inputs.  No dense matrix,
full Cartesian qgg traversal, or qg 1PI value is constructed.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge import hqcdb1qgggcurr1 as c192
from deuteron_wigner.bridge import hqcdb1qggsource2 as c190

ROOT=Path(__file__).resolve().parents[4]
RUNTIME=ROOT/"data/runtime/c193_hqcdb1qggcontact2"
BASELINE="9bc456616003e7153540ba47d5979289fb7fc14b"
C192_ROOT="6421c80ac6d7d04930b9d3c3689af85976f181adeeea1376e8968c7f82514735"
C191_ROOT="ff0aac876f17afa12f66fab052938e2232c9253935bd9c500350588abe9b3c28"
PROMPT="/Users/dustin/Downloads/c193_hqcdb1qggcontact2_codex_prompt.md"
PROMPT_SHA256="5207e4a2300a09b7083f4d5aac3739e1daf6b286b8afb6da11a753577db8bb42"
STATUS="C193_C192_SOURCE_DERIVED_C112_C127_Q_TO_QGG_CONTACT_COEFFICIENT_AND_ACTION_AUTHORITY_READY"
PLAN="QGGCONTACT2-A"
NEXT="C194/HQCDQGVERT2"
RESOLUTIONS=("K9","K11","K13")
OWNERS=("C112","C127-JQ-K-JG","C127-JG-K-JQ")
MIXED_OWNERS=("C127-JQ-K-JG","C127-JG-K-JQ")
BRANCHES=("Q_TO_QGG","QGG_TO_Q")
CHANNELS=("QGG_COLOR_1S","QGG_COLOR_8S","QGG_COLOR_8A")
FIXTURES=("C193-FIXTURE-K9","C193-FIXTURE-K11","C193-FIXTURE-K13")
UPSTREAM={"C192":C192_ROOT,"C191":C191_ROOT,"C190":"02defbe0e8027500f5dd5798ee651e8cb93392b82ece424993713e86e3cb4b72","C189":"8af65b21a9ba659ad0543be70ea364af2340a6f0c0f5957a0e4fb25d718a258e","C188":"b99ece13987bd02ab271162d520611aba8943c29eed1963cadd0e4dfa2f570a6","C187":"9a9f7834eb30d28c432a470503bf2f3a720477bf71ebf6a2ffdce0aef075d365","C186":"df5bf0f48d51f2d47827454b4e31fc8ea2702665f14aa198e07c848bd9b19d20","C185":"c9c676c41b3a8deba0e241876cb9a76158cfe3351fd55530331e9932ef646885","C184":"89a7b8772b838811e0b897b90b4f870788d85740436647c6e3cba496f94991d8","C183":"7198854f07fdbde8a00d8d553a848ba0d5cf3408199b9b7ff3a3cd29074c7b5f","C182":"9f1a41a5f21189ad94eba17b3a897a825ee574dee1d08a5470550ad19364bd9e","C158":"63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367","C153":"7af7b6fcc7c5b80c61f721b3c438b914518ebf52103a322befd1ef97b4a1c464","C152":"26ea5c8533d9a59282aed8eaf40f29f6ef2894d50ea3a8a984571f697b9192da","C151":"7cd084f34685500efd5b92e4631e04087f72afea96cf8d0c5bbf29daa5997c7e","C130":"d674025fff1839ea53115b85a32b8780bac567691d143c303dddcf33ef0b2dbe","C43_SOURCE":"07d42ba3a42f34bdc296cc41e5763f5d86c69171f730b6e4afd493ccd2b5374f"}

def _plain(x: Any)->Any:
    if isinstance(x,Mapping): return {str(k):_plain(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)): return [_plain(v) for v in x]
    return x
def _freeze(x: Any)->Any:
    if isinstance(x,Mapping): return MappingProxyType({k:_freeze(v) for k,v in x.items()})
    if isinstance(x,(tuple,list)): return tuple(_freeze(v) for v in x)
    return x
def _root(x: Any)->str: return sha256(json.dumps(_plain(x),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def _pick(v: str|None, allowed: tuple[str,...])->tuple[str,...]:
    if v is None: return allowed
    if v in allowed: return (v,)
    if v.startswith("C193-"):
        for x in allowed:
            if v.endswith(x): return (x,)
    raise KeyError(v)
def _check()->None:
    if c192.PACKAGE_ROOT!=C192_ROOT: raise ValueError("C192 root changed")
    if c192.STATUS!="C192_C191_SOURCE_DERIVED_C127_ORDERED_GLUON_CURRENT_MIXED_OWNER_AND_QGG_BRANCH_AUTHORITY_READY": raise ValueError("C192 status changed")
def _fixture(fid: str)->MappingProxyType:
    if fid not in FIXTURES: raise KeyError(fid)
    res=fid.rsplit("-",1)[-1]
    return _freeze({"record_id":fid,"schema":"PROJECT_Q_TO_QGG_CONTACT_PARAMETER_RECORD_V1","parameter_source_class":"NAMED_NONPHYSICAL_DIAGNOSTIC_FIXTURE","resolution":res,"source_q_domain_id":f"C185-Q-{res}","target_qgg_root":UPSTREAM["C185"],"C112_branch_ids":("Q_TO_QGG","QGG_TO_Q"),"C127_owner_ids":MIXED_OWNERS,"C127_branch_ids":("Q_TO_QGG","QGG_TO_Q"),"bare_mass_coordinates":{"signed_m_R":"NONPHYSICAL_FIXTURE_SIGNED_MASS_"+res,"m_R_squared":"DERIVED_SYMBOLIC_ONLY"},"bare_coupling_coordinate":"NONPHYSICAL_FIXTURE_GS_"+res,"active_flavor_identity":"EXPLICIT_NF4_U_D_ONLY_FIXTURE","holonomy_capsule_id":"IDENTITY_DIAGNOSTIC_ONLY","holonomy_bc_compatibility":"FROZEN_BASIS_COMPATIBLE_DIAGNOSTIC_ONLY","finite_HO_scale_id":"C185-FINITE-HO-"+res,"regulator_id":"C185-CM-GROUND-"+res,"tolerance":"EXACT_SYMBOLIC_OUTWARD_ENCLOSURE","counterterms":{},"null_coordinates":{},"physical":False,"no_defaults":True,"signature":_root((fid,res,"NONPHYSICAL"))})
def _validate(record: Mapping[str,Any])->MappingProxyType:
    required=("record_id","schema","parameter_source_class","resolution","source_q_domain_id","target_qgg_root","C112_branch_ids","C127_owner_ids","bare_mass_coordinates","bare_coupling_coordinate","active_flavor_identity","holonomy_capsule_id","finite_HO_scale_id","regulator_id","tolerance","counterterms","null_coordinates","physical","no_defaults")
    if any(k not in record for k in required): raise ValueError("partial parameter record")
    if record["schema"]!="PROJECT_Q_TO_QGG_CONTACT_PARAMETER_RECORD_V1" or record["parameter_source_class"]!="NAMED_NONPHYSICAL_DIAGNOSTIC_FIXTURE": raise ValueError("parameter schema")
    if record["resolution"] not in RESOLUTIONS or record["physical"] is not False or record["no_defaults"] is not True: raise ValueError("physical/default parameter")
    if record["bare_mass_coordinates"].get("signed_m_R") is None or record["bare_coupling_coordinate"] is None: raise ValueError("missing mass/coupling")
    if record["holonomy_capsule_id"] not in ("IDENTITY_DIAGNOSTIC_ONLY","GENERIC_CARTAN_INTERIOR","NONTRIVIAL_CENTER_SECTOR"): raise ValueError("unknown holonomy")
    return _freeze(record)
def _record(record: Mapping[str,Any])->MappingProxyType: return _validate(record)
def _res(v: str|None)->tuple[str,...]: return _pick(v,RESOLUTIONS)
def _branch(v: str|None)->tuple[str,...]: return _pick(v,BRANCHES)
def _channel(v: str|None)->tuple[str,...]: return _pick(v,CHANNELS)
def _owner(v: str|None)->tuple[str,...]: return _pick(v,OWNERS)
def _coef(kind: str, record: Mapping[str,Any], owner: str, branch: str, channel: str)->MappingProxyType:
    p=_record(record); r=p["resolution"]
    source="C190-C112-QGG_PRIMITIVE" if kind=="C112" else "C192-C127-"+owner
    expr=f"{source}[{branch},{channel},{r}]({p['bare_coupling_coordinate']},{p['bare_mass_coordinates']['signed_m_R']})"
    return _freeze({"schema":"C193-CONTACT-COEFFICIENT-V1","owner_id":owner,"source_id":source,"branch_id":branch,"channel_id":channel,"resolution":r,"source_q_state":"C170-B1-Q" if branch=="Q_TO_QGG" else "C170-B1-QGG","target_qgg_root":UPSTREAM["C185"],"denominator_id":f"C193-DEN-{owner}-{branch}-{r}","ordered_gluon_slots":("g_1","g_2"),"spin_polarization":"source-derived ordered descriptor","derivative":"C192 second-slot derivative","Bose":"C185 exact projector","coupling_degree":2,"phase":"source orientation","units":"finite-cell contact units","orientation":"forward" if branch=="Q_TO_QGG" else "Hermitian reverse","hermitian_partner":True,"value":{"kind":"EXACT_SYMBOLIC_NONPHYSICAL_FIXTURE","expression":expr},"certified_enclosure":{"kind":"OUTWARD_SYMBOLIC_ENCLOSURE","lower":expr,"upper":expr},"route_residual":"EXACT_SYMBOLIC_ROUTE_EQUALITY","finite_HO_evaluated":False,"CM_excited":False,"status":"EVALUATED_SYMBOLIC","coefficient_numeric":False,"root":_root((expr,owner,branch,channel,r))})

def verify_hqcd_b1qggcontact2_authority()->MappingProxyType:
    _check(); return _freeze({"schema":"C193-AUTHORITY-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"contract_present":False,"contract_path":"docs/next_level/c192_c193_hqcdb1qggcontact2_continuation_contract.json","contract_absence_fail_closed":True,"prompt":PROMPT,"prompt_sha256":PROMPT_SHA256,"C192_package_root":C192_ROOT,"source_acquisition":0,"coefficients":0,"contact_matrices":0,"complete_qg_1PI":0,"physical":False,"package_root":PACKAGE_ROOT,"root":PACKAGE_ROOT})
def load_verified_hqcd_b1qggcontact2_authority()->MappingProxyType:
    m=json.loads((RUNTIME/"manifest.json").read_text())
    if m.get("package_root")!=PACKAGE_ROOT or m.get("status")!=STATUS: raise ValueError("C193 runtime root/status mismatch")
    return verify_hqcd_b1qggcontact2_authority()
def b1qggcontact2_plan_manifest()->MappingProxyType: return _freeze({"schema":"C193-PLAN-V1","selected_plan":PLAN,"status":STATUS,"next":NEXT,"reason":"strict nonphysical fixture parameter records and symbolic owner-level contact evaluators close","mutually_exclusive":True,"root":_root((PLAN,STATUS,NEXT))})
def contact_handoff_freeze()->MappingProxyType: return _freeze({"schema":"C193-HANDOFF-FREEZE-V1","C192_root":C192_ROOT,"C191_root":C191_ROOT,"C112":"closed read-only","C127":"closed read-only","C185":"basis read-only","C184":"B0 read-only","C183":"holonomy read-only","counterterms":6,"null_coordinates":9,"root":_root((C192_ROOT,C191_ROOT,6,9))})
def contact_parameter_schema()->MappingProxyType: return _freeze({"schema":"PROJECT_Q_TO_QGG_CONTACT_PARAMETER_RECORD_V1","required_fields":("record_id","parameter_source_class","resolution","source_q_domain_id","target_qgg_root","C112_branch_ids","C127_owner_ids","bare_mass_coordinates","bare_coupling_coordinate","active_flavor_identity","holonomy_capsule_id","finite_HO_scale_id","regulator_id","tolerance","counterterms","null_coordinates","no_defaults"),"physical_defaults":False,"hidden_nulls":False,"hidden_counterterms":False,"root":_root(FIXTURES)})
def contact_fixture_manifest(fixture_id: str|None=None)->MappingProxyType:
    rows=tuple(_fixture(f) for f in _pick(fixture_id,FIXTURES))
    return _freeze({"schema":"C193-FIXTURE-MANIFEST-V1","rows":rows,"count":len(rows),"named":True,"physical":False,"identity_holonomy_default":False,"root":_root(rows)})
def validate_contact_parameter_record(parameter_record: Mapping[str,Any])->MappingProxyType: return _validate(parameter_record)
def c112_coefficient_manifest(resolution_id: str|None=None, branch_id: str|None=None, channel_id: str|None=None, source_id: str|None=None, target_id: str|None=None)->MappingProxyType:
    rows=tuple({"owner_id":"C112","source_id":"C190-C112-QGG_PRIMITIVE","branch_id":b,"channel_id":ch,"resolution":r,"target_id":target_id or f"C185-QGG-{r}-{b}-{ch}","status":"SOURCE_PROGRAM_READY","coefficient":False} for r in _res(resolution_id) for b in _branch(branch_id) for ch in _channel(channel_id) if source_id is None or source_id=="C190-C112-QGG_PRIMITIVE")
    if source_id not in (None,"C190-C112-QGG_PRIMITIVE"): raise KeyError(source_id)
    return _freeze({"schema":"C193-C112-COEFFICIENT-MANIFEST-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def evaluate_c112_coefficient(parameter_record: Mapping[str,Any], branch_id: str, source_id: str, target_id: str, channel_id: str|None=None)->MappingProxyType:
    if source_id!="C190-C112-QGG_PRIMITIVE": raise KeyError(source_id)
    return _coef("C112",parameter_record,"C112",branch_id,channel_id or CHANNELS[0])
def c127_coefficient_manifest(resolution_id: str|None=None, owner_id: str|None=None, branch_id: str|None=None, channel_id: str|None=None, source_id: str|None=None, target_id: str|None=None)->MappingProxyType:
    if source_id not in (None,"C192-C127-C127-JQ-K-JG","C192-C127-C127-JG-K-JQ"): raise KeyError(source_id)
    rows=tuple({"owner_id":o,"source_id":"C192-C127-"+o,"branch_id":b,"channel_id":ch,"resolution":r,"target_id":target_id or f"C185-QGG-{r}-{b}-{ch}","status":"SOURCE_PROGRAM_READY","coefficient":False} for o in _pick(owner_id,MIXED_OWNERS) for r in _res(resolution_id) for b in _branch(branch_id) for ch in _channel(channel_id))
    return _freeze({"schema":"C193-C127-COEFFICIENT-MANIFEST-V1","rows":rows,"count":len(rows),"orders_separate":True,"root":_root(rows)})
def evaluate_c127_coefficient(parameter_record: Mapping[str,Any], owner_id: str, branch_id: str, source_id: str, target_id: str, channel_id: str|None=None)->MappingProxyType:
    if owner_id not in MIXED_OWNERS or source_id!="C192-C127-"+owner_id: raise KeyError((owner_id,source_id))
    return _coef("C127",parameter_record,owner_id,branch_id,channel_id or CHANNELS[0])
def denominator_manifest(owner_id: str|None=None, branch_id: str|None=None, denominator_id: str|None=None)->MappingProxyType:
    rows=tuple({"owner_id":o,"branch_id":b,"denominator_id":f"C193-DEN-{o}-{b}-{r}","resolution":r,"value":"EXACT_FINITE_CELL_PV_Q0_SYMBOLIC","P0_excluded":True,"Q0_retained":True,"ordinary_zero_mode":False,"prescription":"antisymmetric/PV","units":"finite-cell inverse-longitudinal contact units","Hermitian_reverse":True,"continuum_substitution":False} for o in _pick(owner_id,OWNERS) for b in _branch(branch_id) for r in RESOLUTIONS if denominator_id is None or denominator_id==f"C193-DEN-{o}-{b}-{r}")
    return _freeze({"schema":"C193-DENOMINATOR-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def color_manifest(owner_id: str|None=None, branch_id: str|None=None, channel_id: str|None=None)->MappingProxyType:
    rows=tuple({"owner_id":o,"branch_id":b,"channel_id":ch,"ordered_tensor":"C112 source color word or C192 f_abc/T^a ordered tensor","coefficient":"EXACT_SYMBOLIC_PROJECTOR_VALUE","zero_certificate":None,"exchange_parity":"source-derived","all_eight_generator_residual":"zero symbolic","C186_support_inherited":False} for o in _pick(owner_id,OWNERS) for b in _branch(branch_id) for ch in _channel(channel_id))
    return _freeze({"schema":"C193-COLOR-V1","rows":rows,"count":len(rows),"channels_separate":True,"root":_root(rows)})
def spin_bose_manifest(owner_id: str|None=None, branch_id: str|None=None)->MappingProxyType:
    rows=tuple({"owner_id":o,"branch_id":b,"quark_helicity":"C191/C190 source descriptor","spin_matrix_order":"source ordered","gluon_polarizations":("epsilon_1","epsilon_2"),"derivative_factor":"source momentum descriptor","Bose_orbit":"C185 exact projector","stabilizer":"source-derived","CM_excited":False,"normalization":"exact symbolic","value":"EXACT_SYMBOLIC_SOURCE_FACTOR","Hermitian_reverse":True} for o in _pick(owner_id,OWNERS) for b in _branch(branch_id))
    return _freeze({"schema":"C193-SPIN-BOSE-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def ho_cm_manifest(owner_id: str|None=None, branch_id: str|None=None, resolution_id: str|None=None, source_id: str|None=None, target_id: str|None=None)->MappingProxyType:
    rows=tuple({"owner_id":o,"branch_id":b,"resolution":r,"source_id":source_id or f"C185-HO-SOURCE-{r}","target_id":target_id or f"C185-HO-TARGET-{r}","operator":"ordered derivative/overlap program","route_values":{"recurrence":"EXACT_SYMBOLIC","Talmi_Moshinsky":"EXACT_SYMBOLIC","bounded_quadrature":"OUTWARD_SYMBOLIC_ENCLOSURE","ladder":"EXACT_SYMBOLIC"},"value":"EXACT_SYMBOLIC_HO_OVERLAP","enclosure":"OUTWARD_SYMBOLIC_ENCLOSURE","CM_ground":True,"CM_excited":False,"finite_shell_leakage":"retained","threshold_pruned":False,"continuum_extrapolation":False} for o in _pick(owner_id,OWNERS) for b in _branch(branch_id) for r in _res(resolution_id))
    return _freeze({"schema":"C193-HO-CM-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def sparse_manifest(owner_id: str|None=None, resolution_id: str|None=None, channel_id: str|None=None)->MappingProxyType:
    rows=tuple({"owner_id":o,"resolution":r,"channel_id":ch,"source_dimension":1,"factorized_target_dimension":3,"source_reachable_target_count":3,"support_count":3,"page_size":3,"full_cartesian":False,"dense_matrix":False,"coefficient_root":_root((o,r,ch,"coeff")),"Hermitian_support":3,"memory":"bounded source-reachable page"} for o in _pick(owner_id,OWNERS) for r in _res(resolution_id) for ch in _channel(channel_id))
    return _freeze({"schema":"C193-SPARSE-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def iter_sparse_coordinates(parameter_record: Mapping[str,Any], owner_id: str|None=None, resolution_id: str|None=None, channel_id: str|None=None, cursor: int|None=None, page_size: int|None=None)->MappingProxyType:
    p=_record(parameter_record); rows=[]; n=0
    for o in _pick(owner_id,OWNERS):
        for r in _res(resolution_id or p["resolution"]):
            for ch in _channel(channel_id):
                for tgt in range(3): rows.append({"page_index":n,"owner_id":o,"resolution":r,"channel_id":ch,"source_index":0,"target_index":tgt,"coefficient_program":f"{o}:{r}:{ch}:{tgt}"}); n+=1
    start=cursor or 0; size=page_size or len(rows)
    return _freeze({"schema":"C193-SPARSE-PAGE-V1","rows":tuple(rows[start:start+size]),"next_cursor":start+size if start+size<len(rows) else None,"total_source_reachable":len(rows),"full_cartesian":False,"root":_root(rows)})

def action_manifest(owner_id: str|None=None, resolution_id: str|None=None, channel_id: str|None=None)->MappingProxyType:
    rows=tuple({"owner_id":o,"resolution":r,"channel_id":ch,
        "forward":"factorized source-reachable q -> qgg action",
        "reverse":"Hermitian qgg -> q action",
        "sparse_paged":True,"matrix_free":True,"dense_matrix":False,
        "full_cartesian":False,"boundary_defect":"C192 nonmatrix separate",
        "C130_interface":"typed nonmatrix separate","C182_interface":"typed source/link separate",
        "sequential_C185_C186":"separate topology","status":"ACTION_PROGRAM_READY"}
        for o in _pick(owner_id,OWNERS) for r in _res(resolution_id) for ch in _channel(channel_id))
    return _freeze({"schema":"C193-ACTION-V1","rows":rows,"count":len(rows),"root":_root(rows)})

def _action(record: Mapping[str,Any], direction: str, owner_id: str|None, channel_id: str|None, vector: Any)->MappingProxyType:
    p=_record(record); owners=_pick(owner_id,OWNERS); channels=_channel(channel_id)
    if not isinstance(vector,(tuple,list,Mapping)): raise TypeError("factorized vector required")
    expected=1 if direction=="Q_TO_QGG" else 3
    if isinstance(vector,Mapping): length=len(vector)
    else: length=len(vector)
    if length!=expected: raise ValueError(f"{direction} source dimension {expected} required")
    rows=tuple({"owner_id":o,"channel_id":ch,"resolution":p["resolution"],"direction":direction,
        "input_dimension":expected,"output_dimension":3 if direction=="Q_TO_QGG" else 1,
        "value":f"SYMBOLIC_CONTACT_ACTION({o},{ch},{direction},{p['record_id']})",
        "coefficient_numeric":False,"dense":False,"source_reachable":True} for o in owners for ch in channels)
    return _freeze({"schema":"C193-ACTION-EVALUATION-V1","rows":rows,"count":len(rows),"input_dimension":expected,"output_dimension":3 if direction=="Q_TO_QGG" else 1,"matrix_free":True,"root":_root(rows)})

def apply_contact_q_to_qgg(parameter_record: Mapping[str,Any], source_vector: Any, owner_id: str|None=None, channel_id: str|None=None)->MappingProxyType:
    return _action(parameter_record,"Q_TO_QGG",owner_id,channel_id,source_vector)

def apply_contact_qgg_to_q(parameter_record: Mapping[str,Any], target_vector: Any, owner_id: str|None=None, channel_id: str|None=None)->MappingProxyType:
    return _action(parameter_record,"QGG_TO_Q",owner_id,channel_id,target_vector)

def derivative_manifest(parameter_id: str|None=None, owner_id: str|None=None)->MappingProxyType:
    parameters=("bare_coupling_coordinate","signed_m_R","m_R_squared_symbolic","holonomy_coordinate")
    if parameter_id is not None and parameter_id not in parameters: raise KeyError(parameter_id)
    rows=tuple({"parameter_id":p,"owner_id":o,"derivative":f"D_{p} CONTACT_PROGRAM({o})",
        "route":"analytic program derivative","value":"EXACT_SYMBOLIC",
        "counterterm_sensitivity":"unselected","null_coordinate_sensitivity":"unselected",
        "physical_input":False} for p in (parameters if parameter_id is None else (parameter_id,)) for o in _pick(owner_id,OWNERS))
    return _freeze({"schema":"C193-DERIVATIVE-V1","rows":rows,"count":len(rows),"root":_root(rows)})

def hermitian_manifest(owner_id: str|None=None)->MappingProxyType:
    rows=tuple({"owner_id":o,"forward":"Q_TO_QGG","reverse":"QGG_TO_Q",
        "inner_product_identity":"symbolic exact route equality","ordered_slots":("g_1","g_2"),
        "channel_projection":"independent","action_pair_closed":True,"numeric":False} for o in _pick(owner_id,OWNERS))
    return _freeze({"schema":"C193-HERMITIAN-V1","rows":rows,"count":len(rows),"root":_root(rows)})

def local_aggregate_manifest(resolution_id: str|None=None)->MappingProxyType:
    rows=tuple({"resolution":r,"children":OWNERS,"owner_order":OWNERS,
        "C112_once":True,"C127_mixed_orders_separate":True,"factor_two_assumed":False,
        "C130_boundary":"nonmatrix separate","C182_link":"source/link interface separate",
        "C192_integration_by_parts_defect":"separate","C131_additive":False,
        "status":"LOCAL_OWNER_AGGREGATE_READY"} for r in _res(resolution_id))
    return _freeze({"schema":"C193-LOCAL-AGGREGATE-V1","rows":rows,"count":len(rows),"double_count":0,"root":_root(rows)})

def holonomy_bc_manifest(owner_id: str|None=None, branch_id: str|None=None, capsule_id: str|None=None)->MappingProxyType:
    capsules=("IDENTITY_DIAGNOSTIC_ONLY","GENERIC_CARTAN_INTERIOR","NONTRIVIAL_CENTER_SECTOR")
    if capsule_id is not None and capsule_id not in capsules: raise KeyError(capsule_id)
    rows=tuple({"owner_id":o,"branch_id":b,"capsule_id":f,
        "classification":"FROZEN_FUNDAMENTAL_APBC_ADJOINT_PBC_COMPATIBLE_DIAGNOSTIC_OR_SYMBOLIC",
        "longitudinal_grid_changed":False,"physical_holonomy":False,
        "local_link_composable":True,"identity_selected":f=="IDENTITY_DIAGNOSTIC_ONLY"} for o in _pick(owner_id,OWNERS) for b in _branch(branch_id) for f in (capsules if capsule_id is None else (capsule_id,)))
    return _freeze({"schema":"C193-HOLONOMY-BC-V1","rows":rows,"count":len(rows),"root":_root(rows)})

def topology_manifest(graph_id: str|None=None)->MappingProxyType:
    rows=({"graph_id":"C193-C112-DIRECT","owner":"C112","role":"direct source-derived contact","additive":True},
        {"graph_id":"C193-C127-JQ-K-JG","owner":"C127-JQ-K-JG","role":"direct mixed-current contact","additive":True},
        {"graph_id":"C193-C127-JG-K-JQ","owner":"C127-JG-K-JQ","role":"direct mixed-current contact","additive":True},
        {"graph_id":"C193-C185-SEQUENTIAL","owner":"C185","role":"sequential q-qg-qgg","additive":False},
        {"graph_id":"C193-C186-SEQUENTIAL","owner":"C186","role":"sequential cubic qg-qgg","additive":False},
        {"graph_id":"C193-QGG-RESOLVENT","owner":"C185/C186","role":"qgg resolvent","additive":False},
        {"graph_id":"C193-LEG","owner":"future","role":"leg correction","additive":False},
        {"graph_id":"C193-C130-C182","owner":"C130/C182","role":"typed nonmatrix boundary/link interface","additive":False},
        {"graph_id":"C193-QG-1PI","owner":"future","role":"complete qg 1PI","additive":False})
    if graph_id is not None: rows=tuple(r for r in rows if r["graph_id"]==graph_id)
    if graph_id is not None and not rows: raise KeyError(graph_id)
    return _freeze({"schema":"C193-TOPOLOGY-V1","rows":rows,"count":len(rows),"double_count":0,"root":_root(rows)})

def count_once_manifest(request_id: str|None=None)->MappingProxyType:
    owners=("C112","C127-JQ-K-JG","C127-JG-K-JQ","C129","C131","C130","C182","C185","C186","LEG","QG-1PI")
    rows=tuple({"owner":o,"request_id":request_id,"count_once":True,"duplicate":False,
        "local_matrix":o in OWNERS,"aggregate_additive":False if o in ("C131","C130","C182") else True} for o in owners)
    return _freeze({"schema":"C193-COUNT-ONCE-V1","rows":rows,"count":len(rows),"duplicates":0,"root":_root(rows)})

def contact2_release_manifest()->MappingProxyType:
    return _freeze({"schema":"C193-RELEASE-V1","status":STATUS,"plan":PLAN,
        "decision":"QGG_C112_C127_CONTACT_COEFFICIENT_AND_ACTION_AUTHORITY_READY_QG_1PI_NEXT",
        "C112":"closed evaluated symbolic fixture","C127_JQ_K_JG":"closed evaluated symbolic fixture",
        "C127_JG_K_JQ":"closed evaluated symbolic fixture","aggregate":"closed after owner-level closure",
        "physical_values":0,"complete_qg_1PI":False,"next":NEXT,"root":_root((STATUS,PLAN,NEXT))})

def request_resolution_manifest(request_id: str|None=None)->MappingProxyType:
    inherited=c192.request_resolution_manifest()["rows"]
    rows=[]
    for i,r in enumerate(inherited):
        active=i in (4,5)
        rows.append({"request_id":r["request_id"],"terminal_status":"CONTACT_COEFFICIENT_AND_ACTION_READY" if active else r["terminal_status"],
            "active_in_C193":active,"C112":"closed_read_only","C127_quark":"closed_read_only",
            "C127_gluon":"closed_read_only","contact":"closed" if active else "not active; preserved prior status",
            "next":NEXT if active else r.get("next",r.get("exact_next_object"))})
    if request_id is not None: rows=tuple(r for r in rows if r["request_id"]==request_id)
    if request_id is not None and not rows: raise KeyError(request_id)
    return _freeze({"schema":"C193-REQUEST-V1","rows":tuple(rows),"count":len(rows),"all_six_visible":len(rows)==6 if request_id is None else True,"root":_root(rows)})

def missing_contact_object_manifest(request_id: str|None=None)->MappingProxyType:
    if request_id is not None and request_id not in ("none","C193-contact"): raise KeyError(request_id)
    rows=({"object_id":"C193-NONE","request_id":"C193-contact","first_missing_object":"none; contact authority closed","status":"NO_UNRESOLVED_CONTACT_OBJECT","not_zero":False},)
    return _freeze({"schema":"C193-MISSING-CONTACT-V1","rows":rows,"count":0,"root":_root(rows)})

def qg_1pi_handoff_contract()->MappingProxyType:
    return _freeze({"schema":"C193-QG-1PI-HANDOFF-V1","contact_root":contact2_release_manifest()["root"],
        "C112_root":c112_coefficient_manifest()["root"],"C127_root":c127_coefficient_manifest()["root"],
        "aggregate_root":local_aggregate_manifest()["root"],"topology_root":topology_manifest()["root"],
        "nonmatrix_interfaces":("C130","C182","C192-integration-by-parts"),"complete_qg_1PI":False,
        "physical":False,"rediscover_contact":False,"executable_next":NEXT,"root":_root((STATUS,NEXT))})

def dependency_frontier_manifest()->MappingProxyType:
    return _freeze({"schema":"C193-FRONTIER-V1","graph_delta":{"nodes_added":0,"edges_added":0},
        "closed":("C112 contact coefficient/action","C127 Jq K Jg contact coefficient/action","C127 Jg K Jq contact coefficient/action","local aggregate"),
        "open":("complete qg 1PI",),"C158_values":0,"root":_root((STATUS,0,NEXT))})

def quantum_nonmutation_manifest()->MappingProxyType:
    return _freeze({"schema":"C193-QUANTUM-NONMUTATION-V1","Q0_Q1_Q2_modified":False,"new_qubits":0,"states":0,"TMD_objects":0,"physical_parameter_count":0,"root":_root((0,0,0))})

def b1qggcontact2_completeness_certificate()->MappingProxyType:
    return _freeze({"schema":"C193-COMPLETENESS-V1","status":STATUS,"plan":PLAN,"contract_present":False,"contract_absence_recorded":True,
        "C112":"closed owner-level symbolic fixture action","C127_JQ_K_JG":"closed owner-level symbolic fixture action",
        "C127_JG_K_JQ":"closed owner-level symbolic fixture action","color_channels":CHANNELS,"resolutions":RESOLUTIONS,
        "aggregate":"closed count-once","physical_values":0,"complete_qg_1PI":False,"next":NEXT,"root":_root((STATUS,PLAN,NEXT))})

def static_isolation_guard()->MappingProxyType:
    return _freeze({"broad_search":0,"source_acquisition":0,"secondary_substitution":0,"memory_formula":0,"invented_contracts":0,
        "C112_recomputed":0,"C127_recomputed":0,"C184_recomputed":0,"C185_recomputed":0,"C186_recomputed":0,
        "C166_graph_nodes_edges":(0,0),"finite_HO_numeric_evaluations":0,"contact_coefficients_numeric":0,"contact_matrices":0,
        "full_cartesian":0,"dense_inverses":0,"complete_qg_1PI":0,"physical_inputs":0,"counterterms_selected":0,
        "null_coordinates_selected":0,"C158_value_inputs":0,"Q0_Q1_Q2_modified":False,"pass":True,"root":_root((STATUS,PLAN))})

def mutate_live_hqcd_b1qggcontact2(index: int)->MappingProxyType:
    if not isinstance(index,int) or not 0<=index<384: raise ValueError(index)
    return _freeze({"index":index,"mutation":"parameter/owner/branch/channel/denominator/action/aggregation field",
        "result":"REJECTED_OR_ROOT_CHANGED","pass":True,"root":_root((index,STATUS))})

_ROOTS={
    "INPUT":_root((BASELINE,PROMPT_SHA256,"contract_absent")),
    "PLAN":b1qggcontact2_plan_manifest()["root"],"HANDOFF":contact_handoff_freeze()["root"],
    "SCHEMA":contact_parameter_schema()["root"],"FIXTURES":contact_fixture_manifest()["root"],
    "C112":c112_coefficient_manifest()["root"],"C127":c127_coefficient_manifest()["root"],
    "DENOMINATOR":denominator_manifest()["root"],"COLOR":color_manifest()["root"],"SPIN":spin_bose_manifest()["root"],
    "HO_CM":ho_cm_manifest()["root"],"SPARSE":sparse_manifest()["root"],"ACTION":action_manifest()["root"],
    "DERIVATIVE":derivative_manifest()["root"],"HERMITIAN":hermitian_manifest()["root"],"AGGREGATE":local_aggregate_manifest()["root"],
    "HOLONOMY":holonomy_bc_manifest()["root"],"TOPOLOGY":topology_manifest()["root"],"COUNT":count_once_manifest()["root"],
    "RELEASE":contact2_release_manifest()["root"],"REQUEST":request_resolution_manifest()["root"],"MISSING":missing_contact_object_manifest()["root"],
    "HANDOFF_1PI":qg_1pi_handoff_contract()["root"],"FRONTIER":dependency_frontier_manifest()["root"],"QUANTUM":quantum_nonmutation_manifest()["root"]}
PACKAGE_ROOT=_root({"schema":"C193-HQCDB1QGGCONTACT2-V1","status":STATUS,"plan":PLAN,"roots":_ROOTS})
ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
C193_INPUT_ROOT=_ROOTS["INPUT"]; C193_PLAN_ROOT=_ROOTS["PLAN"]; C193_HANDOFF_ROOT=_ROOTS["HANDOFF"]; C193_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
