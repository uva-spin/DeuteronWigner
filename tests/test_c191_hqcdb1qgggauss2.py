from deuteron_wigner.bridge import hqcdb1qgggauss2 as c


def test_contract_plan_and_read_only_boundary():
    a = c.load_verified_hqcd_b1qgggauss2_authority()
    assert a["status"] == "C191_HQCDB1QGGGAUSS2_GLUON_CURRENT_INCOMPLETE"
    assert a["plan"] == "QGGGAUSS2-C"
    assert a["package_root"] == c.PACKAGE_ROOT
    assert a["parent_package_root"] == "02defbe0e8027500f5dd5798ee651e8cb93392b82ece424993713e86e3cb4b72"
    assert a["coefficients"] == 0 and a["contact_matrices"] == 0
    assert c.gauss_handoff_freeze()["C112"] == "ready_read_only"


def test_quark_gluon_current_split_and_aggregate():
    assert c.quark_current_manifest()["rows"][0]["status"] == "SOURCE_QUALIFIED_QUARK_CURRENT_READY"
    assert c.quark_current_manifest()["rows"][0]["normalization"] == "source-declared; no conventional factor assumed"
    assert c.gluon_current_manifest()["rows"][0]["status"] == c.STATUS
    assert c.gluon_current_manifest()["rows"][0]["not_zero"]
    assert c.aggregate_current_manifest()["double_count"] == 0
    assert c.aggregate_current_manifest()["rows"][0]["residual"] == "SYMBOLIC_EQUIVALENCE_PENDING_GLUON_CHILD"


def test_current_owners_branches_and_denominators():
    h = c.current_hamiltonian_manifest()
    assert len(h["rows"]) == 7
    assert h["mixed_orders_separate"]
    assert sum(x["status"] == "INCOMPLETE_NOT_ZERO" for x in h["rows"]) == 3
    assert c.current_branch_manifest()["count"] == 18
    assert c.qgg_branch_manifest()["count"] == 4
    assert c.qgg_branch_manifest()["C112_preserved"] and c.qgg_branch_manifest()["C127_not_zero"]
    assert c.denominator_manifest()["count"] == 12
    assert c.denominator_manifest()["continuum_substitution"] is False
    assert c.color_manifest()["count"] == 12
    assert c.spin_bose_manifest()["count"] == 4


def test_targets_reproduction_and_nonmutation():
    assert c.target_descendant_manifest()["count"] == 12
    assert c.descendant_reproduction_manifest()["rows"][0]["status"] == "REPRODUCED_EXACTLY_READ_ONLY"
    assert c.ownership_reconciliation_manifest()["double_count"] == 0
    assert c.holonomy_bc_manifest()["count"] == 20
    assert c.contact_handoff_manifest()["count"] == 12
    assert c.request_resolution_manifest()["all_six_visible"]
    assert c.quantum_nonmutation_manifest()["Q0_Q1_Q2_modified"] is False
    assert c.static_isolation_guard()["pass"]
    assert all(c.mutate_live_hqcd_b1qgggauss2(i)["pass"] for i in range(384))


def test_unknown_ids_fail_closed():
    for call in (
        lambda: c.blocker_manifest("unknown"),
        lambda: c.quark_current_manifest("unknown"),
        lambda: c.gluon_current_manifest("unknown"),
        lambda: c.current_hamiltonian_manifest("unknown"),
        lambda: c.topology_manifest("unknown"),
        lambda: c.target_descendant_manifest(owner_id="unknown"),
    ):
        try:
            call()
        except KeyError:
            pass
        else:
            raise AssertionError("unknown identifier was accepted")
