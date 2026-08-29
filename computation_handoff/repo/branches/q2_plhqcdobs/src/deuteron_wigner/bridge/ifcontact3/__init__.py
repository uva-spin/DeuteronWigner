"""C81 fail-closed composition audit for C78 support and C80 kernels."""

from .core import PairAggregationUnavailable, audit_pair_aggregation

__all__ = ["PairAggregationUnavailable", "audit_pair_aggregation"]
