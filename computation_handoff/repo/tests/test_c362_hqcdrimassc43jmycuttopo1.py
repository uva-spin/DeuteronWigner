from deuteron_wigner.bridge import hqcdrimassc43jmycuttopo1 as c
def test_single_cut():assert c.distribution_topology()["cuts"].endswith("only") and "uncut" in c.distribution_topology()["active_quark"]
def test_virtuality():assert "kT^2+x lambda^2+(1-x)^2 m^2" in c.distribution_topology()["active_virtuality"]
def test_correction():assert not c.correction_certificate()["C361_extra_final_quark_cut_required"] and c.correction_certificate()["trace_reduction_safe"]
def test_crossing():assert "one emitted-gluon" in c.fragmentation_topology()["cuts"] and "z^(-2+2epsilon)" in c.fragmentation_topology()["jacobian"]
def test_reload():assert not c.load_verified_hqcdrimassc43jmycuttopo1_authority()["physical"]
def test_mutations():assert all(c.mutate_live_hqcdrimassc43jmycuttopo1(i)["pass"] for i in range(384))
