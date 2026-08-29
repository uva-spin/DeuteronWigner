import pytest
from deuteron_wigner.bridge.hqcdfield import core as c

def test_verified_forward_source_authority():
    r = c.load_verified_hqcd_field_authority()
    assert r["status"] == c.STATUS and r["positive_gate"]
    assert r["selected_plan"] == "FIELD-A"
    assert tuple(r["source_mode_counts"]) == (6, 6, 6)
    assert tuple(r["source_map_rank"]) == (6, 6, 6)
    assert r["q_span"] and r["route_fa_fb_mismatches"] == 0

def test_maps_metrics_and_scope():
    for resolution in c.RESOLUTIONS:
        assert c.quark_source_matrix(resolution) == c.quark_sink_matrix(resolution)
        assert c.source_metric(resolution) == c.q_sector_metric(resolution)
        assert c.source_span_certificate(resolution)["kernel_dimension"] == 0
        assert c.apply_quark_source(resolution, range(6)) == tuple(range(6))
        assert c.apply_quark_sink(resolution, range(6)) == tuple(range(6))
    assert c.antiquark_source_manifest()["retained_antiquark_hilbert"] is False
    assert c.local_qcd_vacuum_manifest()["distinct_from_c33_tmd_soft_vacuum"]
    assert c.field_source_completeness_certificate()["direct_qg_source_status"].startswith("NOT_APPLICABLE")

def test_forbidden_layers_and_mutations():
    assert c.static_isolation_guard()["pass"]
    for fn in (c.projected_q_resolvent, c.good_component_two_point, c.full_spinor_two_point,
               c.inverse_two_point, c.self_energy, c.mass_projector, c.quark_field_residue):
        with pytest.raises(ValueError):
            fn("K9", "z")
    for i in range(384):
        assert not c.mutate_live_hqcdfield(i)["positive_gate"]
