#!/usr/bin/env python3
"""Generate a rank-aware fixed-Q evolved quark momentum grid."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.integrate import simpson
from scipy.special import j0, j1, jv

from deuteron_wigner.nucleon_inputs import build_nucleon_quark_models
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.quark_tmd_matching import MatchedRankZeroQuarkTMD
from deuteron_wigner.tmd_evolution import OneLoopQuarkCSSEvolution
from deuteron_wigner.transversity import JAMDiFFTransversityGrid
from deuteron_wigner.worm_gear_inputs import Yang2024G1TInput

OUTPUT = Path("data/processed/evolved_quark_tmd_Q5.npz")
METADATA = OUTPUT.with_suffix(".metadata.json")
FLAVORS = (2, 1, -2, -1)
COMPONENTS = ("f1", "g1", "h1", "g1T", "h1Lperp", "h1Tperp")
SCENARIOS = ("negative", "central", "positive")
FRACTIONS = (-0.25, 0.0, 0.25)
MASS = 0.93891897


def reverse_integral(x: np.ndarray, integrand: np.ndarray) -> np.ndarray:
    intervals = 0.5 * np.diff(x) * (integrand[:-1] + integrand[1:])
    return np.concatenate((np.cumsum(intervals[::-1])[::-1], (0.0,)))


def main() -> None:
    scale = 5.0
    x = np.unique(np.concatenate((
        np.geomspace(1e-3, 0.1, 81),
        np.linspace(0.1, 0.9, 161),
        np.linspace(0.9, 0.99, 31),
        np.asarray((0.995, 0.999, 1.0)),
    )))
    k = np.unique(np.concatenate((
        np.linspace(0.0, 0.5, 51),
        np.linspace(0.5, 1.5, 51),
        np.linspace(1.5, 3.0, 61),
    )))
    b = np.linspace(0.0, 12.0, 401)
    mu = np.geomspace(np.sqrt(2.0), scale, 25)

    pdf = LHAPDFProvider("CT18NNLO", 0)
    polarized = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
    transversity = JAMDiFFTransversityGrid(
        "data/processed/jamdiff_wlqcd_transversity.csv"
    )
    yang_g1t = Yang2024G1TInput().fitted_input()
    proton, neutron = build_nucleon_quark_models(
        pdf, polarized, transversity_input=transversity,
        g1t_input=yang_g1t,
    )
    evolution = OneLoopQuarkCSSEvolution(pdf.alpha_s)
    # Common canonical scales and Sudakov do not depend on flavor or nucleon.
    boundary_for_geometry = MatchedRankZeroQuarkTMD(proton)
    b_star = np.asarray([boundary_for_geometry.b_star(float(v)) for v in b])
    initial = np.asarray([
        evolution.canonical_scale(float(v), scale) for v in b_star
    ])
    sudakov = np.asarray([
        evolution.factor(float(bb), float(bs), scale)
        for bb, bs in zip(b, b_star)
    ])

    values = np.zeros((
        2, len(FLAVORS), len(COMPONENTS), len(SCENARIOS), len(x), len(k)
    ))
    for nucleon_index, model in enumerate((proton, neutron)):
        for flavor_index, flavor in enumerate(FLAVORS):
            widths = {
                name: model.components[name].width(flavor)
                for name in COMPONENTS
            }
            collinear = {
                name: np.zeros((len(mu), len(x))) for name in ("f1", "g1", "h1")
            }
            for q_index, q in enumerate(mu):
                for name in collinear:
                    component = model.components[name]
                    collinear[name][q_index, :-1] = [
                        component.value(flavor, float(xx), float(q))
                        for xx in x[:-1]
                    ]
                    collinear[name][q_index, -1] = 0.0

            fitted_g1t = np.zeros_like(collinear["g1"])
            ww_h = np.zeros_like(collinear["h1"])
            for q_index in range(len(mu)):
                fitted_g1t[q_index, :-1] = [
                    model.components["g1T"].value(
                        flavor, float(xx), float(mu[q_index])
                    )
                    for xx in x[:-1]
                ]
                ww_h[q_index] = (
                    -2.0 * MASS**2 * x**2
                    * reverse_integral(x, collinear["h1"][q_index] / x**2)
                    / widths["h1Lperp"]
                )
            sources = {
                "f1": collinear["f1"],
                "g1": collinear["g1"],
                "h1": collinear["h1"],
                "g1T": fitted_g1t,
                "h1Lperp": ww_h,
            }

            def at_initial(source):
                result = np.empty((len(x), len(b)))
                for x_index in range(len(x)):
                    result[x_index] = np.interp(
                        np.log(initial), np.log(mu), source[:, x_index]
                    )
                return result

            for component_index, name in enumerate(COMPONENTS[:-1]):
                amplitude = at_initial(sources[name])
                width = widths[name]
                intrinsic = np.exp(-width * b**2 / 4.0)
                if name in ("f1", "g1", "h1"):
                    coordinate = amplitude * intrinsic * sudakov
                    transformed = np.asarray([
                        simpson(
                            coordinate * (b * j0(b * kk))[None, :],
                            x=b, axis=1,
                        ) / (2.0 * np.pi)
                        for kk in k
                    ]).T
                else:
                    radial = (
                        amplitude * width * b * intrinsic * sudakov
                        / (2.0 * MASS)
                    )
                    transformed_columns = []
                    for kk in k:
                        if kk == 0.0:
                            transformed_columns.append(
                                MASS * simpson(radial * b**2, x=b, axis=1)
                                / (4.0 * np.pi)
                            )
                        else:
                            transformed_columns.append(
                                MASS * simpson(
                                    radial * (b * j1(b * kk))[None, :],
                                    x=b, axis=1,
                                ) / (2.0 * np.pi * kk)
                            )
                    transformed = np.asarray(transformed_columns).T
                values[
                    nucleon_index, flavor_index, component_index, :, :, :
                ] = transformed[None, :, :]

            f_initial = at_initial(collinear["f1"])
            g_initial = at_initial(collinear["g1"])
            width = widths["h1Tperp"]
            intrinsic = np.exp(-width * b**2 / 4.0)
            for scenario_index, fraction in enumerate(FRACTIONS):
                amplitude = (
                    fraction * MASS**2
                    * np.maximum(0.0, f_initial - g_initial) / width
                )
                radial = (
                    amplitude * width**2 * b**2 * intrinsic * sudakov
                    / (4.0 * MASS**2)
                )
                columns = []
                for kk in k:
                    if kk == 0.0:
                        columns.append(
                            MASS**2 * simpson(radial * b**3, x=b, axis=1)
                            / (16.0 * np.pi)
                        )
                    else:
                        columns.append(
                            MASS**2 * simpson(
                                radial * (b * jv(2, b * kk))[None, :],
                                x=b, axis=1,
                            ) / (2.0 * np.pi * kk**2)
                        )
                values[
                    nucleon_index, flavor_index, -1, scenario_index
                ] = np.asarray(columns).T

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        OUTPUT, x=x, k=k, flavors=np.asarray(FLAVORS),
        components=np.asarray(COMPONENTS), scenarios=np.asarray(SCENARIOS),
        values=values, scale_gev=np.asarray(scale), b=b, mu=mu,
    )
    metadata = {
        "status": "generated",
        "output": str(OUTPUT),
        "shape": list(values.shape),
        "Q_GeV": scale,
        "x_nodes": len(x), "k_nodes": len(k), "b_nodes": len(b),
        "canonical_scale_nodes": len(mu),
        "nucleons": ["proton", "neutron"],
        "flavors": list(FLAVORS), "components": list(COMPONENTS),
        "pretzelosity_scenarios": dict(zip(SCENARIOS, FRACTIONS)),
        "g1T_boundary": {
            "source": "Yang et al. arXiv:2403.12795 Eq. (46), Table IV",
            "flavor_scope": "u,d fitted; ubar,dbar zero boundary",
            "evolution": "project rank-one J1/CSS common-kernel model",
            "uncertainty": "published parameter intervals but no released covariance/replicas",
        },
        "h1Lperp_boundary": "Wandzura-Wilczek central with separate breaking uncertainty",
        "rank_transforms": {
            "rank_zero": "J0", "rank_one": "J1", "rank_two": "J2"
        },
        "limitations": (
            "fixed-Q central fitted inputs; interpolation and direct-boundary "
            "validation required before production parent use"
        ),
    }
    METADATA.write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
