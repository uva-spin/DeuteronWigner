#!/usr/bin/env python3
"""Export the Fock-normalized spin-resolved Sullivan-pion TMD correlator."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.gtmd import Species
from deuteron_wigner.pion_exchange import (
    FockNormalizedMillerPionDistribution,
    JAM21IsoscalarPionPDF,
    MillerTensorPionDistribution,
)
from deuteron_wigner.pion_tmd import (
    SpinResolvedTransversePionBoundary,
    Vpion19IntrinsicProfile,
)
from deuteron_wigner.quark_correlator import (
    project_spin1_quark_correlator,
    project_spin1_quark_correlator_at_origin,
)
from deuteron_wigner.registry import leading_twist_quark_registry

M_D_GEV = 1.87561294257
FLAVORS = (
    (2, "u", Species.QUARK),
    (1, "d", Species.QUARK),
    (-2, "ubar", Species.ANTIQUARK),
    (-1, "dbar", Species.ANTIQUARK),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x-n", type=float, default=0.1)
    parser.add_argument("--scale", type=float, default=5.0)
    parser.add_argument("--k-max-gev", type=float, default=1.5)
    parser.add_argument("--n-k-points", type=int, default=41)
    parser.add_argument("--azimuth", type=float, default=0.37)
    parser.add_argument("--b-max-gev-inv", type=float, default=12.0)
    parser.add_argument("--b-nodes", type=int, default=64)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("outputs/parent_tmds/spin_resolved_pion_tmds.csv"),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    raw = MillerTensorPionDistribution()
    splitting = FockNormalizedMillerPionDistribution(raw)
    boundary = SpinResolvedTransversePionBoundary(
        splitting,
        JAM21IsoscalarPionPDF(0),
        Vpion19IntrinsicProfile(0),
    )
    k_axis = np.linspace(0.0, args.k_max_gev, args.n_k_points)
    rows = []
    supported = {"f1", "f1LL"}
    for flavor, flavor_label, species in FLAVORS:
        correlators = boundary.correlators_k(
            flavor,
            args.x_n,
            k_axis,
            args.scale,
            b_max_gev_inv=args.b_max_gev_inv,
            b_nodes=args.b_nodes,
        )
        registry = {
            entry.name: entry
            for entry in leading_twist_quark_registry(species).select()
        }
        for k, correlator in zip(k_axis, correlators):
            projected = (
                project_spin1_quark_correlator_at_origin(correlator, M_D_GEV)
                if k == 0.0
                else project_spin1_quark_correlator(
                    correlator,
                    (
                        float(k * np.cos(args.azimuth)),
                        float(k * np.sin(args.azimuth)),
                    ),
                    M_D_GEV,
                )
            )
            for tmd, entry in registry.items():
                rows.append(
                    {
                        "scenario": "miller_jam21_vpion19_fock_normalized",
                        "species": species.value,
                        "flavor": flavor,
                        "flavor_label": flavor_label,
                        "mechanism": "meson_exchange",
                        "operator_projection": entry.parent_projection,
                        "target_channel": entry.target_channel.value,
                        "tmd": tmd,
                        "rank": entry.transverse_rank,
                        "t_odd": int(entry.t_odd),
                        "gauge_link": "[+,+]",
                        "x_N": args.x_n,
                        "Q_GeV": args.scale,
                        "k_GeV": float(k),
                        "F_GeV-2": (
                            float(projected[tmd]) if tmd in supported else 0.0
                        ),
                        "parent_derived": 1,
                        "evidence_class": "model_dependent",
                        "uncertainty_axis": (
                            "JAM21_replica_x_axial_mass_x_Vpion19_replica"
                        ),
                        "zero_class": (
                            "nonzero_source_supported"
                            if tmd in supported
                            else "spin_zero_pion_operator_boundary"
                        ),
                    }
                )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    frame = pd.DataFrame(rows)
    frame.to_csv(args.output, index=False)
    ledger = splitting.ledger
    metadata = {
        "source": (
            "Miller Sullivan NNpi spin projections arXiv:1311.4561; "
            "JAM21PionPDFnlo; Vpion19 intrinsic profile arXiv:1907.10356"
        ),
        "implemented_nonzero_tmds": ["f1", "f1LL"],
        "transform": "rank-zero Fourier-Bessel J0 from common b-space correlator",
        "b_max_gev_inv": args.b_max_gev_inv,
        "b_nodes": args.b_nodes,
        "fock_ledger": {
            "Z": ledger.z_factor,
            "pinn_probability": ledger.pinn_probability,
            "pion_plus_momentum": ledger.pinn_sector_pion_momentum,
            "pinn_nucleon_plus_momentum": ledger.pinn_sector_nucleon_momentum,
            "nn_nucleon_plus_momentum": ledger.nn_sector_nucleon_momentum,
            "total_plus_momentum": ledger.total_momentum,
        },
        "rows": len(frame),
        "normalization": "dimensional F in GeV^-2",
        "limitation": (
            "pion component exported separately; coupled NNpi transverse recoil "
            "counterterm remains a distinct configurable mechanism"
        ),
    }
    args.output.with_suffix(".metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n"
    )
    print(f"Wrote {len(frame)} rows to {args.output}")


if __name__ == "__main__":
    main()
