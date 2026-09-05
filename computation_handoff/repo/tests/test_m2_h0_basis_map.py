from __future__ import annotations

import numpy as np
import pytest
from scipy import sparse

from deuteron_wigner.microscopic.h0 import H0BasisMapContract


def _contract() -> H0BasisMapContract:
    embedding = sparse.csr_matrix(
        (
            np.ones(3, dtype=np.complex128),
            (np.array([0, 3, 7]), np.array([0, 1, 2])),
        ),
        shape=(10, 3),
    )
    return H0BasisMapContract(
        resolution="K9",
        source_basis_id="TEST_SOURCE_H0",
        target_basis_id="C401_C410_K9_COORDINATES",
        source_dimension=3,
        target_dimension=10,
        embedding=embedding,
        source_units="GeV^2",
        target_units="GeV^2",
        source_sector_labels=("qqq", "qqq", "qqqg"),
        omitted_sector_treatment="NOT_SUPPLIED_UNTIL_SOURCE_QUALIFIED",
        hermiticity_test_id="TEST_HERMITICITY",
        commutator_test_ids=("TEST_CHARGE_COMMUTATOR", "TEST_JZ_COMMUTATOR"),
    )


def test_explicit_map_is_isometric_and_records_target_support() -> None:
    contract = _contract()
    assert contract.isometry_residual == 0.0
    assert contract.nonzero_count == 3
    assert contract.target_support_count == 3
    assert contract.map_state([1.0, 2.0, 3.0]).tolist() == [1.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 3.0, 0.0, 0.0]


def test_operator_embedding_preserves_hermiticity_and_commuting_generator() -> None:
    contract = _contract()
    operator = sparse.diags([1.0, 2.0, 3.0], format="csr")
    generator = sparse.diags([0.0, 1.0, 2.0], format="csr")
    record = contract.validation_record(
        source_operator=operator,
        conserved_generators={"JZ": generator},
    )
    assert record["source_operator_hermiticity_residual"] == 0.0
    assert record["embedded_operator_hermiticity_residual"] == 0.0
    assert record["commutator_residuals"]["JZ"] == 0.0
    assert record["claim_tier"] == "EXPLORATORY"
    assert record["physical"] is False


def test_map_requires_full_source_labels_and_named_commutator_evidence() -> None:
    values = _contract().__dict__
    values["source_sector_labels"] = ("qqq",)
    with pytest.raises(ValueError, match="source_sector_labels"):
        H0BasisMapContract(**values)
    values = _contract().__dict__
    values["commutator_test_ids"] = ()
    with pytest.raises(ValueError, match="commutator"):
        H0BasisMapContract(**values)


def test_non_isometric_map_is_reported_without_being_promoted() -> None:
    values = _contract().__dict__
    values["embedding"] = sparse.csr_matrix(np.array([[2.0, 0.0, 0.0]] + [[0.0, 0.0, 0.0]] * 9))
    contract = H0BasisMapContract(**values)
    assert contract.isometry_residual == 3.0
    assert contract.validation_record()["claim_tier"] == "EXPLORATORY"


def test_physical_map_requires_source_certificate() -> None:
    values = _contract().__dict__
    values["claim_tier"] = "PHYSICAL"
    values["physical"] = True
    with pytest.raises(ValueError, match="source_certificate_id"):
        H0BasisMapContract(**values)
