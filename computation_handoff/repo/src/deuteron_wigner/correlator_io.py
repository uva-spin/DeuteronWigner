"""Portable long-table serialization for unprojected spin-1 correlators."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field

import numpy as np
import pandas as pd
from scipy.interpolate import PchipInterpolator

from .quark_correlator import Spin1QuarkCorrelator


def quark_correlator_rows(
    correlator: Spin1QuarkCorrelator,
    labels: Mapping[str, object],
) -> list[dict[str, object]]:
    """Serialize all 36 complex quark-correlator matrix entries."""

    rows: list[dict[str, object]] = []
    projections = (
        ("vector", correlator.vector[None, ...]),
        ("axial", correlator.axial[None, ...]),
        ("transverse", correlator.transverse),
    )
    for projection, values in projections:
        for operator_index in range(values.shape[0]):
            for target_out in range(3):
                for target_in in range(3):
                    value = values[operator_index, target_out, target_in]
                    rows.append({
                        **labels,
                        "projection": projection,
                        "operator_index": (
                            operator_index if projection == "transverse" else -1
                        ),
                        "target_out": target_out,
                        "target_in": target_in,
                        "gluon_out": -1,
                        "gluon_in": -1,
                        "real": float(np.real(value)),
                        "imag": float(np.imag(value)),
                    })
    return rows


def gluon_correlator_rows(
    correlator: np.ndarray,
    labels: Mapping[str, object],
) -> list[dict[str, object]]:
    """Serialize all 36 complex target/gluon matrix entries."""

    values = np.asarray(correlator, dtype=np.complex128)
    if values.shape != (3, 3, 2, 2):
        raise ValueError("gluon correlator must have shape (3,3,2,2)")
    rows: list[dict[str, object]] = []
    for target_out in range(3):
        for target_in in range(3):
            for gluon_out in range(2):
                for gluon_in in range(2):
                    value = values[target_out, target_in, gluon_out, gluon_in]
                    rows.append({
                        **labels,
                        "projection": "gluon_tensor",
                        "operator_index": -1,
                        "target_out": target_out,
                        "target_in": target_in,
                        "gluon_out": gluon_out,
                        "gluon_in": gluon_in,
                        "real": float(np.real(value)),
                        "imag": float(np.imag(value)),
                    })
    return rows


def deserialize_quark_correlator(rows: pd.DataFrame) -> Spin1QuarkCorrelator:
    """Reconstruct one quark correlator from a 36-row serialized group."""

    vector = np.zeros((3, 3), dtype=np.complex128)
    axial = np.zeros((3, 3), dtype=np.complex128)
    transverse = np.zeros((2, 3, 3), dtype=np.complex128)
    seen: set[tuple[str, int, int, int]] = set()
    for row in rows.itertuples(index=False):
        key = (
            str(row.projection), int(row.operator_index),
            int(row.target_out), int(row.target_in),
        )
        if key in seen:
            raise ValueError(f"duplicate correlator entry {key}")
        seen.add(key)
        value = complex(float(row.real), float(row.imag))
        if row.projection == "vector":
            vector[row.target_out, row.target_in] = value
        elif row.projection == "axial":
            axial[row.target_out, row.target_in] = value
        elif row.projection == "transverse":
            transverse[row.operator_index, row.target_out, row.target_in] = value
        else:
            raise ValueError(f"unknown quark projection {row.projection}")
    if len(seen) != 36:
        raise ValueError(f"quark correlator requires 36 entries, found {len(seen)}")
    return Spin1QuarkCorrelator(vector, axial, transverse)


@dataclass(frozen=True)
class TabulatedQuarkCorrelatorProvider:
    """Shape-preserving arbitrary-x provider for serialized LF parents.

    Interpolation is PCHIP in ``ln(x)``.  PDF-like parent functions change
    on multiplicative x scales, and direct linear-x interpolation produces a
    demonstrably unstable small-x recoil convolution.
    """

    x_nodes: np.ndarray
    values: np.ndarray
    scale_gev: float
    parton_sector: str
    _real_interpolator: PchipInterpolator = field(init=False, repr=False)
    _imag_interpolator: PchipInterpolator = field(init=False, repr=False)

    def __post_init__(self) -> None:
        x = np.asarray(self.x_nodes, dtype=float)
        values = np.asarray(self.values, dtype=np.complex128)
        if x.ndim != 1 or x.size < 2 or np.any(np.diff(x) <= 0.0):
            raise ValueError("correlator x nodes must be strictly increasing")
        if values.shape != (x.size, 4, 3, 3):
            raise ValueError("tabulated correlators require shape (nx,4,3,3)")
        if not np.all(np.isfinite(values)):
            raise ValueError("tabulated correlators must be finite")
        if self.scale_gev <= 0.0:
            raise ValueError("tabulated correlator scale must be positive")
        if self.parton_sector not in ("valence", "sea"):
            raise ValueError("parton sector must be valence or sea")
        object.__setattr__(self, "x_nodes", x)
        object.__setattr__(self, "values", values)
        object.__setattr__(
            self, "_real_interpolator",
            PchipInterpolator(np.log(x), values.real, axis=0, extrapolate=False),
        )
        object.__setattr__(
            self, "_imag_interpolator",
            PchipInterpolator(np.log(x), values.imag, axis=0, extrapolate=False),
        )

    @classmethod
    def from_frame(
        cls,
        frame: pd.DataFrame,
        *,
        scale_gev: float,
        parton_sector: str,
    ) -> "TabulatedQuarkCorrelatorProvider":
        required = {
            "x_N", "Q_GeV", "projection", "operator_index",
            "target_out", "target_in", "real", "imag",
        }
        missing = required.difference(frame.columns)
        if missing:
            raise ValueError(f"correlator table misses columns {sorted(missing)}")
        if not np.allclose(frame["Q_GeV"].to_numpy(float), scale_gev):
            raise ValueError("correlator table scale does not match provider scale")
        x_nodes = np.sort(frame["x_N"].unique().astype(float))
        correlators = [
            deserialize_quark_correlator(frame[frame["x_N"] == x])
            for x in x_nodes
        ]
        values = np.stack([
            np.concatenate((
                c.vector[None, ...], c.axial[None, ...], c.transverse
            ), axis=0)
            for c in correlators
        ])
        return cls(x_nodes, values, scale_gev, parton_sector)

    def __call__(
        self, x: float, scale_gev: float, parton_sector: str
    ) -> Spin1QuarkCorrelator:
        if not np.isclose(scale_gev, self.scale_gev):
            raise ValueError("requested scale does not match tabulated parent")
        if parton_sector != self.parton_sector:
            raise ValueError("requested parton sector does not match tabulated parent")
        if x < self.x_nodes[0] or x > self.x_nodes[-1]:
            values = np.zeros((4, 3, 3), dtype=np.complex128)
        else:
            real = self._real_interpolator(np.log(x))
            imag = self._imag_interpolator(np.log(x))
            values = real + 1j * imag
            values = 0.5 * (values + values.conj().swapaxes(-1, -2))
        return Spin1QuarkCorrelator(values[0], values[1], values[2:])


def deserialize_gluon_correlator(rows: pd.DataFrame) -> np.ndarray:
    """Reconstruct one gluon correlator from a 36-row serialized group."""

    values = np.zeros((3, 3, 2, 2), dtype=np.complex128)
    seen: set[tuple[int, int, int, int]] = set()
    for row in rows.itertuples(index=False):
        key = (
            int(row.target_out), int(row.target_in),
            int(row.gluon_out), int(row.gluon_in),
        )
        if key in seen:
            raise ValueError(f"duplicate correlator entry {key}")
        seen.add(key)
        values[key] = complex(float(row.real), float(row.imag))
    if len(seen) != 36:
        raise ValueError(f"gluon correlator requires 36 entries, found {len(seen)}")
    return values


def write_correlator_table(
    rows: Iterable[Mapping[str, object]],
    path,
) -> None:
    """Write a deterministic, human-inspectable correlator CSV."""

    frame = pd.DataFrame(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False)
