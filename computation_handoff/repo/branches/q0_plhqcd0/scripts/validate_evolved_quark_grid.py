#!/usr/bin/env python3
"""Compare the portable evolved quark grid to direct rank-aware transforms."""

from __future__ import annotations

import json
from pathlib import Path

from deuteron_wigner.evolved_quark_grid import EvolvedQuarkGridModel
from deuteron_wigner.evolved_quark_model import EvolvedRankZeroQuarkModel
from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.nucleon_inputs import (
    NucleonInputConfiguration,
    build_nucleon_quark_models,
)
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.quark_tmd_matching import MatchedRankZeroQuarkTMD
from deuteron_wigner.tmd_evolution import (
    EvolvedMatchedRankZeroQuarkTMD,
    OneLoopQuarkCSSEvolution,
)
from deuteron_wigner.transversity import JAMDiFFTransversityGrid
from deuteron_wigner.worm_gear_inputs import Yang2024G1TInput

GRID = Path("data/processed/evolved_quark_tmd_Q5.npz")
OUTPUT = Path("data/processed/evolved_quark_tmd_Q5.validation.json")


def main() -> None:
    pdf = LHAPDFProvider("CT18NNLO", 0)
    polarized = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
    transversity = JAMDiFFTransversityGrid(
        "data/processed/jamdiff_wlqcd_transversity.csv"
    )
    configs = {
        "central": NucleonInputConfiguration.flavor_resolved_baseline(),
        "positive": (
            NucleonInputConfiguration.flavor_resolved_baseline()
            .with_pretzelosity_fraction(0.25)
        ),
    }
    rows = []
    yang_g1t = Yang2024G1TInput().fitted_input()
    for scenario, config in configs.items():
        proton, neutron = build_nucleon_quark_models(
            pdf, polarized, config, transversity_input=transversity,
            g1t_input=yang_g1t,
        )
        for nucleon_name, model in (("proton", proton), ("neutron", neutron)):
            direct = EvolvedRankZeroQuarkModel(
                model,
                EvolvedMatchedRankZeroQuarkTMD(
                    MatchedRankZeroQuarkTMD(model),
                    OneLoopQuarkCSSEvolution(pdf.alpha_s),
                ),
                b_max_gev_inverse=12.0,
                n_b=401,
                n_rank_one_scales=25,
            )
            grid = EvolvedQuarkGridModel(
                model, GRID, nucleon_name, scenario
            )
            for flavor in (2, 1, -2, -1):
                for x in (0.035, 0.12, 0.37):
                    for k in (0.07, 0.33, 0.83, 1.8):
                        common = dict(
                            flavor=flavor, x=x, k_x_gev=k, k_y_gev=0.0,
                            scale_gev=5.0, gauge_link=GaugeLink("+", "+"),
                        )
                        expected = direct.tmd_values(**common)
                        actual = grid.tmd_values(**common)
                        names = (
                            ("h1Tperp",)
                            if scenario == "positive"
                            else ("f1", "g1", "h1", "g1T", "h1Lperp")
                        )
                        for name in names:
                            absolute = abs(actual[name] - expected[name])
                            relative = absolute / max(abs(expected[name]), 1e-8)
                            rows.append({
                                "scenario": scenario,
                                "nucleon": nucleon_name,
                                "flavor": flavor,
                                "x": x,
                                "k_GeV": k,
                                "component": name,
                                "direct": expected[name],
                                "grid": actual[name],
                                "absolute": absolute,
                                "mixed_relative": relative,
                            })
    maximum = max(row["mixed_relative"] for row in rows)
    failed = [
        row for row in rows
        if row["mixed_relative"] >= 0.02 and row["absolute"] >= 2e-6
    ]
    report = {
        "status": "pass" if not failed else "fail",
        "sample_count": len(rows),
        "maximum_mixed_relative": maximum,
        "acceptance": "relative < 2% or absolute < 2e-6 GeV^-2",
        "failed_count": len(failed),
        "worst_points": sorted(
            rows, key=lambda row: row["mixed_relative"], reverse=True
        )[:12],
    }
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
