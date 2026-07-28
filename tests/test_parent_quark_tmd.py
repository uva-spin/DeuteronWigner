import unittest

import numpy as np

from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.gtmd_convolution import OffForwardSpinQuadrature
from deuteron_wigner.light_front import (
    LFNormalization,
    off_forward_active_nucleon_density,
)
from deuteron_wigner.nucleon_quark_correlator import (
    FlavorResolvedNucleonQuarkModel,
    NucleonTMDComponent,
    NUCLEON_QUARK_TMD_NAMES,
)
from deuteron_wigner.parent_quark_tmd import (
    convolve_spin1_quark_collinear_correlator,
    convolve_spin1_quark_correlator,
    convolve_spin1_quark_wave_components,
    project_parent_derived_quark_tmds,
)
from deuteron_wigner.provenance import (
    ComponentProvenance,
    EvidenceClass,
    Mechanism,
    ValidityDomain,
)


class ParentQuarkTMDTests(unittest.TestCase):
    def model(self, nucleon_factor):
        provenance = ComponentProvenance(
            name="fixture",
            evidence=EvidenceClass.MODEL,
            mechanism=Mechanism.NUCLEON_IMPULSE,
            sources=("unit test",),
            assumptions=("constant synthetic input",),
            validity=ValidityDomain(0.01, 0.9, 1.0, 10.0),
            uncertainty_kind="parameter fixture",
            replaceable_interface="NucleonTMDComponent",
        )
        components = {}
        for index, name in enumerate(NUCLEON_QUARK_TMD_NAMES):
            components[name] = NucleonTMDComponent(
                value=lambda flavor, x, q, index=index: (
                    nucleon_factor * flavor * (index + 1)
                ),
                width_gev2={1: 0.3, 2: 0.25},
                provenance=provenance,
            )
        return FlavorResolvedNucleonQuarkModel(components, 0.9389)

    def quadrature(self):
        spectral = np.zeros((1, 3, 3, 2, 2), dtype=np.complex128)
        for target in range(3):
            spectral[0, target, target] = np.eye(2) / 2.0
        return OffForwardSpinQuadrature(
            y=np.asarray((0.6,)),
            p_x=np.asarray((0.0,)),
            p_y=np.asarray((0.0,)),
            weights=np.asarray((1.0,)),
            delta_x=0.0,
            delta_y=0.0,
            spectral=spectral,
        )

    def test_proton_and_neutron_remain_separate_and_sum_exactly(self):
        result = convolve_spin1_quark_correlator(
            x=0.2,
            k_x=0.3,
            k_y=0.1,
            scale=3.0,
            flavor=2,
            proton=self.model(1.0),
            neutron=self.model(0.4),
            gauge_link=GaugeLink("+", "+"),
            quadrature=self.quadrature(),
            momentum_unit_to_gev=1.0,
        )
        self.assertFalse(np.allclose(result.proton.vector, result.neutron.vector))
        np.testing.assert_allclose(
            result.total.vector, result.proton.vector + result.neutron.vector
        )
        np.testing.assert_allclose(
            result.total.transverse,
            result.proton.transverse + result.neutron.transverse,
        )

    def test_pure_spin_transfer_does_not_turn_h1_into_pretzelosity(self):
        model = self.model(0.0)
        components = dict(model.components)
        fixture = next(iter(components.values()))
        components["h1"] = NucleonTMDComponent(
            value=lambda flavor, x, q: 0.4,
            width_gev2={1: 0.3, 2: 0.25},
            provenance=fixture.provenance,
        )
        model = FlavorResolvedNucleonQuarkModel(components, 0.9389)
        spectral = off_forward_active_nucleon_density(
            y=0.5, p_x=0.0, p_y=0.0, delta_x=0.0, delta_y=0.0,
            mass=4.75, radial=lambda momentum: (1.0, 0.0),
            normalization=LFNormalization.FLAT,
        )
        pure_s_quadrature = OffForwardSpinQuadrature(
            y=np.asarray((0.5,)), p_x=np.asarray((0.0,)),
            p_y=np.asarray((0.0,)), weights=np.asarray((1.0,)),
            delta_x=0.0, delta_y=0.0, spectral=np.asarray((spectral,)),
        )
        result = convolve_spin1_quark_correlator(
            x=0.2, k_x=0.3, k_y=0.1, scale=3.0, flavor=2,
            proton=model, neutron=model, gauge_link=GaugeLink("+", "+"),
            quadrature=pure_s_quadrature, momentum_unit_to_gev=1.0,
        )
        values = project_parent_derived_quark_tmds(
            result, k_x_gev=0.3, k_y_gev=0.1, deuteron_mass_gev=1.8756
        )["total"]
        self.assertGreater(abs(values["h1"]), 0.0)
        self.assertAlmostEqual(values["h1Tperp"], 0.0, places=12)

    def test_coherent_wave_components_reconstruct_full_parent(self):
        full = self.quadrature()
        fractions = {"SS": 0.72, "SD": 0.11, "DS": 0.09, "DD": 0.08}
        components = {
            label: OffForwardSpinQuadrature(
                y=full.y, p_x=full.p_x, p_y=full.p_y,
                weights=full.weights, delta_x=0.0, delta_y=0.0,
                spectral=fraction * full.spectral,
            )
            for label, fraction in fractions.items()
        }
        arguments = dict(
            x=0.2, k_x=0.3, k_y=0.1, scale=3.0, flavor=2,
            proton=self.model(1.0), neutron=self.model(0.4),
            gauge_link=GaugeLink("+", "+"), momentum_unit_to_gev=1.0,
        )
        resolved = convolve_spin1_quark_wave_components(
            **arguments, quadratures=components
        )
        direct = convolve_spin1_quark_correlator(
            **arguments, quadrature=full
        )
        for nucleon in ("proton", "neutron"):
            np.testing.assert_allclose(
                sum(getattr(value, nucleon).vector for value in resolved.values()),
                getattr(direct, nucleon).vector,
                atol=1e-14,
            )
            np.testing.assert_allclose(
                sum(getattr(value, nucleon).transverse for value in resolved.values()),
                getattr(direct, nucleon).transverse,
                atol=1e-14,
            )

    def test_node_response_uses_stored_virtuality_inside_convolution(self):
        full = self.quadrature()
        virtuality = np.asarray((-0.08,))
        components = {
            label: OffForwardSpinQuadrature(
                y=full.y, p_x=full.p_x, p_y=full.p_y,
                weights=full.weights, delta_x=0.0, delta_y=0.0,
                spectral=fraction * full.spectral,
                virtuality=virtuality,
            )
            for label, fraction in {
                "SS": 0.72, "SD": 0.11, "DS": 0.09, "DD": 0.08
            }.items()
        }
        arguments = dict(
            x=0.2, k_x=0.3, k_y=0.1, scale=3.0, flavor=2,
            proton=self.model(1.0), neutron=self.model(0.4),
            gauge_link=GaugeLink("+", "+"), momentum_unit_to_gev=1.0,
            quadratures=components,
        )
        baseline = convolve_spin1_quark_wave_components(**arguments)
        response = convolve_spin1_quark_wave_components(
            **arguments,
            node_response=lambda nucleon, z, scale, v: 1.0 + 2.0 * v,
        )
        for label in components:
            np.testing.assert_allclose(
                response[label].total.vector,
                0.84 * baseline[label].total.vector,
                atol=1e-14,
            )

    def test_collinear_parent_keeps_only_rank_zero_structures(self):
        result = convolve_spin1_quark_collinear_correlator(
            x=0.2, scale=3.0, flavor=2,
            proton=self.model(1.0), neutron=self.model(0.4),
            quadrature=self.quadrature(),
        )
        values = project_parent_derived_quark_tmds(
            result, k_x_gev=0.0, k_y_gev=0.0,
            deuteron_mass_gev=1.8756,
        )["total"]
        self.assertAlmostEqual(values["f1"], (2.0 + 0.8) / 0.6)
        self.assertAlmostEqual(values["h1LT"], 0.0, places=14)
        positive_rank = set(values) - {"f1", "g1", "h1", "f1LL", "h1LT"}
        for name in positive_rank:
            self.assertEqual(values[name], 0.0)


if __name__ == "__main__":
    unittest.main()
