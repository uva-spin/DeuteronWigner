from deuteron_wigner.bridge import hqcdrimassc43physicalobsinputphase1 as c
def test_dataset():assert c.dataset_inventory()["points"]==334 and c.dataset_inventory()["correlated_errors"]==1
def test_points():
 p=c.point_manifest();assert len(p)==334 and p[0]["x_bin"][0]<=p[0]["x"]<=p[0]["x_bin"][1]
def test_covariance():assert c.covariance_entry(0,0)>0 and c.covariance_entry(0,1)!=0 and c.covariance_manifest()["PSD_proof"]
def test_ensemble_nonclaim():assert not c.ensemble_binding_manifest()["normalized_ensemble_membership"] and all(not x["averaged"] for x in c.ensemble_binding_manifest()["rows"])
def test_reload_mutations():assert not c.load_verified_hqcdrimassc43physicalobsinputphase1_authority()["physical"] and all(c.mutate_live_hqcdrimassc43physicalobsinputphase1(i)["pass"] for i in range(384))
