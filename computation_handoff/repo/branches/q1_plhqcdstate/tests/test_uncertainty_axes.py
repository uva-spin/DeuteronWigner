import numpy as np
import pytest

from deuteron_wigner.uncertainty_axes import (
    EnsembleKind,
    JointProbabilityInput,
    SeparatedUncertaintyLedger,
    UncertaintyAxis,
    UncertaintyEnsemble,
)


def ensemble(axis):
    return UncertaintyEnsemble(
        name=axis.value,
        axis=axis,
        kind=EnsembleKind.CORRELATED_SCENARIOS,
        member_ids=("central", "variation"),
        source="controlled fixture",
        central_member="central",
        correlated_dimensions=("x", "flavor", "wave"),
    )


def test_all_required_uncertainty_axes_remain_separate():
    ledger = SeparatedUncertaintyLedger({
        axis.value: ensemble(axis) for axis in UncertaintyAxis
    })
    ledger.require_all_axes()
    assert ledger.axes == frozenset(UncertaintyAxis)
    with pytest.raises(ValueError, match="cannot be collapsed"):
        ledger.joint_covariance()


def test_sourced_joint_covariance_is_validated_and_explicit():
    ledger = SeparatedUncertaintyLedger({
        axis.value: ensemble(axis) for axis in UncertaintyAxis
    })
    joint = JointProbabilityInput(
        axes=(UncertaintyAxis.WAVE_FUNCTION, UncertaintyAxis.PDF_TMD_FIT),
        covariance=np.asarray(((1.0, 0.2), (0.2, 2.0))),
        source="controlled joint-fit fixture",
        parameter_labels=("wave_parameter", "fit_parameter"),
    )
    np.testing.assert_allclose(ledger.joint_covariance(joint), joint.covariance)
    with pytest.raises(ValueError, match="PSD"):
        JointProbabilityInput(
            axes=(UncertaintyAxis.WAVE_FUNCTION,),
            covariance=np.asarray(((1.0, 2.0), (2.0, 1.0))),
            source="bad fixture",
            parameter_labels=("a", "b"),
        )


def test_ensemble_preserves_member_identity_and_correlation_dimensions():
    item = ensemble(UncertaintyAxis.NUCLEAR_MECHANISM)
    assert item.central_member == "central"
    assert item.member_ids == ("central", "variation")
    assert "flavor" in item.correlated_dimensions
    with pytest.raises(ValueError, match="central member"):
        UncertaintyEnsemble(
            name="bad",
            axis=UncertaintyAxis.TRANSFORM,
            kind=EnsembleKind.CONVERGENCE_SEQUENCE,
            member_ids=("fine", "ultrafine"),
            source="fixture",
            central_member="missing",
            correlated_dimensions=("k",),
        )

