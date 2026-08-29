"""Sourced pion intrinsic-TMD profile and nuclear transverse composition."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import re
import sys
from typing import Any

import numpy as np
from scipy.integrate import quad
from scipy.special import j0

from .pion_exchange import (
    FockNormalizedMillerPionDistribution,
    JAM21IsoscalarPionPDF,
    MillerTensorPionDistribution,
)
from .quark_correlator import Spin1QuarkCorrelator
from .gluon_correlator import DELTA_T
from .tmd_evolution import OneLoopQuarkCSSEvolution


ARTEMIDE_HARPY_PATH = Path("data/vendor/artemide-v2.05/harpy")
VPION19_NATIVE_CONSTANTS = Path("build/artemide/const-Vpion19-native")


@dataclass(frozen=True)
class Vpion19IntrinsicProfile:
    """Vpion19 nonperturbative factor from arXiv:1907.10356.

    This is the fitted multiplicative large-b factor, not the complete TMD.
    Its original OPE used JAM18 and the BSV19 evolution scheme. Applying it
    to JAM21 is therefore exposed as a scheme/input-transfer scenario.
    """

    member: int = 0
    source_path: str | Path = (
        "data/vendor/artemide-v2.05/Models/Vpion19/uTMDPDF_model.f90"
    )

    def __post_init__(self) -> None:
        if not 0 <= self.member <= 100:
            raise ValueError("Vpion19 member must lie in [0,100]")

    @staticmethod
    @lru_cache(maxsize=4)
    def _parameters(path: str) -> np.ndarray:
        text = Path(path).read_text()
        match = re.search(
            r"dimension\(1:309\)::replicas=\(/&(.*?)\n\s*allocate",
            text,
            flags=re.DOTALL,
        )
        if match is None:
            raise ValueError("cannot locate Vpion19 replica table")
        clean = re.sub(r"!.*", "", match.group(1))
        values = np.asarray(
            [
                float(value.replace("d", "e").replace("D", "E"))
                for value in re.findall(
                    r"[+-]?(?:\d+\.\d*|\.\d+|\d+)(?:[eEdD][+-]?\d+)?",
                    clean,
                )
            ]
        )
        if values.size != 309:
            raise ValueError(f"expected 309 Vpion19 parameters, found {values.size}")
        return values.reshape(103, 3)

    @property
    def parameters(self) -> tuple[float, float, float]:
        # The Fortran table reserves two leading triples; replica 0 is row 2.
        row = self._parameters(str(self.source_path))[self.member + 2]
        return tuple(float(value) for value in row)

    def factor(self, x: float, b_gev_inv: float) -> float:
        if not 0.0 <= x <= 1.0:
            raise ValueError("pion momentum fraction must lie in [0,1]")
        if b_gev_inv < 0.0:
            raise ValueError("impact parameter must be nonnegative")
        a1, a2, a3 = self.parameters
        width = a1 + (1.0 - x) ** 2 * a2
        return float(np.exp(-width * b_gev_inv**2 / np.sqrt(1.0 + a3 * b_gev_inv**2)))


@dataclass
class TransverseSpinAveragedPionBoundary:
    """Nuclear pion contribution at the nonperturbative b-space boundary."""

    splitting: MillerTensorPionDistribution
    pion_pdf: JAM21IsoscalarPionPDF
    intrinsic_profile: Vpion19IntrinsicProfile
    y_max: float = 2.0

    def value(self, flavor: int, x: float, b_gev_inv: float, q_gev: float) -> float:
        if not 0.0 < x < self.y_max:
            return 0.0
        return float(
            quad(
                lambda y: (
                    self.pion_pdf.value(flavor, x / y, q_gev)
                    * self.intrinsic_profile.factor(x / y, b_gev_inv)
                    * self.splitting.spin_averaged_f_b(
                        y, x / y, b_gev_inv
                    )
                    / y
                ),
                x,
                self.y_max,
                epsabs=2.0e-8,
                epsrel=4.0e-4,
                limit=180,
            )[0]
        )


@dataclass
class SpinResolvedTransversePionBoundary:
    """Flavor-resolved NNπ vector correlator at a common TMD b boundary.

    The pion has spin zero, so it contributes to the quark vector projection.
    The deuteron U and LL dependence resides in the three sourced pion
    splitting projections. Off-diagonal/vector target polarization and
    pion axial/transversity operators remain exactly absent in this
    Sullivan component rather than being filled by an ansatz.
    """

    splitting: MillerTensorPionDistribution | FockNormalizedMillerPionDistribution
    pion_pdf: JAM21IsoscalarPionPDF
    intrinsic_profile: Vpion19IntrinsicProfile
    y_max: float = 2.0

    def helicity_value(
        self,
        helicity: int,
        flavor: int,
        x: float,
        b_gev_inv: float,
        q_gev: float,
    ) -> float:
        if helicity not in (-1, 0, 1):
            raise ValueError("deuteron helicity must be -1,0,+1")
        if not 0.0 < x < self.y_max:
            return 0.0
        return float(
            quad(
                lambda y: (
                    self.pion_pdf.value(flavor, x / y, q_gev)
                    * self.intrinsic_profile.factor(x / y, b_gev_inv)
                    * self.splitting.spin_projection_f_b(
                        helicity, y, x / y, b_gev_inv
                    )
                    / y
                ),
                x,
                self.y_max,
                epsabs=2.0e-8,
                epsrel=4.0e-4,
                limit=180,
            )[0]
        )

    def correlator_b(
        self, flavor: int, x: float, b_gev_inv: float, q_gev: float
    ) -> Spin1QuarkCorrelator:
        diagonal = np.asarray([
            self.helicity_value(1, flavor, x, b_gev_inv, q_gev),
            self.helicity_value(0, flavor, x, b_gev_inv, q_gev),
            self.helicity_value(-1, flavor, x, b_gev_inv, q_gev),
        ])
        return Spin1QuarkCorrelator(
            vector=np.diag(diagonal).astype(np.complex128),
            axial=np.zeros((3, 3), dtype=np.complex128),
            transverse=np.zeros((2, 3, 3), dtype=np.complex128),
        )

    def correlators_k(
        self,
        flavor: int,
        x: float,
        k_values_gev: np.ndarray,
        q_gev: float,
        *,
        b_max_gev_inv: float = 12.0,
        b_nodes: int = 64,
    ) -> tuple[Spin1QuarkCorrelator, ...]:
        """Fourier--Bessel transform the rank-zero U/LL pion correlator.

        The convention is
        ``F(k)=1/(2*pi) integral b db J0(b k) Phi(b)``.  All k values share
        one evaluated b-grid, which keeps the nested Sullivan convolution
        reproducible and avoids an independent Gaussian completion.
        """

        momentum = np.asarray(k_values_gev, dtype=float)
        if momentum.ndim != 1 or np.any(momentum < 0.0):
            raise ValueError("pion transverse momenta must be a nonnegative vector")
        if b_max_gev_inv <= 0.0 or b_nodes < 24:
            raise ValueError("pion Hankel transform requires a resolved physical grid")
        nodes, weights = np.polynomial.legendre.leggauss(b_nodes)
        b = b_max_gev_inv * (nodes + 1.0) / 2.0
        b_weights = b_max_gev_inv * weights / 2.0
        diagonal_b = np.asarray(
            [
                [
                    self.helicity_value(helicity, flavor, x, float(value), q_gev)
                    for value in b
                ]
                for helicity in (1, 0, -1)
            ],
            dtype=float,
        )
        kernel = j0(np.outer(momentum, b)) * (b * b_weights)[None, :] / (
            2.0 * np.pi
        )
        diagonal_k = kernel @ diagonal_b.T
        return tuple(
            Spin1QuarkCorrelator(
                vector=np.diag(values).astype(np.complex128),
                axial=np.zeros((3, 3), dtype=np.complex128),
                transverse=np.zeros((2, 3, 3), dtype=np.complex128),
            )
            for values in diagonal_k
        )


@dataclass
class SpinResolvedTransversePionGluonBoundary:
    """Spin-zero pion gluon density in the spin-1 nuclear helicity basis."""

    splitting: MillerTensorPionDistribution | FockNormalizedMillerPionDistribution
    pion_pdf: JAM21IsoscalarPionPDF
    intrinsic_profile: Vpion19IntrinsicProfile
    y_max: float = 2.0

    def _helicity_value(
        self, helicity: int, x: float, b_gev_inv: float, q_gev: float
    ) -> float:
        if helicity not in (-1, 0, 1):
            raise ValueError("deuteron helicity must be -1,0,+1")
        if not 0.0 < x < self.y_max:
            return 0.0
        return float(
            quad(
                lambda y: (
                    self.pion_pdf.value(21, x / y, q_gev)
                    * self.intrinsic_profile.factor(x / y, b_gev_inv)
                    * self.splitting.spin_projection_f_b(
                        helicity, y, x / y, b_gev_inv
                    )
                    / y
                ),
                x, self.y_max,
                epsabs=2.0e-8, epsrel=4.0e-4, limit=180,
            )[0]
        )

    def correlators_k(
        self,
        x: float,
        k_values_gev: np.ndarray,
        q_gev: float,
        *,
        b_max_gev_inv: float = 12.0,
        b_nodes: int = 64,
    ) -> tuple[np.ndarray, ...]:
        momentum = np.asarray(k_values_gev, dtype=float)
        if momentum.ndim != 1 or np.any(momentum < 0.0):
            raise ValueError("pion transverse momenta must be nonnegative")
        if b_max_gev_inv <= 0.0 or b_nodes < 24:
            raise ValueError("pion Hankel transform requires a resolved grid")
        nodes, weights = np.polynomial.legendre.leggauss(b_nodes)
        b = b_max_gev_inv * (nodes + 1.0) / 2.0
        b_weights = b_max_gev_inv * weights / 2.0
        diagonal_b = np.asarray([
            [
                self._helicity_value(helicity, x, float(value), q_gev)
                for value in b
            ]
            for helicity in (1, 0, -1)
        ])
        kernel = (
            j0(np.outer(momentum, b)) * (b * b_weights)[None, :]
            / (2.0 * np.pi)
        )
        diagonal_k = kernel @ diagonal_b.T
        return tuple(
            np.einsum(
                "IH,ij->IHij",
                np.diag(values).astype(np.complex128),
                DELTA_T,
            )
            for values in diagonal_k
        )


@dataclass
class EvolvedTransversePionScenario:
    """Route the pion boundary through the current rank-zero CSS scenario."""

    boundary: TransverseSpinAveragedPionBoundary
    evolution: OneLoopQuarkCSSEvolution
    b_max_gev_inv: float = 1.5

    def value(self, flavor: int, x: float, b_gev_inv: float, q_gev: float) -> float:
        if b_gev_inv < 0.0 or self.b_max_gev_inv <= 0.0:
            raise ValueError("impact parameters and b_max must be physical")
        b_star = b_gev_inv / np.sqrt(1.0 + (b_gev_inv / self.b_max_gev_inv) ** 2)
        initial_scale = self.evolution.canonical_scale(float(b_star), q_gev)
        initial = self.boundary.value(
            flavor, x, b_gev_inv, initial_scale
        )
        return float(
            initial
            * self.evolution.factor(
                b_gev_inv, float(b_star), q_gev
            )
        )

    @property
    def metadata(self) -> dict[str, object]:
        return {
            "rank": 0,
            "scheme": self.evolution.metadata,
            "production_ready": False,
            "limitations": (
                "Vpion19-to-JAM21 input transfer and current one-loop quark "
                "CSS evolution scenario; not an order-consistent pion refit"
            ),
        }


class Vpion19ArtemidePionTMD:
    """High-order Vpion19/JAM21-transfer pion TMD from native arTeMiDe.

    The original Vpion19 fit used JAM18, which is no longer distributed by
    the official LHAPDF archive.  The dedicated reproducible constants file
    substitutes maintained JAM21 while retaining the fitted Vpion19 profile,
    NNLO small-b coefficients, and BSV19 NNNLO evolution.  This is more
    order-consistent than the one-loop adapter, but remains an input-transfer
    scenario rather than a refit.

    arTeMiDe is process-global and cannot be reinitialized safely with a
    different constants file. Production scripts using this class must run
    in their own process, separate from BPV20 initialization.
    """

    def __init__(
        self,
        member: int = 0,
        *,
        constants_path: str | Path = VPION19_NATIVE_CONSTANTS,
        harpy_path: str | Path = ARTEMIDE_HARPY_PATH,
        data_root: str | Path = "data/raw/lhapdf",
        backend: Any | None = None,
    ) -> None:
        if not 0 <= member <= 100:
            raise ValueError("Vpion19 member must lie in [0,100]")
        if backend is None:
            try:
                import lhapdf
            except ImportError as exc:
                raise RuntimeError("LHAPDF is required for native Vpion19") from exc
            root = str(Path(data_root).resolve())
            paths = list(lhapdf.paths())
            if root not in paths:
                lhapdf.setPaths([root, *paths])
            module_path = str(Path(harpy_path).resolve())
            if module_path not in sys.path:
                sys.path.insert(0, module_path)
            try:
                import harpy  # type: ignore[import-not-found]
            except (ImportError, OSError) as exc:
                raise RuntimeError(
                    "compiled arTeMiDe/harpy binding unavailable; follow "
                    "environment-artemide.yml"
                ) from exc
            constants = Path(constants_path).resolve()
            if not constants.exists():
                raise FileNotFoundError(
                    "prepare native pion constants with "
                    "tools/prepare_vpion19_artemide.py"
                )
            harpy.initialize(str(constants))
            backend = harpy
        self._harpy = backend
        self._member: int | None = None
        self.set_member(member)

    def set_member(self, member: int) -> None:
        if not 0 <= member <= 100:
            raise ValueError("Vpion19 member must lie in [0,100]")
        if member != self._member:
            self._harpy.setNPparameters_uTMDPDF(int(member))
            self._member = member

    def charged_pion_b_value(
        self, flavor: int, x: float, b_gev_inv: float, q_gev: float
    ) -> float:
        """Return the native pi- TMD for one LHAPDF light flavor."""

        if flavor not in (-2, -1, 1, 2):
            raise ValueError("only u,d,ubar,dbar pion flavors are supported")
        if not 0.0 < x < 1.0 or b_gev_inv < 0.0 or q_gev <= 0.0:
            raise ValueError("require 0<x<1, b>=0, and Q>0")
        values = self._harpy.get_uTMDPDF(
            float(x), float(b_gev_inv), 2, float(q_gev), float(q_gev**2)
        )
        return float(values[flavor + 5])

    def isoscalar_b_value(
        self, flavor: int, x: float, b_gev_inv: float, q_gev: float
    ) -> float:
        """Charge-average appropriate to isoscalar deuteron pion exchange."""

        return 0.5 * (
            self.charged_pion_b_value(flavor, x, b_gev_inv, q_gev)
            + self.charged_pion_b_value(-flavor, x, b_gev_inv, q_gev)
        )

    @property
    def metadata(self) -> dict[str, object]:
        return {
            "rank": 0,
            "matching_order": "NNLO",
            "evolution_order": "NNNLO (BSV19 optimal-TMD setup)",
            "nonperturbative_model": "Vpion19 member identity 0..100",
            "collinear_input": "JAM21PionPDFnlo member 0 substitution",
            "production_ready": False,
            "validity": "low-kT W-term b-space input",
            "limitations": (
                "JAM18 is unavailable from the official archive; JAM21 "
                "substitution has not been refitted; no fixed-order Y term"
            ),
        }


@dataclass
class NativeEvolvedTransversePionScenario:
    """Compose fit-native pion TMD evolution with exact nuclear recoil."""

    splitting: MillerTensorPionDistribution
    pion_tmd: Vpion19ArtemidePionTMD
    y_max: float = 2.0

    def value(self, flavor: int, x: float, b_gev_inv: float, q_gev: float) -> float:
        if not 0.0 < x < self.y_max:
            return 0.0
        if b_gev_inv < 0.0 or q_gev <= 0.0:
            raise ValueError("require b>=0 and Q>0")
        return float(
            quad(
                lambda y: (
                    self.pion_tmd.isoscalar_b_value(
                        flavor, x / y, b_gev_inv, q_gev
                    )
                    * self.splitting.spin_averaged_f_b(
                        y, x / y, b_gev_inv
                    )
                    / y
                ),
                x,
                self.y_max,
                epsabs=2.0e-8,
                epsrel=4.0e-4,
                limit=180,
            )[0]
        )

    @property
    def metadata(self) -> dict[str, object]:
        return {
            **self.pion_tmd.metadata,
            "nuclear_recoil": "Miller Sullivan kernel with exact J0(z b qT)",
        }
