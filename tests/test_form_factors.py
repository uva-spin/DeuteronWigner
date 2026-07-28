import unittest

import numpy as np

from deuteron_wigner.form_factors import (
    charge_impulse_from_body,
    deuteron_impulse_form_factors,
    elastic_observables,
    load_av18_electromagnetic_tables,
)


class AV18ElectromagneticTableTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tables = load_av18_electromagnetic_tables(
            "data/raw/av18/fdeut.av18"
        )

    def test_static_normalizations(self):
        self.assertAlmostEqual(self.tables.ges[0], 0.5)
        self.assertAlmostEqual(self.tables.gms[0], 0.43990235)
        self.assertAlmostEqual(self.tables.ce[0], 0.9999981148)
        self.assertAlmostEqual(self.tables.gc[0], 0.9999981148)

    def test_tabulated_charge_relation(self):
        predicted = charge_impulse_from_body(
            body_overlap=self.tables.ce, ges=self.tables.ges
        )
        np.testing.assert_allclose(predicted, self.tables.gc, rtol=3e-9, atol=2e-10)

    def test_all_impulse_form_factors_and_observables(self):
        gc, gm, gq = deuteron_impulse_form_factors(
            ges=self.tables.ges,
            gms=self.tables.gms,
            ce=self.tables.ce,
            cl=self.tables.cl,
            cs=self.tables.cs,
            cq=self.tables.cq,
            deuteron_mass_mev=self.tables.deuteron_mass_mev,
            reduced_mass_mev=self.tables.reduced_mass_mev,
        )
        np.testing.assert_allclose(gc, self.tables.gc, rtol=3e-9, atol=2e-10)
        np.testing.assert_allclose(gm, self.tables.gm, rtol=1e-8, atol=2e-10)
        np.testing.assert_allclose(gq, self.tables.gq, rtol=3e-9, atol=2e-9)
        structure_a, structure_b, t20 = elastic_observables(
            q_fm=self.tables.q_deuteron,
            gc=gc,
            gm=gm,
            gq=gq,
            deuteron_mass_mev=self.tables.deuteron_mass_mev,
        )
        np.testing.assert_allclose(
            structure_a, self.tables.structure_a, rtol=1e-7, atol=1e-8
        )
        np.testing.assert_allclose(
            structure_b, self.tables.structure_b, rtol=1e-7, atol=1e-8
        )
        np.testing.assert_allclose(t20, self.tables.t20_70deg, rtol=5e-6, atol=3e-6)

    def test_interpolation_and_no_extrapolation(self):
        self.assertGreater(self.tables.charge_form_factor(0.55), 0.0)
        with self.assertRaises(ValueError):
            self.tables.charge_form_factor(21.0)


if __name__ == "__main__":
    unittest.main()
