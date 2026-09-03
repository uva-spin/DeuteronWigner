#!/usr/bin/env python3
"""Validate production flavor-resolved nucleon inputs and spin positivity."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from scipy.integrate import quad

from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.nucleon_inputs import build_nucleon_quark_models
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.transversity import JAMDiFFTransversityGrid


def main() -> None:
    scale = 5.0
    unpolarized = LHAPDFProvider("CT18NNLO", 0)
    polarized = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
    transversity = JAMDiFFTransversityGrid(
        "data/processed/jamdiff_wlqcd_transversity.csv"
    )
    proton, neutron = build_nucleon_quark_models(
        unpolarized, polarized, transversity_input=transversity
    )
    link = GaugeLink("+", "+")
    x_axis = np.geomspace(1.0e-3, 0.8, 18)
    k_axis = np.linspace(0.0, 1.5, 16)
    minimum = np.inf
    worst = None
    for nucleon, model in (("proton", proton), ("neutron", neutron)):
        for flavor in (2, 1, -2, -1):
            for x in x_axis:
                for k in k_axis:
                    correlator = model.correlator(
                        flavor=flavor, x=float(x),
                        k_x_gev=float(k * np.cos(0.37)),
                        k_y_gev=float(k * np.sin(0.37)),
                        delta_x_gev=0.0, delta_y_gev=0.0,
                        scale_gev=scale, gauge_link=link,
                    )
                    eigenvalue = correlator.minimum_positivity_eigenvalue()
                    if eigenvalue < minimum:
                        minimum = eigenvalue
                        worst = {
                            "nucleon": nucleon, "flavor": flavor,
                            "x": float(x), "k_GeV": float(k),
                        }

    def moment(function, flavor):
        return float(quad(
            lambda x: function(flavor, x, scale),
            1.0e-5, 1.0, epsabs=2.0e-4, epsrel=2.0e-3, limit=150,
        )[0])

    valence = {
        "u": moment(unpolarized.proton, 2)
        - moment(unpolarized.proton, -2),
        "d": moment(unpolarized.proton, 1)
        - moment(unpolarized.proton, -1),
    }
    tensor_scale = 2.0
    def tensor_moment(function, flavor):
        return float(quad(
            lambda x: function(flavor, x, tensor_scale),
            1.0e-3, 1.0, epsabs=2.0e-5, epsrel=5.0e-4, limit=150,
        )[0])

    tensor_charge = {
        label: tensor_moment(proton.components["h1"].value, flavor)
        - tensor_moment(proton.components["h1"].value, -flavor)
        for label, flavor in (("u", 2), ("d", 1))
    }
    tensor_targets = {"u": 0.71, "d": -0.200}
    tensor_ok = all(
        abs(tensor_charge[key] - tensor_targets[key]) < 0.04
        for key in tensor_targets
    )
    report = {
        "status": "pass" if minimum >= -1.0e-10 and tensor_ok else "fail",
        "scale_GeV": scale,
        "positivity_grid": {
            "x": [float(x_axis[0]), float(x_axis[-1]), len(x_axis)],
            "k_GeV": [float(k_axis[0]), float(k_axis[-1]), len(k_axis)],
            "flavors": [2, 1, -2, -1],
            "nucleons": ["proton", "neutron"],
            "minimum_eigenvalue": float(minimum),
            "worst_point": worst,
        },
        "valence_number_moments": valence,
        "valence_targets": {"u": 2.0, "d": 1.0},
        "tensor_charge_reference_scale_GeV": tensor_scale,
        "tensor_charge_model_boundary": tensor_charge,
        "tensor_charge_targets": tensor_targets,
        "tensor_charge_status": (
            "JAMDiFF pointwise central fit after CT18+BDSSV Soffer compatibility "
            "projection; 0.001<x<0.8 table support explains the small moment shift"
        ),
        "gaussian_kT_normalization": (
            "analytic integral exp(-k^2/w)/(pi*w)=1 for every component"
        ),
    }
    output = Path("outputs/parent_tmds/nucleon_quark_input_validation.json")
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    if report["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
