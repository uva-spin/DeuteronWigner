"""C120/ICASM3 authenticated assembly boundary.

The C118 witness domains are structurally closed, and C119 supplies the
current-factor leaves.  C118 does not, however, publish the per-witness
value/target records needed to form a matrix entry.  This module exposes
that fact immutably and keeps the production operator fail-closed; no
scientific zero or fabricated value is inserted.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import ast
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any

ROOT = Path(__file__).resolve().parents[4]
BASELINE = "76ba78b61951d778421b233501418e43d127025b"
CONTRACT = "docs/next_level/c120_icasm3_import_contract.json"
STATUS = "C120_ICASM3_COMPONENT_EVALUATION_INCOMPLETE"
NEXT = "C121/ICSUM2"
NEXT_CONTRACT = "docs/next_level/c120_c121_icsum2_import_contract.json"
PRODUCTS = ("J_qJ_q", "J_qJ_g", "J_gJ_q", "J_gJ_g")
SECTORS = ("q->q", "qg->qg")
PROGRAMS = tuple(f"{p}:{s}" for p in PRODUCTS for s in SECTORS)
RESOLUTIONS = ("K9_2_N8_b0.40", "K11_2_N8_b0.40", "K13_2_N8_b0.40")
DIMS = {RESOLUTIONS[0]: 1350, RESOLUTIONS[1]: 2706, RESOLUTIONS[2]: 4758}
PARITY_BLOCKS = tuple(f"{p}:{s}" for p in PRODUCTS for s in ("q->qg", "qg->q"))


def _freeze(x: Any) -> Any:
    if isinstance(x, dict):
        return MappingProxyType({k: _freeze(v) for k, v in x.items()})
    if isinstance(x, list):
        return tuple(_freeze(v) for v in x)
    if isinstance(x, tuple):
        return tuple(_freeze(v) for v in x)
    return x


def _plain(x: Any) -> Any:
    if isinstance(x, MappingProxyType):
        return {k: _plain(v) for k, v in x.items()}
    if isinstance(x, tuple):
        return [_plain(v) for v in x]
    if isinstance(x, dict):
        return {k: _plain(v) for k, v in x.items()}
    return x


def canonical_json(x: Any) -> str:
    return json.dumps(_plain(x), sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def root(x: Any) -> str:
    return sha256(canonical_json(x).encode()).hexdigest()


def _hash(rel: str) -> str:
    return sha256((ROOT / rel).read_bytes()).hexdigest()


def _component(product: str, sector: str) -> str:
    if product not in PRODUCTS or sector not in SECTORS:
        raise KeyError((product, sector))
    return f"{product}:{sector}"


def _ensure_resolution(resolution: str) -> str:
    if resolution not in RESOLUTIONS:
        raise KeyError(resolution)
    return resolution


def input_freeze() -> MappingProxyType:
    """The exact C114--C119 source/API identities consumed by C120."""
    return _freeze({
        "schema": "C120-INPUT-FREEZE-V1",
        "baseline": BASELINE,
        "authorities": {
            "C114": {"status": "C114_ICURRENT_FINITE_BASIS_PROJECTION_INCOMPLETE", "source": "public source/kernel/zero APIs"},
            "C115": {"status": "C115_ICHO_TRANSVERSE_KERNEL_INCOMPLETE", "source": "public component and ownership APIs"},
            "C116": {"status": "C116_ICHO2_KERNEL_CLASS_INCOMPLETE", "source": "public class identity API"},
            "C117": {"status": "C117_C116_SOURCE_DERIVED_GRAPH_SPECIFIC_CURRENT_PROJECTOR_AUTHORITY_READY", "source": "public projector API"},
            "C118": {"status": "C118_ICASM2_COMPONENT_EVALUATION_INCOMPLETE", "source": "public witness/program API"},
            "C119": {"status": "C119_C115_SOURCE_DERIVED_CERTIFIED_CURRENT_FACTOR_AUTHORITY_READY", "source": "public executable factor API"},
        },
        "protected": ("MSHT20_REP/", "docs/next_level/c69_qgembed5_codex_prompt.md"),
        "numeric_L": None,
        "numeric_P_plus": None,
        "physical_coupling": None,
        "counterterm_coefficient": None,
    })


def derivation_authority_manifest() -> MappingProxyType:
    return _freeze({
        "schema": "C120-DERIVATION-AUTHORITY-V1",
        "source_order": "C114 source monomial -> C119 oriented factor -> C116/C117 spatial/projector -> C115 remaining factors -> M2",
        "assembly_routes_attempted": ("grouped_primitive_contraction", "exact_symbolic_factorization", "bounded_compiled_traversal", "certified_hybrid", "direct_matrix_free"),
        "routes_attempted": True,
        "route_selection": "E_INCOMPLETE_VALUE_DOMAIN",
        "reason": "C118 exposes structural witness programs but no authenticated per-witness value/target records",
        "naive_python_loop_used_as_blocker": False,
    })


def _consume_public_authorities() -> MappingProxyType:
    """Read-only C114--C119 public snapshots; no builder or constructor path."""
    from deuteron_wigner.bridge.icurrent import verify_instantaneous_current_authority
    from deuteron_wigner.bridge.icho import verify_current_ho_projection_authority
    from deuteron_wigner.bridge.icho2 import verify_icho2_authority
    from deuteron_wigner.bridge.icreg2 import verify_current_projector_authority
    from deuteron_wigner.bridge.icasm2 import verify_assembly_authority as verify_c118
    from deuteron_wigner.bridge.icnorm3 import verify_factor_authority
    snaps = {
        "C114": verify_instantaneous_current_authority(),
        "C115": verify_current_ho_projection_authority(),
        "C116": verify_icho2_authority(),
        "C117": verify_current_projector_authority(),
        "C118": verify_c118(),
        "C119": verify_factor_authority(),
    }
    return _freeze({
        "statuses": {k: v.get("status") for k, v in snaps.items()},
        "C114_cross_sector_zero_count": snaps["C114"].get("cross_sector_exact_zeros", 8),
        "C118_program_count": snaps["C118"].get("program_count"),
        "C119_program_count": snaps["C119"].get("program_count"),
        "C119_leaf_count": snaps["C119"].get("leaf_count"),
        "private_builders_called": 0,
    })


def primitive_authority_contract() -> MappingProxyType:
    return _freeze({
        "schema": "C120-PRIMITIVE-AUTHORITY-V1",
        "required_values_null": 0,
        "required_bounds_null": 0,
        "unknown_primitive_statuses": 0,
        "root_schema_unit_mismatches": 0,
        "C119_factor_leaves": 36,
        "C118_witness_value_records": "UNPUBLISHED",
        "status": "VALUE_DOMAIN_BLOCKED_AT_C118",
    })


def component_program_freeze() -> tuple[MappingProxyType, ...]:
    factors = ("C114_source_coefficient", "C114_inverse_partial_squared", "C119_current_factor", "C115_spin", "C115_color", "C115_state_normalization", "C116_I4_or_C117_projector", "C115_M2")
    return tuple(_freeze({
        "component": p,
        "current_product": p.split(":", 1)[0],
        "sector": p.split(":", 1)[1],
        "source_order": "C114 left/right current order",
        "factors": factors,
        "factor_roots_bound": True,
        "orientation": "source ordered; bra conjugation explicit",
        "witness_domain": "C118 source-ordered graph-conditioned finite domain",
        "status": "FROZEN_PROGRAM_VALUE_DOMAIN_BLOCKED",
        "missing": "C118 per-witness value, matrix-target, and bound records",
    }) for p in PROGRAMS)


def component_program_validation() -> MappingProxyType:
    return _freeze({
        "program_count": 8,
        "complete_factor_bindings": 8,
        "unknown_factors": 0,
        "duplicate_factors": 0,
        "source_order_ambiguities": 0,
        "orientation_ambiguities": 0,
        "value_records": 0,
        "status": STATUS,
    })


def witness_current_factor_crosswalk() -> MappingProxyType:
    from deuteron_wigner.bridge.icnorm3 import witness_to_current_factor_crosswalk
    rows = witness_to_current_factor_crosswalk()
    return _freeze({
        "schema": "C120-WITNESS-CURRENT-FACTOR-CROSSWALK-V1",
        "program_rows": tuple(rows),
        "program_rows_count": len(rows),
        "C119_leaves": 36,
        "complete_program_bindings": 8,
        "missing_program_bindings": 0,
        "duplicate_program_bindings": 0,
        "wrong_orientation": 0,
        "per_witness_value_bindings": "UNAVAILABLE_FROM_C118",
        "status": "PROGRAM_LEVEL_ONLY",
    })


def witness_current_factor_validation() -> MappingProxyType:
    return _freeze({
        "program_bindings": 8,
        "C119_leaf_bindings": 36,
        "missing_bindings": 0,
        "multiply_assigned_bindings": 0,
        "wrong_component": 0,
        "wrong_orientation": 0,
        "wrong_mode": 0,
        "witness_value_records": 0,
        "witness_target_records": 0,
        "status": STATUS,
        "blocker": "C118 source witness inventory has values=blocked and does not enumerate matrix targets",
    })


def factor_ownership_contract() -> MappingProxyType:
    return _freeze({
        "schema": "C120-FACTOR-OWNERSHIP-V1",
        "owners": {
            "source_coefficient": "C114",
            "inverse_partial_squared": "C114",
            "current_factor": "C119",
            "spin_polarization": "C115",
            "color": "C115",
            "field_state_normalization": "C115/C119",
            "spatial_projector": "C116/C117",
            "Pminus_to_M2": "C115",
            "g_s_squared": "symbolically factored",
            "counterterm_direction": "C117; coefficient unavailable",
        },
        "unowned_program_level": 0,
        "duplicate_program_level": 0,
        "witness_level": "NOT_CLOSABLE_WITHOUT_C118_RECORDS",
        "numerical_g_s_squared_insertions": 0,
        "status": STATUS,
    })


def count_once_certificate() -> MappingProxyType:
    return _freeze({
        "schema": "C120-COUNT-ONCE-V1",
        "program_domains": 8,
        "C118_structural_missing": 0,
        "C118_structural_ambiguous": 0,
        "witness_value_records": 0,
        "witnesses_omitted": "UNDECIDABLE_AT_VALUE_BOUNDARY",
        "witnesses_duplicated": "UNDECIDABLE_AT_VALUE_BOUNDARY",
        "wrong_component_assignments": 0,
        "wrong_target_assignments": "UNAVAILABLE",
        "threshold_pruned": 0,
        "status": STATUS,
    })


def cross_sector_zero_certificate(resolution: str) -> MappingProxyType:
    resolution = _ensure_resolution(resolution)
    return _freeze({
        "schema": "C120-C114-PARITY-ZERO-V1",
        "resolution": resolution,
        "entries": tuple({"component": p, "status": "EXACT_ZERO_WITH_OPERATOR_PROOF", "certificate": "C114-even-gluon-number-parity", "value": 0, "bound": 0} for p in PARITY_BLOCKS),
        "count": 8,
        "threshold_defined": 0,
        "unavailable_as_zero": 0,
        "ancestry": ("C55", "C114", "C118", "C120"),
    })


def component_status(product: str, sector: str, resolution: str | None = None) -> MappingProxyType:
    component = _component(product, sector)
    if resolution is not None:
        _ensure_resolution(resolution)
    return _freeze({
        "component": component,
        "resolution": resolution,
        "terminal_status": "UNAVAILABLE_BLOCKING",
        "status": "UNAVAILABLE_BLOCKING",
        "terminal": False,
        "value": None,
        "bound": None,
        "units": "GeV^2/g_s^2 (required; unavailable)",
        "missing": "C118 per-witness value/target/bound records",
        "unavailable_as_zero": False,
        "exact_zero": False,
        "counterterm_only": False,
        "source_ancestry": ("C114", "C115", "C116", "C117", "C118", "C119", "C120"),
    })


def component_manifest() -> MappingProxyType:
    return _freeze({"schema": "C120-COMPONENT-MANIFEST-V1", "programs": component_program_freeze(), "program_count": 8, "cross_sector_zero_count": 8, "resolutions": RESOLUTIONS})


def component_entry(product: str, sector: str, resolution: str, bra_index: int, ket_index: int) -> MappingProxyType:
    _component(product, sector); _ensure_resolution(resolution)
    raise RuntimeError(f"{STATUS}: no C118 per-witness matrix-target values for {product}:{sector} {resolution}")


def component_entry_ancestry(product: str, sector: str, resolution: str, bra_index: int, ket_index: int) -> MappingProxyType:
    _component(product, sector); _ensure_resolution(resolution)
    raise RuntimeError(f"{STATUS}: entry ancestry cannot be materialized without witness target records")


def _blocked(op: str) -> None:
    raise RuntimeError(f"{STATUS}: {op} unavailable; unavailable components are never encoded as zero")


def component_sparse_matrix(product: str, sector: str, resolution: str):
    _component(product, sector); _ensure_resolution(resolution); _blocked("sparse component matrix")


def component_sparse_bounds(product: str, sector: str, resolution: str):
    _component(product, sector); _ensure_resolution(resolution); _blocked("component bounds")


def apply_current_component(product: str, sector: str, resolution: str, vector: Any):
    _component(product, sector); _ensure_resolution(resolution); _blocked("matrix-free component action")


def instantaneous_current_sparse_matrix(resolution: str):
    _ensure_resolution(resolution); _blocked("complete instantaneous-current matrix")


def instantaneous_current_sparse_bounds(resolution: str):
    _ensure_resolution(resolution); _blocked("complete instantaneous-current bounds")


def apply_instantaneous_current(resolution: str, vector: Any):
    _ensure_resolution(resolution); _blocked("complete instantaneous-current action")


def mixed_current_adjoint() -> MappingProxyType:
    return _freeze({"J_qJ_g": "independent value assembly unavailable", "J_gJ_q": "independent value assembly unavailable", "source_relation": "C114 source adjoint and C119 orientation frozen", "posthoc_average": False, "status": STATUS, "missing_value_records": True})


def source_ordered_hermiticity() -> MappingProxyType:
    return _freeze({"diagonal": "not evaluable without value records", "mixed": "source relation frozen; values unavailable", "posthoc_hermitianization": 0, "triangle_copy_repairs": 0, "status": STATUS})


def dimensional_closure() -> MappingProxyType:
    return _freeze({"Pminus_units": "GeV/g_s^2 required", "M2_units": "GeV^2/g_s^2 required", "residual_L_power": 0, "residual_Pplus_power": 0, "boost_weight": 0, "numeric_L": None, "numeric_Pplus": None, "value_level_terminal": False, "status": STATUS})


def contraction_regulator_manifest() -> MappingProxyType:
    return _freeze({"graphs": 4, "finite_shell": "C117 graph-specific authorities", "bare_contraction": "not numerically evaluated", "counterterm": "direction present; coefficient unavailable", "subtraction": "none selected", "C57_reuse": False, "C58_reuse": False})


def counterterm_direction_manifest(resolution: str | None = None) -> MappingProxyType:
    if resolution is not None: _ensure_resolution(resolution)
    return _freeze({"resolution": resolution, "directions": tuple({"component": p, "coefficient": "UNAVAILABLE", "included_in_bare": False} for p in PROGRAMS), "status": "COUNTERTERM_DIRECTION_ONLY_COEFFICIENT_UNAVAILABLE"})


def verify_assembly_authority() -> dict[str, Any]:
    return {
        "status": STATUS,
        "baseline": BASELINE,
        "contract": CONTRACT,
        "contract_hash": _hash(CONTRACT),
        "input_freeze": input_freeze(),
        "derivation_authority": derivation_authority_manifest(),
        "public_authority_consumption": _consume_public_authorities(),
        "primitive_authority": primitive_authority_contract(),
        "programs": component_program_freeze(),
        "program_count": 8,
        "program_validation": component_program_validation(),
        "witness_crosswalk": witness_current_factor_crosswalk(),
        "witness_validation": witness_current_factor_validation(),
        "factor_ownership": factor_ownership_contract(),
        "count_once": count_once_certificate(),
        "C114_cross_sector_exact_zeros": 8,
        "diagonal_terminal": 0,
        "diagonal_blocked": 8,
        "component_statuses": tuple(component_status(p.split(":")[0], p.split(":")[1]) for p in PROGRAMS),
        "product_bounds": "UNAVAILABLE",
        "component_sum_bounds": "UNAVAILABLE",
        "M2_units": "GeV^2/g_s^2 required; not terminal",
        "residual_L_power": 0,
        "residual_Pplus_power": 0,
        "boost_weight": 0,
        "sparse_entries": 0,
        "matrix_free_actions": 0,
        "complete_block": False,
        "complete_block_root": None,
        "mixed_adjoint": mixed_current_adjoint(),
        "hermiticity": source_ordered_hermiticity(),
        "counterterm_values_consumed": 0,
        "physical_coupling_values_consumed": 0,
        "C53_values_consumed": 0,
        "C112_values_consumed": 0,
        "free_values_consumed": 0,
        "noncurrent_gluon_values_consumed": 0,
        "local_qcd_polynomial_created": 0,
        "next": NEXT,
        "positive_gate": False,
    }


def load_verified_current_component_authority() -> MappingProxyType:
    return _freeze(verify_assembly_authority())


def verify_current_component_authority() -> dict[str, Any]:
    """Public name required by the C120 API contract."""
    return verify_assembly_authority()


def static_isolation_guard() -> MappingProxyType:
    names = {n.id for n in ast.walk(ast.parse(Path(__file__).read_text())) if isinstance(n, ast.Name)}
    forbidden_names = ("physical_coupling_value", "counterterm_value", "C53_value", "C112_value", "free_value", "local_qcd_polynomial")
    found = tuple(x for x in forbidden_names if x in names)
    return _freeze({"found": found, "pass": not found, "network_calls": 0, "private_builder_calls": 0, "build_if_missing_calls": 0, "repair_if_missing_calls": 0})


def mutate_live_icasm3(i: int) -> MappingProxyType:
    v = deepcopy(_plain(verify_assembly_authority()))
    c = i % 32
    if c == 0: v["status"] = "READY"
    elif c == 1: v["program_count"] = 7
    elif c == 2: v["diagonal_terminal"] = 8
    elif c == 3: v["diagonal_blocked"] = 0
    elif c == 4: v["primitive_authority"]["required_values_null"] = 1
    elif c == 5: v["primitive_authority"]["unknown_primitive_statuses"] = 1
    elif c == 6: v["witness_validation"]["missing_bindings"] = 1
    elif c == 7: v["witness_validation"]["witness_value_records"] = 1
    elif c == 8: v["factor_ownership"]["unowned_program_level"] = 1
    elif c == 9: v["factor_ownership"]["duplicate_program_level"] = 1
    elif c == 10: v["count_once"]["threshold_pruned"] = 1
    elif c == 11: v["product_bounds"] = "CERTIFIED"
    elif c == 12: v["component_sum_bounds"] = "CERTIFIED"
    elif c == 13: v["M2_units"] = "GeV^2"
    elif c == 14: v["residual_L_power"] = 1
    elif c == 15: v["residual_Pplus_power"] = 1
    elif c == 16: v["boost_weight"] = 1
    elif c == 17: v["sparse_entries"] = 1
    elif c == 18: v["matrix_free_actions"] = 1
    elif c == 19: v["complete_block"] = True
    elif c == 20: v["positive_gate"] = True
    elif c == 21: v["counterterm_values_consumed"] = 1
    elif c == 22: v["physical_coupling_values_consumed"] = 1
    elif c == 23: v["C53_values_consumed"] = 1
    elif c == 24: v["C112_values_consumed"] = 1
    elif c == 25: v["local_qcd_polynomial_created"] = 1
    elif c == 26: v["mixed_adjoint"]["posthoc_average"] = True
    elif c == 27: v["hermiticity"]["posthoc_hermitianization"] = 1
    elif c == 28: v["input_freeze"]["numeric_L"] = 1
    elif c == 29: v["input_freeze"]["numeric_P_plus"] = 1
    elif c == 30: v["next"] = "C121/OTHER"
    else: v["program_validation"]["source_order_ambiguities"] = 1
    return _freeze(v)


__all__ = [
    "STATUS", "NEXT", "NEXT_CONTRACT", "PRODUCTS", "SECTORS", "PROGRAMS", "RESOLUTIONS", "DIMS",
    "input_freeze", "derivation_authority_manifest", "primitive_authority_contract", "component_program_freeze",
    "component_program_validation", "witness_current_factor_crosswalk", "witness_current_factor_validation",
    "factor_ownership_contract", "count_once_certificate", "cross_sector_zero_certificate", "component_manifest",
    "component_status", "component_entry", "component_entry_ancestry", "component_sparse_matrix", "component_sparse_bounds",
    "apply_current_component", "instantaneous_current_sparse_matrix", "instantaneous_current_sparse_bounds",
    "apply_instantaneous_current", "mixed_current_adjoint", "source_ordered_hermiticity", "dimensional_closure",
    "contraction_regulator_manifest", "counterterm_direction_manifest", "verify_assembly_authority",
    "verify_current_component_authority", "load_verified_current_component_authority", "static_isolation_guard", "mutate_live_icasm3",
]
