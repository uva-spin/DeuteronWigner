"""Immutable assumption bundles and fail-closed H1 prediction plans."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass

from ...formal.diagnostics import ArchitectureError


@dataclass(frozen=True)
class H1AssumptionBundle:
    confinement_route: str
    spin_interaction_route: str
    solver_routes: tuple[str, ...] = ("EXACT", "KRYLOV", "TREE_TENSOR_NETWORK")
    scope: str = "C8_H1_VALIDATION_ONLY"
    fock_set: tuple[str, ...] = ("qqq",)
    strong_isospin: str = "exact"
    resolution_tower_id: str = "C8:H1:TOWER:PRIMARY"
    current_route: str = "GAUGED_HAMILTONIAN"
    renormalization_conditions: tuple[str, ...] = ("MASS", "PROTON_CHARGE", "CM", "SPIN_SPLITTING")
    calibration_partition: tuple[str, ...] = ("MASS", "PROTON_CHARGE", "CM", "SPIN_SPLITTING")
    withheld_partition: tuple[str, ...] = ("PROTON_F1_Q2", "NEUTRON_F1_Q2", "CURRENT_COMPONENT_B", "ROTATIONAL_DEFECT", "FLOW_HOLDOUT")
    operator_basis_version: str = "C8:H1:OPERATOR_BASIS:1"
    provenance_root: str = "C8:H1:PROVENANCE"

    def __post_init__(self):
        if self.scope != "C8_H1_VALIDATION_ONLY" or self.fock_set != ("qqq",):
            raise ArchitectureError("C8.PLAN", "H1 must remain valence-only", expected=("C8_H1_VALIDATION_ONLY", ("qqq",)), received=(self.scope, self.fock_set))
        if self.confinement_route not in ("INDUCED_REFIT", "ZERO_CONFINEMENT"):
            raise ArchitectureError("C8.PLAN", "invalid confinement route", expected=("INDUCED_REFIT", "ZERO_CONFINEMENT"), received=self.confinement_route)
        if self.spin_interaction_route not in ("EFFECTIVE_COLOR_SPIN", "NONE"):
            raise ArchitectureError("C8.PLAN", "invalid spin route", expected=("EFFECTIVE_COLOR_SPIN", "NONE"), received=self.spin_interaction_route)
        if set(self.calibration_partition) & set(self.withheld_partition):
            raise ArchitectureError("C8.PLAN", "calibration and holdout overlap", expected="disjoint frozen partitions", received=self.calibration_partition)

    @property
    def bundle_id(self):
        record=asdict(self)
        digest=hashlib.sha256(json.dumps(record,sort_keys=True,separators=(",",":")).encode()).hexdigest()[:20]
        return f"C8:H1:ASSUMPTION:{digest}"


@dataclass(frozen=True)
class H1PredictionPlan:
    plan_id: str
    assumption: H1AssumptionBundle
    stages: tuple[str, ...]
    allowed_outputs: tuple[str, ...] = ("VALENCE_STATE", "VALENCE_CURRENT", "DIAGNOSTICS")
    forbidden_outputs: tuple[str, ...] = ("TMD", "WILSON", "NUCLEAR", "MATCHING", "EVOLUTION", "PROCESS", "INFERENCE")

    def require_output(self, output: str):
        if output in self.forbidden_outputs:
            raise ArchitectureError("C8.READINESS", "downstream output unavailable from H1", expected=self.allowed_outputs, received=output)
        if output not in self.allowed_outputs:
            raise KeyError(output)


def compile_plan(bundle: H1AssumptionBundle, *, explicit_qqqg=False, frozen_confinement=False) -> H1PredictionPlan:
    if explicit_qqqg and bundle.spin_interaction_route=="EFFECTIVE_COLOR_SPIN":
        raise ArchitectureError("C8.PLAN", "induced qqq color-spin and explicit qqqg overlap", expected="one route or an overlap subtraction", received="both")
    if frozen_confinement and bundle.confinement_route=="INDUCED_REFIT":
        raise ArchitectureError("C8.RENORMALIZATION", "induced confinement must refit across resolutions", expected="resolution-indexed coefficients", received="frozen")
    stages=("BASIS","HAMILTONIAN","RENORMALIZATION","SOLVER","STATE_TRACKING","CURRENT","OBSERVABLES","STATE_BUNDLE")
    digest=hashlib.sha256((bundle.bundle_id+"|".join(stages)).encode()).hexdigest()[:20]
    return H1PredictionPlan(f"C8:H1:PLAN:{digest}",bundle,stages)
