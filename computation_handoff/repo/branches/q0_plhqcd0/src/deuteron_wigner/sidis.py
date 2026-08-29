"""Minimal rank-zero SIDIS structure functions."""

from __future__ import annotations

from typing import Callable, Mapping

import numpy as np
from scipy.integrate import simpson
from scipy.special import j0

DeuteronTMD = Callable[[int, float], complex]
FragmentationTMD = Callable[[int, float], complex]
CartesianTMD = Callable[[int, float, float], complex]


def rank_zero_sidis_structure(
    *,
    b: np.ndarray,
    p_h_t: float,
    z_h: float,
    flavors: tuple[int, ...],
    charges: Mapping[int, float],
    deuteron_tmd: DeuteronTMD,
    fragmentation_tmd: FragmentationTMD,
) -> float:
    """The radial W term of Eq. (106), without common hard prefactors."""

    b_axis = np.asarray(b, dtype=np.float64)
    if b_axis.ndim != 1 or len(b_axis) < 2 or not np.all(np.diff(b_axis) > 0.0):
        raise ValueError("b must be a strictly increasing one-dimensional axis")
    if p_h_t < 0.0 or not 0.0 < z_h <= 1.0:
        raise ValueError("require p_h_t >= 0 and 0 < z_h <= 1")
    integrand = np.zeros_like(b_axis, dtype=np.complex128)
    for flavor in flavors:
        if flavor not in charges:
            raise KeyError(f"missing electric charge for flavor {flavor}")
        integrand += charges[flavor] ** 2 * np.asarray(
            [
                deuteron_tmd(flavor, float(coordinate))
                * fragmentation_tmd(flavor, float(coordinate))
                for coordinate in b_axis
            ]
        )
    kernel = b_axis * j0(b_axis * p_h_t / z_h) / (2.0 * np.pi)
    result = simpson(kernel * integrand, x=b_axis)
    if abs(result.imag) > 1e-9 * max(1.0, abs(result.real)):
        raise ValueError("rank-zero SIDIS structure function has a significant imaginary part")
    return float(result.real)


def tensor_sidis_ratio(*, unpolarized: float, tensor_difference: float) -> float:
    """Convention-safe LL/U ratio using delta_T F rather than a named f1LL."""

    if unpolarized == 0.0:
        raise ZeroDivisionError("unpolarized SIDIS structure function vanishes")
    return float(tensor_difference / unpolarized)


def tensor_cos2phi_sidis_structure(
    *,
    x: float,
    p_axis: np.ndarray,
    p_h_x: float,
    p_h_y: float,
    z_h: float,
    target_mass: float,
    hadron_mass: float,
    flavors: tuple[int, ...],
    charges: Mapping[int, float],
    h1ll_perp: CartesianTMD,
    collins: CartesianTMD,
) -> float:
    """Leading-twist ``F_U(LL)^{cos(2 phi_h)}`` of EPJ A 61:81 Eq. (5d).

    The transverse delta function is used to set
    ``k_T=p_T-P_hT/z``. Common hard factors are not included.
    """

    axis = np.asarray(p_axis, dtype=np.float64)
    if axis.ndim != 1 or len(axis) < 3 or not np.all(np.diff(axis) > 0.0):
        raise ValueError("p_axis must be a strictly increasing 1D grid")
    if not 0.0 < x <= 1.0 or not 0.0 < z_h <= 1.0:
        raise ValueError("require 0 < x,z_h <= 1")
    if target_mass <= 0.0 or hadron_mass <= 0.0:
        raise ValueError("target and hadron masses must be positive")
    p_h = np.array([p_h_x, p_h_y], dtype=np.float64)
    p_h_norm = float(np.linalg.norm(p_h))
    if p_h_norm == 0.0:
        raise ValueError("cos(2 phi_h) requires nonzero hadron transverse momentum")
    h_hat = p_h / p_h_norm
    p_x, p_y = np.meshgrid(axis, axis, indexing="ij")
    k_x = p_x - p_h_x / z_h
    k_y = p_y - p_h_y / z_h
    weight = -(
        2.0 * (h_hat[0] * k_x + h_hat[1] * k_y)
        * (h_hat[0] * p_x + h_hat[1] * p_y)
        - (k_x * p_x + k_y * p_y)
    ) / (target_mass * hadron_mass)
    integrand = np.zeros_like(p_x, dtype=np.complex128)
    for flavor in flavors:
        try:
            charge = charges[flavor]
        except KeyError as exc:
            raise KeyError(f"missing electric charge for flavor {flavor}") from exc
        distribution = np.asarray(
            [[h1ll_perp(flavor, float(px), float(py)) for py in axis] for px in axis],
            dtype=np.complex128,
        )
        fragmentation = np.asarray(
            [
                [collins(flavor, float(kx), float(ky)) for kx, ky in zip(rx, ry)]
                for rx, ry in zip(k_x, k_y)
            ],
            dtype=np.complex128,
        )
        integrand += charge**2 * weight * distribution * fragmentation
    result = x * simpson(simpson(integrand, x=axis, axis=1), x=axis, axis=0)
    if abs(result.imag) > 1e-9 * max(1.0, abs(result.real)):
        raise ValueError("cos(2 phi_h) structure has a significant imaginary part")
    return float(result.real)
