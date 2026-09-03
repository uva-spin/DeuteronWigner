"""Configured phenomenological nucleon inputs for the parent TMD model."""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from functools import lru_cache
import math
from typing import Callable, Mapping

from scipy.integrate import quad
from scipy.optimize import brentq, minimize_scalar

from .nucleon_quark_correlator import (
    FlavorResolvedNucleonQuarkModel,
    NucleonTMDComponent,
)
from .pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from .provenance import (
    ComponentProvenance,
    EvidenceClass,
    Mechanism,
    ValidityDomain,
)

LIGHT_FLAVORS = (2, 1, -2, -1)
ISOSPIN_ROTATION = {2: 1, 1: 2, -2: -1, -1: -2}
ChargeSymmetryResponse = Callable[[str, int, str, float, float], float]
ChargeSymmetryUncertainty = Callable[[str, int, str, float, float], float]
FittedMomentumResponse = Callable[[str, int, float, float, float], float]
FittedScalarResponse = Callable[[str, int, float, float], float]


@dataclass(frozen=True)
class FittedMomentumTMDInput:
    """Full momentum-space TMD that must bypass the Gaussian profile layer."""

    response: FittedMomentumResponse
    provenance: ComponentProvenance
    process_reference: str

    def value(
        self,
        nucleon: str,
        flavor: int,
        x: float,
        k_gev: float,
        q_gev: float,
    ) -> float:
        if not self.provenance.validity.contains(x=x, q_gev=q_gev, k_gev=k_gev):
            return 0.0
        value = float(self.response(nucleon, flavor, x, k_gev, q_gev))
        if not math.isfinite(value):
            raise ValueError("fitted momentum-space TMD returned a nonfinite value")
        return value


@dataclass(frozen=True)
class FittedScalarTMDInput:
    """Collinear coefficient or transverse moment with explicit provenance."""

    response: FittedScalarResponse
    provenance: ComponentProvenance

    def value(
        self, nucleon: str, flavor: int, x: float, q_gev: float
    ) -> float:
        if not self.provenance.validity.contains(x=x, q_gev=q_gev):
            return 0.0
        value = float(self.response(nucleon, flavor, x, q_gev))
        if not math.isfinite(value):
            raise ValueError("fitted scalar TMD input returned a nonfinite value")
        return value


@dataclass(frozen=True)
class ChargeSymmetryBreakingInput:
    """Replaceable relative CSB/QED correction to nucleon TMD amplitudes.

    ``response`` returns ``delta`` in ``F -> (1 + delta) F`` for a named
    nucleon, PDG flavor, TMD, x, and Q.  The transverse width is deliberately
    unchanged: a width-level CSB input requires a separate fitted interface
    rather than being inferred from an amplitude correction.
    """

    response: ChargeSymmetryResponse
    provenance: ComponentProvenance
    exact_zero: bool = False
    uncertainty_response: ChargeSymmetryUncertainty | None = None

    def __post_init__(self) -> None:
        if self.provenance.mechanism != Mechanism.ISOSPIN_BREAKING:
            raise ValueError("CSB input provenance must use isospin_breaking")
        if self.exact_zero and self.provenance.evidence != EvidenceClass.EXACT:
            raise ValueError("an exact-zero CSB limit requires exact provenance")

    def relative_correction(
        self, nucleon: str, flavor: int, tmd_name: str, x: float, q_gev: float
    ) -> float:
        if not self.provenance.validity.contains(x=x, q_gev=q_gev):
            return 0.0
        delta = float(self.response(nucleon, flavor, tmd_name, x, q_gev))
        if not math.isfinite(delta) or delta <= -1.0:
            raise ValueError("CSB relative correction must be finite and greater than -1")
        if self.exact_zero and delta != 0.0:
            raise ValueError("exact-zero CSB input returned a nonzero correction")
        return delta

    def relative_uncertainty(
        self, nucleon: str, flavor: int, tmd_name: str, x: float, q_gev: float
    ) -> float:
        """Return an absolute one-sigma uncertainty on the relative correction."""

        if not self.provenance.validity.contains(x=x, q_gev=q_gev):
            return 0.0
        if self.uncertainty_response is None:
            return 0.0
        uncertainty = float(
            self.uncertainty_response(nucleon, flavor, tmd_name, x, q_gev)
        )
        if not math.isfinite(uncertainty) or uncertainty < 0.0:
            raise ValueError("CSB relative uncertainty must be finite and nonnegative")
        return uncertainty

    @staticmethod
    def exact_isospin_limit() -> "ChargeSymmetryBreakingInput":
        return ChargeSymmetryBreakingInput(
            response=lambda nucleon, flavor, tmd_name, x, q_gev: 0.0,
            provenance=ComponentProvenance(
                name="exact charge-symmetry limit",
                evidence=EvidenceClass.EXACT,
                mechanism=Mechanism.ISOSPIN_BREAKING,
                sources=("QCD isospin limit m_u=m_d with electromagnetism disabled",),
                assumptions=(
                    "neutron inputs are the u<->d and ubar<->dbar rotation of proton inputs",
                    "no QED evolution or nucleon mass-splitting correction",
                ),
                validity=ValidityDomain(1.0e-3, 0.8, 1.3, 100.0, 1.5),
                uncertainty_kind="exact configured limit; physical CSB remains unresolved",
                replaceable_interface="ChargeSymmetryBreakingInput",
            ),
            exact_zero=True,
        )


@dataclass(frozen=True)
class NucleonInputConfiguration:
    """Replaceable choices for the first parent-derived phenomenology layer."""

    unpolarized_widths_gev2: Mapping[int, float]
    helicity_widths_gev2: Mapping[int, float]
    transversity_widths_gev2: Mapping[int, float]
    t_odd_widths_gev2: Mapping[int, float]
    transversity_tensor_charges: Mapping[int, float]
    transversity_small_x_power: Mapping[int, float]
    transversity_large_x_power: Mapping[int, float]
    pretzelosity_fractions: Mapping[int, float] = field(
        default_factory=lambda: {2: 0.0, 1: 0.0, -2: 0.0, -1: 0.0}
    )
    transversity_reference_scale_gev: float = 2.0
    transversity_sea_endpoint_power: float = 8.0
    transfer_slope_gev2: float = 1.0
    t_odd_boundary: str = "zero_one_body"

    @staticmethod
    def flavor_resolved_baseline() -> "NucleonInputConfiguration":
        return NucleonInputConfiguration(
            # Model representatives informed by the flavor-dependent
            # unpolarized-TMD extraction arXiv:2405.13833. They are scanned,
            # not treated as fitted parameter values from that analysis.
            unpolarized_widths_gev2={2: 0.28, 1: 0.32, -2: 0.36, -1: 0.39},
            helicity_widths_gev2={2: 0.24, 1: 0.29, -2: 0.34, -1: 0.37},
            transversity_widths_gev2={2: 0.23, 1: 0.27, -2: 0.34, -1: 0.36},
            t_odd_widths_gev2={2: 0.30, 1: 0.34, -2: 0.38, -1: 0.40},
            # JAMDiFF phenomenology+lattice central tensor charges at
            # mu^2=4 GeV^2 (arXiv:2306.12998, Table II). Antiquark central
            # values remain zero until replicas are ingested.
            transversity_tensor_charges={
                2: 0.71, 1: -0.200, -2: 0.0, -1: 0.0
            },
            # A bounded shape multiplies the pointwise Soffer ceiling. These
            # exponents are explicitly model-dependent, replaceable choices.
            transversity_small_x_power={2: 0.35, 1: 0.35, -2: 0.35, -1: 0.35},
            transversity_large_x_power={2: 0.25, 1: 0.25, -2: 0.25, -1: 0.25},
            pretzelosity_fractions={2: 0.0, 1: 0.0, -2: 0.0, -1: 0.0},
        )

    def with_pretzelosity_fraction(
        self, fraction: float
    ) -> "NucleonInputConfiguration":
        """Return a named-sign sensitivity member for all light flavors."""

        if not -1.0 <= fraction <= 1.0:
            raise ValueError("pretzelosity fraction must lie in [-1,1]")
        return replace(
            self,
            pretzelosity_fractions={
                flavor: float(fraction) for flavor in LIGHT_FLAVORS
            },
        )


def _provenance(
    *,
    name: str,
    evidence: EvidenceClass,
    sources: tuple[str, ...],
    assumptions: tuple[str, ...],
    uncertainty: str,
) -> ComponentProvenance:
    return ComponentProvenance(
        name=name,
        evidence=evidence,
        mechanism=Mechanism.NUCLEON_IMPULSE,
        sources=sources,
        assumptions=assumptions,
        validity=ValidityDomain(1.0e-3, 0.8, 1.3, 100.0, 1.5),
        uncertainty_kind=uncertainty,
        replaceable_interface="NucleonTMDComponent",
    )


def composed_transversity_ceiling(
    f1: float,
    g1: float,
    *,
    unpolarized_width_gev2: float,
    helicity_width_gev2: float,
    transversity_width_gev2: float,
    k_max_gev: float = 1.5,
) -> float:
    """Largest collinear h1 compatible with the composed Gaussian TMDs."""

    wf = float(unpolarized_width_gev2)
    wg = float(helicity_width_gev2)
    wh = float(transversity_width_gev2)
    if min(wf, wg, wh) <= 0.0 or k_max_gev <= 0.0:
        raise ValueError("transversity ceiling requires positive widths and k max")
    collinear = 0.5 * max(0.0, float(f1) + float(g1))

    def ceiling(k2: float) -> float:
        return 0.5 * wh * (
            float(f1) / wf * math.exp(k2 * (1.0 / wh - 1.0 / wf))
            + float(g1) / wg * math.exp(k2 * (1.0 / wh - 1.0 / wg))
        )

    result = minimize_scalar(
        ceiling, bounds=(0.0, k_max_gev**2), method="bounded",
        options={"xatol": 1.0e-10},
    )
    tmd_ceiling = max(
        0.0, min(ceiling(0.0), ceiling(k_max_gev**2), result.fun)
    )
    return float(min(collinear, tmd_ceiling))


def build_nucleon_quark_models(
    unpolarized: LHAPDFProvider,
    polarized: PolarizedLHAPDFProvider,
    configuration: NucleonInputConfiguration | None = None,
    transversity_input: Callable[[int, float, float], float] | None = None,
    charge_symmetry_breaking: ChargeSymmetryBreakingInput | None = None,
    sivers_input: FittedMomentumTMDInput | None = None,
    boer_mulders_input: FittedMomentumTMDInput | None = None,
    g1t_input: FittedScalarTMDInput | None = None,
    h1lperp_input: FittedScalarTMDInput | None = None,
    pretzelosity_input: FittedScalarTMDInput | None = None,
) -> tuple[FlavorResolvedNucleonQuarkModel, FlavorResolvedNucleonQuarkModel]:
    """Build distinct proton and neutron models without early isoscalar sums."""

    config = configuration or NucleonInputConfiguration.flavor_resolved_baseline()
    csb = charge_symmetry_breaking or ChargeSymmetryBreakingInput.exact_isospin_limit()
    if config.t_odd_boundary != "zero_one_body":
        raise ValueError(
            "only the explicit zero one-body T-odd boundary is implemented; "
            "use a fitted component provider for nonzero Sivers/Boer-Mulders input"
        )

    def make(nucleon: str) -> FlavorResolvedNucleonQuarkModel:
        if nucleon == "proton":
            f1_pdf = unpolarized.proton
            g1_pdf = polarized.proton
            map_flavor: Callable[[int], int] = lambda flavor: flavor
        elif nucleon == "neutron":
            f1_pdf = unpolarized.neutron
            g1_pdf = polarized.neutron
            map_flavor = lambda flavor: ISOSPIN_ROTATION.get(flavor, flavor)
        else:
            raise ValueError("nucleon must be proton or neutron")

        raw_f1_pdf = f1_pdf
        raw_g1_pdf = g1_pdf

        @lru_cache(maxsize=None)
        def f1_pdf(flavor: int, x: float, scale: float) -> float:
            return float(raw_f1_pdf(flavor, x, scale))

        @lru_cache(maxsize=None)
        def g1_pdf(flavor: int, x: float, scale: float) -> float:
            return float(raw_g1_pdf(flavor, x, scale))

        def widths(values: Mapping[int, float]) -> dict[int, float]:
            # Charge symmetry rotates both the collinear flavor and its
            # transverse profile. Isospin breaking belongs in a separate
            # mechanism component, never in an accidental width mismatch.
            return {flavor: float(values[map_flavor(flavor)]) for flavor in LIGHT_FLAVORS}

        @lru_cache(maxsize=None)
        def transversity_amplitude(proton_flavor: int) -> float:
            """Fit the bounded shape to its reference tensor-charge moment."""

            target = float(config.transversity_tensor_charges[proton_flavor])
            if target == 0.0:
                return 0.0
            sign = 1.0 if target > 0.0 else -1.0
            a = float(config.transversity_small_x_power[proton_flavor])
            b = float(config.transversity_large_x_power[proton_flavor])
            reference_scale = float(config.transversity_reference_scale_gev)
            wf = float(config.unpolarized_widths_gev2[proton_flavor])
            wg = float(config.helicity_widths_gev2[proton_flavor])
            wh = float(config.transversity_widths_gev2[proton_flavor])

            def proton_tmd_ceiling(x: float) -> float:
                f = unpolarized.proton(proton_flavor, x, reference_scale)
                g = polarized.proton(proton_flavor, x, reference_scale)

                def value(k2: float) -> float:
                    return 0.5 * wh * (
                        f / wf * math.exp(k2 * (1.0 / wh - 1.0 / wf))
                        + g / wg * math.exp(k2 * (1.0 / wh - 1.0 / wg))
                    )

                optimum = minimize_scalar(
                    value, bounds=(0.0, 1.5**2), method="bounded"
                )
                return max(0.0, min(value(0.0), value(1.5**2), optimum.fun))

            # Use the proton PDFs because the configured moments are proton
            # charges. Charge symmetry subsequently rotates the entire input
            # into the neutron without identifying u and d.
            def moment(amplitude: float) -> float:
                return quad(
                    lambda x: proton_tmd_ceiling(x)
                    * sign
                    * math.tanh(
                        amplitude * x**a * (1.0 - x) ** b
                    ),
                    1.0e-5,
                    1.0,
                    epsabs=2.0e-5,
                    epsrel=5.0e-4,
                    limit=150,
                )[0]

            ceiling = abs(moment(1.0e6))
            if abs(target) > ceiling + 1.0e-6:
                raise ValueError(
                    f"tensor charge {target} for flavor {proton_flavor} "
                    f"exceeds the integrated Soffer ceiling {ceiling}"
                )
            return float(brentq(
                lambda amplitude: abs(moment(amplitude)) - abs(target),
                0.0,
                1.0e6,
                xtol=1.0e-10,
                rtol=1.0e-10,
            ))

        @lru_cache(maxsize=None)
        def tmd_soffer_ceiling(flavor: int, x: float, scale: float) -> float:
            """Largest collinear h1 compatible with Gaussian TMD positivity."""

            proton_flavor = map_flavor(flavor)
            wf = float(config.unpolarized_widths_gev2[proton_flavor])
            wg = float(config.helicity_widths_gev2[proton_flavor])
            wh = float(config.transversity_widths_gev2[proton_flavor])
            f = f1_pdf(flavor, x, scale)
            g = g1_pdf(flavor, x, scale)
            # The caller separately applies the collinear Soffer ceiling.
            return composed_transversity_ceiling(
                f, g,
                unpolarized_width_gev2=wf,
                helicity_width_gev2=wg,
                transversity_width_gev2=wh,
            )

        @lru_cache(maxsize=None)
        def h1(flavor: int, x: float, scale: float) -> float:
            proton_flavor = map_flavor(flavor)
            collinear_soffer = 0.5 * max(
                0.0, f1_pdf(flavor, x, scale) + g1_pdf(flavor, x, scale)
            )
            soffer = min(
                collinear_soffer, tmd_soffer_ceiling(flavor, x, scale)
            )
            if transversity_input is not None:
                # The published JAMDiFF replicas use their own f1/g1 basis.
                # Project their central value onto the Soffer interval of
                # the CT18+BDSSV boundary actually composed here.
                fitted = float(transversity_input(
                    proton_flavor, x, scale
                ))
                if proton_flavor < 0 and x > 0.5:
                    # Sea transversity is effectively unconstrained at large
                    # x and the published mean falls more slowly than the
                    # CT18 sea used in this composition. Enforce a smooth
                    # counting-rule endpoint before the positivity projection.
                    fitted *= (
                        (1.0 - x) / 0.5
                    ) ** config.transversity_sea_endpoint_power
                fit_ceiling = 0.995 * soffer
                return float(max(-fit_ceiling, min(fit_ceiling, fitted)))
            target = float(config.transversity_tensor_charges[proton_flavor])
            sign = 0.0 if target == 0.0 else (1.0 if target > 0.0 else -1.0)
            a = float(config.transversity_small_x_power[proton_flavor])
            b = float(config.transversity_large_x_power[proton_flavor])
            fraction = sign * math.tanh(
                transversity_amplitude(proton_flavor)
                * x**a
                * (1.0 - x) ** b
            )
            return float(
                fraction * soffer
            )

        @lru_cache(maxsize=None)
        def g1t_moment(flavor: int, x: float, scale: float) -> float:
            integral = quad(
                lambda y: g1_pdf(flavor, y, scale) / y,
                x,
                1.0,
                epsabs=1.0e-5,
                epsrel=2.0e-3,
                limit=80,
            )[0]
            width = config.helicity_widths_gev2[map_flavor(flavor)]
            return float(2.0 * 0.93891897**2 * x * integral / width)

        @lru_cache(maxsize=None)
        def h1l_moment(flavor: int, x: float, scale: float) -> float:
            integral = quad(
                lambda y: h1(flavor, y, scale) / y**2,
                x,
                1.0,
                epsabs=1.0e-5,
                epsrel=2.0e-3,
                limit=80,
            )[0]
            width = config.transversity_widths_gev2[map_flavor(flavor)]
            return float(-2.0 * 0.93891897**2 * x**2 * integral / width)

        zero = lambda flavor, x, scale: 0.0
        pdf_provenance = _provenance(
            name=f"{nucleon} unpolarized PDF",
            evidence=EvidenceClass.PHENOMENOLOGY,
            sources=("CT18NNLO member 0", "arXiv:2405.13833"),
            assumptions=("Gaussian k-space boundary with flavor-resolved scanned width",),
            uncertainty="CT18 Hessian plus transverse-width parameter scan",
        )
        helicity_provenance = _provenance(
            name=f"{nucleon} helicity PDF",
            evidence=EvidenceClass.PHENOMENOLOGY,
            sources=("BDSSV24-NLO replicas",),
            assumptions=("Gaussian k-space boundary",),
            uncertainty="BDSSV24 replicas plus transverse-width parameter scan",
        )
        transversity_provenance = _provenance(
            name=f"{nucleon} transversity boundary",
            evidence=EvidenceClass.PHENOMENOLOGY,
            sources=(
                "Soffer bound",
                "JAMDiFF arXiv:2306.12998 Table II with lattice constraints",
            ),
            assumptions=(((
                "JAMDiFF pointwise mean evolved on its published Q2 grid",
                "projected onto the CT18+BDSSV Soffer interval",
                "large-x sea mean uses a configurable positivity-compatible endpoint",
            ) if transversity_input is not None else (
                "bounded x-dependent shape normalized to reference tensor charges",
                "central antiquark transversity is zero",
                "shape exponents are model dependent",
            ))),
            uncertainty=(
                "JAMDiFF LHAPDF member 0 central plus physical members 1-968; "
                "member identity and cross-x/flavor covariance are propagated "
                "through nuclear h1 outputs"
            ),
        )
        ww_provenance = _provenance(
            name=f"{nucleon} Wandzura-Wilczek boundary",
            evidence=EvidenceClass.MODEL,
            sources=("leading-twist WW integral relations",),
            assumptions=("neglect genuine quark-gluon-quark terms",),
            uncertainty="WW-breaking parameter scan",
        )
        zero_provenance = _provenance(
            name=f"{nucleon} real one-body phase boundary",
            evidence=EvidenceClass.EXACT,
            sources=("time reversal of a real impulse boundary",),
            assumptions=("no fitted gauge-link phase in the one-body term",),
            uncertainty="separate omitted gauge-link mechanism; exact zero in this component",
        )
        pretzel_provenance = _provenance(
            name=f"{nucleon} nonperturbative pretzelosity sensitivity",
            evidence=EvidenceClass.MODEL,
            sources=(
                "arXiv:1808.10560 (vanishing massless-quark perturbative matching)",
                "model-independent transverse-moment positivity bound",
            ),
            assumptions=(
                "Gaussian bound-state large-b component",
                "fraction of |h1Tperp^(1)| <= (f1-g1)/2",
                "zero remains the central member; signed members are sensitivities",
            ),
            uncertainty="signed configurable positivity-fraction ensemble",
        )
        @lru_cache(maxsize=None)
        def pretzelosity(flavor: int, x: float, scale: float) -> float:
            proton_flavor = map_flavor(flavor)
            fraction = float(config.pretzelosity_fractions[proton_flavor])
            if not -1.0 <= fraction <= 1.0:
                raise ValueError("pretzelosity fraction outside positivity range")
            width = float(config.transversity_widths_gev2[proton_flavor])
            helicity_minus = max(
                0.0, f1_pdf(flavor, x, scale) - g1_pdf(flavor, x, scale)
            )
            # For a normalized Gaussian,
            # h1Tperp^(1)=width*h1Tperp_collinear/(2 M^2).
            return float(
                fraction * 0.93891897**2 * helicity_minus / width
            )
        components = {
            "f1": NucleonTMDComponent(
                f1_pdf, widths(config.unpolarized_widths_gev2), pdf_provenance
            ),
            "g1": NucleonTMDComponent(
                g1_pdf, widths(config.helicity_widths_gev2), helicity_provenance
            ),
            "h1": NucleonTMDComponent(
                h1, widths(config.transversity_widths_gev2), transversity_provenance
            ),
            "h1perp": (
                NucleonTMDComponent(
                    zero,
                    widths(config.t_odd_widths_gev2),
                    boer_mulders_input.provenance,
                    momentum_value=lambda flavor, x, k, scale: (
                        boer_mulders_input.value(
                            nucleon, flavor, x, k, scale
                        )
                    ),
                )
                if boer_mulders_input is not None
                else NucleonTMDComponent(
                    zero, widths(config.t_odd_widths_gev2), zero_provenance
                )
            ),
            "f1Tperp": (
                NucleonTMDComponent(
                    zero,
                    widths(config.t_odd_widths_gev2),
                    sivers_input.provenance,
                    momentum_value=lambda flavor, x, k, scale: sivers_input.value(
                        nucleon, flavor, x, k, scale
                    ),
                )
                if sivers_input is not None
                else NucleonTMDComponent(
                    zero, widths(config.t_odd_widths_gev2), zero_provenance
                )
            ),
            "g1T": NucleonTMDComponent(
                (
                    lambda flavor, x, scale: g1t_input.value(
                        nucleon, flavor, x, scale
                    )
                )
                if g1t_input is not None
                else g1t_moment,
                widths(config.helicity_widths_gev2),
                g1t_input.provenance if g1t_input is not None else ww_provenance,
            ),
            "h1Lperp": NucleonTMDComponent(
                (
                    lambda flavor, x, scale: h1lperp_input.value(
                        nucleon, flavor, x, scale
                    )
                )
                if h1lperp_input is not None
                else h1l_moment,
                widths(config.transversity_widths_gev2),
                (
                    h1lperp_input.provenance
                    if h1lperp_input is not None
                    else ww_provenance
                ),
            ),
            "h1Tperp": NucleonTMDComponent(
                (
                    lambda flavor, x, scale: pretzelosity_input.value(
                        nucleon, flavor, x, scale
                    )
                )
                if pretzelosity_input is not None
                else pretzelosity,
                widths(config.transversity_widths_gev2),
                (
                    pretzelosity_input.provenance
                    if pretzelosity_input is not None
                    else pretzel_provenance
                ),
            ),
        }
        if not csb.exact_zero:
            corrected_components: dict[str, NucleonTMDComponent] = {}
            for component_name, component in components.items():
                raw_value = component.value

                def corrected_value(
                    flavor: int,
                    x: float,
                    scale: float,
                    *,
                    _raw: Callable[[int, float, float], float] = raw_value,
                    _name: str = component_name,
                ) -> float:
                    return float(
                        _raw(flavor, x, scale)
                        * (
                            1.0
                            + csb.relative_correction(
                                nucleon, flavor, _name, x, scale
                            )
                        )
                    )

                corrected_components[component_name] = NucleonTMDComponent(
                    corrected_value,
                    component.width_gev2,
                    component.provenance,
                    momentum_value=(
                        None
                        if component.momentum_value is None
                        else (
                            lambda flavor, x, k, scale,
                            _raw_momentum=component.momentum_value,
                            _name=component_name: float(
                                _raw_momentum(flavor, x, k, scale)
                                * (
                                    1.0
                                    + csb.relative_correction(
                                        nucleon, flavor, _name, x, scale
                                    )
                                )
                            )
                        )
                    ),
                )
            components = corrected_components
        model = FlavorResolvedNucleonQuarkModel(
            components,
            nucleon_mass_gev=0.93891897,
            transfer_slope_gev2=config.transfer_slope_gev2,
            auxiliary_provenance=(csb.provenance,),
        )
        model.require_component_provenance()
        return model

    return make("proton"), make("neutron")
