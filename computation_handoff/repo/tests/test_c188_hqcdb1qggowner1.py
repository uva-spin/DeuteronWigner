import pytest

from deuteron_wigner.bridge import hqcdb1qggowner1 as c


def test_authority_plan_and_frozen_roots():
    authority = c.verify_hqcd_b1qggowner1_authority()
    assert authority["status"] == "C188_HQCDB1QGGOWNER1_SOURCE_EXPRESSION_INCOMPLETE"
    assert authority["plan"] == "QGGOWNER1-E"
    assert authority["C187_package_root"] == "9a9f7834eb30d28c432a470503bf2f3a720477bf71ebf6a2ffdce0aef075d365"
    assert c.owner_release_manifest()["decision"] == "QGG_NOT_RELEASED_SOURCE_EXPRESSION_INCOMPLETE"
    assert c.request_resolution_manifest()["all_six_visible"] is True


def test_public_source_inventory_and_safe_programs():
    inventory = c.source_inventory_manifest()
    assert inventory["count"] == 5
    assert all(row["completeness"] == "SOURCE_EXPRESSION_AST_INCOMPLETE" for row in inventory["rows"])
    schema = c.source_program_schema()
    assert "SELECT_CREATION_ANNIHILATION_BRANCH" in schema["allowed_opcodes"]
    assert schema["eval"] is False and schema["pickle"] is False and schema["network"] is False
    programs = c.source_program_manifest()
    assert programs["count"] == 2
    assert all(row["safe"] and row["coupling_degree"] == 2 for row in programs["rows"])


def test_branch_census_fail_closed_and_exact_public_zero_scope():
    branches = c.branch_manifest()
    assert branches["count"] == 16
    qgg = [row for row in branches["rows"] if row["branch_id"].endswith("Q_TO_QGG") or row["branch_id"].endswith("QGG_TO_Q")]
    assert len(qgg) == 4
    assert all(row["terminal_classification"] == "BRANCH_INCOMPLETE" for row in qgg)
    assert all(row["net_particle_number"] in (2, -2) for row in qgg)
    assert any(row["terminal_classification"] == "SOURCE_EXCLUDED_EXACT_PUBLIC_ZERO" for row in branches["rows"])
    assert c.branch_manifest(target_sector_id="C170-B1-QGG")["count"] == 2


def test_exclusion_and_factorized_target_adapters():
    exclusions = c.exclusion_manifest()
    assert exclusions["count"] == 4
    assert exclusions["aggregate_double_count"] == 0
    assert all(row["promoted"] is False for row in exclusions["rows"])
    adapters = c.target_adapter_manifest()
    assert adapters["count"] == 12
    assert adapters["full_cartesian_materialized"] is False
    assert adapters["source_preimage_counts"] == "UNAVAILABLE_NOT_ZERO"
    assert all(row["paged_target_iteration"] and row["rank_unrank"] for row in adapters["rows"])


def test_denominator_color_spin_hocm_and_hermitian_descriptors():
    assert c.denominator_manifest()["count"] == 12
    assert c.denominator_manifest()["ordinary_zero_modes"] == 0
    assert c.denominator_manifest()["continuum_substitution"] is False
    assert c.color_descriptor_manifest()["count"] == 4
    assert c.color_descriptor_manifest()["channels_separate"] is True
    assert c.color_descriptor_manifest()["premature_symmetrization"] is False
    assert c.spin_polarization_manifest()["count"] == 4
    assert c.ho_cm_adapter_manifest()["count"] == 12
    assert c.ho_cm_adapter_manifest()["finite_HO_evaluated"] is False
    hermitian = c.hermitian_manifest()
    assert hermitian["count"] == 4
    assert all(row["coefficient_matrix"] is False for row in hermitian["rows"])


def test_holonomy_handoff_topology_and_frontier():
    assert c.holonomy_bc_manifest()["count"] == 20
    assert c.holonomy_bc_manifest()["grid_changed"] is False
    assert c.coefficient_handoff_manifest()["count"] == 12
    assert c.coefficient_handoff_manifest()["executable_next"] is False
    assert c.topology_manifest()["count"] == 9
    assert c.topology_manifest()["direct_sequential_conflation"] is False
    assert c.count_once_manifest()["duplicates"] == 0
    assert c.dependency_frontier_manifest()["graph_delta"] == {"nodes_added": 0, "edges_added": 0}


def test_isolation_and_live_mutations():
    guard = c.static_isolation_guard()
    assert guard["pass"] is True
    assert guard["new_external_sources"] == 0
    assert guard["missing_source_zeros"] == 0
    assert guard["C166_graph_nodes_edges"] == (0, 0)
    assert all(c.mutate_live_hqcd_b1qggowner1(i)["pass"] for i in range(384))
