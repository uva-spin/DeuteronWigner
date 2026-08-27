from deuteron_wigner.bridge import hqcdriquarkfixedkv2ho1 as c
def test_angular():assert c.angular_projection_manifest()["angular_ready"]==3
def test_radial():assert c.angular_projection_manifest()["radial_ready"]==0
def test_contact():assert not c.contact_audit()["smearing_invented"] and not c.contact_audit()["quadrature_promoted"]
def test_scope():assert c.static_isolation_guard()["pass"]
def test_mutations():assert all(c.mutate_live_hqcdriquarkfixedkv2ho1(i)["pass"] for i in range(384))
