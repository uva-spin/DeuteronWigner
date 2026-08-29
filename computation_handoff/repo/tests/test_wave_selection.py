import unittest

from deuteron_wigner.wavefunctions.selection import (
    WAVE_FUNCTION_CHOICES,
    select_momentum_wave_function,
)


class WaveSelectionTests(unittest.TestCase):
    def test_all_named_wave_functions_have_normalized_forward_radials(self):
        for label in WAVE_FUNCTION_CHOICES:
            selected = select_momentum_wave_function(label)
            u, w = selected.radial(0.5)
            self.assertTrue(abs(u) + abs(w) > 0.0)

    def test_tabulated_domains_are_enforced(self):
        selected = select_momentum_wave_function("nvia")
        selected.validate_k_max(20.0)
        with self.assertRaises(ValueError):
            selected.validate_k_max(20.1)


if __name__ == "__main__":
    unittest.main()
