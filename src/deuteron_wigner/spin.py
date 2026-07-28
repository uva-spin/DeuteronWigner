"""Spin-1 target-helicity matrices and convention-safe projections."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .conventions import HELICITIES, HELICITY_INDEX


def _as_matrix(values: np.ndarray) -> np.ndarray:
    matrix = np.asarray(values, dtype=np.complex128)
    if matrix.shape[-2:] != (3, 3):
        raise ValueError("spin-1 helicity matrices must end in shape (3, 3)")
    return matrix


@dataclass(frozen=True)
class HelicityMatrix:
    values: np.ndarray

    def __post_init__(self) -> None:
        object.__setattr__(self, "values", _as_matrix(self.values))

    def is_hermitian(self, tolerance: float = 1e-12) -> bool:
        return bool(
            np.allclose(
                self.values,
                np.swapaxes(self.values.conj(), -1, -2),
                atol=tolerance,
                rtol=0.0,
            )
        )

    def require_hermitian(self, tolerance: float = 1e-12) -> "HelicityMatrix":
        if not self.is_hermitian(tolerance):
            raise ValueError("helicity matrix is not Hermitian")
        return self

    def eigenvalues(self) -> np.ndarray:
        self.require_hermitian()
        return np.linalg.eigvalsh(self.values)

    def is_positive_semidefinite(self, tolerance: float = 1e-12) -> bool:
        return bool(np.all(self.eigenvalues() >= -tolerance))

    def diagonal(self, helicity: int) -> np.ndarray:
        try:
            index = HELICITY_INDEX[helicity]
        except KeyError as exc:
            raise ValueError(f"invalid spin-1 helicity {helicity}") from exc
        return self.values[..., index, index]

    def unpolarized(self) -> np.ndarray:
        return sum(self.diagonal(h) for h in HELICITIES) / 3.0

    def longitudinal_vector(self) -> np.ndarray:
        return 0.5 * (self.diagonal(1) - self.diagonal(-1))

    def tensor_difference(self) -> np.ndarray:
        """Convention-safe delta_T F = F0 - (F+ + F-)/2."""

        return self.diagonal(0) - 0.5 * (self.diagonal(1) + self.diagonal(-1))


def diagonal_from_u_l_delta_t(
    unpolarized: np.ndarray | float,
    longitudinal: np.ndarray | float,
    delta_t: np.ndarray | float,
) -> HelicityMatrix:
    """Invert Eqs. (120)-(122) in the project brief."""

    u, l, tensor = np.broadcast_arrays(unpolarized, longitudinal, delta_t)
    result = np.zeros(u.shape + (3, 3), dtype=np.complex128)
    result[..., HELICITY_INDEX[0], HELICITY_INDEX[0]] = u + 2.0 * tensor / 3.0
    result[..., HELICITY_INDEX[1], HELICITY_INDEX[1]] = u + l - tensor / 3.0
    result[..., HELICITY_INDEX[-1], HELICITY_INDEX[-1]] = u - l - tensor / 3.0
    return HelicityMatrix(result)


def spin_one_basis() -> dict[str, np.ndarray]:
    """Hermitian basis spanning all 3x3 target-helicity matrices.

    Labels follow the U, L, T, LL, LT, TT channel grouping. The two-component
    channels use x/y-like real and imaginary combinations.
    """

    root2 = np.sqrt(2.0)
    basis = {
        "U": np.eye(3, dtype=np.complex128),
        "L": np.diag([1.0, 0.0, -1.0]).astype(np.complex128),
        "T_x": np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=np.complex128) / root2,
        "T_y": np.array([[0, -1j, 0], [1j, 0, -1j], [0, 1j, 0]], dtype=np.complex128)
        / root2,
        "LL": np.diag([-0.5, 1.0, -0.5]).astype(np.complex128),
        "LT_x": np.array([[0, 1, 0], [1, 0, -1], [0, -1, 0]], dtype=np.complex128)
        / root2,
        "LT_y": np.array([[0, -1j, 0], [1j, 0, 1j], [0, -1j, 0]], dtype=np.complex128)
        / root2,
        "TT_x": np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=np.complex128),
        "TT_y": np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=np.complex128),
    }
    return basis


def project_matrix(matrix: np.ndarray, basis_tensor: np.ndarray) -> np.ndarray:
    values = _as_matrix(matrix)
    tensor = _as_matrix(basis_tensor)
    gram = np.einsum("ij,ij->", tensor.conj(), tensor).real
    return np.einsum("ij,...ij->...", tensor.conj(), values) / gram


def reconstruct_from_basis(coefficients: dict[str, np.ndarray | complex]) -> HelicityMatrix:
    basis = spin_one_basis()
    unknown = set(coefficients) - set(basis)
    if unknown:
        raise ValueError(f"unknown spin-1 basis labels: {sorted(unknown)}")
    broadcast = np.broadcast_arrays(*[np.asarray(value) for value in coefficients.values()])
    shape = broadcast[0].shape if broadcast else ()
    result = np.zeros(shape + (3, 3), dtype=np.complex128)
    for (label, _), coefficient in zip(coefficients.items(), broadcast):
        result += coefficient[..., None, None] * basis[label]
    return HelicityMatrix(result)
