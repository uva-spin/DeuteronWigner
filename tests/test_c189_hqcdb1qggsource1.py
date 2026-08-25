from deuteron_wigner.bridge import hqcdb1qggsource1 as c

def test_authority_and_contract_boundary():
    a = c.verify_hqcd_b1qggsource1_authority()
    assert a["status"] == "C189_HQCDB1QGGSOURCE1_DERIVATION_PREREQUISITES_INCOMPLETE"
    assert a["plan"] == "QGGSOURCE1-F"
    assert a["source_acquisition"] == 0
    assert c.load_verified_hqcd_b1qggsource1_authority()["package_root"] == c.PACKAGE_ROOT

def test_local_audit_and_safe_derivation_dag():
    assert c.source_hierarchy_manifest()["rows"][-1]["status"] == "PREREQUISITES_PARTIAL"
    assert c.local_source_audit_manifest()["exact_qgg_ast_count"] == 0
    dag = c.derivation_dag_manifest()
    assert dag["acyclic"] and dag["source_version_consistent"]
    assert len(dag["missing_leaves"]) == 2
    assert c.derivation_dag_schema()["eval"] is False

def test_both_sources_and_branches_fail_closed():
    assert c.c112_source_manifest()["qgg_ast"] is False
    assert c.c127_source_manifest()["qgg_ast"] is False
    b = c.branch_manifest()
    assert b["count"] == 4
    assert all(x["classification"] == "BRANCH_INCOMPLETE" for x in b["rows"])
    assert all(x["not_zero"] for x in b["rows"])

def test_descendants_ownership_and_target_metadata():
    assert c.descendant_reproduction_manifest()["count"] == 12
    assert c.descendant_reproduction_manifest()["qgg_descendant_reproduced"] is False
    assert c.ownership_reconciliation_manifest()["double_count"] == 0
    assert c.target_descendant_manifest()["count"] == 12
    assert c.target_descendant_manifest()["source_preimage_counts"] == "UNAVAILABLE_NOT_ZERO"
    assert c.denominator_manifest()["count"] == 12
    assert c.color_spin_manifest()["channels_separate"]

def test_handoff_requests_and_nonmutation():
    assert c.holonomy_bc_manifest()["count"] == 20
    assert c.coefficient_handoff_manifest()["executable_next"] is False
    assert c.request_resolution_manifest()["all_six_visible"]
    assert c.missing_source_object_manifest()["not_zero"]
    assert c.next_phase_handoff_contract()["next"] == "C190/HQCDB1QGGSOURCE2"
    assert c.dependency_frontier_manifest()["graph_delta"] == {"nodes_added": 0, "edges_added": 0}
    assert c.static_isolation_guard()["pass"]
    assert c.quantum_nonmutation_manifest()["Q0_Q1_Q2_modified"] is False
    assert all(c.mutate_live_hqcd_b1qggsource1(i)["pass"] for i in range(384))
