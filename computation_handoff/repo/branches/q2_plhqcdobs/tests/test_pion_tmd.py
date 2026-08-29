import numpy as np

from deuteron_wigner.pion_exchange import (
    JAM21IsoscalarPionPDF,
    MillerTensorPionDistribution,
    SpinAveragedPionConvolution,
    TensorPionConvolution,
)
from deuteron_wigner.pion_tmd import (
    SpinResolvedTransversePionGluonBoundary,
    EvolvedTransversePionScenario,
    NativeEvolvedTransversePionScenario,
    SpinResolvedTransversePionBoundary,
    TransverseSpinAveragedPionBoundary,
    Vpion19IntrinsicProfile,
    Vpion19ArtemidePionTMD,
)
from deuteron_wigner.tmd_evolution import OneLoopQuarkCSSEvolution


def test_vpion19_central_parameters_and_normalization():
    profile = Vpion19IntrinsicProfile()
    np.testing.assert_allclose(profile.parameters, (0.173426, 0.482789, 2.15172))
    for x in (0.1, 0.5, 0.9):
        assert profile.factor(x, 0.0) == 1.0
        assert 0.0 < profile.factor(x, 2.0) < 1.0


def test_vpion19_replicas_are_distinct():
    central = Vpion19IntrinsicProfile(0)
    replica = Vpion19IntrinsicProfile(1)
    assert replica.parameters != central.parameters
    assert replica.factor(0.4, 1.0) != central.factor(0.4, 1.0)


def test_spin_resolved_pion_gluon_boundary_is_finite_hermitian_and_nonzero():
    splitting = MillerTensorPionDistribution()
    boundary = SpinResolvedTransversePionGluonBoundary(
        splitting, JAM21IsoscalarPionPDF(0), Vpion19IntrinsicProfile(0)
    )
    values = boundary.correlators_k(
        0.1, np.asarray((0.0, 0.3)), 5.0, b_nodes=32
    )
    assert len(values) == 2
    assert np.linalg.norm(values[0]) > 0.0
    for correlator in values:
        assert correlator.shape == (3, 3, 2, 2)
        assert np.isfinite(correlator).all()
        assert np.allclose(
            correlator, correlator.transpose(1, 0, 3, 2).conj()
        )


def test_nuclear_bessel_splitting_reduces_at_zero_b():
    splitting = MillerTensorPionDistribution()
    for y, z in ((0.05, 0.2), (0.2, 0.5), (0.8, 0.8)):
        assert splitting.spin_averaged_f_b(y, z, 0.0) == splitting.spin_averaged_f(y)


def test_transverse_boundary_reduces_to_collinear_convolution():
    splitting = MillerTensorPionDistribution()
    pdf = JAM21IsoscalarPionPDF(0)
    collinear = SpinAveragedPionConvolution(splitting, pdf)
    boundary = TransverseSpinAveragedPionBoundary(
        splitting, pdf, Vpion19IntrinsicProfile()
    )
    assert np.isclose(
        boundary.value(2, 0.1, 0.0, 5.0),
        collinear.f1(2, 0.1, 5.0),
        rtol=2.0e-6,
        atol=2.0e-8,
    )
    assert np.isfinite(boundary.value(2, 0.1, 1.0, 5.0))


def test_spin_resolved_pion_correlator_reduces_to_collinear_u_and_ll():
    splitting = MillerTensorPionDistribution()
    pdf = JAM21IsoscalarPionPDF(0)
    boundary = SpinResolvedTransversePionBoundary(
        splitting, pdf, Vpion19IntrinsicProfile()
    )
    correlator = boundary.correlator_b(2, 0.1, 0.0, 5.0)
    diagonal = np.diag(correlator.vector).real
    spin_average = float(np.mean(diagonal))
    tensor = float(diagonal[1] - 0.5 * (diagonal[0] + diagonal[2]))
    assert np.isclose(
        spin_average,
        SpinAveragedPionConvolution(splitting, pdf).f1(2, 0.1, 5.0),
        rtol=2.0e-6,
        atol=2.0e-8,
    )
    assert np.isclose(
        tensor,
        TensorPionConvolution(splitting, pdf).delta_t(2, 0.1, 5.0),
        rtol=2.0e-6,
        atol=2.0e-8,
    )
    np.testing.assert_array_equal(correlator.axial, 0.0)
    np.testing.assert_array_equal(correlator.transverse, 0.0)


def test_spin_resolved_pion_b_boundary_retains_tensor_recoil():
    boundary = SpinResolvedTransversePionBoundary(
        MillerTensorPionDistribution(),
        JAM21IsoscalarPionPDF(0),
        Vpion19IntrinsicProfile(),
    )
    at_zero = boundary.correlator_b(2, 0.1, 0.0, 5.0).vector
    at_nonzero = boundary.correlator_b(2, 0.1, 1.0, 5.0).vector
    assert np.all(np.isfinite(at_nonzero))
    assert not np.allclose(at_nonzero, at_zero)
    assert not np.isclose(
        at_nonzero[1, 1].real
        - 0.5 * (at_nonzero[0, 0].real + at_nonzero[2, 2].real),
        0.0,
        atol=1.0e-12,
    )


def test_spin_resolved_pion_hankel_transform_is_hermitian_and_convergent():
    boundary = SpinResolvedTransversePionBoundary(
        MillerTensorPionDistribution(),
        JAM21IsoscalarPionPDF(0),
        Vpion19IntrinsicProfile(),
    )
    momentum = np.asarray([0.1, 0.35])
    coarse = boundary.correlators_k(
        2, 0.1, momentum, 5.0, b_max_gev_inv=10.0, b_nodes=32
    )
    fine = boundary.correlators_k(
        2, 0.1, momentum, 5.0, b_max_gev_inv=10.0, b_nodes=48
    )
    for first, second in zip(coarse, fine):
        np.testing.assert_allclose(first.vector, first.vector.conj().T)
        np.testing.assert_allclose(first.axial, 0.0)
        np.testing.assert_allclose(first.transverse, 0.0)
        np.testing.assert_allclose(first.vector, second.vector, rtol=8e-4, atol=2e-7)
        diagonal = np.diag(first.vector).real
        assert abs(diagonal[1] - 0.5 * (diagonal[0] + diagonal[2])) > 0.0


def test_pion_boundary_routes_through_rank_zero_evolution():
    splitting = MillerTensorPionDistribution()
    pdf = JAM21IsoscalarPionPDF(0)
    boundary = TransverseSpinAveragedPionBoundary(
        splitting, pdf, Vpion19IntrinsicProfile()
    )
    scenario = EvolvedTransversePionScenario(
        boundary, OneLoopQuarkCSSEvolution(lambda scale: 0.3)
    )
    at_origin = scenario.value(2, 0.1, 0.0, 5.0)
    assert np.isclose(
        at_origin,
        SpinAveragedPionConvolution(splitting, pdf).f1(2, 0.1, 5.0),
        rtol=2.0e-6,
    )
    assert np.isfinite(scenario.value(2, 0.1, 1.0, 5.0))
    assert scenario.metadata["production_ready"] is False


class _FakeHarpyPion:
    def __init__(self):
        self.member = None

    def setNPparameters_uTMDPDF(self, member):
        self.member = member

    def get_uTMDPDF(self, x, b, hadron, mu, zeta):
        assert hadron == 2
        assert zeta == mu**2
        # Native array order is flavor -5,...,+5.
        return np.asarray(
            [self.member + 0.1 * index + x + 0.01 * b + 0.001 * mu for index in range(11)]
        )


def test_native_vpion_replica_identity_flavor_mapping_and_metadata():
    backend = _FakeHarpyPion()
    native = Vpion19ArtemidePionTMD(member=3, backend=backend)
    assert backend.member == 3
    u = native.charged_pion_b_value(2, 0.3, 1.0, 5.0)
    ubar = native.charged_pion_b_value(-2, 0.3, 1.0, 5.0)
    assert u != ubar
    assert np.isclose(native.isoscalar_b_value(2, 0.3, 1.0, 5.0), 0.5 * (u + ubar))
    assert np.isclose(
        native.isoscalar_b_value(2, 0.3, 1.0, 5.0),
        native.isoscalar_b_value(-2, 0.3, 1.0, 5.0),
    )
    native.set_member(7)
    assert backend.member == 7
    assert native.metadata["matching_order"] == "NNLO"
    assert native.metadata["production_ready"] is False
    assert "JAM21" in native.metadata["collinear_input"]


def test_native_pion_composes_with_nuclear_recoil_and_has_exact_zero_limit():
    native = Vpion19ArtemidePionTMD(member=0, backend=_FakeHarpyPion())
    splitting = MillerTensorPionDistribution()
    scenario = NativeEvolvedTransversePionScenario(splitting, native)
    value_at_zero = scenario.value(2, 0.1, 0.0, 5.0)
    value_at_nonzero_b = scenario.value(2, 0.1, 1.0, 5.0)
    assert np.isfinite(value_at_zero)
    assert np.isfinite(value_at_nonzero_b)
    assert value_at_nonzero_b != value_at_zero
    assert scenario.value(2, 0.0, 1.0, 5.0) == 0.0
    assert scenario.value(2, 2.0, 1.0, 5.0) == 0.0
    assert "J0" in scenario.metadata["nuclear_recoil"]
