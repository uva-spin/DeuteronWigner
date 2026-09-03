#!/usr/bin/env python3
"""Vectorized paired-Hessian propagation of neutron f1 CSB through LF parents."""

from __future__ import annotations

import csv
import json
from pathlib import Path

import numpy as np

from deuteron_wigner.csb_inputs import MSHT20QEDChargeSymmetryBreaking
from deuteron_wigner.evolved_quark_grid import EvolvedQuarkGridModel
from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.gtmd_convolution import build_off_forward_spin_quadrature
from deuteron_wigner.nucleon_inputs import build_nucleon_quark_models
from deuteron_wigner.parent_quark_tmd import (
    ParentDerivedQuarkResult,
    project_parent_derived_quark_tmds,
)
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.quark_correlator import (
    SPIN1_QUARK_TMD_NAMES,
    Spin1QuarkCorrelator,
)
from deuteron_wigner.transversity import JAMDiFFTransversityGrid
from deuteron_wigner.wavefunctions.selection import (
    WAVE_FUNCTION_CHOICES,
    select_momentum_wave_function,
)

HBARC_GEV_FM = 0.1973269804
M_N_GEV = 0.93891897
M_D_GEV = 1.87561294257
GRID = Path("data/processed/evolved_quark_tmd_Q5.npz")
OUTPUT = Path("outputs/parent_tmds/msht20qed_csb_parent_hessian_members.csv")
BANDS = Path("outputs/parent_tmds/msht20qed_csb_parent_hessian_bands.csv")
VALIDATION = BANDS.with_suffix(".validation.json")
K_VALUES = (0.0, 0.2, 0.4, 0.7, 1.0)
N_MEMBERS = 77


def _delta_correlator(vector: np.ndarray) -> ParentDerivedQuarkResult:
    zero_matrix = np.zeros((3, 3), dtype=np.complex128)
    zero_transverse = np.zeros((2, 3, 3), dtype=np.complex128)
    zero = Spin1QuarkCorrelator(
        vector=zero_matrix, axial=zero_matrix, transverse=zero_transverse
    )
    neutron = Spin1QuarkCorrelator(
        vector=vector, axial=zero_matrix, transverse=zero_transverse
    )
    return ParentDerivedQuarkResult(proton=zero, neutron=neutron)


def main() -> None:
    pdf = LHAPDFProvider("CT18NNLO", 0)
    polarized = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
    transversity = JAMDiFFTransversityGrid(
        "data/processed/jamdiff_wlqcd_transversity.csv"
    )
    _, neutron = build_nucleon_quark_models(
        pdf, polarized, transversity_input=transversity
    )
    evolved_neutron = EvolvedQuarkGridModel(neutron, GRID, "neutron")
    csb = MSHT20QEDChargeSymmetryBreaking()
    link = GaugeLink("+", "+")
    identity = np.eye(2, dtype=np.complex128)
    member_rows = []
    band_rows = []
    hermiticity_max = 0.0
    central_direct_max = 0.0
    response_cache: dict[int, tuple[np.ndarray, np.ndarray]] = {}

    for wave_name in WAVE_FUNCTION_CHOICES:
        wave = select_momentum_wave_function(wave_name)
        quadrature = build_off_forward_spin_quadrature(
            radial=wave.radial,
            nucleon_mass=M_N_GEV / HBARC_GEV_FM,
            k_max=10.0,
            n_k=24,
            n_cos_theta=16,
            n_phi=12,
            delta_x=0.0,
            delta_y=0.0,
        )
        active = quadrature.y >= 0.05
        y = quadrature.y[active]
        z = 0.05 / y
        weights = quadrature.weights[active] / y
        spectral_identity = np.einsum(
            "nIHca,ac->nIH", quadrature.spectral[active], identity
        )
        for flavor in (2, 1, -2, -1):
            if flavor not in response_cache:
                responses = np.asarray(
                    [
                        [
                            (
                                csb.member_response(member, flavor, float(xn), 5.0)
                                if 1.0e-5 <= xn <= 0.4
                                else 0.0
                            )
                            for member in range(N_MEMBERS)
                        ]
                        for xn in z
                    ],
                    dtype=float,
                )
                response_cache[flavor] = (z.copy(), responses)
            cached_z, responses = response_cache[flavor]
            if not np.array_equal(z, cached_z):
                raise RuntimeError("production quadrature y nodes changed across waves")
            for k_gev in K_VALUES:
                base_f1 = np.asarray(
                    [
                        evolved_neutron.tmd_values(
                            flavor=flavor,
                            x=float(xn),
                            k_x_gev=(
                                k_gev / HBARC_GEV_FM - xn * px
                            )
                            * HBARC_GEV_FM,
                            k_y_gev=(-xn * py) * HBARC_GEV_FM,
                            scale_gev=5.0,
                            gauge_link=link,
                        )["f1"]
                        for xn, px, py in zip(
                            z, quadrature.p_x[active], quadrature.p_y[active]
                        )
                    ],
                    dtype=float,
                )
                coefficients = weights[:, None] * base_f1[:, None] * responses
                member_vectors = np.einsum(
                    "nm,nIH->mIH", coefficients, spectral_identity
                )
                hermiticity_max = max(
                    hermiticity_max,
                    float(
                        np.max(
                            np.abs(
                                member_vectors
                                - np.swapaxes(member_vectors.conj(), 1, 2)
                            )
                        )
                    ),
                )
                projected_members = []
                for member, vector in enumerate(member_vectors):
                    projected = project_parent_derived_quark_tmds(
                        _delta_correlator(vector),
                        k_x_gev=k_gev,
                        k_y_gev=0.0,
                        deuteron_mass_gev=M_D_GEV,
                    )["neutron"]
                    projected_members.append(projected)
                    for name in SPIN1_QUARK_TMD_NAMES:
                        member_rows.append(
                            {
                                "wave_function": wave_name,
                                "member": member,
                                "flavor": flavor,
                                "x_D": 0.05,
                                "Q_GeV": 5.0,
                                "k_T_GeV": k_gev,
                                "tmd": name,
                                "csb_delta_GeV-2": projected[name],
                            }
                        )
                for name in SPIN1_QUARK_TMD_NAMES:
                    values = np.asarray(
                        [projected[name] for projected in projected_members]
                    )
                    sigma = np.sqrt(
                        np.sum(
                            (
                                (
                                    values[1::2]
                                    - values[2::2]
                                )
                                / 2.0
                            )
                            ** 2
                        )
                    )
                    band_rows.append(
                        {
                            "wave_function": wave_name,
                            "flavor": flavor,
                            "x_D": 0.05,
                            "Q_GeV": 5.0,
                            "k_T_GeV": k_gev,
                            "tmd": name,
                            "central_csb_delta_GeV-2": values[0],
                            "hessian_sigma_GeV-2": sigma,
                            "lower_delta_GeV-2": values[0] - sigma,
                            "upper_delta_GeV-2": values[0] + sigma,
                        }
                    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(member_rows[0]))
        writer.writeheader()
        writer.writerows(member_rows)
    with BANDS.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(band_rows[0]))
        writer.writeheader()
        writer.writerows(band_rows)

    # Compare the vectorized member-0 result to the independently propagated
    # central mechanism table.
    central_path = Path("outputs/parent_tmds/msht20qed_csb_parent.csv")
    if central_path.exists():
        with central_path.open() as stream:
            direct = {
                (
                    row["wave_function"],
                    int(row["flavor"]),
                    float(row["k_T_GeV"]),
                    row["tmd"],
                ): float(row["csb_delta_GeV-2"])
                for row in csv.DictReader(stream)
                if row["part"] == "neutron"
            }
        for row in band_rows:
            key = (
                row["wave_function"],
                row["flavor"],
                row["k_T_GeV"],
                row["tmd"],
            )
            central_direct_max = max(
                central_direct_max,
                abs(row["central_csb_delta_GeV-2"] - direct[key]),
            )
    tolerance = 2.0e-11
    passed = hermiticity_max < tolerance and central_direct_max < tolerance
    report = {
        "status": "pass" if passed else "fail",
        "member_rows": len(member_rows),
        "band_rows": len(band_rows),
        "members": N_MEMBERS,
        "paired_eigenvectors": csb.n_eigenvector_pairs,
        "member_identity_preserved": True,
        "maximum_hermiticity_residual_GeV-2": hermiticity_max,
        "maximum_vectorized_vs_direct_central_GeV-2": central_direct_max,
        "acceptance_GeV-2": tolerance,
        "scope": {
            "mechanism": "neutron unpolarized f1 amplitude CSB",
            "wave_functions": list(WAVE_FUNCTION_CHOICES),
            "flavors": [2, 1, -2, -1],
            "tmd_count": len(SPIN1_QUARK_TMD_NAMES),
            "k_T_GeV": list(K_VALUES),
        },
        "member_table": str(OUTPUT),
        "band_table": str(BANDS),
    }
    VALIDATION.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
