"""C102 authenticated public facade for C94's unchanged theorem checker."""

from .core import (
    factorized_expansion_checker_contract,
    factorized_expansion_theorem_specification,
    load_verified_factorized_semantic_theorem_authority,
    verify_factorized_expansion_equivalence,
    verify_factorized_expansion_invocation,
    verify_factorized_semantic_theorem_authority,
)

__all__ = (
    "load_verified_factorized_semantic_theorem_authority",
    "verify_factorized_semantic_theorem_authority",
    "factorized_expansion_theorem_specification",
    "factorized_expansion_checker_contract",
    "verify_factorized_expansion_equivalence",
    "verify_factorized_expansion_invocation",
)
