"""Resolution-indexed H0 identity with non-aliasing scale types."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from fractions import Fraction

from ...formal.diagnostics import ArchitectureError


def lf_invariant_mass_squared(p_plus: float,p_minus: float,p_transverse_squared: float) -> float:
    return 2*p_plus*p_minus-p_transverse_squared


@dataclass(frozen=True)
class OscillatorScale:
    gev: float
    type_id: str = "BLFQ_OSCILLATOR_SCALE_B"

    def __post_init__(self):
        if self.gev <= 0:
            raise ArchitectureError("C7.RESOLUTION", "oscillator scale must be positive", expected=">0 GeV", received=self.gev)


@dataclass(frozen=True)
class HamiltonianScale:
    gev: float
    type_id: str = "HAMILTONIAN_SIMILARITY_SCALE_LAMBDA_H"

    def __post_init__(self):
        if self.gev <= 0:
            raise ArchitectureError("C7.RESOLUTION", "Hamiltonian resolution must be positive", expected=">0 GeV", received=self.gev)


@dataclass(frozen=True)
class EndpointRegulator:
    minimum_fraction: Fraction
    type_id: str = "LONGITUDINAL_ENDPOINT_REGULATOR"

    def __post_init__(self):
        if not 0 < self.minimum_fraction < 1:
            raise ArchitectureError("C7.RESOLUTION", "endpoint regulator outside support", expected="0<x_min<1", received=self.minimum_fraction)


@dataclass(frozen=True)
class HamiltonianResolution:
    K: Fraction
    N_max: int
    oscillator_scale_b: OscillatorScale
    hamiltonian_resolution_lambda: HamiltonianScale
    endpoint_regulator: EndpointRegulator
    fock_sector_set: tuple[str, ...]
    longitudinal_boundary_conditions: tuple[tuple[str, str], ...]
    transverse_basis_id: str
    zero_mode_policy_id: str
    center_of_mass_policy_id: str
    UV_interpretation: str = "DIAGNOSTIC_B_SQRT_NMAX_NOT_EXACT_CUTOFF"
    IR_interpretation: str = "DIAGNOSTIC_B_OVER_SQRT_NMAX_NOT_EXACT_CUTOFF"
    basis_version: int = 1

    def __post_init__(self):
        if self.K <= 0 or self.N_max < 1:
            raise ArchitectureError("C7.RESOLUTION", "invalid K or N_max", expected="K>0,N_max>=1", received=(self.K,self.N_max))
        if not self.zero_mode_policy_id or not self.center_of_mass_policy_id:
            raise ArchitectureError("C7.RESOLUTION", "resolution lacks zero-mode or CM policy", expected="explicit policy ids", received=(self.zero_mode_policy_id,self.center_of_mass_policy_id))
        if self.oscillator_scale_b.type_id == self.hamiltonian_resolution_lambda.type_id:
            raise ArchitectureError("C7.RESOLUTION", "distinct H0 scales were aliased", expected="separate b and lambda_H types", received=self.oscillator_scale_b.type_id)
        required = {"QUARK":"ANTIPERIODIC_HALF_INTEGER","ANTIQUARK":"ANTIPERIODIC_HALF_INTEGER","GLUON":"PERIODIC_NONZERO_INTEGER"}
        if dict(self.longitudinal_boundary_conditions) != required:
            raise ArchitectureError("C7.RESOLUTION", "wrong longitudinal boundary conditions", expected=required, received=dict(self.longitudinal_boundary_conditions))

    @property
    def resolution_id(self) -> str:
        digest = hashlib.sha256(self.canonical_json().encode()).hexdigest()[:20]
        return f"C7:H0:RESOLUTION:{digest}"

    def canonical_record(self) -> dict[str, object]:
        return {
            "K":[self.K.numerator,self.K.denominator],
            "N_max":self.N_max,
            "oscillator_scale_b":asdict(self.oscillator_scale_b),
            "hamiltonian_resolution_lambda":asdict(self.hamiltonian_resolution_lambda),
            "endpoint_regulator":{"minimum_fraction":[self.endpoint_regulator.minimum_fraction.numerator,self.endpoint_regulator.minimum_fraction.denominator],"type_id":self.endpoint_regulator.type_id},
            "fock_sector_set":list(self.fock_sector_set),
            "longitudinal_boundary_conditions":[list(x) for x in self.longitudinal_boundary_conditions],
            "transverse_basis_id":self.transverse_basis_id,
            "zero_mode_policy_id":self.zero_mode_policy_id,
            "center_of_mass_policy_id":self.center_of_mass_policy_id,
            "UV_interpretation":self.UV_interpretation,
            "IR_interpretation":self.IR_interpretation,
            "basis_version":self.basis_version,
            "diagnostic_scales_gev":{
                "Lambda_IR_approx":self.oscillator_scale_b.gev/(self.N_max**0.5),
                "Lambda_UV_approx":self.oscillator_scale_b.gev*(self.N_max**0.5),
            },
        }

    def canonical_json(self) -> str:
        return json.dumps(self.canonical_record(),sort_keys=True,separators=(",",":"))

    def to_dict(self) -> dict[str, object]:
        return {"resolution_id":self.resolution_id,**self.canonical_record()}


def reference_resolution(K=Fraction(9,2), N_max=8, b=0.45) -> HamiltonianResolution:
    return HamiltonianResolution(
        K,N_max,OscillatorScale(b),HamiltonianScale(1.2),
        EndpointRegulator(Fraction(1,18)),("qqq","qqqg","qqqq-qbar"),
        (("QUARK","ANTIPERIODIC_HALF_INTEGER"),("ANTIQUARK","ANTIPERIODIC_HALF_INTEGER"),("GLUON","PERIODIC_NONZERO_INTEGER")),
        "2D_HO_INTRINSIC_V1","EXCLUDE_GLUON_ZERO_MODE_WITH_CLOSURE_LEDGER",
        "LAWSON_INTRINSIC_GROUND_GATE_V1",
    )
