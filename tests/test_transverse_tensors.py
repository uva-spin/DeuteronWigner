import unittest

import numpy as np

from deuteron_wigner.transverse_tensors import (
    DefiniteRankProjector,
    contract_with_vector,
    symmetric_traceless_2d,
)


class TransverseTensorTests(unittest.TestCase):
    def test_rank_two_matches_explicit_definition(self):
        k = np.array([0.7, -0.2])
        expected = np.outer(k, k) - 0.5 * np.dot(k, k) * np.eye(2)
        np.testing.assert_allclose(symmetric_traceless_2d(k, 2), expected)

    def test_ranks_two_through_four_are_symmetric_and_traceless(self):
        for rank in (2, 3, 4):
            tensor = symmetric_traceless_2d((0.4, 0.9), rank)
            np.testing.assert_allclose(
                tensor, np.swapaxes(tensor, 0, rank - 1), atol=1e-15
            )
            np.testing.assert_allclose(
                np.trace(tensor, axis1=0, axis2=1), 0.0, atol=1e-15
            )

    def test_harmonic_contraction_identity(self):
        k_radius, k_angle = 0.8, 0.37
        v_radius, v_angle = 1.3, -0.41
        k = k_radius * np.array([np.cos(k_angle), np.sin(k_angle)])
        v = v_radius * np.array([np.cos(v_angle), np.sin(v_angle)])
        for rank in (1, 2, 3, 4):
            actual = contract_with_vector(
                symmetric_traceless_2d(k, rank), v
            )
            expected = (
                k_radius**rank * v_radius**rank
                * np.cos(rank * (k_angle - v_angle))
                / 2.0 ** (rank - 1)
            )
            self.assertAlmostEqual(actual, expected, places=14)

    def test_projector_recovers_and_reconstructs_coefficient(self):
        basis = symmetric_traceless_2d((0.3, 0.8), 3)
        projector = DefiniteRankProjector(basis)
        tensor = 2.7 * basis
        coefficient = projector.coefficient(tensor)
        self.assertAlmostEqual(coefficient, 2.7)
        np.testing.assert_allclose(projector.reconstruct(coefficient), tensor)

    def test_invalid_rank_and_shape_are_rejected(self):
        with self.assertRaises(ValueError):
            symmetric_traceless_2d((1.0, 0.0), -1)
        with self.assertRaises(ValueError):
            DefiniteRankProjector(np.eye(3))


if __name__ == "__main__":
    unittest.main()
