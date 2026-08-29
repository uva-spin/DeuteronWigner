import pytest
import numpy as np

from deuteron_wigner.gluon_todd import (
    CGIGPMGluonSiversParameters,
    GluonColorStructure,
    GluonSiversInput,
    GluonTWeightedProcess,
    SiversAugmentedSpinHalfGluonGTMD,
    Spin1GluonTOddMultipletInput,
    build_cgi_gpm_gluon_sivers_input,
    cgi_gpm_gluon_sivers_scenarios,
)
from deuteron_wigner.gtmd import GaugeLink
from deuteron_wigner.gtmd_convolution import (
    OffForwardSpinQuadrature,
    convolve_gluon_gtmd_point,
)
from deuteron_wigner.provenance import EvidenceClass, ValidityDomain


F = GluonColorStructure.F_TYPE
D = GluonColorStructure.D_TYPE


def boundary():
    return GluonSiversInput(
        components={
            F: lambda x, k, q: x + 2 * k + 0 * q,
            D: lambda x, k, q: -3 * x + k + 0 * q,
        },
        source="controlled test fixture",
        evidence=EvidenceClass.MODEL,
        validity=ValidityDomain(0.01, 0.5, 2.0, 10.0, 1.0, "test"),
        uncertainty_kind="explicit fixture parameters",
        convention="future-staple f1Tperp_g in GeV^-2",
    )


def test_color_components_are_independent_and_reverse_separately():
    common = dict(x=0.2, k_gev=0.3, q_gev=5.0)
    future = GaugeLink("+", "+")
    past = GaugeLink("-", "-")
    assert boundary().value(F, **common, gauge_link=future) == pytest.approx(0.8)
    assert boundary().value(D, **common, gauge_link=future) == pytest.approx(-0.3)
    for color in (F, D):
        assert boundary().value(color, **common, gauge_link=past) == pytest.approx(
            -boundary().value(color, **common, gauge_link=future)
        )


def test_process_composition_uses_explicit_hard_coefficients():
    process = GluonTWeightedProcess(
        name="fixture observable",
        coefficients={F: 2.0, D: -4.0},
        source="analytic fixture",
        factorization_statement="controlled linear color decomposition",
    )
    result = process.compose(
        boundary(), x=0.2, k_gev=0.3, q_gev=5.0, gauge_link=GaugeLink("+", "+")
    )
    assert result == pytest.approx(2.0 * 0.8 - 4.0 * -0.3)


def test_contract_refuses_universal_single_component_and_implicit_process():
    kwargs = dict(
        source="bad fixture",
        evidence=EvidenceClass.MODEL,
        validity=ValidityDomain(0.01, 0.5, 2.0, 10.0),
        uncertainty_kind="parameters",
        convention="fixture",
    )
    with pytest.raises(ValueError, match="both independent"):
        GluonSiversInput(components={F: lambda x, k, q: 0.0}, **kwargs)
    with pytest.raises(ValueError, match="both f-type and d-type"):
        GluonTWeightedProcess(
            name="bad",
            coefficients={F: 1.0},
            source="fixture",
            factorization_statement="fixture",
        )


def test_contract_refuses_mixed_links_and_out_of_domain_requests():
    with pytest.raises(ValueError, match="mixed gluon gauge links"):
        boundary().value(
            F, x=0.2, k_gev=0.3, q_gev=5.0, gauge_link=GaugeLink("+", "-")
        )
    with pytest.raises(ValueError, match="outside"):
        boundary().value(
            F, x=0.8, k_gev=0.3, q_gev=5.0, gauge_link=GaugeLink("+", "+")
        )


def test_nonfinite_input_and_coefficients_are_rejected():
    bad = GluonSiversInput(
        components={F: lambda x, k, q: float("nan"), D: lambda x, k, q: 0.0},
        source="bad fixture",
        evidence=EvidenceClass.MODEL,
        validity=ValidityDomain(0.01, 0.5, 2.0, 10.0),
        uncertainty_kind="parameters",
        convention="fixture",
    )
    with pytest.raises(ValueError, match="not finite"):
        bad.value(F, x=0.2, k_gev=0.3, q_gev=5.0, gauge_link=GaugeLink("+", "+"))
    with pytest.raises(ValueError, match="finite"):
        GluonTWeightedProcess(
            name="bad",
            coefficients={F: float("inf"), D: 0.0},
            source="fixture",
            factorization_statement="fixture",
        )


def augmented(link=GaugeLink("+", "+")):
    def t_even(x, k_x, k_y, delta_x, delta_y, scale):
        del x, k_x, k_y, delta_x, delta_y, scale
        return np.zeros((2, 2, 2, 2), dtype=np.complex128)

    return SiversAugmentedSpinHalfGluonGTMD(
        t_even_gtmd=t_even,
        boundary=boundary(),
        process=GluonTWeightedProcess(
            name="fixture",
            coefficients={F: 1.0, D: 0.0},
            source="analytic fixture",
            factorization_statement="controlled linear decomposition",
        ),
        gauge_link=link,
        nucleon_mass_gev=1.0,
    )


def test_spin_half_embedding_is_hermitian_angular_and_link_odd():
    future = augmented()(0.2, 0.3, 0.4, 0.0, 0.0, 5.0)
    past = augmented(GaugeLink("-", "-"))(0.2, 0.3, 0.4, 0.0, 0.0, 5.0)
    np.testing.assert_allclose(future, -past, atol=1e-14)
    np.testing.assert_allclose(
        future, future.transpose(1, 0, 3, 2).conj(), atol=1e-14
    )
    # k_y creates sigma_x target-spin response; k_x creates sigma_y response.
    assert np.linalg.norm(future[0, 1].real) > 0.0
    assert np.linalg.norm(future[0, 1].imag) > 0.0
    at_zero = augmented()(0.2, 0.0, 0.0, 0.0, 0.0, 5.0)
    np.testing.assert_allclose(at_zero, 0.0, atol=1e-14)


def test_forward_only_embedding_refuses_invented_gtmd_transfer_dependence():
    with pytest.raises(ValueError, match="cannot be promoted"):
        augmented()(0.2, 0.3, 0.4, 0.01, 0.0, 5.0)


def test_sivers_tensor_propagates_through_spin1_parent():
    sigma_x = np.asarray(((0.0, 1.0), (1.0, 0.0)), dtype=np.complex128)
    spectral = np.zeros((1, 3, 3, 2, 2), dtype=np.complex128)
    spectral[0, 0, 0] = sigma_x
    quadrature = OffForwardSpinQuadrature(
        y=np.asarray([0.8]),
        p_x=np.asarray([0.0]),
        p_y=np.asarray([0.0]),
        weights=np.asarray([1.0]),
        delta_x=0.0,
        delta_y=0.0,
        spectral=spectral,
    )
    zero = lambda *args: np.zeros((2, 2, 2, 2), dtype=np.complex128)
    parent = convolve_gluon_gtmd_point(
        x=0.16,
        k_x=0.0,
        k_y=0.4,
        scale=5.0,
        proton_gtmd=augmented(),
        neutron_gtmd=zero,
        quadrature=quadrature,
    )
    assert parent.shape == (3, 3, 2, 2)
    assert np.linalg.norm(parent[0, 0]) > 0.0
    np.testing.assert_allclose(parent, parent.transpose(1, 0, 3, 2).conj())


def test_cgi_gpm_numerical_boundary_has_independent_f_and_d_scenarios():
    pdf = lambda x, q: 5.0 * (1.0 - x) / x**0.2
    scenarios = cgi_gpm_gluon_sivers_scenarios()
    assert [item.label for item in scenarios] == [
        "central_midpoint", "negative_d_endpoint", "positive_d_endpoint"
    ]
    values = []
    for parameters in scenarios:
        fitted = build_cgi_gpm_gluon_sivers_input(pdf, parameters)
        values.append([
            fitted.value(
                color, x=0.1, k_gev=0.4, q_gev=5.0,
                gauge_link=GaugeLink("+", "+"),
            )
            for color in GluonColorStructure
        ])
    values = np.asarray(values)
    assert values[0, 0] != 0.0
    assert values[0, 1] == 0.0
    assert values[1, 0] != values[2, 0]
    assert values[1, 1] == pytest.approx(-values[2, 1])


def test_cgi_gpm_boundary_is_finite_at_origin_and_reverses():
    fitted = build_cgi_gpm_gluon_sivers_input(
        lambda x, q: 3.0,
        CGIGPMGluonSiversParameters(n_f=0.05, n_d=-0.15),
    )
    for color in GluonColorStructure:
        future = fitted.value(
            color, x=0.1, k_gev=0.0, q_gev=5.0,
            gauge_link=GaugeLink("+", "+"),
        )
        past = fitted.value(
            color, x=0.1, k_gev=0.0, q_gev=5.0,
            gauge_link=GaugeLink("-", "-"),
        )
        assert np.isfinite(future)
        assert past == pytest.approx(-future)


def test_cgi_gpm_parameter_bounds_fail_closed():
    with pytest.raises(ValueError, match="normalizations"):
        CGIGPMGluonSiversParameters(n_f=1.1)


def test_complete_gluon_todd_multiplet_has_independent_color_rank_and_link():
    fitted = build_cgi_gpm_gluon_sivers_input(
        lambda x, q: 2.0 * (1.0 - x) ** 4,
        CGIGPMGluonSiversParameters(n_f=0.05, n_d=-0.15),
    )
    multiplet = Spin1GluonTOddMultipletInput(fitted)
    names = {"h1Lperp", "f1Tperp", "h1", "h1Tperp", "g1LT", "g1TT"}
    values = {
        (name, color): multiplet.value(
            name, color, x=0.1, k_gev=0.4, q_gev=5.0,
            gauge_link=GaugeLink("+", "+"),
        )
        for name in names
        for color in GluonColorStructure
    }
    assert len(set(values.values())) > 6
    for name in names:
        for color in GluonColorStructure:
            past = multiplet.value(
                name, color, x=0.1, k_gev=0.4, q_gev=5.0,
                gauge_link=GaugeLink("-", "-"),
            )
            assert past == pytest.approx(-values[(name, color)])
    correlator = multiplet.correlator(
        GluonColorStructure.F_TYPE,
        x=0.1, k_x_gev=0.3, k_y_gev=0.2, q_gev=5.0,
        gauge_link=GaugeLink("+", "+"),
    )
    density = correlator.joint_density_matrix()
    np.testing.assert_allclose(density, density.conj().T)
