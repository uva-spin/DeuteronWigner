"""Replaceable pointwise transversity inputs from published fit grids."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from scipy.interpolate import PchipInterpolator


@dataclass(frozen=True)
class TransversityEstimate:
    mean: float
    standard_deviation: float


class JAMDiFFTransversityGrid:
    """Interpolate JAMDiFF replica mean/std without extrapolation."""

    def __init__(self, path: str | Path):
        frame = pd.read_csv(path)
        required = {"Q2_GeV2", "x", "flavor", "xh1_mean", "xh1_std"}
        if not required.issubset(frame.columns):
            raise ValueError(f"missing columns: {sorted(required - set(frame.columns))}")
        self._q2 = np.sort(frame.Q2_GeV2.unique())
        self._curves: dict[tuple[int, float, str], PchipInterpolator] = {}
        for (flavor, q2), group in frame.groupby(["flavor", "Q2_GeV2"]):
            group = group.sort_values("x")
            if group.x.duplicated().any() or np.any(group.x <= 0.0):
                raise ValueError("x grid must be unique and positive")
            for field in ("xh1_mean", "xh1_std"):
                self._curves[(int(flavor), float(q2), field)] = PchipInterpolator(
                    np.log(group.x.to_numpy()),
                    group[field].to_numpy(),
                    extrapolate=False,
                )
        self.x_min = float(frame.x.min())
        self.x_max = float(frame.x.max())
        self.scale_min_gev = float(np.sqrt(self._q2.min()))
        self.scale_max_gev = float(np.sqrt(self._q2.max()))

    def estimate(self, flavor: int, x: float, scale_gev: float) -> TransversityEstimate:
        q2 = float(scale_gev) ** 2
        if flavor not in (2, 1, -2, -1):
            raise ValueError("JAMDiFF grid contains u,d,ubar,dbar only")
        if not self.x_min <= x <= 1.0:
            raise ValueError(f"x={x} outside [{self.x_min}, 1]")
        if not self._q2[0] <= q2 <= self._q2[-1]:
            raise ValueError(f"Q2={q2} outside [{self._q2[0]}, {self._q2[-1]}]")
        upper = int(np.searchsorted(self._q2, q2, side="right"))
        upper = min(max(upper, 1), len(self._q2) - 1)
        qlo, qhi = self._q2[upper - 1], self._q2[upper]
        weight = 0.0 if qhi == qlo else (
            (np.log(q2) - np.log(qlo)) / (np.log(qhi) - np.log(qlo))
        )

        tabulated_x = min(x, self.x_max)
        endpoint_factor = (
            1.0 if x <= self.x_max else (1.0 - x) / (1.0 - self.x_max)
        )

        def interpolate(field: str) -> float:
            lo = float(self._curves[(flavor, float(qlo), field)](
                np.log(tabulated_x)
            ))
            hi = float(self._curves[(flavor, float(qhi), field)](
                np.log(tabulated_x)
            ))
            return endpoint_factor * ((1.0 - weight) * lo + weight * hi)

        # Upstream tabulates x*h1.
        return TransversityEstimate(
            mean=(0.0 if x == 1.0 else interpolate("xh1_mean") / x),
            standard_deviation=(
                0.0 if x == 1.0
                else max(0.0, interpolate("xh1_std") / x)
            ),
        )

    def __call__(self, flavor: int, x: float, scale_gev: float) -> float:
        return self.estimate(flavor, x, scale_gev).mean


class JAMDiFFTransversityReplicas:
    """Official LHAPDF central plus 968 physical wLQCD replicas."""

    set_name = "JAMDiFF23-transversity_lo"
    flavors = (2, 1, -2, -1)

    def __init__(
        self,
        data_root: str | Path = "data/vendor/JAMDiFF_library/lhapdf",
    ) -> None:
        try:
            import lhapdf
        except ImportError as exc:
            raise RuntimeError(
                "LHAPDF Python bindings are required for JAMDiFF replicas"
            ) from exc
        root = str(Path(data_root).resolve())
        paths = list(lhapdf.paths())
        if root not in paths:
            lhapdf.setPaths([root, *paths])
        pdf_set = lhapdf.getPDFSet(self.set_name)
        if int(pdf_set.size) != 969 or str(pdf_set.errorType) != "replicas":
            raise ValueError("unexpected JAMDiFF LHAPDF ensemble metadata")
        self._members: list[Any] = pdf_set.mkPDFs()
        self.central_member = 0
        self.replica_members = tuple(range(1, 969))
        self.x_min = float(self._members[0].xMin)
        self.x_max = float(self._members[0].xMax)
        self.scale_min_gev = float(self._members[0].q2Min) ** 0.5
        self.scale_max_gev = float(self._members[0].q2Max) ** 0.5

    def _validate(self, flavor: int, x: float, scale_gev: float) -> None:
        if flavor not in self.flavors:
            raise ValueError("JAMDiFF grid contains u,d,ubar,dbar only")
        if not self.x_min <= x <= self.x_max:
            raise ValueError(f"x={x} outside [{self.x_min}, {self.x_max}]")
        if not self.scale_min_gev <= scale_gev <= self.scale_max_gev:
            raise ValueError(
                f"Q={scale_gev} outside "
                f"[{self.scale_min_gev}, {self.scale_max_gev}]"
            )

    def central(self, flavor: int, x: float, scale_gev: float) -> float:
        self._validate(flavor, x, scale_gev)
        return float(self._members[0].xfxQ(flavor, x, scale_gev) / x)

    def replicas(self, flavor: int, x: float, scale_gev: float) -> np.ndarray:
        """Return number-density h1 for members 1--968 in stable order."""

        self._validate(flavor, x, scale_gev)
        return np.fromiter(
            (
                self._members[index].xfxQ(flavor, x, scale_gev) / x
                for index in self.replica_members
            ),
            dtype=float,
            count=len(self.replica_members),
        )

    def estimate(self, flavor: int, x: float, scale_gev: float) -> TransversityEstimate:
        values = self.replicas(flavor, x, scale_gev)
        return TransversityEstimate(
            mean=self.central(flavor, x, scale_gev),
            standard_deviation=float(np.std(values, ddof=0)),
        )


@dataclass(frozen=True)
class JAMDiFFReplicaGrid:
    """Member-preserving fixed-Q interpolation cache for nuclear convolution."""

    x_axis: np.ndarray
    flavors: tuple[int, ...]
    central_values: np.ndarray  # (flavor, x)
    replica_values: np.ndarray  # (replica, flavor, x)
    scale_gev: float

    @classmethod
    def generate(
        cls,
        source: JAMDiFFTransversityReplicas,
        *,
        scale_gev: float,
        x_axis: np.ndarray,
        flavors: tuple[int, ...] = (2, 1, -2, -1),
    ) -> "JAMDiFFReplicaGrid":
        x_values = np.asarray(x_axis, dtype=float)
        if (
            x_values.ndim != 1 or len(x_values) < 2
            or np.any(np.diff(x_values) <= 0.0)
            or x_values[0] < source.x_min or x_values[-1] > source.x_max
        ):
            raise ValueError("invalid JAMDiFF replica x axis")
        central = np.empty((len(flavors), len(x_values)))
        replicas = np.empty((968, len(flavors), len(x_values)))
        for flavor_index, flavor in enumerate(flavors):
            for x_index, x in enumerate(x_values):
                central[flavor_index, x_index] = source.central(
                    flavor, float(x), scale_gev
                )
                replicas[:, flavor_index, x_index] = source.replicas(
                    flavor, float(x), scale_gev
                )
        return cls(x_values, flavors, central, replicas, float(scale_gev))

    def save(self, path: str | Path) -> None:
        destination = Path(path)
        destination.parent.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(
            destination,
            x_axis=self.x_axis,
            flavors=np.asarray(self.flavors, dtype=np.int64),
            central_values=self.central_values,
            replica_values=self.replica_values,
            scale_gev=np.asarray(self.scale_gev),
            replica_member_ids=np.arange(1, 969, dtype=np.int64),
        )

    @classmethod
    def load(cls, path: str | Path) -> "JAMDiFFReplicaGrid":
        with np.load(Path(path), allow_pickle=False) as archive:
            member_ids = archive["replica_member_ids"]
            if not np.array_equal(member_ids, np.arange(1, 969)):
                raise ValueError("JAMDiFF replica member identity is not contiguous")
            return cls(
                archive["x_axis"],
                tuple(int(item) for item in archive["flavors"]),
                archive["central_values"],
                archive["replica_values"],
                float(archive["scale_gev"]),
            )

    def interpolate_all(self, flavor: int, x: np.ndarray) -> np.ndarray:
        """Return physical members as ``(968, point)`` with zero at x=1."""

        if flavor not in self.flavors:
            raise KeyError(flavor)
        query = np.asarray(x, dtype=float).ravel()
        result = np.zeros((968, len(query)))
        valid = (query >= self.x_axis[0]) & (query <= self.x_axis[-1])
        if np.any(valid):
            values = query[valid]
            indices = np.clip(
                np.searchsorted(self.x_axis, values) - 1,
                0, len(self.x_axis) - 2,
            )
            fraction = (
                (values - self.x_axis[indices])
                / (self.x_axis[indices + 1] - self.x_axis[indices])
            )
            field = self.replica_values[:, self.flavors.index(flavor)]
            result[:, valid] = (
                (1.0 - fraction) * field[:, indices]
                + fraction * field[:, indices + 1]
            )
        return result

    def interpolate_central(self, flavor: int, x: np.ndarray) -> np.ndarray:
        if flavor not in self.flavors:
            raise KeyError(flavor)
        query = np.asarray(x, dtype=float)
        return np.interp(
            query,
            self.x_axis,
            self.central_values[self.flavors.index(flavor)],
            left=0.0,
            right=0.0,
        )
