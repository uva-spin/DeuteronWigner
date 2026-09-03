import pytest
from deuteron_wigner.bridge import hqcdriquarkfixedkv2currentsource1 as c
def test_inventory_schema():assert c.source_inventory()["qualified_target_sources"]==0 and len(c.target_capsule_schema()["required"])==21
def test_coverage():assert c.direction_coverage()["uncovered"]==4 and c.qualified_candidate_records()["count"]==0
def test_fail_closed_validation():
 with pytest.raises(ValueError):c.validate_target_capsule({"schema":"C256-CURRENT-SUBTRACTION-TARGET-CAPSULE-V1"})
def test_routes_scope():assert c.route_certificate()["mismatches"]==0 and c.static_isolation_guard()["pass"]
def test_mutations():assert all(c.mutate_live_hqcdriquarkfixedkv2currentsource1(i)["pass"] for i in range(384))
