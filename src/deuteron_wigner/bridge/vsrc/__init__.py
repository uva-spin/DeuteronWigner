"""C50 source-qualified canonical q-to-qg vertex derivation.

This package exposes individual, color-stripped source-to-basis evaluations.
It deliberately does not assemble an exhaustive physical vertex matrix.
"""

from .core import (
    STATUS,
    evaluate_canonical_vertex,
    finite_box_pminus_kernel,
    pminus_to_m2,
    run_c50_checks,
)

__all__ = ["STATUS", "evaluate_canonical_vertex", "finite_box_pminus_kernel", "pminus_to_m2", "run_c50_checks"]
