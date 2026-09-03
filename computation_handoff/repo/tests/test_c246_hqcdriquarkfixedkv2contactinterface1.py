from deuteron_wigner.bridge import hqcdriquarkfixedkv2contactinterface1 as c
from deuteron_wigner.bridge import hqcdriquarkfixedkv2contactadapter1 as a
def x():return a.ComplementContactCoordinate(("3/2",0,0,-1,"q"),("1",0,0,-1,"g"),("3/2",0,0,-1,"q"),("1",0,0,-1,"g"),0,0,0,1)
def test_applicability():assert c.applicability_manifest()["applicable"]==3 and c.applicability_manifest()["not_applicable"]==12
def test_inventory():assert c.interface_inventory()["count"]==3
def test_evaluate_routes():
 i=c.interface_inventory()["rows"][0]["interface_id"];assert c.evaluate_interface_contact(i,x(),9,.4)["value"]["Pminus_coefficient"]==c.evaluate_interface_contact(i,x(),9,.4,"factorized")["value"]["Pminus_coefficient"]
def test_scope():assert c.static_isolation_guard()["pass"]
def test_mutations():assert all(c.mutate_live_hqcdriquarkfixedkv2contactinterface1(i)["pass"] for i in range(384))
