"""C405 current-normalization and finite-cell closure audit.

C114 and C119 publish exact symbolic ingredients, but do not publish the
product-specific normal-ordering descendant or the multiplicity/ownership by
which field and external-state normalization factors enter each retained
matrix element.  Literal C119 current expressions already contain factors of
``(2L)^-1`` and the gluon-current expression already contains ``pi*k_c/L``.
Historical C126 then references only one current per product and may add a
separate derivative factor.  C405 therefore records a literal scale ledger and
refuses to evaluate a complete numerical prefactor.
"""
from __future__ import annotations

from typing import Any, Mapping, Sequence

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root
from deuteron_wigner.bridge.icurrent import core as c114
from deuteron_wigner.bridge.icnorm3 import core as c119

from .derivative_order import _normalize_legs
from .topology import PRODUCTS, STATUS, current_pair_grammar, product_structure


def _add_exponents(*rows: Mapping[str, int]) -> dict[str, int]:
    result = {"L": 0, "pi": 0, "K": 0}
    for row in rows:
        for key in result:
            result[key] += int(row.get(key, 0))
    return result


def literal_source_scale_ledger(product: str) -> Mapping[str, Any]:
    """Compile powers present in the literal C114/C119 expressions.

    The ledger includes the C114 x-minus integration measure and the M2
    conversion.  It does not infer any field/state multiplicity or identify a
    normal-ordered matrix element.  Dimensionless mode labels are retained in
    a separate text field.
    """
    structure = product_structure(product)
    current_exponents = {
        "quark_current": {"L": -1, "pi": 0, "K": 0},
        "gluon_current": {"L": -2, "pi": 1, "K": 0},
    }
    factors = (
        {"id": "C114_Q0_inverse", "exponents": {"L": 2, "pi": -2, "K": 0}},
        {"id": "C114_xminus_measure", "exponents": {"L": 1, "pi": 0, "K": 0}},
        *tuple(
            {
                "id": f"C119_{side}_{current}",
                "exponents": current_exponents[current],
            }
            for side, current in zip(("left", "right"), structure.currents)
        ),
        {"id": "C114_M2_conversion", "exponents": {"L": -1, "pi": 1, "K": 1}},
    )
    known = _add_exponents(*(row["exponents"] for row in factors))
    required = {key: -value for key, value in known.items()}
    payload = {
        "schema": "C405-C117-I2-LITERAL-SOURCE-SCALE-LEDGER-V1",
        "status": STATUS,
        "product": product,
        "currents": structure.currents,
        "literal_factors": factors,
        "known_post_exponents": known,
        "correction_required_for_historical_C126_zero_exponent_claim": required,
        "dimensionless_mode_factor": (
            "one k_c per gluon current in the literal C119 expression"
        ),
        "field_state_normalization_multiplicity_applied": False,
        "normal_ordering_measure_applied": False,
        "numerical_prefactor_ready": False,
        "classification": "LITERAL_SOURCE_EXPRESSION_LEDGER_NOT_NORMALIZATION_AUTHORITY",
    }
    return {**payload, "root": content_root(payload)}


def symbolic_prefactor_program(
    product: str,
    derivative_legs: Sequence[str],
) -> Mapping[str, Any]:
    structure = product_structure(product)
    legs = _normalize_legs(product, derivative_legs)
    current_expressions = tuple(
        c119.factor_value(current, "RouteA_source_field_insertion")["expression"]
        for current in structure.currents
    )
    unresolved = (
        f"NORMAL_ORDERING_DESCENDANT[{product}]",
        f"SOURCE_PHASE_AND_CONTRACTION_SIGN[{product}]",
        f"FIELD_NORMALIZATION_OWNERSHIP_AND_MULTIPLICITY[{product}]",
        f"EXTERNAL_STATE_NORMALIZATION_OWNERSHIP_AND_MULTIPLICITY[{product}]",
        f"FINITE_CELL_INTEGRATION_CONTRACTION_MULTIPLICITY[{product}]",
        f"TARGET_COUNT_ONCE_MULTIPLICITY[{product}]",
        f"Q_SECTOR_CONTRACTION_BRANCH[{product}]",
    )
    current_slots = tuple(
        (
            f"{side.upper()}_{current.upper()}"
            + ("[ORDERED_DERIVATIVE_MODE_FACTOR_EXTRACTED_ONCE]" if current == "gluon_current" else "")
        )
        for side, current in zip(("left", "right"), structure.currents)
    )
    program = (
        "AUDIT_ONLY_UNRESOLVED_MULTIPLY("
        "C114_SOURCE_COEFFICIENT[-1/2], "
        "C114_Q0_INVERSE[(L/pi)^2/n^2], "
        f"{current_slots[0]}, {current_slots[1]}, "
        f"ORDERED_GLUON_DERIVATIVE_C_FIELD_ASSIGNMENTS[{','.join(legs) if legs else 'NONE'}], "
        "RECONCILE_CURRENT_INTERNAL_NORMALIZATION_WITH_C119_FIELD_AND_STATE_FACTORS, "
        "NORMAL_ORDERING_DESCENDANT, SOURCE_PHASE, FINITE_CELL_CONTRACTION, TARGET_COUNT_ONCE, "
        "C114_M2_CONVERSION[2*pi*K/L], symbolic_g_s_squared, symbolic_c_C117_1)"
    )
    payload = {
        "schema": "C405-C117-I2-SYMBOLIC-PREFACTOR-PROGRAM-V2",
        "status": STATUS,
        "product": product,
        "currents": structure.currents,
        "gluon_current_count": structure.gluon_current_count,
        "explicit_derivative_legs": legs,
        "source_coefficient": c114.current_operator_identity()["coefficient"],
        "inverse_partial_plus_squared": c114.inverse_partial_plus_squared()["route_a"]["denominator"],
        "current_expressions_literal_source_evidence_only": current_expressions,
        "current_slots_with_derivative_extracted_once": current_slots,
        "ordered_derivative_factor_count": structure.gluon_current_count,
        "derivative_factor_double_count_forbidden": True,
        "Pminus_to_M2": c114.pminus_to_m2_manifest()["relation"],
        "program": program,
        "literal_scale_ledger": literal_source_scale_ledger(product),
        "unresolved_symbols": unresolved,
        "numerically_evaluable": False,
        "classification": "COMPLETE_SYMBOLIC_REQUIREMENT_PROGRAM_NUMERICAL_NORMALIZATION_UNAVAILABLE",
        "complete_C117_action": False,
    }
    return {**payload, "root": content_root(payload)}


def normalization_closure_audit() -> Mapping[str, Any]:
    grammar = current_pair_grammar()
    rows = []
    for product in PRODUCTS:
        structure = product_structure(product)
        representative: Mapping[str, Any]
        if structure.gluon_current_count == 0:
            representative = symbolic_prefactor_program(product, ())
        else:
            representative = {
                "program": "ONE_PROGRAM_PER_EXPLICIT_DERIVATIVE_ASSIGNMENT",
                "derivative_assignments_owned_by": "C405 ordered_derivative_inventory",
            }
        rows.append(
            {
                "product": product,
                "currents": structure.currents,
                "literal_scale_ledger": literal_source_scale_ledger(product),
                "C114_source_coefficient_bound": True,
                "C114_Q0_inverse_bound": True,
                "C114_xminus_measure_identified": True,
                "C119_left_and_right_current_identities_bound": True,
                "C119_current_expressions_symbolic": True,
                "C114_M2_relation_bound_symbolically": True,
                "normal_ordering_descendant_bound": False,
                "current_internal_vs_field_normalization_ownership_reconciled": False,
                "state_normalization_multiplicity_bound": False,
                "ordered_gluon_derivative_leg_bound": structure.gluon_current_count == 0,
                "source_phase_bound": False,
                "C125_witness_count_once_identity_bound": True,
                "C405_conditional_kernel_to_C125_witness_map_bound": False,
                "target_aggregation_multiplicity_bound": False,
                "q_sector_contraction_branch_bound": False,
                "numerical_prefactor_ready": False,
                "representative_program": representative,
            }
        )
    payload = {
        "schema": "C405-C117-I2-NORMALIZATION-CLOSURE-AUDIT-V2",
        "status": STATUS,
        "rows": tuple(rows),
        "current_pair_grammar_root": grammar["root"],
        "C114_field_state_status": c114.field_state_normalization_manifest()["current_products"],
        "C114_M2_status": c114.pminus_to_m2_manifest()["status"],
        "C119_scale_contract": c119.factor_bound_contract(),
        "historical_derivative_factor_conflict": {
            "C119_gluon_current_already_contains_pi_kc_over_L": True,
            "C119_gluon_leaf_program_also_lists_derivative_or_helicity": True,
            "C126_adds_separate_derivative_for_left_gluon_products": True,
            "C250_uses_two_current_factors_without_extra_derivative": True,
            "classification": "HISTORICAL_FACTOR_ASSIGNMENT_CONFLICT_NOT_NUMERICAL_AUTHORITY",
        },
        "historical_C126_scale_claim": {
            "claimed_post_exponents": {"L": 0, "P_plus": 0, "pi": 0, "K": 0},
            "numerical_sparse_entries": 0,
            "numerical_matrix_free_actions": 0,
            "classification": "SYMBOLIC_ASSERTION_NOT_NUMERICALLY_VERIFIED_NORMALIZATION",
        },
        "literal_known_exponents_are_product_dependent": True,
        "complete_numeric_prefactors": 0,
        "no_default_normalization": True,
        "complete_C117_action": False,
        "smallest_missing_normalization_object": (
            "product-specific normal-ordering descendant with exact field/state normalization ownership and "
            "multiplicities, source phase, ordered gluon c-field leg, finite-cell integration/contraction factors, "
            "C405-to-C125 witness mapping, and target aggregation multiplicity"
        ),
    }
    return {**payload, "root": content_root(payload)}


def evaluate_complete_prefactor(*_args: Any, **_kwargs: Any) -> complex:
    raise RuntimeError(
        "C405 cannot evaluate a complete C117 prefactor: product-specific normal-ordering and finite-cell/state normalization ownership are unavailable"
    )


__all__ = [
    "literal_source_scale_ledger",
    "symbolic_prefactor_program",
    "normalization_closure_audit",
    "evaluate_complete_prefactor",
]
