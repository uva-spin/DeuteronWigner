"""C44 fail-closed physical-mode projection gate; no QCD matrices are exported."""
from .preflight import projection_audit, assert_mode_projection_incomplete

__all__=["projection_audit","assert_mode_projection_incomplete"]
