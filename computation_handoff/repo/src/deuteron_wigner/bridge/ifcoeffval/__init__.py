"""C106 executable coefficient authority (fail-closed on missing bindings)."""
from .core import (
    STATUS, load_verified_projected_coefficient_authority,
    verify_projected_coefficient_authority, evaluate_projected_coefficient,
    evaluate_coefficient_bound, coefficient_expression,
)

__all__ = ["STATUS", "load_verified_projected_coefficient_authority",
           "verify_projected_coefficient_authority",
           "evaluate_projected_coefficient", "evaluate_coefficient_bound",
           "coefficient_expression"]
