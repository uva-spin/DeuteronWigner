"""Explicit exploratory action for the first C117 direction.

The C410 aggregate is a real source-reduced finite-basis shape, but the
source-qualified C260/C262 field, state, wave-packet, and finite-C43
normalization has not been supplied. This module therefore provides a
deliberately Lane-A interface for response studies. Every unresolved factor
is caller-supplied and every result is permanently marked EXPLORATORY.

Only the first C117 source direction is available at C410. A scalar mixing
coefficient is consequently used for that direction rather than silently
creating a four-by-four physical mixing matrix.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite, pi
from numbers import Real
from typing import Any, Mapping

import numpy as np
from scipy.sparse import csr_matrix

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import (
    RESOLUTION_LABELS,
    content_root,
)
from deuteron_wigner.bridge.c410_c117_i2_retained_aggregation_boundary import (
    source_reduced_c117_i2_shape_csr,
)

K2_BY_RESOLUTION = {"K9": 9, "K11": 11, "K13": 13}
EXPLORATORY_CLAIM_TIER = "EXPLORATORY"
UNAVAILABLE_SOURCE_DIRECTIONS = (
    "derivative_density",
    "CM_ground",
    "triplet_projected",
)


def _check_resolution(resolution: str) -> str:
    if resolution not in RESOLUTION_LABELS:
        raise ValueError("unsupported C117 exploratory resolution")
    return resolution


def _finite_nonzero(value: Any, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{name} must be a finite nonzero real number")
    numeric = float(value)
    if not isfinite(numeric) or numeric == 0.0:
        raise ValueError(f"{name} must be a finite nonzero real number")
    return numeric


@dataclass(frozen=True)
class ExploratoryC1171Parameters:
    """Caller-owned residual factors for an exploratory action."""

    resolution: str
    residual_normalization: float
    mixing_coefficient: float

    def __post_init__(self) -> None:
        _check_resolution(self.resolution)
        _finite_nonzero(self.residual_normalization, "residual_normalization")
        _finite_nonzero(self.mixing_coefficient, "mixing_coefficient")

    @property
    def scalar(self) -> float:
        return float(self.residual_normalization) * float(self.mixing_coefficient)


def pminus_to_m2_factor(resolution: str, half_length_GeVinv: float) -> float:
    """Return the exact finite-cell factor multiplying a P-minus variation.

    The executable convention uses x-minus in [-L,L] and K2=2K. Thus
    2 P-plus = 2 pi K/L = pi K2/L. The half-cell length is required
    explicitly so no hidden cell convention can enter.
    """

    resolution = _check_resolution(resolution)
    if half_length_GeVinv == 0.0:
        raise ValueError("half_length_GeVinv must be positive")
    length = _finite_nonzero(half_length_GeVinv, "half_length_GeVinv")
    if length <= 0.0:
        raise ValueError("half_length_GeVinv must be positive")
    return pi * float(K2_BY_RESOLUTION[resolution]) / length


def exploratory_parameter_record(
    parameters: ExploratoryC1171Parameters,
) -> Mapping[str, Any]:
    """Describe the assumptions used by an exploratory action."""

    source = source_reduced_c117_i2_shape_csr(parameters.resolution)
    payload = {
        "schema": "C411-C117-I2-EXPLORATORY-ACTION-PARAMETERS-V1",
        "claim_tier": EXPLORATORY_CLAIM_TIER,
        "physical": False,
        "resolution": parameters.resolution,
        "source_direction": "I2_density_projector",
        "source_shape": "C410.source_reduced_c117_i2_shape",
        "source_shape_units": "GeV^2",
        "source_shape_nnz": int(source.nnz),
        "residual_normalization": float(parameters.residual_normalization),
        "first_direction_mixing_coefficient": float(parameters.mixing_coefficient),
        "effective_scalar": parameters.scalar,
        "mixing_scope": "first_available_source_direction_only",
        "unavailable_source_directions": UNAVAILABLE_SOURCE_DIRECTIONS,
        "source_minus_one_half_applied_once": True,
        "g_s_squared": "FACTORED_NOT_NUMERIC",
        "c_C117_1": "EXTERNAL_TO_DERIVATIVE_ACTION",
        "Pminus_to_M2": {
            "formula": "delta M^2 = 2*pi*K/L * delta P^-",
            "K2": K2_BY_RESOLUTION[parameters.resolution],
            "applied_to_C410_shape": False,
            "reason": "C410 source shape is labeled GeV^2; conversion ownership remains explicit",
        },
        "physical_fit_authorized": False,
        "hamiltonian_activation": False,
    }
    return {**payload, "root": content_root(payload)}


def exploratory_c117_1_csr(
    parameters: ExploratoryC1171Parameters,
) -> csr_matrix:
    """Return the explicitly scaled C410 exploratory action."""

    source = source_reduced_c117_i2_shape_csr(parameters.resolution)
    return (parameters.scalar * source).tocsr()


def apply_exploratory_c117_1(
    parameters: ExploratoryC1171Parameters, vector: Any
) -> np.ndarray:
    """Apply the exploratory action with strict input checks."""

    matrix = exploratory_c117_1_csr(parameters)
    values = np.asarray(vector, dtype=np.complex128)
    if values.shape != (matrix.shape[1],):
        raise ValueError("vector has the wrong exploratory C117 direct-sum dimension")
    if not np.all(np.isfinite(values)):
        raise ValueError("vector contains nonfinite entries")
    return matrix @ values


def exploratory_action_record(
    parameters: ExploratoryC1171Parameters,
) -> Mapping[str, Any]:
    """Return action metadata without promoting it to C411 authority."""

    matrix = exploratory_c117_1_csr(parameters)
    parameter_record = exploratory_parameter_record(parameters)
    payload = {
        "schema": "C411-C117-I2-EXPLORATORY-ACTION-V1",
        "claim_tier": EXPLORATORY_CLAIM_TIER,
        "physical": False,
        "resolution": parameters.resolution,
        "shape": tuple(matrix.shape),
        "nnz": int(matrix.nnz),
        "hermitian": bool(np.linalg.norm((matrix - matrix.getH()).data) == 0.0),
        "source_parameter_root": parameter_record["root"],
        "complete_C117_numerical_coordinate_action": False,
        "C411_certificate_supplied": False,
        "physical_fit_authorized": False,
        "hamiltonian_activation": False,
    }
    return {**payload, "root": content_root(payload)}


__all__ = [
    "K2_BY_RESOLUTION",
    "EXPLORATORY_CLAIM_TIER",
    "UNAVAILABLE_SOURCE_DIRECTIONS",
    "ExploratoryC1171Parameters",
    "pminus_to_m2_factor",
    "exploratory_parameter_record",
    "exploratory_c117_1_csr",
    "apply_exploratory_c117_1",
    "exploratory_action_record",
]
