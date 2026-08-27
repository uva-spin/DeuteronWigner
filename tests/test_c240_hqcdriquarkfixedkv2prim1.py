from deuteron_wigner.bridge import hqcdriquarkfixedkv2prim1 as c
def test_primitives():assert c.primitive_manifest()["action_level_ready"]==3 and c.primitive_manifest()["HO_ready"]==0
def test_owners():assert {r["owner"] for r in c.primitive_manifest()["rows"]}=={"C112","C127","C129"}
def test_modes():assert c.mode_schema()["cardinality"]=="UNBOUNDED" and not c.mode_schema()["retained_ids"]
def test_scope():assert c.static_isolation_guard()["pass"]
def test_mutations():assert all(c.mutate_live_hqcdriquarkfixedkv2prim1(i)["pass"] for i in range(384))
