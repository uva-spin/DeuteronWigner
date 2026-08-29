"""Numerical charge-symmetry-breaking inputs from paired nucleon PDF sets."""

from __future__ import annotations

from functools import lru_cache
import math
from pathlib import Path
from typing import Any

from .nucleon_inputs import ChargeSymmetryBreakingInput, ISOSPIN_ROTATION
from .provenance import (
    ComponentProvenance,
    EvidenceClass,
    Mechanism,
    ValidityDomain,
)


class MSHT20QEDChargeSymmetryBreaking:
    """QED-induced neutron CSB from the paired MSHT20 QED Hessian sets.

    The correction is

    ``delta_q^n = q_MSHT,QED^n / q_MSHT,QED,isospin-partner^p - 1``.

    Taking the ratio inside the same fit family isolates neutron charge
    symmetry breaking from differences between the project's CT18 baseline
    and MSHT20.  The published paired Hessian member identity is retained in
    the uncertainty calculation.
    """

    proton_set = "MSHT20qed_nnlo"
    neutron_set = "MSHT20qed_nnlo_neutron"
    n_eigenvector_pairs = 38

    def __init__(
        self,
        data_root: str | Path = "data/raw/lhapdf",
        *,
        denominator_floor: float = 1.0e-14,
    ) -> None:
        if denominator_floor <= 0.0:
            raise ValueError("denominator floor must be positive")
        try:
            import lhapdf
        except ImportError as exc:
            raise RuntimeError("LHAPDF is required for the MSHT20 QED CSB input") from exc
        root = str(Path(data_root).resolve())
        paths = list(lhapdf.paths())
        if root not in paths:
            lhapdf.setPaths([root, *paths])
        self._lhapdf: Any = lhapdf
        self._denominator_floor = float(denominator_floor)
        self._central_proton = lhapdf.mkPDF(self.proton_set, 0)
        self._central_neutron = lhapdf.mkPDF(self.neutron_set, 0)
        if int(self._central_proton.info().get_entry("DataVersion")) != 2:
            raise RuntimeError("MSHT20qed_nnlo DataVersion 2 is required")
        if int(self._central_neutron.info().get_entry("DataVersion")) != 3:
            raise RuntimeError("MSHT20qed_nnlo_neutron DataVersion 3 is required")

    @staticmethod
    def _is_supported(nucleon: str, flavor: int, tmd_name: str) -> bool:
        return (
            nucleon == "neutron"
            and flavor in ISOSPIN_ROTATION
            and tmd_name == "f1"
        )

    def _member_delta(
        self,
        proton: Any,
        neutron: Any,
        flavor: int,
        x: float,
        q_gev: float,
        *,
        require_positive_ratio: bool = False,
    ) -> float:
        partner = ISOSPIN_ROTATION[flavor]
        numerator = float(neutron.xfxQ(flavor, x, q_gev))
        denominator = float(proton.xfxQ(partner, x, q_gev))
        if abs(denominator) <= self._denominator_floor:
            raise ValueError(
                "MSHT20 QED CSB ratio has an unresolved isospin-partner denominator"
            )
        result = numerator / denominator - 1.0
        if not math.isfinite(result) or (
            require_positive_ratio and result <= -1.0
        ):
            raise ValueError("MSHT20 QED CSB ratio is nonphysical")
        return result

    @lru_cache(maxsize=None)
    def _member_pair(self, member: int) -> tuple[Any, Any]:
        return (
            self._lhapdf.mkPDF(self.proton_set, member),
            self._lhapdf.mkPDF(self.neutron_set, member),
        )

    @lru_cache(maxsize=4096)
    def response(
        self, nucleon: str, flavor: int, tmd_name: str, x: float, q_gev: float
    ) -> float:
        if not self._is_supported(nucleon, flavor, tmd_name):
            return 0.0
        return self._member_delta(
            self._central_proton,
            self._central_neutron,
            flavor,
            x,
            q_gev,
            require_positive_ratio=True,
        )

    @lru_cache(maxsize=131072)
    def member_response(
        self, member: int, flavor: int, x: float, q_gev: float
    ) -> float:
        """Return one paired proton/neutron Hessian-member CSB response."""

        if member < 0 or member > 2 * self.n_eigenvector_pairs:
            raise ValueError("MSHT20 QED member must lie in [0,76]")
        proton, neutron = (
            (self._central_proton, self._central_neutron)
            if member == 0
            else self._member_pair(member)
        )
        return self._member_delta(
            proton,
            neutron,
            flavor,
            x,
            q_gev,
            require_positive_ratio=(member == 0),
        )

    @lru_cache(maxsize=1024)
    def uncertainty(
        self, nucleon: str, flavor: int, tmd_name: str, x: float, q_gev: float
    ) -> float:
        if not self._is_supported(nucleon, flavor, tmd_name):
            return 0.0
        squared = 0.0
        for pair in range(self.n_eigenvector_pairs):
            plus_member = 2 * pair + 1
            minus_member = plus_member + 1
            proton_plus, neutron_plus = self._member_pair(plus_member)
            proton_minus, neutron_minus = self._member_pair(minus_member)
            delta_plus = self._member_delta(
                proton_plus,
                neutron_plus,
                flavor,
                x,
                q_gev,
            )
            delta_minus = self._member_delta(
                proton_minus,
                neutron_minus,
                flavor,
                x,
                q_gev,
            )
            squared += ((delta_plus - delta_minus) / 2.0) ** 2
        return math.sqrt(squared)

    def as_input(self) -> ChargeSymmetryBreakingInput:
        return ChargeSymmetryBreakingInput(
            response=self.response,
            uncertainty_response=self.uncertainty,
            provenance=ComponentProvenance(
                name="MSHT20 QED neutron charge-symmetry breaking",
                evidence=EvidenceClass.PHENOMENOLOGY,
                mechanism=Mechanism.ISOSPIN_BREAKING,
                sources=(
                    "MSHT20qed_nnlo DataVersion 2",
                    "MSHT20qed_nnlo_neutron DataVersion 3",
                    "T. Cridge et al., Eur. Phys. J. C 82 (2022) 90; arXiv:2111.05357",
                ),
                assumptions=(
                    "paired proton/neutron member identity is correlated",
                    "ratio to the proton isospin partner isolates neutron CSB",
                    "numerical correction applies only to unpolarized f1 amplitudes",
                    "no polarized, transversity, T-odd, or transverse-width CSB inferred",
                ),
                # At Q=5 GeV the central MSHT anti-up grid changes sign near
                # x=0.458.  A multiplicative positive-density correction is
                # therefore declared only through x=0.4.
                validity=ValidityDomain(1.0e-5, 0.4, 1.0, 100.0, 1.5),
                uncertainty_kind=(
                    "symmetric 68% CL Hessian propagation of 38 paired eigenvectors"
                ),
                replaceable_interface="ChargeSymmetryBreakingInput",
            ),
        )
