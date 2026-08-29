import pytest
from deuteron_wigner.matching.m0.core import *
from deuteron_wigner.matching.m0.injections import INJECTIONS
def test_scheme():assert scheme_report()["roundtrip_residual"]<1e-12 and scheme_report()["bDelta_distinct_bTMD"]
def test_basis():assert basis_report()["lf_dimension"]==basis_report()["qcd_dimension"] and basis_report()["named_tmd_parameters"]==0
def test_matching():assert matching_report()["conditions"]>matching_report()["parameters"] and matching_report()["holdouts"]>0
def test_step_uv():assert step_scaling_report()["cocycle_residual"]<1e-12 and uv_soft_report()["missing_soft_residual"]==-uv_soft_report()["duplicate_soft_residual"]
def test_rank():assert len(rank_report()["rows"])==4 and rank_report()["scalar_alias_rejected"]
def test_ope():assert ope_report()["closure_residual"]<1e-12 and "UNAVAILABLE" in ope_report()["physical_todd_coefficients"]
def test_collinear():assert collinear_report()["singlet_momentum_residual"]<1e-12 and collinear_report()["unsupported_twist3_rejected"]
def test_evolution():assert evolution_report()["integrable_path_residual"]<1e-12 and evolution_report()["finite_order_curl"]>0 and evolution_report()["rank_preserved"]
def test_threshold_nuclear():assert threshold_report()["matched_moment_residual"]<1e-12 and nuclear_report()["hidden_color_covariance_residual"]<1e-12
def test_accuracy_readiness():assert accuracy_report()["laundering_rejected"] and not readiness_report()["production_reachable"]
def test_benchmarks_injections():assert len(benchmark_report()["rows"])==18 and len(INJECTIONS)==480 and len({x[0] for x in INJECTIONS})==480
