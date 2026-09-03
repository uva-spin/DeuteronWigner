import numpy as np
import pytest

from deuteron_wigner.joint_positivity import (
    audit_gluon_correlator_members,
    refuse_projection_only_joint_audit,
)
from deuteron_wigner.quark_correlator import Spin1QuarkCorrelator
from deuteron_wigner.uncertainty_validation import (
    minimum_eigenvalues_under_correlated_replacements,
)


def density_matrix(value):
    return value * np.einsum(
        "IH,ij->IHij", np.eye(3, dtype=complex), np.eye(2, dtype=complex)
    )


def test_member_identity_and_tensions_are_reported_without_clipping():
    bad = density_matrix(1.0)
    bad[0, 0, 0, 0] = -0.2
    audit = audit_gluon_correlator_members({
        "central": [density_matrix(1.0), density_matrix(0.5)],
        "tension": [bad],
    })
    assert [item.member for item in audit.members] == ["central", "tension"]
    assert audit.members[0].compatible
    assert not audit.members[1].compatible
    assert audit.members[1].violating_points == 1
    assert audit.global_minimum_eigenvalue < 0.0
    assert not audit.tensions_are_clipped


def test_projection_only_ensemble_cannot_claim_joint_positivity():
    with pytest.raises(ValueError, match="missing reconstructing TMDs"):
        refuse_projection_only_joint_audit(
            available_tmds=("f1", "g1"),
            required_identifiable_tmds=("f1", "g1", "h1perp"),
            ensemble_name="fixture bands",
        )
    with pytest.raises(ValueError, match="full matrices"):
        refuse_projection_only_joint_audit(
            available_tmds=("f1", "g1", "h1perp"),
            required_identifiable_tmds=("f1", "g1", "h1perp"),
            ensemble_name="fixture bands",
        )


def test_correlated_multi_component_replacement_preserves_member_pairing():
    zero = np.zeros((3, 3), dtype=np.complex128)
    central = Spin1QuarkCorrelator(2 * np.eye(3), zero, np.zeros((2, 3, 3)))
    component_a = Spin1QuarkCorrelator(np.eye(3), zero, np.zeros((2, 3, 3)))
    component_b = Spin1QuarkCorrelator(zero, np.eye(3), np.zeros((2, 3, 3)))
    minima = minimum_eigenvalues_under_correlated_replacements(
        central,
        {"a": component_a, "b": component_b},
        {"a": 0.0, "b": 0.0},
        {"a": np.array([0.1, 0.2]), "b": np.array([-0.1, -0.2])},
    )
    assert minima.shape == (2,)
    assert np.isfinite(minima).all()
