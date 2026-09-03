#!/usr/bin/env python3
"""Export multi-x AV18 LF parents required by conditional NNpi recoil."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.correlator_io import quark_correlator_rows, write_correlator_table
from deuteron_wigner.gtmd import Species
from deuteron_wigner.gtmd_convolution import build_off_forward_component_quadratures
from deuteron_wigner.nucleon_inputs import build_nucleon_quark_models
from deuteron_wigner.parent_quark_tmd import (
    convolve_spin1_quark_collinear_correlator,
)
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.quark_correlator import Spin1QuarkCorrelator
from deuteron_wigner.wavefunctions.selection import select_momentum_wave_function

HBARC_GEV_FM = 0.1973269804
M_N_GEV = 0.93891897
M_D_GEV = 1.87561294257
FLAVORS = (
    (2, "u", Species.QUARK),
    (1, "d", Species.QUARK),
    (-2, "ubar", Species.ANTIQUARK),
    (-1, "dbar", Species.ANTIQUARK),
)


def _grid(kind: str) -> np.ndarray:
    anchors = np.array([
        0.001, 0.002, 0.004, 0.007, 0.012, 0.020, 0.032, 0.050,
        0.075, 0.100, 0.140, 0.190, 0.250, 0.330, 0.430, 0.560,
        0.700, 0.850, 0.950,
    ])
    if kind == "coarse":
        return anchors
    return np.unique(np.concatenate((anchors, np.sqrt(anchors[:-1] * anchors[1:]))))


def _sum(values) -> Spin1QuarkCorrelator:
    items = tuple(values)
    return Spin1QuarkCorrelator(
        sum(item.vector for item in items),
        sum(item.axial for item in items),
        sum(item.transverse for item in items),
    )


def _scale(value: Spin1QuarkCorrelator, factor: float) -> Spin1QuarkCorrelator:
    return Spin1QuarkCorrelator(
        factor * value.vector, factor * value.axial, factor * value.transverse
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--grid", choices=("coarse", "refined"), required=True)
    parser.add_argument("--scale", type=float, default=5.0)
    parser.add_argument("--n-internal-k", type=int, default=24)
    parser.add_argument("--n-cos", type=int, default=16)
    parser.add_argument("--n-phi", type=int, default=12)
    parser.add_argument(
        "--reuse",
        type=Path,
        help="reuse exact matching x nodes from an existing correlator table",
    )
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    wave = select_momentum_wave_function("av18")
    wave.validate_k_max(10.0)
    quadratures = build_off_forward_component_quadratures(
        radial=wave.radial,
        nucleon_mass=M_N_GEV / HBARC_GEV_FM,
        k_max=10.0,
        delta_x=0.0,
        delta_y=0.0,
        n_k=args.n_internal_k,
        n_cos_theta=args.n_cos,
        n_phi=args.n_phi,
        deuteron_mass=M_D_GEV / HBARC_GEV_FM,
    )
    proton_model, neutron_model = build_nucleon_quark_models(
        LHAPDFProvider("CT18NNLO", 0),
        PolarizedLHAPDFProvider("BDSSV24-NLO", 0),
    )
    rows: list[dict[str, object]] = []
    reused_x: set[float] = set()
    if args.reuse is not None:
        reused = pd.read_csv(args.reuse)
        if not np.allclose(reused["Q_GeV"].to_numpy(float), args.scale):
            raise ValueError("reuse table scale does not match requested scale")
        rows.extend(reused.to_dict(orient="records"))
        reused_x = set(reused["x_N"].unique().astype(float))
    x_nodes = _grid(args.grid)
    max_hermiticity = 0.0
    max_pn_difference = 0.0
    for ix, x_n in enumerate(x_nodes):
        if float(x_n) in reused_x:
            print(f"{args.grid}: reused x node {ix + 1}/{x_nodes.size}", flush=True)
            continue
        for flavor, label, species in FLAVORS:
            components = {
                label: convolve_spin1_quark_collinear_correlator(
                    x=float(x_n / 2.0),
                    scale=args.scale,
                    flavor=flavor,
                    proton=proton_model,
                    neutron=neutron_model,
                    quadrature=quadrature,
                )
                for label, quadrature in quadratures.items()
            }
            proton = _scale(_sum(v.proton for v in components.values()), 0.25)
            neutron = _scale(_sum(v.neutron for v in components.values()), 0.25)
            total = _sum((proton, neutron))
            max_pn_difference = max(
                max_pn_difference,
                float(np.max(np.abs(proton.vector - neutron.vector))),
            )
            for mechanism, correlator in (
                ("proton_impulse", proton),
                ("neutron_impulse", neutron),
                ("impulse_total", total),
            ):
                max_hermiticity = max(
                    max_hermiticity,
                    float(np.max(np.abs(
                        correlator.vector - correlator.vector.conj().T
                    ))),
                )
                rows.extend(quark_correlator_rows(correlator, {
                    "wave_function": "av18",
                    "species": species.value,
                    "flavor": flavor,
                    "flavor_label": label,
                    "mechanism": mechanism,
                    "gauge_link": "[collinear,T-even]",
                    "x_N": float(x_n),
                    "x_D": float(x_n / 2.0),
                    "Q_GeV": args.scale,
                    "k_GeV": 0.0,
                    "azimuth_rad": 0.0,
                }))
        print(f"{args.grid}: x node {ix + 1}/{x_nodes.size}", flush=True)
    write_correlator_table(rows, args.output)
    metadata = {
        "status": "production LF parent grid for conditional NNpi recoil",
        "wave_function": "av18",
        "grid": args.grid,
        "x_nodes": x_nodes.tolist(),
        "scale_gev": args.scale,
        "quadrature": {
            "n_internal_k": args.n_internal_k,
            "n_cos": args.n_cos,
            "n_phi": args.n_phi,
        },
        "normalization": "x_D-to-x_N Jacobian and per-nucleon factor 1/4",
        "parent_limit": (
            "exact b_T=0 collinear rank-zero LF contraction; not momentum-space k_T=0"
        ),
        "flavors": [label for _, label, _ in FLAVORS],
        "proton_neutron_kept_separate": True,
        "reused_parent": str(args.reuse) if args.reuse is not None else None,
        "reused_x_nodes": sorted(reused_x),
        "max_target_hermiticity_residual": max_hermiticity,
        "max_proton_neutron_vector_difference": max_pn_difference,
    }
    args.output.with_suffix(".metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n"
    )


if __name__ == "__main__":
    main()
