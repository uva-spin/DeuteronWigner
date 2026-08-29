"""Public BPV20 Sivers-fit replicas and their exact nonperturbative boundary.

This module intentionally exposes the fitted BPV20 ``FNP`` factor rather
than calling it an evolved Sivers TMD.  In arTeMiDe the physical b-space TMD
is the product of this factor and the twist-three small-b matching
convolution, transported from the optimal zeta line to the requested
``(mu, zeta)``.  Keeping that distinction in the type/API prevents the
fit boundary from silently becoming a scale-independent TMD model.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import math
from pathlib import Path
import sys

import numpy as np

BPV20_N3LO_REPLICA_PATH = Path(
    "data/vendor/artemide-v2.05/Models/BPV20/Replica-files/BPV20(n3lo).rep"
)
BPV20_ARTEMIDE_COMMIT = "ea0af1a75e21e316c1ac4ece51933988836a6650"
LIGHT_FLAVORS = (2, 1, 3, -2, -1, -3)
ARTEMIDE_HARPY_PATH = Path("data/vendor/artemide-v2.05/harpy")
ARTEMIDE_CONSTANTS_PATH = Path(
    "build/artemide/const-BPV20_n3lo-proton-sivers"
)


@dataclass(frozen=True)
class BPV20ReplicaEnsemble:
    """Strict parser for the public arTeMiDe BPV20 replica release."""

    technical_initial: np.ndarray
    central: np.ndarray
    replicas: np.ndarray
    source_path: Path

    @classmethod
    def load(
        cls, path: str | Path = BPV20_N3LO_REPLICA_PATH
    ) -> "BPV20ReplicaEnsemble":
        source = Path(path)
        technical: dict[int, np.ndarray] = {}
        replicas: dict[int, np.ndarray] = {}
        declared_count: int | None = None
        mode = ""
        lines = source.read_text().splitlines()
        for index, raw in enumerate(lines):
            line = raw.strip()
            if line.startswith("*C"):
                for candidate in lines[index + 1 :]:
                    if candidate.strip() and not candidate.lstrip().startswith("*"):
                        declared_count = int(candidate.strip())
                        break
            elif line.startswith("*D"):
                mode = "technical"
            elif line.startswith("*R"):
                mode = "replicas"
            elif mode and line and not line.startswith("*") and "," in line:
                fields = [field.strip() for field in line.split(",")]
                member = int(fields[0])
                parameters = np.asarray([float(value) for value in fields[1:]])
                if parameters.shape != (14,) or not np.all(np.isfinite(parameters)):
                    raise ValueError(
                        f"BPV20 member {member} must contain 14 finite parameters"
                    )
                target = technical if mode == "technical" else replicas
                if member in target:
                    raise ValueError(f"duplicate BPV20 member {member}")
                target[member] = parameters

        if declared_count != 500:
            raise ValueError(f"expected 500 BPV20 replicas, found declaration {declared_count}")
        if set(technical) != {-1, 0}:
            raise ValueError("BPV20 technical members must be exactly -1 and 0")
        if set(replicas) != set(range(1, declared_count + 1)):
            raise ValueError("BPV20 physical members must be contiguous 1..500")
        if not np.array_equal(technical[-1], technical[0]):
            raise ValueError("BPV20 grid-initialization and central members differ")
        return cls(
            technical_initial=technical[-1],
            central=technical[0],
            replicas=np.stack([replicas[i] for i in range(1, 501)]),
            source_path=source,
        )

    def parameters(self, member: int) -> np.ndarray:
        if member == -1:
            return self.technical_initial.copy()
        if member == 0:
            return self.central.copy()
        if not 1 <= member <= len(self.replicas):
            raise IndexError("BPV20 member must be -1, 0, or 1..500")
        return self.replicas[member - 1].copy()

    def boundary_shape(
        self, flavor: int, x: float, b_gev_inv: float, *, member: int = 0
    ) -> float:
        """Return the exact BPV20 arTeMiDe ``FNP`` factor.

        Flavor uses PDG signs.  The released model has a common light-sea
        shape for ubar and dbar, an independent strange shape, and no fitted
        gluon/heavy-flavor boundary.
        """

        if not 0.0 < x < 1.0:
            raise ValueError("BPV20 x must lie strictly between zero and one")
        if b_gev_inv < 0.0 or not math.isfinite(b_gev_inv):
            raise ValueError("BPV20 b must be finite and nonnegative")
        if flavor not in LIGHT_FLAVORS:
            return 0.0
        lam = self.parameters(member)
        yy = (
            (lam[0] + x * lam[1])
            * b_gev_inv**2
            / math.sqrt(1.0 + abs(lam[2]) * x**2 * b_gev_inv**2)
        )
        profile = math.exp(-yy)
        norm_u = (
            3.0 + lam[6] + lam[7] * (1.0 + lam[6])
        ) / ((lam[6] + 1.0) * (lam[6] + 2.0) * (lam[6] + 3.0))
        norm_d = (
            3.0 + lam[9] + lam[10] * (1.0 + lam[9])
        ) / ((lam[9] + 1.0) * (lam[9] + 2.0) * (lam[9] + 3.0))
        norm_sea = 1.0 / ((lam[12] + 1.0) * (lam[12] + 2.0))
        factors = {
            2: lam[5] * (1.0 - x) * x ** lam[6] * (1.0 + lam[7] * x) / norm_u,
            1: lam[8] * (1.0 - x) * x ** lam[9] * (1.0 + lam[10] * x) / norm_d,
            3: lam[11] * (1.0 - x) * x ** lam[12] / norm_sea,
            -2: lam[13] * (1.0 - x) * x ** lam[12] / norm_sea,
            -1: lam[13] * (1.0 - x) * x ** lam[12] / norm_sea,
            -3: lam[13] * (1.0 - x) * x ** lam[12] / norm_sea,
        }
        return profile * factors[flavor]

    @staticmethod
    def b_star(b_gev_inv: float) -> float:
        """Exact BPV20 regulator used inside the perturbative convolution."""

        if b_gev_inv < 0.0 or not math.isfinite(b_gev_inv):
            raise ValueError("BPV20 b must be finite and nonnegative")
        return b_gev_inv / math.sqrt(1.0 + (b_gev_inv / 500.0) ** 2)

    @staticmethod
    def mu_ope_gev(b_gev_inv: float) -> float:
        """Exact BPV20 OPE scale, with C0 = 2 exp(-gamma_E)."""

        if b_gev_inv <= 0.0 or not math.isfinite(b_gev_inv):
            raise ValueError("BPV20 mu_OPE requires finite positive b")
        c0 = 2.0 * math.exp(-np.euler_gamma)
        return min(c0 / b_gev_inv + 2.0, 1000.0)


class BPV20ArtemideSivers:
    """Evolved BPV20 momentum-space Sivers TMD through reference arTeMiDe.

    The returned convention is the SIDIS/future-pointing-link
    :math:`f_{1T}^{\\perp}(x,k_T;Q,Q^2)` used in Eq. (45) of
    arXiv:2103.03270. Process reversal is applied by the correlator, not here.
    """

    def __init__(
        self,
        ensemble: BPV20ReplicaEnsemble | None = None,
        *,
        constants_path: str | Path = ARTEMIDE_CONSTANTS_PATH,
        harpy_path: str | Path = ARTEMIDE_HARPY_PATH,
    ) -> None:
        self.ensemble = ensemble or BPV20ReplicaEnsemble.load()
        module_path = str(Path(harpy_path).resolve())
        if module_path not in sys.path:
            sys.path.insert(0, module_path)
        try:
            import harpy  # type: ignore[import-not-found]
        except (ImportError, OSError) as exc:
            raise RuntimeError(
                "compiled arTeMiDe/harpy binding unavailable; follow "
                "environment-artemide.yml and tools/prepare_bpv20_artemide.py"
            ) from exc
        constants = Path(constants_path).resolve()
        if not constants.exists():
            raise FileNotFoundError(
                f"prepared BPV20 constants file not found: {constants}"
            )
        harpy.initialize(str(constants))
        self._harpy = harpy
        self._member: int | None = None

    def set_member(self, member: int) -> None:
        if member == self._member:
            return
        self._harpy.setNPparameters_SiversTMDPDF(
            self.ensemble.parameters(member)
        )
        self._member = member

    def set_scale_variation(
        self, c1: float = 1.0, c2: float = 1.0,
        c3: float = 1.0, c4: float = 1.0,
    ) -> None:
        """Reset nominal scales; reject fake variations in the optimal scheme.

        The released BPV20 constants use arTeMiDe's optimal-TMD evolution.
        arTeMiDe explicitly reports that ``c1`` and ``c3`` do not exist in
        this scheme, ``c4`` is ignored by the Sivers module, and ``c2`` acts
        only in process cross sections.  Accepting non-unit factors here
        would therefore manufacture an identically nominal "uncertainty".
        """

        factors = (float(c1), float(c2), float(c3), float(c4))
        if any(not np.isfinite(value) or value <= 0.0 for value in factors):
            raise ValueError("arTeMiDe scale factors must be finite and positive")
        if factors != (1.0, 1.0, 1.0, 1.0):
            raise NotImplementedError(
                "BPV20 optimal-TMD output has no active standalone TMD scale "
                "variation; vary process hard scales in an observable-level "
                "calculation instead"
            )
        self._harpy.varyScales(*factors)
        self._momentum_values.cache_clear()

    def proton_value(
        self,
        flavor: int,
        x: float,
        k_gev: float,
        q_gev: float,
        *,
        member: int = 0,
    ) -> float:
        if flavor not in LIGHT_FLAVORS:
            return 0.0
        if not 0.0 < x < 1.0 or k_gev < 0.0 or q_gev <= 0.0:
            raise ValueError("require 0<x<1, k>=0, and Q>0")
        values = self._momentum_values(member, float(x), float(k_gev), float(q_gev))
        # harpy arrays are ordered by their native Fortran index -5..5.
        return float(values[flavor + 5])

    def proton_b_value(
        self,
        flavor: int,
        x: float,
        b_gev_inv: float,
        q_gev: float,
        *,
        member: int = 0,
    ) -> float:
        """Return evolved SIDIS-reference BPV20 in impact-parameter space."""

        if flavor not in LIGHT_FLAVORS:
            return 0.0
        if not 0.0 < x < 1.0 or b_gev_inv < 0.0 or q_gev <= 0.0:
            raise ValueError("require 0<x<1, b>=0, and Q>0")
        self.set_member(member)
        values = self._harpy.get_SiversTMDPDF(
            float(x), float(b_gev_inv), 1, float(q_gev), float(q_gev**2)
        )
        return float(values[flavor + 5])

    @lru_cache(maxsize=131072)
    def _momentum_values(
        self, member: int, x: float, k_gev: float, q_gev: float
    ) -> tuple[float, ...]:
        self.set_member(member)
        values = self._harpy.get_SiversTMDPDF_kT(
            x, k_gev, 1, q_gev, q_gev**2
        )
        return tuple(float(value) for value in values)

    def fitted_input(self, *, member: int = 0):
        """Build the nucleon-model adapter with explicit fit provenance."""

        from .nucleon_inputs import FittedMomentumTMDInput, ISOSPIN_ROTATION
        from .provenance import (
            ComponentProvenance,
            EvidenceClass,
            Mechanism,
            ValidityDomain,
        )

        def response(
            nucleon: str, flavor: int, x: float, k: float, q: float
        ) -> float:
            if nucleon == "proton":
                proton_flavor = flavor
            elif nucleon == "neutron":
                proton_flavor = ISOSPIN_ROTATION.get(flavor, flavor)
            else:
                raise ValueError("BPV20 nucleon must be proton or neutron")
            return self.proton_value(
                proton_flavor, x, k, q, member=member
            )

        return FittedMomentumTMDInput(
            response=response,
            provenance=ComponentProvenance(
                name=f"BPV20 N3LO Sivers member {member}",
                evidence=EvidenceClass.PHENOMENOLOGY,
                mechanism=Mechanism.NUCLEON_IMPULSE,
                sources=(
                    "M. Bury, A. Prokudin, A. Vladimirov, "
                    "JHEP 05 (2021) 151, arXiv:2103.03270",
                    f"arTeMiDe v2.05 commit {BPV20_ARTEMIDE_COMMIT}",
                    str(self.ensemble.source_path),
                ),
                assumptions=(
                    "SIDIS/future-pointing-link sign is the reference",
                    "exact charge symmetry rotates proton u<->d for neutron",
                    "ubar, dbar, and sbar share the released sea parameterization",
                    "BPV20 optimal-zeta boundary and N3LO evolution are evaluated "
                    "by the released arTeMiDe implementation",
                ),
                validity=ValidityDomain(
                    0.01, 0.25, 1.5, 91.0, 1.5, process="SIDIS"
                ),
                uncertainty_kind="500 fitted Monte Carlo replicas",
                replaceable_interface="FittedMomentumTMDInput",
            ),
            process_reference="SIDIS future-pointing gauge link",
        )


@dataclass(frozen=True)
class BPV20ReplicaMomentumGrid:
    """Exact arTeMiDe/Ogata momentum grid for all BPV20 replicas at fixed Q."""

    x_axis: np.ndarray
    k_axis_gev: np.ndarray
    flavors: tuple[int, ...]
    values: np.ndarray  # (replica, flavor, x, k)
    q_gev: float
    evaluator: str

    def save(self, path: str | Path) -> None:
        """Persist the member-preserving grid without lossy table conversion."""

        destination = Path(path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(
            destination,
            x_axis=self.x_axis,
            k_axis_gev=self.k_axis_gev,
            flavors=np.asarray(self.flavors, dtype=np.int64),
            values=self.values,
            q_gev=np.asarray(self.q_gev),
            evaluator=np.asarray(self.evaluator),
        )

    @classmethod
    def load(cls, path: str | Path) -> "BPV20ReplicaMomentumGrid":
        """Load a grid while retaining the official replica ordering."""

        with np.load(Path(path), allow_pickle=False) as archive:
            return cls(
                x_axis=archive["x_axis"],
                k_axis_gev=archive["k_axis_gev"],
                flavors=tuple(int(value) for value in archive["flavors"]),
                values=archive["values"],
                q_gev=float(archive["q_gev"]),
                evaluator=str(archive["evaluator"]),
            )

    @classmethod
    def generate(
        cls,
        reference: BPV20ArtemideSivers,
        *,
        q_gev: float,
        x_axis: np.ndarray,
        k_axis_gev: np.ndarray,
        flavors: tuple[int, ...] = (2, 1, -2, -1),
    ) -> "BPV20ReplicaMomentumGrid":
        x_values = np.asarray(x_axis, dtype=float)
        k_values = np.asarray(k_axis_gev, dtype=float)
        if (
            x_values.ndim != 1
            or k_values.ndim != 1
            or len(x_values) < 2
            or len(k_values) < 2
            or np.any(np.diff(x_values) <= 0.0)
            or np.any(np.diff(k_values) <= 0.0)
            or x_values[0] <= 0.0
            or x_values[-1] >= 1.0
            or k_values[0] < 0.0
            or q_gev <= 0.0
        ):
            raise ValueError("invalid BPV20 replica momentum-grid axes")
        result = np.empty(
            (
                len(reference.ensemble.replicas),
                len(flavors),
                len(x_values),
                len(k_values),
            )
        )
        for member_index in range(len(reference.ensemble.replicas)):
            member = member_index + 1
            for x_index, x in enumerate(x_values):
                for k_index, k in enumerate(k_values):
                    native = reference._momentum_values(
                        member, float(x), float(k), float(q_gev)
                    )
                    for flavor_index, flavor in enumerate(flavors):
                        result[
                            member_index, flavor_index, x_index, k_index
                        ] = native[flavor + 5]
        return cls(
            x_values,
            k_values,
            flavors,
            result,
            q_gev,
            "arTeMiDe v2.05 native Ogata rank-one transform",
        )

    def interpolate_all(self, flavor: int, x: np.ndarray, k: np.ndarray) -> np.ndarray:
        """Return all replicas at paired x/k points as ``(replica, point)``."""

        if flavor not in self.flavors:
            raise KeyError(f"flavor {flavor} is not in the BPV20 grid")
        xq, kq = np.broadcast_arrays(np.asarray(x, float), np.asarray(k, float))
        output = np.zeros((self.values.shape[0], xq.size))
        valid = (
            (xq.ravel() >= self.x_axis[0])
            & (xq.ravel() <= self.x_axis[-1])
            & (kq.ravel() >= self.k_axis_gev[0])
            & (kq.ravel() <= self.k_axis_gev[-1])
        )
        if not np.any(valid):
            return output
        xv = xq.ravel()[valid]
        kv = kq.ravel()[valid]
        ix = np.clip(np.searchsorted(self.x_axis, xv) - 1, 0, len(self.x_axis)-2)
        ik = np.clip(
            np.searchsorted(self.k_axis_gev, kv) - 1,
            0,
            len(self.k_axis_gev)-2,
        )
        tx = (xv - self.x_axis[ix]) / (self.x_axis[ix+1] - self.x_axis[ix])
        tk = (
            (kv - self.k_axis_gev[ik])
            / (self.k_axis_gev[ik+1] - self.k_axis_gev[ik])
        )
        field = self.values[:, self.flavors.index(flavor)]
        output[:, valid] = (
            (1-tx)*(1-tk)*field[:, ix, ik]
            + tx*(1-tk)*field[:, ix+1, ik]
            + (1-tx)*tk*field[:, ix, ik+1]
            + tx*tk*field[:, ix+1, ik+1]
        )
        return output
