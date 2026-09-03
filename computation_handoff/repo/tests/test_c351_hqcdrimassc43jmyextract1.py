from deuteron_wigner.bridge import hqcdrimassc43jmyextract1 as c
def test_sources():assert c.source_manifest()["count"]==2 and c.source_manifest()["primary"]
def test_equations():assert c.equation_manifest()["count"]==7 and c.equation_manifest()["endpoint_terms_preserved"]
def test_ir_fail_closed():assert c.closure()["identical_external_state"] and not c.closure()["identical_IR_prescription"] and not c.closure()["direct_conversion_ready"]
def test_soft_count_once():assert "net one soft subtraction" in c.convention_crosswalk()["soft_partition"]
def test_reload():assert not c.load_verified_hqcdrimassc43jmyextract1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43jmyextract1(i)["pass"] for i in range(384))
