"""Canonical observable comparison for the LF and LPS spin-1 current routes."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Optional, Tuple

import numpy as np

from deuteron_wigner.bridge.c400_s2_corrective.current_adapter import (
    CurrentAdapterError,
    CurrentDiagnostics,
    CurrentRequest,
    CurrentRoute,
    UnifiedCurrentAdapter,
)


CANONICAL_NORMALIZATION = "C400_CANONICAL_DIMENSIONLESS_GC_GM_GQ"
_SUPPORTED_NORMALIZATIONS = {
    "GC,GM,GQ Carlson-Ji spin-1 normalization",
    "GC,GM,GQ LPS Eq.21 normalization",
}


@dataclass(frozen=True)
class CanonicalFormFactors:
    route: str
    state_id: str
    q2_GeV2: float
    deuteron_mass_GeV: float
    GC: Optional[complex]
    GM: Optional[complex]
    GQ: Optional[complex]
    canonical_normalization: str
    route_normalization: str
    canonicalization_authority: str
    route_conventions: Mapping[str, Any]
    physical_current_claim: bool = False


@dataclass(frozen=True)
class CanonicalCurrentComparison:
    status: str
    first: CanonicalFormFactors
    second: CanonicalFormFactors
    differences: Mapping[str, Optional[complex]]
    absolute_differences: Mapping[str, Optional[float]]
    relative_differences: Mapping[str, Optional[float]]
    first_angular_condition_residual: Optional[complex]
    second_angular_condition_residual: Optional[complex]
    first_prescription_spread: Mapping[str, Tuple[complex, complex, complex]]
    second_prescription_spread: Mapping[str, Tuple[complex, complex, complex]]
    production_current_selected: bool = False
    covariance_bound: bool = False
    physical_agreement_claim: bool = False
    incomparability_reasons: Tuple[str, ...] = ()
    route_local_extraction_passed: bool = True
    comparison_basis: str = "COMMON_INVARIANT_Q2_MASS_STATE_AND_CANONICAL_GC_GM_GQ"


def _canonicalize(request: CurrentRequest, diagnostics: CurrentDiagnostics) -> CanonicalFormFactors:
    normalization = request.conventions.form_factor_normalization
    if normalization not in _SUPPORTED_NORMALIZATIONS:
        raise CurrentAdapterError(f"no approved diagnostic canonicalization for {normalization!r}")
    values = diagnostics.selected_extraction
    return CanonicalFormFactors(
        route=request.route.value,
        state_id=request.state_id,
        q2_GeV2=float(request.kinematics.q2_GeV2),
        deuteron_mass_GeV=float(request.kinematics.deuteron_mass_GeV),
        GC=values[0],
        GM=values[1],
        GQ=values[2],
        canonical_normalization=CANONICAL_NORMALIZATION,
        route_normalization=normalization,
        canonicalization_authority=(
            "identity on the named dimensionless GC/GM/GQ outputs of "
            "lf_current.extract_form_factors and covariant_current.extract_lps_form_factors"
        ),
        route_conventions={
            "frame": request.conventions.frame,
            "current_component": request.conventions.current_component,
            "amplitude_normalization": request.conventions.amplitude_normalization,
            "form_factor_normalization": request.conventions.form_factor_normalization,
            "extraction_prescription": request.conventions.extraction_prescription,
            "zero_mode_policy": request.conventions.zero_mode_policy,
            "interaction_current_policy": request.conventions.interaction_current_policy,
        },
    )


def _relative_difference(first: complex, second: complex) -> float:
    scale = max(abs(first), abs(second), np.finfo(float).tiny)
    return float(abs(first - second) / scale)


def compare_current_requests(
    first_request: CurrentRequest,
    second_request: CurrentRequest,
    *,
    q2_rtol: float = 1.0e-12,
    q2_atol: float = 1.0e-14,
    mass_rtol: float = 1.0e-12,
    mass_atol: float = 1.0e-14,
) -> CanonicalCurrentComparison:
    """Compare route-local extractions in one canonical observable space.

    Route, frame, current component, and amplitude normalization are expected to
    differ between LF and LPS.  Eligibility depends on common invariants and
    state identity, not identical route-specific convention records.
    """

    reasons: list[str] = []
    if first_request.state_id != second_request.state_id:
        reasons.append("state identifiers differ")
    if not np.isclose(
        first_request.kinematics.q2_GeV2,
        second_request.kinematics.q2_GeV2,
        rtol=q2_rtol,
        atol=q2_atol,
    ):
        reasons.append("Q^2 differs")
    if not np.isclose(
        first_request.kinematics.deuteron_mass_GeV,
        second_request.kinematics.deuteron_mass_GeV,
        rtol=mass_rtol,
        atol=mass_atol,
    ):
        reasons.append("deuteron mass differs")

    adapter = UnifiedCurrentAdapter()
    first_diagnostics = adapter.diagnose(first_request)
    second_diagnostics = adapter.diagnose(second_request)
    first = _canonicalize(first_request, first_diagnostics)
    second = _canonicalize(second_request, second_diagnostics)

    differences: dict[str, Optional[complex]] = {}
    absolute: dict[str, Optional[float]] = {}
    relative: dict[str, Optional[float]] = {}
    comparable_components = 0
    for name in ("GC", "GM", "GQ"):
        left = getattr(first, name)
        right = getattr(second, name)
        if left is None or right is None:
            differences[name] = None
            absolute[name] = None
            relative[name] = None
            continue
        comparable_components += 1
        differences[name] = complex(left - right)
        absolute[name] = float(abs(left - right))
        relative[name] = _relative_difference(left, right)

    if reasons:
        status = "INCOMPARABLE_INVARIANTS"
    elif comparable_components == 3:
        status = "CANONICAL_OBSERVABLE_COMPARISON"
    elif comparable_components > 0:
        status = "PARTIAL_STATIC_LIMIT_CANONICAL_COMPARISON"
    else:
        status = "NO_COMMON_EXTRACTABLE_COMPONENTS"

    return CanonicalCurrentComparison(
        status=status,
        first=first,
        second=second,
        differences=differences,
        absolute_differences=absolute,
        relative_differences=relative,
        first_angular_condition_residual=first_diagnostics.angular_condition_residual,
        second_angular_condition_residual=second_diagnostics.angular_condition_residual,
        first_prescription_spread=first_diagnostics.omitted_amplitude_prescription_spread,
        second_prescription_spread=second_diagnostics.omitted_amplitude_prescription_spread,
        incomparability_reasons=tuple(reasons),
    )


__all__ = [
    "CANONICAL_NORMALIZATION",
    "CanonicalFormFactors",
    "CanonicalCurrentComparison",
    "compare_current_requests",
]
