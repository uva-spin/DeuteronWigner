#!/usr/bin/env python3
"""Sample a helicity-resolved one-body GTMD and transform it to Wigner space."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np
from scipy.integrate import simpson

from deuteron_wigner.fourier import direct_fourier_2d
from deuteron_wigner.conventions import GTMD_IMAGING_CONVENTION
from deuteron_wigner.gtmd_convolution import build_off_forward_spin_quadrature
from deuteron_wigner.gtmd_convolution import build_off_forward_component_quadratures
from deuteron_wigner.gtmd_models import FactorizedGaussianGTMD
from deuteron_wigner.gtmd_sampling import (
    convolve_factorized_gaussian_gpd,
    convolve_factorized_gaussian_grid,
)
from deuteron_wigner.pdfs import LHAPDFProvider
from deuteron_wigner.spin import HelicityMatrix
from deuteron_wigner.wavefunctions.selection import (
    WAVE_FUNCTION_CHOICES,
    select_momentum_wave_function,
)

HBARC_GEV_FM = 0.1973269804
AVERAGE_NUCLEON_MASS_GEV = 0.93891897


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wave-function", choices=WAVE_FUNCTION_CHOICES, required=True)
    parser.add_argument("--x", type=float, default=0.2)
    parser.add_argument("--scale", type=float, default=2.0)
    parser.add_argument("--flavor", type=int, default=2)
    parser.add_argument("--charge-weighted-light", action="store_true")
    parser.add_argument("--components", action="store_true")
    parser.add_argument("--pdf-set", default="CT18NNLO")
    parser.add_argument("--width-gev2", type=float, default=0.25)
    parser.add_argument("--slope-gev-2", type=float, default=1.0)
    parser.add_argument("--k-max-gev", type=float, default=0.8)
    parser.add_argument("--delta-max-gev", type=float, default=0.8)
    parser.add_argument("--b-max-gev-1", type=float, default=8.0)
    parser.add_argument("--n-k-grid", type=int, default=9)
    parser.add_argument("--n-delta-grid", type=int, default=9)
    parser.add_argument("--n-b-grid", type=int, default=9)
    parser.add_argument("--internal-k-max-fm", type=float, default=10.0)
    parser.add_argument("--n-internal-k", type=int, default=16)
    parser.add_argument("--n-cos", type=int, default=12)
    parser.add_argument("--n-phi", type=int, default=12)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if min(args.n_k_grid, args.n_delta_grid, args.n_b_grid) < 3:
        raise ValueError("external Cartesian grids require at least three points")
    if args.n_delta_grid % 2 == 0 or args.n_k_grid % 2 == 0 or args.n_b_grid % 2 == 0:
        raise ValueError("external Cartesian grid orders must be odd and contain zero")
    selection = select_momentum_wave_function(args.wave_function)
    selection.validate_k_max(args.internal_k_max_fm)
    pdf = LHAPDFProvider(args.pdf_set)
    if args.charge_weighted_light:
        charges = {1: -1.0 / 3.0, 2: 2.0 / 3.0}
        proton_pdf = lambda unused, x, scale: sum(
            charge**2 * (
                pdf.proton(flavor, x, scale) + pdf.proton(-flavor, x, scale)
            )
            for flavor, charge in charges.items()
        )
        neutron_pdf = lambda unused, x, scale: sum(
            charge**2 * (
                pdf.neutron(flavor, x, scale) + pdf.neutron(-flavor, x, scale)
            )
            for flavor, charge in charges.items()
        )
        sampled_flavor = 0
    else:
        proton_pdf = pdf.proton
        neutron_pdf = pdf.neutron
        sampled_flavor = args.flavor
    proton = FactorizedGaussianGTMD(
        pdf=proton_pdf,
        width=args.width_gev2 / HBARC_GEV_FM**2,
        slope=args.slope_gev_2 * HBARC_GEV_FM**2,
    )
    neutron = FactorizedGaussianGTMD(
        pdf=neutron_pdf,
        width=args.width_gev2 / HBARC_GEV_FM**2,
        slope=args.slope_gev_2 * HBARC_GEV_FM**2,
    )
    k_gev = np.linspace(-args.k_max_gev, args.k_max_gev, args.n_k_grid)
    delta_gev = np.linspace(
        -args.delta_max_gev, args.delta_max_gev, args.n_delta_grid
    )
    k_fm = k_gev / HBARC_GEV_FM
    values = np.empty(
        (args.n_delta_grid, args.n_delta_grid, args.n_k_grid, args.n_k_grid, 3, 3),
        dtype=np.complex128,
    )
    analytic_gpd = np.empty(
        (args.n_delta_grid, args.n_delta_grid, 3, 3), dtype=np.complex128
    )
    component_values = {
        label: np.empty_like(values) for label in ("SS", "SD", "DS", "DD")
    } if args.components else {}
    for ix, delta_x_gev in enumerate(delta_gev):
        for iy, delta_y_gev in enumerate(delta_gev):
            builder = (
                build_off_forward_component_quadratures
                if args.components else build_off_forward_spin_quadrature
            )
            built = builder(
                radial=selection.radial,
                nucleon_mass=AVERAGE_NUCLEON_MASS_GEV / HBARC_GEV_FM,
                k_max=args.internal_k_max_fm,
                delta_x=float(delta_x_gev / HBARC_GEV_FM),
                delta_y=float(delta_y_gev / HBARC_GEV_FM),
                n_k=args.n_internal_k,
                n_cos_theta=args.n_cos,
                n_phi=args.n_phi,
            )
            quadratures = built if args.components else {"full": built}
            if args.components:
                quadrature = next(iter(quadratures.values()))
                sampled_components = []
                for label, component_quadrature in quadratures.items():
                    component_values[label][ix, iy] = (
                        convolve_factorized_gaussian_grid(
                            x=args.x, k_x=k_fm, k_y=k_fm, scale=args.scale,
                            flavor=sampled_flavor, proton=proton, neutron=neutron,
                            quadrature=component_quadrature,
                        ).values / HBARC_GEV_FM**2
                    )
                    sampled_components.append(component_values[label][ix, iy])
                values[ix, iy] = sum(sampled_components)
                analytic_gpd[ix, iy] = sum(
                    convolve_factorized_gaussian_gpd(
                        x=args.x, scale=args.scale, flavor=sampled_flavor,
                        proton=proton, neutron=neutron, quadrature=item,
                    ).values for item in quadratures.values()
                )
                continue
            quadrature = built
            # Convert density per fm^-2 to density per GeV^-2.
            values[ix, iy] = convolve_factorized_gaussian_grid(
                x=args.x, k_x=k_fm, k_y=k_fm, scale=args.scale,
                flavor=sampled_flavor, proton=proton, neutron=neutron,
                quadrature=quadrature,
            ).values / HBARC_GEV_FM**2
            analytic_gpd[ix, iy] = convolve_factorized_gaussian_gpd(
                x=args.x, scale=args.scale, flavor=sampled_flavor,
                proton=proton, neutron=neutron, quadrature=quadrature,
            ).values

    b_axis = np.linspace(-args.b_max_gev_1, args.b_max_gev_1, args.n_b_grid)
    bx, by = np.meshgrid(b_axis, b_axis, indexing="ij")
    points = np.column_stack((bx.ravel(), by.ravel()))
    wigner = direct_fourier_2d(
        delta_gev, delta_gev, values, points, GTMD_IMAGING_CONVENTION
    ).reshape(args.n_b_grid, args.n_b_grid, args.n_k_grid, args.n_k_grid, 3, 3)
    component_wigner = {
        label: direct_fourier_2d(
            delta_gev, delta_gev, array, points, GTMD_IMAGING_CONVENTION
        ).reshape(
            args.n_b_grid, args.n_b_grid, args.n_k_grid, args.n_k_grid, 3, 3
        )
        for label, array in component_values.items()
    }

    numerical_gpd = simpson(simpson(values, x=k_gev, axis=3), x=k_gev, axis=2)
    gpd_relative_error = np.max(
        np.abs(numerical_gpd - analytic_gpd)
        / np.maximum(np.abs(analytic_gpd), 1e-14)
    )
    minus = values[::-1, ::-1]
    hermiticity_error = np.max(
        np.abs(minus - values.conj().swapaxes(-1, -2))
    )
    center = args.n_delta_grid // 2
    forward = HelicityMatrix(values[center, center])
    metadata = dict(
        wave_function=args.wave_function,
        x=args.x,
        scale_gev=args.scale,
        flavor=sampled_flavor,
        flavor_content=(
            "sum_e2_[u+ubar+d+dbar]"
            if args.charge_weighted_light else str(args.flavor)
        ),
        pdf_set=args.pdf_set,
        width_gev2=args.width_gev2,
        slope_gev_minus2=args.slope_gev_2,
        internal_k_max_fm=args.internal_k_max_fm,
        nucleon_gtmd_model="factorized_gaussian_rank_zero",
        gauge_link="[+,+]",
        transfer_mapping="delta_N=delta_D",
        gpd_k_grid_relative_error=float(gpd_relative_error),
        delta_hermiticity_max_error=float(hermiticity_error),
        truncated_k_integral=1,
        truncated_delta_transform=1,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    payload = dict(
        k_gev=k_gev,
        delta_gev=delta_gev,
        b_gev_inverse=b_axis,
        gtmd=values,
        wigner=wigner,
        analytic_gpd=analytic_gpd,
        numerical_gpd=numerical_gpd,
        forward_unpolarized=forward.unpolarized(),
        forward_tensor_difference=forward.tensor_difference(),
        **metadata,
    )
    for label, array in component_values.items():
        payload[f"gtmd_{label}"] = array
        payload[f"wigner_{label}"] = component_wigner[label]
    np.savez_compressed(args.output, **payload)
    summary = args.output.with_suffix(".csv")
    k0 = args.n_k_grid // 2
    b0 = args.n_b_grid // 2
    with summary.open("w", newline="") as stream:
        fields = [
            "wave_function", "x", "kT_GeV", "gtmd_forward_U",
            "gtmd_forward_deltaT", "wigner_b0_U", "wigner_b0_deltaT",
        ]
        if args.components:
            for label in ("SS", "SD_plus_DS", "DD"):
                fields.extend((f"wigner_b0_U_{label}", f"wigner_b0_deltaT_{label}"))
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        for ik, momentum in enumerate(k_gev):
            matrix = HelicityMatrix(wigner[b0, b0, ik, k0])
            row = dict(
                wave_function=args.wave_function, x=args.x, kT_GeV=momentum,
                gtmd_forward_U=forward.unpolarized()[ik, k0].real,
                gtmd_forward_deltaT=forward.tensor_difference()[ik, k0].real,
                wigner_b0_U=matrix.unpolarized().real,
                wigner_b0_deltaT=matrix.tensor_difference().real,
            )
            if args.components:
                selected = {
                    "SS": component_wigner["SS"],
                    "SD_plus_DS": component_wigner["SD"] + component_wigner["DS"],
                    "DD": component_wigner["DD"],
                }
                for label, array in selected.items():
                    component_matrix = HelicityMatrix(array[b0, b0, ik, k0])
                    row[f"wigner_b0_U_{label}"] = component_matrix.unpolarized().real
                    row[f"wigner_b0_deltaT_{label}"] = (
                        component_matrix.tensor_difference().real
                    )
            writer.writerow(row)
    print(
        f"# {args.wave_function} hermiticity={hermiticity_error:.3e} "
        f"truncated_k_gpd_error={gpd_relative_error:.3e} output={args.output}"
    )


if __name__ == "__main__":
    main()
