"""Small, provenance-tracked experimental data loaders."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np


@dataclass(frozen=True)
class HermesB1Data:
    x: np.ndarray
    q2_gev2: np.ndarray
    azz: np.ndarray
    azz_stat: np.ndarray
    azz_sys: np.ndarray
    b1: np.ndarray
    b1_stat: np.ndarray
    b1_sys: np.ndarray

    @property
    def b1_total_uncertainty(self) -> np.ndarray:
        return np.hypot(self.b1_stat, self.b1_sys)

    @property
    def q_gev(self) -> np.ndarray:
        return np.sqrt(self.q2_gev2)


def load_hermes_b1(path: str | Path) -> HermesB1Data:
    source = Path(path)
    table = np.genfromtxt(source, delimiter=",", names=True, dtype=np.float64)
    required = (
        "x",
        "Q2_GeV2",
        "Azz",
        "Azz_stat",
        "Azz_sys",
        "b1",
        "b1_stat",
        "b1_sys",
    )
    if table.dtype.names != required:
        raise ValueError(f"{source}: unexpected HERMES Table II columns {table.dtype.names}")
    columns = [np.atleast_1d(table[name]) for name in required]
    if any(not np.all(np.isfinite(column)) for column in columns):
        raise ValueError(f"{source}: non-finite HERMES data")
    if not np.all(np.diff(columns[0]) > 0.0):
        raise ValueError(f"{source}: x values must be strictly increasing")
    uncertainty_columns = (columns[3], columns[4], columns[6], columns[7])
    if np.any(columns[1] <= 0.0) or any(
        np.any(column < 0.0) for column in uncertainty_columns
    ):
        raise ValueError(f"{source}: invalid scale or uncertainty")
    return HermesB1Data(
        x=columns[0],
        q2_gev2=columns[1],
        azz=columns[2],
        azz_stat=columns[3],
        azz_sys=columns[4],
        b1=columns[5],
        b1_stat=columns[6],
        b1_sys=columns[7],
    )
