from deuteron_wigner.bridge import hqcdrimassc43sidisdata1 as c
def test_family(): assert c.family_manifest()["dataset_count"]==10 and c.family_manifest()["selected_point_count"]==582
def test_records(): assert c.family_manifest()["all_kinematics_present"] and c.family_manifest()["all_covariance_constructible"]
def test_covariance(): assert not c.covariance_semantics()["diagonalized"]
def test_readiness(): assert c.readiness()["dataset_authority_recovered"] and not c.readiness()["physical_capsule_complete"]
def test_reload(): assert not c.load_verified_hqcdrimassc43sidisdata1_authority()["physical"]
def test_mutations(): assert all(c.mutate_live_hqcdrimassc43sidisdata1(i)["pass"] for i in range(384))
