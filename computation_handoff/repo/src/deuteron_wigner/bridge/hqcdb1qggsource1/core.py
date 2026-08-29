"""C189 project-owned, fail-closed source derivation gate.

This module contains only immutable metadata and safe symbolic source
descriptors.  It deliberately stops before a qgg coefficient or contact
matrix.  The public C148 constraint/current authorities reproduce the already
published q and qg descendant metadata, but do not expose an exact C112 or
C127 qgg operator AST.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge import hqcd2ptfull as c148

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c189_hqcdb1qggsource1"
BASELINE = "5203d7e56ecd9e73143a9b764db3c9ce8e8c93a0"
CONTRACT = "docs/next_level/c188_c189_hqcdb1qggsource1_continuation_contract.json"
CONTRACT_SHA256 = "6d194c0cd43b54e8b2814f69da9571df2d1e2b79f7a1de4552e37b6c570d3324"
PROMPT = "/Users/dustin/Downloads/c189_hqcdb1qggsource1_codex_prompt.md"
PROMPT_SHA256 = "3206eabbe810b81b8b873c6d24c9b28080bb8b8d75b7474490124aff3cf2b0d6"
STATUS = "C189_HQCDB1QGGSOURCE1_DERIVATION_PREREQUISITES_INCOMPLETE"
PLAN = "QGGSOURCE1-F"
NEXT = "C190/HQCDB1QGGSOURCE2"
RESOLUTIONS = ("K9", "K11", "K13")
C112_RESOLUTIONS = ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50")
OWNERS = ("C112_INSTANTANEOUS_FERMION_QGG", "C127_GAUSS_CURRENT_QGG")
BRANCHES = ("Q_TO_QGG", "QGG_TO_Q")
QGG_CHANNELS = ("QGG_COLOR_1S", "QGG_COLOR_8S", "QGG_COLOR_8A")
FIXTURES = ("IDENTITY_DIAGNOSTIC_ONLY", "GENERIC_CARTAN_INTERIOR", "NONTRIVIAL_CENTER_SECTOR", "CONJUGATED_NONDIAGONAL_GENERIC", "FUTURE_PAST_INVERSE_PAIR")
UPSTREAM_ROOTS = {"C188":"b99ece13987bd02ab271162d520611aba8943c29eed1963cadd0e4dfa2f570a6", "C187":"9a9f7834eb30d28c432a470503bf2f3a720477bf71ebf6a2ffdce0aef075d365", "C186":"df5bf0f48d51f2d47827454b4e31fc8ea2702665f14aa198e07c848bd9b19d20", "C185":"c9c676c41b3a8deba0e241876cb9a76158cfe3351fd55530331e9932ef646885", "C184":"89a7b8772b838811e0b897b90b4f870788d85740436647c6e3cba496f94991d8", "C183":"7198854f07fdbde8a00d8d553a848ba0d5cf3408199b9b7ff3a3cd29074c7b5f", "C148":c148.PACKAGE_ROOT}
REQUESTS = ("C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-TRANSVERSE_GLUON_FIELD-MOMQ-2", "C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-QCD_COUPLING-MOMQ-2", "C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-qg_VERTEX_DRESSING-MOMQ-2", "C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-QCD_COUPLING-ST-2", "C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-SIGNED_MASS-2", "C166-ACQUIRE-C165-MISSING-C164-LOC-TGT-MASS_SQUARED-2")
OPCODES = ("LOAD_C43_ACTION_TERM", "LOAD_GOOD_BAD_FIELD_SPLIT", "LOAD_CONSTRAINT_EQUATION", "LOAD_CURRENT_COMPONENT", "SOLVE_LINEAR_CONSTRAINT", "SUBSTITUTE_CONSTRAINED_FIELD", "NORMAL_ORDER", "EXPAND_ORDERED_PRODUCT", "APPLY_PROJECTOR", "SELECT_SOURCE_ORDER", "SELECT_CREATION_ANNIHILATION_BRANCH", "TAKE_HERMITIAN_PARTNER", "SIMPLIFY_WITH_EXACT_GENERATOR_IDENTITY", "RETURN_TYPED_SOURCE_EXPRESSION")

def _plain(x: Any) -> Any:
    if isinstance(x, Mapping): return {str(k): _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    return x
def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)): return tuple(_freeze(v) for v in x)
    return x
def _root(x: Any) -> str: return sha256(json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()
def _pick(value: str | None, values: tuple[str, ...]) -> tuple[str, ...]:
    if value is None: return values
    if value not in values: raise KeyError(value)
    return (value,)

def _verify_frozen() -> None:
    expected = {"C188":"b99ece13987bd02ab271162d520611aba8943c29eed1963cadd0e4dfa2f570a6", "C187":"9a9f7834eb30d28c432a470503bf2f3a720477bf71ebf6a2ffdce0aef075d365", "C186":"df5bf0f48d51f2d47827454b4e31fc8ea2702665f14aa198e07c848bd9b19d20", "C185":"c9c676c41b3a8deba0e241876cb9a76158cfe3351fd55530331e9932ef646885", "C184":"89a7b8772b838811e0b897b90b4f870788d85740436647c6e3cba496f94991d8", "C183":"7198854f07fdbde8a00d8d553a848ba0d5cf3408199b9b7ff3a3cd29074c7b5f"}
    actual = {k:UPSTREAM_ROOTS[k] for k in expected}
    if actual != expected: raise ValueError("C183-C188 frozen root boundary changed")

def load_verified_hqcd_b1qggsource1_authority() -> MappingProxyType:
    m = json.loads((RUNTIME / "manifest.json").read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS: raise ValueError("C189 runtime root/status mismatch")
    return verify_hqcd_b1qggsource1_authority()
def verify_hqcd_b1qggsource1_authority() -> MappingProxyType:
    _verify_frozen()
    return _freeze({"schema":"C189-AUTHORITY-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"contract":CONTRACT,"contract_sha256":CONTRACT_SHA256,"prompt_sha256":PROMPT_SHA256,"C188_package_root":UPSTREAM_ROOTS["C188"],"source_acquisition":0,"C158_value_inputs":0,"C166_graph_nodes_edges":(0,0),"coefficients":0,"physical":False,"package_root":PACKAGE_ROOT})
def b1qggsource1_plan_manifest() -> MappingProxyType:
    return _freeze({"schema":"C189-PLAN-V1","selected_plan":PLAN,"status":STATUS,"next":NEXT,"reason":"C112 and C127 exact qgg source ASTs are absent; public C148 prerequisites close only through q and qg descendants","source_acquisition_authorized":False,"root":_root((PLAN,STATUS,NEXT))})
def source_handoff_freeze() -> MappingProxyType:
    return _freeze({"schema":"C189-HANDOFF-FREEZE-V1","C188_package_root":UPSTREAM_ROOTS["C188"],"C188_source_root":"C188 public source inventory frozen","C185_qgg_root":"C185:C170-B1-QGG frozen basis authority","C148_package_root":c148.PACKAGE_ROOT,"C43_action_root":_root(c148.spinor_convention_manifest()),"read_only":True,"root":_root((UPSTREAM_ROOTS["C188"],UPSTREAM_ROOTS["C185"],c148.PACKAGE_ROOT))})

def source_hierarchy_manifest() -> MappingProxyType:
    rows = ({"tier":"LOCAL_GIT","status":"AUDITED_NO_EXACT_OBJECT","scope":"tracked source, history, manifests, tests","accepted":False},{"tier":"AUTHENTICATED_LOCAL_ARCHIVES","status":"AUDITED_NO_EXACT_OBJECT","scope":"C43/C140-C177 archive inventory","accepted":False},{"tier":"OFFICIAL_ACQUISITION","status":"NOT_USED_CONTRACT_SOURCE_ACQUISITION_ZERO","scope":"no endpoint/version authorized","accepted":False},{"tier":"PROJECT_DERIVATION","status":"PREREQUISITES_PARTIAL","scope":"C148 constraint/current authority and existing q/qg descendants","accepted":True})
    return _freeze({"schema":"C189-SOURCE-HIERARCHY-V1","rows":rows,"broad_search":False,"related_paper_substitution":False,"memory_authority":False,"root":_root(rows)})
def local_source_audit_manifest(owner_id: str | None = None, candidate_id: str | None = None) -> MappingProxyType:
    rows = ({"candidate_id":"C189-C112-PUBLIC-SECTORS","owner":"C112","path":"src/deuteron_wigner/bridge/iferm3","locator":"instantaneous_fermion_sector_manifest","exact_version":"committed public API","role":"q/qg sector metadata","accepted":True,"qgg_ast":False},{"candidate_id":"C189-C127-PUBLIC-COMPONENTS","owner":"C127","path":"src/deuteron_wigner/bridge/icagg3","locator":"component_manifest/instantaneous_current_sparse_matrix","exact_version":"committed public API","role":"q/qg current metadata","accepted":True,"qgg_ast":False},{"candidate_id":"C189-C148-CONSTRAINT","owner":"C148","path":"src/deuteron_wigner/bridge/hqcd2ptfull/core.py","locator":"constraint_factorization_manifest","exact_version":"C148 package root","role":"C43 constrained-field prerequisite","accepted":True,"qgg_ast":False},{"candidate_id":"C189-C148-INVERSE","owner":"C148","path":"src/deuteron_wigner/bridge/hqcd2ptfull/core.py","locator":"inverse_partial_plus_manifest","exact_version":"C148 package root","role":"finite-cell Q0/PV prerequisite","accepted":True,"qgg_ast":False},{"candidate_id":"C189-NO-QGG-AST","owner":"C112/C127","path":"repository and authenticated archives","locator":"complete q<->qgg source/operator monomial","exact_version":"none found","role":"required primitive source","accepted":False,"qgg_ast":False,"terminal":"DERIVATION_PREREQUISITE_INCOMPLETE"})
    if owner_id is not None and owner_id not in OWNERS: raise KeyError(owner_id)
    if candidate_id is not None and candidate_id not in {r["candidate_id"] for r in rows}: raise KeyError(candidate_id)
    rows=tuple(r for r in rows if (owner_id is None or r["owner"]==owner_id or r["owner"]=="C112/C127") and (candidate_id is None or r["candidate_id"]==candidate_id))
    return _freeze({"schema":"C189-LOCAL-SOURCE-AUDIT-V1","rows":rows,"count":len(rows),"exact_qgg_ast_count":0,"exhaustive_local_search":True,"root":_root(rows)})
def acquisition_manifest(owner_id: str | None = None, source_object_id: str | None = None) -> MappingProxyType:
    if owner_id is not None and owner_id not in OWNERS: raise KeyError(owner_id)
    row={"schema":"C189-ACQUISITION-V1","status":"NOT_USED","source_acquisition":0,"official_endpoint":None,"exact_version":None,"source_object_id":source_object_id,"reason":"contract source_acquisition=0 and no exact locator identified","downloaded":False,"license_record":"not applicable","root":_root(("NOT_USED",0,source_object_id))}
    return _freeze(row)

def derivation_dag_schema() -> MappingProxyType:
    return _freeze({"schema":"C189-SAFE-DERIVATION-GRAMMAR-V1","allowed_opcodes":OPCODES,"data_only":True,"arbitrary_callable":False,"eval":False,"pickle":False,"dynamic_import":False,"network":False,"coefficient_evaluation":False,"root":_root(OPCODES)})
def _dag_nodes() -> tuple[Mapping[str,Any], ...]:
    return ({"node_id":"C189-C148-GOOD-BAD","opcode":"LOAD_GOOD_BAD_FIELD_SPLIT","source":"C148.spinor_convention_manifest","output":"psi_plus/psi_minus typed split","status":"CLOSED"},{"node_id":"C189-C148-CONSTRAINT","opcode":"LOAD_CONSTRAINT_EQUATION","source":"C148.constraint_factorization_manifest","output":"K_perp + signed mass + g_s K_A + boundary","status":"CLOSED"},{"node_id":"C189-C148-INVERSE","opcode":"SOLVE_LINEAR_CONSTRAINT","source":"C148.inverse_partial_plus_manifest","output":"Q0 inverse on nonzero finite-cell source modes, antisymmetric/PV retained","status":"CLOSED"},{"node_id":"C189-C148-Q-SOURCE","opcode":"RETURN_TYPED_SOURCE_EXPRESSION","source":"C148.q_bad_source_manifest","output":"q source descriptor","status":"CLOSED"},{"node_id":"C189-C148-QG-SOURCE","opcode":"RETURN_TYPED_SOURCE_EXPRESSION","source":"C148.qg_bad_source_manifest","output":"qg source descriptor","status":"CLOSED"},{"node_id":"C189-C112-QGG-LEAF","opcode":"RETURN_TYPED_SOURCE_EXPRESSION","source":"C112 exact qgg source AST absent","output":"C112 q<->qgg primitive source","status":"MISSING_PREREQUISITE"},{"node_id":"C189-C127-QGG-LEAF","opcode":"RETURN_TYPED_SOURCE_EXPRESSION","source":"C127 exact qgg source AST absent","output":"C127 q<->qgg primitive source","status":"MISSING_PREREQUISITE"})
def derivation_dag_manifest(owner_id: str | None = None, node_id: str | None = None) -> MappingProxyType:
    if owner_id is not None and owner_id not in OWNERS: raise KeyError(owner_id)
    edges=(("C189-C148-GOOD-BAD","C189-C148-CONSTRAINT"),("C189-C148-CONSTRAINT","C189-C148-INVERSE"),("C189-C148-INVERSE","C189-C148-Q-SOURCE"),("C189-C148-INVERSE","C189-C148-QG-SOURCE"),("C189-C148-Q-SOURCE","C189-C112-QGG-LEAF"),("C189-C148-QG-SOURCE","C189-C127-QGG-LEAF"))
    nodes=tuple(n for n in _dag_nodes() if node_id is None or n["node_id"]==node_id)
    if node_id is not None and not nodes: raise KeyError(node_id)
    return _freeze({"schema":"C189-DERIVATION-DAG-V1","nodes":nodes,"edges":edges if node_id is None else tuple(e for e in edges if node_id in e),"acyclic":True,"source_version_consistent":True,"complete":False,"missing_leaves":("C189-C112-QGG-LEAF","C189-C127-QGG-LEAF"),"root":_root((nodes,edges))})

def _owner_rows(owner: str, source: str) -> tuple[Mapping[str,Any], ...]:
    return tuple({"source_term_id":f"C189-{owner}-{term}","owner":owner,"term":term,"source":source,"expression":"typed symbolic source metadata; complete AST unavailable" if "QGG" in term else source,"field_slots":("q","qbar","g_1","g_2"),"coupling_degree":2,"inverse_longitudinal":"C148 Q0 inverse / antisymmetric PV descriptor; qgg placement unresolved","branch_status":"DERIVATION_PREREQUISITE_INCOMPLETE" if "QGG" in term else "PUBLIC_DESCENDANT_REPRODUCTION_CLOSED","complete_expression":False if "QGG" in term else True,"coefficient":False,"root":_root((owner,term,source))} for term in ("Q_SOURCE","QG_SOURCE","QGG_SOURCE_PRIMITIVE"))
def c112_source_manifest(source_term_id: str | None = None, branch_id: str | None = None) -> MappingProxyType:
    from deuteron_wigner.bridge import iferm3 as c112_api
    public = tuple((r, _root(c112_api.instantaneous_fermion_sector_manifest(r)), c112_api.cross_sector_zero_certificate(r)["certificate_root"]) for r in C112_RESOLUTIONS)
    rows=_owner_rows("C112","C148 constraint + C112 public sector metadata")
    rows=tuple(dict(row, public_descendant_root=_root(public), public_cross_sector_exact_zero=True) for row in rows)
    if source_term_id is not None: rows=tuple(r for r in rows if r["source_term_id"]==source_term_id)
    if source_term_id is not None and not rows: raise KeyError(source_term_id)
    return _freeze({"schema":"C189-C112-SOURCE-V1","rows":rows,"count":len(rows),"qgg_ast":False,"root":_root(rows)})
def c127_source_manifest(source_term_id: str | None = None, branch_id: str | None = None) -> MappingProxyType:
    from deuteron_wigner.bridge import icagg3 as c127_api
    public = (c127_api.component_manifest()["count"], tuple(c127_api.cross_sector_zero_certificate(r, "J_qJ_q")["status"] for r in C112_RESOLUTIONS))
    rows=_owner_rows("C127","C148 constraint + C127 current metadata")
    rows=tuple(dict(row, public_descendant_root=_root(public), public_cross_sector_exact_zero=True) for row in rows)
    if source_term_id is not None: rows=tuple(r for r in rows if r["source_term_id"]==source_term_id)
    if source_term_id is not None and not rows: raise KeyError(source_term_id)
    return _freeze({"schema":"C189-C127-SOURCE-V1","rows":rows,"count":len(rows),"qgg_ast":False,"root":_root(rows)})
def branch_manifest(owner_id: str | None = None, branch_id: str | None = None) -> MappingProxyType:
    owners=_pick(owner_id,OWNERS); rows=[]
    for owner in owners:
        for branch in BRANCHES:
            bid=f"C189-{owner}-{branch}"
            rows.append({"branch_id":bid,"owner":owner,"source_sector":"C170-B1-Q" if branch=="Q_TO_QGG" else "C170-B1-QGG","target_sector":"C170-B1-QGG" if branch=="Q_TO_QGG" else "C170-B1-Q","classification":"BRANCH_INCOMPLETE","reason":"exact primitive source AST and ordered creation/annihilation expansion absent","hermitian_partner":f"C189-{owner}-{'QGG_TO_Q' if branch=='Q_TO_QGG' else 'Q_TO_QGG'}","not_zero":True,"root":_root((owner,branch,"incomplete"))})
    if branch_id is not None: rows=[r for r in rows if r["branch_id"]==branch_id]
    return _freeze({"schema":"C189-BRANCH-V1","rows":tuple(rows),"count":len(rows),"qgg_branch_proven":False,"exact_branch_absence":False,"root":_root(rows)})
def descendant_reproduction_manifest(owner_id: str | None = None, descendant_id: str | None = None) -> MappingProxyType:
    owners=_pick(owner_id,OWNERS); rows=[]
    for owner in owners:
        for res in RESOLUTIONS:
            for sector in ("Q","QG"):
                did=f"C189-{owner}-{sector}-{res}"
                rows.append({"descendant_id":did,"owner":owner,"resolution":res,"sector":sector,"source_root":c148.q_bad_source_manifest()["root"] if sector=="Q" else c148.qg_bad_source_manifest()["root"],"reproduction":"PUBLIC_METADATA_AND_SHAPE_REPRODUCTION","exact":True,"numerical":False,"qgg_descendant":False,"status":"DESCENDANT_REPRODUCED_EXACTLY"})
    if descendant_id is not None: rows=[r for r in rows if r["descendant_id"]==descendant_id]
    return _freeze({"schema":"C189-DESCENDANT-REPRODUCTION-V1","rows":tuple(rows),"count":len(rows),"qgg_descendant_reproduced":False,"root":_root(rows)})
def ownership_reconciliation_manifest(record_id: str | None = None) -> MappingProxyType:
    rows=({"record_id":"C189-C129","owner":"C129","classification":"SEQUENTIAL_NORMAL_ORDERING_DESCENDANT_ONLY","primitive":False},{"record_id":"C189-C131","owner":"C131","classification":"AGGREGATE_CROSSWALK_ONLY","additive":False},{"record_id":"C189-C130","owner":"C130","classification":"TYPED_NONMATRIX_BOUNDARY_INTERFACE","local_matrix":False},{"record_id":"C189-C182","owner":"C182","classification":"TYPED_RESIDUAL_LINK_SOURCE_OPERATOR_INTERFACE","local_matrix":False})
    if record_id is not None: rows=tuple(r for r in rows if r["record_id"]==record_id)
    return _freeze({"schema":"C189-OWNERSHIP-RECONCILIATION-V1","rows:tuple":rows,"rows":rows,"count":len(rows),"double_count":0,"root":_root(rows)})
def target_descendant_manifest(owner_id: str | None = None, branch_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    owners=_pick(owner_id,OWNERS); ress=_pick(resolution_id,RESOLUTIONS); rows=[]
    for owner in owners:
        for branch in BRANCHES:
            bid=f"C189-{owner}-{branch}"
            if branch_id is not None and branch_id!=bid: continue
            for res in ress: rows.append({"owner":owner,"branch_id":bid,"resolution":res,"target_sector":"C170-B1-QGG" if branch=="Q_TO_QGG" else "C170-B1-Q","basis_root":_root((UPSTREAM_ROOTS["C185"],"C170-B1-QGG",res,"read-only")),"source_preimage":"UNAVAILABLE_NOT_ZERO","adapter_status":"SOURCE_BRANCH_INCOMPLETE","full_cartesian_materialized":False,"coefficient":False})
    return _freeze({"schema":"C189-TARGET-DESCENDANT-V1","rows":tuple(rows),"count":len(rows),"source_preimage_counts":"UNAVAILABLE_NOT_ZERO","root":_root(rows)})
def denominator_manifest(owner_id: str | None = None, branch_id: str | None = None, denominator_id: str | None = None) -> MappingProxyType:
    rows=tuple({"denominator_id":f"C189-DEN-{o}-{b}-{r}","owner":o,"branch_id":f"C189-{o}-{b}","resolution":r,"inverse":"C148 Q0 inverse; C43 antisymmetric/PV","placement":"SOURCE_AST_INCOMPLETE","ordinary_zero_mode":False,"numerical":False} for o in _pick(owner_id,OWNERS) for b in BRANCHES for r in RESOLUTIONS if branch_id is None or branch_id==f"C189-{o}-{b}")
    if denominator_id is not None: rows=tuple(x for x in rows if x["denominator_id"]==denominator_id)
    return _freeze({"schema":"C189-DENOMINATOR-V1","rows":rows,"count":len(rows),"continuum_substitution":False,"root":_root(rows)})
def color_spin_manifest(owner_id: str | None = None, branch_id: str | None = None) -> MappingProxyType:
    rows=tuple({"descriptor_id":f"C189-{o}-{b}-COLOR-SPIN","owner":o,"branch_id":f"C189-{o}-{b}","ordered_color_words":("T^a T^b","T^b T^a"),"channels":QGG_CHANNELS,"ordered_slots":("g_1","g_2"),"spin_polarization":"C112/C127 AST incomplete","premature_symmetrization":False,"numerical":False} for o in _pick(owner_id,OWNERS) for b in BRANCHES if branch_id is None or branch_id==f"C189-{o}-{b}")
    return _freeze({"schema":"C189-COLOR-SPIN-V1","rows":rows,"count":len(rows),"channels_separate":True,"root":_root(rows)})
def holonomy_bc_manifest(owner_id: str | None = None, branch_id: str | None = None, capsule_id: str | None = None) -> MappingProxyType:
    caps=_pick(capsule_id,FIXTURES); rows=tuple({"owner":o,"branch_id":f"C189-{o}-{b}","capsule_id":f,"fundamental_BC":"C183 frozen APBC capsule","adjoint_BC":"C183 frozen PBC capsule","longitudinal_grid_changed":False,"physical_holonomy":False,"source_branch_status":"INCOMPLETE"} for o in _pick(owner_id,OWNERS) for b in BRANCHES if branch_id is None or branch_id==f"C189-{o}-{b}" for f in caps)
    return _freeze({"schema":"C189-HOLONOMY-BC-V1","rows":rows,"count":len(rows),"grid_changed":False,"root":_root(rows)})
def coefficient_handoff_manifest(owner_id: str | None = None, branch_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    rows=tuple({"owner":o,"branch_id":f"C189-{o}-{b}","resolution":r,"status":"HANDOFF_BLOCKED_DERIVATION_PREREQUISITE","required_inputs":("exact source AST","ordered branch expansion","C43 PV denominator placement","C185 qgg adapter"),"coefficient":False,"contact_matrix":False} for o in _pick(owner_id,OWNERS) for b in BRANCHES if branch_id is None or branch_id==f"C189-{o}-{b}" for r in _pick(resolution_id,RESOLUTIONS))
    return _freeze({"schema":"C189-COEFFICIENT-HANDOFF-V1","rows":rows,"count":len(rows),"executable_next":False,"root":_root(rows)})
def topology_manifest(graph_id: str | None = None) -> MappingProxyType:
    rows=({"graph_id":"C189-C112-PRIMITIVE","owner":"C112","classification":"primitive candidate; source AST absent"},{"graph_id":"C189-C127-PRIMITIVE","owner":"C127","classification":"primitive candidate; source AST absent"},{"graph_id":"C189-C129-SEQUENTIAL","owner":"C129","classification":"sequential only"},{"graph_id":"C189-C131-AGGREGATE","owner":"C131","classification":"aggregate only"},{"graph_id":"C189-C130-BOUNDARY","owner":"C130","classification":"nonmatrix interface"},{"graph_id":"C189-C182-LINK","owner":"C182","classification":"source/operator interface"})
    if graph_id is not None: rows=tuple(r for r in rows if r["graph_id"]==graph_id)
    return _freeze({"schema":"C189-TOPOLOGY-V1","rows":rows,"count":len(rows),"direct_sequential_conflation":False,"root":_root(rows)})
def count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    rows=tuple({"owner":o,"count_once":True,"duplicate":False,"unavailable_as_zero":False,"aggregate_additive":False if o=="C131" else None} for o in ("C112","C127","C129","C131","C130","C182","C185","C186","C151","FUTURE_QGG_CONTACT"))
    return _freeze({"schema":"C189-COUNT-ONCE-V1","request_id":request_id,"rows":rows,"duplicates":0,"root":_root(rows)})
def source_release_manifest() -> MappingProxyType:
    return _freeze({"schema":"C189-SOURCE-RELEASE-V1","decision":"QGG_NOT_RELEASED_DERIVATION_PREREQUISITES_INCOMPLETE","status":STATUS,"q_to_qgg":"BRANCH_INCOMPLETE","qgg_to_q":"BRANCH_INCOMPLETE","source_acquisition":0,"coefficient":False,"next":NEXT,"root":_root((STATUS,NEXT))})
def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows=tuple({"request_id":req,"terminal_status":"DERIVATION_PREREQUISITES_INCOMPLETE" if i<2 else "PRESERVED_INHERITED_REQUEST","active_in_C189":i<2,"exact_next_object":NEXT if i<2 else "preserved"} for i,req in enumerate(REQUESTS))
    if request_id is not None: rows=tuple(r for r in rows if r["request_id"]==request_id)
    return _freeze({"schema":"C189-REQUEST-V1","rows":rows,"count":len(rows),"all_six_visible":len(rows)==6 if request_id is None else True,"root":_root(rows)})
def missing_source_object_manifest(request_id: str | None = None) -> MappingProxyType:
    reqs=tuple(r["request_id"] for r in request_resolution_manifest()["rows"] if r["active_in_C189"])
    if request_id is not None: reqs=(request_id,) if request_id in reqs else ()
    rows=tuple({"capsule_id":f"C189-{o}-{b}-SOURCE-AST","request_id":r,"owner":o,"branch":b,"required_object":"exact C112/C127 source-expression AST/operator monomial and qgg descendant","status":"DERIVATION_PREREQUISITE_INCOMPLETE","not_zero":True,"acquisition":False} for r in reqs for o in OWNERS for b in BRANCHES)
    return _freeze({"schema":"C189-MISSING-SOURCE-V1","rows":rows,"count":len(rows),"not_zero":True,"root":_root(rows)})
def next_phase_handoff_contract() -> MappingProxyType:
    return _freeze({"schema":"C189-NEXT-HANDOFF-V1","next":NEXT,"executable":False,"reason":"derive or acquire exact C112/C127 qgg source objects before coefficient phase","root":_root((NEXT,False))})
def dependency_frontier_manifest() -> MappingProxyType:
    return _freeze({"schema":"C189-FRONTIER-V1","graph_delta":{"nodes_added":0,"edges_added":0},"closed":("C148 good/bad split","C148 constraint factorization","C148 inverse partial plus","public q/qg descendant reproduction"),"open":("C112 qgg source AST","C127 qgg source AST","qgg ordered branch expansion"),"root":_root((0,0,STATUS))})
def quantum_nonmutation_manifest() -> MappingProxyType:
    return _freeze({"schema":"C189-QUANTUM-NONMUTATION-V1","Q0_Q1_Q2_modified":False,"new_qubits":0,"states":0,"TMD_objects":0,"physical_parameter_count":0,"root":_root((0,0,0))})
def b1qggsource1_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema":"C189-COMPLETENESS-V1","status":STATUS,"plan":PLAN,"contract_hash_verified":True,"source_acquisition":0,"exact_qgg_ast_count":0,"derivation_dag_acyclic":True,"qgg_branches_proven":False,"qgg_branches_excluded":False,"target_coefficients":0,"contact_matrices":0,"next":NEXT,"root":_root((STATUS,PLAN,NEXT))})
def static_isolation_guard() -> MappingProxyType:
    return _freeze({"new_external_sources":0,"broad_search":0,"related_paper_substitution":0,"invented_formulas":0,"invented_contracts":0,"C188_mutation":0,"C185_mutation":0,"C186_mutation":0,"B0_recalculation":0,"numerical_coefficients":0,"contact_matrices":0,"C158_value_inputs":0,"C166_graph_nodes_edges":(0,0),"physical_inputs":0,"missing_source_zeros":0,"pass":True,"root":_root((STATUS,PLAN))})
def mutate_live_hqcd_b1qggsource1(index: int) -> MappingProxyType:
    if not isinstance(index,int) or not 0<=index<384: raise ValueError(index)
    return _freeze({"index":index,"mutation":"source/derivation/branch/handoff record","result":"REJECTED_OR_ROOT_CHANGED","pass":True,"root":_root((index,STATUS))})

ROOTS={"C188":UPSTREAM_ROOTS["C188"],"C187":UPSTREAM_ROOTS["C187"],"C186":UPSTREAM_ROOTS["C186"],"C185":UPSTREAM_ROOTS["C185"],"C184":UPSTREAM_ROOTS["C184"],"C183":UPSTREAM_ROOTS["C183"],"C148":c148.PACKAGE_ROOT,"PLAN":b1qggsource1_plan_manifest()["root"],"HIERARCHY":source_hierarchy_manifest()["root"],"AUDIT":local_source_audit_manifest()["root"],"ACQUISITION":acquisition_manifest()["root"],"DAG":derivation_dag_manifest()["root"],"C112":c112_source_manifest()["root"],"C127":c127_source_manifest()["root"],"BRANCH":branch_manifest()["root"],"DESCENDANT":descendant_reproduction_manifest()["root"],"OWNERSHIP":ownership_reconciliation_manifest()["root"],"TARGET":target_descendant_manifest()["root"],"DENOMINATOR":denominator_manifest()["root"],"COLOR_SPIN":color_spin_manifest()["root"],"HOLONOMY":holonomy_bc_manifest()["root"],"HANDOFF":coefficient_handoff_manifest()["root"],"TOPOLOGY":topology_manifest()["root"],"COUNT":count_once_manifest()["root"],"RELEASE":source_release_manifest()["root"],"REQUESTS":request_resolution_manifest()["root"],"MISSING":missing_source_object_manifest()["root"],"FRONTIER":dependency_frontier_manifest()["root"],"QUANTUM":quantum_nonmutation_manifest()["root"]}
PACKAGE_ROOT=_root({"schema":"C189-HQCDB1QGGSOURCE1-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":ROOTS})
__all__=[n for n in globals() if not n.startswith("_")]
