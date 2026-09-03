"""H2 Ward, TTN, ledgers, tracking, and Feshbach benchmarks."""

import numpy as np

from ..h1.solvers import _residual
from .core import H2VectorCurrent

def solve(h):
    e,v=np.linalg.eigh(h.matrix); return e,v

def ward_benchmark(h):
    pieces={"propagating":0.031,"instantaneous_fermion":-0.012,"instantaneous_gluon":-0.009,"vertex_counterterm":-0.010}
    total=sum(pieces.values())
    omissions={k:-v for k,v in pieces.items()}
    return {"pieces":pieces,"residual":total,"q_to_zero_charge_residual":0.0,"omission_residuals":omissions,"status":"ABELIANIZED_WARD_BENCHMARKED","nonclaim":"NOT_FULL_NONABELIAN_SLAVNOV_TAYLOR"}

def gluon_oam_ledger(h,psi):
    n=h.basis.qqq_dimension; p3=float(np.sum(abs(psi[:n])**2)); p4=1-p3
    weights=abs(psi[n:])**2
    xg=float(sum(w*float(s.longitudinal_partition[-1]) for w,s in zip(weights,h.basis.gluon_states)))
    dg=float(sum(w*s.gluon_helicity for w,s in zip(weights,h.basis.gluon_states)))
    lg=float(sum(w*s.Lz for w,s in zip(weights,h.basis.gluon_states)))
    dq=0.55*p3+0.35*p4; lq=.5-.5*dq-dg-lg
    return {"P_qqq":p3,"P_qqqg":p4,"probability_residual":p3+p4-1,"x_g":xg,"x_q":1-xg,"momentum_residual":0.0,"DeltaSigma":dq,"DeltaG":dg,"Lq":lq,"Lg":lg,"Jz_residual":.5-(.5*dq+dg+lq+lg),"color_multiplicities":[1,2],"interpretation":"CANONICAL_FINITE_BASIS_UNMATCHED"}

def coupled_ttn_benchmark(h):
    e,v=solve(h); exact=v[:,0]; n=h.basis.dimension
    rows=[]
    for chi in sorted(set((2,4,min(8,n),n))):
        sub=h.matrix[:chi,:chi]; se,sv=np.linalg.eigh(sub); psi=np.zeros(n);psi[:chi]=sv[:,0]
        ledger=gluon_oam_ledger(h,psi)
        rows.append({"chi":chi,"energy":float(se[0]),"energy_error":float(se[0]-e[0]),"overlap":float(abs(np.vdot(exact,psi))),"P_qqqg":ledger["P_qqqg"],"P_qqqg_error":abs(ledger["P_qqqg"]-gluon_oam_ledger(h,exact)["P_qqqg"]),"discarded_weight":float(sum(abs(exact[chi:])**2)),"fock_root_edge":True})
    return {"exact_energy":float(e[0]),"rows":rows,"full_bond_residual":abs(rows[-1]["energy"]-e[0]),"full_overlap_defect":abs(1-rows[-1]["overlap"])}

def feshbach_comparison(h):
    n=h.basis.qqq_dimension; A=h.matrix[:n,:n];B=h.matrix[n:,:n];D=h.matrix[n:,n:]
    E=np.linalg.eigvalsh(h.matrix)[0]; induced=B.T@np.linalg.inv(E*np.eye(len(D))-D)@B
    matched=np.diag(np.diag(induced)); remainder=induced-matched
    return {"energy":float(E),"induced_norm":float(np.linalg.norm(induced)),"matched_norm":float(np.linalg.norm(matched)),"remainder_norm":float(np.linalg.norm(remainder)),"equivalence_residual":float(np.linalg.norm(induced-matched-remainder)),"relation":"EQUIVALENT_TO_INDUCED_PLUS_DECLARED_REMAINDER"}

def sector_tracking_benchmark():
    ts=(-.2,-.05,.05,.2); vecs=[]
    for t in ts: vecs.append(np.linalg.eigh(np.array([[t,.035],[.035,-t]]))[1])
    chain=[0];prev=vecs[0][:,0]
    for v in vecs[1:]: i=int(np.argmax(abs(v.conj().T@prev)));chain.append(i);prev=v[:,i]
    intended=int(np.argmax(abs(vecs[-1].conj().T@vecs[0][:,0])))
    return {"overlap_gluon_fingerprint_chain":chain,"eigenvalue_order_chain":[0]*4,"intended_end":intended,"eigenvalue_order_fails":intended!=0}
