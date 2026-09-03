#!/usr/bin/env python3
"""Build smooth BPV20 fit bands with explicit proton/neutron decomposition."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import pandas as pd
from scipy.interpolate import PchipInterpolator

WAVES = ("av18", "cd-bonn", "nvia", "nvib", "nviia", "nviib")
FLAVORS = ("u", "d", "ubar", "dbar")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--directory", type=Path, default=Path("outputs/parent_tmds/uncertainty")
    )
    parser.add_argument(
        "--output-csv", type=Path,
        default=Path("outputs/parent_tmds/ensemble/bpv20_sivers_bands.csv"),
    )
    parser.add_argument(
        "--output-pdf", type=Path,
        default=Path("outputs/parent_tmds/ensemble/bpv20_sivers_atlas.pdf"),
    )
    parser.add_argument("--dense-points", type=int, default=301)
    return parser.parse_args()


def interpolate(group: pd.DataFrame, column: str, axis: np.ndarray) -> np.ndarray:
    ordered = group.sort_values("k_GeV")
    return PchipInterpolator(
        ordered.k_GeV, ordered[column], extrapolate=False
    )(axis)


def main() -> None:
    args = parse_args()
    frames = []
    for wave in WAVES:
        frame = pd.read_csv(args.directory / f"bpv20_sivers_{wave}_fine.csv")
        frame["wave_function"] = wave
        frames.append(frame)
    data = pd.concat(frames, ignore_index=True)
    axis = np.linspace(0.0, 1.5, args.dense_points)
    rows: list[dict[str, object]] = []
    group_columns = [
        "flavor", "flavor_label", "gauge_link", "x_N", "x_D", "Q_GeV",
        "azimuth_rad", "mechanism",
    ]
    for labels, group in data.groupby(group_columns, sort=False):
        label_map = dict(zip(group_columns, labels))
        av18 = group.loc[group.wave_function.eq("av18")]
        wave_centrals = np.vstack([
            interpolate(group.loc[group.wave_function.eq(wave)], "F_central_GeV-2", axis)
            for wave in WAVES
        ])
        curves = {
            column: interpolate(av18, column, axis)
            for column in (
                "F_central_GeV-2", "F_replica_mean_GeV-2",
                "F_replica_median_GeV-2", "F_q16_GeV-2", "F_q84_GeV-2",
                "F_replica_std_GeV-2",
            )
        }
        for index, k in enumerate(axis):
            rows.append({
                **label_map,
                "k_GeV": k,
                **{column: values[index] for column, values in curves.items()},
                "F_wave_low_GeV-2": wave_centrals[:, index].min(),
                "F_wave_high_GeV-2": wave_centrals[:, index].max(),
                "central_wave_function": "av18",
                "replica_count": 500,
                "calculated_knot_count": 9,
                "interpolation": "shape-preserving PCHIP through calculated knots",
            })
    dense = pd.DataFrame(rows)
    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    dense.to_csv(args.output_csv, index=False)

    future = dense.loc[dense.gauge_link.eq("[+,+]")]
    colors = {"u": "#1f77b4", "d": "#d62728", "ubar": "#2ca02c", "dbar": "#9467bd"}
    with PdfPages(args.output_pdf) as pdf:
        for flavor in FLAVORS:
            fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.5), constrained_layout=True)
            total = future.loc[
                future.flavor_label.eq(flavor) & future.mechanism.eq("model_total")
            ].sort_values("k_GeV")
            ax = axes[0]
            ax.fill_between(
                total.k_GeV, total["F_q16_GeV-2"], total["F_q84_GeV-2"],
                color=colors[flavor], alpha=0.25, linewidth=0,
                label="BPV20 central 68% replica interval",
            )
            ax.fill_between(
                total.k_GeV, total["F_wave_low_GeV-2"],
                total["F_wave_high_GeV-2"], color="0.25", alpha=0.18,
                linewidth=0, label="six-wave central envelope",
            )
            ax.plot(
                total.k_GeV, total["F_central_GeV-2"],
                color=colors[flavor], linewidth=2.2, label="BPV20 member 0 + AV18",
            )
            ax.plot(
                total.k_GeV, total["F_replica_median_GeV-2"],
                color=colors[flavor], linewidth=1.2, linestyle="--",
                label="replica median",
            )
            ax.set_title(f"Deuteron {flavor}: model total")

            ax = axes[1]
            for mechanism, style, label in (
                ("proton_impulse", "-", "active proton"),
                ("neutron_impulse", "--", "active neutron"),
                ("off_shell", ":", "CJ26 node-wise off-shell"),
            ):
                curve = future.loc[
                    future.flavor_label.eq(flavor) & future.mechanism.eq(mechanism)
                ].sort_values("k_GeV")
                ax.plot(
                    curve.k_GeV, curve["F_central_GeV-2"],
                    linestyle=style, linewidth=2.0, label=label,
                )
            ax.set_title(f"{flavor}: resolved nuclear contributions")
            for ax in axes:
                ax.axhline(0.0, color="0.35", linewidth=0.7)
                ax.set_xlabel(r"$k_T$ [GeV]")
                ax.set_ylabel(r"$f_{1T}^{\perp}(x_N=0.1,k_T;Q=5)$ [GeV$^{-2}$]")
                ax.grid(alpha=0.2)
                ax.legend(frameon=False, fontsize=8)
            fig.suptitle(
                "BPV20 Sivers fit propagated through the spin-1 light-front convolution"
            )
            pdf.savefig(fig)
            plt.close(fig)

    metadata = {
        "status": "production smooth central curves and separated uncertainty bands",
        "fit_band": "pointwise 16th–84th percentiles of official BPV20 members 1–500",
        "central": "separate BPV20 member 0 propagated with AV18",
        "wave_band": "pointwise envelope of six wave-function central members",
        "combination_policy": "bands shown separately; no unsupported joint probability",
        "process": "future/SIDIS reference; past/DY rows are exact sign transforms",
        "flavor_note": (
            "proton and neutron contributions are separately flavor resolved. "
            "Exact charge symmetry makes the p+n deuteron u/d totals equal; "
            "this is an isoscalar consequence, not a proton-level u=d ansatz. "
            "BPV20 itself fits a common ubar/dbar sea."
        ),
        "interpolation": (
            "PCHIP through nine explicitly convolved k knots; visualization "
            "adds no physics information"
        ),
    }
    args.output_csv.with_suffix(".metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n"
    )
    print(f"Wrote {args.output_csv} and {args.output_pdf}")


if __name__ == "__main__":
    main()
