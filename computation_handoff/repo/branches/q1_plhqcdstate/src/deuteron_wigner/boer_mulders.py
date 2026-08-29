"""Flavor-resolved phenomenological Boer--Mulders boundary.

The public phenomenology does not currently provide a modern replica release
with the same evolution and machine-readable coverage as BPV20 Sivers.
This module therefore implements the explicitly modeled proportionality
scenario used in SIDIS/Drell--Yan analyses, while retaining independent
operator, flavor, process, and uncertainty identities.  It is not labeled as
a refit and can be replaced by a future tabulated fit without changing the
nucleon or nuclear correlator layers.
"""

from __future__ import annotations

from dataclasses import dataclass, field
import math
from typing import Mapping

from .nucleon_inputs import FittedMomentumTMDInput, ISOSPIN_ROTATION
from .provenance import (
    ComponentProvenance,
    EvidenceClass,
    Mechanism,
    ValidityDomain,
)


@dataclass(frozen=True)
class BoerMuldersFromSiversModel:
    """Operator-specific Boer--Mulders model based on a Sivers boundary.

    ``lambda_by_flavor`` multiplies the *future-staple reference* Sivers TMD.
    The default valence coefficients reproduce the signs and relative
    magnitudes of the Barone--Melis--Prokudin SIDIS analysis summarized in
    the 2026 sign-reversal review.  Sea coefficients are separate named model
    parameters because existing Drell--Yan extractions constrain them only
    weakly.
    """

    sivers: FittedMomentumTMDInput
    lambda_by_flavor: Mapping[int, float] = field(
        default_factory=lambda: {
            2: 2.0,
            1: -1.1,
            -2: 0.35,
            -1: -0.25,
        }
    )
    relative_uncertainty_by_flavor: Mapping[int, float] = field(
        default_factory=lambda: {
            2: 0.50,
            1: 0.70,
            -2: 1.00,
            -1: 1.00,
        }
    )

    def __post_init__(self) -> None:
        required = {2, 1, -2, -1}
        if set(self.lambda_by_flavor) != required:
            raise ValueError("Boer--Mulders model requires u,d,ubar,dbar coefficients")
        if set(self.relative_uncertainty_by_flavor) != required:
            raise ValueError("Boer--Mulders model requires four flavor uncertainties")
        if any(
            not math.isfinite(float(value))
            for value in self.lambda_by_flavor.values()
        ):
            raise ValueError("Boer--Mulders coefficients must be finite")
        if any(
            not math.isfinite(float(value)) or float(value) < 0.0
            for value in self.relative_uncertainty_by_flavor.values()
        ):
            raise ValueError("Boer--Mulders uncertainties must be finite and nonnegative")

    def fitted_input(self) -> FittedMomentumTMDInput:
        """Return the replaceable nucleon-model adapter.

        The adapter carries a SIDIS/future-staple reference. Gauge-link
        reversal is applied exactly once by the correlator layer.
        """

        def response(
            nucleon: str, flavor: int, x: float, k: float, q: float
        ) -> float:
            if nucleon == "proton":
                proton_flavor = flavor
            elif nucleon == "neutron":
                proton_flavor = ISOSPIN_ROTATION.get(flavor, flavor)
            else:
                raise ValueError("nucleon must be proton or neutron")
            if proton_flavor not in self.lambda_by_flavor:
                return 0.0
            return float(
                self.lambda_by_flavor[proton_flavor]
                * self.sivers.value("proton", proton_flavor, x, k, q)
            )

        validity = self.sivers.provenance.validity
        return FittedMomentumTMDInput(
            response=response,
            provenance=ComponentProvenance(
                name="flavor-resolved Boer--Mulders/Sivers proportionality model",
                evidence=EvidenceClass.MODEL,
                mechanism=Mechanism.NUCLEON_IMPULSE,
                sources=(
                    "V. Barone, S. Melis, A. Prokudin, "
                    "Phys. Rev. D 81, 114026 (2010), arXiv:0912.5194",
                    "V. Barone, S. Melis, A. Prokudin, "
                    "Phys. Rev. D 82, 114025 (2010), arXiv:1009.3423",
                    "J.-C. Peng, M.-X. Liu, G. Xu, "
                    "Phys. Lett. B 876, 140415 (2026)",
                    *self.sivers.provenance.sources,
                ),
                assumptions=(
                    "future-pointing SIDIS staple is the reference",
                    "Boer--Mulders and Sivers share the supplied momentum shape",
                    "u and d use distinct phenomenological proportionality factors",
                    "ubar and dbar are independent weakly constrained model factors",
                    "no claim of a joint Boer--Mulders/Sivers fit covariance",
                ),
                validity=ValidityDomain(
                    validity.x_min,
                    validity.x_max,
                    validity.q_min_gev,
                    validity.q_max_gev,
                    validity.k_max_gev,
                    process="SIDIS",
                ),
                uncertainty_kind=(
                    "BPV20 Sivers member uncertainty plus separate flavor-dependent "
                    "Boer--Mulders proportionality sensitivity"
                ),
                replaceable_interface="FittedMomentumTMDInput",
            ),
            process_reference="SIDIS future-pointing gauge link",
        )

    def coefficient_interval(self, flavor: int) -> tuple[float, float]:
        """Return the named one-sigma coefficient sensitivity interval."""

        central = float(self.lambda_by_flavor[flavor])
        error = abs(central) * float(self.relative_uncertainty_by_flavor[flavor])
        return central - error, central + error
