"""C406 source-qualified one-gluon normal-ordering descendant.

The authenticated C192 source current is

    J_g^{+a}(x) = -f^{abc} A_perp^b(x) partial^+ A_perp^c(x),

with the derivative on the second source-ordered field.  Expanding the real
transverse field in creation and annihilation modes and normal ordering the
number-preserving branch gives two terms.  In the C45 phase convention they
combine into

    i f^{abc} (k_out + k_in)
      = -(k_out + k_in) (F^a)_{bc},

where ``(F^a)_{bc}=-i f^{abc}``.  The bosonic commutator term vanishes exactly
because ``f^{abb}=0``.  This module binds that algebra and its source phase; it
does not claim a complete C117 Hamiltonian prefactor.
"""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from math import sqrt
from pathlib import Path
from typing import Any, Mapping, Sequence

import numpy as np

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root
from deuteron_wigner.bridge.c404_c117_i2_longitudinal_color_primitive.color_spin import (
    adjoint_generators,
)
from deuteron_wigner.bridge.c404_c117_i2_longitudinal_color_primitive.longitudinal import (
    partition_axis,
)
from deuteron_wigner.bridge.hqcdg2pt import core as c151
from deuteron_wigner.bridge.modes import core as c45

STATUS = (
    "C406_C117_I2_ONE_GLUON_NORMAL_ORDER_DESCENDANT_AND_MIXED_CURRENT_"
    "ROUTING_READY_SAME_SPECIES_CONTRACTIONS_UNRESOLVED"
)


def _positive_fraction(value: Fraction | int) -> Fraction:
    result = value if isinstance(value, Fraction) else Fraction(int(value), 1)
    if result <= 0:
        raise ValueError("positive nonzero gluon mode required")
    return result


def _exact(value: Fraction) -> Mapping[str, Any]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "exact": str(value),
        "float": float(value),
    }


ROOT = Path(__file__).resolve().parents[4]
_C192_SOURCE_PATH = "src/deuteron_wigner/bridge/hqcdb1qgggcurr1/core.py"


def source_authority_record() -> Mapping[str, Any]:
    source_path = ROOT / _C192_SOURCE_PATH
    text = source_path.read_text(encoding="utf-8")
    required = (
        '"current_expression":"- f_abc A_perp^b partial_- A_perp^c"',
        '"ordered_field_slots":("A_perp^b first","A_perp^c second")',
        '"derivative_placement":"partial_- acts on second slot"',
        '"pattern":"a†a"',
        '"derivative":"second-slot momentum factor"',
    )
    missing = tuple(snippet for snippet in required if snippet not in text)
    if missing:
        raise ValueError("C192 source surface changed: " + ", ".join(missing))
    c45_contract = c45.longitudinal_contract()
    c151_convention = c151.gluon_convention_ledger()
    payload = {
        "schema": "C406-C117-I2-GLUON-NORMAL-ORDER-SOURCE-AUTHORITY-V1",
        "status": STATUS,
        "C192_source_path": _C192_SOURCE_PATH,
        "C192_source_sha256": sha256(source_path.read_bytes()).hexdigest(),
        "source_expression": "- f_abc A_perp^b partial_- A_perp^c",
        "ordered_field_slots": ("A_perp^b first", "A_perp^c second"),
        "derivative_placement": "partial_- acts on second slot",
        "source_sign": "source minus retained",
        "color_index_order": "f_abc, current a then field slots b,c",
        "number_preserving_branch": {
            "pattern": "a†a",
            "derivative": "second-slot momentum factor",
            "normal_order": "source order followed by bosonic commutator",
        },
        "C45_longitudinal_mode": c45_contract["mode"],
        "C45_momentum": c45_contract["momenta"],
        "C151_commutator": c151_convention["commutator"],
        "C151_source_mode": c151_convention["source_mode"],
        "field_phase_convention": "annihilation exp(-i*pi*k*xminus/L), creation adjoint",
        "adjoint_generator_convention": "(F^a)_bc=-i f^{abc}",
        "complete_C117_action": False,
    }
    return {**payload, "root": content_root(payload)}


def normal_ordered_mode_terms(
    k_bra: Fraction | int,
    k_ket: Fraction | int,
) -> Mapping[str, Any]:
    """Return exact coefficients multiplying the Hermitian adjoint generator.

    Coefficients are dimensionless mode factors.  The common C45 current-density
    scale ``(pi/L)(2L)^-1`` and transverse/polarization overlap are factored.
    """
    bra = _positive_fraction(k_bra)
    ket = _positive_fraction(k_ket)
    first = -ket
    second = -bra
    total = first + second
    payload = {
        "schema": "C406-C117-I2-ONE-GLUON-NORMAL-ORDER-TERMS-V1",
        "status": STATUS,
        "k_bra": _exact(bra),
        "k_ket": _exact(ket),
        "creation_first_derivative_annihilation": {
            "operator": "a_b^dagger(k_bra) a_c(k_ket)",
            "coefficient_multiplying_Fa_bc": _exact(first),
            "origin": "source first field creation; differentiated second field annihilation",
        },
        "annihilation_first_derivative_creation_after_boson_reorder": {
            "operator": "a_b^dagger(k_bra) a_c(k_ket)",
            "coefficient_multiplying_Fa_bc": _exact(second),
            "origin": "source first field annihilation; differentiated second field creation; b<->c relabel",
        },
        "bosonic_commutator": {
            "color_factor": "f^{abc} delta_bc = f^{abb}",
            "coefficient": 0,
            "status": "EXACT_ZERO_BY_STRUCTURE_CONSTANT_ANTISYMMETRY",
        },
        "total_dimensionless_coefficient_multiplying_Fa_bc": _exact(total),
        "equivalent_source_color_form": "i f^{abc} (k_bra+k_ket)",
        "C45_common_scale_factored": "(pi/L)*(2L)^(-1)",
        "polarization_factor_factored": "delta_(lambda_bra,lambda_ket)",
        "source_phase_and_sign_bound": True,
        "field_state_normalization_fully_reconciled": False,
        "complete_current_prefactor": False,
    }
    return {**payload, "root": content_root(payload)}


def dimensionless_descendant_factor_exact(
    k_bra: Fraction | int,
    k_ket: Fraction | int,
) -> Fraction:
    bra = _positive_fraction(k_bra)
    ket = _positive_fraction(k_ket)
    return -(bra + ket)


def c151_canonical_one_gluon_factor(
    k_bra: Fraction | int,
    k_ket: Fraction | int,
) -> float:
    """Coefficient multiplying F^a with C151 (2p+)^-1/2 field factors.

    Since ``p^+=pi*k/L``, the box scale cancels and the result is
    ``-(k_out+k_in)/(2*sqrt(k_out*k_in))``.  This is a route-specific
    one-gluon current matrix element, not the full C117 product normalization.
    """
    bra = float(_positive_fraction(k_bra))
    ket = float(_positive_fraction(k_ket))
    return -(bra + ket) / (2.0 * sqrt(bra * ket))


def adjoint_color_current_matrix(
    generator_index: int,
    k_bra: Fraction | int,
    k_ket: Fraction | int,
    *,
    canonical_field_normalization: bool = False,
) -> np.ndarray:
    if not 0 <= int(generator_index) < 8:
        raise ValueError("generator_index must be in [0,7]")
    generators = adjoint_generators()
    factor = (
        c151_canonical_one_gluon_factor(k_bra, k_ket)
        if canonical_field_normalization
        else float(dimensionless_descendant_factor_exact(k_bra, k_ket))
    )
    return factor * generators[int(generator_index)]


def one_gluon_mode_color_matrix(
    resolution: str,
    generator_index: int,
    *,
    canonical_field_normalization: bool = False,
) -> np.ndarray:
    partitions = partition_axis(resolution)
    mode_matrix = np.asarray(
        [
            [
                c151_canonical_one_gluon_factor(bra.k_g, ket.k_g)
                if canonical_field_normalization
                else float(dimensionless_descendant_factor_exact(bra.k_g, ket.k_g))
                for ket in partitions
            ]
            for bra in partitions
        ],
        dtype=np.float64,
    )
    return np.kron(mode_matrix, adjoint_generators()[int(generator_index)])


@lru_cache(maxsize=1)
def one_gluon_descendant_inventory() -> Mapping[str, Any]:
    rows = []
    for resolution in ("K9", "K11", "K13"):
        partitions = partition_axis(resolution)
        for bra in partitions:
            for ket in partitions:
                record = normal_ordered_mode_terms(bra.k_g, ket.k_g)
                rows.append(
                    {
                        "resolution": resolution,
                        "bra_partition": bra.partition_id,
                        "ket_partition": ket.partition_id,
                        "k_bra": record["k_bra"],
                        "k_ket": record["k_ket"],
                        "dimensionless_F_coefficient": record[
                            "total_dimensionless_coefficient_multiplying_Fa_bc"
                        ],
                        "C151_canonical_factor": c151_canonical_one_gluon_factor(
                            bra.k_g, ket.k_g
                        ),
                        "vacuum_commutator_zero": True,
                    }
                )
    payload = {
        "schema": "C406-C117-I2-ONE-GLUON-DESCENDANT-INVENTORY-V1",
        "status": STATUS,
        "rows": tuple(rows),
        "row_count": len(rows),
        "expected_row_count": 4 * 4 + 5 * 5 + 6 * 6,
        "source_phase_and_sign_bound": True,
        "complete_product_normalization": False,
        "complete_C117_action": False,
    }
    return {**payload, "root": content_root(payload)}


@lru_cache(maxsize=1)
def normal_ordering_validation() -> Mapping[str, Any]:
    generators = adjoint_generators()
    maximum_generator_hermiticity = float(
        max(np.linalg.norm(matrix - matrix.conj().T) for matrix in generators)
    )
    maximum_mode_color_hermiticity = 0.0
    maximum_route_symmetry = 0.0
    vacuum_traces = []
    for a, generator in enumerate(generators):
        # F^a=-i f^a => f^abb=i F^a_bb, which vanishes because every adjoint
        # generator is traceless and the structure constants are antisymmetric.
        vacuum_traces.append(float(abs(1j * np.trace(generator))))
        for resolution in ("K9", "K11", "K13"):
            raw = one_gluon_mode_color_matrix(resolution, a)
            canonical = one_gluon_mode_color_matrix(
                resolution, a, canonical_field_normalization=True
            )
            maximum_mode_color_hermiticity = max(
                maximum_mode_color_hermiticity,
                float(np.linalg.norm(raw - raw.conj().T)),
                float(np.linalg.norm(canonical - canonical.conj().T)),
            )
            partitions = partition_axis(resolution)
            for bra in partitions:
                for ket in partitions:
                    maximum_route_symmetry = max(
                        maximum_route_symmetry,
                        abs(
                            c151_canonical_one_gluon_factor(bra.k_g, ket.k_g)
                            - c151_canonical_one_gluon_factor(ket.k_g, bra.k_g)
                        ),
                    )
    payload = {
        "schema": "C406-C117-I2-ONE-GLUON-NORMAL-ORDER-VALIDATION-V1",
        "status": STATUS,
        "source_authority": source_authority_record(),
        "maximum_adjoint_generator_hermiticity_residual": maximum_generator_hermiticity,
        "maximum_mode_color_hermiticity_residual": maximum_mode_color_hermiticity,
        "maximum_canonical_route_exchange_residual": maximum_route_symmetry,
        "maximum_vacuum_commutator_color_trace": max(vacuum_traces),
        "vacuum_commutator_exact_zero_by_antisymmetry": True,
        "number_preserving_descendant_bound": True,
        "pair_creation_annihilation_branches_promoted": False,
        "pass": bool(
            maximum_generator_hermiticity < 2e-12
            and maximum_mode_color_hermiticity < 2e-12
            and maximum_route_symmetry < 2e-15
            and max(vacuum_traces) < 2e-12
        ),
        "complete_C117_action": False,
    }
    return {**payload, "root": content_root(payload)}


__all__ = [
    "STATUS",
    "source_authority_record",
    "normal_ordered_mode_terms",
    "dimensionless_descendant_factor_exact",
    "c151_canonical_one_gluon_factor",
    "adjoint_color_current_matrix",
    "one_gluon_mode_color_matrix",
    "one_gluon_descendant_inventory",
    "normal_ordering_validation",
]
