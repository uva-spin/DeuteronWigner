"""Immutable C103 historical-descendant factorized-semantic equivalence API."""
from .core import (
    descendant_pair_attestation,
    diagnose_pair_difference,
    historical_pair_attestation,
    load_verified_historical_descendant_equivalence,
    pair_equivalence,
    pair_equivalence_proof,
    primitive_equivalence,
    scientific_equivalence_decision,
    verify_historical_descendant_equivalence_root,
)

__all__ = (
    "load_verified_historical_descendant_equivalence",
    "verify_historical_descendant_equivalence_root",
    "scientific_equivalence_decision",
    "pair_equivalence", "historical_pair_attestation", "descendant_pair_attestation",
    "pair_equivalence_proof", "primitive_equivalence", "diagnose_pair_difference",
)
