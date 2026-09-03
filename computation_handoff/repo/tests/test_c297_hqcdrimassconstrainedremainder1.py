from deuteron_wigner.bridge import hqcdrimassconstrainedremainder1 as c
def test_source():assert c.source_freeze()["dimension"].startswith("Soyez")
def test_constraints():assert c.constraint_equations()["count"]==2 and all(x["linear"] for x in c.constraint_equations()["rows"])
def test_solution():assert c.formal_solution()["rows"][1]["coefficient"].startswith("(3/4)") and not c.formal_solution()["evaluated"]
def test_remainder():assert c.remainder_representation()["available"]=="SYMBOLIC_EXACT" and c.remainder_representation()["numerical"]=="UNAVAILABLE"
def test_covariance():assert c.covariance_pullback()["off_diagonal"].startswith("REQUIRED")
def test_k():assert c.resolution_adapter()["count"]==3 and not c.resolution_adapter()["K_averaged"]
def test_frontier():assert c.residual_frontier()["next"]=="C298/HQCDRIMASSCONSTRAINTKERNEL1" and not c.residual_frontier()["blocker"]
def test_reload():assert c.load_verified_hqcdrimassconstrainedremainder1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassconstrainedremainder1(i)["pass"] for i in range(384))
