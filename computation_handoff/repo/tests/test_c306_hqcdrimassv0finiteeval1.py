from deuteron_wigner.bridge import hqcdrimassv0finiteeval1 as c
def test_program():assert c.evaluator_program()["executable_except"]=="center_branch"
def test_center():assert not c.center_audit()["ordinary_value_exists"] and c.center_audit()["J"]==0
def test_root():assert c.center_audit()["root_coordinates"]["v-u"]==0
def test_attempts():assert c.limit_attempts()["count"]==4 and not any(x["accepted"] for x in c.limit_attempts()["rows"])
def test_unavailable():assert c.limit_attempts()["coefficient_family"]=="NOT_EVALUATED_NOT_ZERO"
def test_certificate():assert not c.evaluation_certificate()["mathematical_contradiction"]
def test_frontier():assert c.residual_frontier()["next"]=="C307/HQCDRIMASSV0CENTERLIMIT1"
def test_reload():assert c.load_verified_hqcdrimassv0finiteeval1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassv0finiteeval1(i)["pass"] for i in range(384))
