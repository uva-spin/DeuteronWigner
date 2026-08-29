#!/usr/bin/env python3
"""Export correlated quark/gluon Wilson-channel members for WP12."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from deuteron_wigner.axial_tensor_todd import (
    EikonalAxialTensorModel,
    EikonalKernelParameters,
    Spin1QuarkNuclearWilsonLine,
)
from deuteron_wigner.gluon_lfwf_todd import (
    GluonWilsonLineKernel,
    Spin1NuclearWilsonLine,
)
from deuteron_wigner.gluon_todd import GluonColorStructure
from deuteron_wigner.gtmd import GaugeLink


OUT = Path("outputs/parent_tmds/wp12_wilson_channel_members.csv")
K = np.linspace(0.0, 1.2, 31)
X = (0.02, 0.05, 0.10, 0.20, 0.40)


def quark_models():
    kernels = {
        "soft": EikonalKernelParameters(
            label="wp12_soft", alpha_s=0.24, screening_mass_gev=0.45,
            dipole_scale_gev=0.95, n_q=40, n_phi=48,
        ),
        "central": EikonalKernelParameters(
            label="wp12_central", alpha_s=0.30, screening_mass_gev=0.36,
            dipole_scale_gev=1.10, n_q=40, n_phi=48,
        ),
        "strong": EikonalKernelParameters(
            label="wp12_strong", alpha_s=0.36, screening_mass_gev=0.28,
            dipole_scale_gev=1.25, n_q=40, n_phi=48,
        ),
    }
    return {
        name: EikonalAxialTensorModel(
            kernel=kernel, d_state_probability=0.0576,
            sd_radial_coherence=0.3898,
        )
        for name, kernel in kernels.items()
    }


def gluon_kernels():
    return {
        "soft": GluonWilsonLineKernel(
            alpha_s=0.24, screening_mass_gev=0.45,
            remnant_scale_gev=0.75, n_q=40, n_phi=48,
        ),
        "central": GluonWilsonLineKernel(
            alpha_s=0.30, screening_mass_gev=0.36,
            remnant_scale_gev=0.90, n_q=40, n_phi=48,
        ),
        "strong": GluonWilsonLineKernel(
            alpha_s=0.36, screening_mass_gev=0.28,
            remnant_scale_gev=1.05, n_q=40, n_phi=48,
        ),
    }


def main() -> None:
    rows = []
    for member, model in quark_models().items():
        for flavor in (2, 1, -2, -1):
            for link, label in (
                (GaugeLink("+", "+"), "[+,+]"),
                (GaugeLink("-", "-"), "[-,-]"),
            ):
                phase = Spin1QuarkNuclearWilsonLine(model, flavor, link)
                for x_n in X:
                  for k in K:
                    for channel, value in phase.channel_phases(
                        float(k), 0.30
                    ).items():
                        rows.append({
                            "sector": "quark" if flavor > 0 else "antiquark",
                            "flavor": flavor, "color_structure": "",
                            "gauge_link": label, "member": member,
                            "correlation_group": "quark_wilson_kernel",
                            "channel": channel, "k_T_GeV": k,
                            "x_N": x_n, "Q_GeV": 5.0,
                            "phase": value, "central": int(member == "central"),
                        })
    for member, kernel in gluon_kernels().items():
        pairs = (
            (GluonColorStructure.F_TYPE, GaugeLink("+", "+"), "[+,+]"),
            (GluonColorStructure.F_TYPE, GaugeLink("-", "-"), "[-,-]"),
            (GluonColorStructure.D_TYPE, GaugeLink("+", "-"), "[+,-]"),
            (GluonColorStructure.D_TYPE, GaugeLink("-", "+"), "[-,+]"),
        )
        for color, link, label in pairs:
            phase = Spin1NuclearWilsonLine(
                color, link, 0.0576, 0.3898, kernel=kernel
            )
            for x_n in X:
              for k in K:
                for channel, value in phase.channel_phases(float(k)).items():
                    rows.append({
                        "sector": "gluon", "flavor": 21,
                        "color_structure": color.value,
                        "gauge_link": label, "member": member,
                        "correlation_group": "gluon_wilson_kernel",
                        "channel": channel, "k_T_GeV": k,
                        "x_N": x_n, "Q_GeV": 5.0,
                        "phase": value, "central": int(member == "central"),
                    })
    frame = pd.DataFrame(rows)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(OUT, index=False)
    print(f"{OUT}: {len(frame)} rows")


if __name__ == "__main__":
    main()
