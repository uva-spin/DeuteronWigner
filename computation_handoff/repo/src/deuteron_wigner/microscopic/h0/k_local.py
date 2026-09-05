"""Exploratory K-local free-kinetic ``H0`` on the C401/C410 space.

The historical C128 free-operator package has the required direct-sum
dimensions, but C401 established that its reconstructed quark longitudinal
fraction is displaced from the C47 source value.  The same defect affects the
historical qg transverse-kinetic denominator, and C401 deliberately did not
resolve the transverse sub-order because its diagonal mass directions do not
need it.

This module takes the scientifically narrower route needed by M2:

* take the C47 x-scaled basis, CM projection, normalization, and diagonal
  ``q_rel^2`` functional in the public C47 shell-major basis;
* assemble the complete sparse intrinsic-HO recurrence at M2, with a direct
  cross-check against the source-qualified recurrence in C128's ``pperp2``
  layer, while never consuming C128 longitudinal fractions or its numerical
  free matrix;
* keep the quark and gluon mass-squared pieces out of ``H0`` because they are
  supplied separately by the two C401/C396 directions;
* map the source operator into the C401/C410 partition-major, historical-C128
  transverse order with an explicit permutation satisfying
  :class:`H0BasisMapContract`.

The result is a useful free-kinetic baseline, not a physical deuteron
Hamiltonian.  Higher Fock sectors, constrained zero modes, confinement,
interactions, counterterms, a charge/flavor assignment, and a physical sector
projector remain absent and are never interpreted as zero.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from math import sqrt
from typing import Any, Mapping

import numpy as np
from scipy import sparse

from deuteron_wigner.bridge.basis1 import core as c47
from deuteron_wigner.bridge.c401_c396_mass_directions import (
    canonical_partitions,
    historical_c128_partition_defect_audit,
    resolution_record,
)
from deuteron_wigner.bridge.modes.core import ho_labels

from .basis_map import H0BasisMapContract


CLAIM_TIER = "EXPLORATORY"
SOURCE_BASIS_PREFIX = "C47_CM_GROUND_Q_PLUS_QG"
TARGET_BASIS_PREFIX = "C401_C410_DIRECT_SUM"

BasisLabel = tuple[Any, ...]


def _plain(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return [_plain(item) for item in value]
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, complex):
        return [float(value.real), float(value.imag)]
    return value


def _root(value: Any) -> str:
    payload = json.dumps(
        _plain(value), sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode()
    return sha256(payload).hexdigest()


def _max_abs(matrix: sparse.spmatrix) -> float:
    value = matrix.tocsr()
    return float(np.max(np.abs(value.data))) if value.nnz else 0.0


def _mode_orders(resolution: str) -> tuple[tuple[tuple[int, int], ...], tuple[tuple[int, int], ...]]:
    """Return ``(C47 shell-major, C128 target)`` intrinsic-HO orders."""

    record = resolution_record(resolution)
    # C128's retained intrinsic rule is 2 n + |m| + 1 <= Nmax - 1.
    target = tuple(ho_labels(int(record["Nmax"]) - 1))
    source = tuple(sorted(target, key=lambda item: (2 * item[0] + abs(item[1]), item[0], item[1])))
    if len(source) != len(target) or set(source) != set(target):
        raise RuntimeError("C47/C401 intrinsic-HO label sets do not agree")
    return source, target


def _basis_labels(resolution: str, *, source_order: bool) -> tuple[BasisLabel, ...]:
    source_modes, target_modes = _mode_orders(resolution)
    modes = source_modes if source_order else target_modes
    rows: list[BasisLabel] = [
        ("q", helicity, color)
        for helicity in (-1, 1)
        for color in range(3)
    ]
    for partition in canonical_partitions(resolution):
        for n, m in modes:
            for quark_helicity in (-1, 1):
                for gluon_helicity in (-1, 1):
                    for color in range(3):
                        rows.append(
                            (
                                "qg",
                                partition.partition_id,
                                n,
                                m,
                                quark_helicity,
                                gluon_helicity,
                                color,
                            )
                        )
    expected = int(resolution_record(resolution)["direct_sum_dimension"])
    if len(rows) != expected or len(set(rows)) != expected:
        raise RuntimeError(f"basis-label construction did not close {resolution}")
    return tuple(rows)


def c47_source_basis_labels(resolution: str) -> tuple[BasisLabel, ...]:
    """C47 q/qg labels in shell-major intrinsic-HO order."""

    return _basis_labels(resolution, source_order=True)


def c401_target_basis_labels(resolution: str) -> tuple[BasisLabel, ...]:
    """C401/C410 labels in their retained C128 transverse sub-order."""

    return _basis_labels(resolution, source_order=False)


def _kinetic_matrix(resolution: str, labels: tuple[BasisLabel, ...]) -> sparse.csr_matrix:
    """Assemble the M2 sparse ``q_rel^2`` recurrence in the supplied order.

    C47 supplies the x-scaled, CM-ground basis and its diagonal functional.
    The complete off-diagonal HO recurrence is assembled here at M2. Tests
    cross-check its selection rules and coefficients against C128 ``pperp2``
    entries only; this routine has no C128 numerical-matrix or partition input.
    """

    record = resolution_record(resolution)
    dimension = int(record["direct_sum_dimension"])
    b_squared = float(record["b_HO"]) ** 2
    lookup = {label: index for index, label in enumerate(labels)}
    rows: list[int] = []
    columns: list[int] = []
    values: list[float] = []
    for index, label in enumerate(labels):
        if label[0] == "q":
            # The one-particle transverse mode is pure CM motion.  C47's
            # intrinsic/CM projection and the exact P_perp subtraction leave
            # no intrinsic kinetic term in this block.
            continue
        _, partition, n, m, quark_helicity, gluon_helicity, color = label
        rows.append(index)
        columns.append(index)
        values.append(b_squared * (2 * n + abs(m) + 1))
        raised = (
            "qg",
            partition,
            n + 1,
            m,
            quark_helicity,
            gluon_helicity,
            color,
        )
        partner = lookup.get(raised)
        if partner is not None:
            coefficient = -b_squared * sqrt((n + 1) * (n + abs(m) + 1))
            rows.extend((index, partner))
            columns.extend((partner, index))
            values.extend((coefficient, coefficient))
    result = sparse.csr_matrix(
        (np.asarray(values), (np.asarray(rows), np.asarray(columns))),
        shape=(dimension, dimension),
        dtype=np.complex128,
    )
    result.sum_duplicates()
    result.eliminate_zeros()
    result.sort_indices()
    return result


def c47_kinetic_source_csr(resolution: str) -> sparse.csr_matrix:
    """Return the M2 recurrence assembled in C47's source basis order."""

    return _kinetic_matrix(resolution, c47_source_basis_labels(resolution))


def direct_target_kinetic_csr(resolution: str) -> sparse.csr_matrix:
    """Independent direct construction in C401/C410 target order."""

    return _kinetic_matrix(resolution, c401_target_basis_labels(resolution))


def _embedding(
    source_labels: tuple[BasisLabel, ...], target_labels: tuple[BasisLabel, ...]
) -> sparse.csr_matrix:
    source_index = {label: index for index, label in enumerate(source_labels)}
    if set(source_index) != set(target_labels):
        raise RuntimeError("source and target basis label sets differ")
    target_rows = np.arange(len(target_labels), dtype=np.int64)
    source_columns = np.asarray([source_index[label] for label in target_labels], dtype=np.int64)
    return sparse.csr_matrix(
        (np.ones(len(target_labels), dtype=np.complex128), (target_rows, source_columns)),
        shape=(len(target_labels), len(source_labels)),
    )


def _conserved_generators(labels: tuple[BasisLabel, ...]) -> dict[str, sparse.csr_matrix]:
    dimension = len(labels)
    sector = np.zeros(dimension, dtype=float)
    partition = np.full(dimension, -1.0, dtype=float)
    jz = np.zeros(dimension, dtype=float)
    color = np.zeros(dimension, dtype=float)
    reflection_rows = np.arange(dimension, dtype=np.int64)
    lookup = {label: index for index, label in enumerate(labels)}
    for index, label in enumerate(labels):
        if label[0] == "q":
            _, helicity, color_index = label
            jz[index] = helicity / 2.0
            color[index] = color_index
            continue
        _, partition_id, n, m, quark_helicity, gluon_helicity, color_index = label
        sector[index] = 1.0
        partition[index] = float(partition_id)
        jz[index] = quark_helicity / 2.0 + gluon_helicity + m
        color[index] = color_index
        reflection_rows[index] = lookup[
            (
                "qg",
                partition_id,
                n,
                -m,
                quark_helicity,
                gluon_helicity,
                color_index,
            )
        ]
    diagonal = lambda values: sparse.diags(values, format="csr", dtype=np.complex128)
    reflection = sparse.csr_matrix(
        (
            np.ones(dimension, dtype=np.complex128),
            (np.arange(dimension, dtype=np.int64), reflection_rows),
        ),
        shape=(dimension, dimension),
    )
    return {
        "FOCK_SECTOR": diagonal(sector),
        "LONGITUDINAL_PARTITION": diagonal(partition),
        "JZ": diagonal(jz),
        "OPEN_TRIPLET_COLOR_COMPONENT": diagonal(color),
        "TRANSVERSE_M_REFLECTION": reflection,
    }


def _minimum_qg_eigenvalue(resolution: str) -> float:
    """Small dense radial blocks suffice to prove finite-truncation positivity."""

    source_modes, _ = _mode_orders(resolution)
    b_squared = float(resolution_record(resolution)["b_HO"]) ** 2
    minimum = float("inf")
    for m in sorted({mode[1] for mode in source_modes}):
        ns = sorted(n for n, mode_m in source_modes if mode_m == m)
        block = np.zeros((len(ns), len(ns)), dtype=float)
        for i, n in enumerate(ns):
            block[i, i] = b_squared * (2 * n + abs(m) + 1)
            if i + 1 < len(ns) and ns[i + 1] == n + 1:
                value = -b_squared * sqrt((n + 1) * (n + abs(m) + 1))
                block[i, i + 1] = value
                block[i + 1, i] = value
        minimum = min(minimum, float(np.linalg.eigvalsh(block)[0]))
    return minimum


@dataclass(frozen=True)
class KLocalH0Supply:
    """One explicitly mapped exploratory H0 supply for the main-line bundle."""

    resolution: str
    source_operator: sparse.csr_matrix
    target_operator: sparse.csr_matrix
    basis_map: H0BasisMapContract
    source_basis_labels: tuple[BasisLabel, ...]
    target_basis_labels: tuple[BasisLabel, ...]
    validation: Mapping[str, Any]
    claim_tier: str = CLAIM_TIER
    physical: bool = False

    @property
    def dimension(self) -> int:
        return int(self.target_operator.shape[0])

    @property
    def source_id(self) -> str:
        return (
            "C47_X_SCALED_BASIS_DIAGONAL_PLUS_M2_HO_RECURRENCE_"
            f"MAPPED_TO_C401_C410:{self.resolution}"
        )


def build_exploratory_k_local_h0(resolution: str) -> KLocalH0Supply:
    """Construct and validate the M2 free-kinetic H0 supply.

    C47 is not represented as a supplied sparse Hamiltonian matrix: it owns
    the x-scaled basis, normalization, CM projection, and diagonal functional.
    M2 assembles the sparse HO recurrence, whose coefficients are independently
    cross-checked against C128's source-qualified ``pperp2`` layer without
    consuming C128 fractions or free-matrix values. No numerical mass, coupling,
    interaction, counterterm, or physical-sector choice is made here. The two
    mass terms are deliberately left for explicit C401/C396 coefficients in
    the operator bundle.
    """

    record = resolution_record(resolution)
    source_labels = c47_source_basis_labels(resolution)
    target_labels = c401_target_basis_labels(resolution)
    source = _kinetic_matrix(resolution, source_labels)
    embedding = _embedding(source_labels, target_labels)
    commutator_ids = (
        "M2-H0-COMMUTATOR-FOCK-SECTOR",
        "M2-H0-COMMUTATOR-LONGITUDINAL-PARTITION",
        "M2-H0-COMMUTATOR-JZ",
        "M2-H0-COMMUTATOR-OPEN-TRIPLET-COLOR",
        "M2-H0-COMMUTATOR-TRANSVERSE-M-REFLECTION",
    )
    contract = H0BasisMapContract(
        resolution=record["resolution_label"],
        source_basis_id=f"{SOURCE_BASIS_PREFIX}:{record['full_resolution_id']}:SHELL_MAJOR",
        target_basis_id=f"{TARGET_BASIS_PREFIX}:{record['resolution_label']}:C128_TRANSVERSE_ORDER",
        source_dimension=len(source_labels),
        target_dimension=len(target_labels),
        embedding=embedding,
        source_units="GeV^2",
        target_units="GeV^2",
        source_sector_labels=tuple(str(label[0]) for label in source_labels),
        omitted_sector_treatment=(
            "q+qg CM-ground kinetic subspace only; higher Fock sectors, constrained "
            "zero modes, confinement, interactions, and counterterms are "
            "UNIMPLEMENTED_NOT_ZERO; C401 mass directions remain external"
        ),
        hermiticity_test_id="M2-H0-C47-QREL2-HERMITICITY",
        commutator_test_ids=commutator_ids,
        claim_tier=CLAIM_TIER,
        physical=False,
    )
    target = contract.embed_operator(source)
    direct_target = _kinetic_matrix(resolution, target_labels)
    generators = _conserved_generators(source_labels)
    basis_validation = contract.validation_record(
        source_operator=source, conserved_generators=generators
    )
    commutator_residuals = dict(basis_validation["commutator_residuals"])
    defect = historical_c128_partition_defect_audit()
    basis_ordering = {
        "direct_sum": "q sector followed by qg sector",
        "q": "quark helicity (-1,+1), then open triplet color component (0,1,2)",
        "qg_outer_to_inner": (
            "longitudinal partition_id, intrinsic-HO mode, quark helicity "
            "(-1,+1), gluon helicity (-1,+1), open triplet color component (0,1,2)"
        ),
        "source_intrinsic_HO": "C47 shell-major (2n+|m|), then n, then m",
        "target_intrinsic_HO": "retained C128 n-major, then m",
    }
    normalization_ownership = {
        "operator": (
            "M2 q_rel^2 recurrence is already an invariant-mass-squared contribution "
            "in the C47 x-scaled basis under M^2=2 P^+ P^- - P_perp^2"
        ),
        "oscillator_scale": "C45/C47 b_HO in GeV; q_rel^2 matrix carries b_HO^2",
        "longitudinal_cell": (
            "C43/C45 normalized finite-cell modes; L and P+ leave no residual "
            "factor in this C47 q_rel^2 contribution"
        ),
        "basis_map": "M2 permutation is exactly isometric and adds no scale factor",
        "sparse_recurrence": "M2; C128 pperp2 cross-check only, with no C128 x fractions or free-matrix values",
        "mass_terms": "C401/C396 D_mu_q_sq and D_delta_mu_g_sq coefficients, external to H0",
        "C117": "C411 owns its separate exploratory Pminus-to-M2 conversion and coefficient",
    }
    validation_payload = {
        "schema": "M2-EXPLORATORY-K-LOCAL-H0-VALIDATION-V1",
        "resolution": record["resolution_label"],
        "full_resolution_id": record["full_resolution_id"],
        "source_operator": (
            "M2 sparse q_rel^2 recurrence in the C47 x-scaled, exact-CM-ground basis; "
            "C47 supplies the diagonal functional, not a complete sparse matrix"
        ),
        "source_formula": (
            "M2 HO recurrence: <n',m'|q_rel^2|n,m> = b_HO^2[(2n+|m|+1)delta_nn' "
            "-sqrt((n+1)(n+|m|+1))delta_n',n+1 - h.c.]"
        ),
        "sparse_recurrence_owner": "M2 assembly; cross-checked against C128 pperp2 Laguerre/HO recurrence",
        "C47_sparse_hamiltonian_matrix_supplied": False,
        "C47_basis_normalization_CM_and_diagonal_functional_used": True,
        "C128_pperp2_recurrence_cross_check": "REQUIRED_TEST_ONLY_NO_NUMERICAL_FREE_MATRIX_OR_FRACTIONS",
        "mass_terms_in_h0": False,
        "mass_term_owner": "explicit C401/C396 D_mu_q_sq and D_delta_mu_g_sq coefficients",
        "basis_ordering": basis_ordering,
        "normalization_ownership": normalization_ownership,
        "shape": tuple(target.shape),
        "source_nnz": int(source.nnz),
        "target_nnz": int(target.nnz),
        "map_id": contract.map_id,
        "map_isometry_residual": contract.isometry_residual,
        "source_target_label_bijection": len(set(source_labels)) == len(target_labels),
        "source_and_target_orders_differ": source_labels != target_labels,
        "embedded_vs_direct_target_max_abs_residual": _max_abs(target - direct_target),
        "source_hermiticity_residual": _max_abs(source - source.getH()),
        "target_hermiticity_residual": _max_abs(target - target.getH()),
        "commutator_residuals": commutator_residuals,
        "minimum_qg_eigenvalue_GeV2": _minimum_qg_eigenvalue(resolution),
        "q_block_exact_zero": int(source[: int(record["q_dimension"]), :].nnz) == 0,
        "C47_status": c47.STATUS,
        "C7_C8_numeric_operator_used": False,
        "C7_C8_dimension_assumption_used": False,
        "historical_C128_numeric_operator_used": False,
        "historical_C128_longitudinal_fractions_used": False,
        "historical_C128_preserved": True,
        "historical_C128_partition_defect_root": defect["root"],
        "historical_C128_qg_transverse_kinetic_denominator_affected": defect[
            "qg_transverse_kinetic_denominator_affected"
        ],
        "charge_policy": "OPEN_QUARK_IDENTITY; NO_PHYSICAL_CHARGE_OR_FLAVOR_SECTOR_SELECTED",
        "Jz_policy": "KINETIC_COMMUTATOR_TESTED; NO_DEUTERON_JZ_SECTOR_SELECTED",
        "color_policy": "OPEN_TRIPLET_COMPONENT_IDENTITY; NO_COLOR_SINGLET_DEUTERON CLAIM",
        "parity_policy": "TRANSVERSE_M_REFLECTION_TESTED; FULL_PHYSICAL_PARITY UNASSIGNED",
        "center_of_mass_policy": "C47 EXACT CM_GROUND SUBSPACE; NO LAWSON TERM",
        "zero_mode_policy": (
            "ordinary dynamical gluon k=0 excluded by C45; constrained P0/boundary "
            "content remains UNIMPLEMENTED_NOT_ZERO"
        ),
        "claim_tier": CLAIM_TIER,
        "physical": False,
        "physical_state_selected": False,
        "hamiltonian_activation": False,
    }
    validation = {
        **validation_payload,
        "pass": bool(
            validation_payload["map_isometry_residual"] == 0.0
            and validation_payload["embedded_vs_direct_target_max_abs_residual"] == 0.0
            and validation_payload["source_hermiticity_residual"] == 0.0
            and validation_payload["target_hermiticity_residual"] == 0.0
            and max(commutator_residuals.values(), default=0.0) == 0.0
            and validation_payload["minimum_qg_eigenvalue_GeV2"] > 0.0
            and validation_payload["q_block_exact_zero"]
        ),
    }
    validation = {**validation, "root": _root(validation)}
    if not validation["pass"]:
        raise RuntimeError(f"exploratory K-local H0 validation failed at {resolution}")
    return KLocalH0Supply(
        resolution=record["resolution_label"],
        source_operator=source,
        target_operator=target,
        basis_map=contract,
        source_basis_labels=source_labels,
        target_basis_labels=target_labels,
        validation=validation,
    )


def k_local_h0_record(supply: KLocalH0Supply) -> Mapping[str, Any]:
    """Return a compact, matrix-free provenance record for one H0 supply."""

    payload = {
        "schema": "M2-EXPLORATORY-K-LOCAL-H0-SUPPLY-V1",
        "resolution": supply.resolution,
        "source_id": supply.source_id,
        "source_basis_id": supply.basis_map.source_basis_id,
        "target_basis_id": supply.basis_map.target_basis_id,
        "basis_map_id": supply.basis_map.map_id,
        "shape": tuple(supply.target_operator.shape),
        "nnz": int(supply.target_operator.nnz),
        "operator_units": supply.basis_map.target_units,
        "sparse_recurrence_owner": supply.validation["sparse_recurrence_owner"],
        "C47_sparse_hamiltonian_matrix_supplied": False,
        "C128_pperp2_recurrence_cross_check": supply.validation[
            "C128_pperp2_recurrence_cross_check"
        ],
        "source_order": "C47 shell-major intrinsic-HO order",
        "target_order": "C401/C410 partition-major C128 transverse order",
        "basis_ordering": supply.validation["basis_ordering"],
        "normalization_ownership": supply.validation["normalization_ownership"],
        "mass_terms_in_h0": False,
        "C7_C8_numeric_operator_used": False,
        "historical_C128_numeric_operator_used": False,
        "validation_root": supply.validation["root"],
        "omitted_sector_treatment": supply.basis_map.omitted_sector_treatment,
        "claim_tier": supply.claim_tier,
        "physical": supply.physical,
        "physical_state_selected": False,
        "hamiltonian_activation": False,
    }
    return {**payload, "root": _root(payload)}


__all__ = [
    "CLAIM_TIER",
    "SOURCE_BASIS_PREFIX",
    "TARGET_BASIS_PREFIX",
    "BasisLabel",
    "KLocalH0Supply",
    "c47_source_basis_labels",
    "c401_target_basis_labels",
    "c47_kinetic_source_csr",
    "direct_target_kinetic_csr",
    "build_exploratory_k_local_h0",
    "k_local_h0_record",
]
