#!/usr/bin/env python3
"""Build smooth, separately sourced JAMDiFF and wave-function h1 bands."""

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
ROOT = Path("outputs/parent_tmds")


def curve(group: pd.DataFrame, column: str, axis: np.ndarray) -> np.ndarray:
    ordered = group.sort_values("k_GeV")
    return PchipInterpolator(
        ordered.k_GeV, ordered[column], extrapolate=False
    )(axis)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tmd", choices=("h1", "h1Lperp"), default="h1")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    # Prevent user-level ``savefig.bbox=tight`` settings from changing page
    # geometry between flavors with different numerical ranges.
    plt.rcParams["savefig.bbox"] = None
    plt.rcParams["figure.constrained_layout.use"] = False
    plt.rcParams["figure.autolayout"] = False
    frames = []
    prefix = (
        "jamdiff_transversity" if args.tmd == "h1" else "jamdiff_h1Lperp"
    )
    for wave in WAVES:
        frame = pd.read_csv(
            ROOT / "uncertainty" / f"{prefix}_{wave}_fine.csv"
        )
        frame["wave_function"] = wave
        frames.append(frame)
    data = pd.concat(frames, ignore_index=True)
    axis = np.linspace(0.0, 1.5, 301)
    labels = [
        "flavor", "flavor_label", "gauge_link", "x_N", "x_D", "Q_GeV",
        "azimuth_rad", "mechanism",
    ]
    rows = []
    for keys, group in data.groupby(labels, sort=False):
        identity = dict(zip(labels, keys))
        av18 = group.loc[group.wave_function.eq("av18")]
        wave_values = np.vstack([
            curve(
                group.loc[group.wave_function.eq(wave)],
                "F_central_GeV-2", axis,
            )
            for wave in WAVES
        ])
        interpolated = {
            name: curve(av18, name, axis)
            for name in (
                "F_central_GeV-2", "F_recomputed_central_GeV-2",
                "F_replica_mean_GeV-2", "F_replica_median_GeV-2",
                "F_q16_GeV-2", "F_q84_GeV-2", "F_replica_std_GeV-2",
            )
        }
        for index, k in enumerate(axis):
            rows.append({
                **identity,
                "k_GeV": k,
                **{name: values[index] for name, values in interpolated.items()},
                "F_wave_low_GeV-2": wave_values[:, index].min(),
                "F_wave_high_GeV-2": wave_values[:, index].max(),
                "central_wave_function": "av18",
                "replica_count": 968,
                "calculated_knot_count": 9,
                "interpolation": "shape-preserving PCHIP",
            })
    dense = pd.DataFrame(rows)
    output_csv = ROOT / "ensemble" / f"{prefix}_bands.csv"
    output_pdf = ROOT / "ensemble" / f"{prefix}_atlas.pdf"
    dense.to_csv(output_csv, index=False)
    future = dense.loc[dense.gauge_link.eq("[+,+]")]
    colors = {"u": "#1f77b4", "d": "#d62728", "ubar": "#2ca02c", "dbar": "#9467bd"}
    with PdfPages(output_pdf) as pdf:
        for flavor in FLAVORS:
            fig, axes = plt.subplots(1, 2, figsize=(11.2, 4.5), layout=None)
            fig.subplots_adjust(
                left=0.105, right=0.985, bottom=0.14, top=0.90, wspace=0.31
            )
            total = future.loc[
                future.flavor_label.eq(flavor)
                & future.mechanism.eq("model_total")
            ].sort_values("k_GeV")
            axes[0].fill_between(
                total.k_GeV, total["F_q16_GeV-2"], total["F_q84_GeV-2"],
                color=colors[flavor], alpha=0.25, linewidth=0,
                label="JAMDiFF central 68% replica interval",
            )
            axes[0].fill_between(
                total.k_GeV, total["F_wave_low_GeV-2"],
                total["F_wave_high_GeV-2"], color="0.25", alpha=0.18,
                linewidth=0, label="six-wave central envelope",
            )
            axes[0].plot(
                total.k_GeV, total["F_central_GeV-2"],
                color=colors[flavor], linewidth=2.2,
                label="JAMDiFF member 0 + AV18",
            )
            axes[0].plot(
                total.k_GeV, total["F_replica_median_GeV-2"],
                color=colors[flavor], linestyle="--", linewidth=1.2,
                label="replica median",
            )
            axes[0].set_title(f"Deuteron {flavor}: model total")
            for mechanism, style, label in (
                ("proton_impulse", "-", "proton impulse"),
                ("neutron_impulse", "--", "neutron impulse"),
                ("off_shell", ":", "CJ26 off-shell"),
            ):
                selected = future.loc[
                    future.flavor_label.eq(flavor)
                    & future.mechanism.eq(mechanism)
                ].sort_values("k_GeV")
                axes[1].plot(
                    selected.k_GeV, selected["F_central_GeV-2"],
                    linestyle=style, linewidth=2.0, label=label,
                )
            axes[1].set_title(f"{flavor}: resolved nuclear contributions")
            for ax in axes:
                ax.axhline(0.0, color="0.35", linewidth=0.7)
                ax.set_xlabel(r"$k_T$ [GeV]")
                ax.set_ylabel(
                    (
                        r"$h_1(x_N=0.1,k_T;Q=5)$ [GeV$^{-2}$]"
                        if args.tmd == "h1"
                        else r"$h_{1L}^{\perp}(x_N=0.1,k_T;Q=5)$ [GeV$^{-2}$]"
                    )
                )
                ax.grid(alpha=0.2)
                ax.legend(frameon=False, fontsize=8)
            pdf.savefig(fig, bbox_inches=None)
            plt.close(fig)
    metadata = {
        "status": "production smooth central curves and separated uncertainty bands",
        "fit_band": (
            "pointwise 16th-84th percentiles of official LHAPDF members 1-968"
        ),
        "central": "separate JAMDiFF LHAPDF member 0 propagated with AV18",
        "wave_band": "pointwise envelope of six wave-function central members",
        "combination_policy": "bands remain separate; no joint probability assigned",
        "composition": (
            "replica-wise CT18+BDSSV Gaussian TMD Soffer projection and "
            "documented sea endpoint applied before LF convolution"
            + (
                ""
                if args.tmd == "h1"
                else "; WW integral evaluated member by member with h1 identity retained"
            )
        ),
        "flavor_note": (
            "active proton and neutron contributions remain distinct; exact "
            "charge symmetry makes p+n deuteron u/d totals equal"
        ),
        "interpolation": "PCHIP through nine explicitly convolved knots",
    }
    output_csv.with_suffix(".metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n"
    )
    print(f"Wrote {output_csv} and {output_pdf}")


if __name__ == "__main__":
    main()
