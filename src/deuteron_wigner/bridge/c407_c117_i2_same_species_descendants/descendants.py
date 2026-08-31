"""Exact same-species one-body current-current longitudinal descendants."""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from typing import Any, Mapping

import numpy as np
from scipy.sparse import csr_matrix, diags

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root
from deuteron_wigner.bridge.c404_c117_i2_longitudinal_color_primitive.color_spin import (
    EXPECTED_SCALARS,
    adjoint_generators,
    fundamental_generators,
)
from deuteron_wigner.bridge.c406_c117_i2_gluon_normal_order_descendant.normal_order import (
    c151_canonical_one_gluon_factor,
)

from .authority import STATUS
from .axis import external_mode_axis, intermediate_axis

CASIMIR = {
    "QUARK": EXPECTED_SCALARS["J_qJ_q"],
    "GLUON": EXPECTED_SCALARS["J_gJ_g"],
}


def _positive_fraction(value: Fraction | int) -> Fraction:
    result = value if isinstance(value, Fraction) else Fraction(int(value), 1)
    if result <= 0:
        raise ValueError("positive longitudinal mode required")
    return result


def _exact(value: Fraction) -> Mapping[str, Any]:
    return {
        "numerator": value.numerator,
        "denominator": value.denominator,
        "exact": str(value),
        "float": float(value),
    }


def quark_current_dimensionless_factor_exact(
    k_bra: Fraction | int,
    k_ket: Fraction | int,
) -> Fraction:
    """C119 good-component one-body factor after common normalization is factored."""
    _positive_fraction(k_bra)
    _positive_fraction(k_ket)
    return Fraction(1, 1)


def gluon_current_pair_factor_exact(
    external_k: Fraction | int,
    intermediate_k: Fraction | int,
) -> Fraction:
    """Product of the two C406 C151-normalized one-gluon current factors."""
    external = _positive_fraction(external_k)
    intermediate = _positive_fraction(intermediate_k)
    return (external + intermediate) ** 2 / (4 * external * intermediate)


def same_species_weight_exact(
    species: str,
    external_k: Fraction | int,
    intermediate_k: Fraction | int,
) -> Fraction:
    species = str(species).upper()
    if species not in CASIMIR:
        raise ValueError("species must be QUARK or GLUON")
    external = _positive_fraction(external_k)
    intermediate = _positive_fraction(intermediate_k)
    transfer = intermediate - external
    if transfer == 0:
        raise ValueError("Q0 excludes zero transfer")
    if transfer.denominator != 1:
        raise ValueError("same-species APBC/PBC transfer must be integer")
    current = (
        quark_current_dimensionless_factor_exact(external, intermediate)
        * quark_current_dimensionless_factor_exact(intermediate, external)
        if species == "QUARK"
        else gluon_current_pair_factor_exact(external, intermediate)
    )
    return CASIMIR[species] * current / (transfer * transfer)


def same_species_weight_record(
    resolution: str,
    species: str,
    sector: str,
    external_id: str,
    external_k: Fraction,
    intermediate_k: Fraction,
) -> Mapping[str, Any]:
    species = str(species).upper()
    transfer = intermediate_k - external_k
    value = same_species_weight_exact(species, external_k, intermediate_k)
    payload = {
        "schema": "C407-C117-I2-SAME-SPECIES-LONGITUDINAL-WEIGHT-V1",
        "status": STATUS,
        "resolution": resolution,
        "species": species,
        "product": "J_qJ_q" if species == "QUARK" else "J_gJ_g",
        "sector": sector,
        "external_id": external_id,
        "external_k": _exact(external_k),
        "intermediate_k": _exact(intermediate_k),
        "transfer_q": _exact(transfer),
        "Q0_inverse_square": _exact(Fraction(1, 1) / (transfer * transfer)),
        "current_pair_factor": _exact(
            Fraction(1, 1)
            if species == "QUARK"
            else gluon_current_pair_factor_exact(external_k, intermediate_k)
        ),
        "color_Casimir": _exact(CASIMIR[species]),
        "dimensionless_weight": _exact(value),
        "source_overall_minus_g2_over_2_factored": True,
        "finite_cell_field_state_M2_normalization_factored": True,
        "complete_C117_action": False,
    }
    return {**payload, "root": content_root(payload)}


def aggregate_weight_exact(
    resolution: str,
    species: str,
    sector: str,
    external_id: str,
    external_k: Fraction,
) -> Fraction:
    axis = intermediate_axis(resolution, species, sector, external_k, external_id)
    return sum(
        (same_species_weight_exact(species, external_k, row.intermediate_k) for row in axis),
        Fraction(0, 1),
    )


@lru_cache(maxsize=None)
def longitudinal_diagonal_exact(
    resolution: str,
    species: str,
    sector: str,
) -> tuple[Fraction, ...]:
    axis = external_mode_axis(resolution, species, sector)
    if not axis:
        raise RuntimeError(
            "the number-preserving same-species branch has no external particle in this sector; "
            "other pair/vacuum branches remain unresolved rather than zero-filled"
        )
    return tuple(
        aggregate_weight_exact(resolution, species, sector, external_id, external_k)
        for external_id, external_k in axis
    )


def longitudinal_diagonal_dense(resolution: str, species: str, sector: str) -> np.ndarray:
    return np.diag([float(value) for value in longitudinal_diagonal_exact(resolution, species, sector)])


def longitudinal_diagonal_csr(resolution: str, species: str, sector: str) -> csr_matrix:
    values = np.asarray([float(value) for value in longitudinal_diagonal_exact(resolution, species, sector)])
    return diags(values, offsets=0, format="csr")


def apply_longitudinal_diagonal(
    resolution: str,
    species: str,
    sector: str,
    vector: np.ndarray,
) -> np.ndarray:
    diagonal = np.asarray(
        [float(value) for value in longitudinal_diagonal_exact(resolution, species, sector)],
        dtype=np.float64,
    )
    values = np.asarray(vector, dtype=np.complex128)
    if values.shape != diagonal.shape:
        raise ValueError(f"vector must have shape {diagonal.shape}")
    return diagonal * values


def _fermion_annihilation(mode: int, count: int) -> np.ndarray:
    dimension = 1 << count
    result = np.zeros((dimension, dimension), dtype=np.complex128)
    for state in range(dimension):
        if not ((state >> mode) & 1):
            continue
        lower = state & ((1 << mode) - 1)
        sign = -1 if lower.bit_count() % 2 else 1
        result[state ^ (1 << mode), state] = sign
    return result


def _boson_annihilation(mode: int, count: int, maximum_occupancy: int = 2) -> np.ndarray:
    base = maximum_occupancy + 1
    dimension = base**count
    result = np.zeros((dimension, dimension), dtype=np.complex128)
    for state in range(dimension):
        digits = []
        value = state
        for _ in range(count):
            digits.append(value % base)
            value //= base
        occupancy = digits[mode]
        if occupancy == 0:
            continue
        target = state - base**mode
        result[target, state] = np.sqrt(occupancy)
    return result


def _second_quantized_current(gamma: np.ndarray, statistics: str) -> np.ndarray:
    count = gamma.shape[0]
    if gamma.shape != (count, count):
        raise ValueError("gamma must be square")
    annihilation = [
        _fermion_annihilation(index, count)
        if statistics == "FERMION"
        else _boson_annihilation(index, count)
        for index in range(count)
    ]
    result = np.zeros_like(annihilation[0])
    for out in range(count):
        creation = annihilation[out].conj().T
        for inn in range(count):
            result += gamma[out, inn] * creation @ annihilation[inn]
    return result


def _one_particle_indices(count: int, statistics: str) -> tuple[int, ...]:
    if statistics == "FERMION":
        return tuple(1 << mode for mode in range(count))
    base = 3
    return tuple(base**mode for mode in range(count))


def direct_fock_contraction_validation() -> Mapping[str, Any]:
    """Independent finite-Fock verification of the one-body contraction algebra."""
    mode_axes = {
        "QUARK": (Fraction(1, 2), Fraction(3, 2), Fraction(5, 2)),
        "GLUON": (Fraction(1), Fraction(2), Fraction(3)),
    }
    rows = []
    maximum = 0.0
    for species, statistics in (("QUARK", "FERMION"), ("GLUON", "BOSON")):
        modes = mode_axes[species]
        count = len(modes)
        for source in range(count):
            for target in range(count):
                if source == target:
                    continue
                gamma_forward = np.zeros((count, count), dtype=np.complex128)
                gamma_reverse = np.zeros((count, count), dtype=np.complex128)
                if species == "QUARK":
                    factor = 1.0
                else:
                    factor = c151_canonical_one_gluon_factor(modes[target], modes[source])
                gamma_forward[target, source] = factor
                gamma_reverse[source, target] = factor
                left = _second_quantized_current(gamma_reverse, statistics)
                right = _second_quantized_current(gamma_forward, statistics)
                indices = _one_particle_indices(count, statistics)
                restricted = (left @ right)[np.ix_(indices, indices)]
                expected = gamma_reverse @ gamma_forward
                residual = float(np.linalg.norm(restricted - expected))
                maximum = max(maximum, residual)
                rows.append(
                    {
                        "species": species,
                        "source_mode": str(modes[source]),
                        "intermediate_mode": str(modes[target]),
                        "residual": residual,
                    }
                )
    payload = {
        "schema": "C407-SAME-SPECIES-DIRECT-FOCK-CONTRACTION-VALIDATION-V1",
        "status": STATUS,
        "rows": tuple(rows),
        "maximum_residual": maximum,
        "pass": maximum < 2e-14,
    }
    return {**payload, "root": content_root(payload)}


@lru_cache(maxsize=1)
def descendant_inventory() -> Mapping[str, Any]:
    rows = []
    summaries = []
    for resolution in ("K9", "K11", "K13"):
        for species in ("QUARK", "GLUON"):
            for sector in ("q->q", "qg->qg"):
                external = external_mode_axis(resolution, species, sector)
                if not external:
                    summaries.append(
                        {
                            "resolution": resolution,
                            "species": species,
                            "sector": sector,
                            "status": "NUMBER_PRESERVING_BRANCH_NOT_APPLICABLE_OTHER_BRANCHES_UNRESOLVED_NOT_ZERO",
                            "row_count": 0,
                        }
                    )
                    continue
                local = []
                for external_id, external_k in external:
                    axis = intermediate_axis(resolution, species, sector, external_k, external_id)
                    for item in axis:
                        record = same_species_weight_record(
                            resolution,
                            species,
                            sector,
                            external_id,
                            external_k,
                            item.intermediate_k,
                        )
                        rows.append(record)
                        local.append(record)
                summaries.append(
                    {
                        "resolution": resolution,
                        "species": species,
                        "sector": sector,
                        "row_count": len(local),
                        "external_count": len(external),
                        "minimum_weight": min(row["dimensionless_weight"]["float"] for row in local),
                        "maximum_weight": max(row["dimensionless_weight"]["float"] for row in local),
                        "all_positive": all(row["dimensionless_weight"]["float"] > 0 for row in local),
                        "status": "LONGITUDINAL_ONE_BODY_DESCENDANT_READY_COMMON_NORMALIZATION_FACTORED",
                    }
                )
    color_fundamental = sum(matrix @ matrix for matrix in fundamental_generators())
    color_adjoint = sum(matrix @ matrix for matrix in adjoint_generators())
    payload = {
        "schema": "C407-C117-I2-SAME-SPECIES-DESCENDANT-INVENTORY-V1",
        "status": STATUS,
        "rows": tuple(rows),
        "row_count": len(rows),
        "expected_row_count": 154,
        "summaries": tuple(summaries),
        "fundamental_Casimir_residual": float(np.linalg.norm(color_fundamental - (4.0 / 3.0) * np.eye(3))),
        "adjoint_Casimir_residual": float(np.linalg.norm(color_adjoint - 3.0 * np.eye(8))),
        "direct_Fock_validation": direct_fock_contraction_validation(),
        "source_overall_minus_g2_over_2_factored": True,
        "complete_product_normalization": False,
        "complete_C117_action": False,
    }
    if payload["row_count"] != payload["expected_row_count"]:
        raise RuntimeError("C407 descendant inventory expected count changed")
    return {**payload, "root": content_root(payload)}


@lru_cache(maxsize=1)
def longitudinal_validation() -> Mapping[str, Any]:
    rng = np.random.default_rng(407)
    rows = []
    maximum_sparse = 0.0
    minimum = float("inf")
    for resolution in ("K9", "K11", "K13"):
        for species, sectors in (("QUARK", ("q->q", "qg->qg")), ("GLUON", ("qg->qg",))):
            for sector in sectors:
                exact = longitudinal_diagonal_exact(resolution, species, sector)
                dense = longitudinal_diagonal_dense(resolution, species, sector)
                vector = rng.normal(size=len(exact)) + 1j * rng.normal(size=len(exact))
                residual = float(
                    np.linalg.norm(longitudinal_diagonal_csr(resolution, species, sector) @ vector - apply_longitudinal_diagonal(resolution, species, sector, vector))
                )
                maximum_sparse = max(maximum_sparse, residual)
                minimum = min(minimum, min(float(value) for value in exact))
                rows.append(
                    {
                        "resolution": resolution,
                        "species": species,
                        "sector": sector,
                        "dimension": len(exact),
                        "diagonal": tuple(_exact(value) for value in exact),
                        "hermiticity_residual": float(np.linalg.norm(dense - dense.conj().T)),
                        "sparse_matrix_free_residual": residual,
                        "minimum_eigenvalue": float(np.min(np.diag(dense))),
                    }
                )
    payload = {
        "schema": "C407-SAME-SPECIES-LONGITUDINAL-VALIDATION-V1",
        "status": STATUS,
        "rows": tuple(rows),
        "maximum_sparse_matrix_free_residual": maximum_sparse,
        "minimum_weight": minimum,
        "all_positive": minimum > 0,
        "direct_Fock_validation": direct_fock_contraction_validation(),
        "pass": bool(
            maximum_sparse < 1e-14
            and minimum > 0
            and direct_fock_contraction_validation()["pass"]
        ),
        "complete_C117_action": False,
    }
    return {**payload, "root": content_root(payload)}


__all__ = [
    "CASIMIR",
    "quark_current_dimensionless_factor_exact",
    "gluon_current_pair_factor_exact",
    "same_species_weight_exact",
    "same_species_weight_record",
    "aggregate_weight_exact",
    "longitudinal_diagonal_exact",
    "longitudinal_diagonal_dense",
    "longitudinal_diagonal_csr",
    "apply_longitudinal_diagonal",
    "direct_fock_contraction_validation",
    "descendant_inventory",
    "longitudinal_validation",
]
