from pathlib import Path

import pytest

from deuteron_wigner.canonical_composition import CanonicalCompositionGraph


ROOT = Path(__file__).resolve().parents[1]


def graph():
    return CanonicalCompositionGraph.from_json(
        ROOT / "validation/wp12_composition_manifest.json"
    )


def test_wp12_active_composition_is_nonoverlapping_and_evidenced():
    model = graph()
    active = model.active_ids()
    model.validate_selection(active)
    assert set(active) == {"wp12_resolved_constituent_parent"}
    for component in model.components.values():
        assert (ROOT / component.source_artifact).exists()


def test_wp12_generic_nnpi_and_shared_fock_cannot_double_count():
    model = graph()
    with pytest.raises(ValueError):
        model.validate_selection((
            "wp12_resolved_constituent_parent",
            "wp12_shared_fock_oam_sensitivity",
        ))
    with pytest.raises(ValueError):
        model.validate_selection((
            "wp12_lf_nuclear_parent", "wp12_sourced_nnpi",
            "wp12_generic_nnpi_interface",
        ))
