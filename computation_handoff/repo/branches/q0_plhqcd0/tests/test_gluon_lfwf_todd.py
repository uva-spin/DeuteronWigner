import numpy as np
import pytest

from deuteron_wigner.gluon_lfwf_todd import (
    GluonWilsonLineKernel,
    LFWFGaugeLinkSpinHalfGluonGTMD,
    Spin1NuclearWilsonLine,
    project_spin_half_gluon_density_psd,
)
from deuteron_wigner.gluon_correlator import (
    compose_spin1_gluon_correlator,
    project_to_allowed_spin1_gluon_basis,
)
from deuteron_wigner.gluon_todd import GluonColorStructure
from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.gtmd_convolution import (
    build_off_forward_component_quadratures,
    convolve_gluon_gtmd_wave_components,
)
from deuteron_wigner.tmd_models import GaussianSpinHalfGluonGTMD
from deuteron_wigner.wavefunctions import RadialWaveFunction


def base(linear=0.35, helicity=0.25):
    return GaussianSpinHalfGluonGTMD(
        unpolarized_pdf=lambda x, q: 2.0 * (1-x),
        helicity_pdf=lambda x, q: helicity * 2.0 * (1-x),
        width=0.30,
        nucleon_mass=0.939,
        linear_fraction=linear,
    )


def model(link=GaugeLink("+", "+"), color=GluonColorStructure.F_TYPE, **kw):
    return LFWFGaugeLinkSpinHalfGluonGTMD(
        t_even_gtmd=base(),
        color=color,
        gauge_link=link,
        nucleon_mass_gev=0.939,
        transverse_width_gev2=0.30,
        **kw,
    )


def test_kernel_harmonics_are_resolved_and_vanish_at_origin():
    kernel = GluonWilsonLineKernel(n_q=32, n_phi=48)
    assert all(kernel.harmonic(0.0, 0.3, rank) == 0.0 for rank in (1, 2, 3))
    values = [kernel.harmonic(0.35, 0.3, rank) for rank in (1, 2, 3)]
    assert all(np.isfinite(values))
    assert values[0] > values[1] > values[2] > 0.0


def test_link_reversal_and_color_classes_act_at_nucleon_parent():
    future = model()
    past = model(link=GaugeLink("-", "-"))
    base_value = base()(0.1, 0.3, 0.1, 0, 0, 5)
    f = future(0.1, 0.3, 0.1, 0, 0, 5)
    p = past(0.1, 0.3, 0.1, 0, 0, 5)
    assert np.allclose(f - base_value, -(p - base_value), atol=1e-12)
    dipole = model(
        link=GaugeLink("+", "-"), color=GluonColorStructure.D_TYPE
    )
    d = dipole(0.1, 0.3, 0.1, 0, 0, 5)
    assert np.linalg.norm(d-base_value) < np.linalg.norm(f-base_value)


def test_overlap_limits_remove_linear_polarization_functions():
    without_linear = LFWFGaugeLinkSpinHalfGluonGTMD(
        t_even_gtmd=base(linear=0.0),
        color=GluonColorStructure.F_TYPE,
        gauge_link=GaugeLink("+", "+"),
        nucleon_mass_gev=0.939,
        transverse_width_gev2=0.3,
    )
    k = (0.3, 0.1)
    raw = without_linear._radial_values(
        base(linear=0.0)(0.1, *k, 0, 0, 5), k
    )
    assert raw["f1Tperp"] != 0.0
    assert raw["h1"] != 0.0
    assert raw["h1Lperp"] == 0.0
    assert raw["h1Tperp"] == 0.0


def test_nucleon_density_is_hermitian_positive_and_refuses_offforward():
    value = model()(0.1, 0.4, 0.2, 0, 0, 5)
    joint = value.transpose(0, 2, 1, 3).reshape(4, 4)
    assert np.allclose(joint, joint.conj().T, atol=1e-12)
    assert np.linalg.eigvalsh(joint)[0] >= -1e-10
    with pytest.raises(ValueError, match="off-forward"):
        model()(0.1, 0.4, 0.2, 0.01, 0, 5)


def test_own_nucleon_parent_passes_through_ss_sd_ds_dd_convolution():
    grid = np.linspace(0.0, 3.0, 301)
    u = np.exp(-0.8 * grid**2)
    w = 0.18 * grid**2 * np.exp(-0.9 * grid**2)
    norm = np.trapz(grid**2 * (u*u+w*w), grid)
    wave = RadialWaveFunction(
        name="test_sd", representation="momentum", grid=grid,
        u=u/np.sqrt(norm), w=w/np.sqrt(norm), source="analytic test fixture",
    )
    quadratures = build_off_forward_component_quadratures(
        radial=wave.radial_callable(),
        nucleon_mass=0.939,
        k_max=2.0,
        delta_x=0.0,
        delta_y=0.0,
        n_k=4,
        n_cos_theta=4,
        n_phi=4,
        deuteron_mass=1.876,
    )
    own = model()
    components = convolve_gluon_gtmd_wave_components(
        x=0.05, k_x=0.25, k_y=0.1, scale=5.0,
        proton_gtmd=own, neutron_gtmd=own, quadratures=quadratures,
    )
    assert set(components) == {"SS", "SD", "DS", "DD"}
    assert all(
        np.isfinite(values[nucleon]).all()
        for values in components.values()
        for nucleon in ("proton", "neutron")
    )
    assert np.linalg.norm(components["SD"]["proton"]) > 0.0


def test_spin1_wilson_phase_generates_lt_tt_without_norm_inflation():
    names = (
        "f1", "h1perp", "g1", "h1Lperp", "f1Tperp", "g1T", "h1",
        "h1Tperp", "f1LL", "h1LLperp", "f1LT", "g1LT", "h1LT",
        "h1LTperp", "f1TT_minus_h1TTperp", "g1TT", "h1TT",
        "h1TTperpperp",
    )
    values = {name: 0.0 for name in names}
    values.update(f1=2.0, g1=0.5, f1LL=0.1)
    base_parent = compose_spin1_gluon_correlator((0.4, 0.2), 1.876, values)
    phase = Spin1NuclearWilsonLine(
        GluonColorStructure.F_TYPE, GaugeLink("+", "+"),
        d_state_probability=0.0576, sd_coherence=0.3898,
    )
    channels = phase.channel_phases(np.hypot(0.4, 0.2))
    phases = phase.phases(np.hypot(0.4, 0.2))
    assert set(channels) == {"S_D_rank1", "D_D_rank2"}
    assert phases == pytest.approx(
        (channels["S_D_rank1"], channels["D_D_rank2"])
    )
    result = phase.apply(base_parent.values, (0.4, 0.2))
    _, projected, residual = project_to_allowed_spin1_gluon_basis(
        result, (0.4, 0.2), 1.876
    )
    assert residual < 5e-4
    assert projected["g1LT"] != 0.0
    assert projected["g1TT"] != 0.0
    assert np.trace(
        result.transpose(0, 2, 1, 3).reshape(6, 6)
    ).real == pytest.approx(
        np.trace(base_parent.joint_density_matrix()).real
    )


def test_spin1_phase_reverses_and_pure_s_limit_is_exact():
    names = (
        "f1", "h1perp", "g1", "h1Lperp", "f1Tperp", "g1T", "h1",
        "h1Tperp", "f1LL", "h1LLperp", "f1LT", "g1LT", "h1LT",
        "h1LTperp", "f1TT_minus_h1TTperp", "g1TT", "h1TT",
        "h1TTperpperp",
    )
    values = {name: 0.0 for name in names}
    values.update(f1=2.0, g1=0.5)
    parent = compose_spin1_gluon_correlator((0.4, 0.2), 1.876, values)
    outputs = []
    for link in (GaugeLink("+", "+"), GaugeLink("-", "-")):
        phase = Spin1NuclearWilsonLine(
            GluonColorStructure.F_TYPE, link, 0.0576, 0.3898
        )
        _, tmds, _ = project_to_allowed_spin1_gluon_basis(
            phase.apply(parent.values, (0.4, 0.2)), (0.4, 0.2), 1.876
        )
        outputs.append(tmds)
    assert outputs[0]["g1LT"] == pytest.approx(-outputs[1]["g1LT"], rel=2e-3)
    assert outputs[0]["g1TT"] == pytest.approx(-outputs[1]["g1TT"], rel=2e-3)
    pure_s = Spin1NuclearWilsonLine(
        GluonColorStructure.F_TYPE, GaugeLink("+", "+"), 0.0, 0.0
    )
    assert np.array_equal(pure_s.apply(parent.values, (0.4, 0.2)), parent.values)


def test_complete_spin_half_psd_projection_is_spectral_not_component_clip():
    joint = np.diag((1.2, 0.5, 0.2, -0.1)).astype(complex)
    values = joint.reshape(2, 2, 2, 2).transpose(0, 2, 1, 3)
    projected, removed = project_spin_half_gluon_density_psd(values)
    result = projected.transpose(0, 2, 1, 3).reshape(4, 4)
    assert removed == pytest.approx(0.1)
    assert np.linalg.eigvalsh(result)[0] >= -1e-12
    assert np.trace(result).real == pytest.approx(np.trace(joint).real)
