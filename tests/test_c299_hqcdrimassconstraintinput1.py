from deuteron_wigner.bridge import hqcdrimassconstraintinput1 as c
def test_audit():assert c.authority_audit()["usable_records"]==0
def test_non_equivalence():assert any(x["result"]=="INCOMPATIBLE_OPERATOR_NO_ADAPTER" for x in c.authority_audit()["rows"])
def test_mass():assert not c.mass_schema()["quark_mass_allowed"] and not c.mass_schema()["zero_default"]
def test_matrix():assert c.matrix_element_schema()["count"]==3 and c.matrix_element_schema()["channel_count"]==6
def test_cov():assert c.covariance_schema()["cross_K_blocks_required"] and not c.covariance_schema()["zero_assumed"]
def test_frontier():assert c.residual_frontier()["next"]=="C300/HQCDRIMASSADJOINTST1"
def test_scope():assert c.static_isolation_guard()["pass"]
def test_reload():assert c.load_verified_hqcdrimassconstraintinput1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassconstraintinput1(i)["pass"] for i in range(384))
