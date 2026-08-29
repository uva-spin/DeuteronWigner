#!/usr/bin/env python3
"""Exercise the rank-zero evolved quark boundary inside the physical LF parent."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from deuteron_wigner.evolved_quark_model import EvolvedRankZeroQuarkModel
from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.gtmd_convolution import build_off_forward_spin_quadrature
from deuteron_wigner.nucleon_inputs import build_nucleon_quark_models
from deuteron_wigner.parent_quark_tmd import (
    convolve_spin1_quark_correlator,
    project_parent_derived_quark_tmds,
)
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.quark_tmd_matching import MatchedRankZeroQuarkTMD
from deuteron_wigner.tmd_evolution import (
    EvolvedMatchedRankZeroQuarkTMD,
    OneLoopQuarkCSSEvolution,
)
from deuteron_wigner.transversity import JAMDiFFTransversityGrid
from deuteron_wigner.wavefunctions.selection import select_momentum_wave_function
from deuteron_wigner.wavefunctions.selection import WAVE_FUNCTION_CHOICES

HBARC_GEV_FM = 0.1973269804
M_N_GEV = 0.93891897
M_D_GEV = 1.87561294257
OUTPUT = Path(
    "outputs/parent_tmds/evolved_quark_parent_connection.validation.json"
)


def main() -> None:
    pdf = LHAPDFProvider("CT18NNLO", 0)
    polarized = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
    transversity = JAMDiFFTransversityGrid(
        "data/processed/jamdiff_wlqcd_transversity.csv"
    )
    proton, neutron = build_nucleon_quark_models(
        pdf, polarized, transversity_input=transversity
    )
    wave = select_momentum_wave_function("av18")

    def make_quadrature(orders):
        return build_off_forward_spin_quadrature(
            radial=wave.radial,
            nucleon_mass=M_N_GEV / HBARC_GEV_FM,
            k_max=10.0,
            n_k=orders[0],
            n_cos_theta=orders[1],
            n_phi=orders[2],
            delta_x=0.0,
            delta_y=0.0,
        )

    quadrature = make_quadrature((8, 6, 6))

    def wrap(model, n_b):
        boundary = MatchedRankZeroQuarkTMD(model)
        return EvolvedRankZeroQuarkModel(
            model,
            EvolvedMatchedRankZeroQuarkTMD(
                boundary, OneLoopQuarkCSSEvolution(pdf.alpha_s)
            ),
            b_max_gev_inverse=12.0,
            n_b=n_b,
            evolve_rank_one=False,
            evolve_rank_two=False,
        )

    wrapper_pairs = {}

    def wrappers(n_b):
        if n_b not in wrapper_pairs:
            wrapper_pairs[n_b] = (wrap(proton, n_b), wrap(neutron, n_b))
        return wrapper_pairs[n_b]

    def evaluate(flavor, quadrature, n_b):
        evolved_proton, evolved_neutron = wrappers(n_b)
        parent = convolve_spin1_quark_correlator(
                x=0.05,
                k_x=0.3 / HBARC_GEV_FM,
                k_y=0.0,
                scale=5.0,
                flavor=flavor,
                proton=evolved_proton,
                neutron=evolved_neutron,
                gauge_link=GaugeLink("+", "+"),
                quadrature=quadrature,
                momentum_unit_to_gev=HBARC_GEV_FM,
            )
        projected = project_parent_derived_quark_tmds(
                parent,
                k_x_gev=0.3,
                k_y_gev=0.0,
                deuteron_mass_gev=M_D_GEV,
            )
        return {
            part: {
                name: float(value)
                for name, value in projected[part].items()
                if name in ("f1", "g1", "h1")
            }
            for part in ("proton", "neutron", "total")
        }

    rows = []
    for flavor in (2, 1, -2, -1):
        results = {
            label: evaluate(flavor, quadrature, n_b)
            for label, n_b in (("resolved", 201), ("doubled_b", 401))
        }
        differences = []
        for part in ("proton", "neutron", "total"):
            for name in ("f1", "g1", "h1"):
                a = results["resolved"][part][name]
                b = results["doubled_b"][part][name]
                differences.append(abs(a - b) / max(abs(b), 1e-10))
        rows.append({
            "flavor": flavor,
            "values": results,
            "maximum_mixed_relative_b_grid_change": max(differences),
            "proton_neutron_resolved": any(
                abs(
                    results["doubled_b"]["proton"][name]
                    - results["doubled_b"]["neutron"][name]
                ) > 1e-10
                for name in ("f1", "g1", "h1")
            ),
        })

    maximum = max(
        row["maximum_mixed_relative_b_grid_change"] for row in rows
    )
    b_passed = maximum < 5e-3 and all(
        row["proton_neutron_resolved"] for row in rows
    )

    lf_results = {}
    for label, orders in (
        ("medium", (16, 12, 8)),
        ("production", (24, 16, 12)),
    ):
        q = make_quadrature(orders)
        lf_results[label] = {
            str(flavor): evaluate(flavor, q, 201)
            for flavor in (2, 1, -2, -1)
        }
    lf_differences = []
    for flavor in (2, 1, -2, -1):
        for part in ("proton", "neutron", "total"):
            for name in ("f1", "g1", "h1"):
                medium = lf_results["medium"][str(flavor)][part][name]
                production = lf_results["production"][str(flavor)][part][name]
                lf_differences.append(
                    abs(medium - production) / max(abs(production), 1e-10)
                )
    lf_maximum = max(lf_differences)
    lf_passed = lf_maximum < 2e-2

    six_wave_results = {}
    for wave_name in WAVE_FUNCTION_CHOICES:
        selected = select_momentum_wave_function(wave_name)
        q = build_off_forward_spin_quadrature(
            radial=selected.radial,
            nucleon_mass=M_N_GEV / HBARC_GEV_FM,
            k_max=10.0,
            n_k=24,
            n_cos_theta=16,
            n_phi=12,
            delta_x=0.0,
            delta_y=0.0,
        )
        six_wave_results[wave_name] = {
            str(flavor): evaluate(flavor, q, 201)
            for flavor in (2, 1, -2, -1)
        }
    six_wave_finite = all(
        np.isfinite(value)
        for wave_values in six_wave_results.values()
        for flavor_values in wave_values.values()
        for part_values in flavor_values.values()
        for value in part_values.values()
    )
    passed = b_passed and lf_passed and six_wave_finite
    report = {
        "status": "pass" if passed else "fail",
        "scope": {
            "wave_function": "AV18",
            "x_D": 0.05,
            "x_N_reference": 0.1,
            "Q_GeV": 5.0,
            "k_T_GeV": 0.3,
            "flavors": [2, 1, -2, -1],
            "lf_quadrature": [8, 6, 6],
            "b_grids": {
                "resolved": [201, 12.0],
                "doubled": [401, 12.0],
            },
        },
        "maximum_mixed_relative_b_grid_change": maximum,
        "b_grid_acceptance": 5e-3,
        "rows": rows,
        "lf_convergence": {
            "orders": {
                "medium": [16, 12, 8],
                "production": [24, 16, 12],
            },
            "values": lf_results,
            "maximum_mixed_relative_change": lf_maximum,
            "acceptance": 2e-2,
            "status": "pass" if lf_passed else "fail",
        },
        "six_wave_production": {
            "status": "pass" if six_wave_finite else "fail",
            "values": six_wave_results,
            "requirement": "finite flavor- and nucleon-resolved projections",
        },
        "limitations": (
            "Representative x,Q,k connection gate; multi-kinematic evolved "
            "output production and full uncertainty propagation remain required. "
            "This gate isolates rank-zero evolution; rank-one has a separate "
            "tensor-transform validation."
        ),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        "status": report["status"],
        "maximum_mixed_relative_b_grid_change": maximum,
        "maximum_mixed_relative_lf_change": lf_maximum,
    }, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
