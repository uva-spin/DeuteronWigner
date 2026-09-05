"""Explicit K-local H0-to-C401/C410 basis-map contract.

The C7/C8 validation bases are not dimension-matched to the current C401/C410
coordinate spaces.  This module defines the evidence required before an H0
from one basis can be embedded into the other.  It intentionally has no
default map and does not authorize physical Hamiltonian use.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from typing import Any, Mapping

import numpy as np
from scipy import sparse


_CLAIM_TIERS = {"EXPLORATORY", "VALIDATED_MODEL", "PHYSICAL"}


def _as_square_sparse(value: Any, dimension: int, name: str) -> sparse.csr_matrix:
    if not sparse.issparse(value):
        value = sparse.csr_matrix(np.asarray(value, dtype=np.complex128))
    matrix = value.tocsr().astype(np.complex128)
    if matrix.shape != (dimension, dimension):
        raise ValueError(f"{name} must have shape {(dimension, dimension)}, got {matrix.shape}")
    if matrix.data.size and not np.all(np.isfinite(matrix.data)):
        raise ValueError(f"{name} contains nonfinite entries")
    return matrix


def _as_embedding(value: Any, target_dimension: int, source_dimension: int) -> sparse.csr_matrix:
    if not sparse.issparse(value):
        value = sparse.csr_matrix(np.asarray(value, dtype=np.complex128))
    matrix = value.tocsr().astype(np.complex128)
    expected = (target_dimension, source_dimension)
    if matrix.shape != expected:
        raise ValueError(f"embedding must have shape {expected}, got {matrix.shape}")
    if matrix.data.size and not np.all(np.isfinite(matrix.data)):
        raise ValueError("embedding contains nonfinite entries")
    return matrix


def _max_abs(value: sparse.spmatrix) -> float:
    value = value.tocsr()
    return float(np.max(np.abs(value.data))) if value.nnz else 0.0


@dataclass(frozen=True)
class H0BasisMapContract:
    """Evidence record for one explicit K-local basis embedding.

    ``embedding`` has shape ``(target_dimension, source_dimension)`` and maps
    source H0 coordinates into the target C401/C410 coordinate space.  The
    source labels are one-to-one labels for the source basis states; target
    labels are represented by the declared target-basis identity until the
    C401/C410 coordinate manifest is available.
    """

    resolution: str
    source_basis_id: str
    target_basis_id: str
    source_dimension: int
    target_dimension: int
    embedding: sparse.csr_matrix
    source_units: str
    target_units: str
    source_sector_labels: tuple[str, ...]
    omitted_sector_treatment: str
    hermiticity_test_id: str
    commutator_test_ids: tuple[str, ...]
    claim_tier: str = "EXPLORATORY"
    physical: bool = False
    source_certificate_id: str | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.resolution, str) or not self.resolution.strip():
            raise ValueError("resolution must identify one K-local space")
        for name, value in (
            ("source_dimension", self.source_dimension),
            ("target_dimension", self.target_dimension),
        ):
            if isinstance(value, bool) or not isinstance(value, int) or value < 1:
                raise ValueError(f"{name} must be a positive integer")
        embedding = _as_embedding(self.embedding, self.target_dimension, self.source_dimension)
        object.__setattr__(self, "embedding", embedding)
        for name, value in (
            ("source_basis_id", self.source_basis_id),
            ("target_basis_id", self.target_basis_id),
            ("source_units", self.source_units),
            ("target_units", self.target_units),
            ("omitted_sector_treatment", self.omitted_sector_treatment),
            ("hermiticity_test_id", self.hermiticity_test_id),
        ):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be a nonempty identity or policy")
        if len(self.source_sector_labels) != self.source_dimension:
            raise ValueError("source_sector_labels must label every source basis state")
        if any(not isinstance(label, str) or not label.strip() for label in self.source_sector_labels):
            raise ValueError("source_sector_labels must contain nonempty labels")
        if not self.commutator_test_ids or any(
            not isinstance(value, str) or not value.strip() for value in self.commutator_test_ids
        ):
            raise ValueError("at least one named commutator test is required")
        if self.claim_tier not in _CLAIM_TIERS:
            raise ValueError(f"claim_tier must be one of {sorted(_CLAIM_TIERS)}")
        if self.physical and self.claim_tier != "PHYSICAL":
            raise ValueError("physical=True requires claim_tier='PHYSICAL'")
        if self.claim_tier == "PHYSICAL" and not self.source_certificate_id:
            raise ValueError("a physical map requires an explicit source_certificate_id")

    @property
    def map_id(self) -> str:
        payload = repr(
            (
                self.resolution,
                self.source_basis_id,
                self.target_basis_id,
                self.source_dimension,
                self.target_dimension,
                self.source_units,
                self.target_units,
                self.source_sector_labels,
                self.omitted_sector_treatment,
                self.hermiticity_test_id,
                self.commutator_test_ids,
                self.claim_tier,
                self.physical,
                self.source_certificate_id,
                self.embedding.indptr.tolist(),
                self.embedding.indices.tolist(),
                self.embedding.data.tolist(),
            )
        ).encode()
        return "H0-BASIS-MAP:" + sha256(payload).hexdigest()[:20]

    @property
    def isometry_residual(self) -> float:
        gram = (self.embedding.getH() @ self.embedding).tocsr()
        gram.setdiag(gram.diagonal() - 1.0)
        gram.eliminate_zeros()
        return _max_abs(gram)

    @property
    def nonzero_count(self) -> int:
        return int(self.embedding.nnz)

    @property
    def target_support_count(self) -> int:
        return int(np.count_nonzero(np.asarray(self.embedding.getnnz(axis=1)).ravel()))

    def map_state(self, source_state: Any) -> np.ndarray:
        state = np.asarray(source_state, dtype=np.complex128)
        if state.shape != (self.source_dimension,):
            raise ValueError(
                f"source_state must have shape ({self.source_dimension},), got {state.shape}"
            )
        if not np.all(np.isfinite(state)):
            raise ValueError("source_state contains nonfinite entries")
        return np.asarray(self.embedding @ state, dtype=np.complex128)

    def embed_operator(self, source_operator: Any) -> sparse.csr_matrix:
        """Embed a source-basis sparse operator into target coordinates."""

        operator = _as_square_sparse(source_operator, self.source_dimension, "source_operator")
        result = (self.embedding @ operator @ self.embedding.getH()).tocsr()
        result.eliminate_zeros()
        return result

    def hermiticity_residual(self, source_operator: Any) -> float:
        embedded = self.embed_operator(source_operator)
        return _max_abs(embedded - embedded.getH())

    def commutator_residual(self, source_operator: Any, generator: Any) -> float:
        operator = _as_square_sparse(source_operator, self.source_dimension, "source_operator")
        conserved = _as_square_sparse(generator, self.source_dimension, "generator")
        return _max_abs(operator @ conserved - conserved @ operator)

    def validation_record(
        self,
        *,
        source_operator: Any | None = None,
        conserved_generators: Mapping[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Return a diagnostic record without promoting the map's claim tier."""

        record: dict[str, Any] = {
            "schema": "H0-BASIS-MAP-CONTRACT-V1",
            "map_id": self.map_id,
            "resolution": self.resolution,
            "source_basis_id": self.source_basis_id,
            "target_basis_id": self.target_basis_id,
            "shape": (self.target_dimension, self.source_dimension),
            "source_units": self.source_units,
            "target_units": self.target_units,
            "source_sector_labels": self.source_sector_labels,
            "omitted_sector_treatment": self.omitted_sector_treatment,
            "isometry_residual": self.isometry_residual,
            "nonzero_count": self.nonzero_count,
            "target_support_count": self.target_support_count,
            "hermiticity_test_id": self.hermiticity_test_id,
            "commutator_test_ids": self.commutator_test_ids,
            "claim_tier": self.claim_tier,
            "physical": self.physical,
            "source_certificate_id": self.source_certificate_id,
        }
        if source_operator is not None:
            record["source_operator_hermiticity_residual"] = _max_abs(
                _as_square_sparse(source_operator, self.source_dimension, "source_operator")
                - _as_square_sparse(source_operator, self.source_dimension, "source_operator").getH()
            )
            record["embedded_operator_hermiticity_residual"] = self.hermiticity_residual(source_operator)
        if conserved_generators is not None:
            record["commutator_residuals"] = {
                name: self.commutator_residual(source_operator, generator)
                for name, generator in conserved_generators.items()
            } if source_operator is not None else {}
        return record


__all__ = ["H0BasisMapContract"]
