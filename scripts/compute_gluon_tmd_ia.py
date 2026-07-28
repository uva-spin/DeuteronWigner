#!/usr/bin/env python3
"""Sample the retained-index nucleonic deuteron gluon TMD."""

from __future__ import annotations

import argparse
import csv
from functools import lru_cache
from pathlib import Path

import numpy as np
from scipy.integrate import simpson

from deuteron_wigner.collinear import (
    ScalingVariable,
    build_lf_smearing_spherical,
    impulse_convolution,
)
from deuteron_wigner.gtmd_convolution import (
    build_off_forward_spin_quadrature,
    convolve_gluon_gtmd_point,
    project_deuteron_gluon_l_t_lt,
    project_deuteron_gluon_u_ll,
)
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.tmd_models import GaussianSpinHalfGluonGTMD
from deuteron_wigner.wavefunctions.selection import (
    WAVE_FUNCTION_CHOICES,
    select_momentum_wave_function,
)

HBARC_GEV_FM = 0.1973269804
AVERAGE_NUCLEON_MASS_GEV = 0.93891897
DEUTERON_MASS_GEV = 1.87561294257
GLUON_FLAVOR = 21


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wave-function", choices=WAVE_FUNCTION_CHOICES, required=True)
    parser.add_argument("--pdf-set", default="CT18NNLO")
    parser.add_argument("--member", type=int, default=0)
    parser.add_argument("--polarized-pdf-set", default="BDSSV24-NLO")
    parser.add_argument("--polarized-member", type=int, default=0)
    parser.add_argument("--x-n", type=float, default=0.1)
    parser.add_argument("--scale", type=float, default=2.0)
    parser.add_argument("--width-gev2", type=float, default=0.25)
    parser.add_argument("--linear-fraction", type=float, default=0.5)
    parser.add_argument("--k-grid-max-gev", type=float, default=1.6)
    parser.add_argument("--n-k-grid", type=int, default=24)
    parser.add_argument("--internal-k-max-fm", type=float, default=10.0)
    parser.add_argument("--n-internal-k", type=int, default=16)
    parser.add_argument("--n-cos", type=int, default=12)
    parser.add_argument("--n-phi", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.n_k_grid < 4 or args.n_k_grid % 2:
        raise ValueError("n-k-grid must be even and at least four (avoids k_T=0)")
    selection = select_momentum_wave_function(args.wave_function)
    selection.validate_k_max(args.internal_k_max_fm)
    nucleon_mass_fm = AVERAGE_NUCLEON_MASS_GEV / HBARC_GEV_FM
    deuteron_mass_fm = DEUTERON_MASS_GEV / HBARC_GEV_FM
    quadrature = build_off_forward_spin_quadrature(
        radial=selection.radial,
        nucleon_mass=nucleon_mass_fm,
        k_max=args.internal_k_max_fm,
        delta_x=0.0,
        delta_y=0.0,
        n_k=args.n_internal_k,
        n_cos_theta=args.n_cos,
        n_phi=args.n_phi,
    )
    smearing = build_lf_smearing_spherical(
        radial=selection.radial,
        nucleon_mass=nucleon_mass_fm,
        k_max=args.internal_k_max_fm,
        n_k=args.n_internal_k,
        n_cos_theta=args.n_cos,
        n_phi=args.n_phi,
    )
    provider = LHAPDFProvider(args.pdf_set, args.member)
    polarized = PolarizedLHAPDFProvider(
        args.polarized_pdf_set, args.polarized_member
    )

    @lru_cache(maxsize=None)
    def gluon_pdf(x: float, scale: float) -> float:
        return provider.proton(GLUON_FLAVOR, x, scale)

    @lru_cache(maxsize=None)
    def helicity_gluon_pdf(x: float, scale: float) -> float:
        return polarized.gluon(x, scale)

    model = GaussianSpinHalfGluonGTMD(
        gluon_pdf,
        width=args.width_gev2 / HBARC_GEV_FM**2,
        nucleon_mass=nucleon_mass_fm,
        helicity_pdf=helicity_gluon_pdf,
        linear_fraction=args.linear_fraction,
    )
    axis_gev = np.linspace(
        -args.k_grid_max_gev, args.k_grid_max_gev, args.n_k_grid
    )
    axis_fm = axis_gev / HBARC_GEV_FM
    shape = (args.n_k_grid, args.n_k_grid)
    names = (
        "f1g", "h1perpg", "f1LLg", "h1LLperpg",
        "g1g", "h1Lperpg",
        "f1Tperpg", "g1Tg", "h1Tg", "h1Tperpg",
        "f1LTg", "g1LTg", "h1LTg", "h1LTperpg",
    )
    grids = {name: np.empty(shape, dtype=np.float64) for name in names}
    x_d = args.x_n / 2.0
    for ix, k_x in enumerate(axis_fm):
        for iy, k_y in enumerate(axis_fm):
            correlator = convolve_gluon_gtmd_point(
                x=x_d,
                k_x=float(k_x),
                k_y=float(k_y),
                scale=args.scale,
                proton_gtmd=model,
                neutron_gtmd=model,
                quadrature=quadrature,
            )
            unpolarized, ll = project_deuteron_gluon_u_ll(
                correlator, (k_x, k_y), deuteron_mass_fm
            )
            polarized_sectors = project_deuteron_gluon_l_t_lt(
                correlator, (k_x, k_y), deuteron_mass_fm
            )
            # The parent uses x_D and the p+n deuteron density.  Convert with
            # the x_N=2*x_D Jacobian and the explicit per-nucleon factor used
            # by impulse_convolution(..., per_nucleon=True).
            density_conversion = 1.0 / (4.0 * HBARC_GEV_FM**2)
            grids["f1g"][ix, iy] = density_conversion * unpolarized.trace
            grids["h1perpg"][ix, iy] = density_conversion * unpolarized.linear
            grids["f1LLg"][ix, iy] = density_conversion * ll.trace
            grids["h1LLperpg"][ix, iy] = density_conversion * ll.linear
            grids["g1g"][ix, iy] = (
                density_conversion * polarized_sectors["L"]["g1"]
            )
            grids["h1Lperpg"][ix, iy] = (
                density_conversion * polarized_sectors["L"]["h1Lperp"]
            )
            for output_name, sector, tmd_name in (
                ("f1Tperpg", "T", "f1Tperp"),
                ("g1Tg", "T", "g1T"),
                ("h1Tg", "T", "h1"),
                ("h1Tperpg", "T", "h1Tperp"),
                ("f1LTg", "LT", "f1LT"),
                ("g1LTg", "LT", "g1LT"),
                ("h1LTg", "LT", "h1LT"),
                ("h1LTperpg", "LT", "h1LTperp"),
            ):
                grids[output_name][ix, iy] = (
                    density_conversion
                    * polarized_sectors[sector][tmd_name]
                )

    marginals = {
        name: float(
            simpson(simpson(values, x=axis_gev, axis=1), x=axis_gev, axis=0)
        )
        for name, values in grids.items()
    }
    common = dict(
        x=args.x_n,
        scale=args.scale,
        flavor=GLUON_FLAVOR,
        proton_pdf=provider.proton,
        neutron_pdf=provider.neutron,
        smearing=smearing,
        scaling_variable=ScalingVariable.NUCLEON,
        per_nucleon=True,
    )
    collinear_f1 = impulse_convolution(**common)
    collinear_delta_t = impulse_convolution(**common, tensor=True)
    collinear_f1ll = -(2.0 / 3.0) * collinear_delta_t
    summary = {
        "wave_function": args.wave_function,
        "pdf_set": args.pdf_set,
        "member": args.member,
        "polarized_pdf_set": args.polarized_pdf_set,
        "polarized_member": args.polarized_member,
        "x_N": args.x_n,
        "x_D": x_d,
        "Q_GeV": args.scale,
        "width_GeV2": args.width_gev2,
        "linear_fraction": args.linear_fraction,
        "k_grid_max_GeV": args.k_grid_max_gev,
        "n_k_grid": args.n_k_grid,
        "internal_k_max_fm": args.internal_k_max_fm,
        "n_internal_k": args.n_internal_k,
        "n_cos": args.n_cos,
        "n_phi": args.n_phi,
        "f1g_grid_marginal": marginals["f1g"],
        "f1g_collinear": collinear_f1,
        "f1g_relative_error": (marginals["f1g"] - collinear_f1) / collinear_f1,
        "f1LLg_grid_marginal": marginals["f1LLg"],
        "f1LLg_collinear": collinear_f1ll,
        "f1LLg_relative_error": (
            (marginals["f1LLg"] - collinear_f1ll) / collinear_f1ll
            if collinear_f1ll != 0.0
            else float("nan")
        ),
        "h1perpg_grid_integral": marginals["h1perpg"],
        "h1LLperpg_grid_integral": marginals["h1LLperpg"],
        "h1TTg_collinear_one_body": 0.0,
        "smearing_norm": smearing.unpolarized_norm(),
        "tensor_sum": smearing.tensor_norm(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        args.output,
        k_x_GeV=axis_gev,
        k_y_GeV=axis_gev,
        **grids,
        **{key: np.asarray(value) for key, value in summary.items()},
    )
    summary_path = args.output.with_suffix(".csv")
    with summary_path.open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=tuple(summary))
        writer.writeheader()
        writer.writerow(summary)
    print(
        f"# {args.wave_function} f1_error={summary['f1g_relative_error']:.3e} "
        f"f1LL_error={summary['f1LLg_relative_error']:.3e} "
        f"wrote={args.output}"
    )


if __name__ == "__main__":
    main()
