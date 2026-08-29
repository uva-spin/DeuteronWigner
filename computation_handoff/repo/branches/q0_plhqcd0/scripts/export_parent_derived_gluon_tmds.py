#!/usr/bin/env python3
"""Export all identifiable gluon TMDs through the retained-index LF parent."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.correlator_io import (
    gluon_correlator_rows,
    write_correlator_table,
)
from deuteron_wigner.gtmd_convolution import (
    build_off_forward_component_quadratures,
    convolve_gluon_gtmd_wave_components,
    project_deuteron_gluon_l_t_lt,
    project_deuteron_gluon_tt,
    project_deuteron_gluon_u_ll,
)
from deuteron_wigner.nucleon_gluon_inputs import (
    EvolvedGluonBoundaryConfig,
    build_evolved_gluon_boundary,
)
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.registry import leading_twist_gluon_registry
from deuteron_wigner.wavefunctions.selection import (
    WAVE_FUNCTION_CHOICES,
    select_momentum_wave_function,
)

HBARC_GEV_FM = 0.1973269804
M_N_GEV = 0.93891897
M_D_GEV = 1.87561294257


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wave-function", choices=WAVE_FUNCTION_CHOICES, required=True)
    parser.add_argument("--x-n", type=float, default=0.1)
    parser.add_argument("--scale", type=float, default=5.0)
    parser.add_argument("--k-min-gev", type=float, default=0.05)
    parser.add_argument("--k-max-gev", type=float, default=1.5)
    parser.add_argument("--n-k-points", type=int, default=9)
    parser.add_argument("--boundary-k-max-gev", type=float, default=5.0)
    parser.add_argument("--boundary-k-points", type=int, default=121)
    parser.add_argument("--azimuth", type=float, default=0.37)
    parser.add_argument("--internal-k-max-fm", type=float, default=10.0)
    parser.add_argument("--n-internal-k", type=int, default=16)
    parser.add_argument("--n-cos", type=int, default=12)
    parser.add_argument("--n-phi", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--correlator-output", type=Path)
    return parser.parse_args()


def project_all(correlator: np.ndarray, momentum_fm: tuple[float, float]):
    mass_fm = M_D_GEV / HBARC_GEV_FM
    unpolarized, ll = project_deuteron_gluon_u_ll(
        correlator, momentum_fm, mass_fm
    )
    polarized = project_deuteron_gluon_l_t_lt(
        correlator, momentum_fm, mass_fm
    )
    return {
        "f1": unpolarized.trace,
        "h1perp": unpolarized.linear,
        "g1": polarized["L"]["g1"],
        "h1Lperp": polarized["L"]["h1Lperp"],
        **polarized["T"],
        "f1LL": ll.trace,
        "h1LLperp": ll.linear,
        **polarized["LT"],
        **project_deuteron_gluon_tt(correlator, momentum_fm, mass_fm),
    }


def main() -> None:
    args = parse_args()
    if not 0.0 < args.x_n <= 1.0 or args.k_min_gev <= 0.0:
        raise ValueError("x must be physical and k-min must be positive")
    wave = select_momentum_wave_function(args.wave_function)
    wave.validate_k_max(args.internal_k_max_fm)
    quadratures = build_off_forward_component_quadratures(
        radial=wave.radial,
        nucleon_mass=M_N_GEV / HBARC_GEV_FM,
        k_max=args.internal_k_max_fm,
        delta_x=0.0,
        delta_y=0.0,
        n_k=args.n_internal_k,
        n_cos_theta=args.n_cos,
        n_phi=args.n_phi,
        deuteron_mass=M_D_GEV / HBARC_GEV_FM,
    )
    unpolarized = LHAPDFProvider("CT18NNLO", 0)
    polarized = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
    boundary = build_evolved_gluon_boundary(
        unpolarized,
        polarized,
        config=EvolvedGluonBoundaryConfig(
            scale_GeV=args.scale,
            x_min=args.x_n / 2.0,
            k_max_GeV=args.boundary_k_max_gev,
            k_points=args.boundary_k_points,
        ),
        momentum_unit_to_GeV=HBARC_GEV_FM,
        nucleon_mass_GeV=M_N_GEV,
    )
    entries = {
        entry.name: entry for entry in leading_twist_gluon_registry().select()
    }
    # The exact 2D TT degeneracy replaces these two entries by one observable.
    entries["f1TT_minus_h1TTperp"] = entries["f1TT"]
    k_axis = np.linspace(args.k_min_gev, args.k_max_gev, args.n_k_points)
    rows: list[dict[str, object]] = []
    correlator_table_rows: list[dict[str, object]] = []
    for index, k in enumerate(k_axis):
        kx = float(k * np.cos(args.azimuth))
        ky = float(k * np.sin(args.azimuth))
        wave_components = convolve_gluon_gtmd_wave_components(
            x=args.x_n / 2.0,
            k_x=kx / HBARC_GEV_FM,
            k_y=ky / HBARC_GEV_FM,
            scale=args.scale,
            proton_gtmd=boundary.model,
            neutron_gtmd=boundary.model,
            quadratures=quadratures,
        )
        components = {
            nucleon: sum(
                value[nucleon] for value in wave_components.values()
            )
            for nucleon in ("proton", "neutron")
        }
        components["impulse_total"] = (
            components["proton"] + components["neutron"]
        )
        components.update({
            f"wave_{label}": value["proton"] + value["neutron"]
            for label, value in wave_components.items()
        })
        projected = {
            mechanism: project_all(correlator, (kx / HBARC_GEV_FM, ky / HBARC_GEV_FM))
            for mechanism, correlator in components.items()
        }
        for mechanism, correlator in components.items():
            mechanism_label = (
                f"{mechanism}_impulse"
                if mechanism in ("proton", "neutron")
                else mechanism
            )
            correlator_table_rows.extend(gluon_correlator_rows(
                0.25 * correlator,
                {
                    "wave_function": args.wave_function,
                    "species": "g",
                    "flavor": 21,
                    "mechanism": mechanism_label,
                    "gauge_link": "T-even boundary; T-odd unresolved",
                    "x_N": args.x_n,
                    "x_D": args.x_n / 2.0,
                    "Q_GeV": args.scale,
                    "k_GeV": float(k),
                    "azimuth_rad": args.azimuth,
                },
            ))
        f1 = 0.25 * projected["impulse_total"]["f1"]
        for mechanism, values in projected.items():
            mechanism_label = (
                f"{mechanism}_impulse"
                if mechanism in ("proton", "neutron")
                else mechanism
            )
            for name, raw_value in values.items():
                entry = entries[name]
                value = 0.25 * raw_value
                if entry.t_odd and abs(value) < 1.0e-10:
                    value = 0.0
                rows.append({
                    "wave_function": args.wave_function,
                    "species": "g",
                    "flavor": 21,
                    "mechanism": mechanism_label,
                    "operator_projection": entry.parent_projection,
                    "target_channel": entry.target_channel.value,
                    "tmd": name,
                    "rank": entry.transverse_rank,
                    "t_odd": int(entry.t_odd),
                    "gauge_link": "T-even boundary; T-odd unresolved",
                    "x_N": args.x_n,
                    "x_D": args.x_n / 2.0,
                    "Q_GeV": args.scale,
                    "k_GeV": k,
                    "azimuth_rad": args.azimuth,
                    "F_GeV-2": value,
                    "physical_ratio_to_total_f1": (
                        (k / M_D_GEV) ** entry.transverse_rank * value / f1
                        if f1 != 0.0 else 0.0
                    ),
                    "parent_derived": 1,
                    "identifiability": (
                        "exact_combination_only"
                        if name == "f1TT_minus_h1TTperp"
                        else "projected"
                    ),
                })
        print(f"{args.wave_function} k-point {index + 1}/{len(k_axis)}")
    frame = pd.DataFrame(rows)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(args.output, index=False)
    correlator_output = args.correlator_output or args.output.with_name(
        f"{args.output.stem}.correlators.csv"
    )
    write_correlator_table(correlator_table_rows, correlator_output)
    metadata = {
        "status": "parent-derived matched/CSS-evolved gluon impulse result",
        "wave_function": args.wave_function,
        "quadrature": {
            "n_internal_k": args.n_internal_k,
            "n_cos": args.n_cos,
            "n_phi": args.n_phi,
            "k_max_fm_inverse": args.internal_k_max_fm,
        },
        "boundary": boundary.metadata,
        "normalization": "x_D=x_N/2 and 1/4 per-nucleon x-Jacobian",
        "factorization_validity": {
            "k_T_GeV": [args.k_min_gev, args.k_max_gev],
            "content": "low-k_T CSS W term",
            "full_kT_marginal": False,
            "missing": "fixed-order Y term",
        },
        "TT_identifiability": "f1TT-h1TTperp only at fixed transverse momentum",
        "temporary_or_missing": [
            "T-odd gauge-link phases are absent at the spin-half boundary",
            "nuclear coherent/shadowing/EMC mechanisms not yet applied",
            "proton and neutron gluon inputs equal under charge symmetry but retained separately",
            "finite-b W transform cannot satisfy the full collinear marginal without a Y term",
        ],
        "rows": len(frame),
        "unprojected_correlators": {
            "path": str(correlator_output),
            "format": "long CSV, complex entries split into real/imaginary columns",
            "rows": len(correlator_table_rows),
            "entries_per_correlator": 36,
        },
    }
    args.output.with_suffix(".metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n"
    )
    print(
        f"Wrote {len(frame)} projections to {args.output} and "
        f"{len(correlator_table_rows)} correlator entries to {correlator_output}"
    )


if __name__ == "__main__":
    main()
