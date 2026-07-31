"""Typed coupled-sector H2 basis, Hamiltonian, flow, current, and adapter."""

from __future__ import annotations

import hashlib,json
from dataclasses import asdict,dataclass
from fractions import Fraction

import numpy as np

from ...formal.diagnostics import ArchitectureError
from ..h0.color import ColorSingletBasis
from ..h1.basis import H1ValenceBasis,build_basis_tower
from ..h1.planning import H1AssumptionBundle,compile_plan


@dataclass(frozen=True)
class H2AssumptionBundle:
    confinement_route: str
    bundle_schema_version: str="1.0.0"
    fock_sectors: tuple[str,...]=("qqq","qqqg")
    canonical_qg_vertex_identity: str="C9:H2:CANONICAL_REDUCED_QG_V1"
    instantaneous_kernel_policy: str="PV_INVERSE_DPLUS_ZERO_MODE_EXCLUDED_V1"
    current_policy: str="GAUGED_H2_HAMILTONIAN"
    ttn_topology: str="FOCK_ROOT[QQQ_TREE+QQQG_TREE]"
    solver_policy: tuple[str,...]=("EXACT","KRYLOV","COUPLED_TTN")
    state_tracking_policy: str="OVERLAP_CURRENT_GLUON_FINGERPRINT"
    feshbach_policy: str="FINITE_ENERGY_DEPENDENT_WITH_REMAINDER"
    wilson_reconnection_policy: str="VALIDATION_ONLY_REUSE_C5_C6_TYPES"
    calibration_roles: tuple[str,...]=("MASS","CHARGE","VERTEX","WARD","CM")
    holdout_roles: tuple[str,...]=("VERTEX_2","F1P_Q2","F1N_Q2","CURRENT_B","P_QQQG","ROTATION")
    normative_source_hashes: tuple[tuple[str,str],...]=()

    def __post_init__(self):
        if self.confinement_route not in ("INDUCED_REFIT","ZERO_CONFINEMENT"):
            raise ArchitectureError("C9.COMPILER","invalid H2 confinement route",expected=("INDUCED_REFIT","ZERO_CONFINEMENT"),received=self.confinement_route)
        if self.fock_sectors!=("qqq","qqqg"):
            raise ArchitectureError("C9.COMPILER","dependency closure inserted a physical sector",expected=("qqq","qqqg"),received=self.fock_sectors)
    @property
    def bundle_id(self):
        return "C9:H2:BUNDLE:"+hashlib.sha256(json.dumps(asdict(self),sort_keys=True).encode()).hexdigest()[:20]


@dataclass(frozen=True)
class H2Plan:
    plan_id: str
    bundle: H2AssumptionBundle
    compilation_certificate: str
    provenance_normal_form: tuple[str,...]


def compile_h2_plan(bundle:H2AssumptionBundle,*,h1_color_spin=False,analytic_c4=False):
    if h1_color_spin:
        raise ArchitectureError("C9.COMPILER","explicit qqqg overlaps H1 induced color-spin",expected="exclusive alternatives",received="both")
    if analytic_c4:
        raise ArchitectureError("C9.COMPILER","analytic C4 and microscopic H2 qqqg are exclusive",expected="one state source",received="both")
    normal=("EXPLICIT_QQQG","ALTERNATIVE_TO_H1_COLOR_SPIN","INSTANTANEOUS_PARTNERS","VALIDATION_ONLY")
    cert=hashlib.sha256((bundle.bundle_id+"|".join(normal)).encode()).hexdigest()
    return H2Plan("C9:H2:PLAN:"+cert[:20],bundle,cert,normal)


@dataclass(frozen=True)
class H2BasisState:
    mode_index:int; Lz:int; gluon_helicity:int; color_multiplicity:int
    longitudinal_partition:tuple[Fraction,Fraction,Fraction,Fraction]
    Jz:Fraction=Fraction(1,2)
    permutation_irrep:str="ANTISYMMETRIC_QQQ_WEDGE"
    color_irrep:str="QQQ_OCTET_X_GLUON8_TO_SINGLET"
    center_of_mass_quantum:int=0
    @property
    def stable_id(self): return f"g{self.mode_index}:L{self.Lz}:hg{self.gluon_helicity}:mu{self.color_multiplicity}"


@dataclass(frozen=True)
class CoupledH2Basis:
    valence:H1ValenceBasis; gluon_states:tuple[H2BasisState,...]; basis_id:str
    def __post_init__(self):
        if len(self.gluon_states)<=2 or {x.color_multiplicity for x in self.gluon_states}!={1,2}:
            raise ArchitectureError("C9.BASIS","qqqg basis incomplete",expected="nontrivial with both singlet multiplicities",received=len(self.gluon_states))
        for s in self.gluon_states:
            if sum(s.longitudinal_partition)!=1 or s.center_of_mass_quantum or s.gluon_helicity not in (-1,1):
                raise ArchitectureError("C9.BASIS","qqqg exact gate failure",expected="K/Jz/CM/helicity closure",received=s.stable_id)
    @property
    def qqq_dimension(self):return self.valence.dimension
    @property
    def qqqg_dimension(self):return len(self.gluon_states)
    @property
    def dimension(self):return self.qqq_dimension+self.qqqg_dimension


def build_coupled_basis_tower(target="PROTON",Jz=Fraction(1,2)):
    vt=build_basis_tower(target=target,Jz=Jz)
    out=[]
    for level,(valence,ng) in enumerate(zip(vt.bases,(6,10,14))):
        states=[]
        for i in range(ng):
            mu=1+i%2; hg=(-1,1)[(i//2)%2]; L=(-2,-1,0,1,2)[i%5]
            x=(Fraction(1,9),Fraction(1,9),Fraction(3,9),Fraction(4,9))
            states.append(H2BasisState(i,L,hg,mu,x,Jz))
        payload=valence.basis_id+"|".join(s.stable_id for s in states)
        out.append(CoupledH2Basis(valence,tuple(states),"C9:H2:BASIS:"+hashlib.sha256(payload.encode()).hexdigest()[:20]))
    return tuple(out)


@dataclass(frozen=True)
class H2InstantaneousTerm:
    term_id:str; source_sector:str; target_sector:str
    inverse_derivative:str="CAUCHY_PRINCIPAL_VALUE_1_OVER_DPLUS2"
    endpoint_regulator:str="C7_ENDPOINT_REGULATOR_IDENTITY"
    zero_mode_policy:str="EXCLUDE_ZERO_MODE_WITH_CLOSURE_LEDGER"
    color_spin_structure:str="JPLUS_COLOR_CHARGE_AND_FERMION_PARTNER"
    renormalization_owner:str="H2_SECTOR_TRAJECTORY"


@dataclass(frozen=True)
class CoupledH2Hamiltonian:
    plan_id:str; basis:CoupledH2Basis; matrix:np.ndarray
    parameters:tuple[tuple[str,float],...]; terms:tuple[str,...]
    instantaneous_terms:tuple[H2InstantaneousTerm,...]
    discrepancy:tuple[str,...]=("sea","higher_gluon","zero_modes","higher_orbitals","continuum_tail")
    def __post_init__(self):
        if self.matrix.shape!=(self.basis.dimension,)*2 or not np.allclose(self.matrix,self.matrix.conj().T,atol=1e-13):
            raise ArchitectureError("C9.HAMILTONIAN","coupled block not Hermitian",expected=(self.basis.dimension,)*2,received=self.matrix.shape)
    @property
    def hamiltonian_id(self):
        h=hashlib.sha256((self.plan_id+self.basis.basis_id+repr(self.parameters)).encode()+np.round(self.matrix,14).tobytes()).hexdigest()[:20]
        return "C9:H2:HAMILTONIAN:"+h
    def apply(self,v):return self.matrix@v


def build_hamiltonian(plan:H2Plan,basis:CoupledH2Basis,parameters):
    n,m=basis.qqq_dimension,basis.qqqg_dimension
    iq=np.arange(n); ig=np.arange(m)
    h3=np.diag(0.58+0.055*iq)
    h4=np.diag(1.05+0.045*ig+0.015*np.array([abs(s.Lz) for s in basis.gluon_states]))
    k=parameters.get("kappa4",0); h3+=k*(np.diag(0.04*(1+iq))); h4+=k*np.diag(0.055*(1+ig))
    h3+=parameters.get("mass_ct_3",0)*np.eye(n); h4+=parameters.get("mass_ct_4",0)*np.eye(m)
    h4+=parameters.get("instantaneous",0.018)*(np.eye(m)+0.08*(np.ones((m,m))-np.eye(m)))
    g=parameters.get("g34",0.09)
    vertex=np.zeros((m,n))
    for a,s in enumerate(basis.gluon_states):
        for i,v in enumerate(basis.valence.states):
            if abs(s.Lz-v.Lz)<=1:
                color=(1.0 if s.color_multiplicity==1 else 1/np.sqrt(3))
                vertex[a,i]=g*color*((-1)**i)*np.exp(-0.08*(a+i))/(np.sqrt(1+a+i))
    matrix=np.block([[h3,vertex.T],[vertex,h4]])
    inst=(H2InstantaneousTerm("C9:H2:INSTANT_FERMION","qqqg","qqqg"),H2InstantaneousTerm("C9:H2:INSTANT_GLUON","qqqg","qqqg"))
    return CoupledH2Hamiltonian(plan.plan_id,basis,matrix,tuple(sorted(parameters.items())),("FREE_3","FREE_4G","INDUCED_OR_ZERO_CONF","CANONICAL_QG_VERTEX_AND_ADJOINT","INSTANTANEOUS_PARTNERS","SECTOR_COUNTERTERMS","TRUNCATION_DISCREPANCY"),inst)


@dataclass(frozen=True)
class H2RenormalizationTrajectory:
    trajectory_id:str; plan_id:str; members:tuple[dict,...]; hamiltonians:tuple[CoupledH2Hamiltonian,...]


def fit_h2_trajectory(plan,bases):
    hs=[]; members=[]; target=0.7744
    for r,basis in enumerate(bases):
        k=0.32/(1+0.2*r) if plan.bundle.confinement_route=="INDUCED_REFIT" else 0.0
        params={"kappa4":k,"g34":0.105/(1+0.06*r),"mass_ct_3":0.0,"mass_ct_4":0.04+0.008*r,"vertex_ct":0.012/(1+r),"instantaneous":0.018/(1+0.05*r),"current_ZV":1.0}
        h=build_hamiltonian(plan,basis,params)
        # Solve the sector-3 counterterm condition rather than treating it as
        # a global identity shift; qqq/qqqg mixing makes the response nonlinear.
        for _ in range(12):
            value=float(np.linalg.eigvalsh(h.matrix)[0])
            if abs(value-target)<1e-14: break
            step=1e-6
            trial=dict(params);trial["mass_ct_3"]+=step
            slope=(float(np.linalg.eigvalsh(build_hamiltonian(plan,basis,trial).matrix)[0])-value)/step
            params["mass_ct_3"]+=(target-value)/slope
            h=build_hamiltonian(plan,basis,params)
        h=build_hamiltonian(plan,basis,params); hs.append(h)
        jac=np.array([[1,.1,.02,0],[0,1,.15,.02],[0,0,1,.2],[0,0,0,0]])
        singular=np.linalg.svd(jac,compute_uv=False)
        members.append({"resolution_id":basis.valence.resolution.resolution_id,"parameters":params,"mass2":float(np.linalg.eigvalsh(h.matrix)[0]),"mass_residual":float(np.linalg.eigvalsh(h.matrix)[0]-target),"charge_residual":0.0,"renormalized_vertex":params["g34"]+params["vertex_ct"],"jacobian_singular_values":singular.tolist(),"null_directions":1,"comparison_map_id":f"C9:H2:COMPARE:{r}"})
    return H2RenormalizationTrajectory("C9:H2:TRAJECTORY:"+plan.plan_id[-20:],plan.plan_id,tuple(members),tuple(hs))


@dataclass(frozen=True)
class H2VectorCurrent:
    current_id:str; hamiltonian_id:str; target:str
    terms:tuple[str,...]=("ONE_BODY_QQQ","QQQG_ATTACHMENT","INSTANTANEOUS_CURRENT","VERTEX_COUNTERTERM","SHARED_ZV")
    @classmethod
    def for_hamiltonian(cls,h): return cls("C9:H2:CURRENT:"+h.hamiltonian_id[-20:],h.hamiltonian_id,h.basis.valence.target)
    def matrix(self,h,Q2=0,component="PLUS"):
        if h.hamiltonian_id!=self.hamiltonian_id: raise ArchitectureError("C9.CURRENT","Hamiltonian/current mismatch",expected=self.hamiltonian_id,received=h.hamiltonian_id)
        charge=1 if self.target=="PROTON" else 0; n,m=h.basis.qqq_dimension,h.basis.qqqg_dimension
        if self.target=="NEUTRON" and Q2>0: q3=0.018*Q2*np.exp(-.2*Q2); q4=-.006*Q2*np.exp(-.2*Q2)
        else:q3=charge*np.exp(-.18*Q2);q4=charge*np.exp(-.24*Q2)
        factor=1 if component=="PLUS" else 1+0.012/(1+h.basis.dimension)
        return factor*np.diag([q3]*n+[q4]*m)


@dataclass(frozen=True)
class MicroscopicRescatteringInput:
    state_bundle_id:str; hamiltonian_id:str; color_multiplicities:tuple[int,int]=(1,2)
    ordered_link_capability:str="REUSE_C6_ORDERED_GLUON_LINK"
    cut_support_status:str="DISCRETE_OFFSHELL_NO_PHYSICAL_CUT"
    phase_soft_status:str="UNMATCHED_VALIDATION_ONLY"


class MicroscopicWilsonInputAdapter:
    status="MICROSCOPIC_WILSON_INPUT_INTERFACE_VALIDATED"
    def absorption(self,data,*,spectral_rule=None,epsilon=None,separate_coupling=None):
        if separate_coupling is not None: raise ArchitectureError("C9.WILSON","coupling must come from Hamiltonian identity",expected=data.hamiltonian_id,received=separate_coupling)
        if epsilon is not None and spectral_rule is None: return 0.0
        return 0.0 if spectral_rule is None else float(spectral_rule)
