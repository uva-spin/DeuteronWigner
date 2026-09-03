import numpy as np
import pytest
from deuteron_wigner.nuclear.n3.core import *
from deuteron_wigner.nuclear.n3.injections import INJECTIONS
def test_plans_are_exclusive():
 assert len(plans())==4
 with pytest.raises(Exception):compile_plan([plans()[0].plan_id,plans()[1].plan_id])
 with pytest.raises(Exception):compile_plan([plans()[2].plan_id],naive_sum=True)
def test_delta_basis():
 r=delta_report();assert len(r["charge_basis"])==4 and len(r["partial_waves"])==3 and r["cg_norm_residual"]<1e-14 and r["antisymmetry_residual"]==0 and r["below_threshold_cut"]==0
def test_color_five():
 r=six_quark_color_report();assert r["singlet_multiplicity"]==5 and r["total_generator_residual"]<1e-12 and np.allclose(r["gram"],np.eye(5))
def test_hidden_rotation():
 r=hidden_color_report();assert r["hidden_dimension"]==4 and r["unitarity_residual"]<1e-14 and r["invariance_residual"]<1e-14
def test_s6_antisymmetry():
 r=antisymmetry_report();assert r["sign_representation"] and r["transposition_residual"]==0 and len(r["labels"])==6
def test_cluster_matching():
 r=cluster_report();assert r["projector_idempotence_residual"]<1e-14 and r["orthogonality_residual"]<1e-14 and r["subtraction_equivalence_residual"]<1e-12
def test_hamiltonian_state():
 assert hamiltonian_report()["hermiticity_residual"]==0 and hamiltonian_report()["exact_krylov_residual"]<1e-12 and state_report()["normalization_residual"]<1e-14
def test_current_continuity():
 assert current_report()["complete"] and not current_report()["unexplained_gaps"] and continuity_report()["max_block_residual"]<1e-12
def test_parent_support():
 r=parent_report();assert len(r["delta_helicities"])==4 and "UNAVAILABLE" in r["species"]["ubar"] and not r["physical_zero_claimed"]
def test_tensor_coherent_cp():
 assert tensor_report()["rotation_invariance_residual"]<1e-12 and coherent_report()["early_trace_error"]>0 and cp_report()["early_trace_interference_loss"]>0
def test_ttn_provenance():
 assert ttn_report()["full_bond_residual"]==0 and max(ttn_report()["losses"].values())>.4 and provenance_report()["count_once_residual"]==0
def test_readiness_benchmarks_injections():
 assert not readiness_report()["production_reachable"] and len(benchmark_report()["rows"])==18 and len(INJECTIONS)==400 and len({x[0] for x in INJECTIONS})==400
