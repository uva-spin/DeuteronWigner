#!/usr/bin/env python3
"""Export the effective two-cluster non-nucleonic spin-1 TMD boundary."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.hidden_color_cluster_lfwf import (
    EffectiveClusterParameters,
    EffectiveClusterTMDConvolution,
    EffectiveClusterVectorCurrentLFWF,
)
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.quark_correlator import (
    project_spin1_quark_correlator,
    project_spin1_quark_correlator_at_origin,
)
from deuteron_wigner.registry import leading_twist_quark_registry
from deuteron_wigner.gtmd import Species

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
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("outputs/parent_tmds/nonnucleonic_cluster_tmds.csv"),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not 0.0 < args.x_n < 1.0 or args.scale <= 0.0:
        raise ValueError("physical x and Q are required")
    parameters = EffectiveClusterParameters(longitudinal_nodes=240)
    wave = EffectiveClusterVectorCurrentLFWF(
        scalar=None, normalization_nodes=48
    )
    # Ensure the exported parameter contract is explicit even if the wave
    # factory defaults change later.
    if wave.scalar.parameters != EffectiveClusterParameters():
        raise RuntimeError("cluster wave defaults changed; update export provenance")
    convolution = EffectiveClusterTMDConvolution(
        unpolarized=LHAPDFProvider("CT18NNLO", 0),
        polarized=PolarizedLHAPDFProvider("BDSSV24-NLO", 0),
        wave=wave,
        convolution_nodes=48,
    )
    rows = []
    k_axis = np.linspace(0.0, args.k_max_gev, args.n_k_points)
    for flavor, flavor_label, species in FLAVORS:
        registry = {
            entry.name: entry
            for entry in leading_twist_quark_registry(species).select()
        }
        for k in k_axis:
            correlator = convolution.correlator(
                flavor, args.x_n, float(k), args.scale
            )
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
                supported_tmds = {"f1", "g1", "f1LL"}
                # The source construction contains only these three operator
                # tensors. Values in other projector channels are numerical
                # rank-conditioning leakage and are structural zeros here.
                value = (
                    float(projected[tmd]) if tmd in supported_tmds else 0.0
                )
                rows.append(
                    {
                        "scenario": "kaur_2026_effective_two_cluster",
                        "wave_function": "holographic_x_thooft_vector_current",
                        "species": species.value,
                        "flavor": flavor,
                        "flavor_label": flavor_label,
                        "mechanism": "non_nucleonic",
                        "operator_projection": entry.parent_projection,
                        "target_channel": entry.target_channel.value,
                        "tmd": tmd,
                        "rank": entry.transverse_rank,
                        "t_odd": int(entry.t_odd),
                        "gauge_link": "[+,+]",
                        "x_N": args.x_n,
                        "Q_GeV": args.scale,
                        "k_GeV": float(k),
                        "F_GeV-2": value,
                        "parent_derived": 1,
                        "evidence_class": "model_dependent",
                        "uncertainty_axis": "cluster_parameter_scenario",
                        "zero_class": (
                            "nonzero_source_supported"
                            if tmd in supported_tmds
                            else "spin_zero_cluster_pdf_operator_boundary"
                        ),
                    }
                )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    frame = pd.DataFrame(rows)
    frame.to_csv(args.output, index=False)
    metadata = {
        "source": "arXiv:2507.09886 effective two-cluster vector-current LF state",
        "cluster_pdf_inputs": ["CT18NNLO member 0", "BDSSV24-NLO member 0"],
        "implemented_nonzero_tmds": ["f1", "g1", "f1LL"],
        "intrinsic_parton_kT": (
            "collinear boundary; transverse momentum is generated by the "
            "effective cluster wave only"
        ),
        "parameters": {
            "cluster_mass_gev": parameters.cluster_mass_gev,
            "transverse_kappa_gev": parameters.transverse_kappa_gev,
            "longitudinal_g_gev": parameters.longitudinal_g_gev,
        },
        "rows": len(frame),
        "normalization": "dimensional F in GeV^-2",
        "limitations": (
            "sensitivity component, not an extracted hidden-color probability; "
            "intrinsic cluster-parton transverse structure remains replaceable"
        ),
    }
    args.output.with_suffix(".metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n"
    )
    print(f"Wrote {len(frame)} rows to {args.output}")


if __name__ == "__main__":
    main()
