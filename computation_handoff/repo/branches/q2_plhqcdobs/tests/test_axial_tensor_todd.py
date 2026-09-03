import numpy as np
import pytest

from deuteron_wigner.axial_tensor_todd import (
    AxialTensorTOddScenario,
    EikonalAxialTensorModel,
    EikonalKernelParameters,
    Spin1QuarkNuclearWilsonLine,
    add_axial_tensor_todd,
    axial_tensor_todd_scenarios,
)
from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.quark_correlator import (
    SPIN1_QUARK_TMD_NAMES,
    compose_spin1_quark_correlator,
    project_spin1_quark_correlator,
)


def positive_base(k=0.4):
    values = {name: 0.0 for name in SPIN1_QUARK_TMD_NAMES}
    values["f1"] = 2.0
    return compose_spin1_quark_correlator((k, 0.0), 1.87561294257, values)


def test_phase_scenarios_are_flavor_operator_and_member_resolved():
    scenarios = axial_tensor_todd_scenarios()
    assert [item.label for item in scenarios] == [
        "phase_low", "phase_central", "phase_high"
    ]
    values = {
        flavor: scenarios[1].future_values(
            flavor, f1_gev2=2.0, k_gev=0.4
        )
        for flavor in (2, 1, -2, -1)
    }
    assert len(set(values.values())) == 4
    assert all(g1lt != g1tt for g1lt, g1tt in values.values())


def test_phase_scenario_validation_refuses_missing_flavor():
    with pytest.raises(ValueError, match="u,d,ubar,dbar"):
        AxialTensorTOddScenario("bad", {2: 0.1}, {2: 0.2})


def test_full_density_cap_preserves_hermiticity_positivity_and_link_reversal():
    base = positive_base()
    future = add_axial_tensor_todd(
        base, momentum=(0.4, 0.0), g1lt_future=20.0, g1tt_future=-15.0,
        gauge_link=GaugeLink("+", "+"),
    )
    past = add_axial_tensor_todd(
        base, momentum=(0.4, 0.0), g1lt_future=20.0, g1tt_future=-15.0,
        gauge_link=GaugeLink("-", "-"),
    )
    assert 0.0 < future[1] < 1.0
    assert future[0].is_target_hermitian()
    assert future[0].minimum_positivity_eigenvalue() >= -1e-12
    assert past[2] == pytest.approx(-future[2])
    assert past[3] == pytest.approx(-future[3])
    fproj = project_spin1_quark_correlator(future[0], (0.4, 0), 1.87561294257)
    pproj = project_spin1_quark_correlator(past[0], (0.4, 0), 1.87561294257)
    assert pproj["g1LT"] == pytest.approx(-fproj["g1LT"], abs=1e-12)
    assert pproj["g1TT"] == pytest.approx(-fproj["g1TT"], abs=1e-12)


def test_mixed_link_and_nonpositive_base_fail_closed():
    with pytest.raises(ValueError, match="mixed links"):
        add_axial_tensor_todd(
            positive_base(), momentum=(0.4, 0.0),
            g1lt_future=0.1, g1tt_future=0.1,
            gauge_link=GaugeLink("+", "-"),
        )
    bad_values = {name: 0.0 for name in SPIN1_QUARK_TMD_NAMES}
    bad_values["f1"] = -1.0
    bad = compose_spin1_quark_correlator((0.4, 0), 1.87561294257, bad_values)
    with pytest.raises(ValueError, match="outside the positivity"):
        add_axial_tensor_todd(
            bad, momentum=(0.4, 0), g1lt_future=0.1, g1tt_future=0.1,
            gauge_link=GaugeLink("+", "+"),
        )


def test_eikonal_rescattering_generates_both_ranks_and_phase_zero_limit():
    model = EikonalAxialTensorModel()
    g1lt, g1tt = model.future_values(
        2, f1_gev2=2.0, k_gev=0.45, width_gev2=0.30
    )
    assert g1lt != 0.0
    assert g1tt != 0.0
    disabled = EikonalAxialTensorModel(
        p_odd={2: 0.0, 1: 0.0, -2: 0.0, -1: 0.0}
    )
    assert disabled.future_values(
        2, f1_gev2=2.0, k_gev=0.45, width_gev2=0.30
    ) == (0.0, 0.0)
    pure_s = EikonalAxialTensorModel(d_state_probability=0.0)
    assert pure_s.future_values(
        2, f1_gev2=2.0, k_gev=0.45, width_gev2=0.30
    ) == (0.0, 0.0)


def test_eikonal_quadrature_converges():
    coarse = EikonalAxialTensorModel(
        kernel=EikonalKernelParameters(n_q=40, n_phi=48)
    )
    fine = EikonalAxialTensorModel(
        kernel=EikonalKernelParameters(n_q=64, n_phi=80)
    )
    for left, right in zip(
        coarse.future_values(
            2, f1_gev2=2.0, k_gev=0.55, width_gev2=0.30
        ),
        fine.future_values(
            2, f1_gev2=2.0, k_gev=0.55, width_gev2=0.30
        ),
    ):
        assert left == pytest.approx(right, rel=2e-5, abs=1e-12)


def test_axial_tensor_coefficients_are_rotation_covariant():
    base_a = positive_base()
    values = {name: 0.0 for name in SPIN1_QUARK_TMD_NAMES}
    values["f1"] = 2.0
    momentum_b = (0.4 / np.sqrt(2.0), 0.4 / np.sqrt(2.0))
    base_b = compose_spin1_quark_correlator(
        momentum_b, 1.87561294257, values
    )
    result_a = add_axial_tensor_todd(
        base_a, momentum=(0.4, 0.0), g1lt_future=0.2, g1tt_future=-0.1,
        gauge_link=GaugeLink("+", "+"),
    )[0]
    result_b = add_axial_tensor_todd(
        base_b, momentum=momentum_b, g1lt_future=0.2, g1tt_future=-0.1,
        gauge_link=GaugeLink("+", "+"),
    )[0]
    projected_a = project_spin1_quark_correlator(
        result_a, (0.4, 0.0), 1.87561294257
    )
    projected_b = project_spin1_quark_correlator(
        result_b, momentum_b, 1.87561294257
    )
    assert projected_a["g1LT"] == pytest.approx(projected_b["g1LT"])
    assert projected_a["g1TT"] == pytest.approx(projected_b["g1TT"])


def test_unitary_nuclear_phase_generates_tensor_todd_and_preserves_spectrum():
    values = {name: 0.0 for name in SPIN1_QUARK_TMD_NAMES}
    values.update(f1=2.0, g1=0.5, f1LL=0.1)
    base = compose_spin1_quark_correlator(
        (0.4, 0.0), 1.87561294257, values
    )
    phase = Spin1QuarkNuclearWilsonLine(
        EikonalAxialTensorModel(
            d_state_probability=0.0576, sd_radial_coherence=0.3898,
        ),
        flavor=2,
        gauge_link=GaugeLink("+", "+"),
    )
    unitary = phase.unitary((0.4, 0.0), 0.30)
    result = phase.apply_unitary(base, unitary)
    projected = project_spin1_quark_correlator(
        result, (0.4, 0.0), 1.87561294257
    )
    assert projected["g1LT"] != 0.0
    assert projected["g1TT"] != 0.0
    assert np.allclose(
        np.linalg.eigvalsh(base.quark_target_density_matrix()),
        np.linalg.eigvalsh(result.quark_target_density_matrix()),
    )


def test_unitary_nuclear_phase_reverses_and_has_exact_pure_s_limit():
    outputs = []
    for link in (GaugeLink("+", "+"), GaugeLink("-", "-")):
        phase = Spin1QuarkNuclearWilsonLine(
            EikonalAxialTensorModel(
                d_state_probability=0.0576, sd_radial_coherence=0.3898,
            ),
            flavor=1,
            gauge_link=link,
        )
        result = phase.apply_unitary(
            positive_base(), phase.unitary((0.4, 0.0), 0.30)
        )
        channels = phase.channel_phases(0.4, 0.30)
        lt, tt = phase.phases(0.4, 0.30)
        assert set(channels) == {"S_P", "S_D", "P_P"}
        assert lt == pytest.approx(channels["S_P"])
        assert tt == pytest.approx(channels["S_D"] + channels["P_P"])
        outputs.append(project_spin1_quark_correlator(
            result, (0.4, 0.0), 1.87561294257
        ))
    assert outputs[0]["g1LT"] == pytest.approx(-outputs[1]["g1LT"])
    assert outputs[0]["g1TT"] == pytest.approx(-outputs[1]["g1TT"])
    pure_s = Spin1QuarkNuclearWilsonLine(
        EikonalAxialTensorModel(d_state_probability=0.0),
        flavor=2,
        gauge_link=GaugeLink("+", "+"),
    )
    assert np.array_equal(
        pure_s.unitary((0.4, 0.0), 0.30), np.eye(3)
    )
