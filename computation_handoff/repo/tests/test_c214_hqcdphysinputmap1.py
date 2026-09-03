from deuteron_wigner.bridge import hqcdphysinputmap1 as c


def test_edge_schema_and_separate_dags():
    assert len(c.edge_schema()["required"])==15
    assert c.mapping_dag("mass")["count"]==7 and c.mapping_dag("coupling")["count"]==7


def test_c158_and_expression_roles():
    assert not c.c158_role_audit()["physical_target_values"]
    assert c.c158_role_audit()["values_consumed"]==0
    assert c.source_expression_audit()["complete"]==4


def test_independent_audits_and_missing_edge():
    assert c.independent_dependency_audits()["agree_on_calculation_frontier"]
    d=c.missing_edge_decision();assert d["C168_capsules"]==6 and d["adapter_programs"]==0 and not d["blocker"]


def test_release_handoff():
    assert c.release_manifest()["map_schema_ready"] and not c.release_manifest()["map_executable"]
    assert c.next_handoff_contract()["next"]=="C215/HQCDPHYSADAPTERCALC1"


def test_isolation_mutations():
    assert c.static_isolation_guard()["pass"]
    assert all(c.mutate_live_hqcdphysinputmap1(i)["pass"] for i in range(384))
