from deuteron_wigner.bridge import hqcdrimassadjointst1 as c
def test_auth():assert c.authority_freeze()["C203"]=="BRST differential authority"
def test_split():assert c.operator_split()["count"]==3
def test_brst():assert not c.brst_identity()["generic_zero"]
def test_bulk():assert c.brst_identity()["bulk_mass_coefficient"].startswith("FORBIDDEN")
def test_boundary():assert not c.boundary_exception()["local_mass_equivalent"] and c.boundary_exception()["coefficient"]=="UNMATCHED_NOT_ZERO"
def test_k():assert c.resolution_classification()["count"]==3
def test_frontier():assert c.residual_frontier()["next"]=="C301/HQCDRIMASSHOLONOMYPOT1"
def test_reload():assert c.load_verified_hqcdrimassadjointst1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassadjointst1(i)["pass"] for i in range(384))
