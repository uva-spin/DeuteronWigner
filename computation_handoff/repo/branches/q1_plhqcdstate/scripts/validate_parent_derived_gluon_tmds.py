#!/usr/bin/env python3
"""Validate traced parent-derived gluon tables and optional convergence pair."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.gluon_correlator import compose_spin1_gluon_correlator

M_D_GEV = 1.87561294257

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("table", type=Path)
    parser.add_argument("--reference", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    frame = pd.read_csv(args.table)
    required_tmds = {
        "f1", "h1perp", "g1", "h1Lperp",
        "f1Tperp", "g1T", "h1", "h1Tperp",
        "f1LL", "h1LLperp",
        "f1LT", "g1LT", "h1LT", "h1LTperp",
        "f1TT_minus_h1TTperp", "g1TT", "h1TT", "h1TTperpperp",
    }
    checks: dict[str, object] = {
        "finite": bool(np.isfinite(frame["F_GeV-2"]).all()),
        "complete_identifiable_basis": set(frame.tmd) == required_tmds,
        "mechanisms": sorted(frame.mechanism.unique()),
        "rows": len(frame),
    }
    pivot = frame.pivot_table(
        index=["k_GeV", "tmd"], columns="mechanism", values="F_GeV-2"
    )
    checks["proton_plus_neutron_max_abs"] = float(
        (pivot.proton_impulse + pivot.neutron_impulse - pivot.impulse_total)
        .abs().max()
    )
    checks["wave_component_reconstruction_max_abs"] = float(
        (
            pivot.wave_SS + pivot.wave_SD + pivot.wave_DS + pivot.wave_DD
            - pivot.impulse_total
        ).abs().max()
    )
    checks["t_odd_raw_max_abs"] = float(
        frame.loc[frame.t_odd.eq(1), "F_GeV-2"].abs().max()
    )
    checks["physical_ratio_max_abs"] = float(
        frame.physical_ratio_to_total_f1.abs().max()
    )
    checks["tt_combination_only"] = bool(
        "f1TT_minus_h1TTperp" in set(frame.tmd)
        and "f1TT" not in set(frame.tmd)
        and "h1TTperp" not in set(frame.tmd)
    )
    positivity_mechanisms = (
        "proton_impulse", "neutron_impulse", "impulse_total"
    )
    positivity = {name: np.inf for name in positivity_mechanisms}
    positivity_worst = {}
    for labels, group in frame.loc[
        frame.mechanism.isin(positivity_mechanisms)
    ].groupby(["mechanism", "k_GeV"]):
        mechanism, k = labels
        angle = float(group.azimuth_rad.iloc[0])
        correlator = compose_spin1_gluon_correlator(
            (float(k) * np.cos(angle), float(k) * np.sin(angle)),
            M_D_GEV,
            dict(zip(group.tmd, group["F_GeV-2"])),
        )
        eigenvalue = correlator.minimum_positivity_eigenvalue()
        if eigenvalue < positivity[mechanism]:
            positivity[mechanism] = eigenvalue
            positivity_worst[mechanism] = {"k_GeV": float(k)}
    checks["spin1_joint_density_minimum_eigenvalues"] = {
        key: float(value) for key, value in positivity.items()
    }
    checks["spin1_joint_density_worst_points"] = positivity_worst
    if args.reference:
        reference = pd.read_csv(args.reference)
        keys = ["mechanism", "tmd", "k_GeV"]
        joined = frame.merge(
            reference, on=keys, suffixes=("_candidate", "_reference"),
            validate="one_to_one",
        )
        candidate = joined["F_GeV-2_candidate"].to_numpy()
        expected = joined["F_GeV-2_reference"].to_numpy()
        checks["convergence_F_relative_L2"] = float(
            np.linalg.norm(candidate - expected)
            / max(np.linalg.norm(expected), 1.0e-30)
        )
        checks["convergence_physical_ratio_max_abs"] = float(
            np.max(np.abs(
                joined.physical_ratio_to_total_f1_candidate
                - joined.physical_ratio_to_total_f1_reference
            ))
        )
    checks["passed"] = bool(
        checks["finite"]
        and checks["complete_identifiable_basis"]
        and checks["proton_plus_neutron_max_abs"] < 1.0e-12
        # Rank-two coefficient extraction amplifies roundoff at the lowest
        # nonzero k point; this absolute tolerance remains below 4e-13 of
        # the largest table coefficient and is paired with physical ratios.
        and checks["wave_component_reconstruction_max_abs"] < 1.0e-11
        and checks["t_odd_raw_max_abs"] < 1.0e-10
        and checks["tt_combination_only"]
        and min(positivity.values()) >= -1.0e-10
    )
    output = args.output or args.table.with_suffix(".validation.json")
    output.write_text(json.dumps(checks, indent=2) + "\n")
    print(json.dumps(checks, indent=2))
    if not checks["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
