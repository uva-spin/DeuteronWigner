from deuteron_wigner.bridge.hqcdqgvert import core as c

Z = {"real": 0, "imaginary": 1, "units": "GeV^2", "analytic_query": True, "physical_width": False}
SUB = {"schema":"C149-OFFSHELL-SUBTRACTION-RECORD-V1","subtraction_id":"diag","mu":"mu_FB","units":"GeV","kinematics":Z,"state_selector":"q_source_image","projector_id":"mass","no_default":True}


def vertex_record():
    src = c.q_to_qg_source_manifest("K9")["rows"][0]
    return {"schema":"C152-VERTEX-RECORD-V1","vertex_id":"v1","incoming_quark_scheme":"K_MINUS","outgoing_quark_scheme":"K_PLUS","gluon_scheme":"K_PERP","incoming_subtraction":SUB,"outgoing_subtraction":SUB,"gluon_subtraction":SUB,"kinematics":Z,"embedding":"C77 physical qg","orientation":"emission","conservation":{"longitudinal":True,"transverse":True,"helicity":True,"color":True},"no_default":True,"incoming_quark_source_id":src["quark_sources"][0],"gluon_source_id":src["gluon_sources"][0]}


def test_explicit_vertex_schema_and_routes():
    v=vertex_record(); assert c.validate_vertex_record(v)["vertex_id"]=="v1"
    for route in ("direct","block","matrix_free","response_derivative"):
        out=c.amputated_qg_vertex("K9",v,fixture_id="FIXTURE-FREE",route=route)
        assert out["retained_qg_proper"] is True
    assert c.vertex_projector_manifest()["gram_rank"]==8


def test_conditional_vertex_maps_and_scope():
    v=vertex_record()
    z1=c.conditional_z1f("K9",v,fixture_id="FIXTURE-FREE")
    gr=c.conditional_renormalized_coupling("K9",v,fixture_id="FIXTURE-FREE")
    assert "g_s=0" in z1["derivative_guard"]
    assert gr["physical"] is False
    assert c.vertex_properness_report()["full_QCD_1PI"] is False
    assert c.historical_vertex_coordinate_crosswalk()["overwrite"] is False


def test_no_implicit_fixture_and_mutations():
    try: c.conditional_z1f("K9",vertex_record())
    except ValueError as exc: assert "exactly one" in str(exc)
    else: raise AssertionError("implicit fixture accepted")
    assert c.verify_hqcd_qg_vertex_authority()["positive_gate"] is True
    for i in range(384):
        m=c.mutate_live_hqcdqgvert(i); assert m["positive_gate"] is False and m["must_fail_or_change_root"] is True
