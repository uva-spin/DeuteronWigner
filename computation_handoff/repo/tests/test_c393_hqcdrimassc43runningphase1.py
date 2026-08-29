from deuteron_wigner.bridge import hqcdrimassc43runningphase1 as c
def rec(nf=4,mu=2):return {"record_id":"x","Nf":nf,"mu":mu,"mu_units":"GeV","threshold_side":"fixed-sector","active_flavors":tuple("udsctb"[:nf]),"heavy_flavors":tuple("udsctb"[nf:]),"source_root":c.PDG_SHA,"no_default":True}
def test_beta_threshold():assert "b0" in c.beta_function_manifest()["coefficients"] and c.threshold_manifest()["mass_scheme_branch_required"]
def test_running_roundtrip():
 a=c.evolve_one_loop(.1,2,3,rec());b=c.evolve_one_loop(a["alpha_s"],3,2,rec());assert abs(b["alpha_s"]-.1)<1e-14
def test_nf_guard():assert c.validate_active_flavor_record(rec())["Nf"]==4
def test_resolution_conversion():assert len(c.resolution_transport_manifest())==3 and c.standard_conversion_manifest()["coefficients"].endswith("not zero")
def test_reload_mutations():assert not c.load_verified_hqcdrimassc43runningphase1_authority()["physical"] and all(c.mutate_live_hqcdrimassc43runningphase1(i)["pass"] for i in range(384))
