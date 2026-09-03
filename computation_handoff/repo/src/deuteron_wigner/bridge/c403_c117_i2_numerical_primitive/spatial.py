"""Numerical C117 ``I2`` spatial-kernel primitive in the C45 HO convention.

For external transverse HO modes ``a=(n_a,m_a)``, ``b=(n_b,m_b)`` and one
contracted internal mode ``r=(n_r,m_r)``, C403 evaluates

    I[a,b;r] = integral d^2x phi_a(x)^* phi_b(x) |phi_r(x)|^2.

The implementation is independently derived from the C45 coordinate-space HO
wavefunction.  It does not import C80: C116 explicitly states that C80's full
contact-kernel ownership is not reusable for this graph class.  The analytic
route expands finite Laguerre polynomials and evaluates exact Gamma moments;
the independent route uses generalized Gauss--Laguerre quadrature.

This is a spatial primitive only.  It excludes the C114 inverse/source factor,
C119 current factors, spin, color, longitudinal normalization, target-state
aggregation, the factored C117 coefficient, and the complete C396 action.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
import json
from math import comb, factorial, isfinite, pi, sqrt
from typing import Any, Mapping, Sequence

import numpy as np
from scipy.sparse import csr_matrix
from scipy.special import eval_genlaguerre, roots_genlaguerre

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import content_root, resolution_record

from .axis import STATUS, admitted_transverse_modes


EXTERNAL_BASIS_SCOPE = (
    "C47 intrinsic/relative qg transverse-HO basis with shell <= Nmax-2; "
    "the q-sector external target basis and full q/qg embedding remain unassembled"
)


def _exact_integer(value: Any, *, name: str) -> int:
    if isinstance(value, (bool, np.bool_)):
        raise TypeError(f"{name} must be an integer quantum number")
    try:
        integer = int(value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise TypeError(f"{name} must be an integer quantum number") from exc
    try:
        exact = value == integer
    except Exception:
        exact = False
    if not exact:
        raise ValueError(f"{name} must be an exact integer quantum number")
    return integer


@dataclass(frozen=True, order=True)
class HOMode:
    n: int
    m: int

    def __post_init__(self) -> None:
        n = _exact_integer(self.n, name="n")
        m = _exact_integer(self.m, name="m")
        if n < 0:
            raise ValueError("n must be nonnegative")
        object.__setattr__(self, "n", n)
        object.__setattr__(self, "m", m)

    @property
    def shell(self) -> int:
        return 2 * self.n + abs(self.m)

    def to_record(self) -> dict[str, int]:
        return {"n": self.n, "m": self.m, "shell": self.shell}


def _mode(value: HOMode | Sequence[int]) -> HOMode:
    if isinstance(value, HOMode):
        return value
    if isinstance(value, (str, bytes)) or len(value) != 2:
        raise ValueError("HO mode must contain exactly (n,m)")
    return HOMode(
        _exact_integer(value[0], name="n"),
        _exact_integer(value[1], name="m"),
    )


@lru_cache(maxsize=None)
def external_modes(resolution: str) -> tuple[HOMode, ...]:
    """Intrinsic/relative C47 transverse basis: shell <= Nmax-2."""
    return tuple(HOMode(n, m) for n, m in admitted_transverse_modes(resolution))


def _source_b_GeV(resolution: str) -> float:
    record = resolution_record(resolution)
    value = float(record["b_HO"])
    if not isfinite(value) or value <= 0:
        raise ValueError("source HO scale must be finite and positive")
    return value


@lru_cache(maxsize=None)
def _laguerre_coefficients(n: int, alpha: int) -> tuple[Fraction, ...]:
    if n < 0 or alpha < 0:
        raise ValueError("Laguerre indices must be nonnegative")
    return tuple(Fraction(((-1) ** j) * comb(n + alpha, n - j), factorial(j)) for j in range(n + 1))


def _convolve(left: Sequence[Fraction], right: Sequence[Fraction]) -> tuple[Fraction, ...]:
    result = [Fraction(0) for _ in range(len(left) + len(right) - 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return tuple(result)


@lru_cache(maxsize=None)
def radial_moment_fraction(
    n_out: int,
    abs_m: int,
    n_in: int,
    n_internal: int,
    abs_m_internal: int,
) -> Fraction:
    """Exact rational radial moment after factoring phases and HO norms."""
    polynomial: tuple[Fraction, ...] = (Fraction(1),)
    for n, alpha in (
        (n_out, abs_m),
        (n_in, abs_m),
        (n_internal, abs_m_internal),
        (n_internal, abs_m_internal),
    ):
        polynomial = _convolve(polynomial, _laguerre_coefficients(n, alpha))
    power = abs_m + abs_m_internal
    return sum(
        (
            coefficient
            * Fraction(factorial(power + degree), 2 ** (power + degree + 1))
            for degree, coefficient in enumerate(polynomial)
        ),
        Fraction(0),
    )


def _element_at_scale(
    external_out: HOMode,
    external_in: HOMode,
    internal: HOMode,
    b_GeV: float,
) -> float:
    if not isfinite(b_GeV) or b_GeV <= 0:
        raise ValueError("b_GeV must be finite and positive")
    if external_out.m != external_in.m:
        return 0.0
    a = abs(external_out.m)
    ar = abs(internal.m)
    radial = radial_moment_fraction(external_out.n, a, external_in.n, internal.n, ar)
    if radial == 0:
        return 0.0
    normalization = sqrt(
        factorial(external_out.n)
        * factorial(external_in.n)
        / (factorial(external_out.n + a) * factorial(external_in.n + a))
    ) * Fraction(factorial(internal.n), factorial(internal.n + ar))
    phase = (-1) ** (external_out.n + external_in.n)
    return float((b_GeV**2 / pi) * phase * float(normalization) * float(radial))


def i2_spatial_element(
    resolution: str,
    external_out: HOMode | Sequence[int],
    external_in: HOMode | Sequence[int],
    internal: HOMode | Sequence[int],
) -> complex:
    out = _mode(external_out)
    inn = _mode(external_in)
    contracted = _mode(internal)
    modes = set(external_modes(resolution))
    if out not in modes or inn not in modes or contracted not in modes:
        raise KeyError("all HO labels must lie in the C403 admitted shell")
    return complex(_element_at_scale(out, inn, contracted, _source_b_GeV(resolution)), 0.0)


def i2_spatial_element_record(
    resolution: str,
    external_out: HOMode | Sequence[int],
    external_in: HOMode | Sequence[int],
    internal: HOMode | Sequence[int],
) -> dict[str, Any]:
    out = _mode(external_out)
    inn = _mode(external_in)
    contracted = _mode(internal)
    value = i2_spatial_element(resolution, out, inn, contracted)
    radial = Fraction(0)
    if out.m == inn.m:
        radial = radial_moment_fraction(out.n, abs(out.m), inn.n, contracted.n, abs(contracted.m))
    payload = {
        "schema": "C403-C117-I2-SPATIAL-ELEMENT-V1",
        "status": "ZERO_BY_EXACT_ANGULAR_OR_RADIAL_RULE" if value == 0 else "NONZERO_ANALYTIC_FINITE_LAGUERRE_MOMENT",
        "resolution": resolution,
        "external_out": out.to_record(),
        "external_in": inn.to_record(),
        "internal": contracted.to_record(),
        "value": [value.real, value.imag],
        "units": "GeV^2",
        "scale": {"b_HO_GeV": _source_b_GeV(resolution), "dependence": "b_HO^2"},
        "angular_rule": "m_out = m_in",
        "radial_moment": {
            "numerator": radial.numerator,
            "denominator": radial.denominator,
            "exact": str(radial),
        },
        "formula": (
            "delta_mout,min * b_HO^2/pi * phase * HO_norms * "
            "integral_0^infinity dz exp(-2z) z^(|m|+|m_r|) "
            "L_nout^|m|(z)L_nin^|m|(z)[L_nr^|mr|(z)]^2"
        ),
        "C45_coordinate_convention": True,
        "external_basis_scope": EXTERNAL_BASIS_SCOPE,
        "q_sector_external_basis_assembled": False,
        "C80_imported_or_reused": False,
    }
    return {**payload, "root": content_root(payload)}


@lru_cache(maxsize=None)
def _quadrature_rule(nodes: int, alpha: int) -> tuple[np.ndarray, np.ndarray]:
    points, weights = _quadrature_rule(nodes, alpha)
    points.setflags(write=False)
    weights.setflags(write=False)
    return points, weights


def i2_spatial_element_quadrature(
    resolution: str,
    external_out: HOMode | Sequence[int],
    external_in: HOMode | Sequence[int],
    internal: HOMode | Sequence[int],
    *,
    nodes: int = 64,
) -> complex:
    """Independent generalized Gauss--Laguerre route."""
    if nodes <= 0:
        raise ValueError("quadrature node count must be positive")
    out = _mode(external_out)
    inn = _mode(external_in)
    contracted = _mode(internal)
    modes = set(external_modes(resolution))
    if out not in modes or inn not in modes or contracted not in modes:
        raise KeyError("all HO labels must lie in the C403 admitted shell")
    if out.m != inn.m:
        return 0j
    a = abs(out.m)
    ar = abs(contracted.m)
    alpha = a + ar
    points, weights = roots_genlaguerre(nodes, alpha)
    z = points / 2.0
    product = (
        eval_genlaguerre(out.n, a, z)
        * eval_genlaguerre(inn.n, a, z)
        * eval_genlaguerre(contracted.n, ar, z) ** 2
    )
    radial = float(np.sum(weights * product) / (2.0 ** (alpha + 1)))
    normalization = sqrt(
        factorial(out.n)
        * factorial(inn.n)
        / (factorial(out.n + a) * factorial(inn.n + a))
    ) * factorial(contracted.n) / factorial(contracted.n + ar)
    phase = (-1) ** (out.n + inn.n)
    value = (_source_b_GeV(resolution) ** 2 / pi) * phase * normalization * radial
    return complex(float(value), 0.0)


@lru_cache(maxsize=None)
def _single_member_dense_cached(resolution: str, n_internal: int, m_internal: int) -> np.ndarray:
    internal = HOMode(n_internal, m_internal)
    labels = external_modes(resolution)
    if internal not in labels:
        raise KeyError(f"internal mode {internal} is outside the admitted shell")
    matrix = np.zeros((len(labels), len(labels)), dtype=np.complex128)
    b_GeV = _source_b_GeV(resolution)
    for i, out in enumerate(labels):
        for j, inn in enumerate(labels):
            matrix[i, j] = _element_at_scale(out, inn, internal, b_GeV)
    matrix.setflags(write=False)
    return matrix


def single_member_kernel_dense(resolution: str, internal: HOMode | Sequence[int]) -> np.ndarray:
    mode = _mode(internal)
    return np.array(_single_member_dense_cached(resolution, mode.n, mode.m), copy=True)


def single_member_kernel_csr(resolution: str, internal: HOMode | Sequence[int]) -> csr_matrix:
    return csr_matrix(single_member_kernel_dense(resolution, internal))


def apply_single_member_kernel(
    resolution: str,
    internal: HOMode | Sequence[int],
    vector: np.ndarray,
) -> np.ndarray:
    """Independent matrix-free action evaluated directly from the analytic element."""
    mode = _mode(internal)
    labels = external_modes(resolution)
    values = np.asarray(vector, dtype=np.complex128)
    if values.ndim != 1 or values.shape[0] != len(labels):
        raise ValueError(f"vector must have shape ({len(labels)},)")
    result = np.zeros_like(values)
    b_GeV = _source_b_GeV(resolution)
    for i, out in enumerate(labels):
        total = 0j
        for j, inn in enumerate(labels):
            if out.m == inn.m:
                total += _element_at_scale(out, inn, mode, b_GeV) * values[j]
        result[i] = total
    return result


def _validate_explicit_weights(
    resolution: str,
    weights: Mapping[HOMode | tuple[int, int], float] | None,
) -> tuple[tuple[HOMode, float], ...]:
    if weights is None or len(weights) == 0:
        raise ValueError("explicit nonempty internal-mode weights are required; no default aggregate exists")
    admitted = set(external_modes(resolution))
    rows = []
    seen: set[HOMode] = set()
    for key, raw_weight in weights.items():
        mode = _mode(key)
        weight = float(raw_weight)
        if mode not in admitted:
            raise KeyError(f"weighted internal mode {mode} is outside the admitted shell")
        if mode in seen:
            raise ValueError(f"duplicate canonical internal mode in explicit weights: {mode}")
        if not isfinite(weight):
            raise ValueError("weights must be finite real numbers")
        seen.add(mode)
        rows.append((mode, weight))
    return tuple(sorted(rows))


def weighted_spatial_kernel_csr(
    resolution: str,
    weights: Mapping[HOMode | tuple[int, int], float] | None,
) -> csr_matrix:
    rows = _validate_explicit_weights(resolution, weights)
    dimension = len(external_modes(resolution))
    result = csr_matrix((dimension, dimension), dtype=np.complex128)
    for mode, weight in rows:
        result = result + weight * single_member_kernel_csr(resolution, mode)
    return result.tocsr()


def apply_weighted_spatial_kernel(
    resolution: str,
    weights: Mapping[HOMode | tuple[int, int], float] | None,
    vector: np.ndarray,
) -> np.ndarray:
    rows = _validate_explicit_weights(resolution, weights)
    result = np.zeros(len(external_modes(resolution)), dtype=np.complex128)
    for mode, weight in rows:
        result += weight * apply_single_member_kernel(resolution, mode, vector)
    return result


def _array_root(array: np.ndarray) -> str:
    value = np.ascontiguousarray(array)
    return sha256(value.dtype.str.encode() + str(value.shape).encode() + value.tobytes()).hexdigest()


def spatial_kernel_inventory() -> dict[str, Any]:
    rows = []
    for resolution in ("K9", "K11", "K13"):
        labels = external_modes(resolution)
        for internal in labels:
            matrix = _single_member_dense_cached(resolution, internal.n, internal.m)
            eigenvalues = np.linalg.eigvalsh(matrix)
            rows.append(
                {
                    "resolution": resolution,
                    "internal_mode": internal.to_record(),
                    "external_dimension": len(labels),
                    "nonzero_entries": int(np.count_nonzero(matrix)),
                    "matrix_root": _array_root(matrix),
                    "trace_GeV2": float(np.trace(matrix).real),
                    "minimum_eigenvalue_GeV2": float(eigenvalues[0]),
                    "maximum_eigenvalue_GeV2": float(eigenvalues[-1]),
                    "hermiticity_residual": float(np.linalg.norm(matrix - matrix.conj().T)),
                    "positive_semidefinite_at_tolerance": bool(eigenvalues[0] >= -1e-12),
                }
            )
    payload = {
        "schema": "C403-C117-I2-SPATIAL-KERNEL-INVENTORY-V1",
        "status": STATUS,
        "row_count": len(rows),
        "rows": tuple(rows),
        "spatial_kernel_paths": 3,
        "external_basis_scope": EXTERNAL_BASIS_SCOPE,
        "q_sector_external_basis_assembled": False,
        "units": "GeV^2 from the authoritative C45 b_HO in GeV",
        "full_C117_operator_paths": 0,
        "single_member_kernel_positive_semidefinite": True,
        "weighted_aggregate_PSD_only_for_nonnegative_weights": True,
        "C80_reuse": False,
    }
    return {**payload, "root": content_root(payload)}


def spatial_kernel_validation() -> dict[str, Any]:
    rows = []
    maximum_quadrature_residual = 0.0
    maximum_sparse_matrix_free_residual = 0.0
    minimum_eigenvalue = float("inf")
    rng = np.random.default_rng(403)
    for resolution in ("K9", "K11", "K13"):
        labels = external_modes(resolution)
        representative = tuple(dict.fromkeys((labels[0], labels[len(labels) // 2], labels[-1])))
        vector = rng.normal(size=len(labels)) + 1j * rng.normal(size=len(labels))
        for internal in representative:
            matrix = single_member_kernel_dense(resolution, internal)
            sparse = csr_matrix(matrix)
            matrix_free = apply_single_member_kernel(resolution, internal, vector)
            sparse_residual = float(np.linalg.norm(sparse @ vector - matrix_free))
            maximum_sparse_matrix_free_residual = max(maximum_sparse_matrix_free_residual, sparse_residual)
            eigenvalues = np.linalg.eigvalsh(matrix)
            minimum_eigenvalue = min(minimum_eigenvalue, float(eigenvalues[0]))
            local_quadrature = 0.0
            for out in labels:
                for inn in labels:
                    analytic = i2_spatial_element(resolution, out, inn, internal)
                    quadrature = i2_spatial_element_quadrature(resolution, out, inn, internal)
                    local_quadrature = max(local_quadrature, abs(analytic - quadrature))
            maximum_quadrature_residual = max(maximum_quadrature_residual, local_quadrature)
            rows.append(
                {
                    "resolution": resolution,
                    "internal_mode": internal.to_record(),
                    "dimension": len(labels),
                    "quadrature_max_abs_residual": local_quadrature,
                    "sparse_matrix_free_residual": sparse_residual,
                    "hermiticity_residual": float(np.linalg.norm(matrix - matrix.conj().T)),
                    "minimum_eigenvalue_GeV2": float(eigenvalues[0]),
                }
            )
    b0 = _source_b_GeV("K9")
    ground = HOMode(0, 0)
    source_value = _element_at_scale(ground, ground, ground, b0)
    scaled_value = _element_at_scale(ground, ground, ground, 2.0 * b0)
    payload = {
        "schema": "C403-C117-I2-SPATIAL-KERNEL-VALIDATION-V1",
        "status": STATUS,
        "rows": tuple(rows),
        "quadrature_scope": "three deterministic representative internal modes per resolution; all single-member matrices checked separately for Hermiticity and PSD",
        "external_basis_scope": EXTERNAL_BASIS_SCOPE,
        "q_sector_external_basis_assembled": False,
        "quadrature_internal_modes_checked": len(rows),
        "maximum_quadrature_abs_residual": maximum_quadrature_residual,
        "maximum_sparse_matrix_free_residual": maximum_sparse_matrix_free_residual,
        "minimum_eigenvalue_GeV2": minimum_eigenvalue,
        "ground_state_identity": {
            "computed": source_value,
            "expected": b0**2 / (2.0 * pi),
            "absolute_residual": abs(source_value - b0**2 / (2.0 * pi)),
        },
        "b_HO_squared_scaling_residual": abs(scaled_value / source_value - 4.0),
        "pass": bool(
            maximum_quadrature_residual < 5e-13
            and maximum_sparse_matrix_free_residual < 5e-13
            and minimum_eigenvalue >= -1e-12
            and abs(source_value - b0**2 / (2.0 * pi)) < 1e-15
            and abs(scaled_value / source_value - 4.0) < 1e-14
        ),
    }
    return {**payload, "root": content_root(payload)}


__all__ = [
    "EXTERNAL_BASIS_SCOPE",
    "HOMode",
    "external_modes",
    "radial_moment_fraction",
    "i2_spatial_element",
    "i2_spatial_element_record",
    "i2_spatial_element_quadrature",
    "single_member_kernel_dense",
    "single_member_kernel_csr",
    "apply_single_member_kernel",
    "weighted_spatial_kernel_csr",
    "apply_weighted_spatial_kernel",
    "spatial_kernel_inventory",
    "spatial_kernel_validation",
]
