from deuteron_wigner.bridge import hqcdriquarkfixedkv2contactkernel1 as c
def test_audit():assert c.dependency_audit()["count"]==4 and c.dependency_audit()["parameterization_incomplete"]==3
def test_release():assert not c.release_manifest()["full_kernel"]
def test_scope():assert c.static_isolation_guard()["pass"]
def test_routes():assert c.route_certificate()["mismatches"]==0
def test_mutations():assert all(c.mutate_live_hqcdriquarkfixedkv2contactkernel1(i)["pass"] for i in range(384))
