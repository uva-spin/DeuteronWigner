from deuteron_wigner.bridge import hqcdrimassv0grameval1 as c
def test_design():assert c.scan_design()["evaluations"]==36
def test_scan():assert len(c.reference_scan()["rows"])==4
def test_norm():assert .99<c.reference_scan()["normalization"]<1.01
def test_tails():assert not c.shape_tail_fit()["converged_without_subtraction"]
def test_shape_nonzero():assert c.shape_tail_fit()["CHI8"]["b"]>10 and c.shape_tail_fit()["RE_TF3"]["b"]<-3
def test_order():assert c.regulator_audit()["ordered_requirement"].startswith("subtract N")
def test_frontier():assert c.residual_frontier()["next"]=="C310/HQCDRIMASSSHAPETAIL1"
def test_reload():assert c.load_verified_hqcdrimassv0grameval1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassv0grameval1(i)["pass"] for i in range(384))
