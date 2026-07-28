#!/usr/bin/env python3
"""Build smooth, provenance-preserving wave-function envelopes and atlases."""

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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-directory", type=Path, default=Path("outputs/parent_tmds")
    )
    parser.add_argument(
        "--output-directory", type=Path,
        default=Path("outputs/parent_tmds/ensemble"),
    )
    parser.add_argument("--dense-points", type=int, default=241)
    parser.add_argument("--quark-grid-label", default="fine")
    parser.add_argument("--gluon-grid-label", default="medium")
    return parser.parse_args()


def load_species(directory: Path, species: str, grid_label: str) -> pd.DataFrame:
    frames = []
    for wave in WAVES:
        path = directory / f"{species}_{wave}_{grid_label}.csv"
        frame = pd.read_csv(path)
        frame["wave_function"] = wave
        frames.append(frame)
    return pd.concat(frames, ignore_index=True)


def dense_envelope(
    frame: pd.DataFrame,
    *,
    group_columns: list[str],
    mechanism: str,
    dense_points: int,
) -> pd.DataFrame:
    selected = frame.loc[frame.mechanism.eq(mechanism)].copy()
    # Current parent boundaries are explicitly real. Values below this scale
    # in T-odd rows are projector roundoff, not a physical uncertainty band.
    selected.loc[
        selected.t_odd.eq(1) & selected["F_GeV-2"].abs().lt(1.0e-10),
        "F_GeV-2",
    ] = 0.0
    rows = []
    for labels, group in selected.groupby(group_columns, sort=False):
        if not isinstance(labels, tuple):
            labels = (labels,)
        curves = {}
        for wave, wave_group in group.groupby("wave_function"):
            wave_group = wave_group.sort_values("k_GeV")
            curves[wave] = PchipInterpolator(
                wave_group.k_GeV, wave_group["F_GeV-2"], extrapolate=False
            )
        missing = set(WAVES) - set(curves)
        if missing:
            raise ValueError(f"missing wave functions: {sorted(missing)}")
        k_axis = np.linspace(group.k_GeV.min(), group.k_GeV.max(), dense_points)
        values = np.vstack([curves[wave](k_axis) for wave in WAVES])
        central = curves["av18"](k_axis)
        for index, k in enumerate(k_axis):
            row = dict(zip(group_columns, labels))
            row.update({
                "k_GeV": float(k),
                "F_central_GeV-2": float(central[index]),
                "F_wave_low_GeV-2": float(values[:, index].min()),
                "F_wave_high_GeV-2": float(values[:, index].max()),
                "central_wave_function": "av18",
                "wave_function_members": ",".join(WAVES),
                "interpolation": "PCHIP through calculated knots",
                "calculated_knot_count": int(group.k_GeV.nunique()),
            })
            rows.append(row)
    return pd.DataFrame(rows)


def make_atlas(frame: pd.DataFrame, path: Path, title_prefix: str) -> None:
    group_columns = [
        column for column in ("flavor_label", "tmd", "target_channel")
        if column in frame
    ]
    with PdfPages(path) as pdf:
        for labels, group in frame.groupby(group_columns, sort=False):
            if not isinstance(labels, tuple):
                labels = (labels,)
            label_map = dict(zip(group_columns, labels))
            fig, ax = plt.subplots(figsize=(7.2, 4.8), constrained_layout=True)
            ax.fill_between(
                group.k_GeV,
                group["F_wave_low_GeV-2"],
                group["F_wave_high_GeV-2"],
                color="#4C78A8", alpha=0.25, linewidth=0,
                label="six-wave-function envelope",
            )
            ax.plot(
                group.k_GeV, group["F_central_GeV-2"],
                color="#163A5F", linewidth=2.1, label="AV18 central",
            )
            ax.axhline(0.0, color="0.35", linewidth=0.7)
            flavor = label_map.get("flavor_label", "g")
            ax.set_title(
                f"{title_prefix}: {flavor}  {label_map['tmd']}"
                f"  [{label_map['target_channel']}]"
            )
            ax.set_xlabel(r"$k_T$ [GeV]")
            ax.set_ylabel(r"$F(x_N=0.1,k_T;Q=5\,\mathrm{GeV})$ [GeV$^{-2}$]")
            ax.grid(alpha=0.2)
            if "factorization_valid" in group and not group[
                "factorization_valid"
            ].all():
                invalid = group.loc[~group["factorization_valid"]]
                boundary = float(invalid.k_GeV.min())
                ax.axvspan(
                    boundary, float(group.k_GeV.max()), color="0.5",
                    alpha=0.12, hatch="//", linewidth=0,
                    label="outside W-only validity; process Y required",
                )
                ax.axvline(boundary, color="0.4", linewidth=0.8)
            if np.max(np.abs(group["F_wave_high_GeV-2"])) == 0.0 and np.max(
                np.abs(group["F_wave_low_GeV-2"])
            ) == 0.0:
                ax.set_ylim(-1.0, 1.0)
                ax.text(
                    0.5, 0.60,
                    "configured baseline zero in this component\n"
                    "(not a physical null prediction)",
                    transform=ax.transAxes, ha="center", va="center",
                    color="0.25",
                )
            ax.legend(frameon=False, fontsize=9)
            pdf.savefig(fig)
            plt.close(fig)


def main() -> None:
    args = parse_args()
    args.output_directory.mkdir(parents=True, exist_ok=True)
    quark = load_species(args.input_directory, "quark", args.quark_grid_label)
    # Show the future/SIDIS reference once. T-even rows coincide while fitted
    # Sivers rows in the past/DY table are the exact sign transform.
    quark = quark.loc[quark.gauge_link.eq("[+,+]")]
    quark_dense = dense_envelope(
        quark,
        group_columns=[
            "species", "flavor", "flavor_label", "tmd", "target_channel",
            "rank", "t_odd", "x_N", "Q_GeV",
        ],
        mechanism="model_total",
        dense_points=args.dense_points,
    )
    gluon = load_species(args.input_directory, "gluon", args.gluon_grid_label)
    gluon_dense = dense_envelope(
        gluon,
        group_columns=[
            "species", "flavor", "tmd", "target_channel", "rank", "t_odd",
            "x_N", "Q_GeV",
        ],
        mechanism="impulse_total",
        dense_points=args.dense_points,
    )
    gluon_dense["flavor_label"] = "g"
    gluon_dense["factorization_valid"] = (
        (gluon_dense["k_GeV"] <= 1.0)
        & (gluon_dense["k_GeV"] / gluon_dense["Q_GeV"] <= 0.25)
    )
    quark_path = args.output_directory / "quark_parent_tmd_ensemble.csv"
    gluon_path = args.output_directory / "gluon_parent_tmd_ensemble.csv"
    quark_dense.to_csv(quark_path, index=False)
    gluon_dense.to_csv(gluon_path, index=False)
    make_atlas(
        quark_dense,
        args.output_directory / "quark_parent_tmd_atlas.pdf",
        "Parent-derived quark TMD",
    )
    make_atlas(
        gluon_dense,
        args.output_directory / "gluon_parent_tmd_atlas.pdf",
        "Parent-derived gluon TMD",
    )
    metadata = {
        "status": "smooth visualization of parent-derived calculated knots",
        "central": "AV18",
        "band": "pointwise min/max of AV18, CD-Bonn, NV-Ia, NV-Ib, NV-IIa, NV-IIb",
        "interpolation": "PCHIP; no extrapolation",
        "important": "interpolation adds no physical information",
        "quark_mechanism": "model_total including separately stored temporary corrections",
        "gluon_mechanism": "impulse_total; nuclear correction bands not yet implemented",
        "gluon_factorization_domain": (
            "W-only valid for kT<=1 GeV and kT/Q<=0.25; serialized flag and "
            "hatched atlas region enforce that higher kT needs an "
            "observable-specific sourced Y=FO-ASY remainder"
        ),
        "gauge_link": (
            "future/SIDIS reference shown; T-even rows are link invariant and "
            "BPV20 Sivers past/DY rows reverse sign exactly"
        ),
        "quark_grid_label": args.quark_grid_label,
        "gluon_grid_label": args.gluon_grid_label,
        "rows": {"quark": len(quark_dense), "gluon": len(gluon_dense)},
    }
    (args.output_directory / "ensemble.metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n"
    )
    print(f"Wrote {quark_path} and {gluon_path}")


if __name__ == "__main__":
    main()
