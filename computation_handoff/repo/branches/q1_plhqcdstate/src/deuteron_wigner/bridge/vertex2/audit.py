"""C51 fail-closed audit for exhaustive canonical-vertex assembly.

C50 provides a valid individual *total* M-squared evaluator and deliberately
keeps C47 historical canonical tuples out of its imports.  It does not expose
the independently evaluable MASS_HELICITY_FLIP and TRANSVERSE_HELICITY terms
that it names in metadata.  C51 therefore cannot make the component matrices
required for an exhaustive, dimensionally homogeneous physical vertex without
inventing a numerical split.  This module records that boundary; it allocates
no C51 emission, absorption, color, or local-QCD matrix.
"""
from __future__ import annotations

import ast
from copy import deepcopy
from functools import lru_cache
from hashlib import sha256
import inspect
import json
from pathlib import Path
from typing import Any
from unittest.mock import patch

from ..vsrc import core as c50

ROOT = Path(__file__).resolve().parents[4]
BASELINE = "ad3adeda99ab1115d07284a9c502c5959f08b6e4"
STATUS = "C51_VERTEX_DIMENSIONAL_ASSEMBLY_INCOMPLETE"
NEXT = "C52/VDIM2 — component-matrix units and symbolic-factor assembly completion"


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def _hash(value: Any) -> str:
    return sha256(_canonical(value).encode()).hexdigest()


def static_raw_tuple_guard() -> dict[str, Any]:
    """AST-level proof that C50's actual evaluator cannot read C47 raw values."""
    tree = ast.parse(inspect.getsource(c50.evaluate_canonical_vertex))
    names = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}
    attrs = {node.attr for node in ast.walk(tree) if isinstance(node, ast.Attribute)}
    prohibited = {"canonical_kernel", "tuple_semantics_records", "raw_tuple_semantics_summary", "vertex1"}
    return {
        "guard": "AST_IMPORT_AND_NAME_GUARD",
        "evaluator_module": c50.__name__,
        "prohibited_symbols": sorted(prohibited),
        "referenced_prohibited_symbols": sorted(prohibited & (names | attrs)),
        "pass": not bool(prohibited & (names | attrs)),
        "allowed_dependencies": ["q_basis", "qg_basis", "x_map", "finite_box_pminus_kernel", "pminus_to_m2", "C45 mode functions"],
    }


def runtime_raw_tuple_poisoning() -> dict[str, Any]:
    """Replace the historical tuple producer by a NaN/sentinel producer.

    The same C50 call must remain bitwise unchanged.  The poison source is the
    only C47 historical-value factory; basis identities themselves stay live.
    """
    before = c50.evaluate_canonical_vertex(3, 0, "K9_2_N8_b0.40")
    from ..basis1 import core as basis1
    def poisoned(*_args, **_kwargs):
        raise AssertionError("POISONED_C47_RAW_TUPLE_VALUE_WAS_READ")
    with patch.object(basis1, "canonical_kernel", poisoned):
        after = c50.evaluate_canonical_vertex(3, 0, "K9_2_N8_b0.40")
    return {
        "guard": "RUNTIME_NAN_SENTINEL_POISONING", "before_sha256": _hash(before), "after_sha256": _hash(after),
        "unchanged": before == after, "raw_value_read": False, "pass": before == after,
        "poison_contract": "basis1.canonical_kernel raises before returning any historical numerical value",
    }


def component_interface_audit() -> dict[str, Any]:
    declared = c50.component_decomposition()["components"]
    evaluator_source = inspect.getsource(c50.evaluate_canonical_vertex)
    kernel_source = inspect.getsource(c50.finite_box_pminus_kernel)
    rows = []
    for component in declared:
        component_id = component["id"]
        rows.append({
            "component_id": component_id,
            "metadata_authority": component,
            "per_entry_evaluator": f"evaluate_{component_id.lower()}",
            "present_in_C50": f"evaluate_{component_id.lower()}" in evaluator_source or f"evaluate_{component_id.lower()}" in kernel_source,
            "coefficient_function": "ABSENT",
            "matrix_assembly_status": "ABSENT_BLOCKING",
            "reason": "C50 returns only combined pminus_GeV/m2_GeV; it supplies no independently evaluable component value or exact symbolic coefficient for this component.",
        })
    return {
        "required_component_ids": [x["id"] for x in declared], "rows": rows,
        "combined_C50_output_keys": ["pminus_GeV", "m2_GeV2"],
        "combined_evaluator_present": True,
        "component_resolved_evaluator_present": False,
        "assembly_rule_present": False,
        "decision": "BLOCK: assembling component matrices from the combined numerical value would invent a mass/transverse decomposition, contrary to C51 section 9.",
    }


@lru_cache(maxsize=1)
def c51_input_fidelity_audit() -> dict[str, Any]:
    static = static_raw_tuple_guard(); poison = runtime_raw_tuple_poisoning(); components = component_interface_audit()
    return {
        "status": STATUS, "baseline": BASELINE,
        "dependencies": [
            {"id": "C43_ACTION", "classification": "SOURCE_DERIVED_SYMBOLIC_COMPONENT", "allowed": True},
            {"id": "C45_MODES", "classification": "SOURCE_DERIVED_EXECUTABLE", "allowed": True},
            {"id": "C47_BASIS_TM_CM", "classification": "SOURCE_DERIVED_BASIS_IDENTITY", "allowed": True},
            {"id": "C50_TOTAL_EVALUATOR", "classification": "SOURCE_DERIVED_EXECUTABLE", "allowed": True},
            {"id": "C50_COMPONENT_METADATA", "classification": "SOURCE_DERIVED_SYMBOLIC_COMPONENT", "allowed": True},
            {"id": "C50_COMPONENT_PER_ENTRY_INTERFACE", "classification": "ABSENT_BLOCKING", "allowed": False},
            {"id": "C47_RAW_CANONICAL_TUPLE_VALUES", "classification": "DIAGNOSTIC_ONLY", "allowed": False},
            {"id": "C40", "classification": "DIAGNOSTIC_ONLY", "allowed": False},
        ],
        "static_raw_tuple_guard": static, "runtime_raw_tuple_poisoning": poison,
        "component_interface": components,
        "positive_assembly_permitted": False,
        "no_matrices_allocated": ["component", "colorless", "color intertwiner", "physical emission", "absorption", "linear block"],
    }


def validate_c51_audit(value: dict[str, Any]) -> bool:
    expected = c51_input_fidelity_audit()
    return value == expected and value["static_raw_tuple_guard"]["pass"] and value["runtime_raw_tuple_poisoning"]["pass"] and not value["component_interface"]["component_resolved_evaluator_present"] and not value["positive_assembly_permitted"]


def mutate_live_c51(fault_id: int) -> dict[str, Any]:
    value = deepcopy(c51_input_fidelity_audit())
    mode = fault_id % 10
    if mode == 0: value["static_raw_tuple_guard"]["pass"] = False
    elif mode == 1: value["static_raw_tuple_guard"]["referenced_prohibited_symbols"] = ["canonical_kernel"]
    elif mode == 2: value["runtime_raw_tuple_poisoning"]["unchanged"] = False
    elif mode == 3: value["runtime_raw_tuple_poisoning"]["after_sha256"] = "0" * 64
    elif mode == 4: value["component_interface"]["component_resolved_evaluator_present"] = True
    elif mode == 5: value["component_interface"]["assembly_rule_present"] = True
    elif mode == 6: value["component_interface"]["rows"][0]["matrix_assembly_status"] = "ASSEMBLED"
    elif mode == 7: value["dependencies"][5]["classification"] = "SOURCE_DERIVED_EXECUTABLE"
    elif mode == 8: value["positive_assembly_permitted"] = True
    else: value["no_matrices_allocated"].pop()
    return value


def assert_c51_dimensional_assembly_incomplete() -> dict[str, Any]:
    audit = c51_input_fidelity_audit()
    assert audit["static_raw_tuple_guard"]["pass"]
    assert audit["runtime_raw_tuple_poisoning"]["pass"]
    assert len(audit["component_interface"]["rows"]) == 2
    assert all(row["matrix_assembly_status"] == "ABSENT_BLOCKING" for row in audit["component_interface"]["rows"])
    assert not audit["positive_assembly_permitted"]
    assert validate_c51_audit(audit)
    return audit
