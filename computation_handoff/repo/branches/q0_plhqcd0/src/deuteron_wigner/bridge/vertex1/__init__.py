"""C49 canonical-vertex source-chain gate; no vertex matrix is exported."""

from .audit import (
    STATUS,
    assert_canonical_source_chain_incomplete,
    raw_tuple_semantics_summary,
    source_sufficiency_matrix,
)

__all__ = ["STATUS", "assert_canonical_source_chain_incomplete", "raw_tuple_semantics_summary", "source_sufficiency_matrix"]
