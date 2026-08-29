from deuteron_wigner.bridge import hqcdrimassc43jmygroupreduce1 as c
def test_groups():assert c.grouped_ast()["count"]==3 and c.grouped_ast()["order"].startswith("sum bare")
def test_distribution():assert "Sigma_q" in c.grouped_ast()["rows"][0]["terms"][-1]
def test_laurent_gate():assert not c.laurent_ledger()["published_numeric_coefficients"]
def test_closure():assert c.closure()["gauge_complete_groups_formed"] and not c.closure()["common_master_integrals"]
def test_reload():assert not c.load_verified_hqcdrimassc43jmygroupreduce1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43jmygroupreduce1(i)["pass"] for i in range(384))
