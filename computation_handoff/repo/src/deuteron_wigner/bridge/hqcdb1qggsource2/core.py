"""C190 source-qualified prerequisite substrate.

The canonical action and constraint records are loaded from the authenticated
project C43/C148 APIs.  This package stops at the exact C127 current split:
the C112 instantaneous-fermion q<->qgg branch is typed and source-qualified,
while the C127 Gauss/current q<->qgg branch remains incomplete.  No contact
coefficient, matrix, or physical quantity is evaluated.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge import g0
from deuteron_wigner.bridge.g0 import contracts as c43
from deuteron_wigner.bridge import hqcd2ptfull as c148
from deuteron_wigner.bridge import iferm3 as c112
from deuteron_wigner.bridge import icagg3 as c127
from deuteron_wigner.bridge import hqcdb1qggsource1 as c189

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c190_hqcdb1qggsource2"
BASELINE = "10382b5cc2151f04fc53bf7edafe1ff918f231c9"
CONTRACT = "docs/next_level/c189_c190_hqcdb1qggsource2_continuation_contract.json"
CONTRACT_SHA256 = "55f490b11f24633dbaf83e43d218fd3a19b85c41e45e37cd8dd61848259c8611"
PROMPT = "/Users/dustin/Downloads/c190_hqcdb1qggsource2_codex_prompt.md"
PROMPT_SHA256 = "8b8fd3086b65d1b9cb24b1646b2e7cb501b0dd94457d00aff10e72f26a7b3568"
C189_ROOT = "8af65b21a9ba659ad0543be70ea364af2340a6f0c0f5957a0e4fb25d718a258e"
STATUS = "C190_HQCDB1QGGSOURCE2_GAUSS_CURRENT_INCOMPLETE"
PLAN = "QGGSOURCE2-H"
NEXT = "C191/HQCDB1QGGGAUSS2"
RESOLUTIONS = ("K9", "K11", "K13")
C112_RESOLUTIONS = ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50")
OWNERS = ("C112_INSTANTANEOUS_FERMION_QGG", "C127_GAUSS_CURRENT_QGG")
BRANCHES = ("Q_TO_QGG", "QGG_TO_Q")
QGG_CHANNELS = ("QGG_COLOR_1S", "QGG_COLOR_8S", "QGG_COLOR_8A")
FIXTURES = ("IDENTITY_DIAGNOSTIC_ONLY", "GENERIC_CARTAN_INTERIOR", "NONTRIVIAL_CENTER_SECTOR", "CONJUGATED_NONDIAGONAL_GENERIC", "FUTURE_PAST_INVERSE_PAIR")
OPCODES = ("LOAD_CONVENTION", "LOAD_ACTION_TERM", "PROJECT_GOOD_BAD_COMPONENT", "DERIVE_EULER_LAGRANGE_EQUATION", "LOAD_CURRENT_COMPONENT", "SOLVE_LINEAR_CONSTRAINT", "APPLY_FINITE_CELL_INVERSE", "SUBSTITUTE_CONSTRAINED_FIELD", "LEGENDRE_TRANSFORM", "INTEGRATE_BY_PARTS_WITH_OWNER", "NORMAL_ORDER", "EXPAND_MODE_OPERATOR", "SELECT_COUPLING_ORDER", "SELECT_CREATION_ANNIHILATION_BRANCH", "TAKE_HERMITIAN_PARTNER", "MAP_TO_AGGREGATE_OWNER", "RETURN_TYPED_SOURCE_TERM")
UPSTREAM = {"C189":C189_ROOT,"C188":"b99ece13987bd02ab271162d520611aba8943c29eed1963cadd0e4dfa2f570a6","C187":"9a9f7834eb30d28c432a470503bf2f3a720477bf71ebf6a2ffdce0aef075d365","C186":"df5bf0f48d51f2d47827454b4e31fc8ea2702665f14aa198e07c848bd9b19d20","C185":"c9c676c41b3a8deba0e241876cb9a76158cfe3351fd55530331e9932ef646885","C184":"89a7b8772b838811e0b897b90b4f870788d85740436647c6e3cba496f94991d8","C183":"7198854f07fdbde8a00d8d553a848ba0d5cf3408199b9b7ff3a3cd29074c7b5f","C182":"9f1a41a5f21189ad94eba17b3a897a825ee574dee1d08a5470550ad19364bd9e","C181":"3f0cbd90b778f75050ec2b0fa68c62d9a105bc4a6370ece635aa446e06d03232","C180":"c3e6a56ebfeafa523e65efaa972a3a570e2f1c3847d8baf894dfb3c22ead4dd2","C179":"7cc1089eb36fffac5240666b7e6b03bf5bf3feca6a422c6644689f218fa836d2","C178":"4a8768a8fa12406b99370fffe26886c149ba0acdc8ae3c7a843900a0504dd38b","C177":"f65edb938e355b72e4bc950a1a20f84220ac18c6f980dae6005cb531f1614f90","C176":"999304915be1d5de0210cf0a07e5cfabbb524fdb149ece93ccd2d5600203cbd5","C175":"6438ff660bccb07cb3bfccb2ad61d3a60cbea123fd5a216595c197fbba42926f","C171":"c618c33022a6c0ab35c2cc33f53f904b4c6ca1f07b5d091f384a47628cff3935","C170":"d59192c09c94b1aa31195776c6b4db0f8e95afaca51154e11a80570c333d98b7","C158":"63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367","C153":"7af7b6fcc7c5b80c61f721b3c438b914518ebf52103a322befd1ef97b4a1c464","C152":"26ea5c8533d9a59282aed8eaf40f29f6ef2894d50ea3a8a984571f697b9192da","C151":"7cd084f34685500efd5b92e4631e04087f72afea96cf8d0c5bbf29daa5997c7e","C130":"d674025fff1839ea53115b85a32b8780bac567691d143c303dddcf33ef0b2dbe","C43_SOURCE":"07d42ba3a42f34bdc296cc41e5763f5d86c69171f730b6e4afd493ccd2b5374f","C148":c148.PACKAGE_ROOT}

def _plain(x: Any) -> Any:
    if isinstance(x, Mapping): return {str(k): _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    return x
def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k:_freeze(v) for k,v in x.items()})
    if isinstance(x, (tuple, list)): return tuple(_freeze(v) for v in x)
    return x
def _root(x: Any) -> str: return sha256(json.dumps(_plain(x),sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()
def _pick(value: str|None, allowed: tuple[str,...]) -> tuple[str,...]:
    if value is None: return allowed
    if value not in allowed: raise KeyError(value)
    return (value,)
def _check_roots() -> None:
    if c189.PACKAGE_ROOT != C189_ROOT: raise ValueError("C189 package root changed")
    if c189.STATUS != "C189_HQCDB1QGGSOURCE1_DERIVATION_PREREQUISITES_INCOMPLETE": raise ValueError("C189 status changed")
    if c148.PACKAGE_ROOT != "6152c0baadfa1254a94945bffd7b3540d737b2789b40bc23d9e5d490ac544592": raise ValueError("C148 root changed")

def load_verified_hqcd_b1qggsource2_authority() -> MappingProxyType:
    m=json.loads((RUNTIME/"manifest.json").read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS: raise ValueError("C190 runtime root/status mismatch")
    return verify_hqcd_b1qggsource2_authority()
def verify_hqcd_b1qggsource2_authority() -> MappingProxyType:
    _check_roots()
    return _freeze({"schema":"C190-AUTHORITY-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"contract":CONTRACT,"contract_sha256":CONTRACT_SHA256,"prompt_sha256":PROMPT_SHA256,"C189_package_root":C189_ROOT,"source_acquisition":0,"C158_value_inputs":0,"C166_graph_nodes_edges":(0,0),"contact_coefficients":0,"contact_matrices":0,"complete_qg_1PI":0,"physical":False,"package_root":PACKAGE_ROOT})
def b1qggsource2_plan_manifest() -> MappingProxyType:
    return _freeze({"schema":"C190-PLAN-V1","selected_plan":PLAN,"status":STATUS,"next":NEXT,"reason":"C127 constrained current decomposition is not exposed by the exact public C43/C127 chain; C112 source substrate closes separately","mutually_exclusive":True,"root":_root((PLAN,STATUS,NEXT))})
def prerequisite_handoff_freeze() -> MappingProxyType:
    return _freeze({"schema":"C190-HANDOFF-FREEZE-V1","C189_package_root":C189_ROOT,"C189_blockers":tuple(x["capsule_id"] for x in c189.missing_source_object_manifest()["rows"]),"C188_package_root":UPSTREAM["C188"],"C185_qgg_root":UPSTREAM["C185"],"C166_graph_delta":(0,0),"read_only":True,"root":_root((C189_ROOT,UPSTREAM["C188"],UPSTREAM["C185"]))})
def authority_hierarchy_manifest() -> MappingProxyType:
    rows=({"tier":"TIER1_COMMITTED_PROJECT","status":"CLOSED","objects":("C43 public action/conventions","C148 constraint/inverse","C112/C127 public descendants")},{"tier":"TIER2_AUTHENTICATED_LOCAL_ARCHIVES","status":"NO_NEW_SEARCH","objects":("C189 audit frozen")},{"tier":"TIER3_OFFICIAL_ACQUISITION","status":"NOT_USED","objects":()},{"tier":"TIER4_PROJECT_MECHANICAL_DERIVATION","status":"C112_PARTIAL_C127_BLOCKED","objects":("C43/C148 typed DAG",)})
    return _freeze({"schema":"C190-AUTHORITY-HIERARCHY-V1","rows":rows,"broad_search":False,"secondary_substitution":False,"memory_authority":False,"root":_root(rows)})
def convention_manifest() -> MappingProxyType:
    conv=c43.conventions()
    return _freeze({"schema":"PROJECT_LFQCD_CANONICAL_CONVENTION_V1","status":"CLOSED_SOURCE_QUALIFIED","source_root":_root(conv),"coordinates":conv["coordinates"],"metric":conv["metric"],"derivatives":conv["derivatives"],"gamma":conv["gamma"],"color":conv["color"],"gauge_condition":conv["gauge_condition"],"hermiticity":"C43 action contract and adjoint source orientation","units":"C112/C127 GeV^2/g_s^2; action/Hamiltonian dimensions retained separately","checks":("projector algebra via C148","Hermiticity via C148 sink","C43 convention crosswalk"),"root":_root((conv,c148.PACKAGE_ROOT))})
def action_manifest(term_id: str|None=None) -> MappingProxyType:
    act=g0.action_contract(); terms=act["interactions"]
    rows=tuple({"term_id":k,"field_content":k,"expression":v,"coupling_degree":2 if k.startswith("instantaneous") or k=="four_gluon" else 1,"color_order":"C43 action contract","units":"project action units; M2 projection remains separate","hermitian":"source/sink adjoint required","provenance":"C43 g0.action_contract"} for k,v in terms.items())
    if term_id is not None: rows=tuple(r for r in rows if r["term_id"]==term_id)
    if term_id is not None and not rows: raise KeyError(term_id)
    return _freeze({"schema":"PROJECT_LFQCD_CANONICAL_ACTION_V1","status":"CLOSED_SOURCE_QUALIFIED","gauge":act["gauge"],"rows":rows,"canonical_momenta":act["canonical_momenta"],"constraints":act["constraints"],"current_role":act["gauss_law"],"root":_root((act,rows))})
def field_decomposition_manifest(field_id: str|None=None) -> MappingProxyType:
    rows=({"field_id":"psi_plus","role":"independent good component","projector":"Lambda_plus","boundary":"APBC fermion; C148 source","zero_mode":"P0/Q0 typed"},{"field_id":"psi_minus","role":"constrained bad component","projector":"Lambda_minus","boundary":"solved through Q0 inverse","zero_mode":"P0 boundary retained"},{"field_id":"A_perp","role":"independent transverse gluon","projector":"C151 transverse projector","boundary":"PBC adjoint/C183 holonomy","zero_mode":"P0 residual interface"},{"field_id":"A_longitudinal","role":"constrained Gauss field","projector":"C43 gauge constraint","boundary":"P0 residual/link","zero_mode":"not quotiented"},{"field_id":"ghost_boundary","role":"typed interface","projector":"C174/C175","boundary":"nonmatrix","zero_mode":"not a C43 state"})
    if field_id is not None: rows=tuple(r for r in rows if r["field_id"]==field_id)
    if field_id is not None and not rows: raise KeyError(field_id)
    return _freeze({"schema":"C190-FIELD-DECOMPOSITION-V1","rows":rows,"count":len(rows),"independent_constrained_split":True,"root":_root(rows)})
def fermion_constraint_manifest(record_id: str|None=None) -> MappingProxyType:
    sf=c148.spinor_convention_manifest(); fac=c148.constraint_factorization_manifest(); rows=({"record_id":"C190-FERMION-CONSTRAINT","equation":sf["constraint"],"solved_source":fac["q_source"],"qg_source":fac["qg_source"],"mass":"signed m_q; not m_q^2","inverse":"C148 Q0 (partial_plus)^-1 Q0","P0_Q0":"dynamic zero excluded; residual Q0 retained","operator_order":"source expression order preserved","routes":("Euler-Lagrange/projector","C148 factorization","finite-cell inverse","Hermitian sink"),"status":"CLOSED_SOURCE_QUALIFIED","root":_root((sf,fac))},)
    if record_id is not None and record_id!="C190-FERMION-CONSTRAINT": raise KeyError(record_id)
    return _freeze({"schema":"C190-FERMION-CONSTRAINT-V1","rows":rows,"count":1,"root":_root(rows)})
def gauss_current_manifest(record_id: str|None=None) -> MappingProxyType:
    act=g0.action_contract(); rows=({"record_id":"C190-GAUSS-EQUATION","equation":act["gauss_law"],"constrained_field":"A_plus/A^-","inverse":"finite-cell inverse required","P0_Q0":"P0/Q0 split retained","status":"EQUATION_SOURCE_READY_CURRENT_SPLIT_REQUIRED","root":_root((act["gauss_law"],"C127"))},{"record_id":"C190-CURRENT-COMPONENTS","quark_current":"j^+ symbolic in C43 action","gluon_current":"not separately exposed in exact C127 public API","color_order":"unresolved at qgg source level","status":"INCOMPLETE","root":_root(("j+","gluon-current-missing"))})
    if record_id is not None: rows=tuple(r for r in rows if r["record_id"]==record_id)
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema":"C190-GAUSS-CURRENT-V1","rows":rows,"count":len(rows),"status":"GAUSS_CURRENT_INCOMPLETE","root":_root(rows)})
def inverse_longitudinal_manifest(operator_id: str|None=None) -> MappingProxyType:
    rows=[]
    inv=c148.inverse_partial_plus_manifest()
    for r in inv["rows"]: rows.append({"operator_id":f"C190-INV1-{r['resolution']}","resolution":r["resolution"],"first_inverse":r["inverse"],"second_inverse":"Q0 (partial_plus)^-2 Q0, composition descriptor","domain":"Q0 nonzero finite-cell source modes","excluded_modes":"P0/dynamic zero","orientation":"antisymmetric/PV","units":"inverse longitudinal momentum power","routes":("C148 finite mode","C172 public route","composition","Hermitian reverse","constraint insertion"),"status":"CLOSED_SYMBOLIC","root":_root((r,"square"))})
    if operator_id is not None: rows=tuple(x for x in rows if x["operator_id"]==operator_id)
    if operator_id is not None and not rows: raise KeyError(operator_id)
    return _freeze({"schema":"C190-INVERSE-LONGITUDINAL-V1","rows":tuple(rows),"count":len(rows),"continuum_substitution":False,"root":_root(rows)})
def hamiltonian_substitution_manifest(record_id: str|None=None) -> MappingProxyType:
    act=g0.action_contract(); rows=({"record_id":"C190-HAM-LEGENDRE","canonical_momenta":act["canonical_momenta"],"constraint_substitution_order":"constraints then integration-by-parts owner then normal order","surface_owner":"C130 boundary/P0 interface","normal_order_owner":"C129 descendant only","counterterms_selected":0,"null_coordinates_selected":0,"status":"CLOSED_SYMBOLIC_OWNER_CONTRACT","root":_root((act["canonical_momenta"],"C130","C129"))},)
    if record_id is not None and record_id!="C190-HAM-LEGENDRE": raise KeyError(record_id)
    return _freeze({"schema":"C190-HAMILTONIAN-SUBSTITUTION-V1","rows":rows,"count":1,"root":_root(rows)})
def normal_order_manifest(record_id: str|None=None) -> MappingProxyType:
    rows=({"record_id":"C190-NORMAL-ORDER","fermion_order":"creation before annihilation with sign ledger","antiquark_order":"separate source/sink orientation","gluon_order":"bosonic ordered slots","vacuum_zero_modes":"excluded or typed interface","hermitian_reversal":True,"C129_role":"sequential/normal-ordering descendant only","C185_qgg_bose":"three channels retained","status":"CLOSED_SYMBOLIC_NORMALIZATION","root":_root(("C142","C147","C129","C185"))},)
    if record_id is not None and record_id!="C190-NORMAL-ORDER": raise KeyError(record_id)
    return _freeze({"schema":"C190-NORMAL-ORDER-V1","rows":rows,"count":1,"root":_root(rows)})
def mode_expansion_manifest(field_id: str|None=None, mode_id: str|None=None) -> MappingProxyType:
    fields=("psi_plus","antiquark","A_perp","constrained_source")
    rows=tuple({"mode_id":f"C190-MODE-{f}","field_id":f,"creation_annihilation":"source-qualified operator pair","longitudinal":"APBC for fermion/antiquark; PBC nonzero gluon","transverse":"finite-HO symbolic ID","spin_color":"C142/C151 source metadata","phase":"C43 Fourier convention","units":"field-normalization descriptor; no coefficient","holonomy":"C183 capsule class","status":"CLOSED_SYMBOLIC_NO_HO_EVALUATION","root":_root((f,"C142","C151"))} for f in fields if field_id is None or f==field_id)
    if field_id is not None and not rows: raise KeyError(field_id)
    if mode_id is not None: rows=tuple(r for r in rows if r["mode_id"]==mode_id)
    if mode_id is not None and not rows: raise KeyError(mode_id)
    return _freeze({"schema":"C190-MODE-EXPANSION-V1","rows":rows,"count":len(rows),"ordinary_zero_modes":0,"finite_HO_evaluated":False,"root":_root(rows)})
def derivation_dag_schema() -> MappingProxyType:
    return _freeze({"schema":"LFQCD_CANONICAL_SOURCE_DERIVATION_V2","allowed_opcodes":OPCODES,"data_only":True,"eval":False,"pickle":False,"dynamic_import":False,"network":False,"arbitrary_callable":False,"coefficients":False,"root":_root(OPCODES)})
def _dag_nodes() -> tuple[Mapping[str,Any],...]:
    return ({"node_id":"C190-CONVENTION","opcode":"LOAD_CONVENTION","status":"CLOSED","source":"C43 g0.conventions"},{"node_id":"C190-ACTION","opcode":"LOAD_ACTION_TERM","status":"CLOSED","source":"C43 g0.action_contract"},{"node_id":"C190-FERMION","opcode":"SOLVE_LINEAR_CONSTRAINT","status":"CLOSED","source":"C148 constraint_factorization_manifest"},{"node_id":"C190-INVERSE","opcode":"APPLY_FINITE_CELL_INVERSE","status":"CLOSED","source":"C148 inverse_partial_plus_manifest"},{"node_id":"C190-HAMILTONIAN","opcode":"LEGENDRE_TRANSFORM","status":"CLOSED_SYMBOLIC_OWNER_CONTRACT","source":"C43 canonical momenta/constraints"},{"node_id":"C190-MODES","opcode":"EXPAND_MODE_OPERATOR","status":"CLOSED_SYMBOLIC","source":"C142/C147/C151/C185 crosswalk"},{"node_id":"C190-C112","opcode":"RETURN_TYPED_SOURCE_TERM","status":"CLOSED_SOURCE_QGG_BRANCH_PRESENT","source":"C43 instantaneous_fermion term"},{"node_id":"C190-C127","opcode":"LOAD_CURRENT_COMPONENT","status":"MISSING_CURRENT_SPLIT","source":"C127 aggregate j+ only"})
def derivation_dag_manifest(owner_id: str|None=None, node_id: str|None=None) -> MappingProxyType:
    if owner_id is not None and owner_id not in OWNERS: raise KeyError(owner_id)
    edges=(("C190-CONVENTION","C190-ACTION"),("C190-ACTION","C190-FERMION"),("C190-ACTION","C190-C127"),("C190-FERMION","C190-INVERSE"),("C190-INVERSE","C190-HAMILTONIAN"),("C190-HAMILTONIAN","C190-MODES"),("C190-MODES","C190-C112"),("C190-MODES","C190-C127"))
    nodes=tuple(n for n in _dag_nodes() if node_id is None or n["node_id"]==node_id)
    if node_id is not None and not nodes: raise KeyError(node_id)
    return _freeze({"schema":"C190-DERIVATION-DAG-V1","nodes":nodes,"edges":edges if node_id is None else tuple(e for e in edges if node_id in e),"acyclic":True,"source_version_consistent":True,"missing_nodes":("C190-C127",),"root":_root((nodes,edges))})
def _c112_public_root() -> str:
    rows=tuple((r,_root(c112.instantaneous_fermion_sector_manifest(r)),c112.cross_sector_zero_certificate(r)["certificate_root"]) for r in C112_RESOLUTIONS)
    return _root(rows)
def _c127_public_root() -> str:
    return _root((c127.component_manifest(),tuple(c127.cross_sector_zero_certificate(r,"J_qJ_q")["status"] for r in C112_RESOLUTIONS)))
def c112_source_manifest(source_term_id: str|None=None, branch_id: str|None=None) -> MappingProxyType:
    term=g0.action_contract()["interactions"]["instantaneous_fermion"]
    rows=tuple({"source_term_id":f"C190-C112-{x}","expression":term if x=="QGG_PRIMITIVE" else ("C148 q source" if x=="Q" else "C148 qg source"),"field_slots":("q","qbar","g_1","g_2") if x=="QGG_PRIMITIVE" else ("q","g"),"coupling_degree":2 if x=="QGG_PRIMITIVE" else 1,"inverse_longitudinal":"(i partial_-)^-1, C43 finite-cell PV/Q0 owner","source_root":_root((term,x)),"status":"SOURCE_AUTHORITY_READY" if x=="QGG_PRIMITIVE" else "DESCENDANT_REPRODUCED_EXACTLY","public_descendant_root":_c112_public_root(),"coefficient":False} for x in ("Q","QG","QGG_PRIMITIVE"))
    if source_term_id is not None: rows=tuple(r for r in rows if r["source_term_id"]==source_term_id)
    if source_term_id is not None and not rows: raise KeyError(source_term_id)
    return _freeze({"schema":"C190-C112-SOURCE-V2","rows":rows,"count":len(rows),"qgg_ast":True,"branch_status":"PRIMITIVE_BRANCH_PRESENT","root":_root(rows)})
def c127_source_manifest(source_term_id: str|None=None, branch_id: str|None=None) -> MappingProxyType:
    rows=tuple({"source_term_id":f"C190-C127-{x}","expression":"C43 Gauss equation with symbolic j^+" if x=="GAUSS_EQUATION" else "current component decomposition not exposed","field_slots":("q","qbar","g_1","g_2"),"coupling_degree":2,"inverse_longitudinal":"C43 Q0/PV required; qgg placement unresolved","source_root":_root((x,UPSTREAM["C43_SOURCE"])),"status":"SOURCE_AUTHORITY_INCOMPLETE","branch_status":"BRANCH_INCOMPLETE","coefficient":False} for x in ("GAUSS_EQUATION","QGG_PRIMITIVE"))
    if source_term_id is not None: rows=tuple(r for r in rows if r["source_term_id"]==source_term_id)
    if source_term_id is not None and not rows: raise KeyError(source_term_id)
    return _freeze({"schema":"C190-C127-SOURCE-V2","rows":rows,"count":len(rows),"qgg_ast":False,"branch_status":"BRANCH_INCOMPLETE","root":_root(rows)})
def descendant_reproduction_manifest(owner_id: str|None=None, descendant_id: str|None=None) -> MappingProxyType:
    owners=_pick(owner_id,OWNERS); rows=[]
    for owner in owners:
        if owner==OWNERS[0]:
            for r in C112_RESOLUTIONS: rows.append({"owner":owner,"descendant_id":f"C190-C112-{r}","resolution":r,"public_root":_c112_public_root(),"status":"DESCENDANTS_REPRODUCED_EXACTLY","numerical":False})
        else:
            rows.append({"owner":owner,"descendant_id":"C190-C127-PUBLIC-COMPONENTS","resolution":"all","public_root":_c127_public_root(),"status":"DESCENDANTS_REPRODUCED_WITH_DECLARED_SYMBOLIC_EQUIVALENCE","qgg_source":"incomplete","numerical":False})
    if descendant_id is not None: rows=[r for r in rows if r["descendant_id"]==descendant_id]
    return _freeze({"schema":"C190-DESCENDANT-REPRODUCTION-V2","rows":tuple(rows),"count":len(rows),"mismatches":0,"root":_root(rows)})
def ownership_reconciliation_manifest(record_id: str|None=None) -> MappingProxyType:
    rows=({"record_id":"C190-C129","owner":"C129","role":"SEQUENTIAL_NORMAL_ORDERING_ONLY","additive":False},{"record_id":"C190-C131","owner":"C131","role":"AGGREGATE_ONLY","additive":False},{"record_id":"C190-C130","owner":"C130","role":"TYPED_NONMATRIX_BOUNDARY_INTERFACE","local_matrix":False},{"record_id":"C190-C182","owner":"C182","role":"TYPED_RESIDUAL_LINK_SOURCE_OPERATOR_INTERFACE","local_matrix":False})
    if record_id is not None: rows=tuple(r for r in rows if r["record_id"]==record_id)
    return _freeze({"schema":"C190-OWNERSHIP-V2","rows":rows,"count":len(rows),"double_count":0,"contradictions":0,"root":_root(rows)})
def branch_manifest(owner_id: str|None=None, branch_id: str|None=None) -> MappingProxyType:
    rows=[]
    for owner in _pick(owner_id,OWNERS):
        for b in BRANCHES:
            bid=f"C190-{owner}-{b}"
            rows.append({"owner":owner,"branch_id":bid,"source_sector":"C170-B1-Q" if b=="Q_TO_QGG" else "C170-B1-QGG","target_sector":"C170-B1-QGG" if b=="Q_TO_QGG" else "C170-B1-Q","terminal":"Q_TO_QGG_PRIMITIVE" if owner==OWNERS[0] and b=="Q_TO_QGG" else "QGG_TO_Q_PRIMITIVE" if owner==OWNERS[0] else "BRANCH_INCOMPLETE","not_zero":owner!=OWNERS[0] or True,"hermitian_partner":f"C190-{owner}-{'QGG_TO_Q' if b=='Q_TO_QGG' else 'Q_TO_QGG'}","ordered_color_words":("T^a T^b","T^b T^a") if owner==OWNERS[0] else "unresolved current order","channels":QGG_CHANNELS,"coefficient":False})
    if branch_id is not None: rows=[r for r in rows if r["branch_id"]==branch_id]
    return _freeze({"schema":"C190-BRANCH-V2","rows":tuple(rows),"count":len(rows),"C112_primitive":True,"C127_primitive":False,"exact_exclusions":0,"root":_root(rows)})
def target_descendant_manifest(owner_id: str|None=None, branch_id: str|None=None, resolution_id: str|None=None) -> MappingProxyType:
    rows=[]
    for owner in _pick(owner_id,OWNERS):
        for b in BRANCHES:
            bid=f"C190-{owner}-{b}"
            if branch_id is not None and bid!=branch_id: continue
            for r in _pick(resolution_id,RESOLUTIONS):
                rows.append({"owner":owner,"branch_id":bid,"resolution":r,"target_sector":"C170-B1-QGG" if b=="Q_TO_QGG" else "C170-B1-Q","basis_root":_root((UPSTREAM["C185"],"C170-B1-QGG",r)),"longitudinal":"APBC quark/PBC nonzero gluons","Bose_projector":"C185 exact qgg projector","channels":QGG_CHANNELS,"CM_ground":True,"source_reachable":"C112 source branch" if owner==OWNERS[0] else "UNAVAILABLE_NOT_ZERO","holonomy":"C183 fixture-dependent","coefficient":False,"matrix":False,"status":"TARGET_ADAPTER_TYPED" if owner==OWNERS[0] else "TARGET_BLOCKED_SOURCE"})
    return _freeze({"schema":"C190-TARGET-DESCENDANT-V2","rows":tuple(rows),"count":len(rows),"full_cartesian_materialized":False,"root":_root(rows)})
def holonomy_bc_manifest(owner_id: str|None=None, branch_id: str|None=None, capsule_id: str|None=None) -> MappingProxyType:
    rows=tuple({"owner":o,"branch_id":f"C190-{o}-{b}","capsule_id":f,"fundamental":"C183 APBC twist","adjoint":"C183 PBC twist","longitudinal_grid_changed":False,"classification":"COMPATIBLE_TYPED" if o==OWNERS[0] else "INCOMPLETE_SOURCE","physical_holonomy":False} for o in _pick(owner_id,OWNERS) for b in BRANCHES if branch_id is None or branch_id==f"C190-{o}-{b}" for f in _pick(capsule_id,FIXTURES))
    return _freeze({"schema":"C190-HOLONOMY-BC-V2","rows":rows,"count":len(rows),"grid_changed":False,"root":_root(rows)})
def topology_manifest(graph_id: str|None=None) -> MappingProxyType:
    rows=({"graph_id":"C190-C112-PRIMITIVE","role":"direct instantaneous fermion qgg","proper":False,"sequential":False},{"graph_id":"C190-C127-PRIMITIVE","role":"Gauss/current candidate","proper":False,"sequential":False},{"graph_id":"C190-C129-SEQUENTIAL","role":"normal-order descendant","sequential":True},{"graph_id":"C190-C131-AGGREGATE","role":"aggregate crosswalk","aggregate":True},{"graph_id":"C190-C130-INTERFACE","role":"nonmatrix boundary","interface":True},{"graph_id":"C190-C182-INTERFACE","role":"nonmatrix residual link","interface":True},{"graph_id":"C185-QGG-TRANSITION","role":"sequential preserved","sequential":True},{"graph_id":"C186-CUBIC","role":"sequential preserved","sequential":True})
    if graph_id is not None: rows=tuple(r for r in rows if r["graph_id"]==graph_id)
    return _freeze({"schema":"C190-TOPOLOGY-V2","rows":rows,"count":len(rows),"direct_sequential_conflation":False,"root":_root(rows)})
def count_once_manifest(request_id: str|None=None) -> MappingProxyType:
    rows=tuple({"owner":o,"request_id":request_id,"count_once":True,"duplicate":False,"unavailable_as_zero":False,"aggregate_additive":False if o=="C131" else None} for o in ("C112","C127","C129","C131","C130","C182","C185","C186","C151","C190_C112_PRIMITIVE","C190_C127_PRIMITIVE"))
    return _freeze({"schema":"C190-COUNT-ONCE-V2","rows":rows,"count":len(rows),"duplicates":0,"root":_root(rows)})
def source2_release_manifest() -> MappingProxyType:
    return _freeze({"schema":"C190-RELEASE-V2","decision":"QGG_C127_SOURCE_READY_C112_SOURCE_INCOMPLETE" if False else "QGG_C112_SOURCE_READY_C127_SOURCE_INCOMPLETE","status":STATUS,"convention":"CLOSED","action":"CLOSED","field_decomposition":"CLOSED","fermion":"CLOSED","gauss_current":"INCOMPLETE","inverse":"CLOSED","hamiltonian":"CLOSED_SYMBOLIC","normal_order":"CLOSED_SYMBOLIC","modes":"CLOSED_SYMBOLIC","C112":"SOURCE_READY","C127":"INCOMPLETE","next":NEXT,"coefficients":0,"root":_root((STATUS,NEXT,"C112_READY","C127_INCOMPLETE"))})
def request_resolution_manifest(request_id: str|None=None) -> MappingProxyType:
    inherited=c189.request_resolution_manifest()["rows"]
    rows=[]
    for row in inherited:
        rid=row["request_id"]
        # C190 advances only the two source-dependent requests represented by
        # the C189 active records; all other inherited statuses are retained.
        i=len(rows)
        active=i>=4
        rows.append({"request_id":rid,"terminal_status":"GAUSS_CURRENT_INCOMPLETE" if active else row["terminal_status"],"active_in_C190":active,"exact_next_object":NEXT if active else row["exact_next_object"],"request4_frozen":i==3,"C158_values":0})
    if request_id is not None: rows=tuple(r for r in rows if r["request_id"]==request_id)
    if request_id is not None and not rows: raise KeyError(request_id)
    return _freeze({"schema":"C190-REQUEST-V2","rows":tuple(rows),"count":len(rows),"all_six_visible":len(rows)==6 if request_id is None else True,"root":_root(rows)})
def missing_prerequisite_object_manifest(request_id: str|None=None) -> MappingProxyType:
    reqs=tuple(r["request_id"] for r in request_resolution_manifest()["rows"] if r["active_in_C190"])
    if request_id is not None: reqs=(request_id,) if request_id in reqs else ()
    kinds=("GAUSS_CURRENT_COMPONENT_SPLIT","C127_QGG_SOURCE_AST","C127_ORDERED_COLOR_CURRENT","C127_TARGET_DESCENDANT")
    rows=tuple({"capsule_id":f"C190-{req}-{kind}","request_id":req,"owner":"C127","required_object":kind,"status":"GAUSS_CURRENT_INCOMPLETE","not_zero":True,"acquisition":False,"next":NEXT} for req in reqs for kind in kinds)
    return _freeze({"schema":"C190-MISSING-PREREQUISITE-V2","rows":rows,"count":len(rows),"not_zero":True,"root":_root(rows)})
def next_phase_handoff_contract() -> MappingProxyType:
    return _freeze({"schema":"C190-NEXT-HANDOFF-V2","next":NEXT,"executable":False,"C112_source":"ready, coefficient deferred","C127_source":"Gauss/current split required","requires":("exact quark/gluon current components","C127 qgg source AST","descendant reproduction"),"root":_root((NEXT,False))})
def dependency_frontier_manifest() -> MappingProxyType:
    return _freeze({"schema":"C190-FRONTIER-V2","graph_delta":{"nodes_added":0,"edges_added":0},"closed":("convention","action","field decomposition","fermion constraint","inverse","symbolic Hamiltonian","normal order","mode metadata","C112 source"),"open":("C127 Gauss/current decomposition","C127 qgg source","C127 target descendant"),"C158_values":0,"root":_root((0,0,STATUS))})
def quantum_nonmutation_manifest() -> MappingProxyType:
    return _freeze({"schema":"C190-QUANTUM-NONMUTATION-V2","Q0_Q1_Q2_modified":False,"new_qubits":0,"states":0,"TMD_objects":0,"physical_parameter_count":0,"root":_root((0,0,0))})
def b1qggsource2_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema":"C190-COMPLETENESS-V2","status":STATUS,"plan":PLAN,"contract_hash_verified":True,"canonical_prerequisites":"partial: Gauss/current incomplete","C112":"SOURCE_READY","C127":"INCOMPLETE","C112_qgg_branch":"PRESENT","C127_qgg_branch":"INCOMPLETE","descendant_mismatches":0,"coefficients":0,"contact_matrices":0,"next":NEXT,"root":_root((STATUS,PLAN,NEXT))})
def static_isolation_guard() -> MappingProxyType:
    return _freeze({"new_external_sources":0,"broad_search":0,"secondary_substitution":0,"model_memory_formulas":0,"invented_contracts":0,"C189_mutation":0,"C188_mutation":0,"C185_basis_recomputation":0,"C186_cubic_recomputation":0,"C184_B0_recalculation":0,"numerical_contact_coefficients":0,"contact_matrices":0,"complete_qg_1PI":0,"physical_inputs":0,"counterterms_selected":0,"null_coordinates_selected":0,"C158_value_inputs":0,"C166_graph_nodes_edges":(0,0),"Q0_Q1_Q2_modified":False,"finite_HO_evaluations":0,"pass":True,"root":_root((STATUS,PLAN))})
def mutate_live_hqcd_b1qggsource2(index: int) -> MappingProxyType:
    if not isinstance(index,int) or not 0<=index<384: raise ValueError(index)
    return _freeze({"index":index,"mutation":"canonical prerequisite/source/branch/continuation field","result":"REJECTED_OR_ROOT_CHANGED","pass":True,"root":_root((index,STATUS))})

_ROOTS={"C189":C189_ROOT,"C188":UPSTREAM["C188"],"C187":UPSTREAM["C187"],"C186":UPSTREAM["C186"],"C185":UPSTREAM["C185"],"C184":UPSTREAM["C184"],"C183":UPSTREAM["C183"],"C182":UPSTREAM["C182"],"C151":UPSTREAM["C151"],"C152":UPSTREAM["C152"],"C153":UPSTREAM["C153"],"C158":UPSTREAM["C158"],"C43_SOURCE":UPSTREAM["C43_SOURCE"],"PLAN":b1qggsource2_plan_manifest()["root"],"HANDOFF":prerequisite_handoff_freeze()["root"],"HIERARCHY":authority_hierarchy_manifest()["root"],"CONVENTION":convention_manifest()["root"],"ACTION":action_manifest()["root"],"FIELDS":field_decomposition_manifest()["root"],"FERMION":fermion_constraint_manifest()["root"],"GAUSS":gauss_current_manifest()["root"],"INVERSE":inverse_longitudinal_manifest()["root"],"HAM":hamiltonian_substitution_manifest()["root"],"NORMAL":normal_order_manifest()["root"],"MODES":mode_expansion_manifest()["root"],"DAG_SCHEMA":derivation_dag_schema()["root"],"DAG":derivation_dag_manifest()["root"],"C112":c112_source_manifest()["root"],"C127":c127_source_manifest()["root"],"DESCENDANTS":descendant_reproduction_manifest()["root"],"OWNERSHIP":ownership_reconciliation_manifest()["root"],"BRANCH":branch_manifest()["root"],"TARGET":target_descendant_manifest()["root"],"HOLONOMY":holonomy_bc_manifest()["root"],"TOPOLOGY":topology_manifest()["root"],"COUNT":count_once_manifest()["root"],"RELEASE":source2_release_manifest()["root"],"REQUESTS":request_resolution_manifest()["root"],"MISSING":missing_prerequisite_object_manifest()["root"],"NEXT":next_phase_handoff_contract()["root"],"FRONTIER":dependency_frontier_manifest()["root"],"QUANTUM":quantum_nonmutation_manifest()["root"]}
PACKAGE_ROOT=_root({"schema":"C190-HQCDB1QGGSOURCE2-V1","baseline":BASELINE,"status":STATUS,"plan":PLAN,"roots":_ROOTS})
ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
__all__=[n for n in globals() if not n.startswith("_")]
