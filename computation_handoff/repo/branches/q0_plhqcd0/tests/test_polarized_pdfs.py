import unittest

from deuteron_wigner.pdfs import PolarizedLHAPDFProvider


class PolarizedPDFTests(unittest.TestCase):
    def test_project_local_bdssv24_central_member(self):
        provider = PolarizedLHAPDFProvider()
        self.assertLessEqual(provider.q_min, 2.0)
        self.assertGreaterEqual(provider.q_max, 2.0)
        self.assertAlmostEqual(provider.gluon(0.1, 2.0), 0.8274285011592781)

    def test_domain_validation(self):
        provider = PolarizedLHAPDFProvider()
        with self.assertRaises(ValueError):
            provider.gluon(0.0, 2.0)
        with self.assertRaises(ValueError):
            provider.gluon(0.1, 0.0)


if __name__ == "__main__":
    unittest.main()
