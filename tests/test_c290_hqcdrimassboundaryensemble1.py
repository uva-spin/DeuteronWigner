from deuteron_wigner.bridge import hqcdrimassboundaryensemble1 as c
def test_schema():assert c.ensemble_schema()["complete_instances"]==0 and len(c.ensemble_schema()["classes"])==3
def test_defaults():assert not c.ensemble_schema()["uniform_default"] and not c.ensemble_schema()["unit_volume_default"]
def test_program():assert len(c.action_to_weight_program()["safe_opcodes"])==7 and not c.action_to_weight_program()["executable"]
def test_audit():assert c.authority_audit()["physical_records"]==0 and not c.authority_audit()["missing_as_uniform"]
def test_frontier():assert c.residual_frontier()["next"]=="C291/HQCDRIMASSBOUNDARYACTION1"
def test_nonblocker():assert not c.residual_frontier()["blocker"]
def test_scope():assert c.static_isolation_guard()["pass"] and c.static_isolation_guard()["K_independence_assumed"]==0
def test_reload():assert c.load_verified_hqcdrimassboundaryensemble1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassboundaryensemble1(i)["pass"] for i in range(384))
