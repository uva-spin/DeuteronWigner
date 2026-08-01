from deuteron_wigner.evolution.m2.core import *
from deuteron_wigner.evolution.m2.injections import INJECTIONS
H={x:"h" for x in ("2002.04617","2205.02242")}
def test_anomalous():assert len(anomalous_records(H))==7 and anomalous_report(H)["quartic_casimir_visible"]
def test_coupling():assert coupling_report()["forward_reverse_residual"]<1e-10 and coupling_report()["threshold_order"]==3
def test_kernels():assert not kernel_report()["one_kernel_per_tmd"] and not kernel_report()["gluon"]["nonperturbative_casimir_scaling"]
def test_evolution():assert evolution_report()["exact_path_residual"]<1e-10 and evolution_report()["finite_order_curl"]>0 and not evolution_report()["curl_fitted_away"]
def test_capability():assert len(capability_report()["rows"])==540 and capability_report()["matching_executable"]==492 and capability_report()["matching_unavailable"]==48
def test_multiq():assert len(multiq_report()["grid"])>=7 and multiq_report()["rank_preserved"] and len(multiq_report()["ranks"])==4
def test_collinear():assert collinear_report()["singlet_momentum_residual"]<1e-10 and collinear_report()["twist3_unavailable"]
def test_nuclear():assert nuclear_report()["impulse_commutation_residual"]<1e-10 and not nuclear_report()["scalar_collapse"]
def test_accuracy_holdouts():assert len(uncertainty_report())==17 and accuracy_report()["laundering_rejected"] and len(holdout_report()["classes"])==6
def test_release():assert len(INJECTIONS)==640 and len({x[0] for x in INJECTIONS})==640 and not readiness_report()["production_reachable"]
