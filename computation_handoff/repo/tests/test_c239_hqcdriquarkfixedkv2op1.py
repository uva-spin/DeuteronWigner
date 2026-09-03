from deuteron_wigner.bridge import hqcdriquarkfixedkv2op1 as c
def test_components():assert c.component_manifest()["owned"]==3 and c.component_manifest()["complement_ready"]==0
def test_schema():assert not c.operator_schema()["retained_index_reuse"] and not c.operator_schema()["executable"]
def test_release():assert c.release_manifest()["components_owned"]==3 and c.release_manifest()["complement_primitives"]==0
def test_scope():assert c.static_isolation_guard()["pass"]
def test_mutations():assert all(c.mutate_live_hqcdriquarkfixedkv2op1(i)["pass"] for i in range(384))
