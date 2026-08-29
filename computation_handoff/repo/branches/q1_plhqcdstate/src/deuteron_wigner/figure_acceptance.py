"""Fail-closed acceptance checks for parent-derived TMD figure products."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


QUARK_FLAVORS = ("u", "d", "ubar", "dbar")
SPIN1_TMD_COUNT = 18


@dataclass(frozen=True)
class FigureTableAudit:
    species: str
    group_count: int
    expected_group_count: int
    band_ordered: bool
    central_contained: bool
    finite: bool
    dense_common_grid: bool

    @property
    def passed(self) -> bool:
        return (
            self.group_count == self.expected_group_count
            and self.band_ordered
            and self.central_contained
            and self.finite
            and self.dense_common_grid
        )


def audit_ensemble_table(frame: pd.DataFrame, species: str) -> FigureTableAudit:
    """Check only properties supported by the serialized figure source table."""
    required = {
        "flavor_label", "tmd", "target_channel", "k_GeV",
        "F_central_GeV-2", "F_wave_low_GeV-2", "F_wave_high_GeV-2",
        "x_N", "Q_GeV", "interpolation",
    }
    missing = required - set(frame.columns)
    if missing:
        raise ValueError(f"figure table is missing columns: {sorted(missing)}")
    flavors = QUARK_FLAVORS if species == "quark" else ("g",)
    if species == "gluon":
        if "factorization_valid" not in frame:
            raise ValueError("gluon figure table requires factorization_valid")
        expected_validity = (
            frame["k_GeV"].le(1.0)
            & frame["k_GeV"].div(frame["Q_GeV"]).le(0.25)
        )
        if not frame["factorization_valid"].astype(bool).equals(expected_validity):
            raise ValueError("gluon factorization-validity flags are inconsistent")
    expected = len(flavors) * SPIN1_TMD_COUNT
    groups = frame.groupby(["flavor_label", "tmd", "target_channel"], sort=False)
    low = frame["F_wave_low_GeV-2"].to_numpy()
    central = frame["F_central_GeV-2"].to_numpy()
    high = frame["F_wave_high_GeV-2"].to_numpy()
    numeric = frame[[
        "k_GeV", "F_central_GeV-2", "F_wave_low_GeV-2",
        "F_wave_high_GeV-2", "x_N", "Q_GeV",
    ]].to_numpy()
    grid_sizes = groups["k_GeV"].nunique().to_numpy()
    return FigureTableAudit(
        species=species,
        group_count=groups.ngroups,
        expected_group_count=expected,
        band_ordered=bool(np.all(low <= high)),
        central_contained=bool(np.all(low <= central) and np.all(central <= high)),
        finite=bool(np.isfinite(numeric).all()),
        dense_common_grid=bool(
            len(set(grid_sizes.tolist())) == 1
            and grid_sizes[0] >= 200
            and frame["interpolation"].eq("PCHIP through calculated knots").all()
        ),
    )


def audit_flavor_traceability(source: pd.DataFrame) -> dict[str, object]:
    """Prove flavor identity is retained before the controlled deuteron sum."""
    selected = source.loc[
        source["mechanism"].isin(("proton_impulse", "neutron_impulse"))
        & source["tmd"].eq("f1")
        & source["gauge_link"].eq("[+,+]")
    ]
    differences: dict[str, float] = {}
    for mechanism in ("proton_impulse", "neutron_impulse"):
        pivot = selected.loc[selected.mechanism.eq(mechanism)].pivot(
            index="k_GeV", columns="flavor_label", values="F_GeV-2"
        )
        differences[f"{mechanism}:u-d"] = float(
            np.max(np.abs(pivot["u"] - pivot["d"]))
        )
        differences[f"{mechanism}:ubar-dbar"] = float(
            np.max(np.abs(pivot["ubar"] - pivot["dbar"]))
        )
    return {
        "source_flavors": sorted(selected["flavor_label"].unique().tolist()),
        "mechanisms": sorted(selected["mechanism"].unique().tolist()),
        "max_absolute_flavor_differences_GeV-2": differences,
        "flavor_resolved_before_assembly": all(value > 0.0 for value in differences.values()),
        "inclusive_deuteron_equality_interpretation": (
            "u_D=d_D and ubar_D=dbar_D are controlled consequences of the "
            "configured exact charge-symmetric I=0 one-body limit; they are "
            "not identities of the retained proton and neutron sources"
        ),
    }
