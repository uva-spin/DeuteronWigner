"""Configurable correlator-level nuclear mechanisms beyond one-body impulse."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Callable, Mapping

import numpy as np

from .provenance import (
    ComponentProvenance,
    EvidenceClass,
    Mechanism,
    ValidityDomain,
)
from .quark_correlator import Spin1QuarkCorrelator
from .spin import project_matrix, spin_one_basis


@dataclass(frozen=True)
class NuclearCorrectionParameters:
    """Small-deuteron correction family with disjoint kinematic roles."""

    shadowing_strength: float = 0.012
    shadowing_x_scale: float = 0.055
    tensor_shadowing_strength: float = 0.025
    antishadowing_strength: float = 0.006
    antishadowing_center: float = 0.12
    antishadowing_width: float = 0.045
    emc_strength: float = 0.018
    emc_onset: float = 0.30
    shadowing_x_max: float = 0.1
    nucleon_mass_gev: float = 0.93891897
    deuteron_coherence_radius_fm: float = 1.975
    average_nucleon_virtuality: float = -0.045

    def __post_init__(self) -> None:
        if self.shadowing_x_scale <= 0 or self.antishadowing_width <= 0:
            raise ValueError("nuclear correction scales must be positive")
        if not 0.0 < self.emc_onset < 1.0:
            raise ValueError("EMC onset must lie in (0,1)")
        if not 0.0 < self.shadowing_x_max < self.emc_onset:
            raise ValueError("shadowing domain must end below the EMC onset")
        if self.nucleon_mass_gev <= 0.0 or self.deuteron_coherence_radius_fm <= 0.0:
            raise ValueError("mass and coherence radius must be positive")
        if not -0.25 < self.average_nucleon_virtuality <= 0.0:
            raise ValueError("average nucleon virtuality must lie in (-0.25,0]")


@dataclass(frozen=True)
class DiffractiveShadowingInput:
    """Replaceable leading-twist diffractive input for coherent shadowing.

    ``fraction`` is the effective diffractive-to-inclusive strength before
    the deuteron longitudinal coherence form factor. A fitted DPDF adapter
    can replace the default without changing correlator composition.
    """

    fraction: Callable[[str, float, float], float]
    source: str
    relative_uncertainty: float
    classification: EvidenceClass
    uncertainty_members: Mapping[
        str, Callable[[str, float, float], float]
    ] | None = None
    applies_longitudinal_coherence: bool = True

    def __post_init__(self) -> None:
        if not self.source:
            raise ValueError("diffractive input requires a source")
        if self.relative_uncertainty < 0.0:
            raise ValueError("relative uncertainty cannot be negative")

    def value(self, parton_sector: str, x: float, scale_gev: float) -> float:
        result = float(self.fraction(parton_sector, x, scale_gev))
        if not np.isfinite(result) or result < 0.0:
            raise ValueError("diffractive fraction must be finite and nonnegative")
        return result

    def member_values(
        self, parton_sector: str, x: float, scale_gev: float
    ) -> Mapping[str, float]:
        members = self.uncertainty_members or {}
        result = {
            name: float(function(parton_sector, x, scale_gev))
            for name, function in members.items()
        }
        if any(not np.isfinite(value) or value < 0.0 for value in result.values()):
            raise ValueError("diffractive uncertainty members must be nonnegative")
        return result


@dataclass(frozen=True)
class PolarizedTensorShadowingInput:
    """Irreducible target-channel and quark-operator shadowing response.

    The response returns the *fractional suppression* before the common
    longitudinal coherence factor. It must explicitly cover every target
    irrep and every quark operator projection; no unpolarized response is
    silently copied into a polarized block.
    """

    responses: Mapping[
        str, Mapping[str, Callable[[str, float, float], float]]
    ]
    source: str
    evidence: EvidenceClass
    relative_uncertainty: float
    validity: ValidityDomain
    uncertainty_kind: str

    def __post_init__(self) -> None:
        required_channels = set(spin_one_basis())
        required_operators = {"vector", "axial", "transverse"}
        if set(self.responses) != required_operators:
            raise ValueError("shadowing responses require vector, axial, and transverse")
        for operator, channels in self.responses.items():
            if set(channels) != required_channels:
                raise ValueError(
                    f"{operator} shadowing must cover every target irrep"
                )
        if not self.source or not self.uncertainty_kind:
            raise ValueError("polarized shadowing requires source and uncertainty")
        if self.relative_uncertainty < 0.0:
            raise ValueError("shadowing uncertainty must be nonnegative")

    def value(
        self,
        operator: str,
        channel: str,
        parton_sector: str,
        x: float,
        scale_gev: float,
    ) -> float:
        if not self.validity.contains(x=x, q_gev=scale_gev):
            return 0.0
        result = float(
            self.responses[operator][channel](parton_sector, x, scale_gev)
        )
        if not np.isfinite(result):
            raise ValueError("polarized/tensor shadowing response must be finite")
        return result


def build_polarized_tensor_shadowing_input(
    unpolarized: DiffractiveShadowingInput | None = None,
    *,
    vector_ratios: Mapping[str, float] | None = None,
    axial_operator_ratio: float = 0.65,
    transverse_operator_ratio: float = 0.75,
) -> PolarizedTensorShadowingInput:
    """Build a named spin-response ensemble around the sourced U boundary.

    Present data do not determine all spin-dependent diffractive PDFs. The
    default therefore uses explicit, independently replaceable response
    ratios rather than copying the U correction. Tensor ratios are tied to
    the configured HERMES-b1 sensitivity scale and remain model parameters.
    """

    base = unpolarized or default_diffractive_shadowing_input()
    group_ratios = dict(vector_ratios or {
        "U": 1.0,
        "L": 0.65,
        "T": 0.65,
        "LL": 2.0,
        "LT": 1.5,
        "TT": 1.5,
    })
    if set(group_ratios) != {"U", "L", "T", "LL", "LT", "TT"}:
        raise ValueError("spin shadowing ratios must cover U,L,T,LL,LT,TT")
    if any(not np.isfinite(value) for value in group_ratios.values()):
        raise ValueError("spin shadowing ratios must be finite")
    ratios = {
        label: group_ratios[
            "T" if label.startswith("T_")
            else "LT" if label.startswith("LT_")
            else "TT" if label.startswith("TT_")
            else label
        ]
        for label in spin_one_basis()
    }
    operator_ratios = {
        "vector": 1.0,
        "axial": float(axial_operator_ratio),
        "transverse": float(transverse_operator_ratio),
    }
    if any(not np.isfinite(value) for value in operator_ratios.values()):
        raise ValueError("operator shadowing ratios must be finite")

    @lru_cache(maxsize=256)
    def base_value(sector: str, x: float, q: float) -> float:
        return base.value(sector, x, q)

    responses = {}
    for operator, operator_ratio in operator_ratios.items():
        responses[operator] = {}
        for channel, channel_ratio in ratios.items():
            responses[operator][channel] = (
                lambda sector, x, q, op=operator_ratio, ch=channel_ratio: (
                    op * ch * base_value(sector, x, q)
                )
            )
    return PolarizedTensorShadowingInput(
        responses=responses,
        source=(
            f"{base.source}; polarized/tensor irreducible-response model "
            "anchored to HERMES b1, arXiv:hep-ex/0506018"
        ),
        evidence=EvidenceClass.MODEL,
        relative_uncertainty=max(1.0, base.relative_uncertainty),
        validity=ValidityDomain(1.0e-4, 0.1, 2.0, 100.0, 1.5),
        uncertainty_kind=(
            "independent axial, transverse, L/T, LL, LT, and TT response "
            "scenarios; no joint probability"
        ),
    )

def default_diffractive_shadowing_input() -> DiffractiveShadowingInput:
    """Deuteron DIS anchored shadowing with explicit sector extensions.

    The quark central follows the published weak-binding deuteron correction:
    1.5% at x=1e-2, rising to 3% by x<=1e-5.  The continuation to zero at
    x=0.1 prevents the small-x mechanism from leaking into the EMC region.
    Sea/valence separation and the gluon enhancement are model extensions
    because the quoted inclusive correction does not determine them.
    """

    def fraction(parton_sector: str, x: float, scale_gev: float) -> float:
        del scale_gev
        bounded_x = max(float(x), 1.0e-12)
        if bounded_x >= 0.1:
            quark_fraction = 0.0
        elif bounded_x >= 0.01:
            quark_fraction = 0.015 * np.log10(0.1 / bounded_x)
        elif bounded_x >= 1.0e-5:
            quark_fraction = 0.015 + 0.005 * np.log10(0.01 / bounded_x)
        else:
            quark_fraction = 0.03
        sector_factor = {
            "valence": 1.0,
            "sea": 1.0,
            # FGS leading-twist studies expect stronger gluon shadowing, but
            # no deuteron gluon fit fixes this ratio.
            "gluon": 1.5,
        }.get(parton_sector, 1.0)
        return float(sector_factor * quark_fraction)

    relative_uncertainty = 0.5
    return DiffractiveShadowingInput(
        fraction=fraction,
        source=(
            "quark anchors from Accardi et al. deuteron weak-binding "
            "shadowing, FERMILAB-PUB-11-909-T; leading-twist DPDF mechanism "
            "from Frankfurt-Guzey-Strikman hep-ph/0601123; gluon ratio model"
        ),
        relative_uncertainty=relative_uncertainty,
        classification=EvidenceClass.MODEL,
        uncertainty_members={
            "shadowing_low": lambda sector, x, q: (
                (1.0 - relative_uncertainty) * fraction(sector, x, q)
            ),
            "shadowing_high": lambda sector, x, q: (
                (1.0 + relative_uncertainty) * fraction(sector, x, q)
            ),
        },
    )


@dataclass(frozen=True)
class OffShellModificationInput:
    """Replaceable logarithmic PDF response to bound-nucleon virtuality."""

    delta_f: Callable[[str, float, float], float]
    source: str
    relative_uncertainty: float
    classification: EvidenceClass
    absolute_uncertainty: Callable[[float], float] | None = None
    constrained_x_max: float = 1.0

    def value(self, parton_sector: str, x: float, scale_gev: float) -> float:
        result = float(self.delta_f(parton_sector, x, scale_gev))
        if not np.isfinite(result):
            raise ValueError("off-shell response must be finite")
        return result

    def uncertainty(self, x: float) -> float:
        if self.absolute_uncertainty is None:
            return abs(self.value("valence", x, 5.0)) * self.relative_uncertainty
        result = float(self.absolute_uncertainty(x))
        if not np.isfinite(result) or result < 0.0:
            raise ValueError("off-shell uncertainty must be finite and nonnegative")
        return result


@dataclass(frozen=True)
class CJ26OffShellScenario:
    """Published CJ26 cubic off-shell coefficients and marginal errors."""

    label: str
    coefficients: tuple[float, float, float, float]
    standard_errors: tuple[float, float, float, float]

    def value(self, x: float) -> float:
        return float(sum(value * x**power for power, value in enumerate(
            self.coefficients
        )))

    def diagonal_standard_error(self, x: float) -> float:
        # CJ26 v1 publishes marginal errors but not their covariance matrix.
        return float(np.sqrt(sum(
            (error * x**power) ** 2
            for power, error in enumerate(self.standard_errors)
        )))


CJ26_ADDITIVE = CJ26OffShellScenario(
    "CJ26 additive higher twist",
    (-0.474, 3.9, -15.1, 16.2),
    (0.090, 1.3, 5.2, 5.6),
)
CJ26_MULTIPLICATIVE = CJ26OffShellScenario(
    "CJ26 multiplicative higher twist",
    (-0.408, 5.2, -20.6, 20.5),
    (0.088, 1.1, 4.4, 4.4),
)


def default_off_shell_input() -> OffShellModificationInput:
    """CJ26 midpoint with statistical and higher-twist scenario uncertainty."""

    def delta_f(parton_sector: str, x: float, scale_gev: float) -> float:
        del parton_sector, scale_gev
        return 0.5 * (
            CJ26_ADDITIVE.value(x) + CJ26_MULTIPLICATIVE.value(x)
        )

    def uncertainty(x: float) -> float:
        midpoint = delta_f("valence", x, 5.0)
        scenario_half_range = max(
            abs(CJ26_ADDITIVE.value(x) - midpoint),
            abs(CJ26_MULTIPLICATIVE.value(x) - midpoint),
        )
        statistical = max(
            CJ26_ADDITIVE.diagonal_standard_error(x),
            CJ26_MULTIPLICATIVE.diagonal_standard_error(x),
        )
        return float(np.hypot(scenario_half_range, statistical))

    return OffShellModificationInput(
        delta_f=delta_f,
        source=(
            "CJ26 arXiv:2605.31424v1 Eq. (14) and released additive/"
            "multiplicative parameter tables; midpoint central"
        ),
        relative_uncertainty=0.0,
        classification=EvidenceClass.PHENOMENOLOGY,
        absolute_uncertainty=uncertainty,
        constrained_x_max=0.7,
    )


@dataclass(frozen=True)
class AntishadowingInput:
    """Replaceable enhancement constrained by a momentum-sum audit."""

    enhancement: Callable[[float, float], float]
    source: str
    relative_uncertainty: float
    compensation_fraction: float
    lost_momentum: float
    restored_momentum: float

    def __post_init__(self) -> None:
        if not self.source:
            raise ValueError("antishadowing input requires a source")
        if self.relative_uncertainty < 0.0:
            raise ValueError("relative uncertainty cannot be negative")
        if not 0.0 <= self.compensation_fraction <= 1.5:
            raise ValueError("compensation fraction is outside the supported range")
        expected = self.compensation_fraction * self.lost_momentum
        tolerance = 1.0e-10 * max(abs(expected), 1.0)
        if abs(self.restored_momentum - expected) > tolerance:
            raise ValueError("antishadowing input fails its momentum-sum audit")

    def value(self, x: float, scale_gev: float) -> float:
        result = float(self.enhancement(x, scale_gev))
        if not np.isfinite(result) or result < 0.0:
            raise ValueError("antishadowing enhancement must be finite and nonnegative")
        return result


@dataclass(frozen=True)
class AdditionalNuclearComponentInput:
    """Source-required mesonic or non-nucleonic parent contribution."""

    component: Callable[
        [Spin1QuarkCorrelator, Spin1QuarkCorrelator, float, float, str],
        Spin1QuarkCorrelator,
    ]
    source: str
    evidence: EvidenceClass
    mechanism: Mechanism
    relative_uncertainty: float
    validity: ValidityDomain
    uncertainty_description: str = ""

    def __post_init__(self) -> None:
        if self.mechanism not in (
            Mechanism.MESON_EXCHANGE, Mechanism.NON_NUCLEONIC
        ):
            raise ValueError("additional component must be mesonic or non-nucleonic")
        if not self.source:
            raise ValueError("additional nuclear component requires a source")
        if self.relative_uncertainty < 0.0:
            raise ValueError("relative uncertainty cannot be negative")

    def value(
        self,
        proton: Spin1QuarkCorrelator,
        neutron: Spin1QuarkCorrelator,
        x: float,
        scale_gev: float,
        parton_sector: str,
    ) -> Spin1QuarkCorrelator:
        if not self.validity.contains(x=x, q_gev=scale_gev):
            return _zero_correlator()
        result = self.component(proton, neutron, x, scale_gev, parton_sector)
        if not isinstance(result, Spin1QuarkCorrelator):
            raise TypeError("additional component must return a quark correlator")
        if not result.is_target_hermitian():
            raise ValueError("additional nuclear component must be Hermitian")
        return result


def build_momentum_sum_antishadowing_input(
    momentum_density: Callable[[float, float], float],
    *,
    scale_gev: float,
    parton_sector: str,
    diffractive_input: DiffractiveShadowingInput | None = None,
    parameters: NuclearCorrectionParameters = NuclearCorrectionParameters(),
    compensation_fraction: float = 1.0,
    relative_uncertainty: float = 0.5,
    integration_points: int = 160,
) -> AntishadowingInput:
    """Normalize antishadowing to restore a declared shadowing momentum loss.

    ``momentum_density`` returns ``x f(x,Q)`` for the p+n sector being
    corrected. The construction restores ``compensation_fraction`` of the
    leading-twist shadowing loss within a Gaussian enhancement window.
    """

    if scale_gev <= 0.0 or integration_points < 32:
        raise ValueError("invalid scale or antishadowing integration order")
    if not 0.0 <= compensation_fraction <= 1.5:
        raise ValueError("invalid compensation fraction")
    diffractive = diffractive_input or default_diffractive_shadowing_input()
    nodes, weights = np.polynomial.legendre.leggauss(integration_points)

    def integrate(low: float, high: float, values: Callable[[float], float]) -> float:
        x_nodes = 0.5 * ((high - low) * nodes + high + low)
        return float(
            0.5 * (high - low)
            * np.dot(weights, [values(float(x)) for x in x_nodes])
        )

    lost = integrate(
        1.0e-4,
        parameters.shadowing_x_max,
        lambda x: momentum_density(x, scale_gev)
        * diffractive.value(parton_sector, x, scale_gev)
        * longitudinal_coherence_factor(
            x,
            nucleon_mass_gev=parameters.nucleon_mass_gev,
            radius_fm=parameters.deuteron_coherence_radius_fm,
        ),
    )

    def bump(x: float) -> float:
        if x < 0.06 or x > 0.25:
            return 0.0
        return float(np.exp(
            -0.5
            * ((x - parameters.antishadowing_center)
               / parameters.antishadowing_width) ** 2
        ))

    denominator = integrate(
        0.06, 0.25,
        lambda x: momentum_density(x, scale_gev) * bump(x),
    )
    if lost < 0.0 or denominator <= 0.0:
        raise ValueError("momentum density cannot normalize antishadowing")
    normalization = compensation_fraction * lost / denominator

    def enhancement(x: float, query_scale: float) -> float:
        del query_scale
        return normalization * bump(x)

    restored = integrate(
        0.06, 0.25,
        lambda x: momentum_density(x, scale_gev) * enhancement(x, scale_gev),
    )
    return AntishadowingInput(
        enhancement=enhancement,
        source=(
            "momentum-sum compensation of the configured leading-twist "
            f"shadowing kernel for sector {parton_sector}"
        ),
        relative_uncertainty=relative_uncertainty,
        compensation_fraction=compensation_fraction,
        lost_momentum=lost,
        restored_momentum=restored,
    )


def default_antishadowing_input(
    parameters: NuclearCorrectionParameters = NuclearCorrectionParameters(),
) -> AntishadowingInput:
    """Fallback bracket; production callers should use the sum-rule builder."""

    def enhancement(x: float, scale_gev: float) -> float:
        del scale_gev
        return parameters.antishadowing_strength * np.exp(
            -0.5
            * ((x - parameters.antishadowing_center)
               / parameters.antishadowing_width) ** 2
        )

    return AntishadowingInput(
        enhancement=enhancement,
        source="temporary unnormalized antishadowing fallback",
        relative_uncertainty=1.0,
        compensation_fraction=0.0,
        lost_momentum=0.0,
        restored_momentum=0.0,
    )


def longitudinal_coherence_factor(
    x: float,
    *,
    nucleon_mass_gev: float,
    radius_fm: float,
) -> float:
    """Gaussian deuteron longitudinal form factor at q_L=2 m_N x."""

    hbarc_gev_fm = 0.1973269804
    ql_radius = 2.0 * nucleon_mass_gev * x * radius_fm / hbarc_gev_fm
    return float(np.exp(-0.5 * ql_radius**2))


@dataclass(frozen=True)
class MechanismResolvedQuarkCorrelator:
    proton_impulse: Spin1QuarkCorrelator
    neutron_impulse: Spin1QuarkCorrelator
    corrections: Mapping[str, Spin1QuarkCorrelator]
    provenance: Mapping[str, ComponentProvenance]

    @property
    def impulse(self) -> Spin1QuarkCorrelator:
        return _sum_correlators((self.proton_impulse, self.neutron_impulse))

    @property
    def total(self) -> Spin1QuarkCorrelator:
        return _sum_correlators((self.impulse, *self.corrections.values()))


def _sum_correlators(
    correlators: tuple[Spin1QuarkCorrelator, ...]
) -> Spin1QuarkCorrelator:
    return Spin1QuarkCorrelator(
        sum((item.vector for item in correlators), np.zeros((3, 3), complex)),
        sum((item.axial for item in correlators), np.zeros((3, 3), complex)),
        sum(
            (item.transverse for item in correlators),
            np.zeros((2, 3, 3), complex),
        ),
    )


def _zero_correlator() -> Spin1QuarkCorrelator:
    return Spin1QuarkCorrelator(
        np.zeros((3, 3), dtype=np.complex128),
        np.zeros((3, 3), dtype=np.complex128),
        np.zeros((2, 3, 3), dtype=np.complex128),
    )


def _channel_scaled_difference(
    correlator: Spin1QuarkCorrelator,
    channel_factors: Mapping[str, float],
) -> Spin1QuarkCorrelator:
    basis = spin_one_basis()

    def correction(matrix: np.ndarray) -> np.ndarray:
        output = np.zeros((3, 3), dtype=np.complex128)
        for channel, tensor in basis.items():
            factor = float(channel_factors.get(channel, 1.0))
            output += (factor - 1.0) * project_matrix(matrix, tensor) * tensor
        return output

    return Spin1QuarkCorrelator(
        correction(correlator.vector),
        correction(correlator.axial),
        np.asarray([correction(item) for item in correlator.transverse]),
    )


def _operator_channel_scaled_difference(
    correlator: Spin1QuarkCorrelator,
    factors: Mapping[str, Mapping[str, float]],
) -> Spin1QuarkCorrelator:
    """Apply distinct irrep factors to vector/axial/transverse projections."""

    basis = spin_one_basis()

    def correction(matrix: np.ndarray, operator: str) -> np.ndarray:
        output = np.zeros((3, 3), dtype=np.complex128)
        for channel, tensor in basis.items():
            factor = float(factors[operator][channel])
            output += (factor - 1.0) * project_matrix(matrix, tensor) * tensor
        return output

    return Spin1QuarkCorrelator(
        correction(correlator.vector, "vector"),
        correction(correlator.axial, "axial"),
        np.asarray([
            correction(item, "transverse") for item in correlator.transverse
        ]),
    )


def apply_nuclear_corrections(
    *,
    proton_impulse: Spin1QuarkCorrelator,
    neutron_impulse: Spin1QuarkCorrelator,
    x: float,
    scale_gev: float = 5.0,
    parton_sector: str = "sea",
    parameters: NuclearCorrectionParameters = NuclearCorrectionParameters(),
    diffractive_input: DiffractiveShadowingInput | None = None,
    polarized_shadowing_input: PolarizedTensorShadowingInput | None = None,
    off_shell_input: OffShellModificationInput | None = None,
    antishadowing_input: AntishadowingInput | None = None,
    meson_exchange_input: AdditionalNuclearComponentInput | None = None,
    non_nucleonic_input: AdditionalNuclearComponentInput | None = None,
) -> MechanismResolvedQuarkCorrelator:
    """Apply regime-localized correction terms at correlator level.

    These functions are transparent sensitivity models, not a replacement
    for a future diffractive shadowing or off-shell convolution.  They act
    on target irreducible sectors so hermiticity and operator projections
    remain intact.
    """

    if not 0.0 < x <= 1.0 or scale_gev <= 0.0:
        raise ValueError("x and scale must be physical")
    impulse = _sum_correlators((proton_impulse, neutron_impulse))
    p = parameters
    diffractive = diffractive_input or default_diffractive_shadowing_input()
    polarized_shadowing = (
        polarized_shadowing_input
        or build_polarized_tensor_shadowing_input(diffractive)
    )
    off_shell = off_shell_input or default_off_shell_input()
    antishadowing = antishadowing_input or default_antishadowing_input(p)
    antishadowing_shape = antishadowing.value(x, scale_gev)
    off_shell_factor = (
        p.average_nucleon_virtuality
        * off_shell.value(parton_sector, x, scale_gev)
    )
    corrections = {
        "coherent_shadowing": _operator_channel_scaled_difference(
            impulse,
            {
                operator: {
                    channel: 1.0 - (
                        0.0
                        if x > p.shadowing_x_max
                        else polarized_shadowing.value(
                            operator, channel, parton_sector, x, scale_gev
                        )
                        * (
                            longitudinal_coherence_factor(
                                x,
                                nucleon_mass_gev=p.nucleon_mass_gev,
                                radius_fm=p.deuteron_coherence_radius_fm,
                            )
                            if diffractive.applies_longitudinal_coherence
                            else 1.0
                        )
                    )
                    for channel in spin_one_basis()
                }
                for operator in ("vector", "axial", "transverse")
            },
        ),
        "antishadowing": _channel_scaled_difference(
            impulse,
            {
                "U": 1.0 + antishadowing_shape,
                "L": 1.0 + 0.5 * antishadowing_shape,
                "LL": 1.0 + antishadowing_shape,
            },
        ),
        "off_shell": _channel_scaled_difference(
            impulse,
            {
                channel: 1.0 + off_shell_factor
                for channel in spin_one_basis()
            },
        ),
        "meson_exchange": (
            _zero_correlator()
            if meson_exchange_input is None
            else meson_exchange_input.value(
                proton_impulse, neutron_impulse, x, scale_gev, parton_sector
            )
        ),
        "non_nucleonic": (
            _zero_correlator()
            if non_nucleonic_input is None
            else non_nucleonic_input.value(
                proton_impulse, neutron_impulse, x, scale_gev, parton_sector
            )
        ),
    }
    common_validity = ValidityDomain(1.0e-3, 0.8, 1.3, 100.0, 1.5)
    provenance = {
        "coherent_shadowing": ComponentProvenance(
            name="deuteron coherent shadowing sensitivity",
            evidence=EvidenceClass.MODEL,
            mechanism=Mechanism.COHERENT,
            sources=(
                polarized_shadowing.source,
                "HERMES b1 measurement arXiv:hep-ex/0506018",
            ),
            assumptions=(
                "leading-twist diffractive factorization",
                (
                    "Gaussian longitudinal deuteron coherence form factor"
                    if diffractive.applies_longitudinal_coherence
                    else "full transverse-plus-longitudinal deuteron form factor inside DPDF integral"
                ),
                "independent operator and U/L/T/LL/LT/TT response ratios",
            ),
            validity=ValidityDomain(
                1.0e-4, p.shadowing_x_max, 2.0, 100.0, 1.5
            ),
            uncertainty_kind=(
                f"polarized/tensor response relative uncertainty "
                f"{polarized_shadowing.relative_uncertainty:g}; no probability assigned"
            ),
            replaceable_interface="CorrelatorNuclearCorrection",
        ),
        "antishadowing": ComponentProvenance(
            name="momentum-compensating deuteron antishadowing",
            evidence=EvidenceClass.PHENOMENOLOGY,
            mechanism=Mechanism.COHERENT,
            sources=(antishadowing.source,),
            assumptions=(
                "localized enhancement window 0.06<x<0.25",
                f"restores fraction {antishadowing.compensation_fraction:g} "
                "of configured shadowing momentum loss",
            ),
            validity=common_validity,
            uncertainty_kind=(
                f"compensation/profile relative uncertainty "
                f"{antishadowing.relative_uncertainty:g}; no probability assigned"
            ),
            replaceable_interface="CorrelatorNuclearCorrection",
        ),
        "off_shell": ComponentProvenance(
            name="bound-nucleon off-shell response",
            evidence=EvidenceClass.MODEL,
            mechanism=Mechanism.OFF_SHELL,
            sources=(off_shell.source,),
            assumptions=(
                f"average virtuality {p.average_nucleon_virtuality:g}",
                "same response for spin irreps pending polarized off-shell fits",
            ),
            validity=common_validity,
            uncertainty_kind=(
                "CJ26 marginal parameter errors plus additive/multiplicative "
                "higher-twist scenario half-range; published parameter "
                "covariance unavailable"
                if off_shell.absolute_uncertainty is not None
                else f"off-shell response relative uncertainty "
                f"{off_shell.relative_uncertainty:g}; no probability assigned"
            ),
            replaceable_interface="CorrelatorNuclearCorrection",
        ),
        "meson_exchange": ComponentProvenance(
            name="meson-exchange quark contribution",
            evidence=(
                EvidenceClass.MODEL
                if meson_exchange_input is None
                else meson_exchange_input.evidence
            ),
            mechanism=Mechanism.MESON_EXCHANGE,
            sources=(
                "inactive by default: no deuteron meson splitting input configured"
                if meson_exchange_input is None
                else meson_exchange_input.source,
            ),
            assumptions=(
                "exact zero only for the configured nucleonic baseline; not a claim of physical absence",
            ),
            validity=(
                common_validity
                if meson_exchange_input is None
                else meson_exchange_input.validity
            ),
            uncertainty_kind=(
                "unresolved component; source-required activation"
                if meson_exchange_input is None
                else (
                    meson_exchange_input.uncertainty_description
                    or f"relative uncertainty {meson_exchange_input.relative_uncertainty:g}"
                )
            ),
            replaceable_interface="AdditionalNuclearComponentInput",
        ),
        "non_nucleonic": ComponentProvenance(
            name="non-nucleonic quark contribution",
            evidence=(
                EvidenceClass.MODEL
                if non_nucleonic_input is None
                else non_nucleonic_input.evidence
            ),
            mechanism=Mechanism.NON_NUCLEONIC,
            sources=(
                "inactive by default: no six-quark/delta-delta probability input configured"
                if non_nucleonic_input is None
                else non_nucleonic_input.source,
            ),
            assumptions=(
                "exact zero only for the configured nucleonic baseline; not a claim of physical absence",
            ),
            validity=(
                common_validity
                if non_nucleonic_input is None
                else non_nucleonic_input.validity
            ),
            uncertainty_kind=(
                "unresolved component; source-required activation"
                if non_nucleonic_input is None
                else (
                    non_nucleonic_input.uncertainty_description
                    or f"relative uncertainty {non_nucleonic_input.relative_uncertainty:g}"
                )
            ),
            replaceable_interface="AdditionalNuclearComponentInput",
        ),
    }
    return MechanismResolvedQuarkCorrelator(
        proton_impulse, neutron_impulse, corrections, provenance
    )
