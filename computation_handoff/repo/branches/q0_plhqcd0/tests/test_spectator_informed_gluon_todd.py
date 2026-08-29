import numpy as np
import pytest

from deuteron_wigner.gluon_correlator import Spin1GluonCorrelator
from deuteron_wigner.gluon_todd import (
    GLUON_TODD_RANKS,
    GluonColorStructure,
    SpectatorInformedGluonTOdd,
    add_gluon_todd_with_positivity,
    gluon_link_sign,
)
from deuteron_wigner.gtmd import GaugeLink


def test_color_classes_have_correct_links_and_exact_reversal():
    assert gluon_link_sign(
        GluonColorStructure.F_TYPE, GaugeLink("+", "+")
    ) == 1
    assert gluon_link_sign(
        GluonColorStructure.F_TYPE, GaugeLink("-", "-")
    ) == -1
    assert gluon_link_sign(
        GluonColorStructure.D_TYPE, GaugeLink("+", "-")
    ) == 1
    assert gluon_link_sign(
        GluonColorStructure.D_TYPE, GaugeLink("-", "+")
    ) == -1
    with pytest.raises(ValueError):
        gluon_link_sign(
            GluonColorStructure.D_TYPE, GaugeLink("+", "+")
        )


def test_full_vertex_hierarchy_node_and_independent_color_strength():
    model = SpectatorInformedGluonTOdd()
    low = model.future_values(
        GluonColorStructure.F_TYPE, f1_gev2=2.0, k_gev=0.2
    )
    assert set(low) == set(GLUON_TODD_RANKS)
    assert abs(low["h1"]) > abs(low["f1Tperp"])
    assert abs(low["h1Tperp"]) < abs(low["h1Lperp"])
    below = model.future_values(
        GluonColorStructure.F_TYPE, f1_gev2=2.0, k_gev=0.30
    )["h1Lperp"]
    above = model.future_values(
        GluonColorStructure.F_TYPE, f1_gev2=2.0, k_gev=0.34
    )["h1Lperp"]
    assert below * above < 0.0
    d_model = SpectatorInformedGluonTOdd(d_type_relative_coupling=0.73)
    f = d_model.future_values(
        GluonColorStructure.F_TYPE, f1_gev2=2.0, k_gev=0.2
    )
    d = d_model.future_values(
        GluonColorStructure.D_TYPE, f1_gev2=2.0, k_gev=0.2
    )
    assert d["f1Tperp"] / f["f1Tperp"] == pytest.approx(0.73)


def test_tensor_functions_require_sd_mixing_and_all_six_are_nonzero():
    full = SpectatorInformedGluonTOdd()
    pure_s = SpectatorInformedGluonTOdd(d_state_probability=0.0)
    values = full.future_values(
        GluonColorStructure.F_TYPE, f1_gev2=1.0, k_gev=0.4
    )
    assert all(values[name] != 0.0 for name in GLUON_TODD_RANKS)
    values_s = pure_s.future_values(
        GluonColorStructure.F_TYPE, f1_gev2=1.0, k_gev=0.4
    )
    assert values_s["g1LT"] == 0.0
    assert values_s["g1TT"] == 0.0


def test_full_density_positivity_cap_preserves_relative_amplitudes():
    base = Spin1GluonCorrelator(
        np.eye(6).reshape(3, 2, 3, 2).transpose(0, 2, 1, 3)
    )
    model = SpectatorInformedGluonTOdd(strength=1000.0)
    raw = model.values(
        GluonColorStructure.F_TYPE,
        f1_gev2=1.0,
        k_gev=0.5,
        gauge_link=GaugeLink("+", "+"),
    )
    result, scale, final = add_gluon_todd_with_positivity(
        base, momentum=(0.5, 0.0), radial_values=raw
    )
    assert 0.0 < scale < 1.0
    assert result.minimum_positivity_eigenvalue() >= -1e-10
    assert final["g1LT"] / final["f1Tperp"] == pytest.approx(
        raw["g1LT"] / raw["f1Tperp"]
    )
