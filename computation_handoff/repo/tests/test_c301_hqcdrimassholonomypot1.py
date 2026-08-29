from deuteron_wigner.bridge import hqcdrimassholonomypot1 as c
def test_auth():assert c.authority_freeze()["C183"].startswith("explicit")
def test_basis():assert c.class_function_basis()["count"]==2 and "omitted" in c.class_function_basis()["dependent_identity"]
def test_symmetry():assert all(x["center"]=="invariant" and x["weyl"]=="invariant" for x in c.class_function_basis()["rows"])
def test_brst():assert c.endpoint_brst_proof()["class_function_variation"]==0 and not c.endpoint_brst_proof()["bulk_mass_equivalence"]
def test_potential():assert c.potential_contract()["coefficients"]=="UNMATCHED_NOT_ZERO"
def test_k():assert c.resolution_adapter()["count"]==3
def test_frontier():assert c.residual_frontier()["next"]=="C302/HQCDRIMASSHOLONOMYCOEFF1"
def test_reload():assert c.load_verified_hqcdrimassholonomypot1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassholonomypot1(i)["pass"] for i in range(384))
