from __future__ import annotations

import numpy as np
import pytest

from deuteron_wigner.bridge.c401_c396_mass_directions.basis import RESOLUTION_LABELS
from deuteron_wigner.bridge.c410_c117_i2_retained_aggregation_boundary import (
    source_reduced_c117_i2_shape_csr,
)
from deuteron_wigner.bridge.c411_c117_i2_finite_c43_adapter import (
    EXPLORATORY_CLAIM_TIER,
    ExploratoryC1171Parameters,
    apply_exploratory_c117_1,
    exploratory_action_record,
    exploratory_c117_1_csr,
    exploratory_parameter_record,
    pminus_to_m2_factor,
)


def _parameters(resolution: str) -> ExploratoryC1171Parameters:
    return ExploratoryC1171Parameters(
        resolution=resolution,
        residual_normalization=1.25,
        mixing_coefficient=-0.8,
    )


@pytest.mark.parametrize("resolution", RESOLUTION_LABELS)
def test_exploratory_action_scales_live_c410_shape(resolution: str) -> None:
    source = source_reduced_c117_i2_shape_csr(resolution)
    parameters = _parameters(resolution)
    action = exploratory_c117_1_csr(parameters)
    assert action.shape == source.shape
    assert np.linalg.norm((action - (-1.0 * source)).data) == 0.0
    assert np.linalg.norm((action - action.getH()).data) == 0.0


@pytest.mark.parametrize("resolution", RESOLUTION_LABELS)
def test_exploratory_matrix_free_action_matches_sparse(resolution: str) -> None:
    parameters = _parameters(resolution)
    matrix = exploratory_c117_1_csr(parameters)
    rng = np.random.default_rng(41101 + RESOLUTION_LABELS.index(resolution))
    vector = rng.normal(size=matrix.shape[1]) + 1j * rng.normal(size=matrix.shape[1])
    residual = np.linalg.norm(
        matrix @ vector - apply_exploratory_c117_1(parameters, vector)
    )
    assert residual < 5e-10


def test_conversion_is_exact_and_requires_explicit_cell_length() -> None:
    assert pminus_to_m2_factor("K9", 2.0) == pytest.approx(4.5 * np.pi)
    assert pminus_to_m2_factor("K11", 2.0) == pytest.approx(5.5 * np.pi)
    assert pminus_to_m2_factor("K13", 2.0) == pytest.approx(6.5 * np.pi)
    with pytest.raises(ValueError, match="positive"):
        pminus_to_m2_factor("K9", 0.0)


def test_records_keep_the_exploratory_claim_boundary() -> None:
    parameters = _parameters("K9")
    parameter_record = exploratory_parameter_record(parameters)
    action_record = exploratory_action_record(parameters)
    assert parameter_record["claim_tier"] == EXPLORATORY_CLAIM_TIER
    assert parameter_record["physical"] is False
    assert parameter_record["source_minus_one_half_applied_once"] is True
    assert parameter_record["g_s_squared"] == "FACTORED_NOT_NUMERIC"
    assert parameter_record["Pminus_to_M2"]["applied_to_C410_shape"] is False
    assert action_record["claim_tier"] == EXPLORATORY_CLAIM_TIER
    assert action_record["C411_certificate_supplied"] is False
    assert action_record["complete_C117_numerical_coordinate_action"] is False
    assert action_record["hamiltonian_activation"] is False


def test_unknown_factors_cannot_be_undocumented_zeroes() -> None:
    with pytest.raises(ValueError, match="nonzero"):
        ExploratoryC1171Parameters("K9", 0.0, 1.0)
    with pytest.raises(ValueError, match="nonzero"):
        ExploratoryC1171Parameters("K9", 1.0, 0.0)
    with pytest.raises(ValueError, match="resolution"):
        ExploratoryC1171Parameters("K15", 1.0, 1.0)


def test_input_validation_rejects_nonfinite_vectors() -> None:
    parameters = _parameters("K9")
    matrix = exploratory_c117_1_csr(parameters)
    vector = np.zeros(matrix.shape[1], dtype=np.complex128)
    vector[0] = np.nan
    with pytest.raises(ValueError, match="nonfinite"):
        apply_exploratory_c117_1(parameters, vector)
