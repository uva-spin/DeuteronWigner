import unittest

import numpy as np

from deuteron_wigner.two_body_current import (
    NORFOLK_PRC106_SET_A_DEUTERON_MOMENTS,
    NORFOLK_PRC106_SET_A_ISOSCALAR_LECS,
    _angular_quadratic_coefficients,
    _spin_operators,
    norfolk_n3lo_magnetic_moment,
    regulated_ope_radial_functions,
)
from deuteron_wigner.wavefunctions.norfolk import load_norfolk_coordinate


class NorfolkCurrentTests(unittest.TestCase):
    def test_matched_contact_moments_reproduce_published_values(self):
        published = {
            "nvia": (0.0002, 0.0093),
            "nvib": (0.0005, 0.0211),
            "nviia": (0.0002, 0.0110),
            "nviib": (0.0009, 0.0396),
        }
        for model, (minimal, nonminimal) in published.items():
            wave = load_norfolk_coordinate(f"data/raw/norfolk/fdeut.{model}")
            result = norfolk_n3lo_magnetic_moment(
                wave, model=model, angular_order=8
            )
            self.assertAlmostEqual(
                result["minimal_contact"], minimal, delta=4.0e-5
            )
            self.assertAlmostEqual(
                result["nonminimal_contact"], nonminimal, delta=2.0e-4
            )

    def test_contact_ratio_is_fixed_by_lecs(self):
        wave = load_norfolk_coordinate("data/raw/norfolk/fdeut.nvia")
        result = norfolk_n3lo_magnetic_moment(wave, model="nvia", angular_order=8)
        self.assertAlmostEqual(
            result["minimal_contact"] / result["nonminimal_contact"],
            0.000195 / 0.00999,
            places=12,
        )

    def test_published_regulator_ordering_is_not_yukawa_differentiation(self):
        radius = np.asarray([0.5, 1.0, 2.0])
        published = regulated_ope_radial_functions(
            radius, pion_mass_fm=0.7, r_long_fm=1.2
        )
        differentiated = regulated_ope_radial_functions(
            radius,
            pion_mass_fm=0.7,
            r_long_fm=1.2,
            ordering="differentiate_regulated_yukawa",
        )
        self.assertGreater(np.max(np.abs(published[0] - differentiated[0])), 0.1)
        self.assertGreater(np.max(np.abs(published[1] - differentiated[1])), 0.1)

    def test_partial_wave_reduction_matches_exact_coefficients(self):
        sigma_1, sigma_2 = _spin_operators()
        sigma_sum = sigma_1 + sigma_2
        spin = _angular_quadratic_coefficients(
            lambda _direction: sigma_sum[2], 8
        )
        tensor = _angular_quadratic_coefficients(
            lambda direction: np.einsum("i,iab->ab", direction, sigma_sum)
            * direction[2],
            8,
        )
        np.testing.assert_allclose(spin, (2.0, 0.0, -1.0), atol=2e-14)
        np.testing.assert_allclose(
            tensor,
            (2.0 / 3.0, 2.0 * np.sqrt(2.0) / 3.0, 1.0 / 3.0),
            atol=2e-14,
        )

    def test_ope_i1_i2_decomposition_closes(self):
        wave = load_norfolk_coordinate("data/raw/norfolk/fdeut.nvia")
        result = norfolk_n3lo_magnetic_moment(
            wave,
            model="nvia",
            angular_order=8,
            isoscalar_lecs=NORFOLK_PRC106_SET_A_ISOSCALAR_LECS["nvia"],
        )
        self.assertAlmostEqual(
            result["ope_i1"] + result["ope_i2"], result["ope"], places=13
        )
        self.assertAlmostEqual(
            result["ope_unit_d2"]
            * NORFOLK_PRC106_SET_A_ISOSCALAR_LECS["nvia"][1],
            result["ope"],
            places=13,
        )

    def test_prc106_set_a_constants_and_targets_are_complete(self):
        self.assertEqual(
            set(NORFOLK_PRC106_SET_A_ISOSCALAR_LECS),
            {"nvia", "nvib", "nviia", "nviib"},
        )
        self.assertEqual(
            set(NORFOLK_PRC106_SET_A_DEUTERON_MOMENTS),
            set(NORFOLK_PRC106_SET_A_ISOSCALAR_LECS),
        )
        self.assertEqual(
            NORFOLK_PRC106_SET_A_ISOSCALAR_LECS["nvia"], (0.012, 0.023)
        )
        self.assertEqual(
            NORFOLK_PRC106_SET_A_DEUTERON_MOMENTS["nvib"]["d2"], 0.008
        )


if __name__ == "__main__":
    unittest.main()
