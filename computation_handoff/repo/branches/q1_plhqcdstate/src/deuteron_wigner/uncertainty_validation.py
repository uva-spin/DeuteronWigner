"""Member-resolved validation helpers that preserve ensemble identity."""

from __future__ import annotations

import numpy as np

from .quark_correlator import Spin1QuarkCorrelator


def minimum_eigenvalues_under_component_replacement(
    central: Spin1QuarkCorrelator,
    component: Spin1QuarkCorrelator,
    central_coefficient: float,
    member_coefficients: np.ndarray,
) -> np.ndarray:
    """Return joint-density minima after replacing one linear TMD component.

    This evaluates the complete target-helicity x parton-spin density for
    every member without projecting or modifying the ensemble.  It is useful
    for diagnostics whose applicability can depend on factorization scheme:
    callers decide whether a negative value is a hard gate or a reported
    tension.
    """

    coefficients = np.asarray(member_coefficients, dtype=float)
    if coefficients.ndim != 1 or not np.isfinite(coefficients).all():
        raise ValueError("member coefficients must be one finite vector")
    central_density = central.quark_target_density_matrix()
    component_density = component.quark_target_density_matrix()
    density = (
        central_density[None, :, :]
        + (coefficients - float(central_coefficient))[:, None, None]
        * component_density[None, :, :]
    )
    return np.linalg.eigvalsh(density)[:, 0]


def minimum_eigenvalues_under_correlated_replacements(
    central: Spin1QuarkCorrelator,
    components: dict[str, Spin1QuarkCorrelator],
    central_coefficients: dict[str, float],
    member_coefficients: dict[str, np.ndarray],
) -> np.ndarray:
    """Replace several linear components with one shared member identity."""
    names = tuple(components)
    if (
        not names
        or set(names) != set(central_coefficients)
        or set(names) != set(member_coefficients)
    ):
        raise ValueError("components and coefficient maps must have identical keys")
    arrays = {name: np.asarray(member_coefficients[name], dtype=float) for name in names}
    shapes = {array.shape for array in arrays.values()}
    if len(shapes) != 1:
        raise ValueError("correlated member coefficients require equal vectors")
    shape = next(iter(shapes))
    if len(shape) != 1 or shape[0] < 1:
        raise ValueError("correlated member coefficients require equal vectors")
    if not all(np.isfinite(array).all() for array in arrays.values()):
        raise ValueError("correlated member coefficients must be finite")
    density = np.broadcast_to(
        central.quark_target_density_matrix(), (shape[0], 6, 6)
    ).copy()
    for name in names:
        shift = arrays[name] - float(central_coefficients[name])
        density += shift[:, None, None] * components[
            name
        ].quark_target_density_matrix()[None, :, :]
    return np.linalg.eigvalsh(density)[:, 0]
