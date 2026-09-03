import json
from pathlib import Path

import pytest

from deuteron_wigner.canonical_composition import (
    CanonicalCompositionGraph,
)


MANIFEST = Path("validation/canonical_composition_manifest.json")


def test_manifest_is_structurally_valid_and_artifacts_are_traced():
    graph = CanonicalCompositionGraph.from_json(MANIFEST)
    payload = json.loads(MANIFEST.read_text())
    assert payload["schema_version"] == 1
    assert len(graph.components) >= 16
    for item in graph.components.values():
        if item.source_artifact != "not_yet_generated":
            assert Path(item.source_artifact).exists()


def test_current_active_selection_is_unique_and_scheme_consistent():
    graph = CanonicalCompositionGraph.from_json(MANIFEST)
    graph.validate_selection(graph.active_ids())


def test_comparison_and_blocked_components_fail_closed():
    graph = CanonicalCompositionGraph.from_json(MANIFEST)
    with pytest.raises(ValueError, match="not canonical-selectable"):
        graph.validate_selection(["gluon_todd_spectator_downstream"])
    with pytest.raises(ValueError, match="not canonical-selectable"):
        graph.validate_selection(["gluon_todd_external_spectator_benchmark"])


def test_duplicate_physical_amplitude_is_rejected():
    graph = CanonicalCompositionGraph.from_json(MANIFEST)
    # Both alternatives deliberately carry the same gauge-link amplitude ID.
    first = graph.components["gluon_todd_cgi_gpm_comparison"]
    second = graph.components["gluon_todd_spectator_downstream"]
    hacked = {
        **graph.components,
        first.component_id: type(first)(
            **{**first.__dict__, "status": second.status.__class__("conditional"),
               "role": first.role.__class__("additive"),
               "scheme_id": graph.scheme_id}
        ),
        second.component_id: type(second)(
            **{**second.__dict__, "status": second.status.__class__("conditional"),
               "role": second.role.__class__("additive"),
               "scheme_id": graph.scheme_id}
        ),
    }
    conflicting = CanonicalCompositionGraph(hacked.values(), graph.scheme_id)
    with pytest.raises(ValueError, match="duplicated"):
        conflicting.validate_selection(
            [first.component_id, second.component_id]
        )


def test_blockers_are_executable_wp11_tasks():
    graph = CanonicalCompositionGraph.from_json(MANIFEST)
    blockers = graph.blockers()
    assert blockers == ()
    assert all(x.replacement_task.startswith("WP11-") for x in blockers)
