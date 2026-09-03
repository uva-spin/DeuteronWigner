import pytest
from deuteron_wigner.bridge.hqcd2pt import core as c
def test_fail_closed_authority():
 r=c.load_verified_hqcd_two_point_authority()
 assert r["status"]==c.STATUS and not r["positive_gate"] and r["selected_plan"]=="2PT-D"
 assert tuple(r["q_dimensions"])==(6,6,6) and tuple(r["qg_dimensions"])==(1344,2700,4752)
 assert r["source_map_complete"] is False and r["null_zeroed"]==0
def test_scope_and_unavailable_layers():
 assert c.flavor_scope_manifest()["status"]=="FLAVOR_IDENTITY_UNAVAILABLE"
 assert c.antiparticle_scope_manifest()["negative_frequency_complete"] is False
 assert c.sector_projector_manifest()["exact"]
 with pytest.raises(ValueError): c.projected_q_resolvent("K9","z")
 with pytest.raises(ValueError): c.full_spinor_two_point("K9","z")
 assert c.mass_projector_manifest()["status"]=="MASS_LINEAR_PROJECTOR_INCOMPLETE"
def test_mutations_and_isolation():
 assert c.static_isolation_guard()["pass"]
 for i in range(384): assert not c.mutate_live_hqcd2pt(i)["positive_gate"]
