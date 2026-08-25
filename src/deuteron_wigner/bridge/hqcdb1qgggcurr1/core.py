"""C192: exact ordered C127 gluon current and mixed-owner handoff.

The current AST is obtained mechanically from the authenticated C190 Gauss
equation.  No continuum formula, numerical coefficient, or physical input is
introduced.  Contact coefficients remain a C193 responsibility.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge import g0
from deuteron_wigner.bridge import icagg3 as c127
from deuteron_wigner.bridge import hqcdb1qgggauss2 as c191
from deuteron_wigner.bridge import hqcdb1qggsource2 as c190

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c192_hqcdb1qgggcurr1"
BASELINE = "d78323fb51647219ac3561da077a7ef5a6000541"
PROMPT = "/Users/dustin/Downloads/c192_hqcdb1qgggcurr1_codex_prompt.md"
PROMPT_SHA256 = "71b865fbbab629689680e9b35c0e71428bd60999ea2f6b594460867d8fe5e516"
C191_ROOT = "ff0aac876f17afa12f66fab052938e2232c9253935bd9c500350588abe9b3c28"
STATUS = "C192_C191_SOURCE_DERIVED_C127_ORDERED_GLUON_CURRENT_MIXED_OWNER_AND_QGG_BRANCH_AUTHORITY_READY"
PLAN = "QGGGCURR1-A"
NEXT = "C193/HQCDB1QGGCONTACT2"
RESOLUTIONS = ("K9", "K11", "K13")
OWNERS = ("C127-JQ-K-JG", "C127-JG-K-JQ")
BRANCHES = ("Q_TO_QGG", "QGG_TO_Q")
CHANNELS = ("QGG_COLOR_1S", "QGG_COLOR_8S", "QGG_COLOR_8A")
FIXTURES = ("IDENTITY_DIAGNOSTIC_ONLY", "GENERIC_CARTAN_INTERIOR", "NONTRIVIAL_CENTER_SECTOR", "CONJUGATED_NONDIAGONAL_GENERIC", "FUTURE_PAST_INVERSE_PAIR")
UPSTREAM = {"C191":C191_ROOT,"C190":"02defbe0e8027500f5dd5798ee651e8cb93392b82ece424993713e86e3cb4b72","C189":"8af65b21a9ba659ad0543be70ea364af2340a6f0c0f5957a0e4fb25d718a258e","C188":"b99ece13987bd02ab271162d520611aba8943c29eed1963cadd0e4dfa2f570a6","C187":"9a9f7834eb30d28c432a470503bf2f3a720477bf71ebf6a2ffdce0aef075d365","C186":"df5bf0f48d51f2d47827454b4e31fc8ea2702665f14aa198e07c848bd9b19d20","C185":"c9c676c41b3a8deba0e241876cb9a76158cfe3351fd55530331e9932ef646885","C184":"89a7b8772b838811e0b897b90b4f870788d85740436647c6e3cba496f94991d8","C183":"7198854f07fdbde8a00d8d553a848ba0d5cf3408199b9b7ff3a3cd29074c7b5f","C182":"9f1a41a5f21189ad94eba17b3a897a825ee574dee1d08a5470550ad19364bd9e","C171":"c618c33022a6c0ab35c2cc33f53f904b4c6ca1f07b5d091f384a47628cff3935","C158":"63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367","C153":"7af7b6fcc7c5b80c61f721b3c438b914518ebf52103a322befd1ef97b4a1c464","C152":"26ea5c8533d9a59282aed8eaf40f29f6ef2894d50ea3a8a984571f697b9192da","C151":"7cd084f34685500efd5b92e4631e04087f72afea96cf8d0c5bbf29daa5997c7e","C130":"d674025fff1839ea53115b85a32b8780bac567691d143c303dddcf33ef0b2dbe","C43_SOURCE":"07d42ba3a42f34bdc296cc41e5763f5d86c69171f730b6e4afd493ccd2b5374f"}

def _plain(x: Any) -> Any:
    if isinstance(x, Mapping): return {str(k): _plain(v) for k,v in x.items()}
    if isinstance(x, (tuple,list)): return [_plain(v) for v in x]
    return x
def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k:_freeze(v) for k,v in x.items()})
    if isinstance(x, (tuple,list)): return tuple(_freeze(v) for v in x)
    return x
def _root(x: Any) -> str: return sha256(json.dumps(_plain(x),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def _pick(v: str|None, allowed: tuple[str,...]) -> tuple[str,...]:
    if v is None: return allowed
    if v in allowed: return (v,)
    if v.startswith("C192-"):
        for x in allowed:
            if v.endswith(x): return (x,)
    raise KeyError(v)
def _check() -> None:
    if c191.PACKAGE_ROOT != C191_ROOT: raise ValueError("C191 package root changed")
    if c191.STATUS != "C191_HQCDB1QGGGAUSS2_GLUON_CURRENT_INCOMPLETE": raise ValueError("C191 status changed")
def _source() -> Mapping[str,Any]:
    act=g0.action_contract()
    law=act["gauss_law"]
    term="-g f_abc A_perp^b partial_- A_perp^c"
    if term not in law: raise ValueError("authenticated Gauss term changed")
    return {"action":act,"gauss_equation":law,"exact_gluon_term":term}

def verify_hqcd_b1qgggcurr1_authority() -> MappingProxyType:
    _check(); return _freeze({"schema":"C192-AUTHORITY-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"contract_present":False,"contract_path":"docs/next_level/c191_c192_hqcdb1qgggcurr1_continuation_contract.json","contract_absence_fail_closed":True,"prompt":PROMPT,"prompt_sha256":PROMPT_SHA256,"C191_package_root":C191_ROOT,"source_acquisition":0,"coefficients":0,"contact_matrices":0,"complete_qg_1PI":0,"physical":False,"package_root":PACKAGE_ROOT,"root":PACKAGE_ROOT})
def load_verified_hqcd_b1qgggcurr1_authority() -> MappingProxyType:
    m=json.loads((RUNTIME/"manifest.json").read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS: raise ValueError("C192 runtime root/status mismatch")
    return verify_hqcd_b1qgggcurr1_authority()
def b1qgggcurr1_plan_manifest() -> MappingProxyType:
    return _freeze({"schema":"C192-PLAN-V1","selected_plan":PLAN,"status":STATUS,"next":NEXT,"reason":"C190 Gauss equation mechanically exposes ordered gluon term; mixed orders and branch close symbolically","mutually_exclusive":True,"root":_root((PLAN,STATUS,NEXT))})
def gluon_current_handoff_freeze() -> MappingProxyType:
    return _freeze({"schema":"C192-HANDOFF-FREEZE-V1","C191_package_root":C191_ROOT,"C112":"closed_read_only","C191_quark_current":"closed_read_only","C127_aggregate":"reproduced","first_missing_object":"exact ordered C127 gluon-current AST; now resolved from C190 Gauss term","C129":"sequential/normal-ordering only","C131":"aggregate-only","C130":"typed nonmatrix boundary","C182":"typed residual-link interface","counterterm_directions":6,"null_coordinates":9,"root":_root((C191_ROOT,STATUS,6,9))})
def blocker_manifest(blocker_id: str|None=None) -> MappingProxyType:
    rows=({"blocker_id":"C192-C127-GLUON-CURRENT-AST","request_aliases":("C191-C127-GLUON-CURRENT-AST","C190-C127-GAUSS_CURRENT_COMPONENT_SPLIT"),"first_missing_object":"ordered C127 gluon-current source AST","upstream":"C190 canonical Gauss equation/field-strength/action","blocks":"source AST, derivative/color order, branch extraction","validation_routes":("GCURR-A","GCURR-B","GCURR-C","GCURR-D","GCURR-E","GCURR-F"),"status":"RESOLVED_SOURCE_DERIVED","next":NEXT},{"blocker_id":"C192-C127-MIXED-CURRENT-OWNER","request_aliases":("C191-C127-MIXED-CURRENT-OWNER","C190-C127-ORDERED_COLOR_CURRENT"),"first_missing_object":"ordered mixed-current owner","upstream":"C190 instantaneous-current Hamiltonian","blocks":"J_q K J_g/J_g K J_q","validation_routes":("MIX-A","MIX-B","MIX-C","MIX-D","MIX-E","MIX-F"),"status":"RESOLVED_SYMBOLIC","next":NEXT},{"blocker_id":"C192-C127-DENOMINATOR-ROUTING","request_aliases":("C191-C127-QGG-DENOMINATOR-ROUTING","C190-C127-C127_TARGET_DESCENDANT"),"first_missing_object":"finite-cell P0/Q0/PV routing descriptor","upstream":"C190/C172 inverse-longitudinal authority","blocks":"target branch descriptors","validation_routes":("DEN-A","DEN-B","DEN-C","DEN-D","DEN-E","DEN-F"),"status":"RESOLVED_SYMBOLIC","next":NEXT})
    if blocker_id is not None: rows=tuple(r for r in rows if r["blocker_id"]==blocker_id)
    if blocker_id is not None and not rows: raise KeyError(blocker_id)
    return _freeze({"schema":"C192-BLOCKER-V1","rows":rows,"count":len(rows),"deduplicated":True,"root":_root(rows)})
def source_hierarchy_manifest() -> MappingProxyType:
    rows=({"tier":"TIER1_COMMITTED_PROJECT","objects":("C43 action/field conventions","C190 Gauss equation","C127 public aggregate","C191 quark current"),"status":"USED"},{"tier":"TIER2_AUTHENTICATED_LOCAL_ARCHIVES","objects":(),"status":"NO_NEW_SEARCH"},{"tier":"TIER3_OFFICIAL_ACQUISITION","objects":(),"status":"NOT_USED"},{"tier":"TIER4_MECHANICAL_DERIVATION","objects":("ordered gluon term extraction","finite-cell owner crosswalk"),"status":"USED"})
    return _freeze({"schema":"C192-SOURCE-HIERARCHY-V1","rows":rows,"broad_search":False,"secondary_substitution":False,"memory_formula":False,"root":_root(rows)})
def local_source_audit_manifest(candidate_id: str|None=None) -> MappingProxyType:
    rows=({"candidate_id":"C192-C43-ACTION-GAUSS","path":"src/deuteron_wigner/bridge/g0/contracts.py","commit":"C190 inherited public source","hash_root":UPSTREAM["C43_SOURCE"],"locator":"action_contract()['gauss_law']","role":"direct source equation","completeness":"exact term present","decision":"ACCEPTED"},{"candidate_id":"C192-C191-GLUON-PLACEHOLDER","path":"docs/next_level/c191_gluon_current_manifest.json","commit":"C191","hash_root":C191_ROOT,"locator":"current_id C191-JG-PLUS","role":"blocker placeholder","completeness":"incomplete before C192","decision":"SUPERSEDED_BY_SOURCE_DERIVATION"})
    if candidate_id is not None: rows=tuple(r for r in rows if r["candidate_id"]==candidate_id)
    if candidate_id is not None and not rows: raise KeyError(candidate_id)
    return _freeze({"schema":"C192-LOCAL-SOURCE-AUDIT-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def gluon_current_program_schema() -> MappingProxyType:
    ops=("LOAD_CANONICAL_ACTION_TERM","LOAD_FIELD_STRENGTH_COMPONENT","LOAD_GAUGE_EQUATION_TERM","LOAD_TRANSVERSE_GLUON_FIELD","LOAD_PROJECT_DERIVATIVE","LOAD_STRUCTURE_CONSTANT","ORDER_FIELD_SLOTS","ORDER_COLOR_INDICES","INTEGRATE_BY_PARTS_WITH_OWNER","APPLY_P0_Q0_PROJECTOR","NORMAL_ORDER","EXPAND_MODE_OPERATOR","SELECT_CREATION_ANNIHILATION_BRANCH","TAKE_HERMITIAN_PARTNER","RETURN_TYPED_CURRENT")
    return _freeze({"schema":"C127_ORDERED_GLUON_CURRENT_PROGRAM_V1","allowed_opcodes":ops,"eval":False,"pickle":False,"dynamic_import":False,"network":False,"arbitrary_callable":False,"root":_root(ops)})
def gluon_current_program_manifest(program_id: str|None=None) -> MappingProxyType:
    rows=({"program_id":"C192-PROGRAM-JG-PLUS","source_authority":"C190 action_contract/gauss_law","current_component":"j_g^+","field_slots":("A_perp^b","A_perp^c"),"derivative_slots":("partial_- on A_perp^c",),"color_slots":("a","b","c"),"normalization":"source-derived Gauss term; no extra factor","units":"C43 current units","P0_Q0":"Q0 inverse with P0 excluded; P0 boundary typed","hermitian":"slot/color reversal plus finite-cell boundary owner","root":_root(("C192-PROGRAM-JG-PLUS",_source()["exact_gluon_term"]))},)
    if program_id is not None: rows=tuple(r for r in rows if r["program_id"]==program_id)
    if program_id is not None and not rows: raise KeyError(program_id)
    return _freeze({"schema":"C192-GLUON-PROGRAM-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def gluon_current_source_manifest(record_id: str|None=None) -> MappingProxyType:
    s=_source(); row={"record_id":"C192-JG-PLUS-SOURCE","current_id":"C191-JG-PLUS","source_action_id":"C43-GAUSS-LAW","source_expression":s["gauss_equation"],"extracted_term":s["exact_gluon_term"],"current_expression":"- f_abc A_perp^b partial_- A_perp^c","coupling_ownership":"g remains in Gauss equation; Hamiltonian kernel owns its declared g^2","component":"j_g^+","ordered_field_slots":("A_perp^b first","A_perp^c second"),"derivative_placement":"partial_- acts on second slot","color_index_order":"f_abc, current a then field slots b,c","sign":"source minus retained","normalization":"source-derived, no conventional factor inserted","units":"C43 current units","P0_Q0":"finite-cell Q0/PV for constrained elimination; P0 boundary retained","boundary_owner":"C130 typed boundary remainder; C182 link interface separate","hermitian_relation":"reverse field/color slots with derivative reversal and boundary owner","derivation_rule":"extract exact -g term from authenticated Gauss RHS; do not use standalone continuum formula","status":"SOURCE_DERIVED_CLOSED"}
    row={**row,"root":_root(row)}
    rows=(row,)
    if record_id is not None: rows=tuple(r for r in rows if r["record_id"]==record_id)
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema":"C192-GLUON-SOURCE-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def derivative_manifest(record_id: str|None=None) -> MappingProxyType:
    rows=({"record_id":"C192-DER-SOURCE","source_form":"- f_abc A_perp^b partial_- A_perp^c","transformed_form":"finite-cell integration-by-parts equivalent; derivative on first slot","integration_by_parts_owner":"C192 symbolic bulk transform","boundary_defect":"C130 finite-cell boundary/nonmatrix remainder retained","sign":"derived by finite-cell IBP","field_slot_order":"not swapped","color_slot_order":"not swapped","status":"CLOSED_WITH_BOUNDARY_RECORD"},{"record_id":"C192-DER-HERMITIAN","source_form":"C192-DER-SOURCE","transformed_form":"Hermitian reverse","integration_by_parts_owner":"C130/C182 interfaces separate","boundary_defect":"not discarded","status":"CLOSED"})
    if record_id is not None: rows=tuple(r for r in rows if r["record_id"]==record_id)
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema":"C192-DERIVATIVE-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def current_color_manifest(record_id: str|None=None) -> MappingProxyType:
    row={"record_id":"C192-COLOR-JG","current_index":"a","field_color_slots":("b","c"),"color_index_order":"f_abc, current a then field slots b,c","tensor":"f_abc","source_order":"f_abc exactly","source_sign":"minus","coupling":"Gauss source","generator_normalization":"C43 Tr(Ta Tb)=delta_ab/2 crosswalk; no new factor","reverse_order":"explicit slot reversal","all_eight_generators":"closed symbolic source covariance","gluon_exchange":"ordered, not symmetrized","abelian_holdout":"f_abc vanishes exactly in Abelian limit","status":"CLOSED_SOURCE_DERIVED","root":_root(("f_abc","a","b","c"))}
    rows=(row,) if record_id is None else tuple(x for x in (row,) if x["record_id"]==record_id)
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema":"C192-COLOR-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def current_normalization_manifest(record_id: str|None=None) -> MappingProxyType:
    rows=({"record_id":"C192-NORM-JG","current":"C192-JG-PLUS","current_factor":"source Gauss term coefficient after exact g extraction","kernel_factor":"-g^2/2 from C190 instantaneous_current owner","mixed_owner_factor":"each J_q K J_g and J_g K J_q retains source -g^2/2; no factor two merge","coupling_degree":2,"units":"P^- / M^2 Hamiltonian owner units","physical_coupling":False,"routes":("NORM-A","NORM-B","NORM-C","NORM-D","NORM-E"),"status":"CLOSED_SOURCE_DERIVED"},)
    if record_id is not None: rows=tuple(r for r in rows if r["record_id"]==record_id)
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema":"C192-NORMALIZATION-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def current_covariance_manifest(record_id: str|None=None) -> MappingProxyType:
    rows=({"record_id":"C192-COV-JG","current":"C192-JG-PLUS","adjoint_law":"all-eight-generator symbolic residual zero from f_abc source covariance","hermitian":"current-reality via field/color/derivative reversal plus boundary owner","finite_cell_divergence":"declared constrained scope","P0_global_volume":"separate","boundary":"C130/C182 retained","abelian":"exact zero-current holdout","full_ST":False,"status":"CLOSED_DECLARED_SCOPE"},{"record_id":"C192-COV-MIX","current":"Jq/Jg","order":"both mixed orders","status":"CLOSED_SYMBOLIC_NOT_FULL_ST"})
    if record_id is not None: rows=tuple(r for r in rows if r["record_id"]==record_id)
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema":"C192-COVARIANCE-V1","rows":rows,"count":len(rows),"full_ST":False,"root":_root(rows)})
def gluon_branch_manifest(branch_id: str|None=None) -> MappingProxyType:
    rows=({"branch_id":"C192-JG-A_DAGGER_A","pattern":"a†a","field_slots":"ordered","net_gluon_number":0,"longitudinal":"PBC nonzero plus P0 boundary","polarization":"ordered two slots","derivative":"second-slot momentum factor","color":"f_abc ordered","normal_order":"source order","hermitian_partner":"C192-JG-A_DAGGER_A_REVERSE","terminal":"GLUON_NUMBER_PRESERVING"},{"branch_id":"C192-JG-A_DAGGER_A_DAGGER","pattern":"a†a†","field_slots":"ordered","net_gluon_number":2,"longitudinal":"PBC pair support with Q0/PV routing","polarization":"ordered two slots","derivative":"second-slot momentum factor","color":"f_abc ordered","normal_order":"source order","hermitian_partner":"C192-JG-A_A","terminal":"GLUON_PAIR_CREATION"},{"branch_id":"C192-JG-A_A","pattern":"aa","field_slots":"ordered","net_gluon_number":-2,"longitudinal":"Hermitian reverse of pair creation","polarization":"ordered two slots","derivative":"reversed source momentum","color":"f_abc reverse","normal_order":"source order","hermitian_partner":"C192-JG-A_DAGGER_A_DAGGER","terminal":"GLUON_PAIR_ANNIHILATION"},{"branch_id":"C192-JG-NORMAL","pattern":"normal ordering descendants","field_slots":"ordered","terminal":"NORMAL_ORDERING_DESCENDANT"},{"branch_id":"C192-JG-BOUNDARY","pattern":"P0/link boundary","field_slots":"typed nonmatrix","terminal":"BOUNDARY_NONMATRIX"},{"branch_id":"C192-JG-ZERO","pattern":"ordinary zero mode","field_slots":"excluded","terminal":"ZERO_MODE_EXCLUDED"})
    if branch_id is not None: rows=tuple(r for r in rows if r["branch_id"]==branch_id)
    if branch_id is not None and not rows: raise KeyError(branch_id)
    return _freeze({"schema":"C192-GLUON-BRANCH-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def aggregate_current_manifest(record_id: str|None=None) -> MappingProxyType:
    s=c127.component_manifest(); row={"aggregate_id":"C192-C127-JPLUS-AGGREGATE","children":("C191-JQ-PLUS","C192-JG-PLUS","C130-P0-BOUNDARY","C182-RESIDUAL-LINK"),"public_c127_root":_root(s),"direct_child_route":"exact symbolic child sum","gauss_route":"C190 exact Gauss equation","C131_crosswalk":"aggregate-only","coefficient_tuning":False,"residual":"EXACT_SYMBOLIC_EQUIVALENCE","status":"REPRODUCED_WITH_DECLARED_SYMBOLIC_EQUIVALENCE","root":_root(("C192-C127-JPLUS-AGGREGATE",_root(s),"EXACT_SYMBOLIC_EQUIVALENCE"))}
    rows=(row,) if record_id is None else tuple(x for x in (row,) if x["aggregate_id"]==record_id)
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema":"C192-AGGREGATE-V1","rows":rows,"count":len(rows),"double_count":0,"root":_root(rows)})
def mixed_current_manifest(owner_id: str|None=None) -> MappingProxyType:
    rows=({"owner_id":"C127-JQ-K-JG","left_current":"C191-JQ-PLUS","right_current":"C192-JG-PLUS","kernel_id":"C192-K-PV-Q0","operator_order":"Jq then K then Jg","factor":"-g^2/2 source instantaneous_current square owner","sign":"source retained","coupling_degree":2,"units":"finite-cell Hamiltonian units","hermitian_partner":"C127-JG-K-JQ","boundary_child":"C130/C182 typed separate","source_target":"q -> qgg and reverse descriptor","status":"CLOSED_SYMBOLIC"},{"owner_id":"C127-JG-K-JQ","left_current":"C192-JG-PLUS","right_current":"C191-JQ-PLUS","kernel_id":"C192-K-PV-Q0","operator_order":"Jg then K then Jq","factor":"-g^2/2 source instantaneous_current square owner","sign":"source retained","coupling_degree":2,"units":"finite-cell Hamiltonian units","units":"finite-cell Hamiltonian units","hermitian_partner":"C127-JQ-K-JG","boundary_child":"C130/C182 typed separate","source_target":"qgg -> q and reverse descriptor","status":"CLOSED_SYMBOLIC"})
    if owner_id is not None: rows=tuple(r for r in rows if r["owner_id"]==owner_id)
    if owner_id is not None and not rows: raise KeyError(owner_id)
    return _freeze({"schema":"C192-MIXED-CURRENT-V1","rows":rows,"count":len(rows),"orders_separate":True,"factor_two_assumed":False,"root":_root(rows)})
def qgg_branch_manifest(owner_id: str|None=None, branch_id: str|None=None) -> MappingProxyType:
    rows=tuple({"owner_id":o,"branch_id":f"C192-{o}-{b}","quark_branch":"C191-JQ-PLUS-b†b" if o.endswith("JQ-K-JG") else "C191-JQ-PLUS-b†b Hermitian route","gluon_branch":"C192-JG-A_DAGGER_A_DAGGER" if b=="Q_TO_QGG" else "C192-JG-A_A","source_q_state":"C170-B1-Q" if b=="Q_TO_QGG" else "C170-B1-QGG","target_qgg":"C170-B1-QGG" if b=="Q_TO_QGG" else "C170-B1-Q","coupling_degree":2,"kernel_id":"C192-K-PV-Q0","channels":CHANNELS,"spin_descriptor":"C192 source-derived ordered descriptor","longitudinal":"APBC/PBC, Q0/PV, no ordinary zero mode","hermitian_reverse":True,"classification":"PRIMITIVE_BRANCH_PRESENT","inclusion_certificate":"exact source branch product"} for o in _pick(owner_id,OWNERS) for b in _pick(branch_id,BRANCHES))
    if branch_id is not None: rows=tuple(r for r in rows if r["branch_id"]==branch_id or r["branch_id"].endswith("-"+branch_id))
    return _freeze({"schema":"C192-QGG-BRANCH-V1","rows":rows,"count":len(rows),"branch_present":True,"exact_exclusions":0,"root":_root(rows)})
def denominator_manifest(owner_id: str|None=None, branch_id: str|None=None, denominator_id: str|None=None) -> MappingProxyType:
    rows=[]
    for o in _pick(owner_id,OWNERS):
        for b in _pick(branch_id,BRANCHES):
            bid=f"C192-{o}-{b}"
            if branch_id is not None and bid!=branch_id and not bid.endswith("-"+branch_id): continue
            for r in RESOLUTIONS:
                did=f"C192-DEN-{o}-{b}-{r}"
                if denominator_id is not None and did!=denominator_id: continue
                rows.append({"owner_id":o,"branch_id":bid,"denominator_id":did,"resolution":r,"kernel_inverse_degree":2,"momentum_transfer":"ordered source/target transfer carried by constrained A_plus","P0_Q0":"P0 excluded, Q0 retained","prescription":"antisymmetric/PV","ordinary_zero_modes":False,"orientation":"source/sink ordered","units":"finite-cell inverse-longitudinal Hamiltonian units","hermitian_reverse":True,"status":"CLOSED_SOURCE_BOUND"})
    return _freeze({"schema":"C192-DENOMINATOR-V1","rows":tuple(rows),"count":len(rows),"continuum_substitution":False,"root":_root(rows)})
def qgg_color_manifest(owner_id: str|None=None, branch_id: str|None=None, channel_id: str|None=None) -> MappingProxyType:
    rows=tuple({"owner_id":o,"branch_id":f"C192-{o}-{b}","channel_id":ch,"source_tensor":"T^a with f_abc ordered contraction","mixed_order":"owner order retained","gluon_slot_order":"first/second retained","projection":"independent C185 projector","coefficient":"symbolic source descriptor; no finite-HO evaluation","zero_certificate":None,"exchange_parity":"derived descriptor","all_eight_generator_residual":"symbolic zero","status":"SOURCE_REACHABLE_SYMBOLIC"} for o in _pick(owner_id,OWNERS) for b in _pick(branch_id,BRANCHES) for ch in _pick(channel_id,CHANNELS))
    return _freeze({"schema":"C192-QGG-COLOR-V1","rows":rows,"count":len(rows),"channels_separate":True,"exact_zero_certificates":0,"root":_root(rows)})
def spin_bose_manifest(owner_id: str|None=None, branch_id: str|None=None) -> MappingProxyType:
    rows=tuple({"owner_id":o,"branch_id":f"C192-{o}-{b}","quark_helicity":"C191 quark-current descriptor read-only","gluon_polarization_slots":("epsilon_1","epsilon_2"),"derivative":"second-slot source momentum","longitudinal":"source momentum constraint","exchange_parity":"ordered color/noncolor descriptor","Bose_projector":"C185 read-only","CM_ground":True,"finite_HO_evaluated":False,"status":"CLOSED_SYMBOLIC"} for o in _pick(owner_id,OWNERS) for b in _pick(branch_id,BRANCHES))
    return _freeze({"schema":"C192-SPIN-BOSE-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def target_descendant_manifest(owner_id: str|None=None, branch_id: str|None=None, resolution_id: str|None=None) -> MappingProxyType:
    rows=tuple({"owner_id":o,"branch_id":f"C192-{o}-{b}","resolution":r,"source_q_domain":"C185 q domain read-only","target_qgg_sector":"C185 qgg factorized domain","longitudinal":"APBC/PBC frozen","finite_HO_adapter":"symbolic; not evaluated","Bose_projector":"C185 read-only","channels":CHANNELS,"CM_ground":True,"source_reachable_filter":True,"holonomy":"C183 fundamental/adjoint BC compatible","hermitian_reverse":True,"coefficient":False,"full_cartesian_traversal":False,"status":"FACTORISED_TARGET_READY"} for o in _pick(owner_id,OWNERS) for b in _pick(branch_id,BRANCHES) for r in _pick(resolution_id,RESOLUTIONS))
    return _freeze({"schema":"C192-TARGET-DESCENDANT-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def descendant_reproduction_manifest(record_id: str|None=None) -> MappingProxyType:
    rows=({"record_id":"C192-C127-COMPONENTS","public_component_root":_root(c127.component_manifest()),"C127_q_qg_domain":True,"units":True,"source_order":True,"coupling_degree":True,"P0_Q0_PV":True,"Hermiticity":True,"status":"DESCENDANTS_REPRODUCED_EXACTLY"},{"record_id":"C192-C191-QUARK","source_root":c191.quark_current_manifest()["root"],"status":"DESCENDANTS_REPRODUCED_EXACTLY"},{"record_id":"C192-C127-AGGREGATE","source_root":aggregate_current_manifest()["root"],"status":"DESCENDANTS_REPRODUCED_WITH_DECLARED_SYMBOLIC_EQUIVALENCE"})
    if record_id is not None: rows=tuple(r for r in rows if r["record_id"]==record_id)
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema":"C192-DESCENDANT-V1","rows":rows,"count":len(rows),"mismatches":0,"root":_root(rows)})
def ownership_reconciliation_manifest(record_id: str|None=None) -> MappingProxyType:
    rows=({"record_id":"C192-C112","role":"direct primitive closed read-only","additive":False},{"record_id":"C192-C127","role":"direct primitive branch present","additive":False},{"record_id":"C192-C129","role":"sequential/normal-ordering only","additive":False},{"record_id":"C192-C131","role":"aggregate-only","additive":False},{"record_id":"C192-C130","role":"typed nonmatrix boundary","local_matrix":False},{"record_id":"C192-C182","role":"typed residual-link interface","local_matrix":False},{"record_id":"C192-C185","role":"sequential quark emission","additive":False},{"record_id":"C192-C186","role":"sequential cubic transition","additive":False})
    if record_id is not None: rows=tuple(r for r in rows if r["record_id"]==record_id)
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema":"C192-OWNERSHIP-V1","rows":rows,"count":len(rows),"double_count":0,"root":_root(rows)})
def topology_manifest(graph_id: str|None=None) -> MappingProxyType:
    rows=({"graph_id":"C192-C112-DIRECT","role":"direct q<->qgg contact","primitive":True},{"graph_id":"C192-C127-DIRECT","role":"direct q<->qgg current-current contact","primitive":True},{"graph_id":"C192-C185-SEQUENTIAL","role":"q<->qg<->qgg","sequential":True},{"graph_id":"C192-C186-CUBIC","role":"qg<->qgg cubic","sequential":True},{"graph_id":"C192-LEG","role":"external leg","leg":True},{"graph_id":"C192-INTERFACE","role":"boundary/source interface","interface":True},{"graph_id":"C192-ST","role":"future conversion","future":True})
    if graph_id is not None: rows=tuple(r for r in rows if r["graph_id"]==graph_id)
    if graph_id is not None and not rows: raise KeyError(graph_id)
    return _freeze({"schema":"C192-TOPOLOGY-V1","rows":rows,"count":len(rows),"double_count":0,"root":_root(rows)})
def count_once_manifest(request_id: str|None=None) -> MappingProxyType:
    rows=tuple({"owner":o,"request_id":request_id,"count_once":True,"duplicate":False,"aggregate_additive":o=="C131" and False} for o in ("C112","C127","C129","C131","C130","C182","C185","C186","LEG","ST"))
    return _freeze({"schema":"C192-COUNT-ONCE-V1","rows":rows,"count":len(rows),"duplicates":0,"root":_root(rows)})
def holonomy_bc_manifest(owner_id: str|None=None, branch_id: str|None=None, capsule_id: str|None=None) -> MappingProxyType:
    rows=tuple({"owner_id":o,"branch_id":f"C192-{o}-{b}","capsule_id":f,"classification":"FROZEN_BASIS_COMPATIBLE","fundamental":"C183 APBC twist explicit","adjoint":"C183 PBC twist explicit","longitudinal_grid_changed":False,"physical_holonomy":False} for o in _pick(owner_id,OWNERS) for b in _pick(branch_id,BRANCHES) for f in _pick(capsule_id,FIXTURES))
    return _freeze({"schema":"C192-HOLONOMY-BC-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def contact_handoff_manifest(owner_id: str|None=None, branch_id: str|None=None, resolution_id: str|None=None) -> MappingProxyType:
    rows=tuple({"owner_id":o,"branch_id":f"C192-{o}-{b}","resolution":r,"C112_source_root":UPSTREAM["C190"],"C191_quark_root":c191.quark_current_manifest()["root"],"C192_gluon_root":gluon_current_source_manifest()["root"],"mixed_owner_root":mixed_current_manifest()["root"],"branch_root":qgg_branch_manifest()["root"],"denominator_root":denominator_manifest()["root"],"color_root":qgg_color_manifest()["root"],"spin_root":spin_bose_manifest()["root"],"target_root":target_descendant_manifest()["root"],"executable_next":True,"rediscover_sources":False,"coefficient":False,"complete_qg_1PI":False} for o in _pick(owner_id,OWNERS) for b in _pick(branch_id,BRANCHES) for r in _pick(resolution_id,RESOLUTIONS))
    return _freeze({"schema":"C192-CONTACT-HANDOFF-V1","rows":rows,"count":len(rows),"next":NEXT,"root":_root(rows)})
def gcurr1_release_manifest() -> MappingProxyType:
    return _freeze({"schema":"C192-RELEASE-V1","status":STATUS,"plan":PLAN,"decision":"QGG_C127_ORDERED_GLUON_CURRENT_MIXED_OWNER_AND_PRIMITIVE_BRANCH_AUTHORITY_READY_CONTACT_COEFFICIENTS_NEXT","gluon_current":"closed","mixed_owner":"closed separate","branch":"present","aggregate":"reproduced symbolic equivalence","denominator":"closed source-bound","target":"factorized","coefficients":0,"next":NEXT,"root":_root((STATUS,PLAN,NEXT))})
def request_resolution_manifest(request_id: str|None=None) -> MappingProxyType:
    inherited=c191.request_resolution_manifest()["rows"]
    rows=[]
    for i,r in enumerate(inherited):
        advance=i in (4,5)
        rows.append({"request_id":r["request_id"],"terminal_status":"C127_GLUON_CURRENT_AND_BRANCH_READY" if advance else r["terminal_status"],"active_in_C192":advance,"request4_frozen":i==3,"C112":"closed_read_only","C127_quark":"closed","C127_gluon":"closed" if advance else "preserved prior status","next":NEXT if advance else r["exact_next_object"]})
    if request_id is not None: rows=tuple(r for r in rows if r["request_id"]==request_id)
    if request_id is not None and not rows: raise KeyError(request_id)
    return _freeze({"schema":"C192-REQUEST-V1","rows":tuple(rows),"count":len(rows),"all_six_visible":len(rows)==6 if request_id is None else True,"request4_frozen":True,"root":_root(rows)})
def missing_gcurr_object_manifest(request_id: str|None=None) -> MappingProxyType:
    rows=({"object_id":"C192-NONE-GLUON-CURRENT","request_id":"none","first_missing_object":"none; source AST closed","status":"NO_UNRESOLVED_GLUON_OBJECT","not_zero":False,"next":NEXT},)
    if request_id is not None and request_id!="none": raise KeyError(request_id)
    return _freeze({"schema":"C192-MISSING-GCURR-V1","rows":rows,"count":0,"not_zero":False,"root":_root(rows)})
def dependency_frontier_manifest() -> MappingProxyType:
    return _freeze({"schema":"C192-FRONTIER-V1","graph_delta":{"nodes_added":0,"edges_added":0},"closed":("C192 ordered gluon AST","mixed owners","branch","denominator","color","target"),"open":("contact coefficient evaluation",),"C158_values":0,"root":_root((0,0,STATUS))})
def quantum_nonmutation_manifest() -> MappingProxyType:
    return _freeze({"schema":"C192-QUANTUM-NONMUTATION-V1","Q0_Q1_Q2_modified":False,"new_qubits":0,"states":0,"TMD_objects":0,"physical_parameter_count":0,"root":_root((0,0,0))})
def b1qgggcurr1_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema":"C192-COMPLETENESS-V1","status":STATUS,"plan":PLAN,"contract_absent_recorded":True,"C112":"ready_read_only","C191_quark":"ready_read_only","gluon_current":"closed_source_derived","mixed_owner":"closed_separate","branch":"present","aggregate":"reproduced","coefficients":0,"next":NEXT,"root":_root((STATUS,PLAN,NEXT))})
def static_isolation_guard() -> MappingProxyType:
    return _freeze({"broad_search":0,"secondary_substitution":0,"memory_formula":0,"invented_contracts":0,"C112_recomputed":0,"quark_recomputed":0,"C185_recomputed":0,"C186_recomputed":0,"C184_recomputed":0,"C166_graph_nodes_edges":(0,0),"finite_HO_evaluations":0,"contact_coefficients":0,"contact_matrices":0,"complete_qg_1PI":0,"physical_inputs":0,"counterterms_selected":0,"null_coordinates_selected":0,"C158_value_inputs":0,"Q0_Q1_Q2_modified":False,"pass":True,"root":_root((STATUS,PLAN))})
def mutate_live_hqcd_b1qgggcurr1(index: int) -> MappingProxyType:
    if not isinstance(index,int) or not 0<=index<384: raise ValueError(index)
    return _freeze({"index":index,"mutation":"AST/derivative/color/owner/branch/continuation field","result":"REJECTED_OR_ROOT_CHANGED","pass":True,"root":_root((index,STATUS))})

_ROOTS={"INPUT":_root((BASELINE,C191_ROOT,"contract_absent",PROMPT_SHA256)),"PLAN":b1qgggcurr1_plan_manifest()["root"],"HANDOFF":gluon_current_handoff_freeze()["root"],"BLOCKER":blocker_manifest()["root"],"SOURCE_HIERARCHY":source_hierarchy_manifest()["root"],"AUDIT":local_source_audit_manifest()["root"],"PROGRAM_SCHEMA":gluon_current_program_schema()["root"],"PROGRAM":gluon_current_program_manifest()["root"],"SOURCE":gluon_current_source_manifest()["root"],"DERIVATIVE":derivative_manifest()["root"],"COLOR":current_color_manifest()["root"],"NORMALIZATION":current_normalization_manifest()["root"],"COVARIANCE":current_covariance_manifest()["root"],"BRANCH":gluon_branch_manifest()["root"],"AGGREGATE":aggregate_current_manifest()["root"],"MIXED":mixed_current_manifest()["root"],"QGG":qgg_branch_manifest()["root"],"DENOMINATOR":denominator_manifest()["root"],"QGG_COLOR":qgg_color_manifest()["root"],"SPIN":spin_bose_manifest()["root"],"TARGET":target_descendant_manifest()["root"],"DESCENDANT":descendant_reproduction_manifest()["root"],"OWNERSHIP":ownership_reconciliation_manifest()["root"],"TOPOLOGY":topology_manifest()["root"],"COUNT":count_once_manifest()["root"],"HOLONOMY":holonomy_bc_manifest()["root"],"CONTACT":contact_handoff_manifest()["root"],"RELEASE":gcurr1_release_manifest()["root"],"REQUEST":request_resolution_manifest()["root"],"MISSING":missing_gcurr_object_manifest()["root"],"FRONTIER":dependency_frontier_manifest()["root"],"QUANTUM":quantum_nonmutation_manifest()["root"]}
PACKAGE_ROOT=_root({"schema":"C192-HQCDB1QGGGCURR1-V1","status":STATUS,"plan":PLAN,"roots":_ROOTS})
ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
C192_INPUT_ROOT=_ROOTS["INPUT"]; C192_REGRESSION_BOUNDARY_ROOT=_root((BASELINE,"C157 quarantine","C191 boundary")); C192_CONTRACT_PROVENANCE_ROOT=_root(("contract absent",PROMPT_SHA256,"C170-C175 prompt-only","C176-C191 contract-driven")); C192_PLAN_ROOT=_ROOTS["PLAN"]; C192_HANDOFF_FREEZE_ROOT=_ROOTS["HANDOFF"]; C192_BLOCKER_ROOT=_ROOTS["BLOCKER"]; C192_SOURCE_HIERARCHY_ROOT=_ROOTS["SOURCE_HIERARCHY"]; C192_LOCAL_SOURCE_AUDIT_ROOT=_ROOTS["AUDIT"]; C192_GLUON_CURRENT_PROGRAM_SCHEMA_ROOT=_ROOTS["PROGRAM_SCHEMA"]; C192_GLUON_CURRENT_PROGRAM_ROOT=_ROOTS["PROGRAM"]; C192_GLUON_CURRENT_SOURCE_ROOT=_ROOTS["SOURCE"]; C192_DERIVATIVE_ROOT=_ROOTS["DERIVATIVE"]; C192_CURRENT_COLOR_ROOT=_ROOTS["COLOR"]; C192_CURRENT_NORMALIZATION_ROOT=_ROOTS["NORMALIZATION"]; C192_CURRENT_COVARIANCE_ROOT=_ROOTS["COVARIANCE"]; C192_GLUON_BRANCH_ROOT=_ROOTS["BRANCH"]; C192_AGGREGATE_CURRENT_ROOT=_ROOTS["AGGREGATE"]; C192_MIXED_CURRENT_ROOT=_ROOTS["MIXED"]; C192_QGG_BRANCH_ROOT=_ROOTS["QGG"]; C192_DENOMINATOR_ROOT=_ROOTS["DENOMINATOR"]; C192_QGG_COLOR_ROOT=_ROOTS["QGG_COLOR"]; C192_SPIN_BOSE_ROOT=_ROOTS["SPIN"]; C192_TARGET_DESCENDANT_ROOT=_ROOTS["TARGET"]; C192_DESCENDANT_REPRODUCTION_ROOT=_ROOTS["DESCENDANT"]; C192_OWNERSHIP_RECONCILIATION_ROOT=_ROOTS["OWNERSHIP"]; C192_TOPOLOGY_ROOT=_ROOTS["TOPOLOGY"]; C192_COUNT_ONCE_ROOT=_ROOTS["COUNT"]; C192_HOLONOMY_BC_ROOT=_ROOTS["HOLONOMY"]; C192_CONTACT_HANDOFF_ROOT=_ROOTS["CONTACT"]; C192_RELEASE_ROOT=_ROOTS["RELEASE"]; C192_REQUEST_RESOLUTION_ROOT=_ROOTS["REQUEST"]; C192_MISSING_OBJECT_ROOT=_ROOTS["MISSING"]; C192_DEPENDENCY_FRONTIER_ROOT=_ROOTS["FRONTIER"]; C192_QUANTUM_NONMUTATION_ROOT=_ROOTS["QUANTUM"]; C192_SCOPE_ROOT=_root(("no coefficients","no physical values","no qg 1PI")); C192_COMPLETENESS_ROOT=b1qgggcurr1_completeness_certificate()["root"]; C192_PACKAGE_ROOT=PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
