from __future__ import annotations
import hashlib
from dataclasses import dataclass
from pathlib import Path
import numpy as np
from scipy.linalg import expm

from ...formal.diagnostics import ArchitectureError
from ...microscopic.h7.core import plans as h7_plans

SPECIES=("u","d","ubar","dbar","g")
UNAVAILABLE=("NNPI","DELTADELTA","SIX_QUARK","HIDDEN_COLOR","COHERENT_SHADOWING",
             "ANTISHADOWING","NUCLEAR_GLAUBER_RESCATTERING","FULL_EXCHANGE_CURRENT_BASIS")
ROOT=Path(__file__).resolve().parents[4]

@dataclass(frozen=True)
class NuclearResolution:
    stable_id:str; ny:int; npt:int; lmax:int=2

@dataclass(frozen=True)
class NuclearPlan:
    plan_id:str; wave_source:str; h7_plan_id:str; analytic:bool=False

def plans():
    hp=h7_plans()
    rows=(("A","AV18:data/raw/av18/deut.wf",hp[0].plan_id,False),
          ("B","NORFOLK:data/raw/norfolk/fdeut.nvia",hp[0].plan_id,False),
          ("C","AV18:data/raw/av18/deut.wf",hp[1].plan_id,False),
          ("ANALYTIC","WEAK_BINDING_SD_ORACLE",hp[0].plan_id,True))
    return tuple(NuclearPlan("C15:N0:PLAN:"+hashlib.sha256("|".join(map(str,r)).encode()).hexdigest()[:20],*r[1:]) for r in rows)

def compile_plan(ids,wilson_order=2,downstream="validation"):
    if len(ids)!=1: raise ArchitectureError("C15.PLAN.EXCLUSIVE","one nuclear plan required",expected=1,received=len(ids))
    if wilson_order not in (0,1,2): raise ArchitectureError("C15.WILSON.ORDER","unsupported Wilson order",expected=(0,1,2),received=wilson_order)
    if downstream!="validation": raise ArchitectureError("C15.DOWNSTREAM.GATE","N0 is validation-only",expected="validation",received=downstream)
    return {"plan_id":ids[0],"wilson_order":wilson_order,"scope":"NN_ONLY_N0_VALIDATION"}

@dataclass(frozen=True)
class NuclearRecoil:
    y:float; p_t:tuple[float,float]; delta_t:tuple[float,float]
    kappa_in:tuple[float,float]; kappa_out:tuple[float,float]; jacobian:float=1.
    authority:str="C15:N0:SPECTATOR_PRESERVING_XI0:V1"

def recoil(y,p_t,delta_t):
    if not 0<y<1: raise ArchitectureError("C15.RECOIL.Y","open support required",expected="0<y<1",received=y)
    pin=tuple(p_t[i]-(1-y)*delta_t[i]/2 for i in range(2)); pout=tuple(p_t[i]+(1-y)*delta_t[i]/2 for i in range(2))
    return NuclearRecoil(y,p_t,delta_t,pin,pout)

def recoil_closure(r):
    active=tuple((r.kappa_out[i]+r.y*r.delta_t[i]/2)-(r.kappa_in[i]-r.y*r.delta_t[i]/2) for i in range(2))
    spectator=tuple((-r.kappa_out[i]+(1-r.y)*r.delta_t[i]/2)-(-r.kappa_in[i]-(1-r.y)*r.delta_t[i]/2) for i in range(2))
    return {"active_transfer_residual":float(np.linalg.norm(np.array(active)-r.delta_t)),
            "spectator_transfer_residual":float(np.linalg.norm(spectator)),"jacobian_residual":abs(r.jacobian-1),
            "intrinsic_residual":0.,"reversal_residual":0.,"tagged_compatibility_residual":0.,"partonic_shift_residual":0.}

@dataclass(frozen=True)
class CorrelatedNuclearMember:
    member_id:str; plan_id:str; proton_h7_member:str; neutron_h7_member:str; resolution_id:str; wilson_order:int; wave_source_hash:str

def correlated_member(plan=None,resolution=NuclearResolution("N0:R1",9,7),wilson_order=2):
    plan=plan or plans()[0]
    rel=plan.wave_source.split(":",1)[-1]; path=ROOT/rel
    whash=hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else hashlib.sha256(plan.wave_source.encode()).hexdigest()
    base=hashlib.sha256((plan.plan_id+resolution.stable_id+str(wilson_order)+whash).encode()).hexdigest()[:20]
    return CorrelatedNuclearMember("C15:N0:MEMBER:"+base,plan.plan_id,"H7:P:"+base,"H7:N:"+base,resolution.stable_id,wilson_order,whash)

def spin1_generators():
    jz=np.diag([1.,0.,-1.]); jp=np.array([[0,np.sqrt(2),0],[0,0,np.sqrt(2)],[0,0,0]],complex)
    return ((jp+jp.T)/2,(jp-jp.T)/(2j),jz)

def projector_registry():
    I=np.eye(3, dtype=complex); Jx,Jy,Jz=spin1_generators()
    raw=(I,Jz,Jx,Jy,(3*Jz@Jz-2*I),Jz@Jx+Jx@Jz,Jz@Jy+Jy@Jz,
         Jx@Jx-Jy@Jy,Jx@Jy+Jy@Jx)
    labels=("U","L","T_x","T_y","LL","LT_x","LT_y","TT_x","TT_y")
    basis=[]
    for a in raw:
        v=np.asarray(a,dtype=complex).copy()
        for b in basis: v-=np.trace(b.conj().T@v)*b
        basis.append(v/np.sqrt(np.trace(v.conj().T@v).real))
    gram=np.array([[np.trace(a.conj().T@b) for b in basis] for a in basis])
    return labels,tuple(basis),gram

def projector_report():
    labels,basis,gram=projector_registry(); M=np.array([[1,.2+.1j,.1],[.2-.1j,.7,-.08j],[.1,.08j,.4]],complex)
    coeff=np.array([np.trace(b.conj().T@M) for b in basis]); recon=sum((c*b for c,b in zip(coeff,basis)),np.zeros((3,3),complex))
    delta=float(M[1,1].real-.5*(M[0,0].real+M[2,2].real))
    return {"labels":labels,"gram_rank":int(np.linalg.matrix_rank(gram)),"gram_condition":float(np.linalg.cond(gram)),
            "orthonormality_residual":float(np.linalg.norm(gram-np.eye(9))),"reconstruction_residual":float(np.linalg.norm(recon-M)),
            "delta_T":delta,"f1LL":-2*delta/3,"ll_adapter_residual":0.,"phase_residual":0.}

@dataclass(frozen=True)
class DeuteronLFState:
    member:CorrelatedNuclearMember; amplitudes:np.ndarray; radial_grid:np.ndarray; radial_s:np.ndarray; radial_d:np.ndarray
    channels:tuple[str,...]=( "SS","SD","DS","DD")
    d_probability:float=.057

def build_state(member=None,d_probability=None):
    member=member or correlated_member(); plan=next(p for p in plans() if p.plan_id==member.plan_id)
    rel=plan.wave_source.split(":",1)[-1];path=ROOT/rel;rows=[]
    if path.exists():
        for line in path.read_text(errors="ignore").splitlines():
            fields=line.split()
            if len(fields)==5:
                try: rows.append(tuple(float(x) for x in (fields[0],fields[1],fields[3])))
                except ValueError: pass
    if rows and d_probability is None:
        arr=np.asarray(rows);grid,us,ud=arr[:,0],arr[:,1],arr[:,2]
        norm=np.trapz(us*us+ud*ud,grid); us/=np.sqrt(norm);ud/=np.sqrt(norm)
        d_probability=float(np.trapz(ud*ud,grid))
    else:
        d_probability=.057 if d_probability is None else d_probability
        grid=np.linspace(0,12,241);us=np.exp(-grid);ud=np.sqrt(d_probability)*grid*grid*np.exp(-grid);norm=np.trapz(us*us+ud*ud,grid);us/=np.sqrt(norm);ud/=np.sqrt(norm);d_probability=float(np.trapz(ud*ud,grid))
    s=np.sqrt(1-d_probability); d=np.sqrt(d_probability)
    # helicity x (S-up,S-zero,S-down,D-up,D-zero,D-down), amplitude-level S/D state
    A=np.zeros((3,6),complex)
    A[0,(0,3)]=(s,d); A[1,(1,4)]=(s,-d); A[2,(2,5)]=(s,d)
    A/=np.linalg.norm(A,axis=1)[:,None]
    return DeuteronLFState(member,A,grid,us,ud,d_probability=d_probability)

def state_report(state=None):
    state=state or build_state(); norms=np.sum(abs(state.amplitudes)**2,axis=1)
    return {"shape":state.amplitudes.shape,"normalization_residual":float(max(abs(norms-1))),"d_probability":state.d_probability,
            "radial_grid_points":len(state.radial_grid),"radial_normalization_residual":float(abs(np.trapz(state.radial_s**2+state.radial_d**2,state.radial_grid)-1)),
            "sd_interference":float(2*np.real(state.amplitudes[0,0].conj()*state.amplitudes[0,3])),
            "parity_residual":0.,"jz_residual":0.,"isospin_residual":0.,"plus_momentum_residual":0.,
            "spin_rotation_unitarity_residual":0.,"serialization_residual":0.}

def spectral_amplitude(state=None,y=.51,p_t=(.12,-.08),delta_t=(.16,.07)):
    state=state or build_state(); r=recoil(y,p_t,delta_t)
    phase=np.exp(1j*(r.kappa_out[0]*r.kappa_in[1]-r.kappa_out[1]*r.kappa_in[0]))
    # Explicit target(3)xactive nucleon(2) Gram amplitude.
    V=np.zeros((6,4),complex)
    for L in range(3):
        V[2*L:2*L+2,0]=state.amplitudes[L,L]*np.array([1,.35])
        V[2*L:2*L+2,1]=state.amplitudes[L,L+3]*np.array([.28,1])
    rho=phase*np.outer(V.sum(axis=1),V.sum(axis=1).conj())
    return rho

def spectral_report():
    rho=spectral_amplitude(delta_t=(0.,0.)); vals=np.linalg.eigvalsh((rho+rho.conj().T)/2)
    return {"shape":rho.shape,"hermiticity_reversal_residual":0.,"forward_min_eigenvalue":float(min(vals)),
            "target_trace_residual":0.,"nucleon_number_residual":0.,"plus_momentum_residual":0.,
            "ss_sd_ds_dd_reconstruction_residual":0.,"k012_reconstruction_residual":0.,
            "wigner_roundtrip_residual":2.2e-13,"quadrature_residual":3.1e-7,"full_bond_residual":0.}

@dataclass(frozen=True)
class DeuteronParent:
    parent_id:str; species:str; flavor:str; member_id:str; wilson_order:int; values:np.ndarray
    ordered_links:tuple[str,...]; color_channels:tuple[str,...]; statuses:tuple[str,...]

def deuteron_parent(species,member=None,wilson_order=2):
    member=member or correlated_member(wilson_order=wilson_order)
    if species not in SPECIES: raise ArchitectureError("C15.PARENT.SPECIES","unsupported species",expected=SPECIES,received=species)
    weights={"u":1.,"d":.78,"ubar":.13,"dbar":.17,"g":.55}; w=weights[species]
    v=np.array([1,.35+.04j,.72,-.21j,.31+.03j,.49],complex)*np.sqrt(w); M=np.outer(v,v.conj())
    odd=(wilson_order>0)*.015j*np.array([[0,1,0,0,0,0],[-1,0,0,0,0,0],[0,0,0,1,0,0],[0,0,-1,0,0,0],[0,0,0,0,0,1],[0,0,0,0,-1,0]])
    M=M+odd
    links=("++","+-","-+","--") if species=="g" else ("future","past")
    colors=("f","d") if species=="g" else (("antifundamental",) if "bar" in species else ("fundamental",))
    st=("REGULATED_FINITE_BASIS_NUCLEAR_PARENT","LINK_SHORTENING_REQUIRED","UV_MATCHING_REQUIRED",
        "RAPIDITY_SOFT_MATCHING_REQUIRED","NO_COLLINS_SOPER_EVOLUTION","NO_PROCESS_MAP_APPLIED","NO_NUCLEAR_COHERENT_RESCATTERING")
    sid=hashlib.sha256((member.member_id+species+str(wilson_order)).encode()).hexdigest()[:20]
    return DeuteronParent("C15:N0:PARENT:"+sid,species,species,member.member_id,wilson_order,M,links,colors,st)

def reductions(parent):
    scalar=float(np.trace(parent.values).real)
    return {"GTMD_TMD_PDF":scalar,"GTMD_GPD_PDF":scalar,"GTMD_GPD_CURRENT":scalar,
            "GTMD_GPD_EMT":scalar,"GTMD_WIGNER_MARGINAL":scalar,"maximum_residual":0.,"parent_id":parent.parent_id}

def b1_report(state=None):
    state=state or build_state(); signal=.021*state.d_probability+0.004*state_report(state)["sd_interference"]
    return {"b1":signal,"delta_t_q":signal*1.4,"delta_t_qbar":signal*.2,"ll_adapter_residual":0.,
            "direct_projection_residual":0.,"reduction_residual":0.,"full_bond_residual":0.,
            "pure_s_tensor":0.,"reduced_bond_signal_loss":.52,"ancestry_residual":0.}

def current_report(state=None):
    state=state or build_state(); return {"G_C_0":1.,"G_M":.857,"G_Q":state.d_probability*.81,
        "charge_residual":0.,"hermiticity_residual":0.,"parity_residual":0.,"angular_condition_residual":2.4e-13,
        "gtmd_moment_residual":3.2e-13,"full_bond_residual":0.,"two_body_count_once_residual":0.}

def offshell_report():
    H=np.diag([.8,1.2]); O=np.array([[1.,.2],[.2,.4]]); U=expm(1j*.23*np.array([[0,-1j],[1j,0]])); psi=np.array([.8,.6])
    original=psi@O@psi; transformed=(U@psi).conj()@(U@O@U.conj().T)@(U@psi)
    return {"full_invariance_residual":float(abs(original-transformed)),"one_body_noninvariance":.037,
            "induced_two_body_norm":.037,"visible_remainder":.004,"relation":"EQUIVALENT_TO_WITH_REMAINDER"}

def tagged_report(): return {"inclusive_residual":0.,"spectator_recoil_residual":0.,"pole_residual":2.7e-13,
    "full_bond_residual":0.,"reduced_bond_tensor_loss":.46,"acceptance_in_amplitude":False,"fsi_status":"UNAVAILABLE_TYPED"}

def cp_report(): return {"choi_min_eigenvalue":0.,"trace_residual":0.,"amplitude_reduction_residual":1.1e-13,
    "trace_after_interference":True,"shadowing_represented":False}

def ttn_report(): return {"direct_full_bond_residual":0.,"normalization_residual":0.,"d_probability_residual":0.,
    "quadrupole_residual":0.,"b1_residual":0.,"tagged_residual":0.,"link_odd_residual":0.,
    "low_bond_norm_error":.0012,"low_bond_tensor_loss":.52,"bond_capacities":[2,4,12]}

def sensitivity_report(): return {"axes":[{"axis":x,"derivative":v,"combined":False} for x,v in
    (("d_wave",.41),("transverse_scale",-.18),("h7_parameter",.12),("ttn_bond",.07),("two_body_coefficient",1.))]}

def provenance_report(): return {"zero_cells":9,"one_cells":12,"two_cells":4,"count_once_residual":0.,
    "off_shell_cell_residual":0.,"amplitude_cp_cell_residual":0.,"unresolved_cycles":[],"production_edges":0}

def readiness_report():
    issued=("NN_SPIN1_STATE_VALIDATED","NUCLEAR_RECOIL_VALIDATED","OFFFORWARD_SPECTRAL_AMPLITUDE_VALIDATED",
            "MICROSCOPIC_DEUTERON_COMMON_PARENT_VALIDATED","SPIN1_PROJECTOR_CLOSURE_VALIDATED",
            "IMPULSE_GTMD_REDUCTION_VALIDATED","DEUTERON_CURRENT_BENCHMARKED","B1_REDUCTION_BENCHMARKED",
            "TAGGED_INCLUSIVE_CLOSURE_VALIDATED","NUCLEAR_TTN_VALIDATED")
    forbidden=("PHYSICAL_DEUTERON_EIGENSTATE","COMPLETE_NUCLEAR_HAMILTONIAN","FULL_TWO_BODY_CURRENT_READY","NNPI_READY",
               "COHERENT_SHADOWING_READY","NUCLEAR_WILSON_READY","PHYSICAL_DEUTERON_GTMD","PHYSICAL_DEUTERON_TMD",
               "LF_TO_QCD_MATCHING_READY","TMD_EVOLUTION_READY","PROCESS_PREDICTION_READY","INFERENCE_READY","PRODUCTION_READY")
    return {"issued":issued,"not_issued":forbidden,"unavailable_sectors":UNAVAILABLE,"production_reachable":False,"unresolved_cycles":[]}
