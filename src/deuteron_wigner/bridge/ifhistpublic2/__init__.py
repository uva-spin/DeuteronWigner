"""C98's deliberately narrow immutable historical theorem-input surface."""
from .core import historical_pair_normal_form, historical_pair_proof_inputs, historical_primitive_record

# The exact C98 public data surface is intentionally limited to these three
# authenticated retrieval methods.  Builder/validator support remains module-
# private in ``core`` and is never a fallback for an application query.
__all__ = ("historical_pair_normal_form", "historical_pair_proof_inputs", "historical_primitive_record")
