"""Direct, convention-aware two-dimensional Fourier transforms."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy.integrate import simpson
from scipy.special import jv

from .conventions import (
    FourierConvention,
    GTMD_IMAGING_CONVENTION,
    TMD_EVOLUTION_CONVENTION,
)
from .kinematics import BDelta, BTMD


def _validate_axes(x_axis: np.ndarray, y_axis: np.ndarray, values: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    x = np.asarray(x_axis, dtype=np.float64)
    y = np.asarray(y_axis, dtype=np.float64)
    if x.ndim != 1 or y.ndim != 1 or len(x) < 2 or len(y) < 2:
        raise ValueError("Fourier axes must be one-dimensional with at least two points")
    if not np.all(np.diff(x) > 0.0) or not np.all(np.diff(y) > 0.0):
        raise ValueError("Fourier axes must be strictly increasing")
    if values.shape[:2] != (len(x), len(y)):
        raise ValueError("values must begin with the two Fourier-axis dimensions")
    return x, y


def direct_fourier_2d(
    x_axis: np.ndarray,
    y_axis: np.ndarray,
    values: np.ndarray,
    coordinate_points: np.ndarray,
    convention: FourierConvention,
) -> np.ndarray:
    """Evaluate a continuous 2D transform by Simpson quadrature.

    ``values`` has shape ``(nx, ny, ...)`` and points have shape ``(n, 2)``.
    The result has shape ``(n, ...)``.
    """

    array = np.asarray(values, dtype=np.complex128)
    x, y = _validate_axes(x_axis, y_axis, array)
    points = np.asarray(coordinate_points, dtype=np.float64)
    if points.ndim != 2 or points.shape[1] != 2:
        raise ValueError("coordinate_points must have shape (n, 2)")
    x_grid, y_grid = np.meshgrid(x, y, indexing="ij")
    outputs = []
    for point in points:
        phase = np.exp(
            1j
            * convention.forward_sign
            * (x_grid * point[0] + y_grid * point[1])
        )
        phased = array * phase[(...,) + (None,) * (array.ndim - 2)]
        integrated_y = simpson(phased, x=y, axis=1)
        integrated = simpson(integrated_y, x=x, axis=0)
        outputs.append(convention.forward_normalization * integrated)
    return np.asarray(outputs)


def gtmd_to_wigner(
    delta_x: np.ndarray,
    delta_y: np.ndarray,
    values: np.ndarray,
    points: list[BDelta],
) -> np.ndarray:
    coordinates = np.asarray([point.array() for point in points])
    return direct_fourier_2d(
        delta_x,
        delta_y,
        values,
        coordinates,
        GTMD_IMAGING_CONVENTION,
    )


def tmd_to_b_space(
    k_x: np.ndarray,
    k_y: np.ndarray,
    values: np.ndarray,
    points: list[BTMD],
) -> np.ndarray:
    coordinates = np.asarray([point.array() for point in points])
    return direct_fourier_2d(
        k_x,
        k_y,
        values,
        coordinates,
        TMD_EVOLUTION_CONVENTION,
    )


def bessel_b_to_k(
    b: np.ndarray,
    values: np.ndarray,
    k: np.ndarray,
    *,
    rank: int = 0,
    rank_normalization: float = 1.0,
) -> np.ndarray:
    """Radial Fourier--Bessel transform of Eq. (102).

    For rank zero this is
    ``F(k) = integral b db J0(b k) F_tilde(b) / (2 pi)``.
    Higher ranks require an explicitly supplied convention normalization.
    """

    b_axis = np.asarray(b, dtype=np.float64)
    k_axis = np.asarray(k, dtype=np.float64)
    array = np.asarray(values, dtype=np.complex128)
    if b_axis.ndim != 1 or len(b_axis) < 2 or not np.all(np.diff(b_axis) > 0.0):
        raise ValueError("b must be a strictly increasing one-dimensional axis")
    if k_axis.ndim != 1 or np.any(k_axis < 0.0):
        raise ValueError("k must be a nonnegative one-dimensional axis")
    if array.shape[0] != len(b_axis):
        raise ValueError("values first dimension must match b")
    if rank < 0:
        raise ValueError("rank cannot be negative")
    outputs = []
    for momentum in k_axis:
        kernel = b_axis * jv(rank, b_axis * momentum) / (2.0 * np.pi)
        outputs.append(
            rank_normalization
            * simpson(
                array * kernel[(...,) + (None,) * (array.ndim - 1)],
                x=b_axis,
                axis=0,
            )
        )
    return np.asarray(outputs)


def bessel_k_to_b(
    k: np.ndarray,
    values: np.ndarray,
    b: np.ndarray,
    *,
    rank: int = 0,
    rank_normalization: float = 1.0,
) -> np.ndarray:
    """Inverse radial transform of Eq. (103)."""

    k_axis = np.asarray(k, dtype=np.float64)
    b_axis = np.asarray(b, dtype=np.float64)
    array = np.asarray(values, dtype=np.complex128)
    if k_axis.ndim != 1 or len(k_axis) < 2 or not np.all(np.diff(k_axis) > 0.0):
        raise ValueError("k must be a strictly increasing one-dimensional axis")
    if b_axis.ndim != 1 or np.any(b_axis < 0.0):
        raise ValueError("b must be a nonnegative one-dimensional axis")
    if array.shape[0] != len(k_axis):
        raise ValueError("values first dimension must match k")
    if rank < 0:
        raise ValueError("rank cannot be negative")
    if rank_normalization == 0.0:
        raise ValueError("rank_normalization cannot vanish")
    outputs = []
    for coordinate in b_axis:
        kernel = 2.0 * np.pi * k_axis * jv(rank, k_axis * coordinate)
        outputs.append(
            simpson(
                array * kernel[(...,) + (None,) * (array.ndim - 1)],
                x=k_axis,
                axis=0,
            )
            / rank_normalization
        )
    return np.asarray(outputs)


@dataclass(frozen=True)
class GluonTMDKSpace:
    """Momentum-space scalars in the project's Cartesian correlator convention."""

    f1: np.ndarray
    g1: np.ndarray
    h1perp: np.ndarray


@dataclass(frozen=True)
class RankZeroQuarkTMDKSpace:
    """Momentum-space rank-zero quark scalars in the project convention."""

    f1: np.ndarray
    g1: np.ndarray
    h1: np.ndarray


def rank_zero_quark_tmd_b_to_k(
    b: np.ndarray,
    f1_b: np.ndarray,
    g1_b: np.ndarray,
    h1_b: np.ndarray,
    k: np.ndarray,
) -> RankZeroQuarkTMDKSpace:
    """Apply the common J0 transform to the three rank-zero quark TMDs."""

    return RankZeroQuarkTMDKSpace(
        f1=bessel_b_to_k(b, f1_b, k, rank=0),
        g1=bessel_b_to_k(b, g1_b, k, rank=0),
        h1=bessel_b_to_k(b, h1_b, k, rank=0),
    )


def gluon_tmd_b_to_k(
    b: np.ndarray,
    f1_b: np.ndarray,
    g1_b: np.ndarray,
    h1perp_b: np.ndarray,
    k: np.ndarray,
    *,
    nucleon_mass: float,
) -> GluonTMDKSpace:
    """Transform b-space gluon TMDs into the project k-space convention.

    The source convention, arXiv:1907.03780 Eqs. (2.6)-(2.8), has
    ``h_paper(k) = - integral b db J2(bk) h(b)/(2 pi)``.  The Cartesian
    correlator used by :func:`compose_unpolarized_gluon_correlator` instead
    multiplies ``k_T^{ij} h_project(k)/(2 M^2)``.  Therefore
    ``h_project(k)=2 M^2 h_paper(k)/k^2``.  The k=0 value is evaluated from
    the analytic J2(z)/z^2 limit.
    """

    if nucleon_mass <= 0.0:
        raise ValueError("nucleon_mass must be positive")
    b_axis = np.asarray(b, dtype=np.float64)
    k_axis = np.asarray(k, dtype=np.float64)
    h_b = np.asarray(h1perp_b, dtype=np.complex128)
    f_k = bessel_b_to_k(b_axis, f1_b, k_axis, rank=0)
    g_k = bessel_b_to_k(b_axis, g1_b, k_axis, rank=0)
    h_paper = -bessel_b_to_k(b_axis, h_b, k_axis, rank=2)
    h_project = np.empty_like(h_paper)
    nonzero = k_axis > 0.0
    h_project[nonzero] = (
        2.0 * nucleon_mass**2 * h_paper[nonzero] / k_axis[nonzero] ** 2
    )
    if np.any(~nonzero):
        limit = (
            -nucleon_mass**2
            / 4.0
            * simpson(
                b_axis**3
                * h_b
                / (2.0 * np.pi),
                x=b_axis,
                axis=0,
            )
        )
        h_project[~nonzero] = limit
    return GluonTMDKSpace(f1=f_k, g1=g_k, h1perp=h_project)
