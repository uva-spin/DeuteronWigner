from deuteron_wigner.bridge import hqcdc117nonlocalmatch1 as c
def test_packets_functionals(): assert c.packet_family()["count"]==4 and c.matching_functionals()["all_fields_closed"]
def test_distribution_scope(): assert not c.distributional_pairings()["pointwise_delta_evaluation"] and not c.distributional_pairings()["tail_zeroed"]
def test_channels(): assert c.channel_amplitudes()["CM"]["excited_leakage"]==0 and c.channel_amplitudes()["triplet"]["anti_sextet_leakage"]==0
def test_rank(): assert all(x["rank"]==4 and x["condition_number"]==1 for x in c.response_matrices()["rows"])
def test_separation(): assert c.response_matrices()["K_separate"] and not c.response_matrices()["resolution_average"]
def test_targets_path(): assert c.target_semantics()["zeros_selected"]==0 and c.standard_matching_path()["path_exists"] and not c.standard_matching_path()["values_ready"]
def test_reload_scope(): assert c.static_isolation_guard()["pass"] and c.load_verified_hqcdc117nonlocalmatch1_authority()["physical"] is False
def test_mutations(): assert all(c.mutate_live_hqcdc117nonlocalmatch1(i)["pass"] for i in range(384))
