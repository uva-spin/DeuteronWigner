from deuteron_wigner.bridge import hqcdrimassstate1 as c
def test_fields():assert c.field_closure_ledger()["classes"]==7
def test_capsules():assert c.symbolic_capsule_family()["count"]==3 and c.symbolic_capsule_family()["complete_instances"]==0
def test_kinematics():assert c.kinematic_certificate()["symmetric_nonexceptional"] and not c.kinematic_certificate()["scale_defaulted"]
def test_audit():assert c.forward_reverse_audit()["first_common_missing"]==c.NEXT_OBJECT
def test_covariance():assert not c.covariance_boundary()["missing_as_zero"]
def test_frontier():assert c.residual_frontier()["next"]=="C279/HQCDRIMASSIR1" and not c.residual_frontier()["blocker"]
def test_scope():assert c.static_isolation_guard()["pass"] and c.static_isolation_guard()["physical_scale_selected"]==0
def test_reload():assert c.load_verified_hqcdrimassstate1_authority()["physical"] is False
def test_mutations():assert all(c.mutate_live_hqcdrimassstate1(i)["pass"] for i in range(384))
