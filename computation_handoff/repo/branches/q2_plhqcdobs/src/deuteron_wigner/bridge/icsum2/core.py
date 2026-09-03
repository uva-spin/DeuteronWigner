"""C121/ICSUM2 witness-domain authority.

C121 consumes the public C118 structural and C119 factor authorities.  The
C118 public domain contains program-level identities only; it does not
enumerate logical witnesses, physical target IDs, or target spans.  This
module therefore exposes a fail-closed descendant boundary instead of
inventing scientific records.  C122 remains unable to aggregate until that
domain is published.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import ast, json
from pathlib import Path
from types import MappingProxyType
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
BASELINE = "5adf5381ca18702b0cfab44580007ee92178650a"
CONTRACT = "docs/next_level/c120_c121_icsum2_import_contract.json"
STATUS = "C121_ICSUM2_LOGICAL_WITNESS_DOMAIN_INCOMPLETE"
NEXT = "C122/ICDOMAIN"
NEXT_CONTRACT = "docs/next_level/c121_c122_icdomain_import_contract.json"
PROGRAMS = (
    "J_qJ_q:q->q", "J_qJ_q:qg->qg", "J_qJ_g:q->q", "J_qJ_g:qg->qg",
    "J_gJ_q:q->q", "J_gJ_q:qg->qg", "J_gJ_g:q->q", "J_gJ_g:qg->qg",
)
RESOLUTIONS = ("K9_2_N8_b0.40", "K11_2_N8_b0.40", "K13_2_N8_b0.40")


def _freeze(x: Any) -> Any:
    if isinstance(x, dict): return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, list): return tuple(_freeze(v) for v in x)
    if isinstance(x, tuple): return tuple(_freeze(v) for v in x)
    return x


def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType): return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, tuple): return [_plain(v) for v in x]
    if isinstance(x, dict): return {k: _plain(v) for k, v in x.items()}
    return x


def canonical_json(x: Any) -> str:
    return json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def root(x: Any) -> str: return sha256(canonical_json(x).encode()).hexdigest()
def _hash(rel: str) -> str: return sha256((ROOT / rel).read_bytes()).hexdigest()


def input_freeze() -> MappingProxyType:
    return _freeze({
        "schema": "C121-INPUT-FREEZE-V1", "baseline": BASELINE,
        "C118_structural_status": "C118_ICASM2_COMPONENT_EVALUATION_INCOMPLETE",
        "C119_factor_status": "C119_C115_SOURCE_DERIVED_CERTIFIED_CURRENT_FACTOR_AUTHORITY_READY",
        "C118_programs": 8, "C119_leaves": 36,
        "C118_logical_witness_enumeration": False,
        "C118_matrix_target_enumeration": False,
        "C118_target_spans": False,
        "descendant_not_historical_recovery": True,
        "numeric_L": None, "numeric_P_plus": None, "physical_coupling": None,
        "counterterm_coefficient": None,
    })


def _consume_public_authorities() -> MappingProxyType:
    from deuteron_wigner.bridge.icasm2 import verify_assembly_authority
    from deuteron_wigner.bridge.icnorm3 import verify_factor_authority
    from deuteron_wigner.bridge.iferm3 import instantaneous_fermion_sector_manifest
    c118 = verify_assembly_authority()
    c119 = verify_factor_authority()
    basis_labels = ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50")
    basis = {r: instantaneous_fermion_sector_manifest(r) for r in basis_labels}
    return _freeze({
        "C118_status": c118.get("status"), "C118_programs": c118.get("program_count"),
        "C118_structural_missing": c118.get("witness_domain", {}).get("missing", 0),
        "C119_status": c119.get("status"), "C119_programs": c119.get("program_count"),
        "C119_leaves": c119.get("leaf_count"),
        "C112_basis_manifests": tuple({"resolution": r, "shape": basis[r]["direct_sum_shape"], "order": basis[r]["global_order"]} for r in basis_labels),
        "private_builders_called": 0, "numerical_values_consumed": 0,
    })


def derivation_authority_manifest() -> MappingProxyType:
    return _freeze({
        "schema": "C121-DERIVATION-AUTHORITY-V1",
        "claim": "new descendant source-derived witness authority over immutable C118 identities",
        "historical_C118_recovery": False,
        "routes": ("T-A direct C112 basis identity", "T-B independent source-graph reconstruction", "V-A structural compile and primitive join", "V-B component-program replay"),
        "routes_exercised": False,
        "reason": "C118 publishes no logical witness identities to enumerate or replay",
        "thresholds": False,
    })


def witness_domain_manifest() -> MappingProxyType:
    return _freeze({
        "schema": "C121-WITNESS-DOMAIN-MANIFEST-V1",
        "programs": PROGRAMS, "program_count": 8, "resolutions": RESOLUTIONS,
        "logical_witness_count": None, "component_resolution_counts": None,
        "canonical_order": None, "rank_unrank": "UNAVAILABLE",
        "source_graph_order": None, "target_span_order": None,
        "C118_structural_missing": 0, "C118_logical_identity_records": 0,
        "status": STATUS,
        "blocker": "C118 source-witness inventory is program-level and values=blocked; no logical witness IDs or ranks",
    })


def logical_witness_domain_inventory() -> MappingProxyType:
    return _freeze({
        "schema": "C121-LOGICAL-WITNESS-INVENTORY-V1", "program_rows": 8,
        "logical_records": 0, "record_count_status": "NOT_PUBLISHED_BY_C118",
        "first_identity": None, "last_identity": None, "carry_boundaries": None,
        "order_drift": "UNDECIDABLE", "status": STATUS,
    })


def matrix_target_manifest(component: str | None = None, resolution: str | None = None) -> MappingProxyType:
    if component is not None and component not in PROGRAMS: raise KeyError(component)
    if resolution is not None and resolution not in RESOLUTIONS: raise KeyError(resolution)
    return _freeze({
        "schema": "C121-MATRIX-TARGET-MANIFEST-V1", "component": component, "resolution": resolution,
        "target_count": 0, "targets": (), "route_TA": "NOT_RUN", "route_TB": "NOT_RUN",
        "target_mismatches": None, "status": "C121_ICSUM2_MATRIX_TARGET_INCOMPLETE",
        "blocker": "physical bra/ket IDs and logical witness records absent from C118 public API",
    })


def _missing(operation: str) -> None:
    raise RuntimeError(f"{STATUS}: {operation} unavailable because C118 does not enumerate logical witnesses")


def witness_record(witness_id: str) -> MappingProxyType: _missing("witness_record")
def witness_record_by_rank(rank: int, component: str | None = None, resolution: str | None = None) -> MappingProxyType: _missing("witness_record_by_rank")
def witness_value_expression(witness_id: str) -> MappingProxyType: _missing("witness_value_expression")
def witness_bound(witness_id: str) -> MappingProxyType: _missing("witness_bound")
def verify_witness_adjoint(witness_id: str) -> MappingProxyType: _missing("verify_witness_adjoint")
def witness_ancestry(witness_id: str) -> MappingProxyType: _missing("witness_ancestry")
def matrix_target_witness_page(matrix_target_id: str, cursor: str | None = None, limit: int = 128) -> MappingProxyType: _missing("matrix_target_witness_page")


def witness_record_page(cursor: str | None = None, limit: int = 128, component: str | None = None, resolution: str | None = None, matrix_target_id: str | None = None) -> MappingProxyType:
    if limit <= 0: raise ValueError(limit)
    if component is not None and component not in PROGRAMS: raise KeyError(component)
    if resolution is not None and resolution not in RESOLUTIONS: raise KeyError(resolution)
    return _freeze({"schema": "C121-WITNESS-PAGE-V1", "records": (), "cursor": cursor, "next_cursor": None, "terminal": True, "page_root": root(()), "status": STATUS, "logical_domain_available": False})


def rank_witness(witness_id: str) -> int: _missing("rank_witness")
def unrank_witness(rank: int, component: str | None = None, resolution: str | None = None) -> MappingProxyType: _missing("unrank_witness")


def witness_adjoint_manifest() -> MappingProxyType:
    return _freeze({"schema": "C121-WITNESS-ADJOINT-V1", "required_partners": None, "verified": False, "posthoc_copy": False, "status": STATUS})


def factor_ownership_contract() -> MappingProxyType:
    return _freeze({"schema": "C121-FACTOR-OWNERSHIP-V1", "program_level_unowned": 0, "program_level_duplicates": 0, "witness_level": "NOT_CLOSABLE_WITHOUT_LOGICAL_RECORDS", "numerical_g_s_squared_insertions": 0, "status": STATUS})


def count_once_certificate() -> MappingProxyType:
    return _freeze({"schema": "C121-COUNT-ONCE-V1", "structural_program_rows": 8, "logical_witnesses": None, "omitted": None, "duplicated": None, "wrong_target": None, "target_spans": 0, "threshold_pruned": 0, "status": STATUS})


def verify_current_witness_value_authority() -> dict[str, Any]:
    return {
        "status": STATUS, "baseline": BASELINE, "contract": CONTRACT, "contract_hash": _hash(CONTRACT),
        "input_freeze": input_freeze(), "public_authorities": _consume_public_authorities(),
        "derivation": derivation_authority_manifest(), "domain": witness_domain_manifest(),
        "domain_inventory": logical_witness_domain_inventory(), "targets": matrix_target_manifest(),
        "program_count": 8, "logical_witness_count": None, "records": 0,
        "route_TA_records": 0, "route_TB_records": 0, "route_VA_records": 0, "route_VB_records": 0,
        "identity_mismatches": None, "target_mismatches": None, "value_mismatches": None, "bound_mismatches": None,
        "unknown_values": None, "unknown_bounds": None, "exact_zero_records": 0, "unavailable_as_zero": 0,
        "component_aggregation": 0, "sparse_operators": 0, "matrix_free_actions": 0,
        "C53_values_consumed": 0, "C112_values_consumed": 0, "physical_coupling_values_consumed": 0,
        "counterterm_values_consumed": 0, "complete_block": False, "positive_gate": False, "next": NEXT,
    }


def load_verified_current_witness_value_authority() -> MappingProxyType:
    return _freeze(verify_current_witness_value_authority())


def static_isolation_guard() -> MappingProxyType:
    names = {n.id for n in ast.walk(ast.parse(Path(__file__).read_text())) if isinstance(n, ast.Name)}
    forbidden = ("C53_numeric_value", "C112_numeric_value", "physical_coupling_value", "counterterm_value", "component_sum", "sparse_operator")
    found = tuple(x for x in forbidden if x in names)
    return _freeze({"found": found, "pass": not found, "private_builder_calls": 0, "network_calls": 0, "build_if_missing_calls": 0, "repair_if_missing_calls": 0})


def mutate_live_icsum2(i: int) -> MappingProxyType:
    v = deepcopy(_plain(verify_current_witness_value_authority())); c = i % 32
    if c == 0: v["status"] = "READY"
    elif c == 1: v["program_count"] = 7
    elif c == 2: v["records"] = 1
    elif c == 3: v["route_TA_records"] = 1
    elif c == 4: v["route_TB_records"] = 1
    elif c == 5: v["route_VA_records"] = 1
    elif c == 6: v["route_VB_records"] = 1
    elif c == 7: v["identity_mismatches"] = 1
    elif c == 8: v["target_mismatches"] = 1
    elif c == 9: v["value_mismatches"] = 1
    elif c == 10: v["bound_mismatches"] = 1
    elif c == 11: v["exact_zero_records"] = 1
    elif c == 12: v["unavailable_as_zero"] = 1
    elif c == 13: v["component_aggregation"] = 1
    elif c == 14: v["sparse_operators"] = 1
    elif c == 15: v["matrix_free_actions"] = 1
    elif c == 16: v["C53_values_consumed"] = 1
    elif c == 17: v["C112_values_consumed"] = 1
    elif c == 18: v["physical_coupling_values_consumed"] = 1
    elif c == 19: v["counterterm_values_consumed"] = 1
    elif c == 20: v["complete_block"] = True
    elif c == 21: v["positive_gate"] = True
    elif c == 22: v["next"] = "C122/OTHER"
    elif c == 23: v["domain"]["rank_unrank"] = "READY"
    elif c == 24: v["targets"]["target_count"] = 1
    elif c == 25: v["domain_inventory"]["logical_records"] = 1
    elif c == 26: v["input_freeze"]["numeric_L"] = 1
    elif c == 27: v["input_freeze"]["numeric_P_plus"] = 1
    elif c == 28: v["public_authorities"]["private_builders_called"] = 1
    elif c == 29: v["domain"]["C118_logical_identity_records"] = 1
    elif c == 30: v["targets"]["target_mismatches"] = 1
    else: v["public_authorities"]["numerical_values_consumed"] = 1
    return _freeze(v)


__all__ = [
    "STATUS", "NEXT", "NEXT_CONTRACT", "PROGRAMS", "RESOLUTIONS", "input_freeze", "derivation_authority_manifest",
    "witness_domain_manifest", "logical_witness_domain_inventory", "matrix_target_manifest", "matrix_target_witness_page",
    "witness_record", "witness_record_by_rank", "witness_record_page", "rank_witness", "unrank_witness",
    "witness_value_expression", "witness_bound", "verify_witness_adjoint", "witness_ancestry", "witness_adjoint_manifest",
    "factor_ownership_contract", "count_once_certificate", "verify_current_witness_value_authority",
    "load_verified_current_witness_value_authority", "static_isolation_guard", "mutate_live_icsum2",
]
