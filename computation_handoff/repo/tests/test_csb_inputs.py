import unittest

from deuteron_wigner.csb_inputs import MSHT20QEDChargeSymmetryBreaking
from deuteron_wigner.evolved_quark_grid import EvolvedQuarkGridModel
from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.nucleon_inputs import build_nucleon_quark_models
from test_nucleon_inputs import FakePDF, FakePolarized


class MSHT20QEDCSBTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.model = MSHT20QEDChargeSymmetryBreaking()
        cls.input = cls.model.as_input()

    def test_central_is_flavor_resolved_and_only_changes_neutron_f1(self):
        corrections = {
            flavor: self.input.relative_correction(
                "neutron", flavor, "f1", 0.1, 5.0
            )
            for flavor in (2, 1, -2, -1)
        }
        self.assertGreater(max(abs(value) for value in corrections.values()), 1.0e-5)
        self.assertNotEqual(corrections[2], corrections[1])
        self.assertEqual(
            self.input.relative_correction("proton", 2, "f1", 0.1, 5.0),
            0.0,
        )
        self.assertEqual(
            self.input.relative_correction("neutron", 2, "g1", 0.1, 5.0),
            0.0,
        )

    def test_paired_hessian_uncertainty_is_finite(self):
        uncertainty = self.input.relative_uncertainty(
            "neutron", 2, "f1", 0.1, 5.0
        )
        self.assertGreater(uncertainty, 0.0)
        self.assertLess(uncertainty, 0.2)
        direct = sum(
            (
                (
                    self.model.member_response(2 * pair + 1, 2, 0.1, 5.0)
                    - self.model.member_response(2 * pair + 2, 2, 0.1, 5.0)
                )
                / 2.0
            )
            ** 2
            for pair in range(self.model.n_eigenvector_pairs)
        ) ** 0.5
        self.assertAlmostEqual(uncertainty, direct)
        with self.assertRaises(ValueError):
            self.model.member_response(77, 2, 0.1, 5.0)

    def test_validity_contract_disables_extrapolation(self):
        self.assertEqual(
            self.input.relative_correction("neutron", 2, "f1", 0.5, 5.0),
            0.0,
        )
        self.assertEqual(
            self.input.relative_uncertainty("neutron", 2, "f1", 0.1, 0.9),
            0.0,
        )

    def test_csb_is_applied_after_evolved_grid_replacement(self):
        proton, neutron = build_nucleon_quark_models(FakePDF(), FakePolarized())
        common = dict(
            grid_path="data/processed/evolved_quark_tmd_Q5.npz",
            nucleon="neutron",
        )
        exact = EvolvedQuarkGridModel(neutron, **common)
        broken = EvolvedQuarkGridModel(
            neutron, **common, charge_symmetry_breaking=self.input
        )
        arguments = dict(
            flavor=2,
            x=0.1,
            k_x_gev=0.2,
            k_y_gev=0.0,
            scale_gev=5.0,
            gauge_link=GaugeLink("+", "+"),
        )
        exact_values = exact.tmd_values(**arguments)
        broken_values = broken.tmd_values(**arguments)
        correction = self.input.relative_correction(
            "neutron", 2, "f1", 0.1, 5.0
        )
        self.assertAlmostEqual(
            broken_values["f1"], exact_values["f1"] * (1.0 + correction)
        )
        for name in ("g1", "h1", "g1T", "h1Lperp", "h1Tperp"):
            self.assertEqual(broken_values[name], exact_values[name])


if __name__ == "__main__":
    unittest.main()
