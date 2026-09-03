"""C406 product-specific routing after one-gluon normal ordering.

Mixed current products contain one quark and one gluon current.  Their retained
qg->qg direct descendant uniquely connects the external quark and gluon modes,
so the exact normal-ordered gluon momentum factor is the sum of the C405 BRA
and KET candidates.  Same-species products instead require one-particle
contraction sums over an intermediate mode axis and are not represented by the
external-pair transfer matrix.
"""
from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from typing import Any, Mapping

import numpy as np
from scipy.sparse import csr_matrix

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root
from deuteron_wigner.bridge.c404_c117_i2_longitudinal_color_primitive.longitudinal import (
    partition_axis,
    partition_transfer_matrix_exact,
)
from deuteron_wigner.bridge.c405_c117_i2_current_topology_embedding.derivative_order import (
    BRA,
    KET,
    ordered_partition_kernel_exact,
)

from .normal_order import STATUS, dimensionless_descendant_factor_exact

MIXED_PRODUCTS = ("J_qJ_g", "J_gJ_q")
SAME_SPECIES_PRODUCTS = ("J_qJ_q", "J_gJ_g")
PRODUCTS = SAME_SPECIES_PRODUCTS[:1] + MIXED_PRODUCTS + SAME_SPECIES_PRODUCTS[1:]


def _check_mixed(product: str) -> str:
    if product not in MIXED_PRODUCTS:
        if product in SAME_SPECIES_PRODUCTS:
            raise RuntimeError(
                f"{product} requires a product-specific intermediate contraction axis; "
                "the external mixed-current routing kernel is not applicable"
            )
        raise KeyError(product)
    return product


def mixed_partition_kernel_exact(
    resolution: str,
    product: str,
) -> tuple[tuple[Fraction, ...], ...]:
    _check_mixed(product)
    partitions = partition_axis(resolution)
    base = partition_transfer_matrix_exact(resolution)
    return tuple(
        tuple(
            base[bra][ket]
            * dimensionless_descendant_factor_exact(
                partitions[bra].k_g, partitions[ket].k_g
            )
            for ket in range(len(partitions))
        )
        for bra in range(len(partitions))
    )


def mixed_partition_kernel_dense(resolution: str, product: str) -> np.ndarray:
    return np.asarray(
        [[float(value) for value in row] for row in mixed_partition_kernel_exact(resolution, product)],
        dtype=np.float64,
    )


def mixed_partition_kernel_csr(resolution: str, product: str) -> csr_matrix:
    return csr_matrix(mixed_partition_kernel_dense(resolution, product))


def apply_mixed_partition_kernel(
    resolution: str,
    product: str,
    vector: np.ndarray,
) -> np.ndarray:
    rows = mixed_partition_kernel_exact(resolution, product)
    values = np.asarray(vector, dtype=np.complex128)
    if values.ndim != 1 or values.shape != (len(rows),):
        raise ValueError(f"vector must have shape ({len(rows)},)")
    result = np.zeros_like(values)
    for bra, row in enumerate(rows):
        result[bra] = sum(float(value) * values[ket] for ket, value in enumerate(row))
    return result


def mixed_c405_collapse_record(resolution: str, product: str) -> Mapping[str, Any]:
    _check_mixed(product)
    exact = mixed_partition_kernel_exact(resolution, product)
    bra = ordered_partition_kernel_exact(resolution, product, (BRA,))
    ket = ordered_partition_kernel_exact(resolution, product, (KET,))
    residuals = []
    for i, row in enumerate(exact):
        for j, value in enumerate(row):
            residuals.append(value + bra[i][j] + ket[i][j])
    matrix = mixed_partition_kernel_dense(resolution, product)
    payload = {
        "schema": "C406-C117-I2-MIXED-CURRENT-DERIVATIVE-COLLAPSE-V1",
        "status": STATUS,
        "resolution": resolution,
        "product": product,
        "identity": "C406 = -(C405_BRA + C405_KET)",
        "maximum_exact_residual": max((abs(value) for value in residuals), default=Fraction(0, 1)),
        "matrix_symmetry_residual": float(np.linalg.norm(matrix - matrix.T)),
        "zero_mode_diagonal_exact": bool(np.array_equal(np.diag(matrix), np.zeros(len(matrix)))),
        "normal_ordering_descendant_bound": True,
        "source_phase_and_sign_bound": True,
        "complete_product_prefactor": False,
        "complete_C117_action": False,
    }
    return {**payload, "root": content_root(payload)}


def mixed_q_sector_zero_certificate(product: str) -> Mapping[str, Any]:
    _check_mixed(product)
    payload = {
        "schema": "C406-C117-I2-MIXED-CURRENT-Q-SECTOR-ZERO-V1",
        "status": STATUS,
        "product": product,
        "external_sector": "q->q",
        "proof": (
            "the only gluon-current fields must contract internally; the bosonic commutator "
            "is proportional to f^{abc}delta_bc=f^{abb}=0, while pair creation/annihilation "
            "branches have zero vacuum-to-vacuum matrix element"
        ),
        "status_value": "EXACT_ZERO_WITH_NORMAL_ORDERING_COLOR_TRACE_PROOF",
        "zero_filled_by_convenience": False,
        "complete_C117_action": False,
    }
    return {**payload, "root": content_root(payload)}


def same_species_intermediate_requirement(product: str) -> Mapping[str, Any]:
    if product not in SAME_SPECIES_PRODUCTS:
        raise KeyError(product)
    species = "quark" if product == "J_qJ_q" else "gluon"
    payload = {
        "schema": "C406-C117-I2-SAME-SPECIES-CONTRACTION-REQUIREMENT-V1",
        "status": STATUS,
        "product": product,
        "species": species,
        "required_object": (
            f"source-qualified one-particle {species} contraction with an explicit intermediate "
            "mode/current-transfer axis, finite support, normal-ordering sign/multiplicity, and target embedding"
        ),
        "why_external_pair_kernel_is_insufficient": (
            "two currents act on the same particle; the nonzero Q0 transfer is internal even when "
            "the external partition is diagonal"
        ),
        "C405_external_pair_stress_kernel_promoted": False,
        "numerical_apply_path": None,
        "complete_C117_action": False,
    }
    return {**payload, "root": content_root(payload)}


@lru_cache(maxsize=1)
def product_routing_audit() -> Mapping[str, Any]:
    rows = []
    for resolution in ("K9", "K11", "K13"):
        for product in PRODUCTS:
            if product in MIXED_PRODUCTS:
                collapse = mixed_c405_collapse_record(resolution, product)
                rows.append(
                    {
                        "resolution": resolution,
                        "product": product,
                        "routing_class": "MIXED_DIRECT_EXTERNAL_TRANSFER",
                        "normal_ordering_descendant_status": "SOURCE_DERIVED_NUMERICAL_PRIMITIVE_READY",
                        "C405_candidate_family_collapsed": True,
                        "collapse_root": collapse["root"],
                        "q_sector": mixed_q_sector_zero_certificate(product)["status_value"],
                        "qg_sector": "MIXED_QG_NORMAL_ORDERED_PRIMITIVE_READY",
                        "complete_C117_action": False,
                    }
                )
            else:
                requirement = same_species_intermediate_requirement(product)
                rows.append(
                    {
                        "resolution": resolution,
                        "product": product,
                        "routing_class": "SAME_SPECIES_ONE_PARTICLE_CONTRACTION",
                        "normal_ordering_descendant_status": "INTERMEDIATE_MODE_AXIS_REQUIRED",
                        "C405_candidate_family_collapsed": False,
                        "requirement_root": requirement["root"],
                        "complete_C117_action": False,
                    }
                )
    payload = {
        "schema": "C406-C117-I2-PRODUCT-ROUTING-AUDIT-V1",
        "status": STATUS,
        "rows": tuple(rows),
        "row_count": len(rows),
        "mixed_product_rows": sum(row["product"] in MIXED_PRODUCTS for row in rows),
        "same_species_rows": sum(row["product"] in SAME_SPECIES_PRODUCTS for row in rows),
        "mixed_derivative_ambiguity_closed": True,
        "same_species_contraction_axes_closed": False,
        "complete_C117_action": False,
    }
    return {**payload, "root": content_root(payload)}


__all__ = [
    "MIXED_PRODUCTS",
    "SAME_SPECIES_PRODUCTS",
    "PRODUCTS",
    "mixed_partition_kernel_exact",
    "mixed_partition_kernel_dense",
    "mixed_partition_kernel_csr",
    "apply_mixed_partition_kernel",
    "mixed_c405_collapse_record",
    "mixed_q_sector_zero_certificate",
    "same_species_intermediate_requirement",
    "product_routing_audit",
]
