#!/usr/bin/env python3
"""Build smooth separated scenario and wave envelopes for all 18 quark TMDs."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from scipy.interpolate import PchipInterpolator

from deuteron_wigner.quark_correlator import SPIN1_QUARK_TMD_NAMES

INPUT = Path("outputs/parent_tmds/evolved_quark_parent_scenarios.csv")
OUTPUT_PDF = Path("output/pdf/evolved_quark_parent_atlas.pdf")
OUTPUT_CSV = Path("outputs/parent_tmds/ensemble/evolved_quark_parent_bands.csv")
FLAVOR_LABELS = {2: r"$u$", 1: r"$d$", -2: r"$\bar u$", -1: r"$\bar d$"}
RANK_ZERO = {"f1", "g1", "h1", "f1LL", "h1LT"}
TEX = {
    "f1": r"f_1", "h1perp": r"h_1^\perp", "g1": r"g_1",
    "h1Lperp": r"h_{1L}^\perp", "f1Tperp": r"f_{1T}^\perp",
    "g1T": r"g_{1T}", "h1": r"h_1", "h1Tperp": r"h_{1T}^\perp",
    "f1LL": r"f_{1LL}", "h1LLperp": r"h_{1LL}^\perp",
    "f1LT": r"f_{1LT}", "g1LT": r"g_{1LT}", "h1LT": r"h_{1LT}",
    "h1LTperp": r"h_{1LT}^\perp", "f1TT": r"f_{1TT}",
    "g1TT": r"g_{1TT}", "h1TT": r"h_{1TT}",
    "h1TTperp": r"h_{1TT}^\perp",
}


def smooth(k, values, axis):
    return PchipInterpolator(k, values)(axis)


def main() -> None:
    table = defaultdict(dict)
    with INPUT.open() as stream:
        for row in csv.DictReader(stream):
            key = (
                row["wave_function"], row["scenario"], int(row["flavor"]),
                row["part"], row["tmd"],
            )
            table[key][float(row["k_T_GeV"])] = float(row["value_GeV-2"])

    band_rows = []
    OUTPUT_PDF.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with PdfPages(OUTPUT_PDF) as pdf:
        for page_number, tmd in enumerate(SPIN1_QUARK_TMD_NAMES, start=1):
            fig, axes = plt.subplots(2, 2, figsize=(10.5, 7.8), sharex=True)
            for axis_plot, flavor in zip(axes.ravel(), (2, 1, -2, -1)):
                knots = np.asarray(sorted(
                    table[("av18", "central", flavor, "total", tmd)]
                ))
                if tmd not in RANK_ZERO:
                    knots = knots[knots > 0.0]
                dense = np.linspace(knots[0], knots[-1], 301)

                def curve(wave, scenario, part):
                    values = np.asarray([
                        table[(wave, scenario, flavor, part, tmd)][point]
                        for point in knots
                    ])
                    return smooth(knots, values, dense)

                central = curve("av18", "central", "total")
                proton = curve("av18", "central", "proton")
                neutron = curve("av18", "central", "neutron")
                negative = curve("av18", "negative", "total")
                positive = curve("av18", "positive", "total")
                scenario_low = np.minimum(negative, positive)
                scenario_high = np.maximum(negative, positive)
                waves = np.asarray([
                    curve(wave, "central", "total")
                    for wave in ("av18", "cd-bonn", "nvia", "nvib", "nviia", "nviib")
                ])
                wave_low = np.min(waves, axis=0)
                wave_high = np.max(waves, axis=0)
                axis_plot.fill_between(
                    dense, wave_low, wave_high, color="#4C78A8", alpha=0.18,
                    label="six-wave envelope",
                )
                axis_plot.fill_between(
                    dense, scenario_low, scenario_high, color="#F58518",
                    alpha=0.24, label="pretzelosity scenario",
                )
                axis_plot.plot(dense, central, color="black", lw=1.8, label="AV18 total")
                axis_plot.plot(
                    dense, proton, color="#1f77b4", lw=1.15, ls="--",
                    label="proton piece",
                )
                axis_plot.plot(
                    dense, neutron, color="#d62728", lw=1.15, ls=":",
                    label="neutron piece",
                )
                axis_plot.axhline(0.0, color="0.5", lw=0.6)
                axis_plot.text(
                    0.97, 0.93, FLAVOR_LABELS[flavor],
                    transform=axis_plot.transAxes, ha="right", va="top",
                    fontsize=12,
                    bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.7},
                )
                axis_plot.grid(alpha=0.18)
                for index, momentum in enumerate(dense):
                    band_rows.append({
                        "tmd": tmd, "flavor": flavor,
                        "k_T_GeV": momentum,
                        "central_AV18_GeV-2": central[index],
                        "proton_AV18_GeV-2": proton[index],
                        "neutron_AV18_GeV-2": neutron[index],
                        "scenario_low_GeV-2": scenario_low[index],
                        "scenario_high_GeV-2": scenario_high[index],
                        "wave_low_GeV-2": wave_low[index],
                        "wave_high_GeV-2": wave_high[index],
                    })
            fig.suptitle(
                rf"Spin-1 deuteron ${TEX[tmd]}$ at $x_N=0.1$, $Q=5$ GeV",
                fontsize=15, y=0.975,
            )
            fig.supxlabel(r"$k_T$ [GeV]", y=0.073)
            fig.supylabel(r"$F(x,k_T)$ [GeV$^{-2}$]")
            handles, labels = axes[0, 0].get_legend_handles_labels()
            fig.legend(
                handles, labels, loc="lower center", ncol=5, frameon=False,
                bbox_to_anchor=(0.5, 0.008), fontsize=8.5,
            )
            fig.text(
                0.99, 0.01, f"{page_number}/18", ha="right", va="bottom",
                fontsize=8, color="0.4",
            )
            fig.subplots_adjust(
                left=0.09, right=0.98, top=0.91, bottom=0.15,
                wspace=0.22, hspace=0.22,
            )
            pdf.savefig(fig)
            plt.close(fig)

    with OUTPUT_CSV.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(band_rows[0]))
        writer.writeheader()
        writer.writerows(band_rows)
    print({
        "pdf": str(OUTPUT_PDF),
        "pages": len(SPIN1_QUARK_TMD_NAMES),
        "band_rows": len(band_rows),
        "csv": str(OUTPUT_CSV),
    })


if __name__ == "__main__":
    main()
