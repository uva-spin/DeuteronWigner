from deuteron_wigner.bridge import hqcdb1qggcontact2 as c


def test_authority_contract_absence_and_freeze():
    a = c.load_verified_hqcd_b1qggcontact2_authority()
    assert a["contract_present"] is False
    assert a["contract_absence_fail_closed"] is True
    assert a["status"] == c.STATUS
    assert a["package_root"] == c.PACKAGE_ROOT
    assert c.contact_handoff_freeze()["C192_root"] == c.C192_ROOT


def test_fixture_requires_explicit_nonphysical_parameters():
    f = c.contact_fixture_manifest("C193-FIXTURE-K9")["rows"][0]
    assert c.validate_contact_parameter_record(f)["no_defaults"] is True
    assert f["physical"] is False
    assert f["bare_mass_coordinates"]["signed_m_R"]
    assert f["bare_coupling_coordinate"]
    try:
        c.validate_contact_parameter_record({"schema": f["schema"]})
    except ValueError:
        pass
    else:
        raise AssertionError("partial parameter records must fail closed")


def test_owner_order_channels_denominators_and_symbolic_coefficients():
    f = c.contact_fixture_manifest("C193-FIXTURE-K11")["rows"][0]
    assert c.c112_coefficient_manifest()["count"] == 18
    assert c.c127_coefficient_manifest()["count"] == 36
    assert c.denominator_manifest()["count"] == 18
    assert c.color_manifest()["count"] == 18
    assert c.ho_cm_manifest()["count"] == 18
    x = c.evaluate_c112_coefficient(f, "Q_TO_QGG", "C190-C112-QGG_PRIMITIVE", "C185-target", "QGG_COLOR_8A")
    assert x["coefficient_numeric"] is False
    assert x["certified_enclosure"]["lower"] == x["certified_enclosure"]["upper"]
    y = c.evaluate_c127_coefficient(f, "C127-JG-K-JQ", "Q_TO_QGG", "C192-C127-C127-JG-K-JQ", "C185-target", "QGG_COLOR_1S")
    assert y["owner_id"] == "C127-JG-K-JQ"
    assert c.color_manifest()["channels_separate"]


def test_matrix_free_actions_derivatives_and_aggregation():
    f = c.contact_fixture_manifest("C193-FIXTURE-K13")["rows"][0]
    forward = c.apply_contact_q_to_qgg(f, ("q",), "C112", "QGG_COLOR_1S")
    reverse = c.apply_contact_qgg_to_q(f, ("g1", "g2", "g3"), "C127-JQ-K-JG", "QGG_COLOR_1S")
    assert forward["matrix_free"] and reverse["matrix_free"]
    assert forward["output_dimension"] == 3 and reverse["output_dimension"] == 1
    assert c.derivative_manifest()["count"] == 12
    assert c.hermitian_manifest()["count"] == 3
    assert c.local_aggregate_manifest()["rows"][0]["factor_two_assumed"] is False
    assert c.topology_manifest()["double_count"] == 0
    assert c.count_once_manifest()["duplicates"] == 0


def test_release_boundaries_reload_and_live_mutations():
    assert c.contact2_release_manifest()["next"] == "C194/HQCDQGVERT2"
    assert c.qg_1pi_handoff_contract()["complete_qg_1PI"] is False
    assert c.dependency_frontier_manifest()["graph_delta"] == {"nodes_added": 0, "edges_added": 0}
    assert c.quantum_nonmutation_manifest()["Q0_Q1_Q2_modified"] is False
    assert c.static_isolation_guard()["pass"]
    assert all(c.mutate_live_hqcd_b1qggcontact2(i)["pass"] for i in range(384))
