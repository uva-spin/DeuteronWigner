from deuteron_wigner.bridge import hqcdrimassgaugeadapter1 as c
def test_endpoints():assert not c.endpoint_manifest()["identity"] and len(c.endpoint_manifest()["rows"])==2
def test_terms():assert c.contribution_ledger()["count"]==6 and not c.contribution_ledger()["missing_as_zero"]
def test_program():assert len(c.adapter_program()["rows"])==3 and not c.adapter_program()["rows"][0]["executable"]
def test_audit():assert not c.cross_gauge_audit()["off_shell_colored_gauge_independence"]
def test_frontier():assert c.residual_frontier()["next"]=="C284/HQCDRIMASSLFLOOP1" and not c.residual_frontier()["blocker"]
def test_release():assert c.release_manifest()["remaining_C165_layer_leaves"]==1
def test_scope():assert c.static_isolation_guard()["pass"] and c.static_isolation_guard()["boundary_zeroed"]==0
def test_reload():assert c.load_verified_hqcdrimassgaugeadapter1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassgaugeadapter1(i)["pass"] for i in range(384))
