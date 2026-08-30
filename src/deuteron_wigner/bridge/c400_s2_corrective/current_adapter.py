"""Self-contained, no-default diagnostics for the repository spin-1 current paths.

The adapter accepts either the existing light-front four-amplitude object or
the existing Lev--Pace--Salme covariant matrix path.  It records conventions
as input data and never chooses a production prescription or a covariance.
For the LPS route the matrix components are dimensional and are required to use
the declared ``mass_units``; they are converted together with the mass before
form-factor extraction.  The LPS spin matrix has one fixed canonical basis, so
noncanonical order or phase metadata are rejected rather than silently ignored.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping, Optional, Protocol, Sequence, Tuple

import numpy as np

from deuteron_wigner.covariant_current import extract_lps_form_factors
from deuteron_wigner.lf_current import (
    CurrentPrescription,
    SpinOnePlusCurrent,
    extract_form_factors,
)


class CurrentAdapterError(ValueError):
    """Raised for incomplete or inconsistent current-convention records."""


class CurrentRoute(str, Enum):
    LIGHT_FRONT = "LIGHT_FRONT_PLUS_CURRENT"
    COVARIANT_LPS = "COVARIANT_LPS_LONGITUDINAL_BREIT"


class MomentumUnits(str, Enum):
    GEV = "GeV"
    MEV = "MeV"
    FM_INV = "fm^-1"


_ENERGY_TO_GEV = {
    MomentumUnits.GEV.value: 1.0,
    MomentumUnits.MEV.value: 1.0e-3,
    # The conversion is an explicit unit conversion, not a physical input.
    MomentumUnits.FM_INV.value: 0.1973269804,
}
_CANONICAL_HELICITIES = ("I++", "I+0", "I+-", "I00")
_KNOWN_FRAMES = ("Drell-Yan q+=0", "longitudinal Breit")
_KNOWN_SIGNS = ("Q2=-(q_mu q^mu)>0", "Q^2=-(p'-p)^2 > 0")
_KNOWN_COMPONENTS = ("J+", "J+/-/Jx")
_KNOWN_AMPLITUDE_NORMALIZATIONS = ("I=J+/(2P+)", "LPS unnormalized free current")
_KNOWN_FF_NORMALIZATIONS = (
    "GC,GM,GQ Carlson-Ji spin-1 normalization",
    "GC,GM,GQ LPS Eq.21 normalization",
)
_KNOWN_POLICIES = ("EXPLICIT_CALLER_BOUND", "DIAGNOSTIC_ONLY", "NOT_APPLICABLE")
_KNOWN_EXTRACTIONS = {item.value for item in CurrentPrescription} | {"GK", "BH", "LPS_EQ21"}


def _require_finite_complex(values: Any, *, label: str) -> np.ndarray:
    array = np.asarray(values, dtype=np.complex128)
    if not np.all(np.isfinite(array)):
        raise CurrentAdapterError(f"{label} must contain only finite complex values")
    return array


@dataclass(frozen=True)
class Kinematics:
    """Canonical physical kinematics shared by current routes.

    ``q2_GeV2`` and ``deuteron_mass_GeV`` are the only numerical values used
    by the adapters.  Source units are retained for provenance, while
    ``eta``/``tau`` are derived and cannot be supplied independently.
    """

    q2_GeV2: float
    deuteron_mass_GeV: float
    momentum_transfer_sign: str
    source_momentum_units: str
    source_mass_units: str

    def __post_init__(self) -> None:
        if not np.isfinite(self.q2_GeV2) or self.q2_GeV2 < 0.0:
            raise CurrentAdapterError("canonical Q^2 must be finite and nonnegative")
        if not np.isfinite(self.deuteron_mass_GeV) or self.deuteron_mass_GeV <= 0.0:
            raise CurrentAdapterError("canonical deuteron mass must be finite and positive")
        if self.momentum_transfer_sign not in _KNOWN_SIGNS:
            raise CurrentAdapterError("unsupported momentum-transfer sign convention")
        for units in (self.source_momentum_units, self.source_mass_units):
            if units not in _ENERGY_TO_GEV:
                raise CurrentAdapterError(f"unsupported energy/momentum units: {units!r}")

    @property
    def tau(self) -> float:
        return self.q2_GeV2 / (4.0 * self.deuteron_mass_GeV**2)

    @property
    def eta(self) -> float:
        return self.tau

    @property
    def momentum_transfer_GeV(self) -> float:
        return float(np.sqrt(self.q2_GeV2))

    def record(self) -> Mapping[str, Any]:
        return {
            "Q2_GeV2": self.q2_GeV2,
            "deuteron_mass_GeV": self.deuteron_mass_GeV,
            "eta": self.eta,
            "tau": self.tau,
            "momentum_transfer_sign": self.momentum_transfer_sign,
            "source_momentum_units": self.source_momentum_units,
            "source_mass_units": self.source_mass_units,
            "derived_only": ("eta", "tau"),
        }


@dataclass(frozen=True)
class CurrentConventions:
    frame: str
    momentum_transfer_sign: str
    current_component: str
    amplitude_normalization: str
    helicity_order: Tuple[str, ...]
    helicity_phases: Tuple[complex, ...]
    form_factor_normalization: str
    momentum_transfer_units: str
    mass_units: str
    extraction_prescription: str
    zero_mode_policy: str
    interaction_current_policy: str

    def __post_init__(self) -> None:
        required = (
            self.frame,
            self.momentum_transfer_sign,
            self.current_component,
            self.amplitude_normalization,
            self.form_factor_normalization,
            self.momentum_transfer_units,
            self.mass_units,
            self.extraction_prescription,
            self.zero_mode_policy,
            self.interaction_current_policy,
        )
        if any(not isinstance(value, str) or not value.strip() for value in required):
            raise CurrentAdapterError("all current convention fields are required")
        if self.frame not in _KNOWN_FRAMES:
            raise CurrentAdapterError(f"unsupported route frame convention: {self.frame!r}")
        if self.momentum_transfer_sign not in _KNOWN_SIGNS:
            raise CurrentAdapterError("unsupported momentum-transfer sign convention")
        if self.current_component not in _KNOWN_COMPONENTS:
            raise CurrentAdapterError("unsupported current component convention")
        if self.amplitude_normalization not in _KNOWN_AMPLITUDE_NORMALIZATIONS:
            raise CurrentAdapterError("unsupported amplitude normalization convention")
        if self.form_factor_normalization not in _KNOWN_FF_NORMALIZATIONS:
            raise CurrentAdapterError("unsupported form-factor normalization convention")
        if self.momentum_transfer_units not in _ENERGY_TO_GEV or self.mass_units not in _ENERGY_TO_GEV:
            raise CurrentAdapterError("unsupported momentum or mass units")
        if self.extraction_prescription not in _KNOWN_EXTRACTIONS:
            raise CurrentAdapterError("unsupported extraction prescription")
        if self.zero_mode_policy not in _KNOWN_POLICIES or self.interaction_current_policy not in _KNOWN_POLICIES:
            raise CurrentAdapterError("unsupported current policy label")
        if len(self.helicity_order) != 4 or len(set(self.helicity_order)) != 4:
            raise CurrentAdapterError("four unique helicity labels are required")
        if set(self.helicity_order) != set(_CANONICAL_HELICITIES):
            raise CurrentAdapterError("helicity labels must be the canonical spin-1 amplitude set")
        if len(self.helicity_phases) != 4 or any(abs(complex(value)) == 0.0 for value in self.helicity_phases):
            raise CurrentAdapterError("four nonzero helicity phases are required")
        if any(not np.isclose(abs(complex(value)), 1.0) for value in self.helicity_phases):
            raise CurrentAdapterError("helicity phases must have unit modulus")


@dataclass(frozen=True)
class CurrentRequest:
    route: CurrentRoute
    conventions: CurrentConventions
    current: Any
    eta: float
    momentum_transfer: float
    deuteron_mass: float
    state_id: str = "UNSPECIFIED_DIAGNOSTIC_STATE"
    kinematics: Kinematics = field(init=False)

    def __post_init__(self) -> None:
        if not np.isfinite(self.eta) or self.eta < 0.0:
            raise CurrentAdapterError("eta must be finite and nonnegative")
        if not np.isfinite(self.momentum_transfer) or self.momentum_transfer < 0.0:
            raise CurrentAdapterError("momentum transfer must be finite and nonnegative")
        if not np.isfinite(self.deuteron_mass) or self.deuteron_mass <= 0.0:
            raise CurrentAdapterError("deuteron mass must be finite and positive")
        if not isinstance(self.state_id, str) or not self.state_id.strip():
            raise CurrentAdapterError("state_id is required")
        q_gev = self.momentum_transfer * _ENERGY_TO_GEV[self.conventions.momentum_transfer_units]
        mass_gev = self.deuteron_mass * _ENERGY_TO_GEV[self.conventions.mass_units]
        kinematics = Kinematics(
            q_gev**2,
            mass_gev,
            self.conventions.momentum_transfer_sign,
            self.conventions.momentum_transfer_units,
            self.conventions.mass_units,
        )
        if not np.isclose(self.eta, kinematics.eta, rtol=1e-10, atol=1e-12):
            raise CurrentAdapterError(
                "inconsistent redundant eta/Q/M inputs; eta must be derived from canonical Q^2 and mass"
            )
        object.__setattr__(self, "kinematics", kinematics)
        if self.route is CurrentRoute.LIGHT_FRONT:
            if not isinstance(self.current, SpinOnePlusCurrent):
                raise CurrentAdapterError("light-front route requires SpinOnePlusCurrent")
            _require_finite_complex(
                (
                    self.current.plus_plus,
                    self.current.plus_zero,
                    self.current.plus_minus,
                    self.current.zero_zero,
                ),
                label="light-front current amplitudes",
            )
            if self.conventions.extraction_prescription not in {
                item.value for item in CurrentPrescription
            }:
                raise CurrentAdapterError("light-front route requires a declared LF extraction prescription")
            if (
                self.conventions.frame != "Drell-Yan q+=0"
                or self.conventions.current_component != "J+"
                or self.conventions.amplitude_normalization != "I=J+/(2P+)"
                or self.conventions.form_factor_normalization != "GC,GM,GQ Carlson-Ji spin-1 normalization"
            ):
                raise CurrentAdapterError("light-front route requires the typed Drell-Yan convention record")
        elif self.route is CurrentRoute.COVARIANT_LPS:
            values = _require_finite_complex(self.current, label="covariant LPS current")
            if values.shape != (4, 3, 3):
                raise CurrentAdapterError("covariant LPS route requires a (4,3,3) current")
            if self.conventions.extraction_prescription != "LPS_EQ21":
                raise CurrentAdapterError("covariant route requires explicit LPS_EQ21 prescription name")
            if (
                self.conventions.frame != "longitudinal Breit"
                or self.conventions.current_component != "J+/-/Jx"
                or self.conventions.amplitude_normalization != "LPS unnormalized free current"
                or self.conventions.form_factor_normalization != "GC,GM,GQ LPS Eq.21 normalization"
            ):
                raise CurrentAdapterError("covariant route requires the typed longitudinal-Breit LPS convention record")
            if self.conventions.helicity_order != _CANONICAL_HELICITIES:
                raise CurrentAdapterError(
                    "covariant LPS current uses the fixed canonical m=(+1,0,-1) spin order; "
                    "noncanonical helicity-order metadata are unsupported"
                )
            if any(
                not np.isclose(complex(phase), 1.0 + 0.0j, rtol=0.0, atol=1.0e-14)
                for phase in self.conventions.helicity_phases
            ):
                raise CurrentAdapterError(
                    "covariant LPS current uses the fixed canonical spin-phase convention; "
                    "nontrivial helicity-phase metadata are unsupported"
                )
        else:
            raise CurrentAdapterError(f"unsupported current route: {self.route!r}")


@dataclass(frozen=True)
class CurrentDiagnostics:
    route: str
    convention_record: Mapping[str, Any]
    selected_extraction: Tuple[Optional[complex], Optional[complex], Optional[complex]]
    angular_condition_residual: Optional[complex]
    relative_angular_residual: Optional[float]
    omitted_amplitude_prescription_spread: Mapping[str, Tuple[complex, complex, complex]]
    covariant_path_comparison: Mapping[str, Any]
    diagnostic_completion: Mapping[str, Any]
    covariance_status: str
    production_prescription_selected: bool
    state_id: str
    kinematics: Mapping[str, Any]
    static_limit: Mapping[str, Any]


class CurrentDiscrepancyReceiver(Protocol):
    def receive_current_diagnostics(self, diagnostics: CurrentDiagnostics) -> Mapping[str, Any]:
        ...


def conventions_record(conventions: CurrentConventions) -> Mapping[str, Any]:
    return {
        "frame": conventions.frame,
        "momentum_transfer_sign": conventions.momentum_transfer_sign,
        "current_component": conventions.current_component,
        "amplitude_normalization": conventions.amplitude_normalization,
        "helicity_order": tuple(conventions.helicity_order),
        "helicity_phases": tuple(complex(value) for value in conventions.helicity_phases),
        "form_factor_normalization": conventions.form_factor_normalization,
        "momentum_transfer_units": conventions.momentum_transfer_units,
        "mass_units": conventions.mass_units,
        "extraction_prescription": conventions.extraction_prescription,
        "zero_mode_policy": conventions.zero_mode_policy,
        "interaction_current_policy": conventions.interaction_current_policy,
    }


def _as_complex_tuple(values: Sequence[complex | None]) -> Tuple[Optional[complex], Optional[complex], Optional[complex]]:
    return tuple(complex(value) for value in values)  # type: ignore[return-value]


def _canonical_lf_current(request: CurrentRequest) -> SpinOnePlusCurrent:
    """Decode a declared LF order/phase representation to the canonical order."""

    current = request.current
    values = (current.plus_plus, current.plus_zero, current.plus_minus, current.zero_zero)
    canonical: dict[str, complex] = {}
    for index, label in enumerate(request.conventions.helicity_order):
        canonical[label] = complex(values[index]) / complex(request.conventions.helicity_phases[index])
    return SpinOnePlusCurrent(
        canonical["I++"], canonical["I+0"], canonical["I+-"], canonical["I00"]
    )


def encode_lf_current(current: SpinOnePlusCurrent, conventions: CurrentConventions) -> SpinOnePlusCurrent:
    """Encode a canonical LF current into a declared order and phase record."""

    canonical = {
        "I++": current.plus_plus,
        "I+0": current.plus_zero,
        "I+-": current.plus_minus,
        "I00": current.zero_zero,
    }
    encoded = tuple(
        canonical[label] * complex(conventions.helicity_phases[index])
        for index, label in enumerate(conventions.helicity_order)
    )
    return SpinOnePlusCurrent(*encoded)


def _lps_current_in_gev(request: CurrentRequest) -> np.ndarray:
    """Return the dimensional LPS current in GeV units.

    LPS Eq. 21 multiplies the current by a factor proportional to ``1/M``.
    Therefore the unnormalized current matrix and the declared mass must share
    units.  ``CurrentRequest`` records that unit in ``mass_units`` and this
    helper converts the current alongside the mass before extraction.
    """

    factor = _ENERGY_TO_GEV[request.conventions.mass_units]
    return _require_finite_complex(request.current, label="covariant LPS current") * factor


class UnifiedCurrentAdapter:
    """Evaluate explicitly requested routes and return diagnostics only."""

    def extract(self, request: CurrentRequest) -> Tuple[complex, complex, complex]:
        if request.route is CurrentRoute.LIGHT_FRONT:
            if request.kinematics.eta == 0.0:
                canonical = _canonical_lf_current(request)
                return (complex(canonical.plus_plus), None, None)  # type: ignore[return-value]
            prescription = CurrentPrescription(request.conventions.extraction_prescription)
            return _as_complex_tuple(
                extract_form_factors(_canonical_lf_current(request), eta=request.kinematics.eta, prescription=prescription)
            )
        if request.conventions.extraction_prescription != "LPS_EQ21":
            raise CurrentAdapterError("covariant route requires explicit LPS_EQ21 prescription name")
        if request.kinematics.tau == 0.0:
            values = _lps_current_in_gev(request)
            zeta = 1.0 / (np.sqrt(2.0) * request.kinematics.deuteron_mass_GeV)
            return (complex(zeta * (2.0 * values[0, 0, 0] + values[0, 1, 1]) / 3.0), None, None)  # type: ignore[return-value]
        return _as_complex_tuple(
            extract_lps_form_factors(
                _lps_current_in_gev(request),
                momentum_transfer=request.kinematics.momentum_transfer_GeV,
                deuteron_mass=request.kinematics.deuteron_mass_GeV,
            )
        )

    def diagnose(
        self,
        request: CurrentRequest,
        *,
        comparison: Optional[CurrentRequest] = None,
    ) -> CurrentDiagnostics:
        selected = self.extract(request)
        angular: Optional[complex] = None
        relative: Optional[float] = None
        spread: Mapping[str, Tuple[complex, complex, complex]] = {}
        completion: Mapping[str, Any] = {
            "available": False,
            "label": "DIAGNOSTIC_NON_DYNAMICAL_COMPLETION_ONLY",
        }
        static_limit: Mapping[str, Any] = {"active": request.kinematics.q2_GeV2 == 0.0}
        if request.route is CurrentRoute.LIGHT_FRONT:
            current = _canonical_lf_current(request)
            angular = complex(current.angular_condition(request.kinematics.eta))
            relative = float(current.relative_angular_violation(request.kinematics.eta))
            if request.kinematics.eta > 0.0:
                spread = {
                    prescription.value: _as_complex_tuple(
                        extract_form_factors(current, eta=request.kinematics.eta, prescription=prescription)
                    )
                    for prescription in CurrentPrescription
                }
            static_limit = {
                "active": request.kinematics.q2_GeV2 == 0.0,
                "GC": current.plus_plus if request.kinematics.q2_GeV2 == 0.0 else None,
                "GM": None,
                "GQ": None,
                "unextractable_at_zero": ("GM", "GQ"),
            }
            completion = {
                "available": True,
                "label": "DIAGNOSTIC_NON_DYNAMICAL_COMPLETION_ONLY",
                "does_not_define_interaction_current": True,
            }
        comparison_record: Mapping[str, Any]
        if comparison is None:
            comparison_record = {"status": "NOT_REQUESTED"}
        else:
            compatible, reasons = self._comparison_compatibility(request, comparison)
            if not compatible:
                comparison_record = {
                    "status": "INCOMPARABLE_CONVENTIONS",
                    "other_route": comparison.route.value,
                    "difference": None,
                    "reasons": reasons,
                    "physical_agreement_claim": False,
                }
            else:
                other = self.extract(comparison)
                comparison_record = {
                    "status": "DIAGNOSTIC_COMPARISON",
                    "other_route": comparison.route.value,
                    "difference": tuple(a - b for a, b in zip(selected, other) if a is not None and b is not None),
                    "same_convention_signature": True,
                    "physical_agreement_claim": False,
                }
        return CurrentDiagnostics(
            route=request.route.value,
            convention_record=conventions_record(request.conventions),
            selected_extraction=selected,
            angular_condition_residual=angular,
            relative_angular_residual=relative,
            omitted_amplitude_prescription_spread=spread,
            covariant_path_comparison=comparison_record,
            diagnostic_completion=completion,
            covariance_status="UNBOUND_SCIENCE_DECISION_REQUIRED",
            production_prescription_selected=False,
            state_id=request.state_id,
            kinematics=request.kinematics.record(),
            static_limit=static_limit,
        )

    @staticmethod
    def _comparison_compatibility(
        request: CurrentRequest, comparison: CurrentRequest
    ) -> tuple[bool, tuple[str, ...]]:
        reasons = []
        if request.route is not comparison.route:
            reasons.append("route definitions differ")
        if request.state_id != comparison.state_id:
            reasons.append("state identifiers differ")
        if conventions_record(request.conventions) != conventions_record(comparison.conventions):
            reasons.append("typed convention records differ")
        if not np.isclose(request.kinematics.q2_GeV2, comparison.kinematics.q2_GeV2, rtol=1e-12, atol=1e-14):
            reasons.append("Q^2 differs")
        if not np.isclose(request.kinematics.deuteron_mass_GeV, comparison.kinematics.deuteron_mass_GeV, rtol=1e-12, atol=1e-14):
            reasons.append("deuteron mass differs")
        return not reasons, tuple(reasons)


@dataclass(frozen=True)
class CurrentDiscrepancyInterface:
    """Typed handoff for future covariance models; no numeric choices are bound."""

    model_id: str
    authority: str
    provenance: str
    covariance_status: str

    def __post_init__(self) -> None:
        if not self.model_id.strip() or not self.authority.strip() or not self.provenance.strip():
            raise CurrentAdapterError("model id, authority, and provenance are required")
        if self.covariance_status != "UNBOUND_SCIENCE_DECISION_REQUIRED":
            raise CurrentAdapterError("C400.S2 interface cannot bind a covariance")

    def receive_current_diagnostics(self, diagnostics: CurrentDiagnostics) -> Mapping[str, Any]:
        return {
            "model_id": self.model_id,
            "authority": self.authority,
            "provenance": self.provenance,
            "covariance_status": self.covariance_status,
            "diagnostics": diagnostics,
        }


__all__ = [
    "CurrentAdapterError",
    "CurrentRoute",
    "CurrentConventions",
    "CurrentRequest",
    "CurrentDiagnostics",
    "CurrentDiscrepancyReceiver",
    "CurrentDiscrepancyInterface",
    "UnifiedCurrentAdapter",
    "MomentumUnits",
    "Kinematics",
    "encode_lf_current",
    "conventions_record",
]
