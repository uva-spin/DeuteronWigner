from deuteron_wigner.bridge import hqcdrimassc43irseparator1 as c
def test_source():assert c.source_authority()["role"].endswith("method only") and not c.source_authority()["JMY_operator_identity"]
def test_separator():assert "epsilon->0" in c.separator_contract()["limit_order"]
def test_gates():assert all(c.acceptance_gates()[k] for k in ("alpha_poles_cancel","beta_poles_cancel","limit_order_parity_required","off_lightcone_vectors_unchanged"))
def test_not_evaluated():assert c.closure()["separator_bound"] and not c.closure()["JMY_group_values_evaluated"]
def test_reload():assert not c.load_verified_hqcdrimassc43irseparator1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43irseparator1(i)["pass"] for i in range(384))
