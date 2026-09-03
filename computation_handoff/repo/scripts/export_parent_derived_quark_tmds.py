#!/usr/bin/env python3
"""Export complete quark TMDs through the LF parent correlator."""

from __future__ import annotations

import argparse
from dataclasses import replace
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.integrate import simpson

from deuteron_wigner.axial_tensor_todd import (
    EikonalAxialTensorModel,
    Spin1QuarkNuclearWilsonLine,
)
from deuteron_wigner.canonical_parent_enrichment import (
    project_spin1_quark_parent_positivity,
)
from deuteron_wigner.bpv20_sivers import BPV20ArtemideSivers
from deuteron_wigner.boer_mulders import BoerMuldersFromSiversModel
from deuteron_wigner.csb_inputs import MSHT20QEDChargeSymmetryBreaking
from deuteron_wigner.correlator_io import (
    quark_correlator_rows,
    write_correlator_table,
)
from deuteron_wigner.diffractive_shadowing import (
    H12007JetsDPDF,
    TabulatedBodyFormFactor,
    build_h1_deuteron_shadowing_input,
)
from deuteron_wigner.evolved_quark_grid import EvolvedQuarkGridModel
from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.gtmd_convolution import build_off_forward_component_quadratures
from deuteron_wigner.nuclear_mechanisms import (
    NuclearCorrectionParameters,
    apply_nuclear_corrections,
    build_momentum_sum_antishadowing_input,
    default_off_shell_input,
)
from deuteron_wigner.nucleon_inputs import (
    NucleonInputConfiguration,
    build_nucleon_quark_models,
)
from deuteron_wigner.oam_interference import build_pdf_anchored_oam_model
from deuteron_wigner.parent_quark_tmd import (
    ParentDerivedQuarkResult,
    convolve_spin1_quark_wave_components,
    project_parent_derived_quark_tmds,
)
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider
from deuteron_wigner.pion_exchange import (
    FockNormalizedMillerPionDistribution,
    JAM21IsoscalarPionPDF,
    MillerTensorPionDistribution,
)
from deuteron_wigner.pion_tmd import (
    SpinResolvedTransversePionBoundary,
    Vpion19IntrinsicProfile,
)
from deuteron_wigner.quark_correlator import (
    Spin1QuarkCorrelator,
    project_spin1_quark_correlator,
    project_spin1_quark_correlator_at_origin,
)
from deuteron_wigner.registry import leading_twist_quark_registry
from deuteron_wigner.provenance import ValidityDomain
from deuteron_wigner.transversity import JAMDiFFTransversityGrid
from deuteron_wigner.gtmd import Species
from deuteron_wigner.wavefunctions.selection import (
    WAVE_FUNCTION_CHOICES,
    select_momentum_wave_function,
)
from deuteron_wigner.worm_gear_inputs import (
    Yang2024G1TInput,
    positivity_informed_pretzelosity_model,
)

HBARC_GEV_FM = 0.1973269804
M_N_GEV = 0.93891897
M_D_GEV = 1.87561294257
FLAVORS = ((2, "u", Species.QUARK), (1, "d", Species.QUARK),
           (-2, "ubar", Species.ANTIQUARK), (-1, "dbar", Species.ANTIQUARK))
EVOLVED_GRID = Path("data/processed/evolved_quark_tmd_Q5.npz")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--wave-function", choices=WAVE_FUNCTION_CHOICES, required=True)
    parser.add_argument("--x-n", type=float, default=0.1)
    parser.add_argument("--scale", type=float, default=5.0)
    parser.add_argument("--k-max-gev", type=float, default=1.5)
    parser.add_argument("--n-k-points", type=int, default=101)
    parser.add_argument("--azimuth", type=float, default=0.37)
    parser.add_argument("--internal-k-max-fm", type=float, default=10.0)
    # Six-wave comparison against 32x20x16 establishes this as the minimum
    # production quadrature. Smaller grids are regression/diagnostic only.
    parser.add_argument("--n-internal-k", type=int, default=24)
    parser.add_argument("--n-cos", type=int, default=16)
    parser.add_argument("--n-phi", type=int, default=12)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--correlator-output", type=Path)
    parser.add_argument(
        "--input-scenario",
        choices=("rich_fit", "pdf_anchored_oam"),
        default="rich_fit",
    )
    return parser.parse_args()


def scaled(correlator: Spin1QuarkCorrelator, factor: float) -> Spin1QuarkCorrelator:
    return Spin1QuarkCorrelator(
        factor * correlator.vector,
        factor * correlator.axial,
        factor * correlator.transverse,
    )


def summed(correlators) -> Spin1QuarkCorrelator:
    values = tuple(correlators)
    return Spin1QuarkCorrelator(
        sum(value.vector for value in values),
        sum(value.axial for value in values),
        sum(value.transverse for value in values),
    )


def difference(
    left: Spin1QuarkCorrelator,
    right: Spin1QuarkCorrelator,
) -> Spin1QuarkCorrelator:
    return Spin1QuarkCorrelator(
        left.vector - right.vector,
        left.axial - right.axial,
        left.transverse - right.transverse,
    )


def project(correlator: Spin1QuarkCorrelator, kx: float, ky: float) -> dict[str, float]:
    if np.hypot(kx, ky) <= 1.0e-14:
        return project_spin1_quark_correlator_at_origin(correlator, M_D_GEV)
    return project_spin1_quark_correlator(correlator, (kx, ky), M_D_GEV)


def main() -> None:
    args = parse_args()
    if args.n_k_points < 3 or args.x_n <= 0.0 or args.x_n > 1.0:
        raise ValueError("invalid external grid")
    wave = select_momentum_wave_function(args.wave_function)
    wave.validate_k_max(args.internal_k_max_fm)
    quadratures = build_off_forward_component_quadratures(
        radial=wave.radial,
        nucleon_mass=M_N_GEV / HBARC_GEV_FM,
        k_max=args.internal_k_max_fm,
        delta_x=0.0,
        delta_y=0.0,
        n_k=args.n_internal_k,
        n_cos_theta=args.n_cos,
        n_phi=args.n_phi,
        deuteron_mass=M_D_GEV / HBARC_GEV_FM,
    )
    radial_grid = np.linspace(0.0, args.internal_k_max_fm, 2001)
    radial_values = np.asarray([wave.radial(float(k)) for k in radial_grid])
    radial_measure = radial_grid**2
    s_norm = float(simpson(
        radial_measure * radial_values[:, 0]**2, x=radial_grid
    ))
    d_norm = float(simpson(
        radial_measure * radial_values[:, 1]**2, x=radial_grid
    ))
    wave_norm = s_norm + d_norm
    d_probability = d_norm / wave_norm
    sd_coherence = float(
        simpson(
            radial_measure * radial_values[:, 0] * radial_values[:, 1],
            x=radial_grid,
        ) / np.sqrt(s_norm * d_norm)
    )
    unpolarized_pdf = LHAPDFProvider("CT18NNLO", 0)
    polarized_pdf = PolarizedLHAPDFProvider("BDSSV24-NLO", 0)
    transversity = JAMDiFFTransversityGrid(
        "data/processed/jamdiff_wlqcd_transversity.csv"
    )
    input_configuration = NucleonInputConfiguration.flavor_resolved_baseline()
    if args.input_scenario == "rich_fit":
        bpv20_sivers = BPV20ArtemideSivers()
        sivers_input = bpv20_sivers.fitted_input()
        boer_mulders_input = BoerMuldersFromSiversModel(
            sivers_input
        ).fitted_input()
        pretzelosity_input = positivity_informed_pretzelosity_model(
            unpolarized=unpolarized_pdf.proton,
            helicity=polarized_pdf.proton,
            widths_gev2=input_configuration.transversity_widths_gev2,
        ).fitted_input()
        g1t_input = Yang2024G1TInput().fitted_input()
        h1lperp_input = None
    else:
        def density(nucleon: str, flavor: int, x: float, q: float) -> float:
            provider = (
                unpolarized_pdf.proton
                if nucleon == "proton"
                else unpolarized_pdf.neutron
                if nucleon == "neutron"
                else None
            )
            if provider is None:
                raise ValueError("nucleon must be proton or neutron")
            return float(provider(flavor, x, q))

        oam = build_pdf_anchored_oam_model(
            density,
            transverse_width_gev2=input_configuration.unpolarized_widths_gev2,
        )
        validity = ValidityDomain(
            1.0e-3, 0.8, 1.3, 100.0, 1.5, "OAM sensitivity scenario"
        )
        source = "PDF-anchored explicit S/P-even/P-odd/D LF amplitude model"
        sivers_input = oam.fitted_momentum_input(
            "f1Tperp", source=source, process_reference="future SIDIS",
            validity=validity,
        )
        boer_mulders_input = oam.fitted_momentum_input(
            "h1perp", source=source, process_reference="future SIDIS",
            validity=validity,
        )
        g1t_input = oam.fitted_scalar_input(
            "g1T", source=source, validity=validity,
            transverse_cutoff_gev=1.5,
        )
        h1lperp_input = oam.fitted_scalar_input(
            "h1Lperp", source=source, validity=validity,
            transverse_cutoff_gev=1.5,
        )
        pretzelosity_input = oam.fitted_scalar_input(
            "h1Tperp", source=source, validity=validity,
            transverse_cutoff_gev=1.5,
        )
    csb = MSHT20QEDChargeSymmetryBreaking().as_input()
    proton_boundary, neutron_boundary = build_nucleon_quark_models(
        unpolarized_pdf,
        polarized_pdf,
        configuration=input_configuration,
        transversity_input=transversity,
        sivers_input=sivers_input,
        boer_mulders_input=boer_mulders_input,
        g1t_input=g1t_input,
        h1lperp_input=h1lperp_input,
        pretzelosity_input=pretzelosity_input,
        charge_symmetry_breaking=csb,
    )
    if not np.isclose(args.scale, 5.0, atol=1.0e-12, rtol=0.0):
        raise ValueError(
            "canonical evolved quark grid is currently fixed at Q=5 GeV"
        )
    proton = EvolvedQuarkGridModel(
        proton_boundary, EVOLVED_GRID, "proton", "central",
        charge_symmetry_breaking=csb,
    )
    neutron = EvolvedQuarkGridModel(
        neutron_boundary, EVOLVED_GRID, "neutron", "central",
        charge_symmetry_breaking=csb,
    )
    dpdf = H12007JetsDPDF.load("data/raw/h1_2007_dpdf")
    body_form_factor_path = (
        f"outputs/stage0/body_form_factor_"
        f"{args.wave_function.replace('-', '_')}.csv"
    )
    body_form_factor = TabulatedBodyFormFactor.load(body_form_factor_path)
    diffractive_inputs = {
        flavor: build_h1_deuteron_shadowing_input(
            inclusive_density=lambda x, q, flavor=flavor: (
                unpolarized_pdf.proton(flavor, x, q)
                + unpolarized_pdf.neutron(flavor, x, q)
            ),
            body_form_factor=body_form_factor,
            dpdf=dpdf,
        )
        for flavor, _, _ in FLAVORS
    }
    antishadowing_inputs = {
        flavor: build_momentum_sum_antishadowing_input(
            lambda x, q, flavor=flavor: x * (
                unpolarized_pdf.proton(flavor, x, q)
                + unpolarized_pdf.neutron(flavor, x, q)
            ),
            scale_gev=args.scale,
            parton_sector=("valence" if flavor > 0 else "sea"),
            diffractive_input=diffractive_inputs[flavor],
        )
        for flavor, _, _ in FLAVORS
    }
    k_axis = np.linspace(0.0, args.k_max_gev, args.n_k_points)
    pion_splitting = FockNormalizedMillerPionDistribution(
        MillerTensorPionDistribution()
    )
    pion_boundary = SpinResolvedTransversePionBoundary(
        pion_splitting,
        JAM21IsoscalarPionPDF(0),
        Vpion19IntrinsicProfile(0),
    )
    pion_correlators = {
        flavor: pion_boundary.correlators_k(
            flavor, args.x_n, k_axis, args.scale,
            b_max_gev_inv=12.0, b_nodes=64,
        )
        for flavor, _, _ in FLAVORS
    }
    pion_momentum = pion_splitting.ledger.pinn_sector_pion_momentum
    off_shell_input = default_off_shell_input()
    correction_parameters = replace(
        NuclearCorrectionParameters(), average_nucleon_virtuality=0.0
    )
    reference_quadrature = quadratures["SS"]
    total_spectral = sum(
        component.spectral for component in quadratures.values()
    )
    spectral_density = np.real(np.einsum("nIIaa->n", total_spectral))
    spectral_measure = reference_quadrature.weights * spectral_density
    spectral_norm = float(np.sum(spectral_measure))
    mean_virtuality = float(
        np.dot(spectral_measure, reference_quadrature.virtuality) / spectral_norm
    )
    strong_virtuality_fraction = float(
        np.sum(
            spectral_measure[reference_quadrature.virtuality < -0.3]
        ) / spectral_norm
    )
    x_d = args.x_n / 2.0
    rows: list[dict[str, object]] = []
    correlator_table_rows: list[dict[str, object]] = []
    axial_tensor_model = EikonalAxialTensorModel(
        d_state_probability=d_probability,
        sd_radial_coherence=sd_coherence,
    )
    for link in (GaugeLink("+", "+"), GaugeLink("-", "-")):
        for index, k in enumerate(k_axis):
            kx = float(k * np.cos(args.azimuth))
            ky = float(k * np.sin(args.azimuth))
            for flavor, flavor_label, species in FLAVORS:
                wave_components = convolve_spin1_quark_wave_components(
                    x=x_d,
                    k_x=kx / HBARC_GEV_FM,
                    k_y=ky / HBARC_GEV_FM,
                    scale=args.scale,
                    flavor=flavor,
                    proton=proton,
                    neutron=neutron,
                    gauge_link=link,
                    quadratures=quadratures,
                    momentum_unit_to_gev=HBARC_GEV_FM,
                )
                off_shell_wave_components = convolve_spin1_quark_wave_components(
                    x=x_d,
                    k_x=kx / HBARC_GEV_FM,
                    k_y=ky / HBARC_GEV_FM,
                    scale=args.scale,
                    flavor=flavor,
                    proton=proton,
                    neutron=neutron,
                    gauge_link=link,
                    quadratures=quadratures,
                    momentum_unit_to_gev=HBARC_GEV_FM,
                    node_response=lambda nucleon, z, scale, virtuality: (
                        1.0
                        + virtuality
                        * off_shell_input.value(
                            "valence" if flavor > 0 else "sea", z, scale
                        )
                    ),
                )
                parent = ParentDerivedQuarkResult(
                    proton=summed(
                        value.proton for value in wave_components.values()
                    ),
                    neutron=summed(
                        value.neutron for value in wave_components.values()
                    ),
                )
                # x_N=2*x_D Jacobian times per-nucleon normalization.
                parent = ParentDerivedQuarkResult(
                    scaled(parent.proton, 0.25), scaled(parent.neutron, 0.25)
                )
                wave_component_correlators = {
                    f"wave_{label}": scaled(value.total, 0.25)
                    for label, value in wave_components.items()
                }
                off_shell_parent = scaled(
                    difference(
                        summed(
                            value.total
                            for value in off_shell_wave_components.values()
                        ),
                        summed(value.total for value in wave_components.values()),
                    ),
                    0.25,
                )
                resolved = apply_nuclear_corrections(
                    proton_impulse=parent.proton,
                    neutron_impulse=parent.neutron,
                    x=args.x_n,
                    scale_gev=args.scale,
                    parton_sector=(
                        "valence" if flavor > 0 else "sea"
                    ),
                    antishadowing_input=antishadowing_inputs[flavor],
                    diffractive_input=diffractive_inputs[flavor],
                    parameters=correction_parameters,
                )
                corrections = dict(resolved.corrections)
                corrections["off_shell"] = off_shell_parent
                # Fock-consistent Sullivan term: the explicit transverse
                # pion correlator is accompanied by the minimal unchanged-
                # shape NNpi nucleon counterterm required by the same
                # plus-momentum ledger.
                corrections["meson_exchange"] = summed((
                    pion_correlators[flavor][index],
                    scaled(resolved.impulse, -pion_momentum),
                ))
                correlators = {
                    "proton_impulse": resolved.proton_impulse,
                    "neutron_impulse": resolved.neutron_impulse,
                    "impulse_total": resolved.impulse,
                    **wave_component_correlators,
                    **corrections,
                    "model_total": summed((
                        resolved.impulse, *corrections.values()
                    )),
                }
                raw_total = correlators["model_total"]
                positive_total, positivity_scale = (
                    project_spin1_quark_parent_positivity(raw_total)
                )
                correlators["joint_density_completion"] = difference(
                    positive_total, raw_total
                )
                correlators["model_total"] = positive_total
                nuclear_phase = Spin1QuarkNuclearWilsonLine(
                    axial_tensor_model, flavor, link
                )
                phase_unitary = nuclear_phase.unitary(
                    (kx, ky),
                    input_configuration.helicity_widths_gev2[flavor],
                )
                correlators = {
                    name: nuclear_phase.apply_unitary(value, phase_unitary)
                    for name, value in correlators.items()
                }
                entries = {
                    entry.name: entry
                    for entry in leading_twist_quark_registry(species).select()
                }
                projected = {
                    mechanism: project(correlator, kx, ky)
                    for mechanism, correlator in correlators.items()
                }
                for mechanism, correlator in correlators.items():
                    correlator_table_rows.extend(quark_correlator_rows(
                        correlator,
                        {
                            "wave_function": args.wave_function,
                            "input_scenario": args.input_scenario,
                            "species": species.value,
                            "flavor": flavor,
                            "flavor_label": flavor_label,
                            "mechanism": mechanism,
                            "gauge_link": link.label(),
                            "x_N": args.x_n,
                            "x_D": x_d,
                            "Q_GeV": args.scale,
                            "k_GeV": float(k),
                            "azimuth_rad": args.azimuth,
                        },
                    ))
                f1 = projected["model_total"]["f1"]
                for mechanism, values in projected.items():
                    for name, value in values.items():
                        entry = entries[name]
                        # The configured one-body boundary and nuclear
                        # corrections are real. Time reversal therefore makes
                        # every T-odd coefficient exactly zero; discard only
                        # floating-point projection leakage.
                        if entry.t_odd and abs(value) < 1.0e-10:
                            value = 0.0
                        physical = (
                            (k / M_D_GEV) ** entry.transverse_rank
                            * value
                            / f1
                            if f1 != 0.0
                            else 0.0
                        )
                        rows.append(
                            {
                                "wave_function": args.wave_function,
                                "input_scenario": args.input_scenario,
                                "species": species.value,
                                "flavor": flavor,
                                "flavor_label": flavor_label,
                                "mechanism": mechanism,
                                "operator_projection": entry.parent_projection,
                                "target_channel": entry.target_channel.value,
                                "tmd": name,
                                "rank": entry.transverse_rank,
                                "t_odd": int(entry.t_odd),
                                "gauge_link": link.label(),
                                "x_N": args.x_n,
                                "x_D": x_d,
                                "Q_GeV": args.scale,
                                "k_GeV": float(k),
                                "azimuth_rad": args.azimuth,
                                "F_GeV-2": value,
                                "physical_ratio_to_total_f1": physical,
                                "parent_derived": 1,
                                "joint_density_completion_scale": positivity_scale,
                            }
                        )
            if index % 10 == 0:
                print(
                    f"{args.wave_function} {link.label()} "
                    f"k-point {index + 1}/{len(k_axis)}",
                    flush=True,
                )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(args.output, index=False)
    correlator_output = args.correlator_output or args.output.with_name(
        f"{args.output.stem}.correlators.csv"
    )
    write_correlator_table(correlator_table_rows, correlator_output)
    metadata = {
        "status": "parent-derived flavor-resolved quark impulse plus separated corrections",
        "parent_derived": True,
        "wave_function": args.wave_function,
        "input_scenario": args.input_scenario,
        "x_N": args.x_n,
        "Q_GeV": args.scale,
        "k_points": args.n_k_points,
        "internal_quadrature": {
            "n_k": args.n_internal_k,
            "n_cos": args.n_cos,
            "n_phi": args.n_phi,
            "k_max_fm-1": args.internal_k_max_fm,
        },
        "flavors": [item[1] for item in FLAVORS],
        "basis_per_flavor": 18,
        "mechanisms": [
            "proton_impulse", "neutron_impulse", "impulse_total",
            "wave_SS", "wave_SD", "wave_DS", "wave_DD",
            "coherent_shadowing", "antishadowing", "off_shell", "model_total",
            "meson_exchange", "non_nucleonic", "joint_density_completion",
        ],
        "axial_tensor_nuclear_phase": {
            "implementation": (
                "unitary rank-one LT plus rank-two TT screened Wilson-line "
                "operator on retained target-helicity parents before projection"
            ),
            "d_state_probability": d_probability,
            "sd_radial_coherence": sd_coherence,
            "kernel": axial_tensor_model.kernel.__dict__,
            "flavor_maps": {
                "p_even": axial_tensor_model.p_even,
                "p_odd": axial_tensor_model.p_odd,
                "tensor_coupling": axial_tensor_model.tensor_coupling,
            },
        },
        "meson_exchange_input": {
            "source": (
                "Miller NNpi splitting arXiv:1311.4561; JAM21PionPDFnlo; "
                "Vpion19 intrinsic profile arXiv:1907.10356"
            ),
            "implemented_tmds": ["f1", "f1LL"],
            "fock_counterterm": (
                "minimal unchanged-shape NNpi nucleon subtraction applied "
                "to the complete impulse correlator"
            ),
            "pion_plus_momentum": pion_momentum,
            "total_plus_momentum": pion_splitting.ledger.total_momentum,
            "uncertainty": (
                "JAM21 replicas x axial-mass x Vpion19 profile x 100% "
                "temporary transverse-recoil counterterm model axis"
            ),
        },
        "t_odd_boundary": {
            "f1Tperp": (
                "BPV20 N3LO 500-replica fit central, evolved with released "
                "arTeMiDe v2.05; SIDIS is the future-link reference"
                if args.input_scenario == "rich_fit"
                else "PDF-anchored S/P-odd imaginary LF interference model"
            ),
            "h1perp": (
                "flavor-resolved Barone-Melis-Prokudin proportionality model "
                "composed with the BPV20 momentum-space Sivers boundary; "
                "separate operator coefficients and SIDIS reference"
                if args.input_scenario == "rich_fit"
                else "independent PDF-anchored S/P-odd imaginary LF interference coefficient"
            ),
            "process_rule": "all T-odd structures reverse sign for past links",
        },
        "shadowing_input": {
            "source": diffractive_inputs[2].source,
            "classification": diffractive_inputs[2].classification.value,
            "relative_uncertainty": diffractive_inputs[2].relative_uncertainty,
            "uncertainty_members": sorted(
                diffractive_inputs[2].uncertainty_members or {}
            ),
            "h1_release": "H1 2007 Jets DPDF v1.0 (04/06/2009)",
            "h1_grid_directory": "data/raw/h1_2007_dpdf",
            "deuteron_body_form_factor": body_form_factor_path,
            "formula": "FGS arXiv:hep-ph/0601123 Eq. (4)",
            "x_pomeron_max": {"quark": 0.1, "gluon": 0.03},
            "real_part_eta": 0.5 * np.pi * (dpdf.alpha_pomeron_0 - 1.0),
            "separate_external_coherence_factor": False,
        },
        "charge_symmetry": {
            "configured_limit": "MSHT20-QED neutron f1 CSB central",
            "active_csb_qed_correction": True,
            "provenance": {
                "name": csb.provenance.name,
                "evidence": csb.provenance.evidence.value,
                "mechanism": csb.provenance.mechanism.value,
                "sources": list(csb.provenance.sources),
                "assumptions": list(csb.provenance.assumptions),
                "uncertainty": csb.provenance.uncertainty_kind,
                "replaceable_interface": (
                    csb.provenance.replaceable_interface
                ),
            },
            "physical_status": (
                "MSHT20-QED central and paired Hessian uncertainty apply to "
                "neutron f1 only; polarized, transversity, T-odd, and width "
                "CSB remain unresolved and use the controlled isospin limit"
            ),
        },
        "limitations": [
            "canonical f1/g1/h1/g1T/h1Lperp/h1Tperp use the fixed-Q=5 rank-aware J0/J1/J2 grid; f1Tperp and h1perp retain their fit/model-native momentum boundaries",
            "transversity uses the JAMDiFF wLQCD replica mean with a documented TMD-level positivity projection; replica covariance is not yet propagated",
            (
                "g1T uses the Yang et al. 2024 world-SIDIS central fit; its "
                "published sea-zero assumption and unavailable replica covariance "
                "are explicit, while h1Lperp retains the independent WW boundary"
                if args.input_scenario == "rich_fit"
                else "g1T and h1Lperp are independent real S/P-even OAM bilinears in the PDF-anchored sensitivity scenario"
            ),
            (
                "pretzelosity uses independent flavor-resolved signed fractions "
                "of its positivity ceiling; this is a nonperturbative model "
                "scenario, not a fitted or lattice-determined distribution"
                if args.input_scenario == "rich_fit"
                else "pretzelosity is the integrated S/D rank-two bilinear of the PDF-anchored OAM sensitivity scenario"
            ),
            "Boer-Mulders uses a phenomenological Sivers-proportionality model, not a joint modern TMD fit; coefficient sensitivity is separate from BPV20 replicas",
            "BPV20 documents parton-model Sivers positivity-bound violations; constituent proton/neutron eigenvalues are reported without clipping, while physical deuteron total positivity remains a validation gate",
            "BPV20 ubar and dbar share a fitted sea shape; exact-isospin deuteron sums can therefore coincide even though proton u and d remain distinct",
            "coherent shadowing uses the H1-DPDF/FGS U/vector anchor plus explicit independent axial/transverse and L/T/LL/LT/TT model responses; no joint polarized nuclear fit is assigned",
            "no combined statistical confidence interval is assigned",
            "meson exchange is active with a Fock-consistent minimal NNpi counterterm; unresolved transverse recoil and NNpi spin entanglement retain a 100% model uncertainty",
            "the non-nucleonic central parent remains zero because no sourced intrinsic transverse six-quark/Delta-Delta correlator is available; the existing cluster table is an excluded upper-limit sensitivity",
            "MSHT20-QED neutron f1 charge-symmetry breaking is active; no unsupported CSB is inferred for polarized, chiral-odd, or T-odd sectors",
        ],
        "off_shell_convolution": {
            "virtuality": "(p_active^2-m_N^2)/m_N^2 at every LF spectral node",
            "spectator": "on shell",
            "response_source": off_shell_input.source,
            "response_constrained_x_max": off_shell_input.constrained_x_max,
            "response_uncertainty_at_x_N": off_shell_input.uncertainty(args.x_n),
            "uncertainty_construction": (
                "CJ26 published marginal coefficient errors in diagonal "
                "propagation plus additive/multiplicative HT half-range; "
                "coefficient covariance is not published"
            ),
            "average_virtuality_shortcut": False,
            "spectral_weighted_mean_virtuality": mean_virtuality,
            "spectral_weight_fraction_below_minus_0.3": (
                strong_virtuality_fraction
            ),
            "linear_response_warning": (
                "the reported v<-0.3 tail is retained and exposed, not clipped"
            ),
        },
        "antishadowing_momentum_sum_audit": {
            str(flavor): {
                "lost_momentum": model.lost_momentum,
                "restored_momentum": model.restored_momentum,
                "compensation_fraction": model.compensation_fraction,
            }
            for flavor, model in antishadowing_inputs.items()
        },
        "rows": len(rows),
        "unprojected_correlators": {
            "path": str(correlator_output),
            "format": "long CSV, complex entries split into real/imaginary columns",
            "rows": len(correlator_table_rows),
            "entries_per_correlator": 36,
        },
    }
    args.output.with_suffix(".metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n"
    )
    print(
        f"Wrote {len(rows)} projections to {args.output} and "
        f"{len(correlator_table_rows)} correlator entries to {correlator_output}"
    )


if __name__ == "__main__":
    main()
