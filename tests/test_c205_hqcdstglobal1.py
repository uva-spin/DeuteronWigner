from deuteron_wigner.bridge import hqcdstglobal1 as c
import pytest

def _p():
 return {"record_id":"test-global","resolution":"K9","sector_id":"GLOBAL_SU3","holonomy_capsule_id":"C183-GENERIC-NONPHYSICAL","capsule_class":"GENERIC","global_frame_id":"C183-CALLER-FRAME","orbit_id":"SU3-ORBIT","stabilizer_id":"GENERIC-TORUS","measure_convention":"SYMBOLIC_UNNORMALIZED_ORBIT_STABILIZER","zero_mode_basis_id":"C175-GLOBAL-ZERO","counterterm_coordinates":c.CT,"null_coordinates":c.NULL,"branch":"caller-symbolic","enclosure":"EXACT_SYMBOLIC_OUTWARD","no_defaults":True,"physical":False}

def test_authority_frontier():
 assert c.verify_hqcd_stglobal1_authority()["C204_package_root"]==c.C204_ROOT
 assert c.frontier_manifest("C197-ST-7")["rows"][0]["aliases"] == ("global zero-mode/gauge-volume treatment","GLOBAL_GAUGE_VOLUME_IDENTITY")
 assert c.frontier_manifest()["ordered_remaining"][0]=="C197-ST-8"
def test_inventory_parameters_programs():
 assert c.global_inventory_manifest()["count"]==180
 assert c.global_program_manifest()["count"]==6
 assert c.validate_global_parameter_record(_p())["valid"]
 bad=dict(_p());bad["measure_convention"]="UNIT_VOLUME"
 with pytest.raises(ValueError):c.validate_global_parameter_record(bad)
def test_zero_stabilizer_frame_identity():
 assert c.zero_mode_decomposition_manifest()["count"]==12
 assert c.holonomy_stabilizer_manifest()["count"]==4
 assert c.frame_covariance_manifest()["count"]==3
 assert c.orbit_volume_identity_manifest()["count"]==12
 iid=c.orbit_volume_identity_manifest()["rows"][0]["identity_id"]
 assert c.evaluate_orbit_volume_identity(_p(),iid)["absolute_normalization"]=="UNSELECTED"
def test_jacobian_replacement_release():
 j=c.jacobian_manifest();assert (j["dimensions"],j["rank"],j["nullity"],j["left_nullity"])==((7,15),1,14,6)
 assert c.st_replacement_manifest()["unrelated_rows_changed"]==0
 assert c.stglobal1_release_manifest()["gates"]["absolute_volume_normalization"] is False
 assert c.next_st_handoff_contract()["next_object"]=="C197-ST-8"
def test_isolation_mutations():
 assert c.static_isolation_guard()["pass"]
 assert all(c.mutate_live_hqcdstglobal1(i)["pass"] for i in range(384))
 assert c.stglobal1_completeness_certificate()["remaining_frontier"]==3
