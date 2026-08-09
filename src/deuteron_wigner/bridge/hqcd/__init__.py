"""C44/C46 physical projection gates; no unsupported QCD matrices are exported."""
from .preflight import projection_audit, assert_mode_projection_incomplete
from .c46_preflight import source_to_matrix_audit, assert_physical_basis_assembly_incomplete

__all__=["projection_audit","assert_mode_projection_incomplete","source_to_matrix_audit","assert_physical_basis_assembly_incomplete"]
