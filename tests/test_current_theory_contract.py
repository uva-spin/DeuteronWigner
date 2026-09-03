import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "references" / "DeuteronWigner_theory_state_current.json"
NOTE_PATH = ROOT / "references" / "DeuteronWigner_complete_theory_note_current.tex"
BIB_PATH = ROOT / "references" / "DeuteronWigner_complete_theory_references.bib"
HANDOFF_PATH = ROOT / "handoff" / "CURRENT_PROJECT_HANDOFF.md"
FOUNDATION_PATH = ROOT / "Deuteron_GTMD.pdf"


def _state():
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def test_current_theory_state_has_canonical_authorities():
    state = _state()
    assert state["schema"] == "DEUTERONWIGNER-CURRENT-THEORY-STATE-V1"
    assert state["source_baseline"]["code_commit"].startswith("186cc816")
    for path in state["canonical_files"].values():
        assert (ROOT / path).is_file(), path


def test_current_theory_counts_and_claim_boundary():
    state = _state()
    counts = state["current_counts"]
    assert counts["c396_complete_numerical_apply_paths"] == 6
    assert counts["c117_source_product_primitives"] == 12
    assert counts["c117_retained_aggregate_shapes"] == 3
    assert counts["c117_complete_numerical_coordinate_actions"] == 0
    assert counts["physical_response_rank"] is None
    assert counts["physical_fit"] is False
    assert counts["hamiltonian_activation"] is False


def test_finite_cell_and_c117_ownership_are_synchronized_with_note():
    state = _state()
    note = NOTE_PATH.read_text(encoding="utf-8")
    conventions = state["conventions"]
    assert "ell_- = 2L" in conventions["executable_longitudinal_cell"]
    assert "4*pi*K/ell_-" in conventions["finite_cell_mass_conversion"]
    assert "\\ell_-\\equiv 2L" in note
    assert "\\label{tab:c117-factor-ownership}" in note
    assert "\\label{eq:c117-source-operator}" in note
    assert "matrix[0][0]" in state["c117_first_direction"]["c411_api_interpretation"]


def test_declared_tmd_scope_and_current_literature_are_explicit():
    state = _state()
    note = NOTE_PATH.read_text(encoding="utf-8")
    bib = BIB_PATH.read_text(encoding="utf-8")
    incomplete = " ".join(state["scope"]["not_complete"])
    assert "nonzero-skewness" in incomplete
    assert "18-function leading-twist quark" in " ".join(
        state["scope"]["complete_within_declared_basis"]
    )
    assert "general nonzero-skewness spin-1 GTMD" in note
    assert "XieLu2026TOdd" in note
    assert "@misc{XieLu2026TOdd" in bib


def test_scientific_progression_ends_at_predictive_gtmd_level():
    state = _state()
    note = NOTE_PATH.read_text(encoding="utf-8")
    handoff = HANDOFF_PATH.read_text(encoding="utf-8")
    progression = state["scientific_progression"]
    assert [item["stage"] for item in progression] == [1, 2, 3, 4]
    assert progression[0]["status"] == "established_public_starting_point"
    assert progression[2]["status"] == "active_construction_program"
    assert "volume_viii_symmetry_adapted_tensor_networks_prediction_compiler.tex" in " ".join(
        progression[2]["primary_sources"]
    )
    assert progression[3]["name"] == "predictive GTMD-level framework"
    assert "rather than only TMDs" in state["project_objective"]
    assert "does not contain" in state["foundational_scope_exclusion"]
    assert "Development arc and predictive endpoint" in note
    assert "Governing scientific progression" in handoff
    assert "Deuteron_GTMD.pdf" in note
    assert "Deuteron_GTMD.pdf" in handoff
    assert state["canonical_files"]["foundational_gtmd_draft"] == "Deuteron_GTMD.pdf"
    assert hashlib.sha256(FOUNDATION_PATH.read_bytes()).hexdigest() == state[
        "source_baseline"
    ]["foundational_gtmd_draft_sha256"]
