"""C45 source-derived one-particle light-front mode library.

This package deliberately stops before constructing any many-body or
interaction matrix.  It supplies only finite-projection ingredients for the
subsequent C46 action projection.
"""

from .core import (
    STATUS,
    RESOLUTIONS,
    build_library,
    validate_library,
    projection_contract_matrix,
)

__all__ = ["STATUS", "RESOLUTIONS", "build_library", "validate_library", "projection_contract_matrix"]
