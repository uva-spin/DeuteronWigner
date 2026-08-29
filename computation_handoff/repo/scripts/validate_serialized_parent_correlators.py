#!/usr/bin/env python3
"""Round-trip serialized parent correlators into their named TMD tables."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.correlator_io import (
    deserialize_gluon_correlator,
    deserialize_quark_correlator,
)
from deuteron_wigner.gtmd_convolution import (
    project_deuteron_gluon_l_t_lt,
    project_deuteron_gluon_tt,
    project_deuteron_gluon_u_ll,
)
from deuteron_wigner.quark_correlator import (
    project_spin1_quark_correlator,
    project_spin1_quark_correlator_at_origin,
)

HBARC_GEV_FM = 0.1973269804
M_D_GEV = 1.87561294257
GROUP_KEYS = (
    "wave_function", "species", "flavor", "mechanism", "gauge_link",
    "x_N", "x_D", "Q_GeV", "k_GeV", "azimuth_rad",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--species", choices=("quark", "gluon"), required=True)
    parser.add_argument("--correlators", type=Path, required=True)
    parser.add_argument("--projections", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def project_gluon(values: np.ndarray, kx_gev: float, ky_gev: float) -> dict:
    momentum = (kx_gev / HBARC_GEV_FM, ky_gev / HBARC_GEV_FM)
    mass = M_D_GEV / HBARC_GEV_FM
    unpolarized, ll = project_deuteron_gluon_u_ll(values, momentum, mass)
    polarized = project_deuteron_gluon_l_t_lt(values, momentum, mass)
    return {
        "f1": unpolarized.trace,
        "h1perp": unpolarized.linear,
        "g1": polarized["L"]["g1"],
        "h1Lperp": polarized["L"]["h1Lperp"],
        **polarized["T"],
        "f1LL": ll.trace,
        "h1LLperp": ll.linear,
        **polarized["LT"],
        **project_deuteron_gluon_tt(values, momentum, mass),
    }


def main() -> None:
    args = parse_args()
    serialized = pd.read_csv(args.correlators)
    expected = pd.read_csv(args.projections)
    reconstructed_rows = []
    for labels, group in serialized.groupby(list(GROUP_KEYS), sort=False):
        label_map = dict(zip(GROUP_KEYS, labels))
        k = float(label_map["k_GeV"])
        angle = float(label_map["azimuth_rad"])
        kx, ky = k * np.cos(angle), k * np.sin(angle)
        if args.species == "quark":
            correlator = deserialize_quark_correlator(group)
            if np.hypot(kx, ky) <= 1.0e-14:
                values = project_spin1_quark_correlator_at_origin(
                    correlator, M_D_GEV
                )
            else:
                values = project_spin1_quark_correlator(
                    correlator, (kx, ky), M_D_GEV
                )
        else:
            correlator = deserialize_gluon_correlator(group)
            values = project_gluon(correlator, kx, ky)
        for tmd, value in values.items():
            reconstructed_rows.append({
                **label_map, "tmd": tmd, "F_reconstructed_GeV-2": value,
            })

    reconstructed = pd.DataFrame(reconstructed_rows)
    joined = expected.merge(
        reconstructed,
        on=[*GROUP_KEYS, "tmd"],
        how="outer",
        validate="one_to_one",
        indicator=True,
    )
    if not bool(joined["_merge"].eq("both").all()):
        raise AssertionError("serialized/projected physical keys do not match")
    difference = (
        joined["F_GeV-2"].to_numpy()
        - joined["F_reconstructed_GeV-2"].to_numpy()
    )
    maximum = float(np.max(np.abs(difference)))
    if maximum > 2.0e-11:
        raise AssertionError(f"round-trip projection residual {maximum:g}")
    report = {
        "status": "pass",
        "species": args.species,
        "correlators": str(args.correlators),
        "projections": str(args.projections),
        "correlator_groups": int(
            serialized.groupby(list(GROUP_KEYS)).ngroups
        ),
        "serialized_rows": int(len(serialized)),
        "projected_rows": int(len(expected)),
        "maximum_absolute_round_trip_residual_GeV-2": maximum,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(f"Serialized correlator validation passed; wrote {args.output}")


if __name__ == "__main__":
    main()
