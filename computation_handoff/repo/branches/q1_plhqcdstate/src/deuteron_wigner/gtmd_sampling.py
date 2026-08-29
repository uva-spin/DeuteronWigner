"""Efficient fixed-k sampling of the one-body spin-1 GTMD convolution."""

from __future__ import annotations

import numpy as np

from .gtmd_convolution import OffForwardSpinQuadrature, TransferMapping
from .gtmd_models import FactorizedGaussianGTMD
from .spin import HelicityMatrix


def deuteron_x_parent_to_nucleon_x(
    matrix: HelicityMatrix, *, x_nucleon: float, x_deuteron: float
) -> HelicityMatrix:
    """Convert a density in x_D to the per-nucleon x_N convention.

    For the standard ``x_N=2*x_D`` convention, density conservation gives
    ``q_N(x_N)=q_D(x_D)/2``.
    """

    if x_nucleon <= 0.0 or x_deuteron <= 0.0:
        raise ValueError("scaling variables must be positive")
    ratio = x_nucleon / x_deuteron
    return HelicityMatrix(matrix.values / ratio)


def convolve_factorized_gaussian_grid(
    *,
    x: float,
    k_x: np.ndarray,
    k_y: np.ndarray,
    scale: float,
    flavor: int,
    proton: FactorizedGaussianGTMD,
    neutron: FactorizedGaussianGTMD,
    quadrature: OffForwardSpinQuadrature,
    transfer_mapping: TransferMapping = TransferMapping.IDENTITY,
) -> HelicityMatrix:
    """Evaluate a complete Cartesian k-grid without a Python loop over nodes."""

    if not 0.0 < x <= 1.0:
        raise ValueError("x must lie in (0,1]")
    kx = np.asarray(k_x, dtype=np.float64)
    ky = np.asarray(k_y, dtype=np.float64)
    if kx.ndim != 1 or ky.ndim != 1:
        raise ValueError("k_x and k_y must be one-dimensional")
    result = np.zeros((len(kx), len(ky), 3, 3), dtype=np.complex128)
    kx_grid, ky_grid = np.meshgrid(kx, ky, indexing="ij")
    for y, p_x, p_y, weight, spectral in zip(
        quadrature.y,
        quadrature.p_x,
        quadrature.p_y,
        quadrature.weights,
        quadrature.spectral,
    ):
        if y < x:
            continue
        z = x / y
        delta_x, delta_y = transfer_mapping.nucleon_transfer(
            float(y), quadrature.delta_x, quadrature.delta_y
        )
        scalar = proton.scalar(
            flavor, z, kx_grid - z * p_x, ky_grid - z * p_y,
            delta_x, delta_y, scale
        ) + neutron.scalar(
            flavor, z, kx_grid - z * p_x, ky_grid - z * p_y,
            delta_x, delta_y, scale
        )
        # I_2/2 nucleon correlator: trace the active-nucleon indices.
        target = np.einsum("IHaa->IH", spectral) / 2.0
        result += weight * scalar[..., None, None] * target / y
    return HelicityMatrix(result)


def convolve_factorized_gaussian_gpd(
    *,
    x: float,
    scale: float,
    flavor: int,
    proton: FactorizedGaussianGTMD,
    neutron: FactorizedGaussianGTMD,
    quadrature: OffForwardSpinQuadrature,
    transfer_mapping: TransferMapping = TransferMapping.IDENTITY,
) -> HelicityMatrix:
    """Analytic k_T marginal of :func:`convolve_factorized_gaussian_grid`."""

    result = np.zeros((3, 3), dtype=np.complex128)
    for y, weight, spectral in zip(
        quadrature.y, quadrature.weights, quadrature.spectral
    ):
        if y < x:
            continue
        z = x / y
        delta_x, delta_y = transfer_mapping.nucleon_transfer(
            float(y), quadrature.delta_x, quadrature.delta_y
        )
        scalar = proton.collinear(
            flavor, z, delta_x, delta_y, scale
        ) + neutron.collinear(flavor, z, delta_x, delta_y, scale)
        result += weight * scalar * np.einsum("IHaa->IH", spectral) / (2.0 * y)
    return HelicityMatrix(result)
