import numpy as np

from deuteron_wigner.canonical_parent_enrichment import (
    ExponentiatedSpin1WilsonOperator,
    FockResolvedNucleonBoundary,
    FockResolvedSpinHalfGluonBoundary,
    FockAmplitude,
    NonNucleonicFockLedger,
    NonNucleonicSector,
    OperatorResponseMap,
    CanonicalParentEnricher,
    NonNucleonicParentSector,
    SharedFockOAMLedger,
    WilsonChannel,
    WilsonChannelMember,
    polarized_tensor_response_map,
    project_spin1_gluon_parent_positivity,
    project_spin1_quark_parent_positivity,
    calibrate_shared_fock_oam_ledger,
    joint_polarized_tensor_response_map,
    gluon_polarized_tensor_response_map,
    CanonicalGluonParentEnricher,
)
from deuteron_wigner.quark_correlator import (
    SPIN1_QUARK_TMD_NAMES,
    compose_spin1_quark_correlator,
    project_spin1_quark_correlator,
)
from deuteron_wigner.gluon_correlator import (
    Spin1GluonCorrelator,
    compose_spin1_gluon_correlator,
)


def parent():
    values = {name: 0.0 for name in SPIN1_QUARK_TMD_NAMES}
    values.update(f1=2.0, g1=0.2, h1=0.1, f1LL=0.03, f1LT=0.02)
    return compose_spin1_quark_correlator((0.3, 0.1), 1.8756, values)


def member():
    return WilsonChannelMember("central", {
        WilsonChannel.QUARK_SPECTATOR: 0.03,
        WilsonChannel.GLUON_SPECTATOR: -0.02,
        WilsonChannel.SP: 0.015,
        WilsonChannel.SD: 0.01,
        WilsonChannel.PP: -0.005,
    })


def test_exponentiated_channels_preserve_spectrum_and_reverse_todd():
    base = parent()
    future = ExponentiatedSpin1WilsonOperator(member(), 1).apply(base, 0.3, 0.1)
    past = ExponentiatedSpin1WilsonOperator(member(), -1).apply(base, 0.3, 0.1)
    assert np.allclose(
        np.linalg.eigvalsh(base.quark_target_density_matrix()),
        np.linalg.eigvalsh(future.quark_target_density_matrix()), atol=2e-11,
    )
    u_future = ExponentiatedSpin1WilsonOperator(member(), 1).unitary(0.3, 0.1)
    u_past = ExponentiatedSpin1WilsonOperator(member(), -1).unitary(0.3, 0.1)
    assert np.allclose(u_past, u_future.conj().T, atol=2e-12)
    # The absorptive displacement is odd at leading phase order; finite
    # exponentiation also contains physical even powers.
    weak = WilsonChannelMember(
        "weak", {channel: 1e-4 * value
                 for channel, value in member().strengths.items()}
    )
    fw = ExponentiatedSpin1WilsonOperator(weak, 1).apply(base, 0.3, 0.1)
    pw = ExponentiatedSpin1WilsonOperator(weak, -1).apply(base, 0.3, 0.1)
    f = project_spin1_quark_correlator(fw, (0.3, 0.1), 1.8756)
    p = project_spin1_quark_correlator(pw, (0.3, 0.1), 1.8756)
    zero = project_spin1_quark_correlator(base, (0.3, 0.1), 1.8756)
    assert max(abs(f[n] + p[n] - 2 * zero[n])
               for n in SPIN1_QUARK_TMD_NAMES) < 1e-9


def test_shared_fock_ledger_normalizes_and_generates_all_orbital_ranks():
    ledger = SharedFockOAMLedger((
        FockAmplitude("s0", "scalar", 0, 1.0, "phenomenological"),
        FockAmplitude("a1", "axial", 1, 0.2 + 0.1j, "model"),
        FockAmplitude("g2", "quark_gluon", 2, -0.08 + 0.04j, "model"),
        FockAmplitude("am1", "axial", -1, 0.05j, "model"),
    )).normalized()
    assert np.isclose(ledger.norm, 1.0)
    coordinates = ledger.shared_tmd_coordinates()
    assert set(coordinates) == {
        "rank0_density", "rank1_even", "rank1_odd",
        "rank2_even", "rank2_odd",
    }
    assert all(np.isfinite(list(coordinates.values())))
    boundary = FockResolvedNucleonBoundary(
        ledger, {2: 2.0, 1: 1.0, -2: 0.12, -1: 0.16},
        {2: 0.25, 1: 0.23, -2: 0.30, -1: 0.31},
    )
    future = boundary.tmd_values(2, 0.2, 0.1, 1)
    past = boundary.tmd_values(2, 0.2, 0.1, -1)
    assert future["f1Tperp"] == -past["f1Tperp"]
    assert future["g1T"] == past["g1T"]
    boundary.correlator(2, 0.2, 0.1, 1).require_hermitian()
    gluon = FockResolvedSpinHalfGluonBoundary(ledger, 3.0, 0.30)
    gf = gluon.correlator(0.2, 0.1, 1)
    gp = gluon.correlator(0.2, 0.1, -1)
    assert gf.shape == (2, 2, 2, 2)
    assert np.linalg.eigvalsh(
        gf.transpose(0, 2, 1, 3).reshape(4, 4)
    )[0] >= -1e-12
    assert not np.allclose(gf, gp)
    targets = {
        key: value for key, value in coordinates.items()
        if key != "rank0_density"
    }
    fitted, residual = calibrate_shared_fock_oam_ledger(targets)
    assert np.isclose(fitted.norm, 1.0)
    assert residual < 1e-7


def test_non_nucleonic_ledger_keeps_unsupported_central_sectors_zero():
    probabilities = {
        NonNucleonicSector.NNPI: 0.02,
        NonNucleonicSector.DELTADELTA: 0.004,
        NonNucleonicSector.HIDDEN_COLOR: 0.01,
        NonNucleonicSector.SRC: 0.06,
    }
    ledger = NonNucleonicFockLedger(
        probabilities,
        {sector: 0.5 * value for sector, value in probabilities.items()},
        {NonNucleonicSector.NNPI: True, NonNucleonicSector.SRC: True},
    )
    assert np.isclose(ledger.nucleonic_probability, 0.906)
    assert ledger.central_weight(NonNucleonicSector.HIDDEN_COLOR) == 0.0
    assert ledger.central_weight(NonNucleonicSector.DELTADELTA) == 0.0


def test_operator_response_is_hermiticity_and_positivity_preserving():
    identity = OperatorResponseMap.identity(0.8)
    result = identity.apply(parent())
    assert np.allclose(result.vector, 0.8 * parent().vector)
    mix = OperatorResponseMap((
        np.diag([np.sqrt(0.7), np.sqrt(0.8), np.sqrt(0.7)]),
        np.asarray([[0, 0.1, 0], [0, 0, 0.1], [0, 0, 0]], dtype=complex),
    ), 0.9, "tensor_shadowing")
    transformed = mix.apply(parent())
    assert transformed.is_target_hermitian()
    assert transformed.minimum_positivity_eigenvalue() >= -1e-12
    polarized = polarized_tensor_response_map(
        unpolarized_factor=0.92, vector_asymmetry=0.03,
        tensor_alignment=-0.06, label="polarized_shadowing",
    )
    rates = np.diag(polarized.completeness()).real
    assert not np.allclose(rates, rates[0])
    mapped = polarized.apply(parent())
    assert mapped.minimum_positivity_eigenvalue() >= -1e-12
    joint = joint_polarized_tensor_response_map(
        unpolarized_factor=0.9, target_vector=0.02,
        target_tensor=-0.04, quark_helicity=0.08,
        label="operator_resolved_shadowing",
    )
    joint_mapped = joint.apply(parent())
    assert joint_mapped.minimum_positivity_eigenvalue() >= -1e-12
    assert not np.allclose(joint_mapped.vector, 0.9 * parent().vector)


def test_canonical_enricher_applies_complete_parent_sectors_in_one_order():
    probabilities = {sector: 0.0 for sector in NonNucleonicSector}
    probabilities[NonNucleonicSector.NNPI] = 0.02
    ledger = NonNucleonicFockLedger(
        probabilities, {sector: 0.0 for sector in NonNucleonicSector},
        {NonNucleonicSector.NNPI: True},
    )
    sector = NonNucleonicParentSector(
        NonNucleonicSector.NNPI, parent(), ledger, "Miller/JAM21/Vpion19"
    )
    enriched = CanonicalParentEnricher(
        wilson=ExponentiatedSpin1WilsonOperator(member(), 1),
        responses=(OperatorResponseMap.identity(0.98),),
        nonnucleonic=(sector,),
    ).apply(parent(), 0.3, 0.1)
    assert enriched.is_target_hermitian()
    assert enriched.minimum_positivity_eigenvalue() >= -1e-12


def test_spin1_parent_positivity_projection_preserves_trace_and_common_ratios():
    base = parent()
    bad = type(base)(
        base.vector, 20*base.axial, 20*base.transverse
    )
    assert bad.minimum_positivity_eigenvalue() < 0
    fixed, scale = project_spin1_quark_parent_positivity(bad)
    assert 0 < scale < 1
    assert fixed.minimum_positivity_eigenvalue() >= -1e-12
    assert np.allclose(
        np.trace(fixed.vector), np.trace(bad.vector), atol=1e-12
    )


def test_gluon_joint_spin_response_and_enricher_preserve_density():
    density = np.eye(6).reshape(3, 2, 3, 2).transpose(0, 2, 1, 3)
    base = Spin1GluonCorrelator(density)
    response = gluon_polarized_tensor_response_map(
        unpolarized_factor=0.91, target_vector=0.02,
        target_tensor=-0.03, gluon_helicity=0.08,
        linear_polarization=0.04, label="gluon_tensor_shadowing",
    )
    result = CanonicalGluonParentEnricher((response,)).apply(base)
    assert result.minimum_positivity_eigenvalue() >= -1e-12
    assert not np.allclose(result.values, 0.91 * base.values)


def test_gluon_complete_parent_projection_uses_one_common_scale():
    values = {
        "f1": 2.0, "h1perp": 0.2, "g1": 0.3, "h1Lperp": 0.0,
        "f1Tperp": 0.0, "g1T": 0.1, "h1": 0.0, "h1Tperp": 0.0,
        "f1LL": 0.1, "h1LLperp": 0.0, "f1LT": 0.1, "g1LT": 0.0,
        "h1LT": 0.0, "h1LTperp": 0.0,
        "f1TT_minus_h1TTperp": 0.1, "g1TT": 0.0, "h1TT": 0.0,
        "h1TTperpperp": 0.0,
    }
    base = compose_spin1_gluon_correlator((0.3, 0.1), 1.8756, values)
    bad_values = {
        name: value if name == "f1" else 40*value
        for name, value in values.items()
    }
    bad = compose_spin1_gluon_correlator(
        (0.3, 0.1), 1.8756, bad_values
    )
    assert bad.minimum_positivity_eigenvalue() < 0
    fixed, scale = project_spin1_gluon_parent_positivity(
        bad, (0.3, 0.1), 1.8756
    )
    assert 0 < scale < 1
    assert fixed.minimum_positivity_eigenvalue() >= -1e-12
    assert np.isclose(
        np.trace(fixed.joint_density_matrix()),
        np.trace(base.joint_density_matrix()),
    )
