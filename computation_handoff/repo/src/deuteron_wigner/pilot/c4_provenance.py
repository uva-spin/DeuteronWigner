"""Deterministic, production-disjoint C4 validation provenance."""

from __future__ import annotations

from ..formal.diagnostics import ArchitectureError
from ..formal.provenance_graph import (
    CompositionPlan, NodeKind, ProvenanceEdge, ProvenanceGraph,
    ProvenanceNode, Relation, SelectionRole,
)


def c4_provenance_graph() -> ProvenanceGraph:
    node_specs = (
        ("c4:state:valence", NodeKind.COMPONENT, "C3 valence state"),
        ("c4:state:sea-explicit", NodeKind.COMPONENT, "explicit qqqq-qbar state"),
        ("c4:parent:antiquark", NodeKind.OPERATOR, "positive-x antiquark parent"),
        ("c4:state:gluon-explicit", NodeKind.COMPONENT, "explicit qqqg state"),
        ("c4:parent:gluon", NodeKind.OPERATOR, "diagonal adjoint gluon parent"),
        ("c4:route:tmd", NodeKind.PROJECTION, "regulated TMD route"),
        ("c4:route:gpd", NodeKind.PROJECTION, "regulated analytic GPD route"),
        ("c4:route:pdf", NodeKind.PROJECTION, "regulated PDF route"),
        ("c4:route:current", NodeKind.PROJECTION, "local current/EMT route"),
        ("c4:closure:sea", NodeKind.EVIDENCE, "sea route closure"),
        ("c4:closure:gluon", NodeKind.EVIDENCE, "gluon route closure"),
        ("c4:feshbach", NodeKind.BENCHMARK, "finite Feshbach model"),
        ("c4:induced:sea", NodeKind.OPERATOR, "induced sea operator plus remainder"),
        ("c4:induced:gluon", NodeKind.OPERATOR, "induced gluon operator plus remainder"),
        ("c4:remainder:sea", NodeKind.COMPONENT, "declared sea matching remainder"),
        ("c4:remainder:gluon", NodeKind.COMPONENT, "declared gluon matching remainder"),
    )
    nodes = []
    for stable_id, kind, identity in node_specs:
        group = None
        if stable_id in ("c4:state:sea-explicit", "c4:induced:sea"):
            group = "c4:sea-representation"
        if stable_id in ("c4:state:gluon-explicit", "c4:induced:gluon"):
            group = "c4:gluon-representation"
        nodes.append(ProvenanceNode(
            stable_id, kind, identity, SelectionRole.BENCHMARK_ONLY,
            alternative_group=group, central_allowed=False,
        ))
    edges = [
        ProvenanceEdge("c4:parent:antiquark", "c4:state:sea-explicit", Relation.DERIVES_FROM, "explicit positive-x antiquark slot"),
        ProvenanceEdge("c4:parent:gluon", "c4:state:gluon-explicit", Relation.DERIVES_FROM, "explicit transverse gluon slot"),
        ProvenanceEdge("c4:route:tmd", "c4:parent:antiquark", Relation.PROJECTS_TO, "forward limit"),
        ProvenanceEdge("c4:route:gpd", "c4:parent:antiquark", Relation.PROJECTS_TO, "regulated kT integral"),
        ProvenanceEdge("c4:route:pdf", "c4:route:tmd", Relation.DERIVES_FROM, "TMD integral"),
        ProvenanceEdge("c4:route:current", "c4:route:gpd", Relation.DERIVES_FROM, "Mellin moment"),
        ProvenanceEdge("c4:closure:sea", "c4:route:pdf", Relation.VALIDATES, "sea commuting routes"),
        ProvenanceEdge("c4:closure:gluon", "c4:parent:gluon", Relation.VALIDATES, "gluon commuting routes"),
        ProvenanceEdge("c4:induced:sea", "c4:feshbach", Relation.DERIVES_FROM, "finite retained-space elimination"),
        ProvenanceEdge("c4:induced:gluon", "c4:feshbach", Relation.DERIVES_FROM, "finite retained-space elimination"),
        ProvenanceEdge("c4:state:sea-explicit", "c4:induced:sea", Relation.ALTERNATIVE_TO, "same higher-sector physics"),
        ProvenanceEdge("c4:state:sea-explicit", "c4:induced:sea", Relation.EXCLUDES, "prevent explicit/induced double counting"),
        ProvenanceEdge("c4:state:gluon-explicit", "c4:induced:gluon", Relation.ALTERNATIVE_TO, "same higher-sector physics"),
        ProvenanceEdge("c4:state:gluon-explicit", "c4:induced:gluon", Relation.EXCLUDES, "prevent explicit/induced double counting"),
        ProvenanceEdge("c4:induced:sea", "c4:remainder:sea", Relation.DERIVES_FROM, "operator plus declared remainder"),
        ProvenanceEdge("c4:induced:gluon", "c4:remainder:gluon", Relation.DERIVES_FROM, "operator plus declared remainder"),
    ]
    return ProvenanceGraph(nodes, edges)


def explicit_plan() -> CompositionPlan:
    return CompositionPlan(
        "c4:plan:explicit",
        ("c4:state:valence", "c4:state:sea-explicit", "c4:state:gluon-explicit"),
        central=False,
    )


def induced_plan() -> CompositionPlan:
    return CompositionPlan(
        "c4:plan:induced",
        ("c4:state:valence", "c4:induced:sea", "c4:induced:gluon"),
        central=False,
    )


def require_c4_isolated(accepted: ProvenanceGraph, c4: ProvenanceGraph) -> None:
    overlap = set(accepted.nodes) & set(c4.nodes)
    if overlap:
        raise ArchitectureError(
            "C4.ISOLATE.PROVENANCE", "C4 shares a production node identity",
            expected="disjoint identities", received=tuple(sorted(overlap)),
        )
    for edge in (*accepted.edges, *c4.edges):
        if (
            edge.source in accepted.nodes and edge.target in c4.nodes
        ) or (
            edge.source in c4.nodes and edge.target in accepted.nodes
        ):
            raise ArchitectureError(
                "C4.ISOLATE.PROVENANCE", "C4 can reach production root",
                expected="no cross-graph edge", received=(edge.source, edge.target),
            )
