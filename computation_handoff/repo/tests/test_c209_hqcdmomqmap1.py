from deuteron_wigner.bridge import hqcdmomqmap1 as c


def test_exact_search_fails_closed():
    m = c.exact_point_search_manifest()
    assert m["count"] == 3 and m["exact_point_exists"] is False


def test_certified_adapter_and_projector():
    assert c.wavepacket_adapter_manifest()["certified_controlled_limit"]
    assert c.projector_intertwiner_manifest()["count"] == 18


def test_complete_caller_record_evaluates_symbolically():
    p = {k: "caller-bound" for k in c.parameter_schema()["required_fields"]}
    p.update(record_id="C209-TEST", resolution="K9", no_defaults=True, physical=False)
    a = c.evaluate_adapter(p)
    assert a["exact"] is False and a["physical"] is False


def test_release_and_handoff():
    assert c.release_manifest()["adapter"] and not c.release_manifest()["target_condition_executed"]
    assert c.next_handoff_contract()["next"] == "C210/HQCDMOMQCOND2"


def test_isolation_and_live_mutations():
    assert c.static_isolation_guard()["pass"]
    assert all(c.mutate_live_hqcdmomqmap1(i)["pass"] for i in range(384))
