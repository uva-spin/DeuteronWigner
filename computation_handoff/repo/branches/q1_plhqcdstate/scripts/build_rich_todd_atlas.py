#!/usr/bin/env python3
"""Build the production rich-structure T-odd atlas and source table."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import pandas as pd
from scipy.interpolate import PchipInterpolator

WAVES = ("av18", "cd-bonn", "nvia", "nvib", "nviia", "nviib")
ROOT = Path("outputs/parent_tmds")
TABLE = ROOT / "ensemble/rich_todd_parent_ensemble.csv"
PDF = Path("output/pdf/rich_spin1_todd_parent_atlas.pdf")


def smooth_curves(groups, k_axis):
    return {
        label: PchipInterpolator(
            group.sort_values("k_GeV").k_GeV,
            group.sort_values("k_GeV")["F_GeV-2"],
        )(k_axis)
        for label, group in groups
    }


def main() -> None:
    rows = []
    quark_frames = []
    for wave in WAVES:
        frame = pd.read_csv(ROOT / f"quark_{wave}_rich_medium.csv")
        frame["wave_function"] = wave
        quark_frames.append(frame)
    quark = pd.concat(quark_frames, ignore_index=True)
    quark = quark[
        quark.tmd.eq("h1perp")
        & quark.mechanism.eq("model_total")
        & quark.gauge_link.eq("[+,+]")
    ]
    for flavor, group in quark.groupby("flavor_label", sort=False):
        k_axis = np.linspace(group.k_GeV.min(), group.k_GeV.max(), 241)
        curves = smooth_curves(group.groupby("wave_function"), k_axis)
        values = np.vstack([curves[wave] for wave in WAVES])
        for index, k in enumerate(k_axis):
            rows.append({
                "sector": "quark_boer_mulders",
                "species": "q",
                "flavor_label": flavor,
                "tmd": "h1perp",
                "color_structure": "",
                "scenario": "BMP_x_BPV20_central",
                "gauge_link": "[+,+]",
                "k_GeV": k,
                "F_central_GeV-2": curves["av18"][index],
                "F_wave_low_GeV-2": values[:, index].min(),
                "F_wave_high_GeV-2": values[:, index].max(),
                "uncertainty_axis": "six_wave_function_envelope",
                "status": "phenomenological proportionality model",
            })

    gluon_frames = []
    for wave in WAVES:
        frame = pd.read_csv(ROOT / f"gluon_{wave}_todd_scenarios.csv")
        frame["wave_function"] = wave
        gluon_frames.append(frame)
    gluon = pd.concat(gluon_frames, ignore_index=True)
    gluon = gluon[gluon.gauge_link.str.contains("incoming='\\+'", regex=True)]
    for (color, scenario), group in gluon.groupby(
        ["color_structure", "scenario"], sort=False
    ):
        k_axis = np.linspace(group.k_GeV.min(), group.k_GeV.max(), 241)
        curves = smooth_curves(group.groupby("wave_function"), k_axis)
        values = np.vstack([curves[wave] for wave in WAVES])
        for index, k in enumerate(k_axis):
            rows.append({
                "sector": "gluon_sivers",
                "species": "g",
                "flavor_label": "g",
                "tmd": "f1Tperp",
                "color_structure": color,
                "scenario": scenario,
                "gauge_link": "[+,+]",
                "k_GeV": k,
                "F_central_GeV-2": curves["av18"][index],
                "F_wave_low_GeV-2": values[:, index].min(),
                "F_wave_high_GeV-2": values[:, index].max(),
                "uncertainty_axis": (
                    "six_wave_function_envelope; CGI-GPM scenarios separate"
                ),
                "status": "preliminary CGI-GPM phenomenological constraint",
            })
    output = pd.DataFrame(rows)
    TABLE.parent.mkdir(parents=True, exist_ok=True)
    output.to_csv(TABLE, index=False)
    PDF.parent.mkdir(parents=True, exist_ok=True)
    colors = {
        "central_midpoint": "#163A5F",
        "negative_d_endpoint": "#B24C3D",
        "positive_d_endpoint": "#3E8E7E",
    }
    with PdfPages(PDF) as pdf:
        for flavor, group in output[
            output.sector.eq("quark_boer_mulders")
        ].groupby("flavor_label", sort=False):
            fig, ax = plt.subplots(figsize=(7.2, 4.8), constrained_layout=True)
            ax.fill_between(
                group.k_GeV, group["F_wave_low_GeV-2"],
                group["F_wave_high_GeV-2"], color="#4C78A8", alpha=0.25,
                linewidth=0, label="six-wave-function envelope",
            )
            ax.plot(
                group.k_GeV, group["F_central_GeV-2"],
                color="#163A5F", linewidth=2.1, label="AV18 central",
            )
            ax.axhline(0.0, color="0.35", linewidth=0.7)
            ax.set_title(f"Parent-derived {flavor} Boer-Mulders $h_1^\\perp$")
            ax.set_xlabel(r"$k_T$ [GeV]")
            ax.set_ylabel(r"$F(x_N=0.1,k_T;Q=5\,\mathrm{GeV})$ [GeV$^{-2}$]")
            ax.text(
                0.02, 0.03,
                "BMP proportionality model x BPV20; future staple",
                transform=ax.transAxes, fontsize=8.5, color="0.3",
            )
            ax.grid(alpha=0.2)
            ax.legend(frameon=False)
            pdf.savefig(fig)
            plt.close(fig)
        for color, color_group in output[
            output.sector.eq("gluon_sivers")
        ].groupby("color_structure", sort=False):
            fig, ax = plt.subplots(figsize=(7.2, 4.8), constrained_layout=True)
            for scenario, group in color_group.groupby("scenario", sort=False):
                ax.fill_between(
                    group.k_GeV, group["F_wave_low_GeV-2"],
                    group["F_wave_high_GeV-2"],
                    color=colors[scenario], alpha=0.13, linewidth=0,
                )
                ax.plot(
                    group.k_GeV, group["F_central_GeV-2"],
                    color=colors[scenario], linewidth=2.0,
                    label=scenario.replace("_", " "),
                )
            ax.axhline(0.0, color="0.35", linewidth=0.7)
            ax.set_title(
                "Parent-derived gluon Sivers $f_{1T}^{\\perp g}$ - "
                + color.replace("_", " ")
            )
            ax.set_xlabel(r"$k_T$ [GeV]")
            ax.set_ylabel(r"$F(x_N=0.1,k_T;Q=5\,\mathrm{GeV})$ [GeV$^{-2}$]")
            ax.text(
                0.02, 0.03,
                "CGI-GPM color basis; observable hard weights not applied",
                transform=ax.transAxes, fontsize=8.5, color="0.3",
            )
            ax.grid(alpha=0.2)
            ax.legend(frameon=False, fontsize=8.5)
            pdf.savefig(fig)
            plt.close(fig)
    print(f"Wrote {len(output)} rows to {TABLE} and atlas to {PDF}")


if __name__ == "__main__":
    main()
