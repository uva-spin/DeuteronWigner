import numpy as np
import pytest

from deuteron_wigner.gluon_correlator import EPSILON_T
from deuteron_wigner.gluon_nuclear_mechanisms import (
    AdditionalGluonNuclearComponentInput,
    apply_gluon_nuclear_mechanisms,
    build_inclusive_gluon_antishadowing_input,
    build_inclusive_gluon_shadowing_input,
    build_polarized_tensor_gluon_shadowing_input,
)
from deuteron_wigner.nuclear_mechanisms import (
    DiffractiveShadowingInput,
    build_momentum_sum_antishadowing_input,
)
from deuteron_wigner.provenance import EvidenceClass, Mechanism, ValidityDomain
from deuteron_wigner.spin import project_matrix, spin_one_basis


def correlator(scale=1.0):
    basis = spin_one_basis()
    target = basis["U"] + 0.2 * basis["L"] + 0.1 * basis["LL"]
    transverse = (
        2.0 * np.eye(2)
        + 0.3j * EPSILON_T
        + np.asarray(((0.2, 0.1), (0.1, -0.2)))
    )
    return scale * np.einsum("IH,ij->IHij", target, transverse)


def test_empty_ledger_is_explicit_and_reconstructs_impulse():
    result = apply_gluon_nuclear_mechanisms(
        proton_impulse=correlator(),
        neutron_impulse=correlator(0.8),
        x=0.1,
        scale_gev=5.0,
    )
    assert set(result.corrections) == {
        "coherent_shadowing", "antishadowing", "off_shell",
        "meson_exchange", "non_nucleonic",
    }
    np.testing.assert_allclose(result.total, result.impulse)
    assert all(np.count_nonzero(item) == 0 for item in result.corrections.values())
    assert all(
        item.evidence == EvidenceClass.UNCONSTRAINED
        for item in result.provenance.values()
    )


def test_inclusive_shadowing_changes_only_target_u_gluon_trace():
    diffractive = DiffractiveShadowingInput(
        fraction=lambda sector, x, q: 0.04 if sector == "gluon" else 99.0,
        source="controlled gluon DPDF fixture",
        relative_uncertainty=0.2,
        classification=EvidenceClass.PHENOMENOLOGY,
        applies_longitudinal_coherence=False,
    )
    result = apply_gluon_nuclear_mechanisms(
        proton_impulse=correlator(),
        neutron_impulse=correlator(0.8),
        x=0.01,
        scale_gev=5.0,
        inputs={
            "coherent_shadowing": build_inclusive_gluon_shadowing_input(
                diffractive_input=diffractive
            )
        },
    )
    correction = result.corrections["coherent_shadowing"]
    u = spin_one_basis()["U"]
    for i in range(2):
        for j in range(2):
            for name, tensor in spin_one_basis().items():
                value = project_matrix(correction[:, :, i, j], tensor)
                if name != "U":
                    assert value == pytest.approx(0.0, abs=1e-14)
    u_gluon = np.asarray(
        [[project_matrix(correction[:, :, i, j], u) for j in range(2)] for i in range(2)]
    )
    np.testing.assert_allclose(u_gluon, np.eye(2) * u_gluon[0, 0])
    assert u_gluon[0, 0].real < 0.0
    np.testing.assert_allclose(
        result.total, result.total.transpose(1, 0, 3, 2).conj()
    )


def test_polarized_tensor_gluon_shadowing_resolves_target_and_gluon_channels():
    diffractive = DiffractiveShadowingInput(
        fraction=lambda sector, x, q: 0.04,
        source="controlled polarized gluon fixture",
        relative_uncertainty=0.2,
        classification=EvidenceClass.MODEL,
        applies_longitudinal_coherence=False,
    )
    shadow = build_polarized_tensor_gluon_shadowing_input(
        diffractive_input=diffractive,
        target_group_ratios={
            "U": 1.0, "L": 0.5, "T": 0.4, "LL": 1.5, "LT": 0.8, "TT": 0.7
        },
        gluon_polarization_ratios={
            "trace": 1.0, "circular": 0.6, "linear": 0.3
        },
    )
    result = apply_gluon_nuclear_mechanisms(
        proton_impulse=correlator(),
        neutron_impulse=correlator(0.8),
        x=0.01,
        scale_gev=5.0,
        inputs={"coherent_shadowing": shadow},
    )
    correction = result.corrections["coherent_shadowing"]
    basis = spin_one_basis()
    assert abs(project_matrix(correction[:, :, 0, 0], basis["LL"])) > 0.0
    assert abs(project_matrix(correction[:, :, 0, 0], basis["L"])) > 0.0
    u_projection = np.asarray(
        [
            [project_matrix(correction[:, :, i, j], basis["U"]) for j in range(2)]
            for i in range(2)
        ]
    )
    assert abs(u_projection[0, 1].imag) > 0.0
    assert abs((u_projection[0, 0] - u_projection[1, 1]).real) > 0.0
    np.testing.assert_allclose(
        correction, correction.transpose(1, 0, 3, 2).conj(), atol=1e-13
    )


def test_polarized_tensor_gluon_shadowing_rejects_incomplete_response_maps():
    with pytest.raises(ValueError, match="target ratios"):
        build_polarized_tensor_gluon_shadowing_input(
            target_group_ratios={"U": 1.0}
        )
    with pytest.raises(ValueError, match="gluon ratios"):
        build_polarized_tensor_gluon_shadowing_input(
            gluon_polarization_ratios={"trace": 1.0}
        )


def test_validity_zero_and_mechanism_identity_are_fail_closed():
    shadow = build_inclusive_gluon_shadowing_input()
    outside = apply_gluon_nuclear_mechanisms(
        proton_impulse=correlator(),
        neutron_impulse=correlator(0.8),
        x=0.5,
        scale_gev=5.0,
        inputs={"coherent_shadowing": shadow},
    )
    np.testing.assert_array_equal(outside.corrections["coherent_shadowing"], 0.0)
    with pytest.raises(ValueError, match="inconsistent mechanism"):
        apply_gluon_nuclear_mechanisms(
            proton_impulse=correlator(),
            neutron_impulse=correlator(),
            x=0.1,
            scale_gev=5.0,
            inputs={"off_shell": shadow},
        )


def test_gluon_antishadowing_uses_explicit_momentum_compensation():
    scalar = build_momentum_sum_antishadowing_input(
        lambda x, q: x**0.2 * (1.0 - x) ** 4,
        scale_gev=5.0,
        parton_sector="gluon",
        compensation_fraction=0.75,
    )
    result = apply_gluon_nuclear_mechanisms(
        proton_impulse=correlator(),
        neutron_impulse=correlator(0.8),
        x=0.12,
        scale_gev=5.0,
        inputs={
            "antishadowing": build_inclusive_gluon_antishadowing_input(scalar)
        },
    )
    correction = result.corrections["antishadowing"]
    assert np.linalg.norm(correction) > 0.0
    assert scalar.restored_momentum == pytest.approx(
        0.75 * scalar.lost_momentum
    )
    for i in range(2):
        for j in range(2):
            for name, tensor in spin_one_basis().items():
                if name != "U":
                    assert project_matrix(
                        correction[:, :, i, j], tensor
                    ) == pytest.approx(0.0, abs=1e-14)


def test_diffractive_named_members_propagate_as_full_correlators():
    diffractive = DiffractiveShadowingInput(
        fraction=lambda sector, x, q: 0.04,
        source="controlled member fixture",
        relative_uncertainty=0.5,
        classification=EvidenceClass.PHENOMENOLOGY,
        uncertainty_members={
            "low": lambda sector, x, q: 0.02,
            "high": lambda sector, x, q: 0.06,
        },
        applies_longitudinal_coherence=False,
    )
    result = apply_gluon_nuclear_mechanisms(
        proton_impulse=correlator(),
        neutron_impulse=correlator(0.8),
        x=0.01,
        scale_gev=5.0,
        inputs={
            "coherent_shadowing": build_inclusive_gluon_shadowing_input(
                diffractive_input=diffractive
            )
        },
    )
    members = result.uncertainty_corrections["coherent_shadowing"]
    assert set(members) == {"low", "high"}
    central_norm = np.linalg.norm(result.corrections["coherent_shadowing"])
    assert np.linalg.norm(members["low"]) == pytest.approx(0.5 * central_norm)
    assert np.linalg.norm(members["high"]) == pytest.approx(1.5 * central_norm)


def test_default_diffractive_input_materializes_declared_uncertainty_members():
    shadow = build_inclusive_gluon_shadowing_input()
    assert set(shadow.uncertainty_components) == {
        "shadowing_low", "shadowing_high"
    }


def test_bad_shape_nonhermitian_and_unknown_mechanisms_are_rejected():
    def nonhermitian(p, n, x, q):
        del p, n, x, q
        values = np.zeros((3, 3, 2, 2), complex)
        values[0, 1, 0, 0] = 1.0
        return values

    fixture = AdditionalGluonNuclearComponentInput(
        component=nonhermitian,
        source="bad controlled fixture",
        evidence=EvidenceClass.MODEL,
        mechanism=Mechanism.NON_NUCLEONIC,
        validity=ValidityDomain(0.01, 0.5, 2.0, 10.0),
        uncertainty_description="fixture",
    )
    with pytest.raises(ValueError, match="Hermitian"):
        apply_gluon_nuclear_mechanisms(
            proton_impulse=correlator(),
            neutron_impulse=correlator(),
            x=0.1,
            scale_gev=5.0,
            inputs={"non_nucleonic": fixture},
        )
    with pytest.raises(ValueError, match="unknown"):
        apply_gluon_nuclear_mechanisms(
            proton_impulse=correlator(),
            neutron_impulse=correlator(),
            x=0.1,
            scale_gev=5.0,
            inputs={"duplicate_shadowing": fixture},
        )
