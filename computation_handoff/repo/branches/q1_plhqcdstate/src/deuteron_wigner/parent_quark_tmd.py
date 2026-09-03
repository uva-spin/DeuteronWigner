"""Parent-derived spin-1 quark TMD assembly through the LF convolution."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np

from .gtmd import GaugeLink
from .gtmd_convolution import OffForwardSpinQuadrature, TransferMapping
from .nucleon_quark_correlator import FlavorResolvedNucleonQuarkModel
from .quark_correlator import (
    Spin1QuarkCorrelator,
    project_spin1_quark_correlator,
    project_spin1_quark_correlator_at_origin,
)


@dataclass(frozen=True)
class ParentDerivedQuarkResult:
    proton: Spin1QuarkCorrelator
    neutron: Spin1QuarkCorrelator

    @property
    def total(self) -> Spin1QuarkCorrelator:
        return Spin1QuarkCorrelator(
            self.proton.vector + self.neutron.vector,
            self.proton.axial + self.neutron.axial,
            self.proton.transverse + self.neutron.transverse,
        )


def convolve_spin1_quark_correlator(
    *,
    x: float,
    k_x: float,
    k_y: float,
    scale: float,
    flavor: int,
    proton: FlavorResolvedNucleonQuarkModel,
    neutron: FlavorResolvedNucleonQuarkModel,
    gauge_link: GaugeLink,
    quadrature: OffForwardSpinQuadrature,
    momentum_unit_to_gev: float,
    transfer_mapping: TransferMapping = TransferMapping.IDENTITY,
) -> ParentDerivedQuarkResult:
    """Convolve all three twist-2 quark operator projections.

    The returned proton and neutron pieces remain separate.  Their sum is
    the inclusive impulse result, while either term can be used by tagged or
    charge-symmetry-breaking extensions.
    """

    if not 0.0 < x <= 1.0 or scale <= 0.0 or momentum_unit_to_gev <= 0.0:
        raise ValueError("invalid x, scale, or momentum conversion")
    accumulated = {
        nucleon: {
            "vector": np.zeros((3, 3), dtype=np.complex128),
            "axial": np.zeros((3, 3), dtype=np.complex128),
            "transverse": np.zeros((2, 3, 3), dtype=np.complex128),
        }
        for nucleon in ("proton", "neutron")
    }
    for y, p_x, p_y, weight, spectral in zip(
        quadrature.y,
        quadrature.p_x,
        quadrature.p_y,
        quadrature.weights,
        quadrature.spectral,
    ):
        if y < x:
            continue
        z = x / y
        parton_k_x = k_x - z * p_x
        parton_k_y = k_y - z * p_y
        delta_x, delta_y = transfer_mapping.nucleon_transfer(
            float(y), quadrature.delta_x, quadrature.delta_y
        )
        for nucleon, model in (("proton", proton), ("neutron", neutron)):
            value = model.correlator(
                flavor=flavor,
                x=float(z),
                k_x_gev=momentum_unit_to_gev * parton_k_x,
                k_y_gev=momentum_unit_to_gev * parton_k_y,
                delta_x_gev=momentum_unit_to_gev * delta_x,
                delta_y_gev=momentum_unit_to_gev * delta_y,
                scale_gev=scale,
                gauge_link=gauge_link,
            )
            factor = weight / y
            accumulated[nucleon]["vector"] += factor * np.einsum(
                "IHca,ac->IH", spectral, value.vector
            )
            accumulated[nucleon]["axial"] += factor * np.einsum(
                "IHca,ac->IH", spectral, value.axial
            )
            accumulated[nucleon]["transverse"] += factor * np.einsum(
                "IHca,iac->iIH", spectral, value.transverse
            )
    correlators = {
        nucleon: Spin1QuarkCorrelator(**values)
        for nucleon, values in accumulated.items()
    }
    return ParentDerivedQuarkResult(**correlators)


def convolve_spin1_quark_collinear_correlator(
    *,
    x: float,
    scale: float,
    flavor: int,
    proton: FlavorResolvedNucleonQuarkModel,
    neutron: FlavorResolvedNucleonQuarkModel,
    quadrature: OffForwardSpinQuadrature,
) -> ParentDerivedQuarkResult:
    """Compose the exact b=0/collinear parent from rank-zero nucleon inputs."""

    if not 0.0 < x <= 1.0 or scale <= 0.0:
        raise ValueError("invalid x or scale")
    identity = np.eye(2, dtype=np.complex128)
    sigma = (
        np.asarray(((0.0, 1.0), (1.0, 0.0)), dtype=np.complex128),
        np.asarray(((0.0, 1j), (-1j, 0.0)), dtype=np.complex128),
        np.asarray(((1.0, 0.0), (0.0, -1.0)), dtype=np.complex128),
    )
    accumulated = {
        nucleon: {
            "vector": np.zeros((3, 3), dtype=np.complex128),
            "axial": np.zeros((3, 3), dtype=np.complex128),
            "transverse": np.zeros((2, 3, 3), dtype=np.complex128),
        }
        for nucleon in ("proton", "neutron")
    }
    for y, weight, spectral in zip(
        quadrature.y, quadrature.weights, quadrature.spectral
    ):
        if y < x:
            continue
        z = float(x / y)
        for nucleon, model in (("proton", proton), ("neutron", neutron)):
            f1 = model.components["f1"].value(flavor, z, scale)
            g1 = model.components["g1"].value(flavor, z, scale)
            h1 = model.components["h1"].value(flavor, z, scale)
            factor = weight / y
            target = accumulated[nucleon]
            target["vector"] += factor * np.einsum(
                "IHca,ac->IH", spectral, f1 * identity
            )
            target["axial"] += factor * np.einsum(
                "IHca,ac->IH", spectral, g1 * sigma[2]
            )
            for index in range(2):
                target["transverse"][index] += factor * np.einsum(
                    "IHca,ac->IH", spectral, h1 * sigma[index]
                )
    return ParentDerivedQuarkResult(**{
        nucleon: Spin1QuarkCorrelator(**values)
        for nucleon, values in accumulated.items()
    })


def convolve_spin1_quark_wave_components(
    *,
    x: float,
    k_x: float,
    k_y: float,
    scale: float,
    flavor: int,
    proton: FlavorResolvedNucleonQuarkModel,
    neutron: FlavorResolvedNucleonQuarkModel,
    gauge_link: GaugeLink,
    quadratures: dict[str, OffForwardSpinQuadrature],
    momentum_unit_to_gev: float,
    transfer_mapping: TransferMapping = TransferMapping.IDENTITY,
    node_response: Callable[[str, float, float, float], float] | None = None,
) -> dict[str, ParentDerivedQuarkResult]:
    """Convolve coherent SS, SD, DS, and DD spectral components in one pass.

    All component quadratures must share nodes and weights. The nucleon
    correlator is evaluated once per node and contracted with each coherent
    wave-function overlap, preserving interference phases and avoiding four
    independent model evaluations.
    """

    required = {"SS", "SD", "DS", "DD"}
    if set(quadratures) != required:
        raise ValueError(f"component quadratures must be exactly {sorted(required)}")
    reference = quadratures["SS"]
    for label, quadrature in quadratures.items():
        for name in ("y", "p_x", "p_y", "weights", "virtuality"):
            if not np.array_equal(getattr(reference, name), getattr(quadrature, name)):
                raise ValueError(f"{label} component does not share {name} nodes")
    accumulated = {
        label: {
            nucleon: {
                "vector": np.zeros((3, 3), dtype=np.complex128),
                "axial": np.zeros((3, 3), dtype=np.complex128),
                "transverse": np.zeros((2, 3, 3), dtype=np.complex128),
            }
            for nucleon in ("proton", "neutron")
        }
        for label in required
    }
    for node, (y, p_x, p_y, weight) in enumerate(zip(
        reference.y, reference.p_x, reference.p_y, reference.weights
    )):
        if y < x:
            continue
        z = x / y
        parton_k_x = k_x - z * p_x
        parton_k_y = k_y - z * p_y
        delta_x, delta_y = transfer_mapping.nucleon_transfer(
            float(y), reference.delta_x, reference.delta_y
        )
        for nucleon, model in (("proton", proton), ("neutron", neutron)):
            value = model.correlator(
                flavor=flavor, x=float(z),
                k_x_gev=momentum_unit_to_gev * parton_k_x,
                k_y_gev=momentum_unit_to_gev * parton_k_y,
                delta_x_gev=momentum_unit_to_gev * delta_x,
                delta_y_gev=momentum_unit_to_gev * delta_y,
                scale_gev=scale, gauge_link=gauge_link,
            )
            response = (
                1.0
                if node_response is None
                else float(node_response(
                    nucleon, float(z), scale, float(reference.virtuality[node])
                ))
            )
            if not np.isfinite(response):
                raise ValueError("node response must be finite")
            for label, quadrature in quadratures.items():
                spectral = quadrature.spectral[node]
                factor = response * weight / y
                target = accumulated[label][nucleon]
                target["vector"] += factor * np.einsum(
                    "IHca,ac->IH", spectral, value.vector
                )
                target["axial"] += factor * np.einsum(
                    "IHca,ac->IH", spectral, value.axial
                )
                target["transverse"] += factor * np.einsum(
                    "IHca,iac->iIH", spectral, value.transverse
                )
    return {
        label: ParentDerivedQuarkResult(
            **{
                nucleon: Spin1QuarkCorrelator(**values)
                for nucleon, values in nucleons.items()
            }
        )
        for label, nucleons in accumulated.items()
    }


def project_parent_derived_quark_tmds(
    result: ParentDerivedQuarkResult,
    *,
    k_x_gev: float,
    k_y_gev: float,
    deuteron_mass_gev: float,
) -> dict[str, dict[str, float]]:
    """Project proton, neutron, and inclusive correlators with one operator basis."""

    momentum = (k_x_gev, k_y_gev)
    projector = (
        project_spin1_quark_correlator_at_origin
        if np.hypot(k_x_gev, k_y_gev) <= 1.0e-14
        else project_spin1_quark_correlator
    )
    if projector is project_spin1_quark_correlator_at_origin:
        return {
            label: projector(correlator, deuteron_mass_gev)
            for label, correlator in (
                ("proton", result.proton),
                ("neutron", result.neutron),
                ("total", result.total),
            )
        }
    return {
        label: projector(correlator, momentum, deuteron_mass_gev)
        for label, correlator in (
            ("proton", result.proton),
            ("neutron", result.neutron),
            ("total", result.total),
        )
    }
