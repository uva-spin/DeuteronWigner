"""Nontrivial nested qqq basis tower inheriting C7 resolution identities."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from fractions import Fraction

import numpy as np

from ...formal.diagnostics import ArchitectureError
from ..h0.resolution import HamiltonianResolution, reference_resolution


@dataclass(frozen=True)
class H1BasisState:
    radial: int
    longitudinal_partition: tuple[Fraction, Fraction, Fraction]
    Lz: int
    spin_projection: Fraction
    pair_spin: int
    permutation_irrep: str = "ANTISYMMETRIC_FERMION_WEDGE"
    color_irrep: str = "SINGLET_1"
    center_of_mass_quantum: int = 0

    @property
    def Jz(self): return Fraction(self.Lz)+self.spin_projection
    @property
    def stable_id(self):
        x="-".join(f"{v.numerator}_{v.denominator}" for v in self.longitudinal_partition)
        return f"r{self.radial}:x{x}:L{self.Lz}:S{self.spin_projection}:s12{self.pair_spin}"


@dataclass(frozen=True)
class H1ValenceBasis:
    resolution: HamiltonianResolution
    states: tuple[H1BasisState, ...]
    target: str
    target_Jz: Fraction
    status: str = "C8_H1_VALIDATION_ONLY"

    def __post_init__(self):
        if len(self.states)<=1 or len({s.stable_id for s in self.states})!=len(self.states):
            raise ArchitectureError("C8.BASIS", "basis must be nontrivial and duplicate-free", expected="dimension >1 unique", received=len(self.states))
        for state in self.states:
            if sum(state.longitudinal_partition,Fraction(0))!=1 or state.Jz!=self.target_Jz or state.center_of_mass_quantum!=0:
                raise ArchitectureError("C8.BASIS", "state violates K/Jz/CM block", expected=(1,self.target_Jz,0), received=(sum(state.longitudinal_partition),state.Jz,state.center_of_mass_quantum))
            if state.color_irrep!="SINGLET_1" or state.permutation_irrep!="ANTISYMMETRIC_FERMION_WEDGE":
                raise ArchitectureError("C8.BASIS", "color/statistics gate failed", expected=("SINGLET_1","ANTISYMMETRIC_FERMION_WEDGE"), received=(state.color_irrep,state.permutation_irrep))

    @property
    def dimension(self): return len(self.states)
    @property
    def basis_id(self):
        payload={"resolution":self.resolution.resolution_id,"target":self.target,"Jz":str(self.target_Jz),"states":[s.stable_id for s in self.states]}
        return "C8:H1:BASIS:"+hashlib.sha256(json.dumps(payload,sort_keys=True).encode()).hexdigest()[:20]


@dataclass(frozen=True)
class H1BasisTower:
    tower_id: str
    bases: tuple[H1ValenceBasis, ...]
    comparison_maps: tuple[np.ndarray, ...]

    def __post_init__(self):
        dims=[b.dimension for b in self.bases]
        if len(dims)<3 or not all(a<b for a,b in zip(dims,dims[1:])):
            raise ArchitectureError("C8.TOWER", "primary tower must grow twice", expected="strictly increasing three-point tower", received=dims)
        for left,right,mapping in zip(self.bases,self.bases[1:],self.comparison_maps):
            if mapping.shape!=(right.dimension,left.dimension):
                raise ArchitectureError("C8.TOWER", "comparison-map shape mismatch", expected=(right.dimension,left.dimension), received=mapping.shape)


def _states(count: int, Jz: Fraction):
    patterns=((Fraction(1,9),Fraction(3,9),Fraction(5,9)),(Fraction(3,9),Fraction(1,9),Fraction(5,9)),(Fraction(1,9),Fraction(5,9),Fraction(3,9)))
    out=[]
    for i in range(count):
        L=(-1,0,1)[i%3]
        out.append(H1BasisState(i//3,patterns[i%3],L,Jz-Fraction(L),i%2))
    return tuple(out)


def build_basis_tower(*, target="PROTON", Jz=Fraction(1,2), dimensions=(4,7,10), b_values=(0.40,0.45,0.50)):
    bases=[]
    for i,(dimension,b) in enumerate(zip(dimensions,b_values)):
        r=reference_resolution(K=Fraction(9,2)+i,N_max=8+2*i,b=b)
        bases.append(H1ValenceBasis(r,_states(dimension,Jz),target,Jz))
    maps=[]
    for left,right in zip(bases,bases[1:]):
        m=np.zeros((right.dimension,left.dimension))
        m[:left.dimension,:]=np.eye(left.dimension)
        maps.append(m)
    return H1BasisTower("C8:H1:TOWER:PRIMARY",tuple(bases),tuple(maps))
