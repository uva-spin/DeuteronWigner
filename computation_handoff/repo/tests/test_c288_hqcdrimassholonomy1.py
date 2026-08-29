from deuteron_wigner.bridge import hqcdrimassholonomy1 as c
def test_family():assert len(c.capsule_family()["rows"])==3 and c.capsule_family()["complete_instances"]==0
def test_neutral():assert all(x["process_neutral"] for x in c.capsule_family()["rows"])
def test_evidence():assert c.evidence_audit()["physical_instances"]==0 and not c.evidence_audit()["fixture_promotion"]
def test_defaults():assert not c.evidence_audit()["identity_default"]
def test_gate():assert c.composition_gate()["schema"] and not c.composition_gate()["physical_sector"]
def test_frontier():assert c.residual_frontier()["next"]=="C289/HQCDRIMASSHOLONOMYMEASURE1" and not c.residual_frontier()["blocker"]
def test_scope():assert c.static_isolation_guard()["pass"] and c.static_isolation_guard()["fixture_promoted"]==0
def test_reload():assert c.load_verified_hqcdrimassholonomy1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassholonomy1(i)["pass"] for i in range(384))
