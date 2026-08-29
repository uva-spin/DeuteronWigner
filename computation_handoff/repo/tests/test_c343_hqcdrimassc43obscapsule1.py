from deuteron_wigner.bridge import hqcdrimassc43obscapsule1 as c
def test_schema(): assert c.capsule_schema()["required_count"]==9 and c.capsule_schema()["bound_count"]==3
def test_missing(): assert set(c.satisfiability_certificate()["missing_fields"])=={"kinematics","renormalization_scales","finite_volume_sequence","covariance","acceptance","ensemble_weights"}
def test_no_promotion(): assert c.repository_audit()["complete_candidate_count"]==0 and c.repository_audit()["numerical_values_bound"]==0
def test_fail_closed(): assert c.satisfiability_certificate()["activation_gate"]=="NOT_READY"
def test_reload(): assert not c.load_verified_hqcdrimassc43obscapsule1_authority()["physical"]
def test_mutations(): assert all(c.mutate_live_hqcdrimassc43obscapsule1(i)["pass"] for i in range(384))
