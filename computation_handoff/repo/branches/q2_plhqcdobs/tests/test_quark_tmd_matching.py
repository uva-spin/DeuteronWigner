import unittest
import tempfile
from pathlib import Path

import numpy as np

from deuteron_wigner.evolved_quark_model import EvolvedRankZeroQuarkModel
from deuteron_wigner.evolved_quark_grid import (
    EvolvedQuarkGridModel,
    GRID_COMPONENTS,
    project_spin_half_quark_positivity,
)
from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.gtmd_convolution import OffForwardSpinQuadrature
from deuteron_wigner.nucleon_quark_correlator import (
    FlavorResolvedNucleonQuarkModel,
    NUCLEON_QUARK_TMD_NAMES,
    NucleonTMDComponent,
)
from deuteron_wigner.provenance import (
    ComponentProvenance,
    EvidenceClass,
    Mechanism,
    ValidityDomain,
)
from deuteron_wigner.parent_quark_tmd import convolve_spin1_quark_correlator
from deuteron_wigner.quark_tmd_matching import MatchedRankZeroQuarkTMD
from deuteron_wigner.tmd_evolution import (
    EvolvedMatchedRankZeroQuarkTMD,
    OneLoopQuarkCSSEvolution,
)


class TestRankZeroQuarkMatching(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        provenance = ComponentProvenance(
            name="analytic matching fixture",
            evidence=EvidenceClass.MODEL,
            mechanism=Mechanism.NUCLEON_IMPULSE,
            sources=("unit-test analytic input",),
            assumptions=("Gaussian transverse profile",),
            validity=ValidityDomain(0.01, 0.9, 1.0, 20.0, 2.0),
            uncertainty_kind="none",
            replaceable_interface="NucleonTMDComponent",
        )
        widths = {2: 0.22, 1: 0.31, -2: 0.27, -1: 0.34}

        def model(sign: float) -> FlavorResolvedNucleonQuarkModel:
            components = {}
            for index, name in enumerate(NUCLEON_QUARK_TMD_NAMES):
                components[name] = NucleonTMDComponent(
                    value=lambda flavor, x, q, i=index: sign
                    * (i + 1) * flavor * x,
                    width_gev2=widths,
                    provenance=provenance,
                )
            return FlavorResolvedNucleonQuarkModel(
                components, nucleon_mass_gev=0.9389
            )

        cls.proton, cls.neutron = model(1.0), model(-0.8)

    def test_b_zero_is_collinear_for_each_flavor_and_structure(self) -> None:
        for nucleon in (self.proton, self.neutron):
            boundary = MatchedRankZeroQuarkTMD(nucleon)
            for name in ("f1", "g1", "h1"):
                for flavor in (2, 1, -2, -1):
                    result = boundary.value(name, flavor, 0.1, 0.0, 5.0)
                    self.assertEqual(result.intrinsic_factor, 1.0)
                    self.assertEqual(result.profile_factor, 1.0)
                    self.assertAlmostEqual(
                        result.value, result.collinear_value, places=14
                    )

    def test_gaussian_transform_is_exact(self) -> None:
        boundary = MatchedRankZeroQuarkTMD(self.proton)
        result = boundary.value("f1", 2, 0.1, 1.3, 5.0)
        self.assertAlmostEqual(
            result.intrinsic_factor,
            np.exp(-result.width_gev2 * 1.3**2 / 4.0),
            places=14,
        )

    def test_unsupported_tensor_rank_is_rejected(self) -> None:
        boundary = MatchedRankZeroQuarkTMD(self.proton)
        with self.assertRaisesRegex(ValueError, "rank-zero"):
            boundary.value("g1T", 2, 0.1, 0.4, 5.0)

    def test_quark_css_uses_boundary_at_canonical_scale(self) -> None:
        boundary = MatchedRankZeroQuarkTMD(self.proton)
        evolution = OneLoopQuarkCSSEvolution(alpha_s=lambda q: 0.25)
        evolved = EvolvedMatchedRankZeroQuarkTMD(boundary, evolution)
        result = evolved.value("f1", 2, 0.1, 0.7, 5.0)
        expected = boundary.value("f1", 2, 0.1, 0.7, result.initial_scale)
        self.assertAlmostEqual(result.boundary.value, expected.value, places=14)
        self.assertAlmostEqual(
            result.value,
            result.boundary.value * result.evolution_factor,
            places=14,
        )

    def test_zero_b_has_no_spurious_evolution(self) -> None:
        boundary = MatchedRankZeroQuarkTMD(self.proton)
        evolution = OneLoopQuarkCSSEvolution(alpha_s=lambda q: 0.25)
        result = EvolvedMatchedRankZeroQuarkTMD(
            boundary, evolution
        ).value("h1", 1, 0.2, 0.0, 5.0)
        self.assertEqual(result.initial_scale, 5.0)
        self.assertEqual(result.evolution_factor, 1.0)

    def test_default_canonical_scale_respects_jamdiff_domain(self):
        evolution = OneLoopQuarkCSSEvolution(alpha_s=lambda q: 0.25)
        self.assertGreaterEqual(
            evolution.canonical_scale(1.5, 5.0), np.sqrt(2.0)
        )

    def test_momentum_adapter_reproduces_native_gaussian_at_reference_scale(self):
        boundary = MatchedRankZeroQuarkTMD(self.proton)
        evolved = EvolvedMatchedRankZeroQuarkTMD(
            boundary, OneLoopQuarkCSSEvolution(alpha_s=lambda q: 0.0)
        )
        adapter = EvolvedRankZeroQuarkModel(
            self.proton, evolved, b_max_gev_inverse=16.0, n_b=801
        )
        common = {
            "flavor": 2,
            "x": 0.15,
            "k_x_gev": 0.4,
            "k_y_gev": -0.2,
            "scale_gev": 2.0,
            "gauge_link": GaugeLink("+", "+"),
        }
        native = self.proton.tmd_values(**common)
        transformed = adapter.tmd_values(**common)
        for name in ("f1", "g1", "h1"):
            self.assertAlmostEqual(transformed[name], native[name], places=6)
        for name in ("g1T", "h1Lperp"):
            self.assertAlmostEqual(transformed[name], native[name], places=5)
        self.assertTrue(np.isclose(
            transformed["h1Tperp"], native["h1Tperp"], rtol=1e-5, atol=1e-7
        ))
        for name in ("f1Tperp", "h1perp"):
            self.assertEqual(transformed[name], native[name])

    def test_rank_one_zero_momentum_limit_reproduces_gaussian(self):
        boundary = MatchedRankZeroQuarkTMD(self.proton)
        adapter = EvolvedRankZeroQuarkModel(
            self.proton,
            EvolvedMatchedRankZeroQuarkTMD(
                boundary, OneLoopQuarkCSSEvolution(alpha_s=lambda q: 0.0)
            ),
            b_max_gev_inverse=16.0,
            n_b=801,
        )
        common = {
            "flavor": 1, "x": 0.2, "k_x_gev": 0.0, "k_y_gev": 0.0,
            "scale_gev": 2.0, "gauge_link": GaugeLink("+", "+"),
        }
        native = self.proton.tmd_values(**common)
        transformed = adapter.tmd_values(**common)
        for name in ("g1T", "h1Lperp"):
            self.assertAlmostEqual(transformed[name], native[name], places=6)
        self.assertTrue(np.isclose(
            transformed["h1Tperp"], native["h1Tperp"], rtol=1e-6, atol=1e-7
        ))

    def test_momentum_adapter_is_parent_callable(self):
        boundary = MatchedRankZeroQuarkTMD(self.proton)
        adapter = EvolvedRankZeroQuarkModel(
            self.proton,
            EvolvedMatchedRankZeroQuarkTMD(
                boundary, OneLoopQuarkCSSEvolution(alpha_s=lambda q: 0.0)
            ),
            n_b=201,
        )
        correlator = adapter.correlator(
            flavor=1, x=0.2, k_x_gev=0.3, k_y_gev=0.1,
            delta_x_gev=0.0, delta_y_gev=0.0, scale_gev=2.0,
            gauge_link=GaugeLink("+", "+"),
        )
        correlator.require_hermitian()

    def test_joint_positivity_projection_uses_one_common_spin_scale(self):
        raw = self.proton.correlator(
            flavor=2, x=0.2, k_x_gev=0.4, k_y_gev=0.1,
            delta_x_gev=0.0, delta_y_gev=0.0, scale_gev=2.0,
            gauge_link=GaugeLink("+", "+"),
        )
        overpolarized = type(raw)(
            raw.vector,
            20.0 * raw.axial,
            20.0 * raw.transverse,
        )
        assert overpolarized.minimum_positivity_eigenvalue() < 0.0
        projected, scale = project_spin_half_quark_positivity(overpolarized)
        self.assertGreater(scale, 0.0)
        self.assertLess(scale, 1.0)
        self.assertGreaterEqual(
            projected.minimum_positivity_eigenvalue(), -1.0e-12
        )
        np.testing.assert_allclose(projected.axial, scale * overpolarized.axial)
        np.testing.assert_allclose(
            projected.transverse, scale * overpolarized.transverse
        )

    def test_adapter_flows_through_parent_without_posthoc_factor(self):
        def wrap(model):
            boundary = MatchedRankZeroQuarkTMD(model)
            return EvolvedRankZeroQuarkModel(
                model,
                EvolvedMatchedRankZeroQuarkTMD(
                    boundary, OneLoopQuarkCSSEvolution(alpha_s=lambda q: 0.0)
                ),
                b_max_gev_inverse=16.0,
                n_b=801,
            )

        spectral = np.zeros((1, 3, 3, 2, 2), dtype=np.complex128)
        for target in range(3):
            spectral[0, target, target] = np.eye(2) / 2.0
        quadrature = OffForwardSpinQuadrature(
            y=np.asarray((0.6,)), p_x=np.asarray((0.0,)),
            p_y=np.asarray((0.0,)), weights=np.asarray((1.0,)),
            delta_x=0.0, delta_y=0.0, spectral=spectral,
        )
        common = dict(
            x=0.2, k_x=0.35, k_y=-0.1, scale=2.0, flavor=2,
            gauge_link=GaugeLink("+", "+"), quadrature=quadrature,
            momentum_unit_to_gev=1.0,
        )
        native = convolve_spin1_quark_correlator(
            proton=self.proton, neutron=self.neutron, **common
        )
        transformed = convolve_spin1_quark_correlator(
            proton=wrap(self.proton), neutron=wrap(self.neutron), **common
        )
        np.testing.assert_allclose(
            transformed.total.vector, native.total.vector, atol=2e-6, rtol=2e-6
        )
        np.testing.assert_allclose(
            transformed.total.axial, native.total.axial, atol=2e-6, rtol=2e-6
        )
        np.testing.assert_allclose(
            transformed.total.transverse,
            native.total.transverse,
            atol=2e-6,
            rtol=2e-6,
        )

    def test_portable_grid_replaces_all_six_t_even_components(self):
        x = np.asarray((0.1, 0.3))
        k = np.asarray((0.0, 0.5))
        flavors = np.asarray((2, 1, -2, -1))
        scenarios = np.asarray(("negative", "central", "positive"))
        payload = np.zeros((2, 4, 6, 3, 2, 2))
        for component in range(6):
            for scenario in range(3):
                payload[:, :, component, scenario] = component + scenario + 1
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "grid.npz"
            np.savez(
                path, x=x, k=k, flavors=flavors,
                components=np.asarray(GRID_COMPONENTS),
                scenarios=scenarios, values=payload,
                scale_gev=np.asarray(5.0),
            )
            model = EvolvedQuarkGridModel(
                self.proton, path, "proton", "positive"
            )
            result = model.tmd_values(
                flavor=2, x=0.2, k_x_gev=0.25, k_y_gev=0.0,
                scale_gev=5.0, gauge_link=GaugeLink("+", "+"),
            )
            for index, name in enumerate(GRID_COMPONENTS):
                expected_scenario = 2 if name == "h1Tperp" else 1
                self.assertEqual(result[name], index + expected_scenario + 1)


if __name__ == "__main__":
    unittest.main()
