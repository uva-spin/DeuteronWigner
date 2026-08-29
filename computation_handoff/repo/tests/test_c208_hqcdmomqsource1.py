from deuteron_wigner.bridge import hqcdmomqsource1 as c
def test_source_hash_and_unique():
 a=c.verify_hqcd_momqsource1_authority();assert a["source"]["hash_verified"]
 assert c.source_uniqueness_decision()["unique"]
def test_locators_definition():
 assert c.locator_manifest()["count"]==5
 d=c.momq_definition_manifest();assert d["kinematics"]["nonexceptional"]
 assert d["tensor_basis_dimension"]==6 and d["tree_channel"]==1
def test_projector_and_map():
 assert c.projector_manifest()["selected_channel"]==1
 assert c.representability_manifest()["exactly_representable_in_C43"] is False
def test_release_handoff():
 assert c.release_manifest()["source"] and not c.release_manifest()["finite_basis_map"]
 assert c.next_handoff_contract()["next"]=="C209/HQCDMOMQMAP1"
def test_isolation_mutations():
 assert c.static_isolation_guard()["pass"]
 assert all(c.mutate_live_hqcdmomqsource1(i)["pass"] for i in range(384))
