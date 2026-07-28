#!/usr/bin/env python3
"""Audit full spin-1 joint-density positivity for every BPV20 member."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.quark_correlator import (
    compose_spin1_quark_correlator,
    quark_correlator_basis,
)
from deuteron_wigner.uncertainty_validation import (
    minimum_eigenvalues_under_component_replacement,
)

M_D_GEV = 1.87561294257
WAVES = ("av18", "cd-bonn", "nvia", "nvib", "nviia", "nviib")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--parent-directory", type=Path, default=Path("outputs/parent_tmds")
    )
    parser.add_argument(
        "--output-directory", type=Path,
        default=Path("outputs/parent_tmds/uncertainty"),
    )
    parser.add_argument("--tolerance", type=float, default=1.0e-10)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    member_minima = np.full((len(WAVES), 2, 500), np.inf)
    point_rows: list[dict[str, object]] = []
    for wave_index, wave in enumerate(WAVES):
        parent = pd.read_csv(args.parent_directory / f"quark_{wave}_fine.csv")
        archive = np.load(
            args.output_directory / f"bpv20_sivers_{wave}_fine.members.npz"
        )
        selected = parent.loc[
            parent.mechanism.isin(("impulse_total", "model_total"))
        ]
        for link_index, link in enumerate(("[+,+]", "[-,-]")):
            linked = selected.loc[selected.gauge_link.eq(link)]
            for labels, group in linked.groupby(
                ["flavor", "flavor_label", "mechanism", "k_GeV"], sort=False
            ):
                flavor, flavor_label, mechanism, k = labels
                if np.isclose(k, 0.0):
                    continue
                angle = float(group.azimuth_rad.iloc[0])
                momentum = (
                    float(k) * np.cos(angle), float(k) * np.sin(angle)
                )
                tmds = dict(zip(group.tmd, group["F_GeV-2"]))
                central = compose_spin1_quark_correlator(
                    momentum, M_D_GEV, tmds
                )
                component = quark_correlator_basis(
                    momentum, M_D_GEV
                )["f1Tperp"]
                members = archive[f"{int(flavor)}_{float(k):.8f}_{mechanism}"]
                if link == "[-,-]":
                    members = -members
                minima = minimum_eigenvalues_under_component_replacement(
                    central, component, tmds["f1Tperp"], members
                )
                member_minima[wave_index, link_index] = np.minimum(
                    member_minima[wave_index, link_index], minima
                )
                point_rows.append({
                    "wave_function": wave,
                    "gauge_link": link,
                    "flavor": int(flavor),
                    "flavor_label": flavor_label,
                    "mechanism": mechanism,
                    "k_GeV": float(k),
                    "minimum_member_eigenvalue": float(minima.min()),
                    "violating_member_count": int(
                        np.count_nonzero(minima < -args.tolerance)
                    ),
                    "worst_member": int(np.argmin(minima) + 1),
                })
    global_minima = member_minima.min(axis=(0, 1))
    compatible = np.flatnonzero(global_minima >= -args.tolerance) + 1
    violating = np.flatnonzero(global_minima < -args.tolerance) + 1
    args.output_directory.mkdir(parents=True, exist_ok=True)
    member_table = pd.DataFrame({
        "member": np.arange(1, 501),
        "global_minimum_eigenvalue": global_minima,
        "tree_level_joint_density_compatible": (
            global_minima >= -args.tolerance
        ).astype(int),
    })
    member_path = args.output_directory / "bpv20_replica_positivity_members.csv"
    point_path = args.output_directory / "bpv20_replica_positivity_points.csv"
    member_table.to_csv(member_path, index=False)
    pd.DataFrame(point_rows).to_csv(point_path, index=False)
    report = {
        "status": "reported theory-scheme tension; not a fit-member rejection",
        "members": 500,
        "compatible_members": len(compatible),
        "violating_members": len(violating),
        "compatible_member_ids": compatible.tolist(),
        "violating_member_ids": violating.tolist(),
        "global_minimum_eigenvalue": float(global_minima.min()),
        "worst_member": int(np.argmin(global_minima) + 1),
        "tolerance": args.tolerance,
        "scope": (
            "six wave functions, future and past links, u/d/ubar/dbar, "
            "impulse_total and model_total, eight nonzero production k knots"
        ),
        "interpretation": (
            "This is the tree-level parton-density PSD diagnostic applied to "
            "soft-subtracted evolved BPV20 TMDs while holding all T-even "
            "inputs at their central values. BPV20 documents violations of "
            "the parton-model Sivers bound. Beyond tree level the diagnostic "
            "is not a scheme-independent probability constraint, so released "
            "members are retained and no conditional confidence interval is "
            "presented as the BPV20 fit uncertainty."
        ),
        "process_consistency": {
            "future_past_member_minima_max_abs_difference": float(
                np.max(np.abs(member_minima[:, 0] - member_minima[:, 1]))
            )
        },
        "outputs": [str(member_path), str(point_path)],
    }
    report_path = args.output_directory / "bpv20_replica_positivity.validation.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n")
    if not np.isfinite(member_minima).all():
        raise AssertionError("non-finite member positivity result")
    if report["process_consistency"][
        "future_past_member_minima_max_abs_difference"
    ] > 5.0e-12:
        raise AssertionError("future/past positivity spectra are inconsistent")
    print(json.dumps({
        key: value for key, value in report.items()
        if key not in ("compatible_member_ids", "violating_member_ids")
    }, indent=2))


if __name__ == "__main__":
    main()
