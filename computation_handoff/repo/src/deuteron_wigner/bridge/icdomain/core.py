"""C122/ICDOMAIN logical witness-domain boundary.

The package preserves the eight C118 program templates and the exact C114
cross-sector zero classes.  C117's graph-domain records are descriptive and
do not publish finite axis members/cardinalities, while C118 publishes no
logical witness identities.  C122 consequently fails closed at the logical
axis gate rather than inferring witnesses, targets, or ranks.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import ast, json
from pathlib import Path
from types import MappingProxyType
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
BASELINE = "1983726b81809e72c6a9078658ce60903527fa0d"
CONTRACT = "docs/next_level/c121_c122_icdomain_import_contract.json"
STATUS = "C122_ICDOMAIN_LOGICAL_AXES_INCOMPLETE"
NEXT = "C123/ICAXIS"
NEXT_CONTRACT = "docs/next_level/c122_c123_icaxis_import_contract.json"
PROGRAMS = (
    "J_qJ_q:q->q", "J_qJ_q:qg->qg", "J_qJ_g:q->q", "J_qJ_g:qg->qg",
    "J_gJ_q:q->q", "J_gJ_q:qg->qg", "J_gJ_g:q->q", "J_gJ_g:qg->qg",
)
PRODUCTS = ("J_qJ_q", "J_qJ_g", "J_gJ_q", "J_gJ_g")
SECTORS = ("q->q", "qg->qg")
RESOLUTIONS = ("K9_2_N8_b0.40", "K11_2_N8_b0.40", "K13_2_N8_b0.40")
ZERO_CLASSES = tuple(f"{p}:{s}" for p in PRODUCTS for s in ("q->qg", "qg->q"))


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


def canonical_json(x: Any) -> str: return json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True)
def root(x: Any) -> str: return sha256(canonical_json(x).encode()).hexdigest()
def _hash(rel: str) -> str: return sha256((ROOT / rel).read_bytes()).hexdigest()


def input_freeze() -> MappingProxyType:
    return _freeze({
        "schema": "C122-INPUT-FREEZE-V1", "baseline": BASELINE,
        "C118_program_templates": 8, "C118_logical_witness_ids": 0,
        "C118_matrix_targets": 0, "C118_target_spans": 0,
        "C117_axis_members": "UNPUBLISHED_CARDINALITIES",
        "C119_factor_leaves": 36, "numeric_values_loaded": 0,
        "historical_C118_recovery": False, "numeric_L": None, "numeric_P_plus": None,
    })


def _consume_public_authorities() -> MappingProxyType:
    from deuteron_wigner.bridge.icasm2 import verify_assembly_authority
    from deuteron_wigner.bridge.icreg2 import verify_current_projector_authority
    from deuteron_wigner.bridge.icnorm3 import verify_factor_authority
    from deuteron_wigner.bridge.iferm3 import instantaneous_fermion_sector_manifest
    c118 = verify_assembly_authority(); c117 = verify_current_projector_authority(); c119 = verify_factor_authority()
    labels = ("K9_2_N8_b0.40", "K11_2_N10_b0.45", "K13_2_N12_b0.50")
    basis = tuple(instantaneous_fermion_sector_manifest(r) for r in labels)
    return _freeze({
        "C118_status": c118.get("status"), "C118_programs": c118.get("program_count"),
        "C117_status": c117.get("status"), "C117_internal_domains": len(c117.get("internal_domains", ())),
        "C119_status": c119.get("status"), "C119_leaves": c119.get("leaf_count"),
        "C112_basis_manifests": tuple({"shape": b["direct_sum_shape"], "order": b["global_order"]} for b in basis),
        "numeric_values_consumed": 0, "private_builders_called": 0,
    })


def domain_taxonomy() -> MappingProxyType:
    return _freeze({
        "schema": "C122-DOMAIN-TAXONOMY-V1",
        "PROGRAM_TEMPLATE_DOMAIN": {"count": 8, "source": "C118 structural rows", "status": "CLOSED"},
        "LOGICAL_WITNESS_DOMAIN": {"count": None, "source": "C122 descendant construction", "status": STATUS},
        "VALUE_DOMAIN": {"count": None, "owner": "C123", "status": "NOT_IN_C122"},
        "historical_C118_recovery": False,
    })


def logical_axis_inventory() -> MappingProxyType:
    axes = ("physical_bra_state", "physical_ket_state", "source_graph", "monomial_descendant", "longitudinal_transfer", "external_modes", "spin_polarization", "ordered_color", "CM_ground", "triplet", "orientation")
    return _freeze({"schema": "C122-LOGICAL-AXIS-INVENTORY-V1", "axes": tuple({"axis_id": a, "cardinality": None, "canonical_order": None, "authority": "not enumerated by C117/C118 public API"} for a in axes), "unknown_required_axes": len(axes), "array_position_identity": 0, "magnitude_selection": 0, "status": STATUS})


def atomicity_ledger() -> MappingProxyType:
    return _freeze({"schema": "C122-ATOMICITY-V1", "classifications": ("UPSTREAM_PRIMITIVE_OWNS_SUM", "C122_WITNESS_DOMAIN_OWNS_MODE", "EXACT_FACTORIZED_AXIS", "NOT_APPLICABLE_WITH_PROOF"), "classified_sums": 0, "unclassified_internal_sums": None, "projector_sums_unrolled": 0, "mode_axes_omitted": None, "status": STATUS})


def component_program_manifest() -> MappingProxyType:
    return _freeze({"schema": "C122-PROGRAM-TEMPLATE-V1", "programs": PROGRAMS, "program_count": 8, "source_order": "C118/C114", "logical_domain_instantiated": False})


def logical_witness_domain_manifest() -> MappingProxyType:
    return _freeze({"schema": "C122-LOGICAL-WITNESS-DOMAIN-V1", "program_templates": 8, "logical_witness_count": None, "segments": 0, "rank_unrank": "UNAVAILABLE", "status": STATUS, "blocker": "C117 graph axes lack public members/cardinalities and C118 lacks logical witness identities"})


def logical_witness_census() -> MappingProxyType:
    return _freeze({"schema": "C122-CENSUS-V1", "program_templates": 8, "complete_component_coverage": 8, "logical_witnesses": None, "candidate": None, "admitted": None, "rejected": None, "route_DA": 0, "route_DB": 0, "status": STATUS})


def cross_sector_zero_domain_manifest() -> MappingProxyType:
    return _freeze({"schema": "C122-CROSS-SECTOR-ZERO-DOMAIN-V1", "classes": tuple({"class": c, "resolutions": RESOLUTIONS, "certificate": "C114-even-gluon-number-parity", "logical_witnesses": 0, "targets": 0, "empty_domain": True} for c in ZERO_CLASSES), "class_count": 8, "logical_witnesses": 0, "targets": 0, "numerical_zero_records": 0, "status": "EXACT_ZERO_EMPTY_DOMAINS"})


def _check_component(component_id: str) -> str:
    if component_id not in PROGRAMS: raise KeyError(component_id)
    return component_id


def _check_resolution(resolution: str) -> str:
    if resolution not in RESOLUTIONS: raise KeyError(resolution)
    return resolution


def _missing(op: str) -> None:
    raise RuntimeError(f"{STATUS}: {op} unavailable; logical axis members/cardinalities are not authenticated")


def witness_identity(witness_id: str) -> MappingProxyType: _missing("witness_identity")
def witness_by_rank(component_id: str, resolution: str, rank: int) -> MappingProxyType: _check_component(component_id); _check_resolution(resolution); _missing("witness_by_rank")
def witness_rank(witness_id: str) -> int: _missing("witness_rank")
def witness_adjoint_partner(witness_id: str) -> MappingProxyType: _missing("witness_adjoint_partner")
def primitive_reference_manifest(witness_id: str) -> MappingProxyType: _missing("primitive_reference_manifest")


def witness_page(*, component_id: str | None = None, resolution: str | None = None, graph_id: str | None = None, matrix_target_id: str | None = None, selection_status: str | None = None, cursor: str | None = None, limit: int = 128) -> MappingProxyType:
    if limit <= 0: raise ValueError(limit)
    if component_id is not None: _check_component(component_id)
    if resolution is not None: _check_resolution(resolution)
    return _freeze({"schema": "C122-WITNESS-PAGE-V1", "records": (), "cursor": cursor, "next_cursor": None, "terminal": True, "page_root": root(()), "status": STATUS})


def matrix_target_manifest(component_id: str, resolution: str) -> MappingProxyType:
    _check_component(component_id); _check_resolution(resolution)
    return _freeze({"schema": "C122-MATRIX-TARGET-MANIFEST-V1", "component": component_id, "resolution": resolution, "targets": (), "target_count": 0, "route_TA": "NOT_INSTANTIATED", "route_TB": "NOT_INSTANTIATED", "status": "C122_ICDOMAIN_MATRIX_TARGET_INCOMPLETE"})


def matrix_target_witness_page(component_id: str, resolution: str, bra_index: int, ket_index: int, *, cursor: str | None = None, limit: int = 128) -> MappingProxyType:
    _check_component(component_id); _check_resolution(resolution)
    return _freeze({"schema": "C122-TARGET-WITNESS-PAGE-V1", "records": (), "cursor": cursor, "next_cursor": None, "terminal": True, "status": STATUS})


def count_once_certificate() -> MappingProxyType:
    return _freeze({"schema": "C122-COUNT-ONCE-V1", "logical_witnesses": None, "omitted": None, "duplicated": None, "wrong_target": None, "target_spans": 0, "status": STATUS})


def factor_ownership_contract() -> MappingProxyType:
    return _freeze({"schema": "C122-FACTOR-OWNERSHIP-V1", "program_template_unowned": 0, "logical_witness_unowned": None, "logical_witness_duplicates": None, "values": 0, "status": STATUS})


def verify_current_logical_domain() -> dict[str, Any]:
    return {"status": STATUS, "baseline": BASELINE, "contract": CONTRACT, "contract_hash": _hash(CONTRACT), "input_freeze": input_freeze(), "taxonomy": domain_taxonomy(), "axis_inventory": logical_axis_inventory(), "atomicity": atomicity_ledger(), "programs": component_program_manifest(), "domain": logical_witness_domain_manifest(), "census": logical_witness_census(), "public_authorities": _consume_public_authorities(), "route_DA": 0, "route_DB": 0, "route_TA": 0, "route_TB": 0, "logical_witnesses": None, "matrix_targets": 0, "segments": 0, "rank_unrank": False, "cross_sector": cross_sector_zero_domain_manifest(), "witness_values_formed": 0, "witness_bounds_formed": 0, "component_sums": 0, "sparse_entries": 0, "matrix_free_actions": 0, "C53_values_consumed": 0, "C112_values_consumed": 0, "physical_couplings_consumed": 0, "counterterm_values_consumed": 0, "complete_block": False, "positive_gate": False, "next": NEXT}


def load_verified_current_logical_domain() -> MappingProxyType: return _freeze(verify_current_logical_domain())


def static_isolation_guard() -> MappingProxyType:
    names = {n.id for n in ast.walk(ast.parse(Path(__file__).read_text())) if isinstance(n, ast.Name)}
    forbidden = ("witness_value", "witness_bound", "component_sum", "sparse_matrix", "matrix_free_action", "physical_coupling_value", "counterterm_value")
    found = tuple(x for x in forbidden if x in names)
    return _freeze({"found": found, "pass": not found, "private_builder_calls": 0, "network_calls": 0, "build_if_missing_calls": 0, "repair_if_missing_calls": 0})


def mutate_live_icdomain(i: int) -> MappingProxyType:
    v = deepcopy(_plain(verify_current_logical_domain())); c = i % 32
    if c == 0: v["status"] = "READY"
    elif c == 1: v["route_DA"] = 1
    elif c == 2: v["route_DB"] = 1
    elif c == 3: v["route_TA"] = 1
    elif c == 4: v["route_TB"] = 1
    elif c == 5: v["logical_witnesses"] = 1
    elif c == 6: v["matrix_targets"] = 1
    elif c == 7: v["segments"] = 1
    elif c == 8: v["rank_unrank"] = True
    elif c == 9: v["witness_values_formed"] = 1
    elif c == 10: v["witness_bounds_formed"] = 1
    elif c == 11: v["component_sums"] = 1
    elif c == 12: v["sparse_entries"] = 1
    elif c == 13: v["matrix_free_actions"] = 1
    elif c == 14: v["C53_values_consumed"] = 1
    elif c == 15: v["C112_values_consumed"] = 1
    elif c == 16: v["physical_couplings_consumed"] = 1
    elif c == 17: v["counterterm_values_consumed"] = 1
    elif c == 18: v["complete_block"] = True
    elif c == 19: v["positive_gate"] = True
    elif c == 20: v["next"] = "C123/OTHER"
    elif c == 21: v["axis_inventory"]["unknown_required_axes"] = 0
    elif c == 22: v["atomicity"]["classified_sums"] = 1
    elif c == 23: v["census"]["logical_witnesses"] = 1
    elif c == 24: v["cross_sector"]["numerical_zero_records"] = 1
    elif c == 25: v["public_authorities"]["numeric_values_consumed"] = 1
    elif c == 26: v["input_freeze"]["numeric_L"] = 1
    elif c == 27: v["input_freeze"]["numeric_P_plus"] = 1
    elif c == 28: v["axis_inventory"]["array_position_identity"] = 1
    elif c == 29: v["axis_inventory"]["magnitude_selection"] = 1
    elif c == 30: v["cross_sector"]["class_count"] = 7
    else: v["atomicity"]["projector_sums_unrolled"] = 1
    return _freeze(v)


__all__ = ["STATUS", "NEXT", "NEXT_CONTRACT", "PROGRAMS", "PRODUCTS", "SECTORS", "RESOLUTIONS", "input_freeze", "domain_taxonomy", "logical_axis_inventory", "atomicity_ledger", "component_program_manifest", "logical_witness_domain_manifest", "logical_witness_census", "cross_sector_zero_domain_manifest", "witness_identity", "witness_by_rank", "witness_rank", "witness_page", "matrix_target_manifest", "matrix_target_witness_page", "witness_adjoint_partner", "primitive_reference_manifest", "count_once_certificate", "factor_ownership_contract", "verify_current_logical_domain", "load_verified_current_logical_domain", "static_isolation_guard", "mutate_live_icdomain"]
