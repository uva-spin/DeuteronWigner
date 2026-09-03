#!/usr/bin/env python3
"""Audit signed nonperturbative pretzelosity scenarios against positivity."""

from __future__ import annotations

import json
from pathlib import Path

from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.nucleon_inputs import (
    NucleonInputConfiguration,
    build_nucleon_quark_models,
)
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.transversity import JAMDiFFTransversityGrid

OUTPUT = Path("outputs/parent_tmds/pretzelosity_scenarios.validation.json")


def main() -> None:
    pdf = LHAPDFProvider("CT18NNLO", 0)
    polarized = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
    transversity = JAMDiFFTransversityGrid(
        "data/processed/jamdiff_wlqcd_transversity.csv"
    )
    rows = []
    for fraction in (-0.25, 0.0, 0.25):
        config = (
            NucleonInputConfiguration.flavor_resolved_baseline()
            .with_pretzelosity_fraction(fraction)
        )
        proton, neutron = build_nucleon_quark_models(
            pdf, polarized, config, transversity_input=transversity
        )
        minimum = float("inf")
        minimum_nonzero = float("inf")
        worst = None
        worst_nonzero = None
        for nucleon_name, model in (("proton", proton), ("neutron", neutron)):
            for flavor in (2, 1, -2, -1):
                for x in (0.03, 0.1, 0.3, 0.6):
                    for k_x, k_y in (
                        (0.0, 0.0), (0.2, 0.0), (0.5, 0.2), (0.9, -0.3)
                    ):
                        correlator = model.correlator(
                            flavor=flavor,
                            x=x,
                            k_x_gev=k_x,
                            k_y_gev=k_y,
                            delta_x_gev=0.0,
                            delta_y_gev=0.0,
                            scale_gev=5.0,
                            gauge_link=GaugeLink("+", "+"),
                        )
                        eigenvalue = correlator.minimum_positivity_eigenvalue()
                        if eigenvalue < minimum:
                            minimum = eigenvalue
                            worst = {
                                "nucleon": nucleon_name,
                                "flavor": flavor,
                                "x": x,
                                "k_x_GeV": k_x,
                                "k_y_GeV": k_y,
                            }
                        if k_x != 0.0 or k_y != 0.0:
                            if eigenvalue < minimum_nonzero:
                                minimum_nonzero = eigenvalue
                                worst_nonzero = {
                                    "nucleon": nucleon_name,
                                    "flavor": flavor,
                                    "x": x,
                                    "k_x_GeV": k_x,
                                    "k_y_GeV": k_y,
                                }
        rows.append({
            "fraction": fraction,
            "minimum_joint_density_eigenvalue": minimum,
            "worst_point": worst,
            "minimum_nonzero_k_eigenvalue": minimum_nonzero,
            "worst_nonzero_k_point": worst_nonzero,
            "status": (
                "pass"
                if minimum >= -1e-12 and minimum_nonzero >= -1e-12
                else "fail"
            ),
        })
    passed = all(row["status"] == "pass" for row in rows)
    report = {
        "status": "pass" if passed else "fail",
        "scenarios": rows,
        "bound": "|h1Tperp^(1)| <= (f1-g1)/2",
        "interpretation": (
            "signed large-b bound-state sensitivities; zero is the perturbative "
            "small-b central and none is a fitted confidence interval"
        ),
        "source": "arXiv:1808.10560",
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
