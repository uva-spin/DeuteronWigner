import json
from pathlib import Path


MANIFEST = Path("validation/canonical_uncertainty_manifest.json")


def test_uncertainty_axes_are_named_unique_and_materialized():
    payload = json.loads(MANIFEST.read_text())
    axes = payload["axes"]
    identifiers = [axis["axis_id"] for axis in axes]
    assert len(identifiers) == len(set(identifiers))
    required = {
        "deuteron_wave_function", "pretzelosity_boundary", "bpv20_sivers",
        "jamdiff_transversity", "yang_g1t", "quark_wilson_kernel",
        "gluon_wilson_kernel_and_color", "polarized_tensor_shadowing",
        "sullivan_pion", "nonnucleonic_cluster",
        "high_k_w_plus_y_completion",
    }
    assert set(identifiers) == required
    for axis in axes:
        assert axis["classification"]
        assert axis["central"]
        assert Path(axis["artifact"]).exists(), axis["axis_id"]


def test_sum_rule_evidence_is_explicitly_bounded():
    payload = json.loads(MANIFEST.read_text())
    evidence = payload["sum_rule_evidence"]
    assert Path(evidence["artifact"]).exists()
    assert evidence["valence_number_passed"]
    assert evidence["all_parton_momentum_passed"]
    assert evidence["global_claim_limited_by"]
