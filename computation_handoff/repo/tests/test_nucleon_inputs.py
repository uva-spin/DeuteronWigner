import unittest

import numpy as np
from scipy.integrate import quad

from deuteron_wigner.gtmd import GaugeLink

from deuteron_wigner.nucleon_inputs import (
    ChargeSymmetryBreakingInput,
    FittedMomentumTMDInput,
    NucleonInputConfiguration,
    build_nucleon_quark_models,
)
from deuteron_wigner.provenance import (
    ComponentProvenance,
    EvidenceClass,
    Mechanism,
    ValidityDomain,
)


class FakePDF:
    def proton(self, flavor, x, scale):
        return {2: 4.0, 1: 2.0, -2: 0.4, -1: 0.7}[flavor] * (1 - x)

    def neutron(self, flavor, x, scale):
        mapping = {2: 1, 1: 2, -2: -1, -1: -2}
        return self.proton(mapping[flavor], x, scale)


class FakePolarized(FakePDF):
    def proton(self, flavor, x, scale):
        return {2: 1.2, 1: -0.4, -2: 0.0, -1: -0.1}[flavor] * (1 - x)


class NucleonInputTests(unittest.TestCase):
    def test_proton_neutron_flavor_resolution_and_isospin_limit(self):
        proton, neutron = build_nucleon_quark_models(FakePDF(), FakePolarized())
        link = __import__(
            "deuteron_wigner.gtmd", fromlist=["GaugeLink"]
        ).GaugeLink("+", "+")
        common = dict(x=0.2, k_x_gev=0.1, k_y_gev=0.0, scale_gev=3.0, gauge_link=link)
        up = proton.tmd_values(flavor=2, **common)["f1"]
        dp = proton.tmd_values(flavor=1, **common)["f1"]
        un = neutron.tmd_values(flavor=2, **common)["f1"]
        dn = neutron.tmd_values(flavor=1, **common)["f1"]
        self.assertNotEqual(up, dp)
        self.assertNotEqual(un, dn)
        # The inclusive equality emerges only after the separately retained
        # proton and neutron pieces are assembled in the charge-symmetric limit.
        self.assertAlmostEqual(up + un, dp + dn)
        self.assertEqual(
            proton.auxiliary_provenance[0].mechanism,
            Mechanism.ISOSPIN_BREAKING,
        )
        self.assertEqual(
            proton.auxiliary_provenance[0].evidence, EvidenceClass.EXACT
        )

    def test_controlled_csb_breaks_inclusive_isospin_without_flavor_collapse(self):
        provenance = ComponentProvenance(
            name="synthetic flavor-resolved CSB validation",
            evidence=EvidenceClass.MODEL,
            mechanism=Mechanism.ISOSPIN_BREAKING,
            sources=("unit-test controlled response",),
            assumptions=("neutron u f1 amplitude shifted by 2%",),
            validity=ValidityDomain(0.01, 0.8, 2.0, 10.0, 1.0),
            uncertainty_kind="synthetic validation parameter",
            replaceable_interface="ChargeSymmetryBreakingInput",
        )
        csb = ChargeSymmetryBreakingInput(
            response=lambda nucleon, flavor, name, x, q: (
                0.02 if (nucleon, flavor, name) == ("neutron", 2, "f1") else 0.0
            ),
            provenance=provenance,
        )
        proton, neutron = build_nucleon_quark_models(
            FakePDF(), FakePolarized(), charge_symmetry_breaking=csb
        )
        common = dict(
            x=0.2, k_x_gev=0.1, k_y_gev=0.0, scale_gev=3.0,
            gauge_link=GaugeLink("+", "+"),
        )
        up = proton.tmd_values(flavor=2, **common)["f1"]
        dp = proton.tmd_values(flavor=1, **common)["f1"]
        un = neutron.tmd_values(flavor=2, **common)["f1"]
        dn = neutron.tmd_values(flavor=1, **common)["f1"]
        self.assertNotAlmostEqual(up + un, dp + dn)
        self.assertNotEqual(up, dp)
        self.assertNotEqual(un, dn)
        self.assertEqual(neutron.auxiliary_provenance, (provenance,))

    def test_csb_contract_rejects_hidden_nonzero_exact_limit(self):
        exact = ChargeSymmetryBreakingInput.exact_isospin_limit()
        object.__setattr__(
            exact, "response",
            lambda nucleon, flavor, name, x, q: 0.01,
        )
        with self.assertRaisesRegex(ValueError, "exact-zero"):
            exact.relative_correction("neutron", 2, "f1", 0.2, 3.0)

    def test_csb_response_is_inactive_outside_declared_domain(self):
        provenance = ComponentProvenance(
            name="bounded synthetic CSB",
            evidence=EvidenceClass.MODEL,
            mechanism=Mechanism.ISOSPIN_BREAKING,
            sources=("unit-test controlled response",),
            assumptions=("test-only",),
            validity=ValidityDomain(0.1, 0.3, 2.0, 4.0),
            uncertainty_kind="synthetic validation parameter",
            replaceable_interface="ChargeSymmetryBreakingInput",
        )
        csb = ChargeSymmetryBreakingInput(
            response=lambda nucleon, flavor, name, x, q: 0.5,
            provenance=provenance,
        )
        self.assertEqual(
            csb.relative_correction("neutron", 2, "f1", 0.05, 3.0), 0.0
        )
        self.assertEqual(
            csb.relative_correction("neutron", 2, "f1", 0.2, 5.0), 0.0
        )
        self.assertEqual(
            csb.relative_correction("neutron", 2, "f1", 0.2, 3.0), 0.5
        )

    def test_configuration_rejects_implicit_t_odd_model(self):
        config = NucleonInputConfiguration.flavor_resolved_baseline()
        config = NucleonInputConfiguration(
            **{**config.__dict__, "t_odd_boundary": "untraced_phase"}
        )
        with self.assertRaises(ValueError):
            build_nucleon_quark_models(FakePDF(), FakePolarized(), config)

    def test_independent_sivers_and_boer_mulders_inputs_reverse_once(self):
        def fitted(name, scale):
            return FittedMomentumTMDInput(
                response=lambda nucleon, flavor, x, k, q: (
                    scale
                    * (1.0 if nucleon == "proton" else 2.0)
                    * flavor
                    * x
                    * np.exp(-k * k)
                ),
                provenance=ComponentProvenance(
                    name=name,
                    evidence=EvidenceClass.MODEL,
                    mechanism=Mechanism.NUCLEON_IMPULSE,
                    sources=("synthetic independent T-odd fixture",),
                    assumptions=("future staple reference",),
                    validity=ValidityDomain(0.01, 0.8, 2.0, 10.0, 1.5),
                    uncertainty_kind="synthetic parameter sensitivity",
                    replaceable_interface="FittedMomentumTMDInput",
                ),
                process_reference="SIDIS future-pointing gauge link",
            )

        proton, neutron = build_nucleon_quark_models(
            FakePDF(),
            FakePolarized(),
            sivers_input=fitted("Sivers", 1.0),
            boer_mulders_input=fitted("Boer--Mulders", -3.0),
        )
        future = dict(
            flavor=2, x=0.2, k_x_gev=0.3, k_y_gev=0.1,
            scale_gev=5.0, gauge_link=GaugeLink("+", "+"),
        )
        past = {**future, "gauge_link": GaugeLink("-", "-")}
        for model in (proton, neutron):
            future_values = model.tmd_values(**future)
            past_values = model.tmd_values(**past)
            self.assertNotEqual(future_values["f1Tperp"], 0.0)
            self.assertNotEqual(future_values["h1perp"], 0.0)
            self.assertNotEqual(
                future_values["f1Tperp"], future_values["h1perp"]
            )
            self.assertAlmostEqual(
                past_values["f1Tperp"], -future_values["f1Tperp"]
            )
            self.assertAlmostEqual(
                past_values["h1perp"], -future_values["h1perp"]
            )

    def test_csb_is_applied_to_fitted_momentum_tmds(self):
        provenance = ComponentProvenance(
            name="momentum TMD CSB",
            evidence=EvidenceClass.MODEL,
            mechanism=Mechanism.ISOSPIN_BREAKING,
            sources=("synthetic fixture",),
            assumptions=("10 percent neutron Boer--Mulders shift",),
            validity=ValidityDomain(0.01, 0.8, 2.0, 10.0, 1.5),
            uncertainty_kind="synthetic parameter",
            replaceable_interface="ChargeSymmetryBreakingInput",
        )
        csb = ChargeSymmetryBreakingInput(
            response=lambda nucleon, flavor, name, x, q: (
                0.1 if nucleon == "neutron" and name == "h1perp" else 0.0
            ),
            provenance=provenance,
        )
        fitted = FittedMomentumTMDInput(
            response=lambda nucleon, flavor, x, k, q: 2.0,
            provenance=ComponentProvenance(
                name="synthetic Boer--Mulders",
                evidence=EvidenceClass.MODEL,
                mechanism=Mechanism.NUCLEON_IMPULSE,
                sources=("synthetic fixture",),
                assumptions=("constant fixture",),
                validity=ValidityDomain(0.01, 0.8, 2.0, 10.0, 1.5),
                uncertainty_kind="synthetic parameter",
                replaceable_interface="FittedMomentumTMDInput",
            ),
            process_reference="SIDIS",
        )
        proton, neutron = build_nucleon_quark_models(
            FakePDF(), FakePolarized(),
            charge_symmetry_breaking=csb,
            boer_mulders_input=fitted,
        )
        common = dict(
            flavor=2, x=0.2, k_x_gev=0.2, k_y_gev=0.0,
            scale_gev=5.0, gauge_link=GaugeLink("+", "+"),
        )
        self.assertEqual(proton.tmd_values(**common)["h1perp"], 2.0)
        self.assertAlmostEqual(neutron.tmd_values(**common)["h1perp"], 2.2)

    def test_complete_joint_spin_density_is_positive_over_support_grid(self):
        proton, neutron = build_nucleon_quark_models(FakePDF(), FakePolarized())
        minimum = np.inf
        for model in (proton, neutron):
            for flavor in (2, 1, -2, -1):
                for x in (0.01, 0.1, 0.4, 0.8):
                    for k_x, k_y in ((0.0, 0.0), (0.2, 0.1), (0.7, -0.3)):
                        correlator = model.correlator(
                            flavor=flavor, x=x,
                            k_x_gev=k_x, k_y_gev=k_y,
                            delta_x_gev=0.0, delta_y_gev=0.0,
                            scale_gev=5.0, gauge_link=GaugeLink("+", "+"),
                        )
                        minimum = min(
                            minimum,
                            correlator.minimum_positivity_eigenvalue(),
                        )
        self.assertGreaterEqual(minimum, -1.0e-12)

    def test_transversity_reproduces_configured_reference_tensor_charges(self):
        config = NucleonInputConfiguration.flavor_resolved_baseline()
        proton, _ = build_nucleon_quark_models(
            FakePDF(), FakePolarized(), config
        )
        h1 = proton.components["h1"].value
        for flavor in (2, 1, -2, -1):
            moment = quad(
                lambda x: h1(flavor, x, config.transversity_reference_scale_gev),
                1.0e-5, 1.0, epsabs=1.0e-7, epsrel=1.0e-6,
            )[0]
            self.assertAlmostEqual(
                moment, config.transversity_tensor_charges[flavor], places=5
            )

    def test_pretzelosity_sensitivity_saturates_declared_moment_fraction(self):
        baseline = NucleonInputConfiguration.flavor_resolved_baseline()
        for fraction in (-0.25, 0.25):
            config = baseline.with_pretzelosity_fraction(fraction)
            proton, neutron = build_nucleon_quark_models(
                FakePDF(), FakePolarized(), config
            )
            for model, nucleon in ((proton, "proton"), (neutron, "neutron")):
                for flavor in (2, 1, -2, -1):
                    width = model.components["h1Tperp"].width(flavor)
                    amplitude = model.components["h1Tperp"].value(
                        flavor, 0.2, 5.0
                    )
                    first_moment = (
                        width * amplitude / (2.0 * model.nucleon_mass_gev**2)
                    )
                    f1 = model.components["f1"].value(flavor, 0.2, 5.0)
                    g1 = model.components["g1"].value(flavor, 0.2, 5.0)
                    ceiling = 0.5 * max(0.0, f1 - g1)
                    self.assertAlmostEqual(
                        first_moment, fraction * ceiling, places=12
                    )
            self.assertNotEqual(
                proton.components["h1Tperp"].value(2, 0.2, 5.0),
                proton.components["h1Tperp"].value(1, 0.2, 5.0),
            )


if __name__ == "__main__":
    unittest.main()
