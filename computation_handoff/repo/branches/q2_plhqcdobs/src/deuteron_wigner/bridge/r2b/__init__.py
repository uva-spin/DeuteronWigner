"""C41 fail-closed fidelity audit for C40 numerical substrate."""
from .audit import audit_c40_substrate, assert_c40_not_eligible

__all__ = ["audit_c40_substrate", "assert_c40_not_eligible"]
