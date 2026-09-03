#!/usr/bin/env python3
"""One-variable-at-a-time convergence audit for evolved AV18 LL gluon TMDs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import numpy as np

from deuteron_wigner.fourier import gluon_tmd_b_to_k
from deuteron_wigner.gluon_tmd_matching import (
    GluonTMDMatchingConfig,
    LargeBProfile,
    MatchedGluonTMD,
)
from deuteron_wigner.gtmd_convolution import (
    OffForwardSpinQuadrature,
    build_off_forward_spin_quadrature,
    convolve_gluon_gtmd_point,
    project_deuteron_gluon_u_ll,
)
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.tmd_evolution import (
    EvolvedMatchedGluonTMD,
    GluonCSSEvolutionConfig,
    NonperturbativeCSProfile,
    OneLoopGluonCSSEvolution,
)
from deuteron_wigner.tmd_models import InterpolatedSpinHalfGluonGTMD
from deuteron_wigner.wavefunctions.selection import select_momentum_wave_function

HBARC_GEV_FM = 0.1973269804
M_N_GEV = 0.93891897
M_D_GEV = 1.87561294257


def build_nucleon_model(scale: float) -> InterpolatedSpinHalfGluonGTMD:
    provider = LHAPDFProvider("CT18NNLO", 0)
    polarized = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
    boundary = MatchedGluonTMD(
        provider.gluon,
        provider.alpha_s,
        helicity_gluon_pdf=polarized.gluon,
        quark_singlet_pdf=provider.quark_singlet,
        config=GluonTMDMatchingConfig(profile=LargeBProfile.CENTRAL),
    )
    evolved = EvolvedMatchedGluonTMD(
        boundary,
        OneLoopGluonCSSEvolution(
            provider.alpha_s,
            GluonCSSEvolutionConfig(
                cs_profile=NonperturbativeCSProfile.CENTRAL
            ),
        ),
    )
    x_axis = np.concatenate((np.geomspace(0.05, 0.9, 15), (1.0,)))
    b_axis = np.linspace(0.0, 8.0, 201)
    k_axis = np.linspace(0.0, 4.5, 241)
    tables = {
        name: np.empty((len(x_axis), len(k_axis)))
        for name in ("f1", "g1", "h1perp")
    }
    for index, x in enumerate(x_axis):
        values = [evolved.values(float(x), float(b), scale) for b in b_axis]
        transformed = gluon_tmd_b_to_k(
            b_axis,
            np.asarray([value.f1 for value in values]),
            np.asarray([value.g1 for value in values]),
            np.asarray([value.h1perp for value in values]),
            k_axis,
            nucleon_mass=M_N_GEV,
        )
        tables["f1"][index] = transformed.f1.real
        tables["g1"][index] = transformed.g1.real
        tables["h1perp"][index] = transformed.h1perp.real
    return InterpolatedSpinHalfGluonGTMD(
        x_axis,
        k_axis,
        tables["f1"],
        tables["g1"],
        tables["h1perp"],
        nucleon_mass_GeV=M_N_GEV,
        momentum_unit_to_GeV=HBARC_GEV_FM,
    )


def evaluate(model, radial, spec, k_values, x_d, scale):
    n_k, n_cos, n_phi, k_max = spec
    quadrature = build_off_forward_spin_quadrature(
        radial=radial,
        nucleon_mass=M_N_GEV / HBARC_GEV_FM,
        k_max=k_max,
        delta_x=0.0,
        delta_y=0.0,
        n_k=n_k,
        n_cos_theta=n_cos,
        n_phi=n_phi,
    )
    results = []
    for k_gev in k_values:
        k_fm = k_gev / HBARC_GEV_FM
        correlator = convolve_gluon_gtmd_point(
            x=x_d,
            k_x=k_fm,
            k_y=0.0,
            scale=scale,
            proton_gtmd=model,
            neutron_gtmd=model,
            quadrature=quadrature,
        )
        unpolarized, ll = project_deuteron_gluon_u_ll(
            correlator, (k_fm, 0.0), M_D_GEV / HBARC_GEV_FM
        )
        results.append(
            {
                "f1g": 0.25 * unpolarized.trace,
                "h1perpg": 0.25 * unpolarized.linear,
                "f1LLg": 0.25 * ll.trace,
                "h1LLperpg": 0.25 * ll.linear,
            }
        )
    return results


def evaluate_segmented(
    model, radial, *, nodes_per_segment, cutoff, n_cos, n_phi,
    k_values, x_d, scale, segment_width=2.0,
):
    edges = np.arange(0.0, cutoff + 1.0e-12, segment_width)
    pieces = [
        build_off_forward_spin_quadrature(
            radial=radial,
            nucleon_mass=M_N_GEV / HBARC_GEV_FM,
            k_min=float(low),
            k_max=float(high),
            delta_x=0.0,
            delta_y=0.0,
            n_k=nodes_per_segment,
            n_cos_theta=n_cos,
            n_phi=n_phi,
        )
        for low, high in zip(edges[:-1], edges[1:])
    ]
    quadrature = OffForwardSpinQuadrature(
        y=np.concatenate([piece.y for piece in pieces]),
        p_x=np.concatenate([piece.p_x for piece in pieces]),
        p_y=np.concatenate([piece.p_y for piece in pieces]),
        weights=np.concatenate([piece.weights for piece in pieces]),
        delta_x=0.0,
        delta_y=0.0,
        spectral=np.concatenate([piece.spectral for piece in pieces]),
    )
    results = []
    for k_gev in k_values:
        k_fm = k_gev / HBARC_GEV_FM
        correlator = convolve_gluon_gtmd_point(
            x=x_d, k_x=k_fm, k_y=0.0, scale=scale,
            proton_gtmd=model, neutron_gtmd=model, quadrature=quadrature,
        )
        unpolarized, ll = project_deuteron_gluon_u_ll(
            correlator, (k_fm, 0.0), M_D_GEV / HBARC_GEV_FM
        )
        results.append({
            "f1g": 0.25 * unpolarized.trace,
            "h1perpg": 0.25 * unpolarized.linear,
            "f1LLg": 0.25 * ll.trace,
            "h1LLperpg": 0.25 * ll.linear,
        })
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--group",
        choices=(
            "n_k", "n_cos", "n_phi", "k_max",
            "segment_order", "segment_cutoff",
            "segment_width",
        ),
        required=True,
    )
    args = parser.parse_args()
    output = Path(
        f"outputs/stage0/convergence/gluon_tmd_evolved_tensor_{args.group}.csv"
    )
    scale = 5.0
    x_n = 0.1
    x_d = x_n / 2.0
    k_values = np.asarray((0.1, 1.5))
    model = build_nucleon_model(scale)
    wave = select_momentum_wave_function("av18")

    reference = (28, 20, 16, 10.0)
    grouped_cases = {
        "n_k": [
            (f"n_k_{value}", "n_k", (value, 20, 16, 10.0))
            for value in (12, 16, 20, 24)
        ],
        "n_cos": [
            (f"n_cos_{value}", "n_cos", (28, value, 16, 10.0))
            for value in (8, 12, 16)
        ],
        "n_phi": [
            (f"n_phi_{value}", "n_phi", (28, 20, value, 10.0))
            for value in (6, 8, 12)
        ],
        "k_max": [
            (f"k_max_{value:g}", "k_max", (28, 20, 16, value))
            for value in (6.0, 8.0, 12.0)
        ],
        "segment_order": [
            (f"segment_order_{value}", "segment_order", (value, 12.0, 16, 12))
            for value in (10, 12)
        ],
        "segment_cutoff": [
            (f"segment_cutoff_{value:g}", "segment_cutoff", (8, value, 16, 12))
            for value in (6.0, 8.0, 10.0)
        ],
        "segment_width": [
            (f"segment_width_{value:g}", "segment_width", (6, 12.0, 12, 8, value))
            for value in (0.5,)
        ],
    }
    cases = [("reference", "reference", reference), *grouped_cases[args.group]]
    segmented = args.group.startswith("segment_")
    if segmented:
        if args.group == "segment_width":
            reference_values = evaluate_segmented(
                model, wave.radial, nodes_per_segment=6, cutoff=12.0,
                n_cos=12, n_phi=8, segment_width=0.25,
                k_values=k_values, x_d=x_d, scale=scale,
            )
        else:
            reference_values = evaluate_segmented(
                model, wave.radial, nodes_per_segment=8, cutoff=12.0,
                n_cos=16, n_phi=12, k_values=k_values, x_d=x_d, scale=scale,
            )
    else:
        reference_values = evaluate(
            model, wave.radial, reference, k_values, x_d, scale
        )
    rows = []
    summaries: dict[str, dict[str, float]] = {}
    for label, varied_parameter, spec in cases:
        if label == "reference":
            values = reference_values
        elif segmented:
            values = evaluate_segmented(
                model, wave.radial,
                nodes_per_segment=int(spec[0]), cutoff=float(spec[1]),
                n_cos=int(spec[2]), n_phi=int(spec[3]),
                segment_width=float(spec[4]) if len(spec) > 4 else 2.0,
                k_values=k_values, x_d=x_d, scale=scale,
            )
        else:
            values = evaluate(model, wave.radial, spec, k_values, x_d, scale)
        summaries[label] = {}
        for index, k_gev in enumerate(k_values):
            row = {
                "case": label,
                "varied_parameter": varied_parameter,
                "n_k": spec[0],
                "n_cos": spec[2] if segmented else spec[1],
                "n_phi": spec[3] if segmented else spec[2],
                "k_max_fm_inverse": spec[1] if segmented else spec[3],
                "segment_width_fm_inverse": (
                    spec[4] if segmented and len(spec) > 4 else
                    (2.0 if segmented else np.nan)
                ),
                "k_GeV": k_gev,
            }
            for observable in ("f1g", "h1perpg", "f1LLg", "h1LLperpg"):
                value = values[index][observable]
                target = reference_values[index][observable]
                relative = (
                    (value - target) / target if target != 0.0 else np.nan
                )
                row[observable] = value
                row[f"{observable}_relative_to_reference"] = relative
                summaries[label][observable] = max(
                    summaries[label].get(observable, 0.0), abs(relative)
                )
            rows.append(row)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    output.with_suffix(".summary.json").write_text(
        json.dumps(
            {
                "reference": {
                    "n_k": reference[0],
                    "n_cos": reference[1],
                    "n_phi": reference[2],
                    "k_max_fm_inverse": reference[3],
                },
                "x_N": x_n,
                "Q_GeV": scale,
                "k_GeV": list(map(float, k_values)),
                "varied_parameter": args.group,
                "maximum_absolute_relative_difference": summaries,
                "production_ready": False,
            },
            indent=2,
        )
        + "\n"
    )
    print(f"Wrote {len(rows)} rows to {output}")


if __name__ == "__main__":
    main()
