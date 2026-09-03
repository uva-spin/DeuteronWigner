"""Exact-mode one-particle and physical Fock basis records."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from ...formal.diagnostics import ArchitectureError
from .resolution import HamiltonianResolution


_REP={"QUARK":"FUNDAMENTAL_3","ANTIQUARK":"ANTI_FUNDAMENTAL_3BAR","GLUON":"ADJOINT_8"}
_STAT={"QUARK":"FERMION","ANTIQUARK":"FERMION","GLUON":"BOSON"}
_CHARGE={"u":Fraction(2,3),"d":Fraction(-1,3),"NOT_APPLICABLE":Fraction(0)}


@dataclass(frozen=True)
class PartonBasisState:
    species: str
    flavor: str
    longitudinal_mode_exact: Fraction
    transverse_n: int
    transverse_m: int
    light_front_helicity: Fraction
    color_basis_label: str
    resolution_id: str
    total_K: Fraction

    def __post_init__(self):
        if self.species not in _REP:
            raise ArchitectureError("C7.MODE", "unknown partonic species", expected=tuple(_REP), received=self.species)
        mode=self.longitudinal_mode_exact
        if self.species=="GLUON" and (mode.denominator!=1 or mode<=0):
            raise ArchitectureError("C7.MODE", "gluon requires positive nonzero integer mode", expected="positive integer", received=mode)
        if self.species!="GLUON" and mode.denominator!=2:
            raise ArchitectureError("C7.MODE", "fermion requires exact half-integer mode", expected="odd/2", received=mode)
        if mode<=0 or self.transverse_n<0:
            raise ArchitectureError("C7.MODE", "mode lies outside basis support", expected="positive k,n>=0", received=(mode,self.transverse_n))

    @property
    def longitudinal_fraction_exact(self): return self.longitudinal_mode_exact/self.total_K
    @property
    def color_representation(self): return _REP[self.species]
    @property
    def statistics_class(self): return _STAT[self.species]
    @property
    def charge(self): return -_CHARGE[self.flavor] if self.species=="ANTIQUARK" else _CHARGE[self.flavor]
    @property
    def baryon_number(self): return Fraction(1,3) if self.species=="QUARK" else Fraction(-1,3) if self.species=="ANTIQUARK" else Fraction(0)
    @property
    def Jz_contribution(self): return self.transverse_m+self.light_front_helicity
    @property
    def ho_usage(self): return 2*self.transverse_n+abs(self.transverse_m)+1
    @property
    def stable_id(self): return f"{self.species}:{self.flavor}:k{self.longitudinal_mode_exact}:n{self.transverse_n}:m{self.transverse_m}:h{self.light_front_helicity}:{self.color_basis_label}"


@dataclass(frozen=True)
class FockSectorSpec:
    sector_id: str
    species_content: tuple[str,...]
    singlet_multiplicity: int


SECTORS={
    "qqq":FockSectorSpec("qqq",("QUARK","QUARK","QUARK"),1),
    "qqqg":FockSectorSpec("qqqg",("QUARK","QUARK","QUARK","GLUON"),2),
    "qqqq-qbar":FockSectorSpec("qqqq-qbar",("QUARK","QUARK","QUARK","QUARK","ANTIQUARK"),3),
}


@dataclass(frozen=True)
class ManyBodyBasisState:
    creation_labels: tuple[PartonBasisState,...]
    sector: FockSectorSpec
    color_multiplicity_label: str
    permutation_identity: str
    center_of_mass_quantum: int
    deterministic_phase: int
    resolution_id: str

    def __post_init__(self):
        if tuple(item.species for item in self.creation_labels)!=self.sector.species_content:
            raise ArchitectureError("C7.BASIS", "creation content does not match sector", expected=self.sector.species_content, received=tuple(x.species for x in self.creation_labels))
        if self.deterministic_phase not in (-1,1) or self.center_of_mass_quantum<0:
            raise ArchitectureError("C7.BASIS", "invalid phase or CM quantum", expected="phase +/-1,CM>=0", received=(self.deterministic_phase,self.center_of_mass_quantum))
        if len({item.stable_id for item in self.creation_labels})!=len(self.creation_labels):
            raise ArchitectureError("C7.PERM", "duplicate fermion creation mode violates Pauli support", expected="unique occupied modes", received=tuple(x.stable_id for x in self.creation_labels))

    @property
    def total_longitudinal_mode(self): return sum((x.longitudinal_mode_exact for x in self.creation_labels),Fraction(0))
    @property
    def nmax_usage(self): return sum(x.ho_usage for x in self.creation_labels)
    @property
    def charge(self): return sum((x.charge for x in self.creation_labels),Fraction(0))
    @property
    def baryon_number(self): return sum((x.baryon_number for x in self.creation_labels),Fraction(0))
    @property
    def Jz(self): return sum((x.Jz_contribution for x in self.creation_labels),Fraction(0))
    @property
    def stable_id(self): return f"C7:BASIS:{self.sector.sector_id}:{self.color_multiplicity_label}:"+":".join(x.stable_id for x in self.creation_labels)


@dataclass(frozen=True)
class PhysicalFockBasis:
    resolution: HamiltonianResolution
    sector: FockSectorSpec
    states: tuple[ManyBodyBasisState,...]
    target_charge: Fraction
    target_Jz: Fraction
    isospin_reference: str
    status: str = "H0_VALIDATION_ONLY"

    def __post_init__(self):
        for state in self.states:
            checks=(state.total_longitudinal_mode==self.resolution.K,state.nmax_usage<=self.resolution.N_max,state.charge==self.target_charge,state.baryon_number==1,state.Jz==self.target_Jz,state.center_of_mass_quantum==0,state.resolution_id==self.resolution.resolution_id)
            if not all(checks):
                raise ArchitectureError("C7.BASIS", "state violates an exact physical basis gate", expected="K/Nmax/charge/B/Jz/CM/resolution block", received=(state.stable_id,checks))
        if len({state.stable_id for state in self.states})!=len(self.states):
            raise ArchitectureError("C7.BASIS", "duplicate many-body basis state", expected="unique stable ids", received=len(self.states))

    @property
    def dimension(self): return len(self.states)


def _parton(species,flavor,k,m,h,color,resolution):
    return PartonBasisState(species,flavor,k,0,m,h,color,resolution.resolution_id,resolution.K)


def reference_basis(resolution: HamiltonianResolution, sector_id: str, *, proton=True, Jz=Fraction(1,2)) -> PhysicalFockBasis:
    sector=SECTORS[sector_id]
    flavors=("u","u","d") if proton else ("d","d","u")
    if sector_id=="qqq":
        modes=(Fraction(1,2),Fraction(3,2),Fraction(5,2))
        helicities=(Fraction(1,2),Fraction(1,2),Fraction(-1,2)) if Jz>0 else (Fraction(-1,2),Fraction(-1,2),Fraction(1,2))
        orbitals=(0,0,0)
        constituents=tuple(_parton("QUARK",f,k,m,h,f"c{i}",resolution) for i,(f,k,m,h) in enumerate(zip(flavors,modes,orbitals,helicities)))
    elif sector_id=="qqqg":
        modes=(Fraction(1,2),Fraction(1,2),Fraction(5,2),Fraction(1))
        qh=(Fraction(1,2),Fraction(1,2),Fraction(-1,2)) if Jz>0 else (Fraction(-1,2),Fraction(-1,2),Fraction(1,2))
        gh=Fraction(1) if Jz>0 else Fraction(-1)
        # One orbital unit compensates the active gluon helicity.
        orbitals=(0,0,-1 if Jz>0 else 1,0)
        constituents=tuple(_parton("QUARK",f,k,m,h,f"c{i}",resolution) for i,(f,k,m,h) in enumerate(zip(flavors,modes[:3],orbitals[:3],qh)))+(_parton("GLUON","NOT_APPLICABLE",modes[3],orbitals[3],gh,"a",resolution),)
    else:
        modes=(Fraction(1,2),)*4+(Fraction(5,2),)
        extra="d" if proton else "u"
        antif=extra
        # Net extra q-qbar charge vanishes.
        qfl=flavors+(extra,)
        helicities=(Fraction(1,2),Fraction(1,2),Fraction(-1,2),Fraction(1,2),Fraction(-1,2)) if Jz>0 else (Fraction(-1,2),Fraction(-1,2),Fraction(1,2),Fraction(-1,2),Fraction(1,2))
        constituents=tuple(_parton("QUARK",f,k,0,h,f"c{i}",resolution) for i,(f,k,h) in enumerate(zip(qfl,modes[:4],helicities[:4])))+(_parton("ANTIQUARK",antif,modes[4],0,helicities[4],"cbar",resolution),)
    states=tuple(ManyBodyBasisState(constituents,sector,f"SINGLET_{i+1}","CANONICAL_FERMION_WEDGE",0,1,resolution.resolution_id) for i in range(sector.singlet_multiplicity))
    return PhysicalFockBasis(resolution,sector,states,Fraction(1 if proton else 0),Jz,"STRONG_ISOSPIN_REFERENCE")
