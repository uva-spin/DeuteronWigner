from deuteron_wigner.bridge import hqcdrimassboundarysu3source1 as c
def test_source():assert c.source_manifest()["hash_verified"] and c.source_manifest()["row"]["pdf_pages"]==22
def test_locators():assert c.equation_locators()["count"]==6 and c.equation_locators()["transcription_visual_check"]
def test_scope():assert c.scope_audit()["gauge_group"]=="SU3" and c.scope_audit()["dynamical_zero_mode_action"]
def test_limits():assert not c.scope_audit()["constrained_zero_modes_retained"] and not c.scope_audit()["C43_direct_map"]
def test_measure():assert not c.scope_audit()["normalized_group_measure_explicit"]
def test_frontier():assert c.residual_frontier()["next"]=="C294/HQCDRIMASSBOUNDARYSU3FULLSOURCE1" and not c.residual_frontier()["blocker"]
def test_scope_guard():assert c.static_isolation_guard()["pass"] and c.static_isolation_guard()["partial_promoted"]==0
def test_reload():assert c.load_verified_hqcdrimassboundarysu3source1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassboundarysu3source1(i)["pass"] for i in range(384))
