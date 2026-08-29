from deuteron_wigner.bridge import hqcdrimassc43deltaextract1 as c
def test_eqs():assert c.equation_manifest()["count"]==5 and c.equation_manifest()["normalized"]
def test_soft():assert c.convention_crosswalk()["soft_partition"]=="minus one half at NLO"
def test_closure():assert c.closure()["delta_side_quark_subtraction"] and not c.closure()["direct_conversion_ready"]
def test_no_import():assert not c.closure()["coefficient_imported_C43"]
def test_reload():assert not c.load_verified_hqcdrimassc43deltaextract1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43deltaextract1(i)["pass"] for i in range(384))
