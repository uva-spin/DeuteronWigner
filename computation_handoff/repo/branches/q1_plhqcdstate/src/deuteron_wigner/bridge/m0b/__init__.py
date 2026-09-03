"""C40 executable finite-basis partonic operator substrate.

This package deliberately stops before bare one-loop correlators and any
matching calculation.  Its public entry point is :func:`build_bundle`.
"""
from .basis import RESOLUTIONS, build_basis
from .readiness import build_bundle, readiness_report, assert_ready

__all__ = ["RESOLUTIONS", "build_basis", "build_bundle", "readiness_report", "assert_ready"]
