#!/usr/bin/env python3
"""Plot finite-kT spin-1 quark h1TT versus x_N and Q^2."""

from __future__ import annotations

from pathlib import Path
from dataclasses import dataclass, field

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import pandas as pd

from deuteron_wigner.axial_tensor_todd import (
    EikonalAxialTensorModel,
    Spin1QuarkNuclearWilsonLine,
)
from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.gtmd_convolution import build_off_forward_spin_quadrature
from deuteron_wigner.nucleon_inputs import build_nucleon_quark_models
from deuteron_wigner.nucleon_quark_correlator import (
    NUCLEON_QUARK_TMD_NAMES,
    compose_spin_half_quark_correlator,
)
from deuteron_wigner.parent_quark_tmd import (
    convolve_spin1_quark_correlator,
)
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.quark_correlator import (
    Spin1QuarkCorrelator,
    project_spin1_quark_correlator,
)
from deuteron_wigner.transversity import JAMDiFFTransversityGrid
from deuteron_wigner.wavefunctions.selection import (
    WAVE_FUNCTION_CHOICES,
    select_momentum_wave_function,
)

HBARC = 0.1973269804
M_N = 0.93891897
M_D = 1.87561294257
K_T = 0.30
AXIAL_TENSOR = EikonalAxialTensorModel()
FLAVORS = ((2, "u"), (1, "d"), (-2, "ubar"), (-1, "dbar"))
OUT = Path("outputs/figures/quark_h1tt")
PDF = Path("output/pdf")


@dataclass
class TransverseOnlyModel:
    """Exact restriction to nucleon structures that can project onto h1TT."""

    source: object
    _collinear_cache: dict = field(default_factory=dict)

    def correlator(
        self, *, flavor, x, k_x_gev, k_y_gev, delta_x_gev, delta_y_gev,
        scale_gev, gauge_link,
    ):
        k2 = k_x_gev**2 + k_y_gev**2
        values = {name: 0.0 for name in NUCLEON_QUARK_TMD_NAMES}
        # Both h1 and rank-two nucleon pretzelosity feed the nuclear TT
        # transverse projection after Fermi-motion/OAM convolution.
        for name in ("h1", "h1Tperp"):
            component = self.source.components[name]
            width = component.width(flavor)
            key = (name, flavor, float(scale_gev))
            if key not in self._collinear_cache:
                x_nodes = np.unique(np.concatenate((
                    np.geomspace(1.0e-3, 0.1, 9),
                    np.linspace(0.1, 1.0, 17),
                )))
                h_nodes = np.asarray([
                    component.value(flavor, float(xx), scale_gev)
                    for xx in x_nodes
                ])
                self._collinear_cache[key] = (x_nodes, h_nodes)
            x_nodes, h_nodes = self._collinear_cache[key]
            values[name] = float(
                np.interp(x, x_nodes, h_nodes)
                * np.exp(-k2 / width) / (np.pi * width)
            )
        return compose_spin_half_quark_correlator(
            values=values, k_x_gev=k_x_gev, k_y_gev=k_y_gev,
            delta_x_gev=delta_x_gev, delta_y_gev=delta_y_gev,
            nucleon_mass_gev=self.source.nucleon_mass_gev,
            transfer_slope_gev2=self.source.transfer_slope_gev2,
        )


def scaled(value: Spin1QuarkCorrelator, factor: float) -> Spin1QuarkCorrelator:
    return Spin1QuarkCorrelator(
        factor * value.vector, factor * value.axial, factor * value.transverse
    )


def evaluate(models, quadrature, *, x_n: float, q_gev: float, flavor: int) -> float:
    # The nuclear convolution uses x_D=x_N/2. The factor 1/4 is the same
    # x_N=2x_D Jacobian/per-nucleon convention as the canonical exporter.
    result = convolve_spin1_quark_correlator(
        x=x_n / 2.0, k_x=K_T / HBARC, k_y=0.0,
        scale=q_gev, flavor=flavor,
        proton=models[0], neutron=models[1], quadrature=quadrature,
        gauge_link=GaugeLink("+", "+"),
        momentum_unit_to_gev=HBARC,
    )
    total = scaled(result.total, 0.25)
    phase = Spin1QuarkNuclearWilsonLine(
        AXIAL_TENSOR, flavor, GaugeLink("+", "+")
    )
    total = phase.apply_unitary(
        total,
        phase.unitary(
            (K_T, 0.0), models[0].source.components["g1"].width(flavor)
        ),
    )
    return float(
        project_spin1_quark_correlator(total, (K_T, 0.0), M_D)["h1TT"]
    )


def main() -> None:
    pdf = LHAPDFProvider("CT18NNLO", 0)
    helicity = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
    transversity = JAMDiFFTransversityGrid(
        "data/processed/jamdiff_wlqcd_transversity.csv"
    )
    full_models = build_nucleon_quark_models(
        pdf, helicity, transversity_input=transversity
    )
    models = tuple(TransverseOnlyModel(model) for model in full_models)
    wave = select_momentum_wave_function("av18")
    quadratures = {"av18": build_off_forward_spin_quadrature(
        radial=wave.radial, nucleon_mass=M_N / HBARC, k_max=10.0,
        n_k=12, n_cos_theta=10, n_phi=8,
        delta_x=0.0, delta_y=0.0,
    )}

    x_grid = np.geomspace(0.01, 0.75, 33)
    q2_grid = np.geomspace(2.0, 100.0, 25)
    rows = []
    for scan, nodes in (("x", x_grid), ("Q2", q2_grid)):
        for node in nodes:
            x_n = float(node if scan == "x" else 0.1)
            q2 = float(25.0 if scan == "x" else node)
            for flavor, label in FLAVORS:
                members = {
                    wave: evaluate(
                        models, quadrature, x_n=x_n,
                        q_gev=np.sqrt(q2), flavor=flavor,
                    )
                    for wave, quadrature in quadratures.items()
                }
                values = np.asarray(list(members.values()))
                rows.append({
                    "scan": scan, "x_N": x_n, "Q2_GeV2": q2,
                    "flavor": flavor, "flavor_label": label,
                    "h1TT_central": members["av18"],
                    "h1TT_wave_low": float(values.min()),
                    "h1TT_wave_high": float(values.max()),
                    "central_wave_function": "av18",
                    "band_semantics": "AV18 central only",
                    "k_T_GeV": K_T,
                    "observable": "finite-kT h1TT in intrinsic LF parent",
                })
    frame = pd.DataFrame(rows)
    OUT.mkdir(parents=True, exist_ok=True)
    PDF.mkdir(parents=True, exist_ok=True)
    frame.to_csv(OUT / "quark_h1TT_x_q2.csv", index=False)

    colors = {2: "#174A7E", 1: "#B44B3A", -2: "#5B8E3E", -1: "#8A5AA5"}
    labels = {2: r"$u$", 1: r"$d$", -2: r"$\bar u$", -1: r"$\bar d$"}
    specs = (
        ("x", "x_N", r"$x_N$", r"$Q^2=25\ {\rm GeV}^2$",
         PDF / "quark_h1TT_vs_x.pdf"),
        ("Q2", "Q2_GeV2", r"$Q^2\ [{\rm GeV}^2]$", r"$x_N=0.1$",
         PDF / "quark_h1TT_vs_Q2.pdf"),
    )
    for scan, axis_name, xlabel, fixed, destination in specs:
        fig, ax = plt.subplots(figsize=(7.2, 4.8))
        selected = frame.loc[frame.scan.eq(scan)]
        for flavor, _ in FLAVORS:
            part = selected.loc[selected.flavor.eq(flavor)].sort_values(axis_name)
            ax.plot(
                part[axis_name], part.h1TT_central, color=colors[flavor],
                linewidth=2.0, label=labels[flavor],
            )
        ax.axhline(0, color="#777777", linewidth=0.7)
        if scan == "Q2":
            ax.set_xscale("log")
        else:
            ax.set_xscale("log")
        ax.set_xlabel(xlabel)
        ax.set_ylabel(r"$h_{1TT}(x_N,k_T;Q^2)\ [{\rm GeV}^{-2}]$")
        ax.set_title(r"Canonical spin-1 quark $h_{1TT}$  |  " + fixed)
        ax.grid(True, alpha=0.18, linewidth=0.6)
        ax.legend(frameon=False, ncol=4)
        fig.text(
            0.5, 0.015,
            rf"$k_T={K_T:.2f}$ GeV; AV18 intrinsic LF parent; "
            r"input-scale DGLAP dependence.",
            ha="center", fontsize=8,
        )
        fig.tight_layout(rect=(0.02, 0.05, 0.98, 0.98))
        with PdfPages(destination) as stream:
            stream.savefig(fig)
        fig.savefig(destination.with_suffix(".png"), dpi=180)
        plt.close(fig)
    print(frame.groupby("scan").size().to_dict())


if __name__ == "__main__":
    main()
