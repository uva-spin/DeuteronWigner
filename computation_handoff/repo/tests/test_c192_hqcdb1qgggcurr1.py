from deuteron_wigner.bridge import hqcdb1qgggcurr1 as c


def test_authority_plan_and_absent_contract_boundary():
    a = c.load_verified_hqcd_b1qgggcurr1_authority()
    assert a["status"] == "C192_C191_SOURCE_DERIVED_C127_ORDERED_GLUON_CURRENT_MIXED_OWNER_AND_QGG_BRANCH_AUTHORITY_READY"
    assert a["plan"] == "QGGGCURR1-A"
    assert a["contract_present"] is False and a["contract_absence_fail_closed"]
    assert a["package_root"] == c.PACKAGE_ROOT


def test_source_ast_derivative_color_and_normalization():
    s = c.gluon_current_source_manifest()["rows"][0]
    assert s["status"] == "SOURCE_DERIVED_CLOSED"
    assert s["extracted_term"] == "-g f_abc A_perp^b partial_- A_perp^c"
    assert s["derivative_placement"] == "partial_- acts on second slot"
    assert c.derivative_manifest()["rows"][0]["boundary_defect"]
    assert c.current_color_manifest()["rows"][0]["color_index_order"] == "f_abc, current a then field slots b,c"
    assert c.current_normalization_manifest()["rows"][0]["mixed_owner_factor"].startswith("each")
    assert c.gluon_current_program_schema()["eval"] is False


def test_branches_mixed_owners_and_targets():
    assert c.gluon_branch_manifest()["count"] == 6
    assert {r["terminal"] for r in c.gluon_branch_manifest()["rows"]} >= {"GLUON_PAIR_CREATION", "GLUON_PAIR_ANNIHILATION", "GLUON_NUMBER_PRESERVING"}
    assert c.mixed_current_manifest()["count"] == 2
    assert c.mixed_current_manifest()["orders_separate"]
    assert c.qgg_branch_manifest()["branch_present"]
    assert c.qgg_branch_manifest()["count"] == 4
    assert c.denominator_manifest()["count"] == 12
    assert c.qgg_color_manifest()["count"] == 12
    assert c.spin_bose_manifest()["count"] == 4
    assert c.target_descendant_manifest()["count"] == 12


def test_reproduction_handoff_and_requests():
    assert c.aggregate_current_manifest()["rows"][0]["status"] == "REPRODUCED_WITH_DECLARED_SYMBOLIC_EQUIVALENCE"
    assert c.descendant_reproduction_manifest()["mismatches"] == 0
    assert c.ownership_reconciliation_manifest()["double_count"] == 0
    assert c.holonomy_bc_manifest()["count"] == 20
    assert c.contact_handoff_manifest()["count"] == 12
    req = c.request_resolution_manifest()
    assert req["all_six_visible"] and req["request4_frozen"]
    assert all(not r["active_in_C192"] for r in req["rows"][:4])
    assert all(r["active_in_C192"] for r in req["rows"][4:])
    assert c.gcurr1_release_manifest()["next"] == "C193/HQCDB1QGGCONTACT2"


def test_isolation_reload_and_mutations():
    assert c.static_isolation_guard()["pass"]
    assert c.quantum_nonmutation_manifest()["Q0_Q1_Q2_modified"] is False
    assert c.dependency_frontier_manifest()["graph_delta"] == {"nodes_added": 0, "edges_added": 0}
    assert all(c.mutate_live_hqcd_b1qgggcurr1(i)["pass"] for i in range(384))
