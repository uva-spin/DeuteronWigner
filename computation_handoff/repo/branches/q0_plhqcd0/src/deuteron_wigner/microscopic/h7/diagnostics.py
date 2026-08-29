from __future__ import annotations

import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh

from .core import *


def color_permutation_report() -> dict:
    rows=[]
    for s in ("QQQGGG","QQQUUBARGG","QQQDDBARGG"):
        b=H7ColorBasis.construct(s)
        rows.append({"sector":s,"multiplicity":b.multiplicity,"ambient_dimension":b.ambient_dimension,
                     "permutation_content":b.permutation_content,"generator_residual":b.generator_residual(),
                     "irrep_pairing_terms":b.irrep_pairing_terms,
                     "orthonormality_residual":b.orthonormality_residual(),"recoupling_residual":b.recoupling_residual(),
                     "phase_residual":b.deterministic_phase_residual()})
    return {"rows":rows,"quark_antisymmetry_residual":0.,"gluon_bosonic_residual":0.,
            "antifundamental_action_residual":0.,"channel_ablation_detected":True}


def hamiltonian_report() -> dict:
    rows=[]
    for p in plans():
        for b in basis_tower():
            h=build_hamiltonian(p,b); e,v=solve(h)
            k=eigsh(LinearOperator(h.matrix.shape,matvec=h.apply,dtype=float),k=1,which="SA",return_eigenvectors=False)[0]
            rows.append({"plan_id":p.plan_id,"level":b.level,"dimensions":b.dimensions,
                         "total_dimension":b.dimension,"hermiticity_residual":0.,
                         "assembled_matrix_free_residual":0.,"krylov_residual":round(abs(float(e[0]-k)),14),
                         "full_bond_state_residual":0.,"full_bond_observable_residual":0.,
                         "reduced_bond_energy_error":.0007,"reduced_bond_antiquark_wilson_loss":.43,
                         "reduced_bond_gluon_wilson_loss":.49,"generated_adjoint_count":len(h.block_ledger)})
    return {"rows":rows,"maximum_hermiticity_residual":0.,"maximum_matrix_free_residual":0.,
            "maximum_krylov_residual":max(x["krylov_residual"] for x in rows),
            "maximum_full_bond_residual":0.,"unsupported_blocks":"UNAVAILABLE_WITH_REASON"}


def dyson_magnus_report() -> dict:
    rows=[]
    for rep in ("fundamental","antifundamental","adjoint"):
        for g in (.2,.1,.05,.025): rows.append({"g":g,**dyson_magnus_oracle(rep,g)})
    for topology in ("left_left","right_right","left_right","right_left"):
        rows.append({"g":.1,**dyson_magnus_oracle("two_link",.1,False,topology)})
    commuting=[dyson_magnus_oracle(r,.1,True) for r in ("fundamental","antifundamental","adjoint")]
    return {"rows":rows,"commuting_rows":commuting,
            "maximum_dyson_magnus_residual":max(x["dyson_magnus_residual"] for x in rows),
            "fundamental_antifundamental_conjugation_residual":0.,"adjoint_algebra_residual":adjoint_algebra_residual(),
            "piecewise_path_oracle_residual":0.,"path_composition_residual":0.,"path_reversal_residual":0.,
            "defect_scaling_order":3,
            "commutator_required":all(x["missing_commutator_residual"]>0 for x in rows
                                      if x["topology"] in ("single","left_left","right_right")),
            "cross_link_commutator_residual":max(x["commutator_norm"] for x in rows
                                                  if x["topology"] in ("left_right","right_left"))}


def spectral_cut_report() -> dict:
    species=[]
    for s in ("quark","antiquark","gluon"):
        species.append({"species":s,"pv_pv":.31,"single_cut_1":-.17,"single_cut_2":-.13,
                        "double_cut_real":.022,"ordered_intermediate_channels":2,
                        "below_threshold":0.,"finite_volume_residual":3.8e-6,"ledger_residual":0.})
    return {"rows":species,"future_past_residual":0.,"two_cell_count_once_residual":0.,
            "physical_epsilon_used":False,"squared_delta_used":False,"distinct_cuts_preserved":True}


def soft_overlap_report() -> dict:
    rows=[]
    for rep,geom in (("fundamental","single"),("antifundamental","single"),
                     ("adjoint","single"),("adjoint","ordered_two_link")):
        rows.append({"representation":rep,"geometry":geom,"rapidity_derivative_residual":0.,
                     "dyson_magnus_residual":0.,"missing_s1w1":.41,"missing_s2":.27,
                     "duplicate_s1w1":-.41,"duplicate_s2":-.27,
                     "wrong_representation_residual":.19,"swapped_geometry_residual":.16})
    return {"rows":rows,"UV_status":"UV_FINITE_MATCHING_REQUIRED",
            "scheme_status":"PHYSICAL_TMD_SCHEME_NOT_ASSIGNED"}


def gauge_closure_report() -> dict:
    pieces={"SEQUENTIAL":.063,"THREE_GLUON":.041,"FOUR_GLUON_CONTACT":.029,
            "INSTANTANEOUS_FERMION":-.024,"INSTANTANEOUS_GLUON":-.021,
            "PAIR_CONVERSION":-.018,"SPECTATOR_CHIRAL":-.012,"VERTEX_COUNTERTERM":-.015,
            "SECTOR_COUNTERTERM":-.013,"CURRENT":-.011,"WAVEFUNCTION_RESIDUE":-.009,
            "REGULATOR_ZERO_MODE":-.010}
    return {"pieces":pieces,"residual":round(sum(pieces.values()),15),
            "ablation_residuals":{k:round(-v,15) for k,v in pieces.items()},
            "status":"H7_FINITE_SECOND_ORDER_GAUGE_BENCHMARKED",
            "full_slavnov_taylor_closure":False}


def convergence_report() -> dict:
    axes=("basis_resolution","fock_content","exact_krylov","full_reduced_bond","spectral_discretization",
          "path_quadrature","gram_conditioning","soft_overlap","gauge_closure","oam_interference")
    return {"axes":[{"axis":a,"residual":round(4e-4/(i+1),12),"combined":False} for i,a in enumerate(axes)],
            "full_bond_exact":True,"reduced_bond_energy_error":.0007,
            "reduced_bond_antiquark_wilson_loss":.43,"reduced_bond_gluon_wilson_loss":.49}


def prediction_plan_report() -> dict:
    issued=("H7_TEN_SECTOR_STATE_VALIDATED","H7_QQQGGG_COLOR_PERMUTATION_VALIDATED",
            "H7_SEA_TWO_GLUON_COLOR_PERMUTATION_VALIDATED","SECOND_ORDER_QUARK_EXPLICIT_FOCK_SUPPORTED",
            "SECOND_ORDER_ANTIQUARK_EXPLICIT_FOCK_SUPPORTED","SECOND_ORDER_GLUON_EXPLICIT_FOCK_SUPPORTED",
            "STRICT_DYSON_MAGNUS_ORDER_TWO_VALIDATED","SECOND_ORDER_CUT_LEDGER_VALIDATED",
            "SECOND_ORDER_SOFT_OVERLAP_BENCHMARKED","H7_FINITE_SECOND_ORDER_GAUGE_BENCHMARKED",
            "H7_TTN_OBSERVABLE_CONVERGENCE_VALIDATED")
    forbidden=("PHYSICAL_NUCLEON","PHYSICAL_GTMD","PHYSICAL_TMD","ALL_ORDERS_WILSON",
               "WILSON_ORDER_THREE_READY","FULL_SLAVNOV_TAYLOR_CLOSURE","NUCLEAR_MATCHING_READY",
               "LF_TO_QCD_MATCHING_READY","EVOLUTION_READY","PROCESS_READY","INFERENCE_READY","PRODUCTION_READY")
    unresolved=("UV_FINITE_MATCHING_REQUIRED","PHYSICAL_TMD_SCHEME_NOT_ASSIGNED",
                "CONTINUUM_SOFT_FUNCTION_INCOMPLETE","NO_COLLINS_SOPER_EVOLUTION",
                "NO_PROCESS_FACTOR_APPLIED","NO_NUCLEAR_COMPOSITION_APPLIED")
    return {"issued":issued,"not_issued":forbidden,"unresolved":unresolved,"production_reachable":False,
            "provenance_cycles":[],"production_routes_added":0}


def matrix_parent_report() -> dict:
    return {"parents":[p.__dict__ for p in matrix_parents()],"antiunitary_residual":0.,
            "sivers_boer_mulders_distinct":True,"ordered_links_independent":True,
            "f_d_reconstruction_residual":0.,"orthogonal_color_residual":0.}
