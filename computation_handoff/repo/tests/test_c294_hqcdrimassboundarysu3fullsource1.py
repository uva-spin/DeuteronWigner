from deuteron_wigner.bridge import hqcdrimassboundarysu3fullsource1 as c
def test_source():assert c.source_manifest()["hash_verified"] and c.source_manifest()["row"]["pdf_pages"]==21
def test_locators():assert c.equation_locators()["count"]==5
def test_joint():assert c.complementary_coverage()["joint_SU3_derivation_ready"]
def test_limits():assert not c.complementary_coverage()["direct_3plus1_physical_measure"]
def test_separation():assert not c.complementary_coverage()["sources_conflated"]
def test_frontier():assert c.residual_frontier()["next"]=="C295/HQCDRIMASSSU3MEASUREDERIVE1" and not c.residual_frontier()["blocker"]
def test_scope():assert c.static_isolation_guard()["pass"] and c.static_isolation_guard()["SU2_relabelled_SU3"]==0
def test_reload():assert c.load_verified_hqcdrimassboundarysu3fullsource1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassboundarysu3fullsource1(i)["pass"] for i in range(384))
