from deuteron_wigner.bridge import hqcdrimassholonomycoeff1 as c
def test_audit():assert c.authority_audit()["usable_C43"]==0
def test_sources():assert c.authority_audit()["rows"][1]["result"].startswith("REDUCED")
def test_coeff():assert c.coefficient_records()["count"]==3
def test_unavailable():assert all(x["lambda8"]=="UNAVAILABLE_NOT_ZERO" for x in c.coefficient_records()["rows"])
def test_benchmark():assert c.benchmark_contract()["label"].endswith("NOT_C43_MATCHING")
def test_scope():assert c.static_isolation_guard()["pass"]
def test_frontier():assert c.residual_frontier()["next"]=="C303/HQCDRIMASSV0PROJECT1"
def test_reload():assert c.load_verified_hqcdrimassholonomycoeff1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassholonomycoeff1(i)["pass"] for i in range(384))
