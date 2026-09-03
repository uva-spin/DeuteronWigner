"""Leading-twist spin-1 quark-correlator basis and joint projectors.

The three stored projections correspond to ``gamma+``,
``gamma+ gamma5``, and ``i sigma^{i+} gamma5``.  The Cartesian basis is a
direct computational representation of Eqs. (12)--(17) of
arXiv:1612.06585, with the project's physical-S_LL sign adapter explicit.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

import numpy as np

from .gluon_correlator import EPSILON_T
from .spin import spin_one_basis
from .transverse_tensors import symmetric_traceless_2d


@dataclass(frozen=True)
class Spin1QuarkCorrelator:
    vector: np.ndarray
    axial: np.ndarray
    transverse: np.ndarray

    def __post_init__(self) -> None:
        vector = np.asarray(self.vector, dtype=np.complex128)
        axial = np.asarray(self.axial, dtype=np.complex128)
        transverse = np.asarray(self.transverse, dtype=np.complex128)
        if vector.shape != (3, 3) or axial.shape != (3, 3):
            raise ValueError("vector and axial projections must be 3x3")
        if transverse.shape != (2, 3, 3):
            raise ValueError("transverse projection must have shape (2,3,3)")
        object.__setattr__(self, "vector", vector)
        object.__setattr__(self, "axial", axial)
        object.__setattr__(self, "transverse", transverse)

    def is_target_hermitian(self, tolerance: float = 1.0e-12) -> bool:
        return bool(
            np.allclose(self.vector, self.vector.conj().T, atol=tolerance, rtol=0)
            and np.allclose(self.axial, self.axial.conj().T, atol=tolerance, rtol=0)
            and np.allclose(
                self.transverse,
                self.transverse.conj().swapaxes(-1, -2),
                atol=tolerance,
                rtol=0,
            )
        )

    def quark_target_density_matrix(self) -> np.ndarray:
        """Return the complete spin-1 target x quark-spin density (6x6)."""

        if not self.is_target_hermitian():
            raise ValueError("spin-1 correlator is not target Hermitian")
        identity = np.eye(2, dtype=np.complex128)
        pauli_x = np.asarray(((0.0, 1.0), (1.0, 0.0)), dtype=np.complex128)
        pauli_y = np.asarray(((0.0, -1j), (1j, 0.0)), dtype=np.complex128)
        pauli_z = np.asarray(((1.0, 0.0), (0.0, -1.0)), dtype=np.complex128)
        density = np.kron(self.vector, identity)
        density += np.kron(self.axial, pauli_z)
        density += np.kron(self.transverse[0], pauli_x)
        density += np.kron(self.transverse[1], pauli_y)
        return 0.5 * density

    def minimum_positivity_eigenvalue(self) -> float:
        return float(np.linalg.eigvalsh(self.quark_target_density_matrix())[0])


_NAMES = (
    "f1",
    "h1perp",
    "g1",
    "h1Lperp",
    "f1Tperp",
    "g1T",
    "h1",
    "h1Tperp",
    "f1LL",
    "h1LLperp",
    "f1LT",
    "g1LT",
    "h1LT",
    "h1LTperp",
    "f1TT",
    "g1TT",
    "h1TT",
    "h1TTperp",
)
SPIN1_QUARK_TMD_NAMES = _NAMES

T_ODD_QUARK_TMDS = frozenset(
    {
        "h1perp", "f1Tperp", "h1LLperp", "g1LT", "h1LT",
        "h1LTperp", "g1TT", "h1TT", "h1TTperp",
    }
)


def reverse_quark_gauge_link(
    tmds: Mapping[str, float],
) -> dict[str, float]:
    """Apply the exact time-reversal relation between future/past links."""

    unknown = set(tmds) - set(_NAMES)
    if unknown:
        raise ValueError(f"unknown quark TMDs: {sorted(unknown)}")
    return {
        name: (-float(value) if name in T_ODD_QUARK_TMDS else float(value))
        for name, value in tmds.items()
    }


def _empty() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    return (
        np.zeros((3, 3), dtype=np.complex128),
        np.zeros((3, 3), dtype=np.complex128),
        np.zeros((2, 3, 3), dtype=np.complex128),
    )


def _add_target_vector(
    output: np.ndarray,
    basis: Mapping[str, np.ndarray],
    channel: str,
    coefficients: np.ndarray,
) -> None:
    output += coefficients[0] * basis[f"{channel}_x"]
    output += coefficients[1] * basis[f"{channel}_y"]


def quark_correlator_basis(
    momentum: tuple[float, float] | np.ndarray,
    mass: float,
) -> dict[str, Spin1QuarkCorrelator]:
    """Return all 18 named basis correlators at one nonzero momentum."""

    k = np.asarray(momentum, dtype=np.float64)
    if k.shape != (2,) or mass <= 0.0:
        raise ValueError("require a two-vector momentum and positive mass")
    basis = spin_one_basis()
    k2 = symmetric_traceless_2d(k, 2)
    k3 = symmetric_traceless_2d(k, 3)
    epsilon_k = EPSILON_T @ k
    tt_components = np.asarray(
        (k[0] ** 2 - k[1] ** 2, 2.0 * k[0] * k[1])
    )
    tt_epsilon = np.asarray((-tt_components[1], tt_components[0]))
    result: dict[str, Spin1QuarkCorrelator] = {}

    def store(
        name: str,
        vector: np.ndarray,
        axial: np.ndarray,
        transverse: np.ndarray,
    ) -> None:
        result[name] = Spin1QuarkCorrelator(vector, axial, transverse)

    v, a, t = _empty()
    v += basis["U"]
    store("f1", v, a, t)

    v, a, t = _empty()
    t += np.einsum("i,ab->iab", epsilon_k / mass, basis["U"])
    store("h1perp", v, a, t)

    v, a, t = _empty()
    a += basis["L"]
    store("g1", v, a, t)

    v, a, t = _empty()
    t += np.einsum("i,ab->iab", k / mass, basis["L"])
    store("h1Lperp", v, a, t)

    v, a, t = _empty()
    _add_target_vector(v, basis, "T", np.asarray((k[1], -k[0])) / mass)
    store("f1Tperp", v, a, t)

    v, a, t = _empty()
    _add_target_vector(a, basis, "T", k / mass)
    store("g1T", v, a, t)

    v, a, t = _empty()
    for index, suffix in enumerate(("x", "y")):
        t[index] += basis[f"T_{suffix}"]
    store("h1", v, a, t)

    v, a, t = _empty()
    for target_index, suffix in enumerate(("x", "y")):
        for operator_index in range(2):
            t[operator_index] += (
                -k2[operator_index, target_index]
                * basis[f"T_{suffix}"]
                / mass**2
            )
    store("h1Tperp", v, a, t)

    v, a, t = _empty()
    # spin_one_basis["LL"] is minus the physical S_LL convention.
    v -= basis["LL"]
    store("f1LL", v, a, t)

    v, a, t = _empty()
    t -= np.einsum("i,ab->iab", epsilon_k / mass, basis["LL"])
    store("h1LLperp", v, a, t)

    v, a, t = _empty()
    _add_target_vector(v, basis, "LT", k / mass)
    store("f1LT", v, a, t)

    v, a, t = _empty()
    _add_target_vector(a, basis, "LT", np.asarray((k[1], -k[0])) / mass)
    store("g1LT", v, a, t)

    v, a, t = _empty()
    for target_index, suffix in enumerate(("x", "y")):
        t[:, :, :] += np.einsum(
            "i,ab->iab",
            EPSILON_T[:, target_index],
            basis[f"LT_{suffix}"],
        )
    store("h1LT", v, a, t)

    v, a, t = _empty()
    for target_index, suffix in enumerate(("x", "y")):
        rotated = EPSILON_T @ k2[:, target_index]
        t += np.einsum(
            "i,ab->iab", -rotated / mass**2, basis[f"LT_{suffix}"]
        )
    store("h1LTperp", v, a, t)

    v, a, t = _empty()
    _add_target_vector(v, basis, "TT", tt_components / mass**2)
    store("f1TT", v, a, t)

    v, a, t = _empty()
    _add_target_vector(a, basis, "TT", tt_epsilon / mass**2)
    store("g1TT", v, a, t)

    v, a, t = _empty()
    tt_matrices = (
        np.asarray(((1.0, 0.0), (0.0, -1.0))),
        np.asarray(((0.0, 1.0), (1.0, 0.0))),
    )
    for target_matrix, suffix in zip(tt_matrices, ("x", "y")):
        operator = EPSILON_T @ (target_matrix @ k) / mass
        t += np.einsum(
            "i,ab->iab", -operator, basis[f"TT_{suffix}"]
        )
    store("h1TT", v, a, t)

    v, a, t = _empty()
    for target_matrix, suffix in zip(tt_matrices, ("x", "y")):
        contracted = np.einsum("irs,rs->i", k3, target_matrix)
        # Eq. (17) is written with sigma^{mu+}; the stored projection is
        # i sigma^{i+} gamma5 and therefore requires epsilon^{i mu}.
        rotated = EPSILON_T @ contracted
        t += np.einsum(
            "i,ab->iab", rotated / mass**3, basis[f"TT_{suffix}"]
        )
    store("h1TTperp", v, a, t)
    return result


def compose_spin1_quark_correlator(
    momentum: tuple[float, float] | np.ndarray,
    mass: float,
    tmds: Mapping[str, float],
) -> Spin1QuarkCorrelator:
    basis = quark_correlator_basis(momentum, mass)
    if set(tmds) != set(_NAMES):
        missing = sorted(set(_NAMES) - set(tmds))
        unknown = sorted(set(tmds) - set(_NAMES))
        raise ValueError(f"complete quark basis required; missing={missing}, unknown={unknown}")
    vector, axial, transverse = _empty()
    for name, value in tmds.items():
        vector += float(value) * basis[name].vector
        axial += float(value) * basis[name].axial
        transverse += float(value) * basis[name].transverse
    return Spin1QuarkCorrelator(vector, axial, transverse)


def _real_column(correlator: Spin1QuarkCorrelator) -> np.ndarray:
    values = np.concatenate(
        (
            correlator.vector.ravel(),
            correlator.axial.ravel(),
            correlator.transverse.ravel(),
        )
    )
    return np.concatenate((values.real, values.imag))


def project_spin1_quark_correlator(
    correlator: Spin1QuarkCorrelator,
    momentum: tuple[float, float] | np.ndarray,
    mass: float,
    condition_limit: float = 1.0e12,
) -> dict[str, float]:
    """Recover all 18 TMD coefficients by a single Gram/design inversion."""

    basis = quark_correlator_basis(momentum, mass)
    design = np.column_stack([_real_column(basis[name]) for name in _NAMES])
    rank = int(np.linalg.matrix_rank(design))
    if rank != len(_NAMES):
        raise ValueError(
            f"quark projector is rank deficient ({rank}/{len(_NAMES)}); "
            "use nonzero generic transverse momentum"
        )
    condition = float(np.linalg.cond(design))
    if not np.isfinite(condition) or condition > condition_limit:
        raise ValueError(f"quark projector is ill-conditioned ({condition:g})")
    values, _, _, _ = np.linalg.lstsq(design, _real_column(correlator), rcond=None)
    return {name: float(value) for name, value in zip(_NAMES, values)}


def project_spin1_quark_correlator_at_origin(
    correlator: Spin1QuarkCorrelator,
    mass: float,
) -> dict[str, float]:
    """Project the identifiable rank-zero functions at ``k_T=0``.

    Positive-rank named coefficients are conventionally reported as zero in
    the physical origin limit because their tensor structures vanish.  The
    exceptional rank-zero ``h1LT`` remains in the inversion.
    """

    names = ("f1", "g1", "h1", "f1LL", "h1LT")
    basis = quark_correlator_basis((0.0, 0.0), mass)
    design = np.column_stack([_real_column(basis[name]) for name in names])
    if np.linalg.matrix_rank(design) != len(names):
        raise ValueError("rank-zero quark origin projector is deficient")
    values, _, _, _ = np.linalg.lstsq(
        design, _real_column(correlator), rcond=None
    )
    result = {name: 0.0 for name in _NAMES}
    result.update({name: float(value) for name, value in zip(names, values)})
    return result
