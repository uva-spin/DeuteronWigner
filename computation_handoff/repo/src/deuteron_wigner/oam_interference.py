"""Light-front partial-wave interference layer for spin--orbit/OAM TMD inputs."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from functools import lru_cache
import math
from typing import Callable, Mapping

import numpy as np

ComplexAmplitude = Callable[[str, int, float, float, float], complex]
CollinearDensity = Callable[[str, int, float, float], float]


class InterferenceKind(str, Enum):
    T_EVEN_REAL = "t_even_real"
    T_ODD_IMAGINARY = "t_odd_imaginary"


@dataclass(frozen=True)
class LFPartialWaveAmplitude:
    """One replaceable LF amplitude carrying definite transverse OAM."""

    label: str
    orbital_m: int
    parity: int
    amplitude: ComplexAmplitude
    source: str

    def __post_init__(self) -> None:
        if not self.label or not self.source:
            raise ValueError("partial wave requires label and source")
        if self.parity not in (-1, 1):
            raise ValueError("partial-wave parity must be +/-1")
        if abs(self.orbital_m) > 4:
            raise ValueError("partial-wave |m| exceeds the declared leading model")

    def value(
        self, nucleon: str, flavor: int, x: float, k_gev: float, q_gev: float
    ) -> complex:
        result = complex(self.amplitude(nucleon, flavor, x, k_gev, q_gev))
        if not np.isfinite(result.real) or not np.isfinite(result.imag):
            raise ValueError("partial-wave amplitude must be finite")
        return result


@dataclass(frozen=True)
class OAMInterferenceTerm:
    """Bilinear between two LF partial waves."""

    left: str
    right: str
    kind: InterferenceKind
    coefficient: float
    tmd_name: str

    def __post_init__(self) -> None:
        if not self.left or not self.right or not self.tmd_name:
            raise ValueError("interference term requires wave and TMD labels")
        if not math.isfinite(self.coefficient):
            raise ValueError("interference coefficient must be finite")


@dataclass(frozen=True)
class OAMInterferenceModel:
    """Compose named TMD coefficients from explicit LF wave bilinears."""

    waves: Mapping[str, LFPartialWaveAmplitude]
    terms: tuple[OAMInterferenceTerm, ...]

    def __post_init__(self) -> None:
        if set(self.waves) != {wave.label for wave in self.waves.values()}:
            raise ValueError("partial-wave mapping keys must equal wave labels")
        for term in self.terms:
            if term.left not in self.waves or term.right not in self.waves:
                raise ValueError("interference term references an unknown wave")
            delta_m = self.rank(term)
            if delta_m > 4:
                raise ValueError("interference transverse rank exceeds four")

    def rank(self, term: OAMInterferenceTerm) -> int:
        return abs(
            self.waves[term.left].orbital_m
            - self.waves[term.right].orbital_m
        )

    def value(
        self,
        tmd_name: str,
        *,
        nucleon: str,
        flavor: int,
        x: float,
        k_gev: float,
        q_gev: float,
        azimuth: float = 0.0,
        staple_orientation: float = 1.0,
    ) -> float:
        """Return the real coefficient for one named interference channel."""

        total = 0.0
        for term in self.terms:
            if term.tmd_name != tmd_name:
                continue
            left_wave = self.waves[term.left]
            right_wave = self.waves[term.right]
            left = left_wave.value(nucleon, flavor, x, k_gev, q_gev)
            right = right_wave.value(nucleon, flavor, x, k_gev, q_gev)
            delta_m = left_wave.orbital_m - right_wave.orbital_m
            harmonic = np.exp(1j * delta_m * azimuth)
            bilinear = left * np.conj(right) * harmonic
            if term.kind == InterferenceKind.T_EVEN_REAL:
                contribution = 2.0 * bilinear.real
            else:
                if staple_orientation not in (-1.0, 1.0):
                    raise ValueError("T-odd interference requires a simple staple orientation")
                contribution = 2.0 * staple_orientation * bilinear.imag
            total += term.coefficient * contribution
        return float(total)

    def named_tmds(self) -> tuple[str, ...]:
        return tuple(sorted({term.tmd_name for term in self.terms}))

    def disable_wave(self, label: str) -> "OAMInterferenceModel":
        """Return a controlled limit with one amplitude set identically zero."""

        if label not in self.waves:
            raise KeyError(label)
        wave = self.waves[label]
        disabled = LFPartialWaveAmplitude(
            label=wave.label,
            orbital_m=wave.orbital_m,
            parity=wave.parity,
            amplitude=lambda nucleon, flavor, x, k, q: 0.0j,
            source=f"disabled controlled limit of {wave.source}",
        )
        return OAMInterferenceModel(
            waves={**self.waves, label: disabled},
            terms=self.terms,
        )

    def fitted_momentum_input(
        self,
        tmd_name: str,
        *,
        source: str,
        process_reference: str,
        validity,
        staple_orientation: float = 1.0,
        uncertainty_kind: str = "partial-wave amplitude parameter ensemble",
    ):
        """Expose one interference coefficient as a full-k fitted input."""

        from .nucleon_inputs import FittedMomentumTMDInput
        from .provenance import ComponentProvenance, EvidenceClass, Mechanism

        if tmd_name not in self.named_tmds():
            raise KeyError(tmd_name)
        matching_terms = tuple(term for term in self.terms if term.tmd_name == tmd_name)
        is_t_odd = any(
            term.kind == InterferenceKind.T_ODD_IMAGINARY for term in matching_terms
        )

        def response(
            nucleon: str, flavor: int, x: float, k_gev: float, q_gev: float
        ) -> float:
            return self.value(
                tmd_name,
                nucleon=nucleon,
                flavor=flavor,
                x=x,
                k_gev=k_gev,
                q_gev=q_gev,
                staple_orientation=staple_orientation,
            )

        return FittedMomentumTMDInput(
            response=response,
            provenance=ComponentProvenance(
                name=f"{tmd_name} from explicit LF OAM interference",
                evidence=EvidenceClass.MODEL,
                mechanism=Mechanism.NUCLEON_IMPULSE,
                sources=(source, *(wave.source for wave in self.waves.values())),
                assumptions=(
                    "partial waves carry definite transverse OAM",
                    "T-odd terms are imaginary bilinears with explicit staple sign",
                    "normalizations and relative phases are model parameters",
                ),
                validity=validity,
                uncertainty_kind=uncertainty_kind,
                replaceable_interface="OAMInterferenceModel",
            ),
            process_reference=(
                process_reference if is_t_odd else "universal T-even interference"
            ),
        )

    def fitted_scalar_input(
        self,
        tmd_name: str,
        *,
        source: str,
        validity,
        transverse_cutoff_gev: float,
        quadrature_nodes: int = 96,
        uncertainty_kind: str = "partial-wave amplitude parameter ensemble",
    ):
        """Integrate a T-even interference into the scalar profile coefficient.

        The returned number is ``integral d^2 k F``.  The nucleon builder may
        subsequently assign a replaceable normalized transverse profile; this
        adapter therefore preserves the integrated partial-wave constraint but
        does not claim to preserve its detailed k shape.
        """

        from .nucleon_inputs import FittedScalarTMDInput
        from .provenance import ComponentProvenance, EvidenceClass, Mechanism

        if tmd_name not in self.named_tmds():
            raise KeyError(tmd_name)
        matching_terms = tuple(term for term in self.terms if term.tmd_name == tmd_name)
        if any(term.kind == InterferenceKind.T_ODD_IMAGINARY for term in matching_terms):
            raise ValueError("T-odd OAM inputs require the full momentum adapter")
        if transverse_cutoff_gev <= 0.0 or quadrature_nodes < 24:
            raise ValueError("scalar OAM integration requires a physical resolved grid")
        nodes, weights = np.polynomial.legendre.leggauss(quadrature_nodes)
        k_values = transverse_cutoff_gev * (nodes + 1.0) / 2.0
        k_weights = transverse_cutoff_gev * weights / 2.0

        @lru_cache(maxsize=131072)
        def response(nucleon: str, flavor: int, x: float, q_gev: float) -> float:
            return float(
                np.dot(
                    k_weights,
                    [
                        2.0
                        * np.pi
                        * k
                        * self.value(
                            tmd_name,
                            nucleon=nucleon,
                            flavor=flavor,
                            x=x,
                            k_gev=float(k),
                            q_gev=q_gev,
                        )
                        for k in k_values
                    ],
                )
            )

        return FittedScalarTMDInput(
            response=response,
            provenance=ComponentProvenance(
                name=f"integrated {tmd_name} LF OAM interference",
                evidence=EvidenceClass.MODEL,
                mechanism=Mechanism.NUCLEON_IMPULSE,
                sources=(source, *(wave.source for wave in self.waves.values())),
                assumptions=(
                    "partial waves carry definite transverse OAM",
                    f"transverse integral truncated at {transverse_cutoff_gev:g} GeV",
                    "downstream normalized profile preserves the integral, not the OAM k shape",
                ),
                validity=validity,
                uncertainty_kind=uncertainty_kind,
                replaceable_interface="OAMInterferenceModel",
            ),
        )


def build_pdf_anchored_oam_model(
    density: CollinearDensity,
    *,
    transverse_width_gev2: Mapping[int, float],
    p_even_coefficients: Mapping[int, float] | None = None,
    p_odd_coefficients: Mapping[int, float] | None = None,
    d_coefficients: Mapping[int, float] | None = None,
) -> OAMInterferenceModel:
    """Build a flavor-resolved LF partial-wave sensitivity scenario.

    The S-wave norm is anchored pointwise to a supplied unpolarized PDF and
    normalized Gaussian. Relativistic P-even, absorptive P-odd, and D-like
    amplitudes are explicit powers of k/M. Their independent coefficients
    are model parameters; no common universal phase is imposed.
    """

    required = {2, 1, -2, -1}
    widths = dict(transverse_width_gev2)
    p_even = dict(p_even_coefficients or {2: 0.22, 1: -0.16, -2: 0.06, -1: -0.05})
    p_odd = dict(p_odd_coefficients or {2: -0.10, 1: 0.14, -2: -0.03, -1: 0.04})
    d_wave = dict(d_coefficients or {2: -0.08, 1: 0.11, -2: -0.02, -1: 0.03})
    if any(set(values) != required for values in (widths, p_even, p_odd, d_wave)):
        raise ValueError("PDF-anchored OAM model requires u,d,ubar,dbar maps")
    if any(value <= 0.0 for value in widths.values()):
        raise ValueError("OAM Gaussian widths must be positive")
    mass = 0.93891897

    def s_amplitude(
        nucleon: str, flavor: int, x: float, k: float, q: float
    ) -> complex:
        collinear = max(0.0, float(density(nucleon, flavor, x, q)))
        profile = np.exp(-k**2 / widths[flavor]) / (np.pi * widths[flavor])
        return complex(np.sqrt(collinear * profile))

    def derived(coefficients: Mapping[int, float], phase: complex, power: int):
        return lambda nucleon, flavor, x, k, q: (
            phase
            * coefficients[flavor]
            * (k / mass) ** power
            * s_amplitude(nucleon, flavor, x, k, q)
        )

    waves = {
        "S": LFPartialWaveAmplitude(
            "S", 0, 1, s_amplitude,
            "unpolarized PDF-normalized Gaussian LF S amplitude",
        ),
        "P_even": LFPartialWaveAmplitude(
            "P_even", 1, -1, derived(p_even, 1.0, 1),
            "real relativistic P-wave spin-orbit scenario",
        ),
        "P_odd": LFPartialWaveAmplitude(
            "P_odd", 1, -1, derived(p_odd, 1j, 1),
            "imaginary eikonal P-wave rescattering scenario",
        ),
        "D": LFPartialWaveAmplitude(
            "D", 2, 1, derived(d_wave, 1.0, 2),
            "real D-like rank-two OAM scenario",
        ),
    }
    terms = (
        OAMInterferenceTerm("S", "P_odd", InterferenceKind.T_ODD_IMAGINARY, 1.0, "f1Tperp"),
        OAMInterferenceTerm("S", "P_odd", InterferenceKind.T_ODD_IMAGINARY, -0.65, "h1perp"),
        OAMInterferenceTerm("S", "P_even", InterferenceKind.T_EVEN_REAL, 0.75, "g1T"),
        OAMInterferenceTerm("S", "P_even", InterferenceKind.T_EVEN_REAL, -0.55, "h1Lperp"),
        OAMInterferenceTerm("S", "D", InterferenceKind.T_EVEN_REAL, 1.0, "h1Tperp"),
    )
    return OAMInterferenceModel(waves, terms)
