"""C404 exact C45/C47 triplet color-charge and J+ spin-selection primitives.

The color matrices are charge-generator contractions in the C45 Hermitian
adjoint convention ``F^a_bc=-i f^{abc}``, projected with the C47 triplet
isometry.  They are not by themselves complete C115 current amplitudes: the
source-field phase, ordered gluon derivative, finite-cell normalization, and
C114 coefficient remain separately unbound.
"""
from __future__ import annotations

from functools import lru_cache
from fractions import Fraction
from typing import Any, Mapping

import numpy as np

from deuteron_wigner.bridge.basis1 import core as c47
from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root
from deuteron_wigner.bridge.modes import core as c45

from .longitudinal import STATUS

PRODUCTS = ("J_qJ_q", "J_qJ_g", "J_gJ_q", "J_gJ_g")
EXPECTED_SCALARS = {
    "J_qJ_q": Fraction(4, 3),
    "J_qJ_g": Fraction(-3, 2),
    "J_gJ_q": Fraction(-3, 2),
    "J_gJ_g": Fraction(3, 1),
}


@lru_cache(maxsize=1)
def _generator_data() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    _projector, _total, fundamental = c45.color_triplet_projector()
    structure = np.empty((8, 8, 8), dtype=np.float64)
    for a in range(8):
        for b in range(8):
            for c in range(8):
                structure[a, b, c] = float(
                    (-2j * np.trace((fundamental[a] @ fundamental[b] - fundamental[b] @ fundamental[a]) @ fundamental[c])).real
                )
    adjoint = -1j * structure
    isometry = c47.triplet_isometry()
    return fundamental, adjoint, isometry


def fundamental_generators() -> np.ndarray:
    return np.array(_generator_data()[0], copy=True)


def adjoint_generators() -> np.ndarray:
    return np.array(_generator_data()[1], copy=True)


def triplet_isometry() -> np.ndarray:
    return np.array(_generator_data()[2], copy=True)


@lru_cache(maxsize=None)
def _product_matrix_cached(product: str) -> np.ndarray:
    if product not in PRODUCTS:
        raise KeyError(product)
    fundamental, adjoint, isometry = _generator_data()
    tq = tuple(np.kron(fundamental[a], np.eye(8)) for a in range(8))
    fg = tuple(np.kron(np.eye(3), adjoint[a]) for a in range(8))
    if product == "J_qJ_q":
        raw = sum(left @ left for left in tq)
    elif product == "J_qJ_g":
        raw = sum(left @ right for left, right in zip(tq, fg))
    elif product == "J_gJ_q":
        raw = sum(right @ left for left, right in zip(tq, fg))
    else:
        raw = sum(right @ right for right in fg)
    projected = isometry.conj().T @ raw @ isometry
    projected.setflags(write=False)
    return projected


def triplet_color_product_matrix(product: str) -> np.ndarray:
    return np.array(_product_matrix_cached(product), copy=True)


def triplet_color_product_record(product: str) -> Mapping[str, Any]:
    matrix = triplet_color_product_matrix(product)
    scalar = EXPECTED_SCALARS[product]
    payload = {
        "schema": "C404-C117-I2-TRIPLET-COLOR-PRODUCT-V1",
        "status": STATUS,
        "product": product,
        "C45_fundamental_convention": "T^a=lambda^a/2; Tr(TaTb)=delta_ab/2",
        "C45_adjoint_convention": "F^a_bc=-i f^{abc}",
        "C47_triplet_isometry": "U_(c,b),alpha=T^b_(c,alpha)/sqrt(C_F)",
        "matrix": [[[float(value.real), float(value.imag)] for value in row] for row in matrix],
        "exact_scalar_times_identity": {
            "numerator": scalar.numerator,
            "denominator": scalar.denominator,
            "exact": str(scalar),
        },
        "scalar_identity_residual": float(np.linalg.norm(matrix - float(scalar) * np.eye(3))),
        "hermiticity_residual": float(np.linalg.norm(matrix - matrix.conj().T)),
        "source_phase_and_gluon_derivative_bound": False,
        "complete_C115_current_factor": False,
    }
    return {**payload, "root": content_root(payload)}


def combined_spin_selection_matrix() -> np.ndarray:
    """J+ helicity/polarization selection on the (h_q,h_g) axis."""
    return np.eye(4, dtype=np.complex128)


def spin_selection_record() -> Mapping[str, Any]:
    matrix = combined_spin_selection_matrix()
    payload = {
        "schema": "C404-C117-I2-JPLUS-SPIN-SELECTION-V1",
        "status": STATUS,
        "axis": ((-1, -1), (-1, 1), (1, -1), (1, 1)),
        "matrix": [[[float(value.real), float(value.imag)] for value in row] for row in matrix],
        "quark_rule": "delta_(h_q,out,h_q,in) from gamma+ good-component current",
        "gluon_rule": "delta_(h_g,out,h_g,in) from transverse polarization contraction",
        "spin_flip_entries": 0,
        "ordered_gluon_derivative_factor_included": False,
    }
    return {**payload, "root": content_root(payload)}


@lru_cache(maxsize=1)
def color_spin_validation() -> Mapping[str, Any]:
    fundamental, adjoint, isometry = _generator_data()
    rows = []
    for product in PRODUCTS:
        record = triplet_color_product_record(product)
        rows.append(record)
    total = sum(triplet_color_product_matrix(product) for product in PRODUCTS)
    payload = {
        "schema": "C404-C117-I2-COLOR-SPIN-VALIDATION-V1",
        "status": STATUS,
        "triplet_isometry_residual": float(np.linalg.norm(isometry.conj().T @ isometry - np.eye(3))),
        "fundamental_hermiticity_residual": float(max(np.linalg.norm(x - x.conj().T) for x in fundamental)),
        "adjoint_hermiticity_residual": float(max(np.linalg.norm(x - x.conj().T) for x in adjoint)),
        "product_rows": rows,
        "total_charge_Casimir_residual": float(np.linalg.norm(total - (4.0 / 3.0) * np.eye(3))),
        "mixed_order_residual": float(
            np.linalg.norm(
                triplet_color_product_matrix("J_qJ_g") - triplet_color_product_matrix("J_gJ_q")
            )
        ),
        "spin_selection": spin_selection_record(),
        "pass": bool(
            np.linalg.norm(isometry.conj().T @ isometry - np.eye(3)) < 2e-12
            and max(row["scalar_identity_residual"] for row in rows) < 2e-12
            and max(row["hermiticity_residual"] for row in rows) < 2e-12
            and np.linalg.norm(total - (4.0 / 3.0) * np.eye(3)) < 2e-12
        ),
    }
    return {**payload, "root": content_root(payload)}


__all__ = [
    "PRODUCTS",
    "EXPECTED_SCALARS",
    "fundamental_generators",
    "adjoint_generators",
    "triplet_isometry",
    "triplet_color_product_matrix",
    "triplet_color_product_record",
    "combined_spin_selection_matrix",
    "spin_selection_record",
    "color_spin_validation",
]
