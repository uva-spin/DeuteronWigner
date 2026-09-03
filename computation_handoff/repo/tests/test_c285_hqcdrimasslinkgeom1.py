from deuteron_wigner.bridge import hqcdrimasslinkgeom1 as c
def test_paths():assert c.source_path_family()["count"]==2 and not c.source_path_family()["unique_selected"]
def test_orientations():assert not c.source_path_family()["future_past_merged"]
def test_geometry():assert len(c.finite_cell_geometry_family()["rows"])==3 and not c.finite_cell_geometry_family()["endpoint_substitution"]
def test_transport():assert not c.representation_transport()["link_unity"] and not c.representation_transport()["holonomy_sector_selected"]
def test_compose():assert c.composability_audit()["path_class"] and not c.composability_audit()["project_path_selected"]
def test_frontier():assert c.residual_frontier()["next"]=="C286/HQCDRIMASSPATHSELECT1" and not c.residual_frontier()["blocker"]
def test_scope():assert c.static_isolation_guard()["pass"] and c.static_isolation_guard()["identity_fixture_promoted"]==0
def test_reload():assert c.load_verified_hqcdrimasslinkgeom1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimasslinkgeom1(i)["pass"] for i in range(384))
