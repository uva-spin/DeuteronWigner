import numpy as np

from deuteron_wigner.hidden_color import MillerSixQuarkB1, MillerSixQuarkParameters


def test_miller_table_values():
    model = MillerSixQuarkB1()
    # Table I values are printed in units of 1e-2 and rounded to two decimals.
    expected = {0.128: 0.01, 0.248: 0.41, 0.452: -0.38}
    for x, table_units in expected.items():
        assert np.isclose(100.0 * model.b1(x), table_units, atol=0.01)


def test_probability_is_explicit_linear_switch():
    central = MillerSixQuarkB1()
    zero = MillerSixQuarkB1(MillerSixQuarkParameters(probability_amplitude_product=0.0))
    doubled = MillerSixQuarkB1(
        MillerSixQuarkParameters(probability_amplitude_product=0.003)
    )
    assert zero.b1(0.452) == 0.0
    assert np.isclose(doubled.b1(0.452), 2.0 * central.b1(0.452))


def test_support_and_valence_tensor_sum_rule():
    model = MillerSixQuarkB1()
    assert model.b1(0.0) == 0.0
    assert model.b1(2.0) == 0.0
    assert abs(model.integral_sum_rule()) < 1.0e-8


def test_variants_are_named_and_change_shape():
    model = MillerSixQuarkB1()
    variants = model.parameter_variants()
    assert set(variants) == {
        "radius_minus_10pct",
        "radius_plus_10pct",
        "mass_minus_10pct",
        "mass_plus_10pct",
    }
    assert any(not np.isclose(v.b1(0.3), model.b1(0.3)) for v in variants.values())
