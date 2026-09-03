import numpy as np
from pathlib import Path
import pytest

from deuteron_wigner.hidden_color_cluster_lfwf import (
    EffectiveClusterParameters,
    EffectiveClusterCollinearConvolution,
    EffectiveClusterTMDConvolution,
    EffectiveClusterLMDFGrid,
    EffectiveClusterScalarLFWF,
    EffectiveClusterSpinOneLFWF,
    EffectiveClusterVectorCurrentLFWF,
    GAMMA,
    MINKOWSKI_METRIC,
    four_momentum_from_light_front,
    light_front_u_spinor,
    light_front_v_spinor,
    melosh_rotation,
    slash,
    spin_one_polarization,
    solve_longitudinal_thooft,
)
from deuteron_wigner.pdfs import LHAPDFProvider, PolarizedLHAPDFProvider


class _ToyFlavorProvider:
    def __init__(self, polarized=False):
        self.polarized = polarized

    def proton(self, flavor, x, scale):
        amplitudes = {2: 4.0, 1: 2.0, -2: 0.8, -1: 1.2, 3: 0.5, -3: 0.3}
        sign = -1.0 if self.polarized and flavor in (1, -1) else 1.0
        factor = 0.35 if self.polarized else 1.0
        return sign * factor * amplitudes[flavor] * (1.0 - x) ** 3

    def neutron(self, flavor, x, scale):
        partner = {2: 1, 1: 2, -2: -1, -1: -2}.get(flavor, flavor)
        return self.proton(partner, x, scale)


@pytest.fixture(scope="module")
def cluster_lmdf_grid():
    return EffectiveClusterLMDFGrid(z_nodes=121, transverse_nodes=48)


def test_thooft_ground_state_is_normalized_positive_and_exchange_symmetric():
    solution = solve_longitudinal_thooft()
    assert np.all(solution.chi > 0.0)
    assert np.isclose(np.dot(solution.weights, solution.chi**2), 1.0)
    z = np.linspace(0.02, 0.98, 31)
    np.testing.assert_allclose(solution.value(z), solution.value(1.0 - z), rtol=2e-8)


def test_thooft_eigenvalue_converges_with_quadrature_order():
    coarse = solve_longitudinal_thooft(
        EffectiveClusterParameters(longitudinal_nodes=240)
    )
    fine = solve_longitudinal_thooft(
        EffectiveClusterParameters(longitudinal_nodes=480)
    )
    assert abs(coarse.mass_squared_gev2 - fine.mass_squared_gev2) < 2.0e-3


def test_scalar_lfwf_normalization_endpoints_and_mass_decomposition():
    wave = EffectiveClusterScalarLFWF()
    assert np.isclose(wave.analytic_norm(), 1.0, atol=2e-10)
    assert wave.amplitude(0.0, 0.0) == 0.0
    assert wave.amplitude(1.0, 0.0) == 0.0
    assert wave.amplitude(0.5, 0.0) > wave.amplitude(0.5, 0.2)
    assert np.isclose(
        wave.total_mass_gev**2,
        wave.longitudinal.mass_squared_gev2
        + wave.transverse_mass_squared_gev2,
    )


def test_source_parameter_variations_change_the_state():
    central = EffectiveClusterScalarLFWF()
    low_mass = EffectiveClusterScalarLFWF(
        EffectiveClusterParameters(cluster_mass_gev=0.838 - 0.083)
    )
    high_kappa = EffectiveClusterScalarLFWF(
        EffectiveClusterParameters(transverse_kappa_gev=0.143)
    )
    assert low_mass.total_mass_gev != central.total_mass_gev
    assert high_kappa.transverse_mass_squared_gev2 != central.transverse_mass_squared_gev2


def test_melosh_rotation_is_unitary_and_identity_at_zero_k():
    rotation = melosh_rotation(0.37, 0.12, -0.08, 0.838, 2.1)
    np.testing.assert_allclose(rotation.conj().T @ rotation, np.eye(2), atol=2e-15)
    zero = melosh_rotation(0.37, 0.0, 0.0, 0.838, 2.1)
    np.testing.assert_allclose(zero, np.eye(2), atol=2e-15)


def test_spin_wave_function_preserves_scalar_probability_pointwise():
    wave = EffectiveClusterSpinOneLFWF()
    k_component = 0.12
    k_perp = np.sqrt(2.0) * k_component
    scalar_probability = wave.scalar.amplitude(0.41, k_perp) ** 2
    for target_helicity in (-1, 0, 1):
        amplitudes = wave.helicity_amplitudes(
            target_helicity, 0.41, k_component, k_component
        )
        assert np.isclose(np.sum(np.abs(amplitudes) ** 2), scalar_probability)


def test_cluster_tmd_projection_sum_rules_and_tensor_structure():
    wave = EffectiveClusterSpinOneLFWF()
    z_nodes, z_weights = np.polynomial.legendre.leggauss(90)
    z_nodes = (z_nodes + 1.0) / 2.0
    z_weights = z_weights / 2.0
    k_nodes, k_weights = np.polynomial.legendre.leggauss(90)
    # Gaussian support is negligible beyond 1 GeV for kappa=0.13 GeV.
    k_nodes = (k_nodes + 1.0) / 2.0
    k_weights = k_weights / 2.0
    integrals = {"f1": 0.0, "g1L": 0.0, "f1LL": 0.0}
    for z, wz in zip(z_nodes, z_weights):
        for k, wk in zip(k_nodes, k_weights):
            projected = wave.leading_twist_tmds(float(z), float(k))
            for name in integrals:
                integrals[name] += wz * wk * 2.0 * np.pi * k * projected[name]
    assert np.isclose(integrals["f1"], 1.0, atol=2e-5)
    assert abs(integrals["f1LL"]) < 2e-6
    assert 0.0 < integrals["g1L"] < 1.0
    # Exact zero is the controlled canonical-triplet diagnostic.  A nonzero
    # result is required from the production vector-current spin vertex.
    assert abs(wave.leading_twist_tmds(0.5, 0.2)["f1LL"]) < 1e-14


def test_gamma_algebra_lf_spinors_and_polarizations_are_independent_checks():
    identity = np.eye(4)
    for mu in range(4):
        for nu in range(4):
            anticommutator = GAMMA[mu] @ GAMMA[nu] + GAMMA[nu] @ GAMMA[mu]
            np.testing.assert_allclose(
                anticommutator,
                2.0 * MINKOWSKI_METRIC[mu, nu] * identity,
                atol=2e-15,
            )
    mass = 0.838
    momentum = four_momentum_from_light_front(1.13, 0.17, -0.09, mass)
    assert np.isclose(momentum @ MINKOWSKI_METRIC @ momentum, mass**2)
    for helicity in (-1, 1):
        u = light_front_u_spinor(momentum, helicity, mass)
        v = light_front_v_spinor(momentum, helicity, mass)
        np.testing.assert_allclose((slash(momentum) - mass * identity) @ u, 0.0, atol=2e-15)
        np.testing.assert_allclose((slash(momentum) + mass * identity) @ v, 0.0, atol=2e-15)
        assert np.isclose(u.conj().T @ GAMMA[0] @ u, 2.0 * mass)
        assert np.isclose(v.conj().T @ GAMMA[0] @ v, -2.0 * mass)
    polarizations = [spin_one_polarization(lam) for lam in (-1, 0, 1)]
    for first_index, first in enumerate(polarizations):
        for second_index, second in enumerate(polarizations):
            inner = first.conj() @ MINKOWSKI_METRIC @ second
            assert np.isclose(inner, -float(first_index == second_index))


def _integrate_vector_tmds(wave, nodes=60):
    points, weights = np.polynomial.legendre.leggauss(nodes)
    z_nodes = (points + 1.0) / 2.0
    z_weights = weights / 2.0
    k_nodes = (points + 1.0) / 2.0
    k_weights = weights / 2.0
    integrals = {"f1": 0.0, "g1L": 0.0, "f1LL": 0.0}
    for z, wz in zip(z_nodes, z_weights):
        for k, wk in zip(k_nodes, k_weights):
            tmds = wave.leading_twist_tmds(float(z), float(k))
            for name in integrals:
                integrals[name] += wz * wk * 2.0 * np.pi * k * tmds[name]
    return integrals


def test_vector_current_state_normalization_tensor_sum_rule_and_nonzero_shape():
    wave = EffectiveClusterVectorCurrentLFWF(normalization_nodes=56)
    integrals = _integrate_vector_tmds(wave, nodes=56)
    assert np.isclose(integrals["f1"], 1.0, atol=3e-8)
    assert abs(integrals["f1LL"]) < 3e-8
    assert -1.0 < integrals["g1L"] < 1.0
    local = [
        wave.leading_twist_tmds(0.35, 0.05)["f1LL"],
        wave.leading_twist_tmds(0.50, 0.20)["f1LL"],
    ]
    assert max(abs(value) for value in local) > 1e-5


def test_vector_current_azimuthal_covariance_and_transverse_parity():
    wave = EffectiveClusterVectorCurrentLFWF(normalization_nodes=40)
    radius = 0.16
    reference = wave.helicity_amplitudes(1, 0.43, radius, 0.0)
    rotated = wave.helicity_amplitudes(
        1, 0.43, radius / np.sqrt(2.0), radius / np.sqrt(2.0)
    )
    assert np.isclose(np.sum(np.abs(reference) ** 2), np.sum(np.abs(rotated) ** 2))
    plus = wave.leading_twist_tmds(0.43, radius)
    minus_total = sum(
        wave.helicity_density(-1, h, 0.43, radius) for h in (-1, 1)
    )
    plus_total = sum(
        wave.helicity_density(1, h, 0.43, radius) for h in (-1, 1)
    )
    assert np.isclose(minus_total, plus_total)
    assert plus["f1"] > 0.0


def test_vector_current_reproduces_published_lmdf_vector_paths():
    benchmark = np.genfromtxt(
        Path("data/benchmarks/kaur_2026_cluster_lmdf.csv"),
        delimiter=",",
        names=True,
    )
    wave = EffectiveClusterVectorCurrentLFWF(normalization_nodes=72)
    # Compare every fifth source point, excluding the numerically irrelevant
    # endpoint neighborhood. The PDF paths have only plot-coordinate precision.
    indices = np.arange(5, 91, 5)
    residuals = {"f1": [], "g1L": [], "f1LL": []}
    for index in indices:
        z = float(benchmark["z"][index])
        model = wave.collinear_lmdfs(z, quadrature_nodes=72)
        residuals["f1"].append(z * model["f1"] - benchmark["z_f1"][index])
        residuals["g1L"].append(z * model["g1L"] - benchmark["z_g1L"][index])
        residuals["f1LL"].append(z * model["f1LL"] - benchmark["z_f1LL"][index])
    assert np.max(np.abs(residuals["f1"])) < 1.6e-2
    assert np.max(np.abs(residuals["g1L"])) < 1.6e-2
    assert np.max(np.abs(residuals["f1LL"])) < 2.0e-3


def test_cluster_pdf_convolution_preserves_flavor_support_and_provider_roles(
    cluster_lmdf_grid,
):
    convolution = EffectiveClusterCollinearConvolution(
        unpolarized=_ToyFlavorProvider(),
        polarized=_ToyFlavorProvider(polarized=True),
        lmdfs=cluster_lmdf_grid,
        convolution_nodes=56,
    )
    assert convolution.flavor_distribution("f1", 2, 0.2, 5.0) != convolution.flavor_distribution(
        "f1", -2, 0.2, 5.0
    )
    # Exact charge-symmetric p+n average makes u and d equal only for this
    # deliberately isoscalar two-cluster observable, not inside either input.
    assert np.isclose(
        convolution.flavor_distribution("f1", 2, 0.2, 5.0),
        convolution.flavor_distribution("f1", 1, 0.2, 5.0),
    )
    assert not np.isclose(
        convolution.flavor_distribution("g1L", 1, 0.2, 5.0),
        convolution.flavor_distribution("f1", 1, 0.2, 5.0),
    )
    assert convolution.flavor_distribution("f1", 2, 0.0, 5.0) == 0.0
    assert convolution.flavor_distribution("f1", 2, 1.0, 5.0) == 0.0
    assert convolution.flavor_distribution("f1LL", 2, 0.3, 5.0) != 0.0


def test_cluster_convolution_number_and_tensor_sum_rules(cluster_lmdf_grid):
    convolution = EffectiveClusterCollinearConvolution(
        unpolarized=_ToyFlavorProvider(),
        polarized=_ToyFlavorProvider(polarized=True),
        lmdfs=cluster_lmdf_grid,
        convolution_nodes=56,
    )
    nodes, weights = np.polynomial.legendre.leggauss(72)
    x_nodes = (nodes + 1.0) / 2.0
    x_weights = weights / 2.0
    f1_number = sum(
        weight * convolution.flavor_distribution("f1", 2, float(x), 5.0)
        for x, weight in zip(x_nodes, x_weights)
    )
    tensor_number = sum(
        weight * convolution.flavor_distribution("f1LL", 2, float(x), 5.0)
        for x, weight in zip(x_nodes, x_weights)
    )
    # ∫dy 1/2[u_p(y)+u_n(y)] = (4+2)/2 * ∫(1-y)^3dy.
    assert np.isclose(f1_number, 0.75, atol=8e-5)
    assert abs(tensor_number) < 8e-5
    f2 = convolution.structure_function("f1", 0.2, 5.0, (2, 1, -2, -1))
    xb1 = convolution.structure_function("f1LL", 0.2, 5.0, (2, 1, -2, -1))
    direct_tensor_charge_sum = 0.2 * 0.5 * sum(
        convolution.electric_charge_squared(flavor)
        * convolution.flavor_distribution("f1LL", flavor, 0.2, 5.0)
        for flavor in (2, 1, -2, -1)
    )
    assert f2 > 0.0
    assert np.isclose(xb1, direct_tensor_charge_sum)


def test_cluster_tmd_convolution_reduces_to_collinear_boundary(cluster_lmdf_grid):
    unpolarized = _ToyFlavorProvider()
    polarized = _ToyFlavorProvider(polarized=True)
    tmd = EffectiveClusterTMDConvolution(
        unpolarized=unpolarized,
        polarized=polarized,
        wave=cluster_lmdf_grid.wave,
        convolution_nodes=48,
    )
    collinear = EffectiveClusterCollinearConvolution(
        unpolarized=unpolarized,
        polarized=polarized,
        lmdfs=cluster_lmdf_grid,
        convolution_nodes=48,
    )
    nodes, weights = np.polynomial.legendre.leggauss(64)
    k_nodes = (nodes + 1.0) / 2.0
    k_weights = weights / 2.0
    for sector in ("f1", "g1L", "f1LL"):
        transverse_integral = sum(
            weight
            * 2.0
            * np.pi
            * k
            * tmd.flavor_tmd(sector, 2, 0.2, float(k), 5.0)
            for k, weight in zip(k_nodes, k_weights)
        )
        expected = collinear.flavor_distribution(sector, 2, 0.2, 5.0)
        assert np.isclose(transverse_integral, expected, rtol=2.5e-3, atol=2e-6)


def test_cluster_tmd_correlator_is_flavor_resolved_hermitian_and_tensor_nonzero(
    cluster_lmdf_grid,
):
    tmd = EffectiveClusterTMDConvolution(
        unpolarized=_ToyFlavorProvider(),
        polarized=_ToyFlavorProvider(polarized=True),
        wave=cluster_lmdf_grid.wave,
        convolution_nodes=40,
    )
    u = tmd.flavor_tmd("f1", 2, 0.2, 0.12, 5.0)
    ubar = tmd.flavor_tmd("f1", -2, 0.2, 0.12, 5.0)
    assert not np.isclose(u, ubar)
    correlator = tmd.correlator(2, 0.2, 0.12, 5.0)
    np.testing.assert_allclose(correlator.vector, correlator.vector.conj().T)
    np.testing.assert_allclose(correlator.axial, correlator.axial.conj().T)
    assert np.linalg.norm(correlator.vector - np.trace(correlator.vector) * np.eye(3) / 3.0) > 0.0


def test_nnpdf_cluster_convolution_reproduces_published_b1_moment(
    cluster_lmdf_grid,
):
    pytest.importorskip("lhapdf")
    unpolarized = LHAPDFProvider("NNPDF31_nnlo_as_0118_1000", 0)
    polarized = PolarizedLHAPDFProvider(
        "BDSSV24-NLO", 0, data_root="data/raw/lhapdf"
    )
    convolution = EffectiveClusterCollinearConvolution(
        unpolarized=unpolarized,
        polarized=polarized,
        lmdfs=cluster_lmdf_grid,
        convolution_nodes=56,
    )
    nodes, weights = np.polynomial.legendre.leggauss(64)
    x_nodes = 0.02 + (0.85 - 0.02) * (nodes + 1.0) / 2.0
    x_weights = weights * (0.85 - 0.02) / 2.0
    b1 = np.asarray(
        [
            convolution.structure_function("f1LL", float(x), np.sqrt(5.0)) / x
            for x in x_nodes
        ]
    )
    moment = float(np.dot(x_weights, b1))
    # Source result: (0.36 +/- 0.03) x 10^-2.
    assert np.isclose(moment, 0.0036, atol=3.0e-4)
