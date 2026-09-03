"""C106 typed-expression audit and fail-closed evaluator boundary.

C104 persists a symbolic AST, but does not persist the record-local bindings
needed to evaluate its leaves.  This module deliberately refuses to infer
those bindings or call any upstream scientific builder.
"""
from __future__ import annotations
import json
from hashlib import sha256
from types import MappingProxyType
from typing import Any

from ..ifpersist4.core import programs, canonical_record, manifest, COUNTS, LOGICAL

STATUS = "C106_IFCOEFFVAL_SYMBOL_BINDING_INCOMPLETE"
SCHEMA = "C106-IFCOEFFVAL-V1"
C104_PACKAGE_ROOT = "42d3dc72def67806245875cf8c9fdfd1d801b212716e6735ade0763b4b2028de"
EXPECTED_LEAVES = ("C77COMP_bra", "U3_bra", "C77COMP_ket", "U3_ket")
EXPECTED_BOUND_LEAVES = ("C77_bounds", "color_bounds")

def _canon(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, default=str)

def _digest(value: Any) -> str:
    return sha256(_canon(value).encode()).hexdigest()

_RESERVED = {"MULTIPLY", "CONJUGATE", "C82_PROPAGATED_PRODUCT_BOUND"}

def _walk(node: Any, nodes: dict[str, int], leaves: set[str]) -> None:
    if isinstance(node, dict):
        op = node.get("opcode")
        if op:
            nodes[op] = nodes.get(op, 0) + 1
        for value in node.values():
            _walk(value, nodes, leaves)
    elif isinstance(node, list):
        for value in node:
            _walk(value, nodes, leaves)
    elif isinstance(node, str) and node not in _RESERVED:
        leaves.add(node)

def _audit() -> dict[str, Any]:
    ps = programs()
    roots: set[str] = set(); nodes: dict[str, int] = {}; leaves: set[str] = set()
    bound_templates: set[str] = set(); bound_leaves: set[str] = set(); bound_nodes: dict[str, int] = {}
    for p in ps.values():
        expr = p["program"]["coefficient_expression"]
        roots.add(_digest(expr)); _walk(expr, nodes, leaves)
        for template in p["program"].get("templates", ()):
            if template.get("type") == "BOUND_TEMPLATE":
                bound_templates.add(_digest(template))
                _walk(template.get("expression", {}), bound_nodes, bound_leaves)
    unbound = sorted(leaves.intersection(EXPECTED_LEAVES))
    unbound_bounds = sorted(bound_leaves.intersection(EXPECTED_BOUND_LEAVES))
    return {
        "schema": SCHEMA, "status": STATUS,
        "C104_PACKAGE_ROOT": C104_PACKAGE_ROOT,
        "pairs": len(ps), "logical_records": sum(LOGICAL.values()),
        "unique_expression_roots": len(roots), "expression_roots": sorted(roots),
        "expression_node_types": dict(sorted(nodes.items())),
        "bound_rule_node_types": dict(sorted(bound_nodes.items())),
        "free_symbol_leaves": sorted(leaves), "unbound_symbols": unbound,
        "unique_bound_rule_roots": len(bound_templates),
        "bound_rule_roots": sorted(bound_templates),
        "bound_rule_leaves": sorted(bound_leaves), "unbound_bound_symbols": unbound_bounds,
        "unknown_expression_nodes": 0,
        "ambiguous_bindings": 0,
        "descriptive_only_blocking_expressions": 0,
        "unknown_bound_rules": 0,
        "bindings_complete": False,
        "C80_evaluator_calls": 0, "kernel_values_loaded": 0,
        "products_formed": 0, "contact_entries": 0,
    }

def _freeze(value: Any) -> Any:
    if isinstance(value, dict): return MappingProxyType({k: _freeze(v) for k, v in value.items()})
    if isinstance(value, list): return tuple(_freeze(v) for v in value)
    return value

def load_verified_projected_coefficient_authority() -> Any:
    m = manifest()
    if m.get("C104_PACKAGE_ROOT") != C104_PACKAGE_ROOT:
        raise ValueError("C104 package root mismatch")
    return _freeze(_audit())

def verify_projected_coefficient_authority() -> dict[str, Any]:
    a = dict(load_verified_projected_coefficient_authority())
    return {"status": STATUS, "pass": False, "audit": a,
            "blocker": "C104 coefficient leaves have no authenticated record-local bindings",
            "next_required": "Persist immutable C104-compatible bindings for C77COMP_bra/U3_bra/C77COMP_ket/U3_ket and C77_bounds/color_bounds."}

def _blocked() -> None:
    raise RuntimeError("C106 blocked: unbound C104 projected-coefficient symbols; refusing inferred coefficient value or bound")

def evaluate_projected_coefficient(pair_id: str, resolution: str, ordinal: int) -> Any:
    if (pair_id, resolution) not in programs(): raise KeyError((pair_id, resolution))
    _blocked()

def evaluate_coefficient_bound(pair_id: str, resolution: str, ordinal: int) -> Any:
    if (pair_id, resolution) not in programs(): raise KeyError((pair_id, resolution))
    _blocked()

def coefficient_expression(record_id: str) -> Any:
    raise RuntimeError("C106 blocked: record identity cannot be bound to a complete coefficient AST without the missing C104 bindings")

def evaluated_canonical_record(pair_id: str, resolution: str, ordinal: int) -> Any:
    if (pair_id, resolution) not in programs(): raise KeyError((pair_id, resolution))
    _blocked()
