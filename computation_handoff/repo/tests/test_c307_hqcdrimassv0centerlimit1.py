from deuteron_wigner.bridge import hqcdrimassv0centerlimit1 as c
def test_definition():assert c.branch_definition()["orientation_neutral"]
def test_scan():assert c.branch_scan()["count"]==4
def test_poles():assert c.branch_scan()["leading_poles_enclosed"]["minus"][0]<-6<c.branch_scan()["leading_poles_enclosed"]["minus"][1]
def test_symmetry():assert not c.symmetry_certificate()["one_sided_selection_allowed"]
def test_tail():assert not c.tail_certificate()["converged"] and not c.tail_certificate()["zero_selected"]
def test_scope():assert c.static_isolation_guard()["pass"]
def test_frontier():assert c.residual_frontier()["next"]=="C308/HQCDRIMASSV0TAILRENORM1"
def test_reload():assert c.load_verified_hqcdrimassv0centerlimit1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassv0centerlimit1(i)["pass"] for i in range(384))
