import numpy as np
import pytest

from deuteron_wigner.oam_interference import (
    InterferenceKind,
    LFPartialWaveAmplitude,
    OAMInterferenceModel,
    OAMInterferenceTerm,
    build_pdf_anchored_oam_model,
)
from deuteron_wigner.provenance import ValidityDomain


def model():
    waves = {
        "L0": LFPartialWaveAmplitude(
            "L0", 0, 1,
            lambda nucleon, flavor, x, k, q: (1 + 0.1 * flavor) * np.exp(-k),
            "controlled S-like LF wave",
        ),
        "L1": LFPartialWaveAmplitude(
            "L1", 1, -1,
            lambda nucleon, flavor, x, k, q: 1j * 0.2 * flavor * k * np.exp(-k),
            "controlled relativistic P-like LF wave",
        ),
        "L2": LFPartialWaveAmplitude(
            "L2", 2, 1,
            lambda nucleon, flavor, x, k, q: 0.1 * k**2 * np.exp(-k),
            "controlled D-like LF wave",
        ),
    }
    terms = (
        OAMInterferenceTerm("L0", "L1", InterferenceKind.T_ODD_IMAGINARY, 1.0, "f1Tperp"),
        OAMInterferenceTerm("L0", "L1", InterferenceKind.T_EVEN_REAL, 0.7, "g1T"),
        OAMInterferenceTerm("L0", "L2", InterferenceKind.T_EVEN_REAL, 1.0, "h1Tperp"),
    )
    return OAMInterferenceModel(waves, terms)


def test_oam_rank_and_rotation_harmonics_are_explicit():
    instance = model()
    assert [instance.rank(term) for term in instance.terms] == [1, 1, 2]
    at_zero = instance.value(
        "h1Tperp", nucleon="proton", flavor=2,
        x=0.1, k_gev=0.4, q_gev=5.0, azimuth=0.0,
    )
    at_quarter_turn = instance.value(
        "h1Tperp", nucleon="proton", flavor=2,
        x=0.1, k_gev=0.4, q_gev=5.0, azimuth=np.pi / 2,
    )
    assert at_quarter_turn == pytest.approx(-at_zero)


def test_todd_phase_reverses_while_teven_does_not():
    instance = model()
    common = dict(
        nucleon="proton", flavor=2, x=0.1, k_gev=0.4, q_gev=5.0,
        azimuth=0.0,
    )
    future = instance.value("f1Tperp", **common, staple_orientation=1.0)
    past = instance.value("f1Tperp", **common, staple_orientation=-1.0)
    assert future != 0.0
    assert past == pytest.approx(-future)
    assert instance.value("h1Tperp", **common, staple_orientation=1.0) == pytest.approx(
        instance.value("h1Tperp", **common, staple_orientation=-1.0)
    )


def test_interference_vanishes_when_either_wave_is_disabled():
    instance = model()
    common = dict(
        nucleon="proton", flavor=2, x=0.1, k_gev=0.4, q_gev=5.0,
    )
    assert instance.value("f1Tperp", **common) != 0.0
    assert instance.disable_wave("L0").value("f1Tperp", **common) == 0.0
    assert instance.disable_wave("L1").value("f1Tperp", **common) == 0.0


def test_nonfinite_amplitudes_and_invalid_staples_fail_closed():
    instance = model()
    with pytest.raises(ValueError, match="simple staple"):
        instance.value(
            "f1Tperp", nucleon="proton", flavor=2,
            x=0.1, k_gev=0.4, q_gev=5.0, staple_orientation=0.0,
        )


def test_oam_full_momentum_adapter_preserves_staple_reversal():
    instance = model()
    validity = ValidityDomain(0.01, 0.8, 2.0, 10.0, 1.5, "SIDIS")
    future = instance.fitted_momentum_input(
        "f1Tperp",
        source="controlled partial-wave model",
        process_reference="future-pointing SIDIS staple",
        validity=validity,
        staple_orientation=1.0,
    )
    past = instance.fitted_momentum_input(
        "f1Tperp",
        source="controlled partial-wave model",
        process_reference="past-pointing DY staple",
        validity=validity,
        staple_orientation=-1.0,
    )
    arguments = ("proton", 2, 0.1, 0.4, 5.0)
    assert future.value(*arguments) == pytest.approx(-past.value(*arguments))
    assert future.provenance.replaceable_interface == "OAMInterferenceModel"


def test_oam_scalar_adapter_matches_direct_transverse_integral():
    instance = model()
    fitted = instance.fitted_scalar_input(
        "h1Tperp",
        source="controlled partial-wave model",
        validity=ValidityDomain(0.01, 0.8, 2.0, 10.0, 1.5),
        transverse_cutoff_gev=1.5,
        quadrature_nodes=96,
    )
    nodes, weights = np.polynomial.legendre.leggauss(128)
    k = 0.75 * (nodes + 1.0)
    direct = np.dot(
        0.75 * weights,
        [
            2.0 * np.pi * value * instance.value(
                "h1Tperp", nucleon="proton", flavor=2,
                x=0.1, k_gev=float(value), q_gev=5.0,
            )
            for value in k
        ],
    )
    assert fitted.value("proton", 2, 0.1, 5.0) == pytest.approx(direct, rel=2e-11)
    with pytest.raises(ValueError, match="full momentum"):
        instance.fitted_scalar_input(
            "f1Tperp",
            source="controlled",
            validity=ValidityDomain(0.01, 0.8, 2.0, 10.0, 1.5),
            transverse_cutoff_gev=1.5,
        )


def test_pdf_anchored_oam_model_has_independent_flavor_and_phase_sectors():
    anchored = build_pdf_anchored_oam_model(
        lambda nucleon, flavor, x, q: (
            (4.0 if nucleon == "proton" else 3.0)
            * (1.0 + 0.1 * flavor)
            * (1.0 - x) ** 3
        ),
        transverse_width_gev2={2: 0.28, 1: 0.32, -2: 0.36, -1: 0.39},
    )
    common = dict(nucleon="proton", x=0.1, k_gev=0.35, q_gev=5.0)
    assert anchored.value("g1T", flavor=2, **common) > 0.0
    assert anchored.value("g1T", flavor=1, **common) < 0.0
    assert anchored.value("h1Tperp", flavor=2, **common) < 0.0
    future = anchored.value("f1Tperp", flavor=2, **common)
    past = anchored.value(
        "f1Tperp", flavor=2, **common, staple_orientation=-1.0
    )
    assert future == pytest.approx(-past)
    assert anchored.disable_wave("P_odd").value(
        "f1Tperp", flavor=2, **common
    ) == 0.0
