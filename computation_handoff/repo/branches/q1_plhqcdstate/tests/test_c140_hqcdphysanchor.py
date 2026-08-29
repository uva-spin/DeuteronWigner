from deuteron_wigner.bridge.hqcdphysanchor import core as c

def test_fail_closed_anchor_authority():
    r = c.load_verified_hqcd_physical_anchor_authority()
    assert r["status"] == c.STATUS and not r["positive_gate"]
    assert r["selected_plan"] == "PHYS-A"
    assert r["source_count"] == 8 and r["source_hashes_locked"]
    assert r["accepted_project_anchors"] == 0
    assert r["quark_two_point_complete"] is False

def test_semantics_and_no_go():
    assert c.legacy_target_semantic_manifest()["legacy_capsules_generated"] is False
    assert c.standard_anchor_manifest()["accepted"] == 0
    assert c.remaining_nullspace_manifest()["dimension"] == 9
    assert c.static_isolation_guard()["pass"]

def test_mutations():
    for i in range(384): assert not c.mutate_live_hqcdphysanchor(i)["positive_gate"]
