"""Isolated C5 provenance subgraph with executable cut equivalence."""

from __future__ import annotations

from ...formal.diagnostics import ArchitectureError


NODES = (
    "C5:ANALYTIC_STATE", "C5:BARE_WILSON_PATH", "C5:EIKONAL_POLE",
    "C5:LF_RESOLVENT", "C5:CUT_LEDGER", "C5:ONE_GLUON_KERNEL",
    "C5:FUTURE_AMPLITUDE", "C5:PAST_AMPLITUDE",
    "C5:ANTIUNITARY_ADAPTER", "C5:LINK_ODD_CORRELATOR",
    "C5:SIVERS_LIKE", "C5:BOER_MULDERS_LIKE", "C5:PHASE_BUDGET",
    "C5:UV_MATCHING_REQUIRED", "C5:RAPIDITY_SOFT_REQUIRED",
    "C5:LINK_SHORTENING_REQUIRED", "C5:PRODUCTION_EXCLUSION",
)

EDGES = (
    ("C5:ANALYTIC_STATE", "DERIVES_FROM_READ_ONLY", "C3:C:SPINOR_OAM"),
    ("C5:ONE_GLUON_KERNEL", "ACTS_ON", "C5:ANALYTIC_STATE"),
    ("C5:ONE_GLUON_KERNEL", "USES", "C5:BARE_WILSON_PATH"),
    ("C5:ONE_GLUON_KERNEL", "USES", "C5:EIKONAL_POLE"),
    ("C5:ONE_GLUON_KERNEL", "USES", "C5:LF_RESOLVENT"),
    ("C5:ONE_GLUON_KERNEL", "USES", "C5:CUT_LEDGER"),
    ("C5:LINK_ODD_CORRELATOR", "DERIVES_FROM", "C5:FUTURE_AMPLITUDE"),
    ("C5:LINK_ODD_CORRELATOR", "DERIVES_FROM_THETA_MAPPED", "C5:PAST_AMPLITUDE"),
    ("C5:SIVERS_LIKE", "PROJECTS_FROM", "C5:LINK_ODD_CORRELATOR"),
    ("C5:BOER_MULDERS_LIKE", "PROJECTS_FROM", "C5:LINK_ODD_CORRELATOR"),
    ("C5:SIVERS_LIKE", "ALTERNATIVE_OPERATOR_PROJECTION_TO", "C5:BOER_MULDERS_LIKE"),
    ("C5:PHASE_BUDGET", "REQUIRES_MATCHING", "C5:UV_MATCHING_REQUIRED"),
    ("C5:PHASE_BUDGET", "REQUIRES_MATCHING", "C5:RAPIDITY_SOFT_REQUIRED"),
    ("C5:PHASE_BUDGET", "REQUIRES_MATCHING", "C5:LINK_SHORTENING_REQUIRED"),
    ("C5:ONE_GLUON_KERNEL", "EXCLUDED_FROM", "C5:PRODUCTION_EXCLUSION"),
)


def graph_dict() -> dict[str, object]:
    return {
        "nodes": [{"stable_id": item, "scope": "C5_VALIDATION_ONLY"} for item in NODES],
        "edges": [{"source": source, "relation": relation, "target": target} for source, relation, target in EDGES],
        "general_provenance_2_complex_complete": False,
        "executable_two_cells": ["CUT_EQUIVALENT_COUNT_ONCE", "CUT_SUBTRACTED"],
    }


def require_isolation(production_nodes: set[str]) -> None:
    overlap = production_nodes.intersection(NODES)
    if overlap:
        raise ArchitectureError("C5.ISOLATE", "C5 provenance entered accepted production graph", expected="disjoint nodes", received=sorted(overlap))
