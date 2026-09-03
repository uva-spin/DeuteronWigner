#!/usr/bin/env python3
"""Plot smooth flavor-separated NNpi JAM21 central lines and bands."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    frame = pd.read_csv(args.input)
    flavors = ("u", "d", "ubar", "dbar")
    colors = {"f1": "#1f5a94", "f1LL": "#b1463c"}
    fig, axes = plt.subplots(2, 4, figsize=(14.0, 6.4), sharex="col")
    for column, flavor in enumerate(flavors):
        for row, tmd in enumerate(("f1", "f1LL")):
            axis = axes[row, column]
            values = frame[
                (frame["flavor_label"] == flavor) & (frame["tmd"] == tmd)
            ].sort_values("x_N")
            x = values["x_N"].to_numpy()
            mean = values["jam21_replica_mean"].to_numpy()
            low = values["jam21_q16"].to_numpy()
            high = values["jam21_q84"].to_numpy()
            axis.plot(x, mean, color=colors[tmd], lw=2.0, label=tmd)
            axis.fill_between(x, low, high, color=colors[tmd], alpha=0.24)
            axis.axhline(0.0, color="0.35", lw=0.7)
            axis.set_xscale("log")
            axis.grid(alpha=0.2)
            axis.legend(frameon=False, loc="best")
            if row == 0:
                axis.set_title(flavor)
            else:
                axis.set_xlabel(r"$x_N$")
    axes[0, 0].set_ylabel(r"$f_1(x_N,Q=5\,\mathrm{GeV})$")
    axes[1, 0].set_ylabel(r"$f_{1LL}(x_N,Q=5\,\mathrm{GeV})$")
    fig.suptitle("AV18 conditional NNπ recoil: JAM21 replica mean and 16–84% band")
    fig.tight_layout()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output)
    fig.savefig(args.output.with_suffix(".png"), dpi=180)
    plt.close(fig)


if __name__ == "__main__":
    main()
