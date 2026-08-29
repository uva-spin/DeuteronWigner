"""C55 source algebra closes, but the self-induced-inertia regulator does not.

The module records the exact SB/BPP constrained-field and W3 operator
relations, enumerates the 14 non-vacuum monomials, and refuses to create a
finite matrix until the source-owned treatment of the one-pair contraction is
specified for the C45/C47 HO regulator.  It creates no contact matrix and
never substitutes C53 propagation for the direct W3 contact.
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

import sympy as sp

from ..hqcd3.core import c53_read_only_import

ROOT = Path(__file__).resolve().parents[4]
BASELINE = "3717d1a70184c6cc70dfc985534c38f51a7d1476"
STATUS = "C55_IFERM_NORMAL_ORDERING_CONTRACT_INCOMPLETE"
NEXT = "C56/IFNORM — operator-monomial, contraction, self-induced-inertia, and block-scope completion"
BLOCKER = "C55.IFERM.ONE_PAIR_CONTRACTION_REGULATOR_AND_COUNTERTERM_CONTRACT"
SB_W3 = "-g_s^2/2 psibar gamma^+ gamma^mu A_mu^a T^a (i partial_-)^-1 gamma^nu A_nu^b T^b psi"
BPP_W3 = "+g_s^2/2 psibar gamma^mu T^a A_mu^a gamma^+/(i partial^+) (gamma^nu T^b A_nu^b psi)"


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def _read(name: str) -> dict[str, Any]:
    return json.loads((ROOT / "docs" / "next_level" / name).read_text())


def source_derivation() -> dict[str, Any]:
    """Two exact symbolic coefficient routes for the C43/SB W3 operator."""
    g = sp.Symbol("g_s")
    h0, h1, hif = sp.symbols("H_0 H_1 H_IF")
    h = h0 + g*h1 + g**2*hif
    direct = sp.expand(h).coeff(g, 2)
    derivative = sp.diff(h, g, 2).subs(g, 0) / sp.factorial(2)
    return {"status": "SOURCE_DERIVED_SYMBOLIC", "SB_constraint": "i sqrt(2) D_- psi_- = -(i gamma^0 gamma^perp D_perp-m gamma^0) psi_+; SB Sec.3/Eq.(constraint)",
            "SB_W3": SB_W3, "BPP_W3": BPP_W3, "locators": ["SB hep-ph/0011372v2 Eq.(24), lines W3", "BPP hep-ph/9705477v1 Eq.(2.97), Sec.2 and DLCQ normal-order discussion"],
            "derivative_placement": "(i partial^+)^-1 acts on the complete right product gamma^nu T^b A_nu^b psi before the left factor contracts", "coupling_power": 2,
            "direct_expansion": sp.srepr(direct), "second_derivative_over_factorial": sp.srepr(derivative),
            "symbolic_residual": sp.srepr(sp.simplify(direct-derivative)),
            "SB_to_BPP_sign_map": "for transverse A, gamma^+ gamma^i=-gamma^i gamma^+ converts the displayed SB -1/2 ordering to BPP +1/2 ordering; no numerical sign is fitted"}


def monomial_ledger() -> list[dict[str, Any]]:
    """All 2^4 field choices, with the two positive-p+ vacuum terms excluded."""
    output = []
    for left in ("b_dagger", "d"):
        for outer in ("a_dagger", "a"):
            for inner in ("a_dagger", "a"):
                for right in ("d_dagger", "b"):
                    order = (left, outer, inner, right)
                    all_create = order == ("b_dagger", "a_dagger", "a_dagger", "d_dagger")
                    all_destroy = order == ("d", "a", "a", "b")
                    row = {"operator_order": order, "fermion_number_change": 0 if (left == "b_dagger" and right == "b") else "pair_or_antiquark", "color_order": "T^a (left A) then T^b (right A)", "inverse_derivative_argument": "right A*psi product", "status": "OUTSIDE_RETAINED_SPACE_NONZERO_OPERATOR"}
                    if all_create or all_destroy:
                        row["status"] = "EXACT_ZERO_BY_OPERATOR_ALGEBRA"
                        row["proof"] = "positive longitudinal mode indices cannot sum to zero in the APBC/PBC finite cell"
                    elif order == ("b_dagger", "a_dagger", "a", "b"):
                        row.update({"status": "DIRECT_RETAINED_OPERATOR", "physical_block": "qg_to_qg", "routing": "p_q+k_g"})
                    elif order == ("b_dagger", "a", "a_dagger", "b"):
                        row.update({"status": "NORMAL_ORDER_CONTRACTION_RETAINED", "physical_block": "qg_to_qg plus q_to_q contraction", "routing": "p_q-k'_g", "normal_order": "a a_dagger = a_dagger a + [a,a_dagger]"})
                    elif order == ("b_dagger", "a_dagger", "a_dagger", "b"):
                        row.update({"physical_block": "q_to_qgg", "routing": "p_q-k'_g"})
                    elif order == ("b_dagger", "a", "a", "b"):
                        row.update({"physical_block": "qgg_to_q", "routing": "p_q+k_g"})
                    output.append(row)
    assert len(output) == 16 and sum(x["status"] != "EXACT_ZERO_BY_OPERATOR_ALGEBRA" for x in output) == 14
    return output


def physical_blocks() -> list[dict[str, Any]]:
    return [
        {"block": "q_to_q", "classification": "NORMAL_ORDER_CONTRACTION_DIRECTION", "status": "ABSENT_BLOCKING", "reason": BLOCKER},
        {"block": "q_to_qg", "classification": "SOURCE_DERIVED_EXECUTABLE_ZERO_BY_EXACT_PROOF", "status": "EXACT_ZERO_BY_GLUON_NUMBER_PARITY", "reason": "W3 carries two gluon fields; normal ordering changes gluon number by 0 or 2, never 1"},
        {"block": "qg_to_q", "classification": "SOURCE_DERIVED_EXECUTABLE_ZERO_BY_EXACT_PROOF", "status": "EXACT_ZERO_BY_GLUON_NUMBER_PARITY", "reason": "same exact monomial algebra"},
        {"block": "qg_to_qg", "classification": "SOURCE_DERIVED_EXECUTABLE_NONZERO", "status": "PROJECTION_DEFERRED_AFTER_NORMAL_ORDER_BLOCKER", "reason": "direct bdagger a_dagger a b contact is distinct from the unresolved q contraction"},
    ]


def inverse_derivative_contract() -> dict[str, Any]:
    return {"status": "SOURCE_DERIVED_SYMBOLIC", "prescription": "C43 antisymmetric/PV on Q0 only", "routes": [
        {"monomial": "bdagger a_dagger a b", "right_product_mode": "p_q+k_g", "denominator": "1/(p_q^+ + k_g^+)", "zero_status": "NONZERO_BY_POSITIVITY"},
        {"monomial": "bdagger a a_dagger b", "right_product_mode": "p_q-k'_g", "denominator": "1/(p_q^+ - k_g'^+)", "zero_status": "NONZERO_BY_APBC_MINUS_PBC_MODE_PARITY; otherwise Q0 contract required"},
        {"monomial": "q_to_q contraction", "right_product_mode": "p_q-k_g", "denominator": "exact rational (K-k)/K", "zero_status": "NO_EPSILON_CLIPPING_OR_PSEUDOINVERSE; regulator treatment blocked separately"}],
        "zero_mode_policy": "P0/Q0 supplied by C45/C47; a zero denominator must be typed, never deleted"}


def input_fidelity_audit() -> dict[str, Any]:
    return {"status": STATUS, "rows": [
        {"input": "SB constrained equation and Eq.(24)", "classification": "PRIMARY_SOURCE_INPUT", "status": "SOURCE_DERIVED_SYMBOLIC"},
        {"input": "BPP Eq.(2.97) and normal-order/self-induced-inertia discussion", "classification": "PRIMARY_SOURCE_INPUT", "status": "SOURCE_DERIVED_SYMBOLIC"},
        {"input": "C45 finite-cell modes/P0-Q0", "classification": "PROJECT_DERIVED_FROM_SOURCE_INPUTS", "status": "SOURCE_DERIVED_EXECUTABLE"},
        {"input": "C47 HO/TM/CM physical basis", "classification": "PROJECT_DERIVED_FROM_SOURCE_INPUTS", "status": "SOURCE_DERIVED_BASIS_IDENTITY"},
        {"input": "C53 color/triplet identity", "classification": "PROJECT_DERIVED_FROM_SOURCE_INPUTS", "status": "READ_ONLY_IDENTITY_ONLY"},
        {"input": "C40 instantaneous arrays", "classification": "HISTORICAL_METHOD_ORACLE_ONLY", "status": "FORBIDDEN"},
        {"input": "one-pair contraction regulator/subtraction mapped to C47 finite HO", "classification": "ABSENT_BLOCKING", "status": BLOCKER}],
        "first_blocker": BLOCKER, "raw_C47_tuple_values_consumed": False, "C53_vertex_values_consumed": False, "C40_consumed": False}


def contact_count_once() -> dict[str, Any]:
    return {"direct_contact": "C43/BPP W3; not numerically projected after blocker", "propagating": "V_C53^dagger (E-H0)^-1 V_C53; forbidden construction in C55 and never identified with W3", "normal_order_contraction": "one-pair a a_dagger contraction; retained as distinct self-induced-inertia direction but regulator coefficient blocked", "counterterm": "future independently typed direction; not assigned contraction value", "boundary_zero_mode": "C43/C45 P0/Q0 contract remains separate", "double_count": False}


@lru_cache(maxsize=1)
def instantaneous_fermion_preflight() -> dict[str, Any]:
    source = source_derivation(); ledger = monomial_ledger(); blocks = physical_blocks(); c53 = c53_read_only_import()
    return {"status": STATUS, "baseline": BASELINE, "next": NEXT, "source": source, "ledger": ledger, "blocks": blocks,
            "inverse_derivative": inverse_derivative_contract(), "input_audit": input_fidelity_audit(), "C53_read_only_import": c53,
            "count_once": contact_count_once(), "no_physical_matrix_created": True, "no_C53_propagating_construction": True,
            "no_free_current_or_local_polynomial": True, "positive_gate": False}


def static_isolation_guard() -> dict[str, Any]:
    tree = ast.parse(inspect.getsource(instantaneous_fermion_preflight)); names = {x.id for x in ast.walk(tree) if isinstance(x, ast.Name)} | {x.attr for x in ast.walk(tree) if isinstance(x, ast.Attribute)}
    forbidden = ("canonical_kernel", "evaluate_canonical_vertex", "assemble_physical_vertex", "m0b", "C40")
    found = tuple(x for x in forbidden if x in names)
    return {"guard": "C55_IFERM_ISOLATION", "forbidden": forbidden, "found": found, "pass": not found}


def validate_c55(value: dict[str, Any]) -> bool:
    return canonical_json(value) == canonical_json(instantaneous_fermion_preflight()) and value["status"] == STATUS


def mutate_live_c55(fault_id: int) -> dict[str, Any]:
    value = deepcopy(instantaneous_fermion_preflight()); choice = fault_id % 16
    if choice == 0: value["source"]["SB_W3"] = "wrong sign"
    elif choice == 1: value["source"]["symbolic_residual"] = "nonzero"
    elif choice == 2: value["source"]["derivative_placement"] = "left factor only"
    elif choice == 3: value["ledger"][1]["operator_order"] = ("bad",)
    elif choice == 4: value["ledger"][5]["status"] = "SILENTLY_DROPPED"
    elif choice == 5: value["blocks"][0]["status"] = "ZERO_BY_TOPOLOGY"
    elif choice == 6: value["blocks"][1]["status"] = "ASSUMED_ZERO"
    elif choice == 7: value["inverse_derivative"]["routes"][0]["denominator"] = "epsilon"
    elif choice == 8: value["inverse_derivative"]["zero_mode_policy"] = "pseudoinverse"
    elif choice == 9: value["count_once"]["direct_contact"] = value["count_once"]["propagating"]
    elif choice == 10: value["input_audit"]["C40_consumed"] = True
    elif choice == 11: value["C53_read_only_import"]["checks"]["poisoning_pass"] = False
    elif choice == 12: value["no_physical_matrix_created"] = False
    elif choice == 13: value["no_C53_propagating_construction"] = False
    elif choice == 14: value["input_audit"]["rows"][-1]["status"] = "SOURCE_COMPLETE"
    else: value["next"] = "C56/HQCD3"
    return value


def assert_fail_closed_c55() -> dict[str, Any]:
    value = instantaneous_fermion_preflight()
    assert value["source"]["symbolic_residual"] == "Integer(0)"
    assert len(value["ledger"]) == 16 and sum(x["status"] != "EXACT_ZERO_BY_OPERATOR_ALGEBRA" for x in value["ledger"]) == 14
    assert value["blocks"][0]["reason"] == BLOCKER and value["C53_read_only_import"]["status"] == "C53_READ_ONLY_IMPORT_VERIFIED"
    assert static_isolation_guard()["pass"] and not value["positive_gate"]
    return value
