from deuteron_wigner.bridge import hqcdrimasslfloop1 as c
def test_partition():assert c.loop_partition()["count"]==10 and c.loop_partition()["kernel_ready"]==9
def test_nozero():assert not c.loop_partition()["missing_as_zero"]
def test_programs():assert len(c.resolution_programs()["rows"])==3 and not c.resolution_programs()["rows"][0]["full_executable"]
def test_owners():assert c.owner_count_once()["duplicates"]==0 and not c.owner_count_once()["residual_link_additive_before_composition"]
def test_routes():assert not c.route_certificate()["false_agreement"]
def test_frontier():assert c.residual_frontier()["next"]=="C285/HQCDRIMASSLINKGEOM1" and not c.residual_frontier()["blocker"]
def test_scope():assert c.static_isolation_guard()["pass"] and c.static_isolation_guard()["link_unity_assumed"]==0
def test_reload():assert c.load_verified_hqcdrimasslfloop1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimasslfloop1(i)["pass"] for i in range(384))
