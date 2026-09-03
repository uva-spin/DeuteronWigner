#!/usr/bin/env python3
"""Audit production parent b=0 reductions across species and kinematics."""

from __future__ import annotations

import json
from pathlib import Path

from deuteron_wigner.collinear import (
    ScalingVariable,
    build_lf_smearing_spherical,
    impulse_convolution,
)
from deuteron_wigner.conventions import delta_t_to_f1ll
from deuteron_wigner.gluon_correlator import transverse_matrix_parts
from deuteron_wigner.gtmd_convolution import (
    build_off_forward_spin_quadrature,
    convolve_gluon_gtmd_point,
    project_deuteron_gluon_target_channel,
    spin_half_collinear_gluon_correlator,
)
from deuteron_wigner.nucleon_inputs import build_nucleon_quark_models
from deuteron_wigner.parent_quark_tmd import (
    convolve_spin1_quark_collinear_correlator,
    project_parent_derived_quark_tmds,
)
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.transversity import JAMDiFFTransversityGrid
from deuteron_wigner.wavefunctions.selection import (
    WAVE_FUNCTION_CHOICES,
    select_momentum_wave_function,
)

HBARC_GEV_FM = 0.1973269804
M_N_GEV = 0.93891897
M_D_GEV = 1.87561294257
X_VALUES = (0.03, 0.1, 0.3)
Q_VALUES = (2.0, 5.0)
QUARK_FLAVORS = (2, 1, -2, -1)
ORDERS = (24, 16, 12)
OUTPUT = Path("outputs/parent_tmds/parent_collinear_reductions.validation.json")


def relative(actual: float, expected: float) -> float:
    return (actual - expected) / expected if expected != 0.0 else actual - expected


def main() -> None:
    unpolarized = LHAPDFProvider("CT18NNLO", 0)
    polarized = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
    transversity = JAMDiFFTransversityGrid(
        "data/processed/jamdiff_wlqcd_transversity.csv"
    )
    proton, neutron = build_nucleon_quark_models(
        unpolarized, polarized, transversity_input=transversity
    )
    rows: list[dict[str, object]] = []

    for wave_name in WAVE_FUNCTION_CHOICES:
        wave = select_momentum_wave_function(wave_name)
        common = {
            "radial": wave.radial,
            "nucleon_mass": M_N_GEV / HBARC_GEV_FM,
            "k_max": 10.0,
            "n_k": ORDERS[0],
            "n_cos_theta": ORDERS[1],
            "n_phi": ORDERS[2],
        }
        parent_quadrature = build_off_forward_spin_quadrature(
            **common, delta_x=0.0, delta_y=0.0
        )
        smearing = build_lf_smearing_spherical(**common)

        for x_n in X_VALUES:
            for scale in Q_VALUES:
                for flavor in QUARK_FLAVORS:
                    parent = convolve_spin1_quark_collinear_correlator(
                        x=x_n / 2.0,
                        scale=scale,
                        flavor=flavor,
                        proton=proton,
                        neutron=neutron,
                        quadrature=parent_quadrature,
                    )
                    projected = project_parent_derived_quark_tmds(
                        parent,
                        k_x_gev=0.0,
                        k_y_gev=0.0,
                        deuteron_mass_gev=M_D_GEV,
                    )["total"]
                    args = {
                        "x": x_n,
                        "scale": scale,
                        "flavor": flavor,
                        "proton_pdf": unpolarized.proton,
                        "neutron_pdf": unpolarized.neutron,
                        "smearing": smearing,
                        "scaling_variable": ScalingVariable.NUCLEON,
                        "per_nucleon": True,
                    }
                    expected_f1 = impulse_convolution(**args)
                    expected_f1ll = float(delta_t_to_f1ll(
                        impulse_convolution(**args, tensor=True)
                    ))
                    actual_f1 = 0.25 * projected["f1"]
                    actual_f1ll = 0.25 * projected["f1LL"]
                    rows.append({
                        "species": "quark",
                        "wave_function": wave_name,
                        "flavor": flavor,
                        "x_N": x_n,
                        "Q_GeV": scale,
                        "f1_relative": relative(actual_f1, expected_f1),
                        "f1LL_relative": relative(actual_f1ll, expected_f1ll),
                        "f1LL_absolute_GeV-2": actual_f1ll - expected_f1ll,
                        "forbidden_rank_zero_absolute": abs(
                            0.25 * projected["h1LT"]
                        ),
                    })

                def proton_gluon(x, k_x, k_y, delta_x, delta_y, q):
                    return spin_half_collinear_gluon_correlator(
                        unpolarized.proton(21, x, q), 0.0
                    )

                def neutron_gluon(x, k_x, k_y, delta_x, delta_y, q):
                    return spin_half_collinear_gluon_correlator(
                        unpolarized.neutron(21, x, q), 0.0
                    )

                parent_g = convolve_gluon_gtmd_point(
                    x=x_n / 2.0,
                    k_x=0.0,
                    k_y=0.0,
                    scale=scale,
                    proton_gtmd=proton_gluon,
                    neutron_gtmd=neutron_gluon,
                    quadrature=parent_quadrature,
                )
                u = project_deuteron_gluon_target_channel(parent_g, "U")
                ll = project_deuteron_gluon_target_channel(parent_g, "LL")
                actual_f1 = 0.5 * transverse_matrix_parts(u)[0].real
                actual_f1ll = -0.5 * transverse_matrix_parts(ll)[0].real
                args_g = {
                    "x": x_n,
                    "scale": scale,
                    "flavor": 21,
                    "proton_pdf": unpolarized.proton,
                    "neutron_pdf": unpolarized.neutron,
                    "smearing": smearing,
                    "scaling_variable": ScalingVariable.NUCLEON,
                    "per_nucleon": True,
                }
                expected_g = impulse_convolution(**args_g)
                expected_gll = float(delta_t_to_f1ll(
                    impulse_convolution(**args_g, tensor=True)
                ))
                rows.append({
                    "species": "gluon",
                    "wave_function": wave_name,
                    "flavor": 21,
                    "x_N": x_n,
                    "Q_GeV": scale,
                    "f1_relative": relative(actual_f1, expected_g),
                    "f1LL_relative": relative(actual_f1ll, expected_gll),
                    "f1LL_absolute_GeV-2": actual_f1ll - expected_gll,
                    "forbidden_rank_zero_absolute": 0.0,
                })

    max_f1 = max(abs(float(row["f1_relative"])) for row in rows)
    max_f1ll = max(abs(float(row["f1LL_relative"])) for row in rows)
    max_f1ll_absolute = max(
        abs(float(row["f1LL_absolute_GeV-2"])) for row in rows
    )
    max_forbidden = max(
        float(row["forbidden_rank_zero_absolute"]) for row in rows
    )
    tensor_points_pass = all(
        abs(float(row["f1LL_relative"])) < 1e-9
        or abs(float(row["f1LL_absolute_GeV-2"])) < 1e-12
        for row in rows
    )
    passed = max_f1 < 1e-10 and tensor_points_pass and max_forbidden < 1e-11
    report = {
        "status": "pass" if passed else "fail",
        "scope": {
            "wave_functions": list(WAVE_FUNCTION_CHOICES),
            "x_N": list(X_VALUES),
            "Q_GeV": list(Q_VALUES),
            "quark_flavors": list(QUARK_FLAVORS),
            "gluon_flavor": 21,
            "quadrature": {
                "n_k": ORDERS[0], "n_cos": ORDERS[1], "n_phi": ORDERS[2]
            },
        },
        "normalization": "x_D-to-x_N Jacobian and per-nucleon factor: 1/4",
        "comparison": (
            "full retained-helicity LF parent versus independently constructed "
            "spherical LF collinear smearing"
        ),
        "maxima": {
            "f1_relative": max_f1,
            "f1LL_relative": max_f1ll,
            "f1LL_absolute_GeV-2": max_f1ll_absolute,
            "forbidden_rank_zero_absolute_GeV-2": max_forbidden,
        },
        "acceptance": {
            "f1_relative": 1e-10,
            "f1LL_mixed": "relative < 1e-9 or absolute < 1e-12 GeV^-2",
            "forbidden_rank_zero_absolute_GeV-2": 1e-11,
        },
        "points": rows,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({key: report[key] for key in ("status", "scope", "maxima")}, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
