#!/usr/bin/env python3
"""Validate parent-derived quark tables and an optional azimuthal partner."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.quark_correlator import compose_spin1_quark_correlator

M_D_GEV = 1.87561294257

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--azimuth-partner", type=Path)
    parser.add_argument("--azimuth-relative-tolerance", type=float, default=0.02)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    args = parse_args()
    data = pd.read_csv(args.input)
    numeric = data.select_dtypes(include=[np.number]).to_numpy()
    require(np.isfinite(numeric).all(), "non-finite table value")
    require(bool((data["parent_derived"] == 1).all()), "untraced output row")
    expected_flavors = {"u", "d", "ubar", "dbar"}
    require(set(data.flavor_label) == expected_flavors, "incomplete flavor set")
    expected_mechanisms = {
        "proton_impulse", "neutron_impulse", "impulse_total",
        "wave_SS", "wave_SD", "wave_DS", "wave_DD",
        "coherent_shadowing", "antishadowing", "off_shell",
        "meson_exchange", "non_nucleonic", "model_total",
    }
    require(set(data.mechanism) == expected_mechanisms, "incomplete mechanisms")
    groups = data.groupby(["flavor_label", "gauge_link", "mechanism"])
    require(int(groups.tmd.nunique().min()) == 18, "incomplete TMD basis")
    require(int(groups.k_GeV.nunique().min()) >= 3, "insufficient k grid")

    keys = ["flavor_label", "gauge_link", "k_GeV", "tmd"]
    pivot = data.pivot_table(
        index=keys, columns="mechanism", values="F_GeV-2", aggfunc="first"
    )
    pn_residual = float(
        np.max(
            np.abs(
                pivot["impulse_total"]
                - pivot["proton_impulse"]
                - pivot["neutron_impulse"]
            )
        )
    )
    mechanism_residual = float(
        np.max(
            np.abs(
                pivot["model_total"]
                - pivot["impulse_total"]
                - pivot["coherent_shadowing"]
                - pivot["antishadowing"]
                - pivot["off_shell"]
                - pivot["meson_exchange"]
                - pivot["non_nucleonic"]
            )
        )
    )
    wave_component_residual = float(
        np.max(np.abs(
            pivot["impulse_total"] - pivot["wave_SS"] - pivot["wave_SD"]
            - pivot["wave_DS"] - pivot["wave_DD"]
        ))
    )
    require(pn_residual < 1.0e-11, "proton+neutron reconstruction failed")
    # Rank-three/four coefficient extraction near small k amplifies otherwise
    # machine-precision matrix closure.  The retained correlator tables close
    # exactly under addition; 2e-10 GeV^-2 is the audited projection-level
    # absolute tolerance for the complete 18-function basis.
    require(mechanism_residual < 2.0e-10, "mechanism reconstruction failed")
    require(
        wave_component_residual < 2.0e-10,
        "SS+SD+DS+DD reconstruction failed",
    )

    origin = data[np.isclose(data.k_GeV, 0.0)]
    require(
        bool(np.allclose(origin.loc[origin["rank"] > 0, "F_GeV-2"], 0.0, atol=1e-13)),
        "positive-rank origin limit failed",
    )
    todd_max = float(np.max(np.abs(data.loc[data.t_odd == 1, "F_GeV-2"])))
    fitted_sivers_max = float(
        np.max(np.abs(data.loc[data.tmd == "f1Tperp", "F_GeV-2"]))
    )
    require(
        fitted_sivers_max > 1.0e-8,
        "fitted BPV20 Sivers boundary was not propagated",
    )

    positivity_mechanisms = (
        "proton_impulse", "neutron_impulse", "impulse_total", "model_total"
    )
    minimum_eigenvalues = {name: np.inf for name in positivity_mechanisms}
    worst_positivity = {}
    positivity_groups = data.loc[
        data.mechanism.isin(positivity_mechanisms)
    ].groupby(["flavor_label", "gauge_link", "mechanism", "k_GeV"])
    for labels, group in positivity_groups:
        flavor, link, mechanism, k = labels
        angle = float(group.azimuth_rad.iloc[0])
        values = dict(zip(group.tmd, group["F_GeV-2"]))
        correlator = compose_spin1_quark_correlator(
            (float(k) * np.cos(angle), float(k) * np.sin(angle)),
            M_D_GEV,
            values,
        )
        eigenvalue = correlator.minimum_positivity_eigenvalue()
        if eigenvalue < minimum_eigenvalues[mechanism]:
            minimum_eigenvalues[mechanism] = eigenvalue
            worst_positivity[mechanism] = {
                "flavor": flavor, "gauge_link": link, "k_GeV": float(k)
            }
    # The physical deuteron impulse and corrected totals must be positive.
    # Individual p/n bookkeeping rows are also audited, but BPV20 explicitly
    # reports violations of the parton-model Sivers positivity inequality;
    # do not silently clip its fit or hide that input-level tension.
    require(
        min(
            minimum_eigenvalues["impulse_total"],
            minimum_eigenvalues["model_total"],
        ) >= -1.0e-10,
        f"spin-1 joint-density positivity failed: {minimum_eigenvalues}",
    )

    future = data[data.gauge_link == "[+,+]"].set_index(
        ["flavor_label", "mechanism", "k_GeV", "tmd"]
    )
    past = data[data.gauge_link == "[-,-]"].set_index(
        ["flavor_label", "mechanism", "k_GeV", "tmd"]
    )
    future_values = future["F_GeV-2"]
    past_values = past["F_GeV-2"]
    todd_mask = np.asarray([
        bool(data.loc[data.tmd.eq(index[-1]), "t_odd"].iloc[0])
        for index in future.index
    ])
    require(
        np.allclose(
            future_values.to_numpy()[~todd_mask],
            past_values.to_numpy()[~todd_mask],
            atol=1e-11,
            rtol=1e-11,
        ),
        "T-even process invariance failed",
    )
    require(
        np.allclose(
            future_values.to_numpy()[todd_mask],
            -past_values.to_numpy()[todd_mask],
            atol=1e-11,
            rtol=1e-11,
        ),
        "T-odd future/past sign reversal failed",
    )

    azimuth_relative = None
    azimuth_absolute = None
    if args.azimuth_partner is not None:
        partner = pd.read_csv(args.azimuth_partner)
        merge_keys = ["flavor_label", "mechanism", "gauge_link", "k_GeV", "tmd"]
        joined = data.merge(partner, on=merge_keys, suffixes=("_a", "_b"))
        left = joined["F_GeV-2_a"].to_numpy()
        right = joined["F_GeV-2_b"].to_numpy()
        difference = np.abs(left - right)
        size = np.maximum(np.abs(left), np.abs(right))
        resolved = size > 1.0e-8
        azimuth_relative = float(
            np.max(difference[resolved] / size[resolved])
        )
        azimuth_absolute = float(np.max(difference))
        require(
            azimuth_relative <= args.azimuth_relative_tolerance,
            f"azimuth covariance failed ({azimuth_relative:g})",
        )

    report = {
        "status": "pass",
        "input": str(args.input),
        "rows": len(data),
        "flavors": sorted(expected_flavors),
        "basis_per_flavor": 18,
        "k_points": int(data.k_GeV.nunique()),
        "proton_neutron_reconstruction_max_abs": pn_residual,
        "mechanism_reconstruction_max_abs": mechanism_residual,
        "wave_component_reconstruction_max_abs": wave_component_residual,
        "t_odd_max_abs": todd_max,
        "fitted_sivers_max_abs": fitted_sivers_max,
        "spin1_joint_density_minimum_eigenvalues": {
            key: float(value) for key, value in minimum_eigenvalues.items()
        },
        "spin1_joint_density_worst_points": worst_positivity,
        "constituent_input_positivity_tension": bool(
            minimum_eigenvalues["proton_impulse"] < -1.0e-10
            or minimum_eigenvalues["neutron_impulse"] < -1.0e-10
        ),
        "maximum_absolute_physical_ratio": float(
            np.max(np.abs(data.physical_ratio_to_total_f1))
        ),
        "azimuth_covariance_max_relative_resolved": azimuth_relative,
        "azimuth_covariance_max_absolute": azimuth_absolute,
        "azimuth_relative_tolerance": args.azimuth_relative_tolerance,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(f"Validation passed; wrote {args.output}")


if __name__ == "__main__":
    main()
