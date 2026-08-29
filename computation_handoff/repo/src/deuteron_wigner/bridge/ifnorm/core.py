"""Fail closed when BPP's DLCQ contraction has no C45 finite-HO owner.

C55 proved that the ``b† a a† b`` monomial has a required one-pair
commutator.  It did not authorize a number for that commutator.  This module
audits the missing regulator bridge before any virtual gluon mode is summed.
In particular, C45's useful HO *basis functions* and C47's external qg
truncation are not silently promoted to a field-level normal-ordering
projector.  Therefore no contraction matrix, counterterm coefficient, or
matrix-free numerical action is made here.
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

from ..iferm.core import (
    BASELINE as C55_BASELINE,
    BPP_W3,
    SB_W3,
    instantaneous_fermion_preflight,
)

ROOT = Path(__file__).resolve().parents[4]
BASELINE = "12796e04f81158bc90da96cb27d29b33eea6e08e"
STATUS = "C56_IFNORM_FINITE_HO_REGULATOR_INCOMPLETE"
NEXT = "C57/IFREG — contracted field-mode collection, truncation projector, and shell regulator completion"
BLOCKER = "C56.IFNORM.FINITE_HO_CONTRACTION_REGULATOR_OWNERSHIP"
PLAN = "IFNORM-UNAVAILABLE"
MONOMIAL = ("b_dagger", "a", "a_dagger", "b")


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def _read(name: str) -> dict[str, Any]:
    return json.loads((ROOT / "docs" / "next_level" / name).read_text())


def _sha(value: Any) -> str:
    return sha256(canonical_json(value).encode()).hexdigest()


def c55_contraction_identity() -> dict[str, Any]:
    """Recover the immutable one-pair row from C55, without a mode sum."""
    c55 = instantaneous_fermion_preflight()
    rows = [row for row in c55["ledger"] if tuple(row["operator_order"]) == MONOMIAL]
    assert len(rows) == 1
    row = rows[0]
    assert row["status"] == "NORMAL_ORDER_CONTRACTION_RETAINED"
    return {
        "c55_monomial_ancestry": "c55_operator_monomial_ledger row b_dagger,a,a_dagger,b",
        "field_ordering": list(MONOMIAL),
        "normal_ordering_reduction": "a_nu a_dagger_nuprime = a_dagger_nuprime a_nu + [a_nu,a_dagger_nuprime]",
        "commutator": "[a_(k,n,m,h,a),a_dagger_(kprime,nprime,mprime,hprime,aprime)] = delta_kkprime delta_nnprime delta_mmprime delta_hhprime delta_aa_prime on the declared finite-cell mode algebra",
        "fermion_bilinear": "b_dagger b",
        "inverse_derivative_placement": "(i partial^+)^-1 acts on the complete right A psi product before the left field contracts",
        "inverse_derivative_routing": row["routing"],
        "ordered_color": row["color_order"],
        "polarization_ordering": "left A_mu then right A_nu; sum may occur only after the ordered contraction",
        "coupling_power": 2,
        "mass_dimension": "P^- before 2 P^+ conversion; unresolved because regulator-mode functional is absent",
        "status": "SOURCE_DERIVED_SYMBOLIC_RETAINED",
        "hash": _sha(row),
    }


def normal_ordering_reference() -> dict[str, Any]:
    return {
        "vacuum_identity": "perturbative light-front Fock vacuum used by BPP normal ordering",
        "annihilation_conditions": "a_nu|0_LF>=b_alpha|0_LF>=d_alpha|0_LF>=0 for positive-p^+ APBC/PBC dynamical modes",
        "commutator_normalization": "finite-cell orthonormal mode delta, inherited from C45 phi_k=exp(i pi k x^-/L)/sqrt(2L)",
        "zero_mode_control": "ordinary gluon k^+=0 is P0-projected out; inverse partial^+ is PV/antisymmetric on Q0; constrained/residual sectors stay distinct",
        "boundary_conditions": "quarks APBC; gluons PBC; cell -L<=x^-<=L; L symbolic",
        "constrained_zero_modes_in_vacuum_algebra": "NO: retained as declared C43 constrained/residual controls, not silently contracted",
        "not_the_vacuum": ["B=0 soft vacuum root", "open-color one-quark matching module", "C47 physical qg basis", "C11 proton", "ART25 ensemble"],
        "status": "SOURCE_DERIVED_NORMAL_ORDER_REFERENCE",
    }


def regulator_plan_audit() -> dict[str, Any]:
    """Evaluate the five mutually exclusive C56 plans before summing a mode."""
    return {
        "selected_plan": PLAN,
        "selection_rule": "No virtual-gluon mode is summed before a field-level finite-HO regulator owner is source/project qualified.",
        "plans": [
            {
                "id": "IFNORM-PROJECTED-FIELD-MODE-REGULATOR",
                "status": "REJECTED_ABSENT_BLOCKING",
                "reason": "C45 defines normalized longitudinal modes, HO functions, and an Nmax basis rule, but no contracted-field projector P_HO^field or all-mode virtual-gluon collection for the BPP a a_dagger commutator. C47 projects external many-body states only.",
            },
            {
                "id": "IFNORM-EXTERNAL-QG-EMBEDDABLE-REGULATOR",
                "status": "REJECTED_NO_SOURCE_AUTHORITY",
                "reason": "Restricting a normal-order loop to gluons embeddable in an external qg state changes a one-body field contraction into an external-Fock-sector cutoff; no C43/C45/C47 contract proves that identification.",
            },
            {
                "id": "IFNORM-SOURCE-DEFINED-REFERENCE-SUBTRACTION",
                "status": "REJECTED_NO_REGULATOR_IDENTICAL_REFERENCE",
                "reason": "BPP permits careful regularization and discusses DLCQ self-induced inertias/counterterms, but specifies no C45-HO reference, mode pairing, subtraction constant, or counterterm relation.",
            },
            {
                "id": "IFNORM-REGULATOR-MATCHED-CONVERSION",
                "status": "REJECTED_NONIDENTICAL_REGULATORS",
                "reason": "BPP's displayed self-induced-inertia ledger is a DLCQ transverse-momentum sum with Omega and gbar^2=2g^2/(Omega P^+); C45 uses x-scaled two-dimensional HO functions and C47 CM/TM projection. No finite operator conversion, inverse, or remainder is locked.",
            },
            {
                "id": PLAN,
                "status": "SELECTED",
                "reason": "The required finite-HO field-level regulator ownership is absent; selecting any positive plan would fabricate the virtual mode domain.",
            },
        ],
        "first_blocker": BLOCKER,
        "status": STATUS,
    }


def input_fidelity_audit() -> dict[str, Any]:
    rows = [
        {"input": "C55 locked SB/BPP W3 and 16-row monomial ledger", "classification": "PRIMARY_SOURCE_DERIVED_SYMBOLIC", "status": "PASS"},
        {"input": "BPP Sec.2 normal ordering and Sec.DLCQ contraction table", "classification": "PRIMARY_SOURCE_DERIVED_DLCQ_CONTRACTION_METHOD", "status": "NONIDENTICAL_TO_C45_HO"},
        {"input": "C45 finite longitudinal cell/PBC nonzero gluons", "classification": "PROJECT_SOURCE_DERIVED_MODE_LIBRARY", "status": "EXECUTABLE_BUT_NOT_CONTRACTION_REGULATOR_OWNER"},
        {"input": "C45 transverse HO functions/Nmax rule", "classification": "PROJECT_SOURCE_DERIVED_BASIS_FUNCTIONS", "status": "EXECUTABLE_BUT_NO_FIELD_MODE_PROJECTOR"},
        {"input": "C47 CM-clean q/qg bases, TM map, Q0", "classification": "PROJECT_SOURCE_DERIVED_EXTERNAL_PROJECTION", "status": "EXECUTABLE_BUT_NOT_VIRTUAL_CONTRACTION_DOMAIN"},
        {"input": "C53 triplet convention", "classification": "READ_ONLY_COLOR_IDENTITY", "status": "NOT_A_CONTRACTION_VALUE"},
        {"input": "finite-HO P_HO^field, complete virtual one-gluon set, shell policy", "classification": "ABSENT_BLOCKING", "status": BLOCKER},
        {"input": "C40 instantaneous values; C47 canonical tuples; C50 combined values; C53 vertex values; C8/C9 coefficients; ART25", "classification": "FORBIDDEN", "status": "NOT_CONSUMED"},
    ]
    return {"status": STATUS, "rows": rows, "first_blocker": BLOCKER, "raw_C47_tuple_values_consumed": False, "C53_vertex_values_consumed": False, "C40_consumed": False, "C50_combined_values_consumed": False, "historical_mass_coefficients_consumed": False, "ART25_consumed": False}


def count_once() -> dict[str, Any]:
    return {
        "direct_normal_ordered_qg_contact": "C55 W3 b_dagger a_dagger a b; not constructed in C56",
        "self_induced_inertia_contraction": "C55 b_dagger a a_dagger b commutator; retained but unsummed due to regulator ownership blocker",
        "C53_sequential_propagation": "forbidden substitute; not consumed",
        "free_mass_direction": "distinct future diagnostic direction; no coefficient",
        "local_counterterm_direction": "not constructed before bare contraction exists",
        "boundary_zero_mode": "separate C43/C45 Q0/P0/residual controls",
        "instantaneous_current_and_future_loop": "outside C56 and distinct",
        "double_count": False,
    }


def blocked_artifact(reason: str = BLOCKER) -> dict[str, Any]:
    return {"status": "NOT_EVALUATED_AFTER_FINITE_HO_REGULATOR_BLOCKER", "reason": reason, "matrix_created": False, "mode_sum_created": False, "counterterm_coefficient_solved": False}


@lru_cache(maxsize=1)
def contraction_preflight() -> dict[str, Any]:
    c55 = instantaneous_fermion_preflight()
    identity = c55_contraction_identity()
    return {
        "baseline": BASELINE,
        "c55_baseline_status": c55["status"],
        "status": STATUS,
        "next": NEXT,
        "blocker": BLOCKER,
        "source_operator": {"SB_W3": SB_W3, "BPP_W3": BPP_W3, "symbolic_residual": c55["source"]["symbolic_residual"]},
        "contraction_identity": identity,
        "normal_ordering_reference": normal_ordering_reference(),
        "regulator_plan": regulator_plan_audit(),
        "input_audit": input_fidelity_audit(),
        "count_once": count_once(),
        "preserved_exact_zeros": {"q_to_qg": "EXACT_ZERO_BY_GLUON_NUMBER_PARITY", "qg_to_q": "EXACT_ZERO_BY_GLUON_NUMBER_PARITY"},
        "no_mode_sum": True,
        "no_contraction_matrix": True,
        "no_counterterm_typing_before_bare_operator": True,
        "no_C53_propagation": True,
        "no_complete_direct_contact": True,
        "positive_gate": False,
    }


def static_isolation_guard() -> dict[str, Any]:
    tree = ast.parse(inspect.getsource(contraction_preflight) + inspect.getsource(input_fidelity_audit))
    names = {x.id for x in ast.walk(tree) if isinstance(x, ast.Name)} | {x.attr for x in ast.walk(tree) if isinstance(x, ast.Attribute)}
    forbidden = ("canonical_kernel", "evaluate_canonical_vertex", "assemble_physical_vertex", "m0b", "C40", "ART25", "raw_tuple")
    found = tuple(x for x in forbidden if x in names)
    return {"guard": "C56_IFNORM_ISOLATION", "forbidden": forbidden, "found": found, "pass": not found}


def validate_c56(value: dict[str, Any]) -> bool:
    expected = contraction_preflight()
    return canonical_json(value) == canonical_json(expected) and value["status"] == STATUS


def mutate_live_c56(fault_id: int) -> dict[str, Any]:
    """224 live mutations of a real source/contract field, each fail-closed validation."""
    value = deepcopy(contraction_preflight())
    choice = fault_id % 28
    if choice == 0: value["source_operator"]["SB_W3"] = "wrong sign"
    elif choice == 1: value["source_operator"]["symbolic_residual"] = "Integer(1)"
    elif choice == 2: value["contraction_identity"]["field_ordering"][1] = "a_dagger"
    elif choice == 3: value["contraction_identity"]["normal_ordering_reduction"] = "commutator dropped"
    elif choice == 4: value["contraction_identity"]["inverse_derivative_routing"] = "p_q"
    elif choice == 5: value["normal_ordering_reference"]["vacuum_identity"] = "proton expectation value"
    elif choice == 6: value["normal_ordering_reference"]["zero_mode_control"] = "epsilon clipping"
    elif choice == 7: value["regulator_plan"]["selected_plan"] = "IFNORM-EXTERNAL-QG-EMBEDDABLE-REGULATOR"
    elif choice == 8: value["regulator_plan"]["plans"][0]["status"] = "SELECTED"
    elif choice == 9: value["regulator_plan"]["plans"][1]["reason"] = "convenience"
    elif choice == 10: value["regulator_plan"]["plans"][2]["status"] = "SELECTED"
    elif choice == 11: value["regulator_plan"]["plans"][3]["reason"] = "continuum finite part"
    elif choice == 12: value["input_audit"]["rows"][1]["status"] = "REGULATOR_IDENTICAL"
    elif choice == 13: value["input_audit"]["rows"][2]["status"] = "CONTRACTION_OWNER"
    elif choice == 14: value["input_audit"]["rows"][3]["status"] = "FIELD_PROJECTOR_PRESENT"
    elif choice == 15: value["input_audit"]["rows"][4]["status"] = "VIRTUAL_DOMAIN_OWNER"
    elif choice == 16: value["input_audit"]["rows"][5]["status"] = "VERTEX_VALUE_CONSUMED"
    elif choice == 17: value["input_audit"]["rows"][6]["classification"] = "SOURCE_COMPLETE"
    elif choice == 18: value["input_audit"]["C40_consumed"] = True
    elif choice == 19: value["input_audit"]["raw_C47_tuple_values_consumed"] = True
    elif choice == 20: value["input_audit"]["C53_vertex_values_consumed"] = True
    elif choice == 21: value["count_once"]["self_induced_inertia_contraction"] = value["count_once"]["C53_sequential_propagation"]
    elif choice == 22: value["count_once"]["double_count"] = True
    elif choice == 23: value["preserved_exact_zeros"]["q_to_qg"] = "NONZERO"
    elif choice == 24: value["no_mode_sum"] = False
    elif choice == 25: value["no_contraction_matrix"] = False
    elif choice == 26: value["no_counterterm_typing_before_bare_operator"] = False
    else: value["next"] = "C57/IFERM2"
    return value


def assert_fail_closed_c56() -> dict[str, Any]:
    value = contraction_preflight()
    assert value["baseline"] == BASELINE and value["c55_baseline_status"] == "C55_IFERM_NORMAL_ORDERING_CONTRACT_INCOMPLETE"
    assert value["source_operator"]["symbolic_residual"] == "Integer(0)"
    assert value["contraction_identity"]["field_ordering"] == list(MONOMIAL)
    assert value["regulator_plan"]["selected_plan"] == PLAN
    assert all(row["status"] != "SELECTED" for row in value["regulator_plan"]["plans"][:-1])
    assert value["input_audit"]["rows"][6]["status"] == BLOCKER
    assert value["no_mode_sum"] and value["no_contraction_matrix"] and not value["positive_gate"]
    assert value["preserved_exact_zeros"]["q_to_qg"] == "EXACT_ZERO_BY_GLUON_NUMBER_PARITY"
    assert static_isolation_guard()["pass"]
    return value
