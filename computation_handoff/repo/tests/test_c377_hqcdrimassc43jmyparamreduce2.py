from deuteron_wigner.bridge import hqcdrimassc43jmyparamreduce2 as c
def test_symbols():assert c.symbol_audit()["count"]==6 and not c.symbol_audit()["kinematically_closed"]
def test_partial():assert c.partial_reduction()["mass_terms"]==0
def test_routes():assert "unsupported" in c.attempted_routes()["model_convention"]
def test_gate():assert c.closure()["ordinary_continuation"] and not c.closure()["all_parameter_polynomials"]
def test_reload():assert not c.load_verified_hqcdrimassc43jmyparamreduce2_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43jmyparamreduce2(i)["pass"] for i in range(384))
