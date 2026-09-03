"""Immutable C37 records for the selected spacelike matching calculation.

The selected regulator is fixed.  C37 records the exact blocker when the
finite-basis realization has not supplied the operator ingredients required
to calculate a common-IR partonic difference.
"""
from dataclasses import asdict, dataclass
from hashlib import sha256
import json

C37_BASELINE = "dee1dfbd49a17db881dc9f52ae16f7c51c86df59"
C36_PLAN = "O4-SPACELIKE-COLLINS-JMY"
C37_NO_GO = "C37_FINITE_BASIS_COLLINEAR_ONE_LOOP_UNAVAILABLE"
C37_NEXT = "C38/M0A — finite-basis spacelike Wilson insertion, partonic states, and counterterm construction"
EMPTY_NOT_ZERO = "EMPTY_NOT_ZERO"
NONZERO_UNKNOWN = "NONZERO_UNKNOWN"

def content_hash(value):
    if hasattr(value, "__dataclass_fields__"): value = asdict(value)
    return sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()

@dataclass(frozen=True)
class C37PartonicCalculationId:
    root_id: str = "C37_SPACELIKE_PARTONIC_MATCHING_DESCENDANT"
    baseline: str = C37_BASELINE
    regulator: str = C36_PLAN
    art25_independent: bool = True
    production_reachable: bool = False
    @property
    def sha256(self): return content_hash(self)

@dataclass(frozen=True)
class PartonicExternalState:
    state_id: str
    ir_regulator: str
    momentum: tuple[float,float,float,float]
    helicity: int
    flavor: str
    hadron_state: bool = False
    @property
    def sha256(self): return content_hash(self)
    def __post_init__(self):
        if self.hadron_state: raise ValueError("C37 matching probes cannot be hadrons")

@dataclass(frozen=True)
class FiniteBasisPartonicCollinear:
    status: str
    missing: tuple[str,...]
    @property
    def sha256(self): return content_hash(self)
    def __post_init__(self):
        if self.status != C37_NO_GO or not self.missing: raise ValueError("C37 must fail closed with exact missing ingredients")

@dataclass(frozen=True)
class HadronApplicationGate:
    status: str
    microscopic_export: str
    bridge_rerun: bool
    @property
    def sha256(self): return content_hash(self)
    def __post_init__(self):
        if self.microscopic_export != EMPTY_NOT_ZERO or self.bridge_rerun: raise ValueError("C37 no-go cannot export or run bridge")

def blocker():
    return FiniteBasisPartonicCollinear(C37_NO_GO, (
        "regulator-identical finite-basis spacelike Wilson insertion",
        "partonic external-state realization with the common IR prescription",
        "instantaneous, boundary, zero-mode, Hamiltonian and operator counterterms",
        "regulated discrete-to-distributional x map and three-resolution trajectory",
        "selected-scheme soft/overlap operator identity",
    ))
