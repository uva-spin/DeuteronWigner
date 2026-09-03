from deuteron_wigner.bridge.hqcdtarget2 import core as c
import pytest

def test_t2a_authority_and_roots():
    r=c.load_verified_hqcd_target2_authority()
    assert r["positive_gate"] and r["selected_plan"]=="T2-A"
    assert r["generic_rank"]==2 and r["rank_deficit"]==9
    assert c.target_plan_manifest()["selected_plan"]=="T2-A"
    assert c.project_scheme_manifest()["scheme_id"]==c.SCHEME_ID

def test_symbolic_inputs_are_required_and_never_defaulted():
    with pytest.raises(ValueError): c.evaluate_target_condition(c.TARGET_IDS[0], c.RESOLUTIONS[0])
    x=c.evaluate_target_condition(c.TARGET_IDS[0],c.RESOLUTIONS[0],external_input_capsule={"external_input_id":"EXT-M","target_id":c.TARGET_IDS[0],"parameter_id":"M_R2_FB","value_or_interval":"symbolic","units":"GeV^2","domain":"finite-resolution-open-triplet","scheme_id":c.SCHEME_ID,"reference_scale_or_kinematics":"K9","flavor_state_identity":"open-triplet","provenance":"caller","uncertainty_semantics":"caller","signature":"sig","no_default":True})
    assert x["value"] is None and x["route_mismatch"]==0
    with pytest.raises(ValueError): c.evaluate_target_condition(c.TARGET_IDS[1],c.RESOLUTIONS[0],external_input_capsule={"scheme_id":"MSbar"})

def test_targets_selectors_and_coverage():
    assert c.target_manifest()["count"]==4
    assert c.reference_selector_manifest()["count"]==3
    assert c.gluon_one_body_factorization_report()["factorized"] is False
    assert c.target_backed_identifiability_report()["rank_deficit"]==9
    assert len(c.counterterm_target_crosswalk()["directions"])==6
    assert c.static_isolation_guard()["pass"]
    for i in range(384): assert not c.mutate_live_hqcdtarget2(i)["positive_gate"]
