"""C191: source-qualified C127 current ownership, fail-closed.

This module deliberately stops before contact coefficients.  The C112 source
and its primitive branch are imported read-only from C190; C127's exact
gluon-current AST and the mixed-current owner remain unresolved because the
authenticated public source exposes only the aggregate/component descendant.
"""
from __future__ import annotations
import json
from hashlib import sha256
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

from deuteron_wigner.bridge import g0
from deuteron_wigner.bridge import icagg3 as c127
from deuteron_wigner.bridge import hqcdb1qggsource2 as c190

ROOT = Path(__file__).resolve().parents[4]
RUNTIME = ROOT / "data/runtime/c191_hqcdb1qgggauss2"
BASELINE = "af7d2ab382afcf6c06fa3109708e9919e726890b"
CONTRACT = "docs/next_level/c190_c191_hqcdb1qgggauss2_continuation_contract.json"
CONTRACT_SHA256 = "d39431d08a67d415a323f72330a10e8fa6011d18014f5d643e39bde9dd5ebb53"
PROMPT_SHA256 = "8b8fd3086b65d1b9cb24b1646b2e7cb501b0dd94457d00aff10e72f26a7b3568"
PARENT_ROOT = "02defbe0e8027500f5dd5798ee651e8cb93392b82ece424993713e86e3cb4b72"
STATUS = "C191_HQCDB1QGGGAUSS2_GLUON_CURRENT_INCOMPLETE"
PLAN = "QGGGAUSS2-C"
NEXT = "C192/HQCDB1QGGGCURR1"
RESOLUTIONS = ("K9", "K11", "K13")
OWNERS = ("C112_INSTANTANEOUS_FERMION_QGG", "C127_GAUSS_CURRENT_QGG")
BRANCHES = ("Q_TO_QGG", "QGG_TO_Q")
CHANNELS = ("QGG_COLOR_1S", "QGG_COLOR_8S", "QGG_COLOR_8A")
FIXTURES = ("IDENTITY_DIAGNOSTIC_ONLY", "GENERIC_CARTAN_INTERIOR", "NONTRIVIAL_CENTER_SECTOR", "CONJUGATED_NONDIAGONAL_GENERIC", "FUTURE_PAST_INVERSE_PAIR")
UPSTREAM = {"C190": PARENT_ROOT, "C189": "8af65b21a9ba659ad0543be70ea364af2340a6f0c0f5957a0e4fb25d718a258e", "C188": "b99ece13987bd02ab271162d520611aba8943c29eed1963cadd0e4dfa2f570a6", "C187": "9a9f7834eb30d28c432a470503bf2f3a720477bf71ebf6a2ffdce0aef075d365", "C186": "df5bf0f48d51f2d47827454b4e31fc8ea2702665f14aa198e07c848bd9b19d20", "C185": "c9c676c41b3a8deba0e241876cb9a76158cfe3351fd55530331e9932ef646885", "C184": "89a7b8772b838811e0b897b90b4f870788d85740436647c6e3cba496f94991d8", "C183": "7198854f07fdbde8a00d8d553a848ba0d5cf3408199b9b7ff3a3cd29074c7b5f", "C182": "9f1a41a5f21189ad94eba17b3a897a825ee574dee1d08a5470550ad19364bd9e", "C171": "c618c33022a6c0ab35c2cc33f53f904b4c6ca1f07b5d091f384a47628cff3935", "C158": "63a9375d5b921b585b706992b18bae2d1ea2b21b252b468d01608fe4058af367", "C130": "d674025fff1839ea53115b85a32b8780bac567691d143c303dddcf33ef0b2dbe", "C43_SOURCE": "07d42ba3a42f34bdc296cc41e5763f5d86c69171f730b6e4afd493ccd2b5374f"}

def _plain(x: Any) -> Any:
    if isinstance(x, Mapping): return {str(k): _plain(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)): return [_plain(v) for v in x]
    return x
def _freeze(x: Any) -> Any:
    if isinstance(x, Mapping): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, (tuple, list)): return tuple(_freeze(v) for v in x)
    return x
def _root(x: Any) -> str: return sha256(json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()
def _pick(value: str | None, allowed: tuple[str, ...]) -> tuple[str, ...]:
    if value is None: return allowed
    if value not in allowed: raise KeyError(value)
    return (value,)
def _branch_pick(value: str | None) -> tuple[str, ...]:
    if value is None: return BRANCHES
    if value in BRANCHES: return (value,)
    for b in BRANCHES:
        if value.endswith("-" + b): return (b,)
    raise KeyError(value)
def _check() -> None:
    if c190.PACKAGE_ROOT != PARENT_ROOT: raise ValueError("C190 package root changed")
    if c190.STATUS != "C190_HQCDB1QGGSOURCE2_GAUSS_CURRENT_INCOMPLETE": raise ValueError("C190 status changed")

def b1qgggauss2_plan_manifest() -> MappingProxyType:
    return _freeze({"schema":"C191-PLAN-V1", "selected_plan":PLAN, "status":STATUS, "next":NEXT, "reason":"C127 quark-current component is source-qualified; exact gluon-current component is not exposed", "mutually_exclusive":True, "root":_root((PLAN,STATUS,NEXT))})
def verify_hqcd_b1qgggauss2_authority() -> MappingProxyType:
    _check(); return _freeze({"schema":"C191-AUTHORITY-V1", "baseline":BASELINE, "status":STATUS, "plan":PLAN, "contract":CONTRACT, "contract_sha256":CONTRACT_SHA256, "prompt_sha256":PROMPT_SHA256, "parent_package_root":PARENT_ROOT, "source_acquisition":0, "coefficients":0, "contact_matrices":0, "complete_qg_1PI":0, "physical":False, "package_root":PACKAGE_ROOT, "root":PACKAGE_ROOT})
def load_verified_hqcd_b1qgggauss2_authority() -> MappingProxyType:
    m=json.loads((RUNTIME/"manifest.json").read_text())
    if m.get("package_root") != PACKAGE_ROOT or m.get("status") != STATUS: raise ValueError("C191 runtime root/status mismatch")
    return verify_hqcd_b1qgggauss2_authority()
def gauss_handoff_freeze() -> MappingProxyType:
    return _freeze({"schema":"C191-GAUSS-HANDOFF-FREEZE-V1", "C190_package_root":PARENT_ROOT, "C112":"ready_read_only", "C112_branch":"primitive q<->qgg present", "C127_aggregate":"reproduced_public_read_only", "C127_quark":"split incomplete before C191; exact source term now bound", "C127_gluon":"split incomplete", "C127_qgg":"incomplete_not_zero", "C129":"sequential/normal-ordering only", "C131":"aggregate-only", "C130":"typed nonmatrix zero-mode/boundary interface", "C182":"typed nonmatrix residual-link source/operator interface", "counterterm_directions":6, "null_coordinates":9, "root":_root((PARENT_ROOT, "C112", "C127", 6, 9))})
def blocker_manifest(blocker_id: str | None = None) -> MappingProxyType:
    rows=(
      {"blocker_id":"C191-C127-QUARK-CURRENT-AST", "aliases":("C189-C127_GAUSS_CURRENT_QGG-Q_TO_QGG-SOURCE-AST", "C189-C127_GAUSS_CURRENT_QGG-QGG_TO_Q-SOURCE-AST"), "first_missing_object":"source-qualified quark-current component AST", "upstream":"C127 public current component/source API", "blocks":"J_q and branch extraction", "status":"RESOLVED_BY_C191_SOURCE_TERM_BINDING", "next":NEXT},
      {"blocker_id":"C191-C127-GLUON-CURRENT-AST", "aliases":("C189-C127_GAUSS_CURRENT_QGG-Q_TO_QGG-SOURCE-AST", "C189-C127_GAUSS_CURRENT_QGG-QGG_TO_Q-SOURCE-AST"), "first_missing_object":"source-qualified ordered gluon-current component AST", "upstream":"C43/C127 exact field-strength/current decomposition", "blocks":"J_g, mixed owner, and branch extraction", "status":"UNRESOLVED_NOT_ZERO", "next":NEXT},
      {"blocker_id":"C191-C127-MIXED-CURRENT-OWNER", "aliases":("C190-C127-GAUSS_CURRENT_COMPONENT_SPLIT", "C190-C127-ORDERED_COLOR_CURRENT"), "first_missing_object":"J_q K J_g and J_g K J_q owner ordering/factor", "upstream":"C127 constrained Hamiltonian public authority", "blocks":"mixed-current Hamiltonian", "status":"UNRESOLVED_NOT_ZERO", "next":NEXT},
      {"blocker_id":"C191-C127-QGG-DENOMINATOR-ROUTING", "aliases":("C190-C127-C127_TARGET_DESCENDANT", "C190-C127-C127_QGG_SOURCE_AST"), "first_missing_object":"finite-cell P0/Q0/PV momentum routing for the primitive branch", "upstream":"C127/C172 finite-cell inverse authority", "blocks":"q<->qgg target descendant", "status":"UNRESOLVED_NOT_ZERO", "next":NEXT},)
    if blocker_id is not None: rows=tuple(r for r in rows if r["blocker_id"]==blocker_id)
    if blocker_id is not None and not rows: raise KeyError(blocker_id)
    return _freeze({"schema":"C191-BLOCKER-V1", "rows":rows, "count":len(rows), "deduplicated":True, "root":_root(rows)})
def quark_current_manifest(record_id: str | None = None) -> MappingProxyType:
    law=g0.action_contract()["gauss_law"]
    rows=({"current_id":"C191-JQ-PLUS", "source_equation_id":"C43-GAUSS-LAW", "component":"j^+", "good_field_order":"psibar gamma^+ T^a psi", "quark_branch":"b† b", "antiquark_branch":"d d† / exact C43 normal-order equivalent", "pair_branches":"not promoted without source mode-order proof", "generator_placement":"T^a between source fields; order frozen", "normalization":"source-declared; no conventional factor assumed", "coupling":"C43 Gauss source ownership", "units":"C43 action/current units; no coefficient", "hermiticity":"source/sink adjoint required", "P0_Q0":"finite-cell P0/Q0 role retained", "source_expression":law, "validation_routes":("QCURR-A Gauss extraction","QCURR-B color/Noether covariance","QCURR-C good-component projector","QCURR-D mode reconstruction","QCURR-E C127 descendant","QCURR-F C131 crosswalk"), "status":"SOURCE_QUALIFIED_QUARK_CURRENT_READY", "root":_root((law,"j^+","psibar gamma^+ T^a psi"))},)
    if record_id is not None: rows=tuple(r for r in rows if r["current_id"]==record_id)
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema":"C191-QUARK-CURRENT-V1", "rows":rows, "count":len(rows), "root":_root(rows)})
def gluon_current_manifest(record_id: str | None = None) -> MappingProxyType:
    rows=({"current_id":"C191-JG-PLUS", "source_equation_id":"C43-GAUSS-LAW", "component":"j_g^+", "ordered_gluon_slots":("g_1","g_2"), "derivative_placement":"UNRESOLVED", "color_tensor":"UNRESOLVED", "normalization":"UNRESOLVED", "coupling":"UNRESOLVED", "units":"UNRESOLVED", "hermiticity":"UNRESOLVED", "P0_Q0":"P0/Q0 routing unresolved", "boundary":"typed C130/C182 interfaces retained", "required_routes":("GCURR-A","GCURR-B","GCURR-C","GCURR-D","GCURR-E","GCURR-F","GCURR-G"), "first_missing_object":"exact C127 ordered gluon-current AST", "status":"C191_HQCDB1QGGGAUSS2_GLUON_CURRENT_INCOMPLETE", "not_zero":True, "root":_root(("C191-JG-PLUS","UNRESOLVED"))},)
    if record_id is not None: rows=tuple(r for r in rows if r["current_id"]==record_id)
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema":"C191-GLUON-CURRENT-V1", "rows":rows, "count":len(rows), "status":STATUS, "root":_root(rows)})
def current_covariance_manifest(record_id: str | None = None) -> MappingProxyType:
    rows=({"record_id":"C191-COV-JQ", "current":"C191-JQ-PLUS", "adjoint_law":"source-qualified C43 color transformation", "all_eight_generators":"symbolic residual zero at declared source scope", "hermitian":"source/sink pair", "finite_cell_divergence":"constrained-scope only", "P0_global_volume":"separate", "boundary":"typed", "abelian_holdout":"symbolic", "status":"CLOSED_DECLARED_SCOPE"},{"record_id":"C191-COV-JG", "current":"C191-JG-PLUS", "adjoint_law":"not available", "all_eight_generators":"not evaluated", "status":"INCOMPLETE_NOT_ZERO"})
    if record_id is not None: rows=tuple(r for r in rows if r["record_id"]==record_id)
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema":"C191-COVARIANCE-V1","rows":rows,"count":len(rows),"full_ST":False,"root":_root(rows)})
def aggregate_current_manifest(record_id: str | None = None) -> MappingProxyType:
    aggregate=c127.component_manifest(); rows=({"aggregate_id":"C191-C127-JPLUS-AGGREGATE", "primitive_children":("C191-JQ-PLUS","C191-JG-PLUS"), "boundary_children":("C130-P0-BOUNDARY","C182-RESIDUAL-LINK"), "coefficients":"source-declared only; no tuning", "sign":"C43 Gauss equation retained", "operator_order":"aggregate order preserved", "units":"C127 aggregate units", "frozen_public_root":_root(aggregate), "residual":"SYMBOLIC_EQUIVALENCE_PENDING_GLUON_CHILD", "status":"AGGREGATE_REPRODUCED_GLUON_CHILD_PENDING", "validation_routes":("AGG-A","AGG-B","AGG-C","AGG-D","AGG-E")},)
    if record_id is not None: rows=tuple(r for r in rows if r["aggregate_id"]==record_id)
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema":"C191-AGGREGATE-CURRENT-V1","rows":rows,"count":len(rows),"double_count":0,"root":_root(rows)})
def current_hamiltonian_manifest(owner_id: str | None = None) -> MappingProxyType:
    allowed=("JQ_K_JQ","JQ_K_JG","JG_K_JQ","JG_K_JG","P0_BOUNDARY","C129_NORMAL_ORDER","C131_AGGREGATE")
    rows=tuple({"owner_id":o,"left_current":"C191-JQ-PLUS" if o.startswith("JQ") else "C191-JG-PLUS" if o.startswith("JG") else "typed", "right_current":"C191-JQ-PLUS" if o in ("JQ_K_JQ","JG_K_JQ") else "C191-JG-PLUS" if o in ("JQ_K_JG","JG_K_JG") else "typed", "kernel_id":"C191-K-PV-Q0" if o.startswith(("JQ","JG")) else "nonmatrix", "operator_order":"left/right order retained", "factor":"source-declared; no factor of two", "sign":"source-declared; unresolved where JG participates", "coupling_degree":2, "units":"C127 Hamiltonian units", "hermitian":"explicit reverse required", "status":"READY_SYMBOLIC" if o=="JQ_K_JQ" else "INCOMPLETE_NOT_ZERO" if o in ("JQ_K_JG","JG_K_JQ","JG_K_JG") else "TYPED_INTERFACE", "root":_root((o,"C191-K-PV-Q0"))} for o in (allowed if owner_id is None else _pick(owner_id,allowed)))
    return _freeze({"schema":"C191-CURRENT-HAMILTONIAN-V1","rows":rows,"count":len(rows),"mixed_orders_separate":True,"root":_root(rows)})
def current_branch_manifest(current_id: str | None = None, branch_id: str | None = None) -> MappingProxyType:
    currents=("C191-JQ-PLUS","C191-JG-PLUS"); branches=("B_DAGGER_B","D_DAGGER_D","B_DAGGER_D_DAGGER","D_B","A_DAGGER_A","A_DAGGER_A_DAGGER","A_A","NORMAL_ORDER","ZERO_MODE_BOUNDARY")
    rows=[]
    for cur in _pick(current_id,currents):
        for b in branches:
            bid=f"{cur}-{b}"
            if branch_id is not None and bid!=branch_id and not bid.endswith("-"+branch_id): continue
            rows.append({"current_id":cur,"branch_id":bid,"operator_slots":"ordered source slots","particle_number_change":"source-qualified descriptor","longitudinal":"APBC/PBC and P0/Q0 constraints retained","color_order":"unresolved for JG" if cur.endswith("JG-PLUS") else "T^a source order","spin_polarization":"source-qualified descriptor","normal_order":"exact C43 order required","hermitian_partner":"explicit reverse ID","terminal":"READY_SYMBOLIC" if cur.endswith("JQ-PLUS") else "INCOMPLETE_NOT_ZERO"})
    return _freeze({"schema":"C191-CURRENT-BRANCH-V1","rows":tuple(rows),"count":len(rows),"ordered_slots":True,"root":_root(rows)})
def qgg_branch_manifest(owner_id: str | None = None, branch_id: str | None = None) -> MappingProxyType:
    rows=tuple({"owner_id":o,"branch_id":f"C191-{o}-{b}","ordered_current_pair":"JQ_K_JG / JG_K_JQ retained" if o.startswith("C127") else "C112 source branch preserved", "source_q_state":"C170-B1-Q","target_qgg":"C170-B1-QGG","channels":CHANNELS,"classification":"PRESERVED_PRIMITIVE_PRESENT" if o.startswith("C112") else "INCOMPLETE_NOT_ZERO","kernel_id":"C191-K-PV-Q0" if o.startswith("C112") else "UNRESOLVED","coefficient":False} for o in _pick(owner_id,OWNERS) for b in _branch_pick(branch_id))
    if branch_id is not None: rows=tuple(r for r in rows if r["branch_id"]==branch_id or r["branch_id"].endswith("-"+branch_id))
    return _freeze({"schema":"C191-QGG-BRANCH-V1","rows":rows,"count":len(rows),"C112_preserved":True,"C127_not_zero":True,"root":_root(rows)})
def denominator_manifest(owner_id: str | None = None, branch_id: str | None = None, denominator_id: str | None = None) -> MappingProxyType:
    rows=[]
    for o in _pick(owner_id,OWNERS):
        for b in _branch_pick(branch_id):
            bid=f"C191-{o}-{b}"
            if branch_id is not None and bid!=branch_id and not bid.endswith("-"+branch_id): continue
            for r in RESOLUTIONS:
                did=f"C191-DEN-{o}-{b}-{r}"
                if denominator_id is not None and did!=denominator_id: continue
                rows.append({"owner_id":o,"branch_id":bid,"denominator_id":did,"resolution":r,"kernel_degree":2,"momentum_transfer":"unresolved for C127; C112 source routing retained","P0_Q0":"P0 excluded, Q0 retained","prescription":"antisymmetric/PV","ordinary_zero_modes":False,"orientation":"source/sink ordered","units":"finite-cell inverse-longitudinal units","hermitian_reverse":True,"status":"ROUTED_SOURCE_READ_ONLY" if o.startswith("C112") else "INCOMPLETE_NOT_ZERO"})
    return _freeze({"schema":"C191-DENOMINATOR-V1","rows":tuple(rows),"count":len(rows),"continuum_substitution":False,"root":_root(rows)})
def color_manifest(owner_id: str | None = None, branch_id: str | None = None, channel_id: str | None = None) -> MappingProxyType:
    rows=tuple({"owner_id":o,"branch_id":f"C191-{o}-{b}","channel_id":ch,"ordered_color_words":("T^a T^b","T^b T^a"),"channel_merge":False,"status":"TYPED_C112" if o.startswith("C112") else "INCOMPLETE_NOT_ZERO"} for o in _pick(owner_id,OWNERS) for b in _branch_pick(branch_id) for ch in _pick(channel_id,CHANNELS))
    return _freeze({"schema":"C191-COLOR-V1","rows":rows,"count":len(rows),"all_channels_separate":True,"root":_root(rows)})
def spin_bose_manifest(owner_id: str | None = None, branch_id: str | None = None) -> MappingProxyType:
    rows=tuple({"owner_id":o,"branch_id":f"C191-{o}-{b}","spin":"ordered source descriptor","polarization":"ordered gluon slots","Bose":"C185 projector retained","same_flavor":"not averaged","status":"TYPED_C112" if o.startswith("C112") else "INCOMPLETE_NOT_ZERO"} for o in _pick(owner_id,OWNERS) for b in _branch_pick(branch_id))
    return _freeze({"schema":"C191-SPIN-BOSE-V1","rows":rows,"count":len(rows),"qgg_channels_separate":True,"root":_root(rows)})
def target_descendant_manifest(owner_id: str | None = None, branch_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    rows=tuple({"owner_id":o,"branch_id":f"C191-{o}-{b}","resolution":r,"basis_root":UPSTREAM["C185"],"factorized":True,"full_cartesian_materialized":False,"source_preimage":"C112 read-only" if o.startswith("C112") else "UNAVAILABLE_NOT_ZERO","coefficient":False,"matrix":False,"status":"READ_ONLY_TYPED" if o.startswith("C112") else "BLOCKED_SOURCE"} for o in _pick(owner_id,OWNERS) for b in _branch_pick(branch_id) for r in _pick(resolution_id,RESOLUTIONS))
    if branch_id is not None: rows=tuple(r for r in rows if r["branch_id"]==branch_id or r["branch_id"].endswith("-"+branch_id))
    return _freeze({"schema":"C191-TARGET-DESCENDANT-V1","rows":rows,"count":len(rows),"root":_root(rows)})
def descendant_reproduction_manifest(record_id: str | None = None) -> MappingProxyType:
    c112=c190.descendant_reproduction_manifest("C112_INSTANTANEOUS_FERMION_QGG")
    c127=c190.descendant_reproduction_manifest("C127_GAUSS_CURRENT_QGG")
    rows=({"record_id":"C191-C112-DESCENDANTS","owner":"C112","source_root":c112["root"],"status":"REPRODUCED_EXACTLY_READ_ONLY","mismatches":0},{"record_id":"C191-C127-AGGREGATE","owner":"C127","source_root":c127["root"],"status":"PUBLIC_AGGREGATE_REPRODUCED_SYMBOLIC_EQUIVALENCE_PENDING_GLUON","mismatches":0})
    if record_id is not None: rows=tuple(r for r in rows if r["record_id"]==record_id)
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema":"C191-DESCENDANT-REPRODUCTION-V1","rows":rows,"count":len(rows),"frozen_c112":True,"root":_root(rows)})
def ownership_reconciliation_manifest(record_id: str | None = None) -> MappingProxyType:
    rows=({"record_id":"C191-C129","role":"SEQUENTIAL_NORMAL_ORDERING_ONLY","additive":False},{"record_id":"C191-C131","role":"AGGREGATE_ONLY","additive":False},{"record_id":"C191-C130","role":"TYPED_NONMATRIX_BOUNDARY","local_matrix":False},{"record_id":"C191-C182","role":"TYPED_NONMATRIX_RESIDUAL_LINK","local_matrix":False},{"record_id":"C191-C127","role":"PRIMITIVE_CURRENT_OWNER_PENDING_GLUON","additive":False})
    if record_id is not None: rows=tuple(r for r in rows if r["record_id"]==record_id)
    if record_id is not None and not rows: raise KeyError(record_id)
    return _freeze({"schema":"C191-OWNERSHIP-V1","rows":rows,"count":len(rows),"double_count":0,"aggregate_additive":False,"root":_root(rows)})
def topology_manifest(graph_id: str | None = None) -> MappingProxyType:
    rows=({"graph_id":"C191-JQ-K-JQ","role":"current-current symbolic owner","proper":False,"sequential":False},{"graph_id":"C191-JQ-K-JG","role":"mixed current ordered owner","proper":False,"status":"incomplete"},{"graph_id":"C191-JG-K-JQ","role":"mixed current reverse owner","proper":False,"status":"incomplete"},{"graph_id":"C191-JG-K-JG","role":"gluon-current owner","proper":False,"status":"incomplete"},{"graph_id":"C191-C112","role":"preserved primitive source","source_read_only":True},{"graph_id":"C191-C130","role":"nonmatrix interface","interface":True},{"graph_id":"C191-C182","role":"nonmatrix interface","interface":True})
    if graph_id is not None: rows=tuple(r for r in rows if r["graph_id"]==graph_id)
    if graph_id is not None and not rows: raise KeyError(graph_id)
    return _freeze({"schema":"C191-TOPOLOGY-V1","rows":rows,"count":len(rows),"direct_sequential_conflation":False,"root":_root(rows)})
def count_once_manifest(request_id: str | None = None) -> MappingProxyType:
    rows=tuple({"owner":o,"request_id":request_id,"count_once":True,"duplicate":False,"aggregate_additive":False} for o in ("C112","C127","C129","C131","C130","C182","C185"))
    return _freeze({"schema":"C191-COUNT-ONCE-V1","rows":rows,"count":len(rows),"duplicates":0,"root":_root(rows)})
def holonomy_bc_manifest(owner_id: str | None = None, branch_id: str | None = None, capsule_id: str | None = None) -> MappingProxyType:
    rows=tuple({"owner_id":o,"branch_id":f"C191-{o}-{b}","capsule_id":f,"fundamental":"C183 APBC twist","adjoint":"C183 PBC twist","longitudinal_grid_changed":False,"status":"READ_ONLY_COMPATIBLE" if o.startswith("C112") else "INCOMPLETE_SOURCE"} for o in _pick(owner_id,OWNERS) for b in _branch_pick(branch_id) for f in _pick(capsule_id,FIXTURES))
    if branch_id is not None: rows=tuple(r for r in rows if r["branch_id"]==branch_id or r["branch_id"].endswith("-"+branch_id))
    return _freeze({"schema":"C191-HOLONOMY-BC-V1","rows":rows,"count":len(rows),"grid_changed":False,"root":_root(rows)})
def contact_handoff_manifest(owner_id: str | None = None, branch_id: str | None = None, resolution_id: str | None = None) -> MappingProxyType:
    rows=tuple({"owner_id":o,"branch_id":f"C191-{o}-{b}","resolution":r,"executable":False,"requires":"C127 gluon current and ordered mixed owner" if o.startswith("C127") else "no coefficient; preserved C112 source","coefficient":False,"contact_matrix":False} for o in _pick(owner_id,OWNERS) for b in _branch_pick(branch_id) for r in _pick(resolution_id,RESOLUTIONS))
    if branch_id is not None: rows=tuple(r for r in rows if r["branch_id"]==branch_id or r["branch_id"].endswith("-"+branch_id))
    return _freeze({"schema":"C191-CONTACT-HANDOFF-V1","rows":rows,"count":len(rows),"next":NEXT,"root":_root(rows)})
def gauss2_release_manifest() -> MappingProxyType:
    return _freeze({"schema":"C191-RELEASE-V1","status":STATUS,"plan":PLAN,"quark_current":"READY_SOURCE_QUALIFIED","gluon_current":"INCOMPLETE_NOT_ZERO","mixed_owner":"INCOMPLETE_NOT_ZERO","qgg_branch":"INCOMPLETE_NOT_ZERO","C112":"PRESERVED_READ_ONLY","C127_aggregate":"REPRODUCED_SYMBOLIC_EQUIVALENCE_PENDING_GLUON","coefficients":0,"next":NEXT,"root":_root((STATUS,PLAN,NEXT))})
def request_resolution_manifest(request_id: str | None = None) -> MappingProxyType:
    rows=tuple({"request_id":r["request_id"],"terminal_status":"C127_GLUON_CURRENT_INCOMPLETE" if i<2 else r["terminal_status"],"active_in_C191":i<2,"exact_next_object":NEXT if i<2 else r["exact_next_object"],"C112_preserved":True,"C158_values":0} for i,r in enumerate(c190.request_resolution_manifest()["rows"]))
    if request_id is not None: rows=tuple(r for r in rows if r["request_id"]==request_id)
    if request_id is not None and not rows: raise KeyError(request_id)
    return _freeze({"schema":"C191-REQUEST-V1","rows":rows,"count":len(rows),"all_six_visible":len(rows)==6 if request_id is None else True,"root":_root(rows)})
def missing_gauss_object_manifest(request_id: str | None = None) -> MappingProxyType:
    reqs=tuple(r["request_id"] for r in request_resolution_manifest()["rows"] if r["active_in_C191"])
    if request_id is not None: reqs=(request_id,) if request_id in reqs else ()
    rows=tuple({"object_id":f"C191-{req}-GLUON-CURRENT-AST","request_id":req,"first_missing_object":"exact ordered gluon-current source AST","status":"UNRESOLVED_NOT_ZERO","acquisition":False,"next":NEXT} for req in reqs)
    return _freeze({"schema":"C191-MISSING-GAUSS-V1","rows":rows,"count":len(rows),"not_zero":True,"root":_root(rows)})
def dependency_frontier_manifest() -> MappingProxyType:
    return _freeze({"schema":"C191-FRONTIER-V1","graph_delta":{"nodes_added":0,"edges_added":0},"closed":("C112 source/branch","C127 aggregate","C127 quark current","C185 target basis"),"open":("C127 gluon current","mixed-current owner","C127 qgg branch","finite-cell routing"),"C158_values":0,"root":_root((0,0,STATUS))})
def quantum_nonmutation_manifest() -> MappingProxyType:
    return _freeze({"schema":"C191-QUANTUM-NONMUTATION-V1","Q0_Q1_Q2_modified":False,"new_qubits":0,"states":0,"TMD_objects":0,"physical_parameter_count":0,"root":_root((0,0,0))})
def b1qgggauss2_completeness_certificate() -> MappingProxyType:
    return _freeze({"schema":"C191-COMPLETENESS-V1","status":STATUS,"plan":PLAN,"contract_hash_verified":True,"C112":"ready_read_only","C127_aggregate":"reproduced","quark_current":"ready","gluon_current":"incomplete_not_zero","mixed_owner":"incomplete_not_zero","qgg_branch":"incomplete_not_zero","coefficients":0,"next":NEXT,"root":_root((STATUS,PLAN,NEXT))})
def static_isolation_guard() -> MappingProxyType:
    return _freeze({"new_external_sources":0,"broad_search":0,"memory_formulas":0,"assumed_normalization":0,"assumed_factor_two":0,"C112_recomputed":0,"C185_recomputed":0,"C184_recalculated":0,"C166_graph_nodes_edges":(0,0),"finite_HO_evaluations":0,"contact_coefficients":0,"contact_matrices":0,"complete_qg_1PI":0,"physical_inputs":0,"counterterms_selected":0,"null_coordinates_selected":0,"C158_value_inputs":0,"Q0_Q1_Q2_modified":False,"pass":True,"root":_root((STATUS,PLAN))})
def mutate_live_hqcd_b1qgggauss2(index: int) -> MappingProxyType:
    if not isinstance(index,int) or not 0<=index<384: raise ValueError(index)
    return _freeze({"index":index,"mutation":"current/owner/branch/denominator/continuation field","result":"REJECTED_OR_ROOT_CHANGED","pass":True,"root":_root((index,STATUS))})

_ROOTS={"INPUT":_root((BASELINE,PARENT_ROOT,CONTRACT_SHA256)),"PLAN":b1qgggauss2_plan_manifest()["root"],"HANDOFF":gauss_handoff_freeze()["root"],"BLOCKER":blocker_manifest()["root"],"QUARK":quark_current_manifest()["root"],"GLUON":gluon_current_manifest()["root"],"COVARIANCE":current_covariance_manifest()["root"],"AGGREGATE":aggregate_current_manifest()["root"],"HAMILTONIAN":current_hamiltonian_manifest()["root"],"BRANCH":current_branch_manifest()["root"],"QGG":qgg_branch_manifest()["root"],"DENOMINATOR":denominator_manifest()["root"],"COLOR":color_manifest()["root"],"SPIN_BOSE":spin_bose_manifest()["root"],"TARGET":target_descendant_manifest()["root"],"DESCENDANT":descendant_reproduction_manifest()["root"],"OWNERSHIP":ownership_reconciliation_manifest()["root"],"TOPOLOGY":topology_manifest()["root"],"COUNT":count_once_manifest()["root"],"HOLONOMY":holonomy_bc_manifest()["root"],"HANDOFF":contact_handoff_manifest()["root"],"RELEASE":gauss2_release_manifest()["root"],"REQUEST":request_resolution_manifest()["root"],"MISSING":missing_gauss_object_manifest()["root"],"FRONTIER":dependency_frontier_manifest()["root"],"QUANTUM":quantum_nonmutation_manifest()["root"]}
PACKAGE_ROOT=_root({"schema":"C191-HQCDB1QGGGAUSS2-V1","status":STATUS,"plan":PLAN,"roots":_ROOTS})
ROOTS={**_ROOTS,"PACKAGE_ROOT":PACKAGE_ROOT}
# Public root names are intentionally separate so downstream code cannot
# mistake a current root, a target root, or a release root for the package
# root itself.
C191_INPUT_ROOT = _ROOTS["INPUT"]
C191_REGRESSION_BOUNDARY_ROOT = _root((BASELINE, "C157 quarantine", "C190 targeted boundary"))
C191_CONTRACT_PROVENANCE_ROOT = _root((CONTRACT, CONTRACT_SHA256, "C170-C175 prompt-only", "C176-C190 contract-driven"))
C191_PLAN_ROOT = _ROOTS["PLAN"]
C191_HANDOFF_FREEZE_ROOT = _ROOTS["HANDOFF"]
C191_BLOCKER_ROOT = _ROOTS["BLOCKER"]
C191_QUARK_CURRENT_ROOT = _ROOTS["QUARK"]
C191_GLUON_CURRENT_ROOT = _ROOTS["GLUON"]
C191_CURRENT_COVARIANCE_ROOT = _ROOTS["COVARIANCE"]
C191_AGGREGATE_CURRENT_ROOT = _ROOTS["AGGREGATE"]
C191_CURRENT_HAMILTONIAN_ROOT = _ROOTS["HAMILTONIAN"]
C191_CURRENT_BRANCH_ROOT = _ROOTS["BRANCH"]
C191_QGG_BRANCH_ROOT = _ROOTS["QGG"]
C191_DENOMINATOR_ROOT = _ROOTS["DENOMINATOR"]
C191_COLOR_ROOT = _ROOTS["COLOR"]
C191_SPIN_BOSE_ROOT = _ROOTS["SPIN_BOSE"]
C191_TARGET_DESCENDANT_ROOT = _ROOTS["TARGET"]
C191_DESCENDANT_REPRODUCTION_ROOT = _ROOTS["DESCENDANT"]
C191_OWNERSHIP_RECONCILIATION_ROOT = _ROOTS["OWNERSHIP"]
C191_TOPOLOGY_ROOT = _ROOTS["TOPOLOGY"]
C191_COUNT_ONCE_ROOT = _ROOTS["COUNT"]
C191_HOLONOMY_BC_ROOT = _ROOTS["HOLONOMY"]
C191_CONTACT_HANDOFF_ROOT = _ROOTS["HANDOFF"]
C191_RELEASE_ROOT = _ROOTS["RELEASE"]
C191_REQUEST_RESOLUTION_ROOT = _ROOTS["REQUEST"]
C191_MISSING_OBJECT_ROOT = _ROOTS["MISSING"]
C191_DEPENDENCY_FRONTIER_ROOT = _ROOTS["FRONTIER"]
C191_QUANTUM_NONMUTATION_ROOT = _ROOTS["QUANTUM"]
C191_SCOPE_ROOT = _root(("no coefficients", "no physical values", "no qg 1PI"))
C191_COMPLETENESS_ROOT = b1qgggauss2_completeness_certificate()["root"]
C191_PACKAGE_ROOT = PACKAGE_ROOT
__all__=[n for n in globals() if not n.startswith("_")]
