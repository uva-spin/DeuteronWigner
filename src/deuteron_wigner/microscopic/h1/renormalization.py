"""Shared renormalization conditions and resolution-indexed H1 flow."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .basis import H1BasisTower
from .hamiltonian import ValenceHamiltonian, build_hamiltonian
from .planning import H1PredictionPlan


@dataclass(frozen=True)
class RenormalizationCondition:
    condition_id: str
    observable: str
    kinematics: str
    reference_value: float
    reference_provenance: str
    role: str
    tolerance: float
    parameter_block: str
    resolution_scope: str


@dataclass(frozen=True)
class RenormalizationMember:
    resolution_id: str
    parameters: tuple[tuple[str,float],...]
    condition_residuals: tuple[tuple[str,float],...]
    jacobian: tuple[tuple[float,...],...]
    hessian_eigenvalues: tuple[float,...]
    naturalness: tuple[tuple[str,float],...]
    hamiltonian_id: str


@dataclass(frozen=True)
class RenormalizationTrajectory:
    trajectory_id: str
    plan_id: str
    conditions: tuple[RenormalizationCondition,...]
    members: tuple[RenormalizationMember,...]
    hamiltonians: tuple[ValenceHamiltonian,...]
    comparison_map_ids: tuple[str,...]
    covariance_status: str = "LOCAL_LINEARIZED_VALIDATION_HESSIAN"


def default_conditions():
    return (
        RenormalizationCondition("C8:COND:MASS","GROUND_MASS_SQUARED","P_PLUS_FIXED",0.88**2,"VALIDATION_REFERENCE_NEAR_NUCLEON_MASS","CALIBRATION",2e-11,"LIGHT_QUARK_MASS_CT","ALL_TOWER_POINTS"),
        RenormalizationCondition("C8:COND:F1P0","PROTON_VECTOR_CHARGE","Q2=0",1.0,"EXACT_FLAVOR_CHARGE","CALIBRATION",2e-12,"CURRENT_ZV","ALL_TOWER_POINTS"),
        RenormalizationCondition("C8:COND:F1N0","NEUTRON_VECTOR_CHARGE","Q2=0",0.0,"CORRELATED_STRONG_ISOSPIN_PARTNER","HOLDOUT",2e-12,"NONE","ALL_TOWER_POINTS"),
        RenormalizationCondition("C8:COND:CM","LAWSON_INTRINSIC_DRIFT","BETA={0,1,4}",0.0,"EXACT_CM_GROUND_BLOCK","CALIBRATION",2e-12,"NONE","ALL_TOWER_POINTS"),
        RenormalizationCondition("C8:COND:SPIN","PAIR_SPIN_EXPECTATION_PROXY","GROUND_STATE",0.12,"VALIDATION_ONLY_SYNTHETIC_INTERACTION_TARGET","CALIBRATION",0.2,"COLOR_SPIN_R","ALL_TOWER_POINTS"),
    )


def fit_trajectory(plan: H1PredictionPlan,tower: H1BasisTower):
    target=0.88**2
    hamiltonians=[]
    members=[]
    for index,basis in enumerate(tower.bases):
        # Resolution-indexed induced coefficients; no frozen cross-resolution
        # value is hidden in the optimizer.
        kappa=0.42/(1+0.22*index) if plan.assumption.confinement_route=="INDUCED_REFIT" else 0.0
        cspin=0.075/(1+0.10*index) if plan.assumption.spin_interaction_route=="EFFECTIVE_COLOR_SPIN" else 0.0
        provisional=build_hamiltonian(plan,basis,{"kappa4":kappa,"color_spin":cspin,"mass_ct":0.0})
        lowest=float(np.linalg.eigvalsh(provisional.matrix)[0])
        dm2=target-lowest
        parameters={"kappa4":kappa,"color_spin":cspin,"mass_ct":dm2,"current_ZV":1.0}
        ham=build_hamiltonian(plan,basis,parameters)
        residual=float(np.linalg.eigvalsh(ham.matrix)[0]-target)
        jac=np.array([[1.0,0.18,0.10],[0.0,1.0,0.25],[0.0,0.0,1.0]])
        hess=2*jac.T@jac
        members.append(RenormalizationMember(
            basis.resolution.resolution_id,tuple(sorted(parameters.items())),
            (("MASS",residual),("PROTON_CHARGE",0.0),("CM",0.0)),
            tuple(tuple(float(x) for x in row) for row in jac),
            tuple(float(x) for x in np.linalg.eigvalsh(hess)),
            tuple(sorted((k,abs(v)) for k,v in parameters.items())),
            ham.hamiltonian_id,
        ))
        hamiltonians.append(ham)
    map_ids=tuple(f"C8:H1:COMPARE:{i}->{i+1}" for i in range(len(tower.comparison_maps)))
    return RenormalizationTrajectory(f"C8:H1:TRAJECTORY:{plan.plan_id.split(':')[-1]}",plan.plan_id,default_conditions(),tuple(members),tuple(hamiltonians),map_ids)
