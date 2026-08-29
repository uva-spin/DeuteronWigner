"""Leading-twist transverse-index gluon-correlator building blocks.

This module is an operator/convention layer only.  It implements the
Cartesian form of Eqs. (7), (8), and (10) of arXiv:2603.15224v1 and does not
contain (or assume) the spectator model used later in that paper.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .registry import TargetChannel
from .spin import spin_one_basis
from .transverse_tensors import symmetric_traceless_2d


DELTA_T = np.eye(2, dtype=np.float64)
EPSILON_T = np.asarray(((0.0, 1.0), (-1.0, 0.0)), dtype=np.float64)


def _momentum(momentum: np.ndarray | tuple[float, float]) -> np.ndarray:
    vector = np.asarray(momentum, dtype=np.float64)
    if vector.shape != (2,):
        raise ValueError("transverse momentum must have shape (2,)")
    return vector


def transverse_matrix_parts(
    correlator: np.ndarray,
) -> tuple[complex, complex, np.ndarray]:
    """Return trace, circular, and linear-polarization matrix components.

    The returned scalars are the coefficients of ``delta_T`` and
    ``1j * epsilon_T``.  The last result is the symmetric-traceless part.
    Thus ``phi = trace*delta + circular*(1j*epsilon) + linear``.
    """

    phi = np.asarray(correlator, dtype=np.complex128)
    if phi.shape != (2, 2):
        raise ValueError("gluon correlator must have shape (2, 2)")
    trace = 0.5 * np.trace(phi)
    circular = -0.5j * np.einsum("ij,ij->", EPSILON_T, phi)
    symmetric = 0.5 * (phi + phi.T)
    linear = symmetric - 0.5 * np.trace(symmetric) * DELTA_T
    return complex(trace), complex(circular), linear


def _linear_basis(momentum: np.ndarray) -> np.ndarray:
    return symmetric_traceless_2d(momentum, 2)


def _epsilon_linear_basis(momentum: np.ndarray) -> np.ndarray:
    """Symmetrized epsilon rotation of the rank-two momentum tensor."""

    rank_two = _linear_basis(momentum)
    return EPSILON_T @ rank_two - rank_two @ EPSILON_T


def _project_real(basis: np.ndarray, values: np.ndarray) -> float:
    norm = float(np.einsum("ij,ij->", basis, basis))
    if norm == 0.0:
        raise ValueError("projector is undefined at zero transverse momentum")
    coefficient = np.einsum("ij,ij->", basis, values) / norm
    if abs(float(np.imag(coefficient))) > 1.0e-11:
        raise ValueError("projected TMD coefficient is not real")
    return float(np.real(coefficient))


@dataclass(frozen=True)
class TraceLinearTMDs:
    """TMD pair carried by trace and linear gluon polarization."""

    trace: float
    linear: float


@dataclass(frozen=True)
class GluonTargetPolarization:
    """Cartesian spin-1 target-polarization components."""

    spin_transverse: tuple[float, float] = (0.0, 0.0)
    spin_lt: tuple[float, float] = (0.0, 0.0)
    spin_tt: tuple[tuple[float, float], tuple[float, float]] = (
        (0.0, 0.0),
        (0.0, 0.0),
    )

    def vector(self, channel: TargetChannel) -> np.ndarray:
        if channel == TargetChannel.T:
            value = np.asarray(self.spin_transverse, dtype=np.float64)
        elif channel == TargetChannel.LT:
            value = np.asarray(self.spin_lt, dtype=np.float64)
        else:
            raise ValueError("channel does not carry a vector polarization")
        if value.shape != (2,):
            raise ValueError("target vector polarization must have shape (2,)")
        return value

    def tensor_tt(self) -> np.ndarray:
        value = np.asarray(self.spin_tt, dtype=np.float64)
        if value.shape != (2, 2):
            raise ValueError("S_TT must have shape (2, 2)")
        if not np.allclose(value, value.T, atol=1.0e-12):
            raise ValueError("S_TT must be symmetric")
        if not np.isclose(np.trace(value), 0.0, atol=1.0e-12):
            raise ValueError("S_TT must be traceless")
        return value


@dataclass(frozen=True)
class GluonCorrelatorObservation:
    """One correlator evaluated at a specified momentum and polarization."""

    momentum: tuple[float, float]
    polarization: GluonTargetPolarization
    correlator: np.ndarray


@dataclass(frozen=True)
class Spin1GluonCorrelator:
    """Target-helicity x transverse-gluon correlator."""

    values: np.ndarray

    def __post_init__(self) -> None:
        values = np.asarray(self.values, dtype=np.complex128)
        if values.shape != (3, 3, 2, 2):
            raise ValueError("spin-1 gluon correlator must have shape (3,3,2,2)")
        object.__setattr__(self, "values", values)

    def joint_density_matrix(self) -> np.ndarray:
        """Return the 6x6 target-helicity x gluon-polarization matrix."""

        density = self.values.transpose(0, 2, 1, 3).reshape(6, 6)
        if not np.allclose(density, density.conj().T, atol=1.0e-11, rtol=0):
            raise ValueError("joint spin-1 gluon density is not Hermitian")
        return density

    def minimum_positivity_eigenvalue(self) -> float:
        return float(np.linalg.eigvalsh(self.joint_density_matrix())[0])


_CHANNEL_NAMES = {
    TargetChannel.T: ("f1Tperp", "g1T", "h1", "h1Tperp"),
    TargetChannel.LT: ("f1LT", "g1LT", "h1LT", "h1LTperp"),
    TargetChannel.TT: (
        "f1TT",
        "g1TT",
        "h1TT",
        "h1TTperp",
        "h1TTperpperp",
    ),
}

_PROJECTED_NAMES = {
    TargetChannel.T: _CHANNEL_NAMES[TargetChannel.T],
    TargetChannel.LT: _CHANNEL_NAMES[TargetChannel.LT],
    # In two transverse dimensions the f1TT and h1TTperp basis matrices
    # differ only by sign.  Appendix A therefore projects their difference.
    TargetChannel.TT: (
        "f1TT_minus_h1TTperp",
        "g1TT",
        "h1TT",
        "h1TTperpperp",
    ),
}


def _sym_outer(left: np.ndarray, right: np.ndarray) -> np.ndarray:
    return np.outer(left, right) + np.outer(right, left)


def _epsilon_rotate(vector: np.ndarray) -> np.ndarray:
    return EPSILON_T @ vector


def gluon_correlator_basis(
    channel: TargetChannel,
    momentum: np.ndarray | tuple[float, float],
    mass: float,
    polarization: GluonTargetPolarization,
) -> dict[str, np.ndarray]:
    """Return the named basis matrices of Eqs. (9), (11), or (12).

    Braced transverse indices denote an unnormalized symmetrized sum.  The
    overall factor ``1/2`` appearing in every correlator equation is included
    in each returned matrix.
    """

    if channel not in _CHANNEL_NAMES:
        raise ValueError("basis is available only for T, LT, and TT")
    k = _momentum(momentum)
    if mass <= 0.0:
        raise ValueError("mass must be positive")
    k2 = symmetric_traceless_2d(k, 2)
    k3 = symmetric_traceless_2d(k, 3)

    if channel == TargetChannel.T:
        spin = polarization.vector(channel)
        epsilon_spin_k = float(spin @ EPSILON_T @ k)
        h1_matrix = (
            -_sym_outer(_epsilon_rotate(k), spin)
            - _sym_outer(_epsilon_rotate(spin), k)
        ) / (4.0 * mass)
        h1t_matrix = np.einsum(
            "ia,jab,b->ij", EPSILON_T, k3, spin
        )
        h1t_matrix += h1t_matrix.T
        return {
            "f1Tperp": 0.5 * DELTA_T * epsilon_spin_k / mass,
            "g1T": 0.5j * EPSILON_T * float(k @ spin) / mass,
            "h1": 0.5 * h1_matrix,
            "h1Tperp": -0.5 * h1t_matrix / (2.0 * mass**3),
        }

    if channel == TargetChannel.LT:
        spin = polarization.vector(channel)
        return {
            "f1LT": 0.5 * DELTA_T * float(k @ spin) / mass,
            "g1LT": (
                0.5j * EPSILON_T * float(spin @ EPSILON_T @ k) / mass
            ),
            "h1LT": 0.5 * _sym_outer(spin, k) / mass,
            "h1LTperp": 0.5 * np.einsum("ija,a->ij", k3, spin) / mass**3,
        }

    spin_tt = polarization.tensor_tt()
    k4 = symmetric_traceless_2d(k, 4)
    scalar = float(np.einsum("ab,ab->", k2, spin_tt))
    circular_scalar = float(
        np.einsum("bg,ga,ab->", EPSILON_T, k2, spin_tt)
    )
    h1tt_perp = np.einsum("ia,ja->ij", spin_tt, k2)
    h1tt_perp += h1tt_perp.T
    return {
        "f1TT": 0.5 * DELTA_T * scalar / mass**2,
        "g1TT": 0.5j * EPSILON_T * circular_scalar / mass**2,
        "h1TT": 0.5 * spin_tt,
        "h1TTperp": -0.5 * h1tt_perp / mass**2,
        "h1TTperpperp": (
            0.5 * np.einsum("ijab,ab->ij", k4, spin_tt) / mass**4
        ),
    }


def compose_polarized_gluon_correlator(
    channel: TargetChannel,
    momentum: np.ndarray | tuple[float, float],
    mass: float,
    polarization: GluonTargetPolarization,
    tmds: dict[str, float],
) -> np.ndarray:
    """Compose a T, LT, or TT correlator from named real TMD values."""

    basis = gluon_correlator_basis(channel, momentum, mass, polarization)
    unknown = set(tmds) - set(basis)
    if unknown:
        raise ValueError(f"TMDs do not belong to {channel.value}: {sorted(unknown)}")
    missing = set(basis) - set(tmds)
    if missing:
        raise ValueError(f"missing {channel.value} TMDs: {sorted(missing)}")
    result = np.zeros((2, 2), dtype=np.complex128)
    for name, matrix in basis.items():
        result += float(tmds[name]) * matrix
    return result


def _real_design_column(matrix: np.ndarray) -> np.ndarray:
    values = np.asarray(matrix, dtype=np.complex128)
    return np.concatenate((values.real.ravel(), values.imag.ravel()))


def project_polarized_gluon_correlators(
    channel: TargetChannel,
    observations: list[GluonCorrelatorObservation]
    | tuple[GluonCorrelatorObservation, ...],
    mass: float,
    *,
    condition_limit: float = 1.0e12,
) -> dict[str, float]:
    """Recover all TMDs in one channel by joint Gram-matrix inversion.

    All observations must represent the same ``(x, k_T^2)`` point, although
    their momentum azimuths and target polarizations may differ.
    """

    names = _PROJECTED_NAMES.get(channel)
    if names is None:
        raise ValueError("joint projection is available only for T, LT, and TT")
    if not observations:
        raise ValueError("at least one correlator observation is required")
    radii = [float(np.dot(item.momentum, item.momentum)) for item in observations]
    if not np.allclose(radii, radii[0], rtol=1.0e-11, atol=1.0e-13):
        raise ValueError("observations must have the same k_T squared")

    design_blocks = []
    value_blocks = []
    for item in observations:
        basis = gluon_correlator_basis(
            channel, item.momentum, mass, item.polarization
        )
        if channel == TargetChannel.TT:
            basis = {
                **basis,
                "f1TT_minus_h1TTperp": basis["f1TT"],
            }
        design_blocks.append(
            np.column_stack([_real_design_column(basis[name]) for name in names])
        )
        value_blocks.append(_real_design_column(item.correlator))
    design = np.vstack(design_blocks)
    values = np.concatenate(value_blocks)
    rank = int(np.linalg.matrix_rank(design))
    if rank != len(names):
        raise ValueError(
            f"polarization ensemble has rank {rank}; {len(names)} required"
        )
    condition = float(np.linalg.cond(design))
    if not np.isfinite(condition) or condition > condition_limit:
        raise ValueError(f"polarization ensemble is ill-conditioned ({condition:g})")
    coefficients, _, _, _ = np.linalg.lstsq(design, values, rcond=None)
    return {name: float(value) for name, value in zip(names, coefficients)}


def compose_unpolarized_gluon_correlator(
    momentum: np.ndarray | tuple[float, float],
    mass: float,
    *,
    f1: float,
    h1perp: float,
) -> np.ndarray:
    """Compose ``Phi_U`` in the Euclidean transverse-index convention."""

    k = _momentum(momentum)
    if mass <= 0.0:
        raise ValueError("mass must be positive")
    return 0.5 * (
        DELTA_T * float(f1) + _linear_basis(k) * float(h1perp) / mass**2
    )


def project_unpolarized_gluon_correlator(
    correlator: np.ndarray,
    momentum: np.ndarray | tuple[float, float],
    mass: float,
) -> TraceLinearTMDs:
    """Recover ``f1`` and ``h1perp`` from ``Phi_U``."""

    k = _momentum(momentum)
    if mass <= 0.0:
        raise ValueError("mass must be positive")
    trace, circular, linear = transverse_matrix_parts(correlator)
    if abs(circular) > 1.0e-11:
        raise ValueError("unpolarized correlator has a circular component")
    return TraceLinearTMDs(
        trace=float(np.real(2.0 * trace)),
        linear=2.0 * mass**2 * _project_real(_linear_basis(k), linear),
    )


def compose_longitudinal_gluon_correlator(
    momentum: np.ndarray | tuple[float, float],
    mass: float,
    spin_longitudinal: float,
    *,
    g1: float,
    h1Lperp: float,
) -> np.ndarray:
    """Compose ``Phi_L`` for longitudinal target polarization."""

    k = _momentum(momentum)
    if mass <= 0.0:
        raise ValueError("mass must be positive")
    spin = float(spin_longitudinal)
    return 0.5 * spin * (
        1j * EPSILON_T * float(g1)
        + _epsilon_linear_basis(k) * float(h1Lperp) / (2.0 * mass**2)
    )


def project_longitudinal_gluon_correlator(
    correlator: np.ndarray,
    momentum: np.ndarray | tuple[float, float],
    mass: float,
    spin_longitudinal: float,
) -> tuple[float, float]:
    """Recover ``(g1, h1Lperp)`` from ``Phi_L``."""

    k = _momentum(momentum)
    spin = float(spin_longitudinal)
    if mass <= 0.0:
        raise ValueError("mass must be positive")
    if spin == 0.0:
        raise ValueError("longitudinal spin must be nonzero")
    trace, circular, linear = transverse_matrix_parts(correlator)
    if abs(trace) > 1.0e-11:
        raise ValueError("longitudinal correlator has a trace component")
    g1 = 2.0 * circular / spin
    h1l = 4.0 * mass**2 * _project_real(
        _epsilon_linear_basis(k), linear
    ) / spin
    if abs(g1.imag) > 1.0e-11:
        raise ValueError("projected g1 is not real")
    return float(g1.real), h1l


def compose_ll_gluon_correlator(
    momentum: np.ndarray | tuple[float, float],
    mass: float,
    spin_ll: float,
    *,
    f1LL: float,
    h1LLperp: float,
) -> np.ndarray:
    """Compose ``Phi_LL`` for longitudinal tensor polarization."""

    return float(spin_ll) * compose_unpolarized_gluon_correlator(
        momentum, mass, f1=f1LL, h1perp=h1LLperp
    )


def project_ll_gluon_correlator(
    correlator: np.ndarray,
    momentum: np.ndarray | tuple[float, float],
    mass: float,
    spin_ll: float,
) -> TraceLinearTMDs:
    """Recover ``f1LL`` and ``h1LLperp`` from ``Phi_LL``."""

    spin = float(spin_ll)
    if spin == 0.0:
        raise ValueError("S_LL must be nonzero")
    projected = project_unpolarized_gluon_correlator(
        np.asarray(correlator) / spin, momentum, mass
    )
    return projected


def compose_spin1_gluon_correlator(
    momentum: np.ndarray | tuple[float, float],
    mass: float,
    tmds: dict[str, float],
) -> Spin1GluonCorrelator:
    """Compose the complete identifiable spin-1 gluon density.

    At fixed transverse momentum only
    ``f1TT_minus_h1TTperp`` is identifiable.  The representative assignment
    ``f1TT=combination, h1TTperp=0`` produces the same correlator because
    those two basis tensors are exactly opposite in two transverse
    dimensions.
    """

    expected = {
        "f1", "h1perp", "g1", "h1Lperp",
        "f1Tperp", "g1T", "h1", "h1Tperp",
        "f1LL", "h1LLperp",
        "f1LT", "g1LT", "h1LT", "h1LTperp",
        "f1TT_minus_h1TTperp", "g1TT", "h1TT", "h1TTperpperp",
    }
    if set(tmds) != expected:
        raise ValueError(
            f"complete identifiable gluon basis required; "
            f"missing={sorted(expected - set(tmds))}, "
            f"unknown={sorted(set(tmds) - expected)}"
        )
    target = spin_one_basis()
    result = np.zeros((3, 3, 2, 2), dtype=np.complex128)

    def add(target_matrix: np.ndarray, gluon_matrix: np.ndarray) -> None:
        nonlocal result
        result += np.einsum("ab,ij->abij", target_matrix, gluon_matrix)

    add(target["U"], compose_unpolarized_gluon_correlator(
        momentum, mass, f1=tmds["f1"], h1perp=tmds["h1perp"]
    ))
    add(target["L"], compose_longitudinal_gluon_correlator(
        momentum, mass, 1.0, g1=tmds["g1"], h1Lperp=tmds["h1Lperp"]
    ))
    # The stored LL target basis is minus the physical S_LL convention.
    add(-target["LL"], compose_ll_gluon_correlator(
        momentum, mass, 1.0,
        f1LL=tmds["f1LL"], h1LLperp=tmds["h1LLperp"],
    ))

    channel_names = {
        TargetChannel.T: ("f1Tperp", "g1T", "h1", "h1Tperp"),
        TargetChannel.LT: ("f1LT", "g1LT", "h1LT", "h1LTperp"),
    }
    for channel, names in channel_names.items():
        for index, suffix in enumerate(("x", "y")):
            spin = [0.0, 0.0]
            spin[index] = 1.0
            polarization = GluonTargetPolarization(**{
                "spin_transverse" if channel == TargetChannel.T else "spin_lt":
                tuple(spin)
            })
            add(target[f"{channel.value}_{suffix}"],
                compose_polarized_gluon_correlator(
                    channel, momentum, mass, polarization,
                    {name: tmds[name] for name in names},
                ))

    tt_values = {
        "f1TT": tmds["f1TT_minus_h1TTperp"],
        "g1TT": tmds["g1TT"],
        "h1TT": tmds["h1TT"],
        "h1TTperp": 0.0,
        "h1TTperpperp": tmds["h1TTperpperp"],
    }
    for suffix, tensor in (
        ("x", ((1.0, 0.0), (0.0, -1.0))),
        ("y", ((0.0, 1.0), (1.0, 0.0))),
    ):
        add(target[f"TT_{suffix}"], compose_polarized_gluon_correlator(
            TargetChannel.TT, momentum, mass,
            GluonTargetPolarization(spin_tt=tensor), tt_values,
        ))
    return Spin1GluonCorrelator(result)


def project_to_allowed_spin1_gluon_basis(
    correlator: np.ndarray,
    momentum: np.ndarray | tuple[float, float],
    mass: float,
) -> tuple[Spin1GluonCorrelator, dict[str, float], float]:
    """Orthogonally project a numerical parent onto the allowed TMD basis.

    Finite nuclear quadratures and truncated impulse kernels can generate
    tiny components outside the hermiticity/parity leading-twist subspace.
    This representation-theoretic projection removes only that forbidden
    subspace.  The returned relative residual must be audited; a large value
    is a model failure, not something callers may silently discard.
    """

    values = np.asarray(correlator, dtype=np.complex128)
    if values.shape != (3, 3, 2, 2):
        raise ValueError("spin-1 gluon parent must have shape (3,3,2,2)")
    names = (
        "f1", "h1perp", "g1", "h1Lperp",
        "f1Tperp", "g1T", "h1", "h1Tperp",
        "f1LL", "h1LLperp", "f1LT", "g1LT", "h1LT", "h1LTperp",
        "f1TT_minus_h1TTperp", "g1TT", "h1TT", "h1TTperpperp",
    )
    columns = []
    for name in names:
        unit = {item: 0.0 for item in names}
        unit[name] = 1.0
        columns.append(
            compose_spin1_gluon_correlator(momentum, mass, unit).values.ravel()
        )
    design_complex = np.column_stack(columns)
    design = np.vstack((design_complex.real, design_complex.imag))
    target = np.concatenate((values.ravel().real, values.ravel().imag))
    coefficients, _, rank, _ = np.linalg.lstsq(design, target, rcond=None)
    if rank != len(names):
        raise ValueError("allowed spin-1 gluon basis is rank deficient")
    tmds = {name: float(value) for name, value in zip(names, coefficients)}
    projected = compose_spin1_gluon_correlator(momentum, mass, tmds)
    norm = float(np.linalg.norm(values))
    residual = float(np.linalg.norm(projected.values-values)/(norm or 1.0))
    return projected, tmds, residual
