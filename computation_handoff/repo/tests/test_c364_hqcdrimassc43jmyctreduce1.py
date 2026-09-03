from deuteron_wigner.bridge import hqcdrimassc43jmyctreduce1 as c
def test_audit():assert c.projector_audit()["count"]==5 and not c.projector_audit()["scalar_coefficients_computable"]
def test_parents_missing():assert all(not x["bare_integrand"] for x in c.projector_audit()["rows"])
def test_required():assert c.required_virtual_ast()["count"]==5 and "epsilon_UV" in c.required_virtual_ast()["MSbar"]
def test_fail_closed():assert not c.closure()["counterterm_scalar_coefficients"] and c.closure()["ordinary_derivation_continuation"]
def test_reload():assert not c.load_verified_hqcdrimassc43jmyctreduce1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43jmyctreduce1(i)["pass"] for i in range(384))
