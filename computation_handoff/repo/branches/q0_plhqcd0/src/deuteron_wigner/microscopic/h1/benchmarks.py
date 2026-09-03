"""Mandatory H-D, H-H, H-J and H-K controlled benchmarks."""

from __future__ import annotations

import numpy as np

from .current import ValenceVectorCurrent
from .planning import H1AssumptionBundle,compile_plan
from .basis import build_basis_tower
from .renormalization import fit_trajectory
from .solvers import exact_solve
from .state import ValenceStateTracker


def renormalization_toy_benchmark():
    # Exactly solvable diagonal sector toy. Refitting delta makes pole mass
    # invariant while the bare self energy and wavefunction charge flow.
    rows=[]
    target=0.81
    for sectors,bare,self_energy in ((2,0.70,0.13),(3,0.64,0.21)):
        counterterm=target-bare-self_energy
        zv=1/(1+0.08*(sectors-1))
        bare_charge=1/zv
        rows.append({"sectors":sectors,"bare_mass2":bare,"self_energy":self_energy,"counterterm":counterterm,"pole_mass2":bare+self_energy+counterterm,"ZV":zv,"bare_charge":bare_charge,"renormalized_charge":zv*bare_charge})
    return rows


def state_tracking_benchmark():
    ts=(-0.2,-0.05,0.05,0.2)
    vectors=[]; values=[]; fingerprints=[]
    for t in ts:
        matrix=np.array([[t,0.04],[0.04,-t]])
        val,vec=np.linalg.eigh(matrix)
        values.append(val); vectors.append(vec)
        fingerprints.append(tuple(float(np.vdot(vec[:,i],np.diag([1,-1])@vec[:,i]).real) for i in range(2)))
    # The diabatic physical identity starting as basis-like state 0 changes
    # eigenvalue ordering through the avoided crossing.
    overlap_chain=[0]
    previous=vectors[0][:,0]
    for vec in vectors[1:]:
        choice=int(np.argmax(np.abs(vec.conj().T@previous)))
        overlap_chain.append(choice); previous=vec[:,choice]
    eigenvalue_only=[0]*len(ts)
    intended_end=int(np.argmax(np.abs(vectors[-1].conj().T@vectors[0][:,0])))
    angle=ValenceStateTracker.principal_angle(vectors[1],vectors[2])
    return {"t":ts,"eigenvalues":values,"fingerprints":fingerprints,"overlap_chain":overlap_chain,"eigenvalue_only":eigenvalue_only,"intended_end":intended_end,"eigenvalue_order_fails":eigenvalue_only[-1]!=intended_end,"principal_angle":angle}


def rotational_benchmark(trajectory):
    rows=[]
    for ham in trajectory.hamiltonians:
        state=exact_solve(ham).eigenvectors[:,0]
        current=ValenceVectorCurrent.for_hamiltonian(ham)
        plus=current.expectation(ham,state,Q2=0.3,component="PLUS")
        transverse=current.expectation(ham,state,Q2=0.3,component="TRANSVERSE")
        rows.append({"resolution_id":ham.basis.resolution.resolution_id,"plus":plus,"transverse":transverse,"defect":abs(transverse-plus)})
    return rows


def confinement_flow_benchmark():
    tower=build_basis_tower()
    out={}
    for name,conf,spin in (("PLAN_A","INDUCED_REFIT","EFFECTIVE_COLOR_SPIN"),("PLAN_B","ZERO_CONFINEMENT","EFFECTIVE_COLOR_SPIN"),("PLAN_C","INDUCED_REFIT","NONE")):
        plan=compile_plan(H1AssumptionBundle(conf,spin))
        trajectory=fit_trajectory(plan,tower)
        rows=[]
        for member,ham in zip(trajectory.members,trajectory.hamiltonians):
            sol=exact_solve(ham); psi=sol.eigenvectors[:,0]
            current=ValenceVectorCurrent.for_hamiltonian(ham)
            lz=np.array([s.Lz for s in ham.basis.states],float)
            rows.append({"resolution_id":member.resolution_id,"mass2":float(sol.eigenvalues[0]),"F1p_Q2_0p3":current.expectation(ham,psi,0.3),"OAM_Lz":float(np.vdot(psi,lz*psi).real),"parameters":dict(member.parameters)})
        out[name]={"plan_id":plan.plan_id,"bundle_id":plan.assumption.bundle_id,"rows":rows}
    return out
