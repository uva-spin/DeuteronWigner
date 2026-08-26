from deuteron_wigner.bridge import hqcdmomqcond2 as c


def test_guards_and_conditions():
    assert c.guard_manifest()["count"] == 3
    assert c.enclosed_condition_manifest()["count"] == 18


def test_program_is_data_only():
    p = c.condition_program_schema()
    assert not p["eval"] and not p["pickle"] and not p["callbacks"]


def test_complete_execution():
    ap = {k: "caller-bound" for k in c.c209.parameter_schema()["required_fields"]}
    ap.update(record_id="C210-ADAPTER", resolution="K9", no_defaults=True, physical=False)
    p = {k: "caller-bound" for k in c.parameter_schema()["required_fields"]}
    p.update(record_id="C210-TEST", resolution="K9", adapter_parameter_record=ap,
             no_defaults=True, physical=False, alpha="alpha", active_Nf="Nf", a_symbol="a")
    assert c.execute_target_condition(p)["selected_channel"] == 1


def test_release_handoff():
    assert c.release_manifest()["condition_executable"]
    assert c.next_handoff_contract()["next"] == "C211/HQCDMOMQEVAL1"


def test_isolation_mutations():
    assert c.static_isolation_guard()["pass"]
    assert all(c.mutate_live_hqcdmomqcond2(i)["pass"] for i in range(384))
