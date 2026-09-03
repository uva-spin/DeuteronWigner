from deuteron_wigner.bridge import hqcdrimassc43jmyintegrand1 as c
def test_ast():assert c.integrand_ast()["count"]==5 and {r["id"] for r in c.integrand_ast()["rows"]}=={"DV","DR","FV","FR","S"}
def test_regulators():assert "alpha" in c.integrand_ast()["rows"][0]["regulator"] and "beta" in c.integrand_ast()["rows"][2]["regulator"]
def test_validation():assert c.validation()["C356_residues_recovered"] and not c.validation()["scaleless_individual_evaluated"]
def test_fail_closed():assert c.closure()["operator_identical"] and not c.closure()["finite_groups_evaluated"]
def test_reload():assert not c.load_verified_hqcdrimassc43jmyintegrand1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43jmyintegrand1(i)["pass"] for i in range(384))
