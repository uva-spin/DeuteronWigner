import pytest
from deuteron_wigner.bridge import hqcdriquarkfixedkvradcore1 as c
def test_manifest():assert c.core_program_manifest()["complete"]==8
def test_program():
 rid=c.core_program_manifest()["rows"][0]["radial_id"];p=c.core_enclosure_program(rid,2)
 assert p["term_count"]==9 and p["missing_count"]==0 and p["directed_interval"]==("-B_core","B_core")
def test_invalid():
 with pytest.raises(ValueError):c.core_enclosure_program(c.core_program_manifest()["rows"][0]["radial_id"],-1)
def test_release():assert c.release_manifest()["core_programs"]==8 and c.release_manifest()["tail_programs"]==0
def test_authority_mutations():
 assert c.verify_hqcd_riquarkfixedkvradcore1_authority()["package_root"]==c.PACKAGE_ROOT
 assert all(c.mutate_live_hqcdriquarkfixedkvradcore1(i)["pass"] for i in range(384))
