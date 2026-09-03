"""Replaceable non-WW worm-gear and pretzelosity input contracts."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
import math
from typing import Callable, Mapping
from math import gamma

from .nucleon_inputs import FittedScalarTMDInput, ISOSPIN_ROTATION
from .provenance import ComponentProvenance, EvidenceClass, Mechanism, ValidityDomain

Scalar = Callable[[int, float, float], float]


@dataclass(frozen=True)
class Yang2024G1TInput:
    """World-SIDIS central g1T input of arXiv:2403.12795, Eq. (46).

    The published fit sets sea flavors to zero and constrains only u and d.
    This adapter preserves that assumption explicitly; it must be combined
    with a separate sea/WW scenario rather than interpreted as evidence that
    sea worm gears physically vanish.
    """

    n_u: float = 0.0206
    n_d: float = -0.0073
    alpha: float = 16.59
    beta: float = 5.57
    reference_scale_gev: float = 2.0

    def published_interval_members(self) -> tuple["Yang2024G1TInput", ...]:
        """Return the 16 corners of the published asymmetric 68% intervals.

        These are a conservative correlated sensitivity hull. They are not
        the unavailable 1000 fit replicas and do not reproduce their unknown
        covariance.
        """

        intervals = (
            (self.n_u-0.0050, self.n_u+0.0058),
            (self.n_d-0.0082, self.n_d+0.0079),
            (self.alpha-10.11, self.alpha+65.88),
            (self.beta-3.87, self.beta+28.65),
        )
        return tuple(
            Yang2024G1TInput(
                n_u=n_u, n_d=n_d, alpha=alpha, beta=beta,
                reference_scale_gev=self.reference_scale_gev,
            )
            for n_u, n_d, alpha, beta in product(*intervals)
        )

    def fitted_input(self) -> FittedScalarTMDInput:
        beta_norm = gamma(self.alpha + 1.0) * gamma(self.beta + 1.0) / gamma(
            self.alpha + self.beta + 2.0
        )

        def response(nucleon: str, flavor: int, x: float, q: float) -> float:
            del q
            proton_flavor = (
                flavor
                if nucleon == "proton"
                else ISOSPIN_ROTATION.get(flavor, flavor)
                if nucleon == "neutron"
                else None
            )
            if proton_flavor is None:
                raise ValueError("nucleon must be proton or neutron")
            normalization = {2: self.n_u, 1: self.n_d}.get(proton_flavor, 0.0)
            return float(
                normalization
                * (1.0 - x) ** self.alpha
                * x**self.beta
                / beta_norm
            )

        return FittedScalarTMDInput(
            response=response,
            provenance=ComponentProvenance(
                name="Yang et al. world-SIDIS g1T central input",
                evidence=EvidenceClass.PHENOMENOLOGY,
                mechanism=Mechanism.NUCLEON_IMPULSE,
                sources=("arXiv:2403.12795 Eq. (46), Table IV",),
                assumptions=(
                    "published common alpha,beta shape for u and d",
                    "published sea-zero fit boundary retained explicitly",
                    "published fitted moment is used as the replaceable Q0 "
                    "boundary of the project's rank-one J1/CSS adapter; this "
                    "common-kernel continuation is model evolution, not a "
                    "claim of fit-native evolution",
                ),
                validity=ValidityDomain(0.003, 0.5, 1.0, 10.0, 1.0),
                uncertainty_kind=(
                    "1000-replica 68% intervals published for five correlated "
                    "parameters; central only here until replicas/covariance are released"
                ),
                replaceable_interface="Yang2024G1TInput",
            ),
        )


@dataclass(frozen=True)
class WWBreakingModel:
    """Additive genuine-twist-3 breaking around separately supplied WW terms.

    The two worm gears have distinct response maps. Their zero-response member
    is the exact configured WW limit; nonzero members represent genuine
    quark--gluon--quark matrix elements and are never inferred from one
    another.
    """

    g1t_ww: Scalar
    h1lperp_ww: Scalar
    g1t_breaking: Mapping[int, Scalar]
    h1lperp_breaking: Mapping[int, Scalar]
    source: str
    validity: ValidityDomain
    uncertainty_kind: str

    def __post_init__(self) -> None:
        required = {2, 1, -2, -1}
        if set(self.g1t_breaking) != required or set(self.h1lperp_breaking) != required:
            raise ValueError("WW breaking requires u,d,ubar,dbar for both worm gears")
        if not self.source or not self.uncertainty_kind:
            raise ValueError("WW breaking model requires source and uncertainty")

    def _input(self, name: str) -> FittedScalarTMDInput:
        if name == "g1T":
            ww, breaking = self.g1t_ww, self.g1t_breaking
        elif name == "h1Lperp":
            ww, breaking = self.h1lperp_ww, self.h1lperp_breaking
        else:
            raise KeyError(name)

        def response(nucleon: str, flavor: int, x: float, q: float) -> float:
            proton_flavor = (
                flavor
                if nucleon == "proton"
                else ISOSPIN_ROTATION.get(flavor, flavor)
                if nucleon == "neutron"
                else None
            )
            if proton_flavor is None:
                raise ValueError("nucleon must be proton or neutron")
            value = float(ww(proton_flavor, x, q)) + float(
                breaking[proton_flavor](proton_flavor, x, q)
            )
            if not math.isfinite(value):
                raise ValueError("worm-gear input must be finite")
            return value

        return FittedScalarTMDInput(
            response=response,
            provenance=ComponentProvenance(
                name=f"{name} WW plus genuine quark-gluon-quark breaking",
                evidence=EvidenceClass.MODEL,
                mechanism=Mechanism.NUCLEON_IMPULSE,
                sources=(self.source, "leading-twist WW integral relation"),
                assumptions=(
                    "WW and genuine twist-3 pieces are additive at the input scale",
                    "g1T and h1Lperp breaking functions are independent",
                    "exact charge symmetry rotates proton inputs for the neutron",
                ),
                validity=self.validity,
                uncertainty_kind=self.uncertainty_kind,
                replaceable_interface="WWBreakingModel",
            ),
        )

    def g1t_input(self) -> FittedScalarTMDInput:
        return self._input("g1T")

    def h1lperp_input(self) -> FittedScalarTMDInput:
        return self._input("h1Lperp")


@dataclass(frozen=True)
class PretzelosityMomentModel:
    """Flavor-resolved first-moment pretzelosity model/input adapter."""

    moments: Mapping[int, Scalar]
    source: str
    evidence: EvidenceClass
    validity: ValidityDomain
    uncertainty_kind: str

    def __post_init__(self) -> None:
        if set(self.moments) != {2, 1, -2, -1}:
            raise ValueError("pretzelosity model requires u,d,ubar,dbar moments")
        if not self.source or not self.uncertainty_kind:
            raise ValueError("pretzelosity model requires source and uncertainty")

    def fitted_input(self) -> FittedScalarTMDInput:
        def response(nucleon: str, flavor: int, x: float, q: float) -> float:
            proton_flavor = (
                flavor
                if nucleon == "proton"
                else ISOSPIN_ROTATION.get(flavor, flavor)
                if nucleon == "neutron"
                else None
            )
            if proton_flavor is None:
                raise ValueError("nucleon must be proton or neutron")
            return float(self.moments[proton_flavor](proton_flavor, x, q))

        return FittedScalarTMDInput(
            response=response,
            provenance=ComponentProvenance(
                name="flavor-resolved nonperturbative pretzelosity moment",
                evidence=self.evidence,
                mechanism=Mechanism.NUCLEON_IMPULSE,
                sources=(self.source,),
                assumptions=(
                    "input supplies the Gaussian-profile coefficient used by the correlator",
                    "rank-two perturbative small-b matching remains zero",
                    "positivity is tested after composition rather than imposed by clipping",
                ),
                validity=self.validity,
                uncertainty_kind=self.uncertainty_kind,
                replaceable_interface="PretzelosityMomentModel",
            ),
        )


def positivity_informed_pretzelosity_model(
    *,
    unpolarized: Scalar,
    helicity: Scalar,
    widths_gev2: Mapping[int, float],
    fractions: Mapping[int, float] | None = None,
) -> PretzelosityMomentModel:
    """Return a flavor-resolved nonperturbative pretzelosity scenario.

    The first transverse moment is a signed fraction of the pointwise
    positivity ceiling.  Signs and magnitudes are a named model scenario,
    not a fit.  The default follows the commonly obtained opposite u/d signs
    while allowing independent sea components.
    """

    selected = dict(
        fractions or {2: -0.12, 1: 0.18, -2: -0.03, -1: 0.04}
    )
    required = {2, 1, -2, -1}
    if set(selected) != required or set(widths_gev2) != required:
        raise ValueError("pretzelosity scenario requires u,d,ubar,dbar inputs")
    if any(abs(value) > 1.0 for value in selected.values()):
        raise ValueError("pretzelosity fractions must lie in [-1,1]")
    mass_gev = 0.93891897
    moments = {
        flavor: (
            lambda parton, x, q, f=flavor: float(
                selected[f]
                * mass_gev**2
                * max(0.0, unpolarized(f, x, q) - helicity(f, x, q))
                / float(widths_gev2[f])
            )
        )
        for flavor in required
    }
    return PretzelosityMomentModel(
        moments=moments,
        source=(
            "arXiv:1808.10560 perturbative rank-two matching boundary; "
            "model-independent transverse-moment positivity ceiling; "
            "independent signed flavor scenario"
        ),
        evidence=EvidenceClass.MODEL,
        validity=ValidityDomain(1.0e-3, 0.8, 1.3, 100.0, 1.5),
        uncertainty_kind=(
            "named independent u,d,ubar,dbar signed-fraction scenarios; "
            "no probability distribution assigned"
        ),
    )
