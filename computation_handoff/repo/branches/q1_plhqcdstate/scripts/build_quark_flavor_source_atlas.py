#!/usr/bin/env python3
"""Expose retained AV18 proton/neutron flavor sources behind deuteron totals."""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import pandas as pd
from scipy.interpolate import PchipInterpolator

DEFAULT_SOURCE = Path("outputs/parent_tmds/quark_av18_fine.csv")
DEFAULT_OUTDIR = Path("outputs/parent_tmds/ensemble")
MECHANISMS = ("proton_impulse", "neutron_impulse", "impulse_total", "model_total")
STYLES = {
    "proton_impulse": ("#D55E00", "--", "active proton"),
    "neutron_impulse": ("#0072B2", "-.", "active neutron"),
    "impulse_total": ("#222222", ":", "impulse sum"),
    "model_total": ("#009E73", "-", "configured model total"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output-directory", type=Path, default=DEFAULT_OUTDIR)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    data = pd.read_csv(args.source)
    data = data.loc[
        data.gauge_link.eq("[+,+]") & data.mechanism.isin(MECHANISMS)
    ]
    rows = []
    group_keys = ["flavor_label", "tmd", "target_channel"]
    for labels, group in data.groupby(group_keys, sort=False):
        k = np.linspace(group.k_GeV.min(), group.k_GeV.max(), 241)
        for mechanism in MECHANISMS:
            member = group.loc[group.mechanism.eq(mechanism)].sort_values("k_GeV")
            if member.empty:
                raise ValueError(f"missing {labels} {mechanism}")
            values = PchipInterpolator(member.k_GeV, member["F_GeV-2"])(k)
            values[np.abs(values) < 1.0e-10] = 0.0
            rows.extend(
                {
                    **dict(zip(group_keys, labels)),
                    "mechanism": mechanism,
                    "x_N": 0.1,
                    "Q_GeV": 5.0,
                    "k_GeV": float(ki),
                    "F_GeV-2": float(fi),
                    "interpolation": "PCHIP through calculated AV18 knots",
                }
                for ki, fi in zip(k, values)
            )
    dense = pd.DataFrame(rows)
    args.output_directory.mkdir(parents=True, exist_ok=True)
    dense.to_csv(
        args.output_directory / "quark_flavor_source_decomposition.csv",
        index=False,
    )
    with PdfPages(
        args.output_directory / "quark_flavor_source_decomposition_atlas.pdf"
    ) as pdf:
        for labels, group in dense.groupby(group_keys, sort=False):
            fig, ax = plt.subplots(figsize=(7.2, 4.8), constrained_layout=True)
            for mechanism in MECHANISMS:
                member = group.loc[group.mechanism.eq(mechanism)]
                color, linestyle, label = STYLES[mechanism]
                ax.plot(member.k_GeV, member["F_GeV-2"], color=color,
                        linestyle=linestyle, linewidth=2.0, label=label)
            flavor, tmd, channel = labels
            ax.axhline(0, color="0.4", linewidth=0.7)
            ax.set_title(f"Retained flavor sources: {flavor}  {tmd}  [{channel}]")
            ax.set_xlabel(r"$k_T$ [GeV]")
            ax.set_ylabel(r"$F(x_N=0.1,k_T;Q=5\,\mathrm{GeV})$ [GeV$^{-2}$]")
            ax.grid(alpha=0.2)
            if group["F_GeV-2"].abs().max() == 0.0:
                ax.set_ylim(-1.0, 1.0)
                ax.text(
                    0.5, 0.53,
                    "configured zero in this sourced component",
                    transform=ax.transAxes, ha="center", va="center",
                    color="0.25",
                )
            ax.legend(frameon=False)
            pdf.savefig(fig)
            plt.close(fig)
    print("Wrote AV18 quark source-decomposition table and atlas")


if __name__ == "__main__":
    main()
