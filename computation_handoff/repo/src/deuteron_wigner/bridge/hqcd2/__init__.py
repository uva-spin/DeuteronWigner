"""C48 local-QCD assembly gate.

This package deliberately exports a fail-closed source-sufficiency audit, not
an unsupported Hamiltonian or vertex matrix.
"""

from .preflight import (
    STATUS,
    canonical_vertex_audit,
    input_fidelity_audit,
    assert_canonical_vertex_assembly_incomplete,
)

__all__ = [
    "STATUS",
    "canonical_vertex_audit",
    "input_fidelity_audit",
    "assert_canonical_vertex_assembly_incomplete",
]
