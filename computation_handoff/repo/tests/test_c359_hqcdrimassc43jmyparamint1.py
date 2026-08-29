from deuteron_wigner.bridge import hqcdrimassc43jmyparamint1 as c
def test_audit():assert c.executability_audit()["count"]==5 and not c.executability_audit()["all_executable"]
def test_real_block():assert sum(not x["exact_numerator"] for x in c.executability_audit()["rows"])==2
def test_nodes():assert c.required_ast_nodes()["count"]==5
def test_fail_closed():assert not c.closure()["parameter_integrals_evaluated"] and c.closure()["ordinary_derivation_continuation"]
def test_reload():assert not c.load_verified_hqcdrimassc43jmyparamint1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43jmyparamint1(i)["pass"] for i in range(384))
