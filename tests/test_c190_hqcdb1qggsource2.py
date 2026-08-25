from deuteron_wigner.bridge import hqcdb1qggsource2 as c

def test_authority_plan_and_roots():
    a=c.verify_hqcd_b1qggsource2_authority()
    assert a["status"] == "C190_HQCDB1QGGSOURCE2_GAUSS_CURRENT_INCOMPLETE"
    assert a["plan"] == "QGGSOURCE2-H"
    assert a["C189_package_root"] == "8af65b21a9ba659ad0543be70ea364af2340a6f0c0f5957a0e4fb25d718a258e"
    assert a["contact_coefficients"] == 0 and a["C166_graph_nodes_edges"] == (0,0)
    assert c.load_verified_hqcd_b1qggsource2_authority()["package_root"] == c.PACKAGE_ROOT

def test_canonical_layers_and_inverse():
    assert c.convention_manifest()["status"] == "CLOSED_SOURCE_QUALIFIED"
    assert c.action_manifest()["status"] == "CLOSED_SOURCE_QUALIFIED"
    assert c.field_decomposition_manifest()["independent_constrained_split"]
    assert c.fermion_constraint_manifest()["rows"][0]["status"] == "CLOSED_SOURCE_QUALIFIED"
    assert c.gauss_current_manifest()["status"] == "GAUSS_CURRENT_INCOMPLETE"
    assert c.inverse_longitudinal_manifest()["continuum_substitution"] is False
    assert c.hamiltonian_substitution_manifest()["rows"][0]["counterterms_selected"] == 0
    assert c.normal_order_manifest()["rows"][0]["C129_role"] == "sequential/normal-ordering descendant only"
    assert c.mode_expansion_manifest()["finite_HO_evaluated"] is False

def test_dag_and_owner_source_results():
    dag=c.derivation_dag_manifest()
    assert dag["acyclic"] and dag["source_version_consistent"]
    assert c.c112_source_manifest()["branch_status"] == "PRIMITIVE_BRANCH_PRESENT"
    assert c.c127_source_manifest()["branch_status"] == "BRANCH_INCOMPLETE"
    b=c.branch_manifest()
    assert b["C112_primitive"] and not b["C127_primitive"]
    assert sum(x["terminal"] == "BRANCH_INCOMPLETE" for x in b["rows"]) == 2
    assert c.descendant_reproduction_manifest()["mismatches"] == 0
    assert c.ownership_reconciliation_manifest()["double_count"] == 0

def test_targets_holonomy_requests_and_frontier():
    assert c.target_descendant_manifest()["count"] == 12
    assert c.target_descendant_manifest()["full_cartesian_materialized"] is False
    assert c.holonomy_bc_manifest()["count"] == 20
    req=c.request_resolution_manifest()
    assert req["all_six_visible"]
    assert sum(x["active_in_C190"] for x in req["rows"]) == 2
    assert req["rows"][3]["request4_frozen"] is True
    assert c.source2_release_manifest()["decision"] == "QGG_C112_SOURCE_READY_C127_SOURCE_INCOMPLETE"
    assert c.next_phase_handoff_contract()["next"] == "C191/HQCDB1QGGGAUSS2"

def test_safe_isolation_and_384_mutations():
    assert c.derivation_dag_schema()["eval"] is False
    assert c.static_isolation_guard()["pass"]
    assert c.quantum_nonmutation_manifest()["Q0_Q1_Q2_modified"] is False
    assert all(c.mutate_live_hqcd_b1qggsource2(i)["pass"] for i in range(384))
