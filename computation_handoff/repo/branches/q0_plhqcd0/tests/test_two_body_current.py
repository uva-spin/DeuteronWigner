import unittest

import numpy as np

from deuteron_wigner.two_body_current import isoscalar_chiral_two_body_current


class TwoBodyCurrentTests(unittest.TestCase):
    def test_current_is_transverse(self):
        q = np.asarray([0.2, -0.1, 0.3])
        current = isoscalar_chiral_two_body_current(
            photon_momentum=q,
            nucleon_1_transfer=np.asarray([0.05, 0.02, 0.1]),
            nucleon_2_transfer=np.asarray([0.15, -0.12, 0.2]),
            d9=0.01,
            l2=0.1,
        )
        np.testing.assert_allclose(np.einsum("i,iab->ab", q, current), 0.0, atol=2e-16)

    def test_current_is_symmetric_under_nucleon_exchange(self):
        q = np.asarray([0.2, -0.1, 0.3])
        q1 = np.asarray([0.05, 0.02, 0.1])
        q2 = q - q1
        direct = isoscalar_chiral_two_body_current(
            photon_momentum=q,
            nucleon_1_transfer=q1,
            nucleon_2_transfer=q2,
            d9=-0.01,
            l2=0.2,
        )
        exchanged = isoscalar_chiral_two_body_current(
            photon_momentum=q,
            nucleon_1_transfer=q2,
            nucleon_2_transfer=q1,
            d9=-0.01,
            l2=0.2,
        )
        swap = np.asarray(
            [[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]],
            dtype=np.complex128,
        )
        np.testing.assert_allclose(
            exchanged,
            np.asarray([swap @ component @ swap for component in direct]),
            atol=2e-15,
        )

    def test_zero_photon_momentum_gives_zero_current(self):
        current = isoscalar_chiral_two_body_current(
            photon_momentum=np.zeros(3),
            nucleon_1_transfer=np.asarray([0.1, 0.0, 0.0]),
            nucleon_2_transfer=np.asarray([-0.1, 0.0, 0.0]),
            d9=0.01,
            l2=0.1,
        )
        np.testing.assert_allclose(current, 0.0, atol=0.0)


if __name__ == "__main__":
    unittest.main()
