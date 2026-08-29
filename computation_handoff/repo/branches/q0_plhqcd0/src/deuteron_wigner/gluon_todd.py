"""Process- and color-resolved boundary contract for gluon T-odd TMDs.

Unlike quark T-odd TMDs, a gluon Sivers contribution is not specified by a
future/past staple sign alone.  The two independent three-gluon color
contractions (antisymmetric f-type and symmetric d-type) must remain
separate, and an observable must provide its own hard coefficients.
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from enum import Enum
from typing import Callable, Mapping, Protocol

import numpy as np

from .gtmd import GaugeLink
from .provenance import EvidenceClass, ValidityDomain


class SpinHalfGluonGTMD(Protocol):
    def __call__(
        self,
        x: float,
        k_x: float,
        k_y: float,
        delta_x: float,
        delta_y: float,
        scale: float,
    ) -> np.ndarray: ...


class GluonColorStructure(str, Enum):
    """Independent universal gluon T-odd color contractions."""

    F_TYPE = "f_type_antisymmetric"
    D_TYPE = "d_type_symmetric"


def staple_sign(gauge_link: GaugeLink) -> float:
    """Return time-reversal sign relative to a future-pointing staple.

    Mixed link pairs occur for more general gluon processes and cannot be
    reduced to the simple future/past sign used by this boundary.
    """

    if gauge_link.incoming == gauge_link.outgoing == "+":
        return 1.0
    if gauge_link.incoming == gauge_link.outgoing == "-":
        return -1.0
    raise ValueError(
        "mixed gluon gauge links require an explicit process-specific link "
        "calculation; no SIDIS/DY-like sign is implied"
    )


@dataclass(frozen=True)
class GluonSiversInput:
    """Sourced future-staple f- and d-type gluon Sivers boundaries."""

    components: Mapping[GluonColorStructure, Callable[[float, float, float], float]]
    source: str
    evidence: EvidenceClass
    validity: ValidityDomain
    uncertainty_kind: str
    convention: str

    def __post_init__(self) -> None:
        if set(self.components) != set(GluonColorStructure):
            raise ValueError("both independent f-type and d-type inputs are required")
        if not self.source or not self.uncertainty_kind or not self.convention:
            raise ValueError("source, uncertainty, and convention are required")

    def value(
        self,
        color: GluonColorStructure,
        *,
        x: float,
        k_gev: float,
        q_gev: float,
        gauge_link: GaugeLink,
    ) -> float:
        if not self.validity.contains(x=x, q_gev=q_gev, k_gev=k_gev):
            raise ValueError("gluon Sivers request lies outside the input validity domain")
        value = float(self.components[color](x, k_gev, q_gev))
        if not np.isfinite(value):
            raise ValueError(f"{color.value} gluon Sivers input is not finite")
        return staple_sign(gauge_link) * value


GLUON_TODD_RANKS = {
    "h1Lperp": 2,
    "f1Tperp": 1,
    "h1": 1,
    "h1Tperp": 3,
    "g1LT": 1,
    "g1TT": 2,
}


def gluon_link_sign(
    color: GluonColorStructure, gauge_link: GaugeLink
) -> float:
    """T-reversal sign for the two independent gluon link classes.

    The WW/f-type class uses equal staples and the dipole/d-type class mixed
    staples.  No relation between their magnitudes is implied.
    """

    pair = (gauge_link.incoming, gauge_link.outgoing)
    expected = {
        GluonColorStructure.F_TYPE: {("+", "+"): 1.0, ("-", "-"): -1.0},
        GluonColorStructure.D_TYPE: {("+", "-"): 1.0, ("-", "+"): -1.0},
    }
    try:
        return expected[color][pair]
    except KeyError as error:
        raise ValueError(
            f"{color.value} requires its own WW/dipole link pair; got {pair}"
        ) from error


@dataclass(frozen=True)
class SpectatorInformedGluonTOdd:
    """Source-informed full-vertex boundary for all six spin-1 structures.

    The four nucleon structures reproduce the qualitative full-vertex
    constraints of Bacchetta, Celiberto and Radici (arXiv:2402.17556):
    a dipole tail, sizable Sivers/linearity, a node in ``h1Lperp`` near
    k_T^2=0.1 GeV^2 at x=0.1, and suppressed rank-three ``h1Tperp``.
    Their absolute normalization is a configurable fraction of the local
    unpolarized spin-1 gluon density because the published replica ensemble
    and a Q0->Q TMD evolution fit are unavailable.

    ``g1LT`` and ``g1TT`` are genuine spin-1 extensions.  They use AV18
    S--D coherence and rank-one/rank-two screened-eikonal moments.  They are
    predictions of this model, not quantities calculated in that paper.
    """

    label: str = "spectator_full_vertex_av18_eikonal_central"
    d_state_probability: float = 0.05759854074095002
    sd_coherence: float = 0.3897991321351392
    alpha_s: float = 0.30
    screening_mass_gev: float = 0.36
    dipole_scale_gev: float = 0.90
    # Independent d-type coupling: the published equal-vertex boundary is
    # 5/9; varying this is mandatory because f- and d-type are independent.
    d_type_relative_coupling: float = 5.0 / 9.0
    strength: float = 1.0

    def __post_init__(self) -> None:
        if not self.label or not 0.0 <= self.d_state_probability < 1.0:
            raise ValueError("invalid spectator-informed gluon scenario")
        if not -1.0 <= self.sd_coherence <= 1.0:
            raise ValueError("S-D coherence must lie in [-1,1]")
        if min(
            self.alpha_s,
            self.screening_mass_gev,
            self.dipole_scale_gev,
            self.d_type_relative_coupling,
            self.strength,
        ) <= 0.0:
            raise ValueError("model scales and strengths must be positive")

    def _color_scale(self, color: GluonColorStructure) -> float:
        return (
            1.0
            if color == GluonColorStructure.F_TYPE
            else self.d_type_relative_coupling
        )

    def _eikonal(self, k: float, rank: int) -> float:
        """Stable screened one-gluon harmonic approximation."""

        mu2 = self.screening_mass_gev**2
        lam2 = self.dipole_scale_gev**2
        return float(
            3.0
            * self.alpha_s
            / (2.0 * np.pi)
            * (k / self.dipole_scale_gev) ** rank
            * lam2**2
            / ((k * k + mu2) * (k * k + lam2) ** 2)
        )

    def future_values(
        self,
        color: GluonColorStructure,
        *,
        f1_gev2: float,
        k_gev: float,
    ) -> dict[str, float]:
        """Return future-link radial coefficients before positivity capping."""

        if k_gev < 0.0 or f1_gev2 < 0.0:
            raise ValueError("f1 and transverse momentum must be nonnegative")
        if k_gev == 0.0 or f1_gev2 == 0.0:
            return {name: 0.0 for name in GLUON_TODD_RANKS}
        k2 = k_gev * k_gev
        tail = (self.dipole_scale_gev**2 / (
            self.dipole_scale_gev**2 + k2
        )) ** 2
        color_scale = self._color_scale(color)
        anchor = self.strength * color_scale * f1_gev2 * tail
        tensor_mix = (
            np.sqrt(self.d_state_probability * (1.0-self.d_state_probability))
            * self.sd_coherence
        )
        # Coefficients encode the full-vertex hierarchy, not universal ratios:
        # each radial structure has its own k dependence and zero structure.
        return {
            "f1Tperp": float(0.22 * anchor),
            "h1": float(0.31 * anchor * (1.0 + 0.30*k2)),
            "h1Lperp": float(
                0.055 * anchor * (1.0 - k2 / 0.10)
                / (1.0 + k2 / 0.35)
            ),
            "h1Tperp": float(
                -0.018 * anchor * (1.0 - k2 / 0.045)
                / (1.0 + k2 / 0.25)
            ),
            "g1LT": float(
                0.70 * anchor * tensor_mix * self._eikonal(k_gev, 1)
            ),
            "g1TT": float(
                -0.55 * anchor * tensor_mix * self._eikonal(k_gev, 2)
            ),
        }

    def values(
        self,
        color: GluonColorStructure,
        *,
        f1_gev2: float,
        k_gev: float,
        gauge_link: GaugeLink,
    ) -> dict[str, float]:
        sign = gluon_link_sign(color, gauge_link)
        return {
            name: sign * value
            for name, value in self.future_values(
                color, f1_gev2=f1_gev2, k_gev=k_gev
            ).items()
        }


def add_gluon_todd_with_positivity(
    base,
    *,
    momentum: tuple[float, float],
    radial_values: Mapping[str, float],
    mass_gev: float = 1.87561294257,
    safety_fraction: float = 0.90,
    tolerance: float = 1.0e-11,
):
    """Compose all six structures and cap them against the full 6x6 density.

    A single scale is applied so relative signs, nodes, and dynamical
    hierarchy survive the positivity projection.
    """

    from .gluon_correlator import (
        Spin1GluonCorrelator,
        compose_spin1_gluon_correlator,
    )

    if set(radial_values) != set(GLUON_TODD_RANKS):
        raise ValueError("all six T-odd radial coefficients are required")
    if base.minimum_positivity_eigenvalue() < -tolerance:
        raise ValueError("base gluon correlator is outside positivity domain")
    values = {
        "f1": 0.0, "h1perp": 0.0, "g1": 0.0, "f1LL": 0.0,
        "h1LLperp": 0.0, "g1T": 0.0, "f1LT": 0.0, "h1LT": 0.0,
        "h1LTperp": 0.0, "f1TT_minus_h1TTperp": 0.0,
        "h1TT": 0.0, "h1TTperpperp": 0.0,
        **{name: float(value) for name, value in radial_values.items()},
    }
    correction = compose_spin1_gluon_correlator(momentum, mass_gev, values)

    def candidate(scale: float):
        return Spin1GluonCorrelator(base.values + scale * correction.values)

    if candidate(1.0).minimum_positivity_eigenvalue() >= -tolerance:
        scale = 1.0
    else:
        low, high = 0.0, 1.0
        for _ in range(64):
            middle = 0.5 * (low + high)
            if candidate(middle).minimum_positivity_eigenvalue() >= -tolerance:
                low = middle
            else:
                high = middle
        scale = safety_fraction * low
    result = candidate(scale)
    return result, float(scale), {
        name: float(scale * value) for name, value in radial_values.items()
    }


@dataclass(frozen=True)
class Spin1GluonTOddMultipletInput:
    """Complete modeled spin-1 gluon T-odd f/d boundary.

    The phenomenological gluon Sivers input anchors ``f1Tperp``. Every other
    T-odd structure has an independent dimensionless color coefficient and
    the minimum additional k/M power required by its transverse rank. These
    are named model amplitudes, not consequences of the Sivers fit.
    """

    sivers: GluonSiversInput
    ratios: Mapping[str, Mapping[GluonColorStructure, float]] = field(
        default_factory=lambda: {
            "h1Lperp": {
                GluonColorStructure.F_TYPE: 0.35,
                GluonColorStructure.D_TYPE: -0.25,
            },
            "f1Tperp": {
                GluonColorStructure.F_TYPE: 1.0,
                GluonColorStructure.D_TYPE: 1.0,
            },
            "h1": {
                GluonColorStructure.F_TYPE: -0.45,
                GluonColorStructure.D_TYPE: 0.30,
            },
            "h1Tperp": {
                GluonColorStructure.F_TYPE: 0.12,
                GluonColorStructure.D_TYPE: -0.08,
            },
            "g1LT": {
                GluonColorStructure.F_TYPE: 0.25,
                GluonColorStructure.D_TYPE: 0.20,
            },
            "g1TT": {
                GluonColorStructure.F_TYPE: -0.10,
                GluonColorStructure.D_TYPE: 0.15,
            },
        }
    )
    mass_gev: float = 1.87561294257
    label: str = "independent_rank_scaled_todd_multiplet"

    def __post_init__(self) -> None:
        if set(self.ratios) != set(GLUON_TODD_RANKS):
            raise ValueError("gluon T-odd multiplet must cover all six structures")
        if any(set(values) != set(GluonColorStructure) for values in self.ratios.values()):
            raise ValueError("every gluon T-odd structure requires f- and d-type ratios")
        if any(
            not np.isfinite(value)
            for values in self.ratios.values()
            for value in values.values()
        ):
            raise ValueError("gluon T-odd multiplet ratios must be finite")
        if self.mass_gev <= 0.0 or not self.label:
            raise ValueError("gluon T-odd multiplet requires a mass and label")

    def value(
        self,
        tmd_name: str,
        color: GluonColorStructure,
        *,
        x: float,
        k_gev: float,
        q_gev: float,
        gauge_link: GaugeLink,
    ) -> float:
        if tmd_name not in GLUON_TODD_RANKS:
            raise KeyError(tmd_name)
        sivers = self.sivers.value(
            color, x=x, k_gev=k_gev, q_gev=q_gev, gauge_link=gauge_link
        )
        extra_rank = GLUON_TODD_RANKS[tmd_name] - 1
        return float(
            self.ratios[tmd_name][color]
            * (k_gev / self.mass_gev) ** extra_rank
            * sivers
        )

    def correlator(
        self,
        color: GluonColorStructure,
        *,
        x: float,
        k_x_gev: float,
        k_y_gev: float,
        q_gev: float,
        gauge_link: GaugeLink,
    ):
        """Compose the full spin-1 correlator carrying this color component."""

        from .gluon_correlator import compose_spin1_gluon_correlator

        k = float(np.hypot(k_x_gev, k_y_gev))
        values = {
            "f1": 0.0,
            "h1perp": 0.0,
            "g1": 0.0,
            "f1LL": 0.0,
            "h1LLperp": 0.0,
            "g1T": 0.0,
            "f1LT": 0.0,
            "h1LT": 0.0,
            "h1LTperp": 0.0,
            "f1TT_minus_h1TTperp": 0.0,
            "h1TT": 0.0,
            "h1TTperpperp": 0.0,
        }
        values.update({
            name: self.value(
                name,
                color,
                x=x,
                k_gev=k,
                q_gev=q_gev,
                gauge_link=gauge_link,
            )
            for name in GLUON_TODD_RANKS
        })
        return compose_spin1_gluon_correlator(
            (k_x_gev, k_y_gev), self.mass_gev, values
        )


@dataclass(frozen=True)
class CGIGPMGluonSiversParameters:
    """Parameters of the Gaussian CGI-GPM boundary in arXiv:1902.02425."""

    n_f: float = 0.02
    n_d: float = 0.0
    rho: float = 2.0 / 3.0
    unpolarized_width_gev2: float = 1.0
    alpha_f: float = 0.0
    beta_f: float = 0.0
    alpha_d: float = 0.0
    beta_d: float = 0.0
    label: str = "central_midpoint"

    def __post_init__(self) -> None:
        if abs(self.n_f) > 1.0 or abs(self.n_d) > 1.0:
            raise ValueError("CGI-GPM normalizations must obey |N_g|<=1")
        if not 0.0 < self.rho < 1.0 or self.unpolarized_width_gev2 <= 0.0:
            raise ValueError("CGI-GPM rho and width are outside their domains")
        if min(self.alpha_f, self.beta_f, self.alpha_d, self.beta_d) < 0.0:
            raise ValueError("CGI-GPM x-shape powers must be nonnegative")
        if not self.label:
            raise ValueError("CGI-GPM scenario requires a label")


def _normalized_beta_shape(x: float, alpha: float, beta: float) -> float:
    if alpha == beta == 0.0:
        return 1.0
    normalization = (
        (alpha + beta) ** (alpha + beta)
        / (alpha**alpha * beta**beta)
    )
    return float(x**alpha * (1.0 - x) ** beta * normalization)


def build_cgi_gpm_gluon_sivers_input(
    gluon_pdf: Callable[[float, float], float],
    parameters: CGIGPMGluonSiversParameters = CGIGPMGluonSiversParameters(),
) -> GluonSiversInput:
    """Build the independent f/d boundary from Eqs. (5)--(8) of 1902.02425."""

    width = float(parameters.unpolarized_width_gev2)
    mprime2 = parameters.rho * width / (1.0 - parameters.rho)
    mprime = float(np.sqrt(mprime2))
    proton_mass = 0.9382720813

    def component(
        normalization: float, alpha: float, beta: float
    ) -> Callable[[float, float, float], float]:
        def value(x: float, k: float, q: float) -> float:
            collinear = float(gluon_pdf(x, q))
            if not np.isfinite(collinear) or collinear < 0.0:
                raise ValueError("unpolarized gluon PDF must be finite and nonnegative")
            nx = normalization * _normalized_beta_shape(x, alpha, beta)
            # Eq. (5): Delta^N f=-2 k/M f1Tperp. The k in h(k)
            # cancels analytically, leaving a finite origin.
            return float(
                -proton_mass
                * nx
                * collinear
                * np.sqrt(2.0 * np.e)
                / mprime
                * np.exp(-k**2 / mprime2)
                * np.exp(-k**2 / width)
                / (np.pi * width)
            )

        return value

    return GluonSiversInput(
        components={
            GluonColorStructure.F_TYPE: component(
                parameters.n_f, parameters.alpha_f, parameters.beta_f
            ),
            GluonColorStructure.D_TYPE: component(
                parameters.n_d, parameters.alpha_d, parameters.beta_d
            ),
        },
        source=(
            "U. D'Alesio et al., Phys. Rev. D 99, 036013 (2019), "
            "arXiv:1902.02425, Eqs. (5)-(8), scenario "
            f"{parameters.label}"
        ),
        evidence=EvidenceClass.PHENOMENOLOGY,
        validity=ValidityDomain(0.005, 0.6, np.sqrt(2.0), 20.0, 1.5),
        uncertainty_kind=(
            "named correlated CGI-GPM scenarios: "
            "-0.01<=N_f<=0.05 and -0.15<=N_d<=0.15"
        ),
        convention=(
            "future-staple reference f1Tperp in "
            "Delta^N f=-2 k_T/M_p f1Tperp; f and d color tensors separate"
        ),
    )


def cgi_gpm_gluon_sivers_scenarios() -> tuple[CGIGPMGluonSiversParameters, ...]:
    """Return the correlated endpoint scenarios stated around Eq. (8)."""

    return (
        CGIGPMGluonSiversParameters(
            n_f=0.02, n_d=0.0, label="central_midpoint"
        ),
        CGIGPMGluonSiversParameters(
            n_f=0.05, n_d=-0.15, label="negative_d_endpoint"
        ),
        CGIGPMGluonSiversParameters(
            n_f=-0.01, n_d=0.15, label="positive_d_endpoint"
        ),
    )


@dataclass(frozen=True)
class GluonTWeightedProcess:
    """Observable-specific hard weights multiplying universal f/d inputs."""

    name: str
    coefficients: Mapping[GluonColorStructure, float]
    source: str
    factorization_statement: str

    def __post_init__(self) -> None:
        if set(self.coefficients) != set(GluonColorStructure):
            raise ValueError("process must specify both f-type and d-type coefficients")
        if not self.name or not self.source or not self.factorization_statement:
            raise ValueError("process name, source, and factorization statement are required")
        values = np.asarray(tuple(self.coefficients.values()), dtype=float)
        if not np.all(np.isfinite(values)):
            raise ValueError("process hard coefficients must be finite")

    def compose(
        self,
        boundary: GluonSiversInput,
        *,
        x: float,
        k_gev: float,
        q_gev: float,
        gauge_link: GaugeLink,
    ) -> float:
        return float(
            sum(
                self.coefficients[color]
                * boundary.value(
                    color,
                    x=x,
                    k_gev=k_gev,
                    q_gev=q_gev,
                    gauge_link=gauge_link,
                )
                for color in GluonColorStructure
            )
        )


@dataclass(frozen=True)
class SiversAugmentedSpinHalfGluonGTMD:
    """Add a sourced process-weighted Sivers tensor to a T-even GTMD.

    The supplied boundary is forward-only.  Nonzero transfer is refused
    because a TMD does not determine the corresponding off-forward GTMD.
    """

    t_even_gtmd: SpinHalfGluonGTMD
    boundary: GluonSiversInput
    process: GluonTWeightedProcess
    gauge_link: GaugeLink
    nucleon_mass_gev: float
    momentum_unit_to_gev: float = 1.0
    transfer_tolerance: float = 1.0e-14
    zero_outside_boundary_validity: bool = True

    def __post_init__(self) -> None:
        if self.nucleon_mass_gev <= 0.0 or self.momentum_unit_to_gev <= 0.0:
            raise ValueError("mass and momentum conversion must be positive")
        if self.transfer_tolerance < 0.0:
            raise ValueError("transfer tolerance cannot be negative")
        staple_sign(self.gauge_link)

    def __call__(
        self,
        x: float,
        k_x: float,
        k_y: float,
        delta_x: float,
        delta_y: float,
        scale: float,
    ) -> np.ndarray:
        if np.hypot(delta_x, delta_y) > self.transfer_tolerance:
            raise ValueError(
                "forward gluon Sivers TMD cannot be promoted to nonzero-transfer GTMD"
            )
        result = np.asarray(
            self.t_even_gtmd(x, k_x, k_y, delta_x, delta_y, scale),
            dtype=np.complex128,
        ).copy()
        if result.shape != (2, 2, 2, 2):
            raise ValueError("T-even nucleon gluon GTMD must have shape (2,2,2,2)")
        from .gluon_correlator import (
            GluonTargetPolarization,
            compose_polarized_gluon_correlator,
        )
        from .registry import TargetChannel

        k_gev = self.momentum_unit_to_gev * np.asarray((k_x, k_y), dtype=float)
        k_norm = float(np.linalg.norm(k_gev))
        if (
            self.zero_outside_boundary_validity
            and not self.boundary.validity.contains(
                x=x, q_gev=scale, k_gev=k_norm
            )
        ):
            sivers = 0.0
        else:
            sivers = self.process.compose(
                self.boundary,
                x=x,
                k_gev=k_norm,
                q_gev=scale,
                gauge_link=self.gauge_link,
            )
        zeros = {
            "f1Tperp": sivers,
            "g1T": 0.0,
            "h1": 0.0,
            "h1Tperp": 0.0,
        }
        sigma_x = np.asarray(((0.0, 1.0), (1.0, 0.0)), dtype=np.complex128)
        sigma_y = np.asarray(((0.0, -1j), (1j, 0.0)), dtype=np.complex128)
        for sigma, spin in (
            (sigma_x, (1.0, 0.0)),
            (sigma_y, (0.0, 1.0)),
        ):
            transverse = compose_polarized_gluon_correlator(
                TargetChannel.T,
                k_gev,
                self.nucleon_mass_gev,
                GluonTargetPolarization(spin_transverse=spin),
                zeros,
            )
            result += np.einsum("ac,ij->acij", sigma, transverse)
        if not np.allclose(
            result.transpose(1, 0, 3, 2).conj(), result, atol=1.0e-12, rtol=0
        ):
            raise ValueError("augmented nucleon gluon correlator is not Hermitian")
        return result
