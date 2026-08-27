from deuteron_wigner.bridge import hqcdriquarkfixedktrans1 as c
def test_schema():assert not c.transverse_program_schema()["threshold"] and not c.transverse_program_schema()["dense"]
def test_tm():
 x=c.exact_tm_coefficient(c.RESOLUTIONS[0],"1/2","1",(0,0,0,0),(0,0,0,0));assert x["status"]=="NONZERO_EXACT_ALGEBRAIC"
def test_kinetic():
 a=c.transverse_kinetic_entry(c.RESOLUTIONS[0],"1/3",0,0,1,0);b=c.transverse_kinetic_entry(c.RESOLUTIONS[0],"1/3",1,0,0,0);assert a["expression"]==b["expression"]
def test_completion():assert c.free_denominator_completion()["Q_R_H0_Q_R"].startswith("COMPLETE") and c.next_handoff_contract()["next"]=="C224/HQCDRIQUARKFIXEDKV1"
def test_authority_mutations():
 assert c.verify_hqcd_riquarkfixedktrans1_authority()["package_root"]==c.PACKAGE_ROOT
 assert c.static_isolation_guard()["pass"] and all(c.mutate_live_hqcdriquarkfixedktrans1(i)["pass"] for i in range(384))
