"""C54 blocks fabricated local QCD matrices before their source projection exists.

This module deliberately contains no local-HQCD matrix generator.  The C43
record fixes action-level instantaneous operators, while C45/C47 provide
modes and PV/P0/Q0 functionals; none supplies the required finite-volume,
normal-ordered q/qg matrix-element functional.  C54 therefore verifies the
C53 input byte-for-byte and fails at the first required instantaneous-fermion
projection gate instead of turning a schematic action term into a stencil.
"""
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
from hashlib import sha256
import ast
import inspect
import json
from pathlib import Path
from typing import Any

import numpy as np

ROOT = Path(__file__).resolve().parents[4]
BASELINE = "ec705d02960d3a1a644958d43d35277a85f9825c"
STATUS = "C54_INSTANTANEOUS_FERMION_ASSEMBLY_INCOMPLETE"
NEXT = "C55/IFERM — finite-volume light-front instantaneous-fermion matrix completion"
BLOCKER = "C54.IFERM.FINITE_VOLUME_NORMAL_ORDERED_PROJECTION"


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def array_hash(value: np.ndarray) -> str:
    x = np.ascontiguousarray(value)
    return sha256(x.dtype.str.encode() + str(x.shape).encode() + x.tobytes()).hexdigest()


def _read(name: str) -> dict[str, Any]:
    return json.loads((ROOT / "docs" / "next_level" / name).read_text())


def _file_hash(name: str) -> str:
    return sha256((ROOT / "docs" / "next_level" / name).read_bytes()).hexdigest()


def _inventory_by_name() -> dict[str, dict[str, Any]]:
    return {x["name"]: x for x in _read("c53_numerical_object_inventory.json")["objects"]}


def c53_read_only_import() -> dict[str, Any]:
    """Verify C53 runtime arrays and contracts without calling C53 builders."""
    inventory = _inventory_by_name()
    primitive = _read("c53_physical_vertex_primitive_matrices.json")["families"]
    symbol = _read("c53_physical_symbolic_vertex.json")["coefficient"]
    basis = _read("c53_physical_resolution_manifest.json")["resolutions"]
    matrix_free = _read("c53_physical_matrix_free_report.json")["all_resolution_columns"]
    poison = _read("c53_dependency_isolation_report.json")["runtime"]
    ancestry = _read("c53_physical_entry_ancestry.json")["entries"]
    count_once = _read("c53_count_once_report.json")["resolutions"]
    records = []
    for family in primitive:
        label = family["resolution"]
        for kind in ("physical_primitive", "physical_diagnostic_m2", "generated_absorption"):
            name = f"{kind}_{label}"
            record = inventory[name]
            path = ROOT / record["runtime_path"]
            value = np.load(path, allow_pickle=False) if path.is_file() else None
            records.append({"name": name, "resolution": label, "present": path.is_file(),
                            "expected_hash": record["array_sha256"],
                            "observed_hash": array_hash(value) if value is not None else None,
                            "hash_match": value is not None and array_hash(value) == record["array_sha256"],
                            "shape": list(record["shape"]), "basis_order_hash": record["basis_order_hash"],
                            "expression_hash": record["expression_hash"]})
        v = np.load(ROOT / inventory[f"physical_diagnostic_m2_{label}"]["runtime_path"], allow_pickle=False)
        a = np.load(ROOT / inventory[f"generated_absorption_{label}"]["runtime_path"], allow_pickle=False)
        records.append({"name": f"adjoint_identity_{label}", "resolution": label,
                        "present": True, "expected_hash": "generated_only", "observed_hash": None,
                        "hash_match": bool(np.linalg.norm(a-v.conj().T) == 0.0), "shape": list(a.shape),
                        "basis_order_hash": basis[label]["basis_order_hash"], "expression_hash": symbol["sha256"]})
    ancestry_hash = _file_hash("c53_physical_entry_ancestry.json")
    ancestry_counts = {family["resolution"]: len(ancestry[family["resolution"]]) for family in primitive}
    checks = {"primitive_runtime_hashes": all(x["hash_match"] for x in records),
              "expression_hash": symbol["sha256"], "expression_executable": symbol["srepr"].startswith("Mul("),
              "basis_hashes_present": all(bool(basis[x["resolution"]]["basis_order_hash"]) for x in records),
              "entry_ancestry_file_hash": ancestry_hash,
              "entry_ancestry_counts": ancestry_counts,
              "entry_ancestry_count_match": all(ancestry_counts[x["resolution"]] == x["primitive_nnz"] == count_once[x["resolution"]]["physical_nonzero_entries"] for x in primitive),
              "matrix_free_zero_residual": max(x["sparse_residual"] for x in matrix_free) == 0.0,
              "poisoning_pass": poison["pass"], "read_only": True}
    return {"status": "C53_READ_ONLY_IMPORT_VERIFIED" if all((checks["primitive_runtime_hashes"], checks["expression_executable"], checks["basis_hashes_present"], checks["entry_ancestry_count_match"], checks["matrix_free_zero_residual"], checks["poisoning_pass"])) else "C53_IMPORT_MISMATCH_BLOCKING",
            "records": records, "checks": checks, "no_c53_builder_called": True,
            "no_rescale_or_color_reconstruction": True}


def input_fidelity_audit() -> dict[str, Any]:
    """Classify the exact inputs before any local matrix is allowed."""
    term_ledger = _read("c43_hamiltonian_term_ledger.json")["terms"]
    c43_projection = _read("c43_finite_basis_projection_contract.json")
    rows = [
        {"id": "C43_ACTION", "classification": "SOURCE_DERIVED_SYMBOLIC", "evidence": "C43 Eq. action/constraints/term ledger"},
        {"id": "C45_MODES", "classification": "SOURCE_DERIVED_EXECUTABLE", "evidence": "normalized longitudinal, HO, spinor and polarization library"},
        {"id": "C47_BASIS_FREE", "classification": "SOURCE_DERIVED_FUNCTIONAL", "evidence": "CM-clean bases and invariant-mass functional"},
        {"id": "C47_PV_P0_Q0", "classification": "SOURCE_DERIVED_FUNCTIONAL", "evidence": "mode-index P0/Q0/d1/d2 arrays"},
        {"id": "C53_VERTEX", "classification": "SOURCE_DERIVED_EXECUTABLE", "evidence": "read-only runtime hashes and SymPy coefficient"},
        {"id": "C40", "classification": "METHOD_ORACLE_ONLY", "evidence": "explicitly forbidden from C54 construction"},
        {"id": "IFERM_FINITE_VOLUME_NORMAL_ORDERED_KERNEL", "classification": "ABSENT_BLOCKING", "evidence": "C43 interface is COMPLETE_INTERFACE_ONLY; no field-expanded, operator-ordered q/qg projection formula"},
        {"id": "ICURRENT_FINITE_VOLUME_NORMAL_ORDERED_KERNEL", "classification": "ABSENT_BLOCKING", "evidence": "same absent q/qg current-current contraction and color/CM matrix-element contract"},
    ]
    projected = {row["operator"]: row["C43_array"] for row in c43_projection["interfaces"]}
    return {"status": STATUS, "inputs": rows, "c43_terms": term_ledger, "c43_projection_interfaces": projected,
            "all_positive_inputs_usable": False, "first_blocker": BLOCKER,
            "C40_consumed": False, "C47_raw_tuples_consumed": False, "C50_combined_values_consumed": False}


def local_term_crosswalk() -> list[dict[str, Any]]:
    return [
        {"C43_term_ID": "free_q/free_qg", "scope": "O(g_s^0)", "C47_input": "free_functional", "C54_block": "not assembled after earliest blocker", "coupling_order": 0, "source_status": "SOURCE_DERIVED_FUNCTIONAL", "projection_status": "DEFERRED_AFTER_EARLIEST_REQUIRED_BLOCKER", "identity_role": "propagating"},
        {"C43_term_ID": "canonical_qg", "scope": "O(g_s^1)", "C47_input": "physical basis", "C54_block": "C53 imported read-only only", "coupling_order": 1, "source_status": "SOURCE_DERIVED_EXECUTABLE", "projection_status": "READ_ONLY_VERIFIED", "identity_role": "canonical"},
        {"C43_term_ID": "instantaneous_fermion", "scope": "REQUIRED_AT_O_G2", "C47_input": "PV/Q0 functional", "C54_block": "none", "coupling_order": 2, "source_status": "ABSENT_BLOCKING", "projection_status": "NO_FINITE_VOLUME_NORMAL_ORDERED_MATRIX_ELEMENT", "identity_role": "required partner"},
        {"C43_term_ID": "instantaneous_current", "scope": "REQUIRED_AT_O_G2", "C47_input": "PV/Q0 functional", "C54_block": "none", "coupling_order": 2, "source_status": "ABSENT_BLOCKING", "projection_status": "NO_FINITE_VOLUME_CURRENT_CONTRACTION", "identity_role": "required partner"},
        {"C43_term_ID": "three_gluon", "scope": "OUTSIDE_SCOPE_BUT_RETAINED", "C47_input": "none", "C54_block": "none", "coupling_order": 1, "source_status": "SOURCE_DERIVED_SYMBOLIC", "projection_status": "NO_OPERATOR_ORDERING_SCOPE_PROOF", "identity_role": "unresolved scope"},
        {"C43_term_ID": "four_gluon", "scope": "OUTSIDE_SCOPE_BUT_RETAINED", "C47_input": "none", "C54_block": "none", "coupling_order": 2, "source_status": "SOURCE_DERIVED_SYMBOLIC", "projection_status": "NO_OPERATOR_ORDERING_SCOPE_PROOF", "identity_role": "unresolved scope"},
        {"C43_term_ID": "boundary_zero_mode", "scope": "local action", "C47_input": "boundary_zero_mode_functional", "C54_block": "none", "coupling_order": 2, "source_status": "SOURCE_DERIVED_FUNCTIONAL", "projection_status": "DEFERRED_AFTER_EARLIEST_REQUIRED_BLOCKER", "identity_role": "required partner"},
    ]


@lru_cache(maxsize=1)
def local_projection_preflight() -> dict[str, Any]:
    imported = c53_read_only_import(); audit = input_fidelity_audit(); crosswalk = local_term_crosswalk()
    blockers = [x for x in audit["inputs"] if x["classification"] == "ABSENT_BLOCKING"]
    return {"status": STATUS, "baseline": BASELINE, "next": NEXT, "c53_import": imported,
            "input_audit": audit, "crosswalk": crosswalk, "blockers": blockers,
            "no_C54_local_matrices_created": True, "no_c53_recomputation": True,
            "no_free_or_g2_block_assembly_after_earliest_required_blocker": True,
            "projected_identity": "UNDEFINED: C43 term ledger is not a projected action/current identity and required O(g_s^2) matrices are absent",
            "positive_gate": False}


def static_isolation_guard() -> dict[str, Any]:
    tree = ast.parse(inspect.getsource(local_projection_preflight))
    names = {x.id for x in ast.walk(tree) if isinstance(x, ast.Name)} | {x.attr for x in ast.walk(tree) if isinstance(x, ast.Attribute)}
    forbidden = ("canonical_kernel", "evaluate_canonical_vertex", "m0b", "C40", "assemble_physical_vertex")
    found = tuple(x for x in forbidden if x in names)
    return {"guard": "C54_AUDIT_ISOLATION", "forbidden": forbidden, "found": found, "pass": not found}


def validate_c54(value: dict[str, Any]) -> bool:
    return canonical_json(value) == canonical_json(local_projection_preflight()) and value["status"] == STATUS


def mutate_live_c54(fault_id: int) -> dict[str, Any]:
    """Alter a concrete audited tensor/functional/hash/count field, never an ID alone."""
    value = deepcopy(local_projection_preflight()); choice = fault_id % 16
    if choice == 0: value["c53_import"]["records"][fault_id % len(value["c53_import"]["records"])]["observed_hash"] = "0" * 64
    elif choice == 1: value["c53_import"]["checks"]["expression_executable"] = False
    elif choice == 2: value["c53_import"]["checks"]["matrix_free_zero_residual"] = False
    elif choice == 3: value["c53_import"]["checks"]["poisoning_pass"] = False
    elif choice == 4: value["input_audit"]["inputs"][1]["classification"] = "METHOD_ORACLE_ONLY"
    elif choice == 5: value["input_audit"]["inputs"][3]["evidence"] = "wrong inverse derivative"
    elif choice == 6: value["input_audit"]["inputs"][6]["classification"] = "SOURCE_DERIVED_EXECUTABLE"
    elif choice == 7: value["crosswalk"][2]["projection_status"] = "FABRICATED_STENCIL"
    elif choice == 8: value["crosswalk"][3]["projection_status"] = "DROPPED_FOR_FOCK_SCOPE"
    elif choice == 9: value["crosswalk"][6]["projection_status"] = "SILENT_ZERO"
    elif choice == 10: value["blockers"][0]["id"] = "REMOVED"
    elif choice == 11: value["no_C54_local_matrices_created"] = False
    elif choice == 12: value["no_c53_recomputation"] = False
    elif choice == 13: value["projected_identity"] = "tuned closure"
    elif choice == 14: value["positive_gate"] = True
    else: value["next"] = "C55/WX"
    return value


def assert_fail_closed_c54() -> dict[str, Any]:
    value = local_projection_preflight()
    assert value["c53_import"]["status"] == "C53_READ_ONLY_IMPORT_VERIFIED"
    assert value["blockers"][0]["id"] == "IFERM_FINITE_VOLUME_NORMAL_ORDERED_KERNEL"
    assert value["status"] == STATUS and not value["positive_gate"]
    assert static_isolation_guard()["pass"]
    return value
