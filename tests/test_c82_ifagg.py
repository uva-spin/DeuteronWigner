from deuteron_wigner.bridge.ifagg import core

def test_c82_bridge_is_factorized_total_and_does_not_multiply_kernel():
    root=core.materialize(); value=core.validate_package(); bridge=core.IFContactAggregationBridge()
    assert root['status']==core.STATUS and value['pass'] and value['focused_live_mutations']>=384
    for r in core.RESOLUTIONS:
        assert bridge.validate_total_coordinate_map(r.label)['unmapped']==0
        x=bridge._c78.load_iferm_contact_support_package(r.label); g=next(q for q in x['witness_groups'] if q['triple_count'])
        e=g['emission_endpoint_ids'][0];a=g['absorption_endpoint_ids'][0];ee=next(v for v in x['emission_edges'] if v['id']==e);aa=next(v for v in x['absorption_edges'] if v['id']==a)
        contribution=bridge.pair_coordinate_contributions(ee['physical_qg_id'],aa['physical_qg_id'],r.label)[0]
        assert contribution['g_s_squared_absent'] and contribution['status'].startswith(('NONZERO','CERTIFIED'))
