"""Isolation proof for the validation-only pilot provenance graph."""

from __future__ import annotations

from ..formal.diagnostics import ArchitectureError
from ..formal.provenance_graph import (
    NodeKind, ProvenanceEdge, ProvenanceGraph, ProvenanceNode, Relation,
    SelectionRole,
)


def pilot_provenance_graph() -> ProvenanceGraph:
    nodes = []
    edges = []
    for benchmark in ("A", "B", "C", "D"):
        root = f"c3:benchmark:{benchmark}"
        state = f"c3:state:{benchmark}"
        recoil = f"c3:recoil:{benchmark}"
        kernel = f"c3:kernel:{benchmark}"
        result = f"c3:result:{benchmark}"
        nodes.extend((
            ProvenanceNode(root, NodeKind.BENCHMARK, f"analytic benchmark {benchmark}", SelectionRole.BENCHMARK_ONLY, central_allowed=False),
            ProvenanceNode(state, NodeKind.COMPONENT, f"validation state {benchmark}", SelectionRole.BENCHMARK_ONLY, central_allowed=False),
            ProvenanceNode(recoil, NodeKind.COMPONENT, "SYMMETRIC_XI0", SelectionRole.BENCHMARK_ONLY, central_allowed=False),
            ProvenanceNode(kernel, NodeKind.OPERATOR, "zeroth-rescattering overlap", SelectionRole.BENCHMARK_ONLY, central_allowed=False),
            ProvenanceNode(result, NodeKind.FINAL_ARTIFACT, f"validation result {benchmark}", SelectionRole.BENCHMARK_ONLY, central_allowed=False),
        ))
        edges.extend((
            ProvenanceEdge(result, root, Relation.DERIVES_FROM, "validation benchmark result"),
            ProvenanceEdge(root, state, Relation.DERIVES_FROM, "analytic state source"),
            ProvenanceEdge(root, recoil, Relation.DERIVES_FROM, "single recoil authority"),
            ProvenanceEdge(root, kernel, Relation.DERIVES_FROM, "common overlap kernel"),
        ))
    return ProvenanceGraph(nodes, edges)


def require_isolated(accepted: ProvenanceGraph, pilot: ProvenanceGraph) -> None:
    overlap = set(accepted.nodes) & set(pilot.nodes)
    if overlap:
        raise ArchitectureError("C3.ISOLATE.PROVENANCE", "pilot shares accepted node identity", expected="disjoint graphs", received=tuple(sorted(overlap)))
    for edge in (*accepted.edges, *pilot.edges):
        if (edge.source in accepted.nodes and edge.target in pilot.nodes) or (edge.source in pilot.nodes and edge.target in accepted.nodes):
            raise ArchitectureError("C3.ISOLATE.PROVENANCE", "pilot reachable from accepted graph", expected="no cross-graph edge", received=(edge.source, edge.target))
