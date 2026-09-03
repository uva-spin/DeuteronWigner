import unittest

import numpy as np

from deuteron_wigner.gluon_tmd_matching import (
    CA,
    CF,
    GluonTMDMatchingConfig,
    LargeBProfile,
    MatchedGluonTMD,
)


class MatchedGluonTMDTests(unittest.TestCase):
    @staticmethod
    def gluon(x, scale):
        return 2.0

    @staticmethod
    def helicity(x, scale):
        return 0.5

    @staticmethod
    def singlet(x, scale):
        return 3.0

    @staticmethod
    def alpha_s(scale):
        return 0.24

    def setUp(self):
        self.model = MatchedGluonTMD(
            self.gluon,
            self.alpha_s,
            helicity_gluon_pdf=self.helicity,
            quark_singlet_pdf=self.singlet,
        )

    def test_collinear_boundary_at_zero_b(self):
        values = self.model.values(0.2, 0.0, 2.0)
        self.assertEqual(values.f1, 2.0)
        self.assertEqual(values.g1, 0.5)
        self.assertEqual(values.profile_factor, 1.0)
        self.assertEqual(values.b_star, 0.0)

    def test_one_loop_linear_matching_for_constant_pdfs(self):
        x = 0.2
        convolution = 1.0 / x + np.log(x) - 1.0
        expected = (
            -self.alpha_s(2.0)
            / (4.0 * np.pi)
            * convolution
            / 4.0
            * (2.0 * CA + 3.0 * CF)
        )
        self.assertAlmostEqual(
            self.model.perturbative_values(x, 0.3, 2.0).h1perp,
            expected,
            places=11,
        )

    def test_linear_matching_vanishes_at_endpoint(self):
        self.assertEqual(
            self.model.perturbative_values(1.0, 0.2, 2.0).h1perp, 0.0
        )

    def test_profile_family_is_explicit_and_ordered(self):
        factors = []
        for profile in (
            LargeBProfile.NARROW,
            LargeBProfile.CENTRAL,
            LargeBProfile.BROAD,
        ):
            model = MatchedGluonTMD(
                self.gluon,
                self.alpha_s,
                config=GluonTMDMatchingConfig(profile=profile),
            )
            factors.append(model.profile_factor(2.0))
        self.assertGreater(factors[0], factors[1])
        self.assertGreater(factors[1], factors[2])

    def test_bstar_is_bounded_and_has_small_b_limit(self):
        self.assertAlmostEqual(self.model.b_star(1.0e-6), 1.0e-6)
        self.assertLess(self.model.b_star(100.0), self.model.config.b_max)

    def test_metadata_exposes_approximations(self):
        metadata = self.model.metadata
        self.assertFalse(metadata["production_ready"])
        self.assertTrue(metadata["quark_singlet_channel"])
        self.assertEqual(
            metadata["matching_accuracy"]["h1perp"],
            "one-loop first nonzero",
        )

    def test_gluon_only_approximation_is_labeled(self):
        model = MatchedGluonTMD(self.gluon, self.alpha_s)
        self.assertFalse(model.metadata["quark_singlet_channel"])

    def test_invalid_points_and_configuration_are_rejected(self):
        for args in ((0.0, 0.0, 2.0), (0.2, -0.1, 2.0), (0.2, 0.1, 0.0)):
            with self.assertRaises(ValueError):
                self.model.values(*args)
        with self.assertRaises(ValueError):
            GluonTMDMatchingConfig(b_max=0.0)
        with self.assertRaises(ValueError):
            GluonTMDMatchingConfig(
                g2_narrow=0.3, g2_central=0.2, g2_broad=0.4
            )
        with self.assertRaises(ValueError):
            GluonTMDMatchingConfig(convolution_order=8)


if __name__ == "__main__":
    unittest.main()
