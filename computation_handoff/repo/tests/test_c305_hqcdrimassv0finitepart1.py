from deuteron_wigner.bridge import hqcdrimassv0finitepart1 as c
def test_walls():assert c.wall_asymptotics()["count"]==3
def test_cancel():assert all("finite" in x["weighted_behavior"] for x in c.wall_asymptotics()["rows"])
def test_regulator():assert c.regulator_definition()["measure"]=="corrected C304 J/6"
def test_subtraction():assert "1/2,1/2" in c.regulator_definition()["center_subtraction"]
def test_order():assert c.finite_part_program()["ordered_limit"].startswith("first N")
def test_covariance():assert c.covariance_contract()["correlated_across_basis"]
def test_frontier():assert c.residual_frontier()["next"]=="C306/HQCDRIMASSV0FINITEEVAL1"
def test_reload():assert c.load_verified_hqcdrimassv0finitepart1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassv0finitepart1(i)["pass"] for i in range(384))
