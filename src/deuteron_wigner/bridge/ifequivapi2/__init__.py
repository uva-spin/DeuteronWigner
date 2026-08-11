"""C94 immutable public facade over the C93 recovered-preimage capsule."""

from .core import (
    expansion_theorem_specification, historical_pair_attestation, historical_pair_by_sequence,
    historical_pair_count, historical_pair_page, historical_primitive_family, historical_primitive_page,
    load_verified_c93_public_authority, verify_factorized_expansion_equivalence,
)

__all__ = (
    "expansion_theorem_specification", "historical_pair_attestation", "historical_pair_by_sequence",
    "historical_pair_count", "historical_pair_page", "historical_primitive_family", "historical_primitive_page",
    "load_verified_c93_public_authority", "verify_factorized_expansion_equivalence",
)
