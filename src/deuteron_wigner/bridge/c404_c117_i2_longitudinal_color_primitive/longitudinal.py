"""C404 exact C114 Q0 longitudinal-transfer primitive on the C47 qg axis.

This module closes only the dimensionless nonzero-transfer factor in

    (i partial^+)^{-2} -> (L/pi)^2 / n^2,  n != 0,

for external qg states at fixed total K.  It does not supply the C119 field
and state normalizations, the ordered gluon-current derivative factor, the
source coefficient, g_s^2, target-member aggregation, or a complete C117
Hamiltonian-coordinate action.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from typing import Any, Mapping

import numpy as np
from scipy.sparse import csr_matrix

from deuteron_wigner.bridge.basis1 import core as c47
from deuteron_wigner.bridge.c401_c396_mass_directions.basis import (
    content_root,
    normalize_resolution,
)
from deuteron_wigner.bridge.c403_c117_i2_numerical_primitive.spatial import (
    HOMode,
    external_modes,
)

STATUS = (
    "C404_C117_I2_Q0_LONGITUDINAL_AND_TRIPLET_COLOR_PRIMITIVE_READY_"
    "FULL_C117_OPERATOR_UNAVAILABLE"
)


@dataclass(frozen=True)
class PartitionRecord:
    resolution: str
    partition_id: int
    k_q: Fraction
    k_g: Fraction
    x_q: Fraction
    x_g: Fraction

    def to_record(self) -> dict[str, Any]:
        def exact(value: Fraction) -> dict[str, Any]:
            return {
                "numerator": value.numerator,
                "denominator": value.denominator,
                "exact": str(value),
                "float": float(value),
            }

        return {
            "resolution": self.resolution,
            "partition_id": self.partition_id,
            "k_q": exact(self.k_q),
            "k_g": exact(self.k_g),
            "x_q": exact(self.x_q),
            "x_g": exact(self.x_g),
            "total_K": exact(self.k_q + self.k_g),
        }


def _source_resolution(resolution: str):
    _short, full = normalize_resolution(resolution)
    for source in c47.RESOLUTIONS:
        if source.label == full:
            return source
    raise KeyError(resolution)


@lru_cache(maxsize=None)
def partition_axis(resolution: str) -> tuple[PartitionRecord, ...]:
    short, _full = normalize_resolution(resolution)
    source = _source_resolution(resolution)
    rows = []
    for index, (k_q, k_g, x_q, x_g) in enumerate(c47.partitions(source)):
        if k_q + k_g != source.K:
            raise ValueError("C47 partition does not conserve total K")
        if x_q + x_g != 1:
            raise ValueError("C47 partition fractions do not sum to one")
        rows.append(PartitionRecord(short, index, k_q, k_g, x_q, x_g))
    return tuple(rows)


def transfer_record(resolution: str, bra_partition: int, ket_partition: int) -> Mapping[str, Any]:
    rows = partition_axis(resolution)
    try:
        bra = rows[int(bra_partition)]
        ket = rows[int(ket_partition)]
    except IndexError as exc:
        raise IndexError((bra_partition, ket_partition)) from exc
    n_q = bra.k_q - ket.k_q
    n_g = bra.k_g - ket.k_g
    if n_q.denominator != 1 or n_g.denominator != 1:
        raise ValueError("fixed-K qg transfer must be an integer mode difference")
    if n_q + n_g != 0:
        raise ValueError("quark and gluon transfer do not conserve total K")
    q0_admitted = n_q != 0
    inverse = Fraction(0, 1) if not q0_admitted else Fraction(1, 1) / (n_q * n_q)
    payload = {
        "schema": "C404-C117-I2-Q0-TRANSFER-V1",
        "status": STATUS,
        "resolution": normalize_resolution(resolution)[0],
        "bra_partition": bra.to_record(),
        "ket_partition": ket.to_record(),
        "n_q": {"exact": str(n_q), "integer": int(n_q)},
        "n_g": {"exact": str(n_g), "integer": int(n_g)},
        "conservation_residual": int(n_q + n_g),
        "Q0_admitted": q0_admitted,
        "zero_mode_status": "Q0_EXCLUDED_EXACT_ZERO_TRANSFER" if not q0_admitted else "Q0_NONZERO_TRANSFER",
        "inverse_partial_plus_squared_dimensionless": {
            "numerator": inverse.numerator,
            "denominator": inverse.denominator,
            "exact": str(inverse),
            "float": float(inverse),
        },
        "full_C114_factor": "(L/pi)^2 * inverse_partial_plus_squared_dimensionless",
        "source_orientation": "n_q=k_q,out-k_q,in; n_g=-n_q",
        "q_sector_direct_exchange_scope": "Q0_ZERO_TRANSFER_ONLY_NOT_A_CERTIFICATE_FOR_ALL_Q_SECTOR_CONTRACTIONS",
    }
    return {**payload, "root": content_root(payload)}


@lru_cache(maxsize=None)
def partition_transfer_matrix_exact(resolution: str) -> tuple[tuple[Fraction, ...], ...]:
    count = len(partition_axis(resolution))
    return tuple(
        tuple(
            Fraction(
                transfer_record(resolution, bra, ket)["inverse_partial_plus_squared_dimensionless"]["numerator"],
                transfer_record(resolution, bra, ket)["inverse_partial_plus_squared_dimensionless"]["denominator"],
            )
            for ket in range(count)
        )
        for bra in range(count)
    )


def partition_transfer_matrix_dense(resolution: str) -> np.ndarray:
    return np.asarray(
        [[float(value) for value in row] for row in partition_transfer_matrix_exact(resolution)],
        dtype=np.float64,
    )


def partition_transfer_matrix_csr(resolution: str) -> csr_matrix:
    return csr_matrix(partition_transfer_matrix_dense(resolution))


def apply_partition_transfer(resolution: str, vector: np.ndarray) -> np.ndarray:
    values = np.asarray(vector, dtype=np.complex128)
    count = len(partition_axis(resolution))
    if values.ndim != 1 or values.shape != (count,):
        raise ValueError(f"vector must have shape ({count},)")
    result = np.zeros_like(values)
    exact = partition_transfer_matrix_exact(resolution)
    for bra, row in enumerate(exact):
        total = 0j
        for ket, coefficient in enumerate(row):
            total += float(coefficient) * values[ket]
        result[bra] = total
    return result


@lru_cache(maxsize=None)
def c47_relative_modes(resolution: str) -> tuple[HOMode, ...]:
    """C47 intrinsic-mode order used inside each longitudinal partition."""
    source = _source_resolution(resolution)
    partitions = c47.partitions(source)
    if not partitions:
        raise ValueError("C47 resolution has no qg partitions")
    intrinsic, _product, _map = c47.tm_cm_ground_map(partitions[0][2], source.Nmax - 2)
    modes = tuple(HOMode(int(n), int(m)) for n, m in intrinsic)
    if len(modes) != len(set(modes)):
        raise ValueError("C47 intrinsic-mode axis contains duplicates")
    admitted = set(external_modes(resolution))
    if set(modes) != admitted:
        raise ValueError("C47 intrinsic-mode support disagrees with the exact C403 support theorem")
    # The label list is independent of x; verify every partition has the same order.
    for _kq, _kg, xq, _xg in partitions[1:]:
        other, _product, _map = c47.tm_cm_ground_map(xq, source.Nmax - 2)
        if tuple((int(n), int(m)) for n, m in other) != tuple((mode.n, mode.m) for mode in modes):
            raise ValueError("C47 intrinsic-mode ordering depends on longitudinal partition")
    return modes


@lru_cache(maxsize=None)
def c47_to_c403_mode_permutation(resolution: str) -> tuple[int, ...]:
    """Indices that read a C403-order vector/matrix in C47 intrinsic-mode order."""
    c403_modes = external_modes(resolution)
    lookup = {mode: index for index, mode in enumerate(c403_modes)}
    return tuple(lookup[mode] for mode in c47_relative_modes(resolution))


def qg_factorized_axis_record(resolution: str) -> Mapping[str, Any]:
    source = _source_resolution(resolution)
    qg_rows, _maps, _product = c47.qg_basis(source)
    partitions = partition_axis(resolution)
    modes = c47_relative_modes(resolution)
    expected = len(partitions) * len(modes) * 2 * 2 * 3
    if len(qg_rows) != expected:
        raise ValueError("C47 qg basis does not match the factorized C404 axis")
    # Verify the exact public ordering without retaining the huge row list.
    index = 0
    for p, partition in enumerate(partitions):
        for mode in modes:
            for h_q in (-1, 1):
                for h_g in (-1, 1):
                    for color in range(3):
                        row = qg_rows[index]
                        observed = (row[0], row[1], row[2], row[5], row[6], row[9], row[10], row[11])
                        expected_row = (p, partition.k_q, partition.k_g, mode.n, mode.m, h_q, h_g, color)
                        if observed != expected_row:
                            raise ValueError(f"C47 qg ordering mismatch at index {index}")
                        index += 1
    payload = {
        "schema": "C404-C117-I2-QG-FACTORIZED-AXIS-V1",
        "status": STATUS,
        "resolution": normalize_resolution(resolution)[0],
        "partition_count": len(partitions),
        "transverse_mode_count": len(modes),
        "transverse_mode_order": tuple(mode.to_record() for mode in modes),
        "C403_to_C47_permutation": c47_to_c403_mode_permutation(resolution),
        "quark_helicity_count": 2,
        "gluon_helicity_count": 2,
        "triplet_color_count": 3,
        "dimension": expected,
        "ordering": "partition, intrinsic_HO_mode, quark_helicity, gluon_helicity, triplet_color",
        "C47_ordering_verified": True,
        "q_sector_external_axis_in_this_primitive": False,
    }
    return {**payload, "root": content_root(payload)}


@lru_cache(maxsize=1)
def longitudinal_inventory() -> Mapping[str, Any]:
    rows = []
    for resolution in ("K9", "K11", "K13"):
        matrix = partition_transfer_matrix_dense(resolution)
        records = [
            transfer_record(resolution, bra, ket)
            for bra in range(matrix.shape[0])
            for ket in range(matrix.shape[1])
        ]
        rows.append(
            {
                "resolution": resolution,
                "axis": qg_factorized_axis_record(resolution),
                "partition_count": matrix.shape[0],
                "transfer_records": records,
                "nonzero_Q0_pairs": int(np.count_nonzero(matrix)),
                "zero_transfer_pairs": int(matrix.shape[0]),
                "symmetry_residual": float(np.linalg.norm(matrix - matrix.T)),
                "diagonal_residual": float(np.linalg.norm(np.diag(matrix))),
                "minimum_nonzero_factor": float(np.min(matrix[matrix > 0])),
                "maximum_factor": float(np.max(matrix)),
            }
        )
    payload = {
        "schema": "C404-C117-I2-LONGITUDINAL-INVENTORY-V1",
        "status": STATUS,
        "rows": rows,
        "complete_C117_apply_paths": 0,
        "complete_C396_apply_paths": 6,
        "rank_status": "RANK_NOT_EVALUATED",
        "physical_fit_authorized": False,
    }
    return {**payload, "root": content_root(payload)}


__all__ = [
    "STATUS",
    "PartitionRecord",
    "partition_axis",
    "transfer_record",
    "partition_transfer_matrix_exact",
    "partition_transfer_matrix_dense",
    "partition_transfer_matrix_csr",
    "apply_partition_transfer",
    "c47_relative_modes",
    "c47_to_c403_mode_permutation",
    "qg_factorized_axis_record",
    "longitudinal_inventory",
]
