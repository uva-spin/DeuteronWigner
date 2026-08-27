import pytest
from deuteron_wigner.bridge import hqcdriquarkfixedkvradconst1 as c
def test_capsule():
 assert c.validate_capsule(.1,1,2,3)["excluded_boundary"]=="UNAVAILABLE_NOT_ZERO"
 with pytest.raises(ValueError):c.validate_capsule(0,1,2,3)
def test_growth():assert c.growth_program_manifest()["computable"]==8 and c.growth_program_manifest()["common_exponent"]==2
def test_critical():assert c.critical_split_manifest()["interior_critical_points"]==0 and c.critical_split_manifest()["complete"]
def test_release():assert c.release_manifest()["core_enclosures"]==0 and c.release_manifest()["next"]=="C232/HQCDRIQUARKFIXEDKVRADCORE1"
def test_authority_mutations():
 assert c.verify_hqcd_riquarkfixedkvradconst1_authority()["package_root"]==c.PACKAGE_ROOT
 assert all(c.mutate_live_hqcdriquarkfixedkvradconst1(i)["pass"] for i in range(384))
