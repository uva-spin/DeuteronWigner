import pytest

from deuteron_wigner.bridge import hqcdb1qggcontact1 as c


def test_authority_and_release_boundary():
    authority = c.verify_hqcd_b1qggcontact1_authority()
    assert authority["status"] == c.STATUS
    assert authority["plan"] == "QGGCONTACT1-E"
    assert authority["C186_package_root"] == "df5bf0f48d51f2d47827454b4e31fc8ea2702665f14aa198e07c848bd9b19d20"
    assert c.qgg_contact_release_manifest()["decision"] == "QGG_NOT_RELEASED_PRIMITIVE_AGGREGATE_OWNERSHIP_INCOMPLETE"
    assert c.REQUESTS == tuple(row["request_id"] for row in c.request_resolution_manifest()["rows"])


def test_owner_dag_and_crosswalk_count_once():
    owners = c.owner_manifest()
    dag = c.owner_dag_manifest()
    assert owners["count"] == 6
    assert dag["acyclic"] is True
    assert dag["C131_additive_count"] == 0
    assert c.polynomial_crosswalk_manifest()["C131_additive_count"] == 0
    assert c.count_once_manifest()["C131_additive_count"] == 0
    assert len(dag["edges"]) == 5


def test_source_owner_capsules_are_fail_closed():
    instantaneous = c.instantaneous_fermion_manifest()
    gauss = c.gauss_current_manifest()
    assert instantaneous["count"] == 9
    assert gauss["count"] == 9
    assert all(row["qgg_target_shape"] is None for row in instantaneous["rows"] + gauss["rows"])
    assert instantaneous["qgg_local_matrix"] is False
    assert gauss["qgg_local_matrix"] is False
    with pytest.raises(TypeError):
        c.apply_instantaneous_fermion({}, [], channel_id="QGG_COLOR_1S")
    with pytest.raises(TypeError):
        c.apply_gauss_current({}, [], channel_id="QGG_COLOR_8S")


def test_nonmatrix_and_channel_resolution_census():
    assert c.zero_boundary_manifest()["count"] == 2
    assert c.link_interface_manifest()["count"] == 3
    assert c.color_manifest()["count"] == 18
    assert c.denominator_manifest()["count"] == 18
    assert c.kinematics_manifest()["count"] == 18
    actions = c.action_manifest()
    assert actions["count"] == 54
    assert all(row["typed_nonmatrix"] and row["matrix_application"] == "REJECT" for row in actions["rows"])
    with pytest.raises(TypeError):
        c.apply_order2_owner({}, [], c.OWNER_IDS[0], channel_id="QGG_COLOR_8A")


def test_topology_holonomy_isolation_and_mutations():
    topology = c.topology_manifest()
    assert topology["count"] == 9
    assert topology["direct_sequential_conflation"] is False
    assert topology["complete_qg_1PI"] is False
    assert c.holonomy_bc_manifest()["count"] == 30
    assert c.holonomy_bc_manifest()["longitudinal_grid_changed"] is False
    guard = c.static_isolation_guard()
    assert guard["pass"] is True
    assert guard["C166_graph_nodes_edges"] == (0, 0)
    assert all(c.mutate_live_hqcd_b1qggcontact1(i)["pass"] for i in range(384))
