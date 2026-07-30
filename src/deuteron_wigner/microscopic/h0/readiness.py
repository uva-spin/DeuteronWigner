"""H0 readiness ceiling and provenance isolation."""

from __future__ import annotations

from dataclasses import dataclass

from ...formal.diagnostics import ArchitectureError


VALIDATED=(
    "BASIS_TYPES_VALIDATED","COLOR_MULTIPLICITIES_VALIDATED",
    "PERMUTATION_BASIS_VALIDATED","CENTER_OF_MASS_GATE_VALIDATED",
    "FREE_OPERATOR_VALIDATED","TERM_INTERFACE_VALIDATED",
)
UNAVAILABLE=(
    "PHYSICAL_NUCLEON_EIGENSTATE","RENORMALIZATION_TRAJECTORY_VALIDATED",
    "CURRENT_READY","GTMD_OVERLAP_READY","WILSON_READY_FROM_MICROSCOPIC_STATE",
    "NUCLEAR_MATCHING_READY","LF_TO_QCD_MATCHING_READY","INFERENCE_READY",
)


@dataclass(frozen=True)
class H0Readiness:
    validated: tuple[str,...]=VALIDATED
    unavailable: tuple[str,...]=UNAVAILABLE
    status: str="VALIDATION_ONLY_H0"

    def require(self,capability: str) -> None:
        if capability in self.unavailable:
            raise ArchitectureError("C7.READINESS", "H0 capability remains unavailable", expected="later H1/H2 or matching package", received=capability)
        if capability not in self.validated:
            raise KeyError(capability)

    def to_dict(self):
        return {"status":self.status,"validated":list(self.validated),"unavailable":list(self.unavailable)}


H0_NODES=(
    "C7:H0:RESOLUTION","C7:H0:ONE_PARTICLE_MODES","C7:H0:COLOR_SINGLET_BASIS",
    "C7:H0:PERMUTATION_BASIS","C7:H0:PHYSICAL_FOCK_BASIS",
    "C7:H0:FREE_OPERATOR","C7:H0:REDUCED_VERTEX","C7:H0:READINESS",
)


def require_isolation(forbidden_roots: set[str]) -> None:
    overlap=set(H0_NODES)&forbidden_roots
    if overlap:
        raise ArchitectureError("C7.ISOLATION", "H0 node reached a forbidden downstream root", expected="disjoint H0 validation graph", received=sorted(overlap))


def provenance_graph():
    return {
        "nodes":[{"stable_id":node,"scope":"C7_H0_VALIDATION_ONLY"} for node in H0_NODES],
        "edges":[
            {"source":"C7:H0:ONE_PARTICLE_MODES","relation":"USES","target":"C7:H0:RESOLUTION"},
            {"source":"C7:H0:PHYSICAL_FOCK_BASIS","relation":"USES","target":"C7:H0:COLOR_SINGLET_BASIS"},
            {"source":"C7:H0:PHYSICAL_FOCK_BASIS","relation":"USES","target":"C7:H0:PERMUTATION_BASIS"},
            {"source":"C7:H0:FREE_OPERATOR","relation":"ACTS_ON","target":"C7:H0:PHYSICAL_FOCK_BASIS"},
            {"source":"C7:H0:REDUCED_VERTEX","relation":"CONNECTS","target":"C7:H0:PHYSICAL_FOCK_BASIS"},
        ],
        "production_reachable":False,
        "nuclear_reachable":False,
        "evolution_process_reachable":False,
        "inference_reachable":False,
    }
