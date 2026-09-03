from deuteron_wigner.bridge import hqcdrimassc43jmydimir1 as c
def test_source():assert c.source_authority()["method_authority"] and not c.source_authority()["operator_identity_JMY"]
def test_sectors():assert c.sector_classification()["count"]==6 and c.sector_classification()["all_retained"]
def test_grouping():assert c.grouped_integrand_contract()["mixed_poles_must_cancel"] and c.grouped_integrand_contract()["arbitrary_scale_forbidden"]
def test_fail_closed():assert not c.ambiguity_certificate()["individual_DR_values_defined"] and not c.closure()["common_IR_conversion_ready"]
def test_reload():assert not c.load_verified_hqcdrimassc43jmydimir1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43jmydimir1(i)["pass"] for i in range(384))
