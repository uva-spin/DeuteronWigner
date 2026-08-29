"""Fail-closed C79 audit of the finite-basis direct W3 contact evaluator.

C78 deliberately freezes *support* and symbolic kernel coordinates.  It does
not attach a value to ``KAPPA[e,a]``.  This module makes that distinction
machine-checkable: C55/C43 provide the operator and inverse-derivative
ordering, while the repository presently contains no source-normalized,
four-mode finite-cell projection of that operator.  In particular, C50's
three-mode canonical q-to-qg vertex is not a legal replacement.

No numerical contact matrix or matrix-free numerical action is created here.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import inspect
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any

from ..g0.contracts import action_contract, symbolic_hash
from ..iferm.core import SB_W3, instantaneous_fermion_preflight
from ..ifsupport2.core import DIRECT_MONOMIAL, IFermContactSupportPackage, STATUS as C78_STATUS
from ..modes.core import RESOLUTIONS
from ..vsrc.core import finite_box_pminus_kernel

ROOT = Path(__file__).resolve().parents[4]
BASELINE = "1ddf21c230d3a16ee7e52ed09d84140f43781bb8"
STATUS = "C79_IFCONTACT_KERNEL_EVALUATION_INCOMPLETE"
NEXT = "C80/IFKERNEL2 — derive and validate the source-normalized finite-cell four-mode b† a† a b direct-contact kernel before evaluating any C78 coordinate"
BLOCKER = "C79.DIRECT_W3.FOUR_MODE_FINITE_CELL_PROJECTION_CONTRACT"
SCHEMA = "C79-IFCONTACT2-NOGO-V1"


def _canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def _digest(value: Any) -> str:
    return sha256(_canonical(value).encode()).hexdigest()


def _freeze(value: Any) -> Any:
    if isinstance(value, dict):
        return MappingProxyType({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, list):
        return tuple(_freeze(item) for item in value)
    return value


@dataclass(frozen=True)
class DirectContactKernelUnavailable(RuntimeError):
    """Raised instead of manufacturing a four-mode direct-contact value."""

    blocker: str = BLOCKER

    def __str__(self) -> str:
        return f"{self.blocker}: no source-derived finite-cell b† a† a b evaluator is available"


def _c78_freeze() -> dict[str, Any]:
    """Authenticate the entire C78 public support domain without regeneration."""
    package = IFermContactSupportPackage()
    by_resolution: dict[str, Any] = {}
    expected = {
        "K9_2_N8_b0.40": (16224, 28606464),
        "K11_2_N10_b0.45": (43350, 165991250),
        "K13_2_N12_b0.50": (95256, 697394304),
    }
    for resolution in RESOLUTIONS:
        payload = package.load_iferm_contact_support_package(resolution.label)
        counts = payload["counts"]
        pair_count, coordinate_count = expected[resolution.label]
        if counts["supported_pairs"] != pair_count or counts["kernel_coordinates"] != coordinate_count:
            raise ValueError("immutable C78 count mismatch")
        if counts["zero_counts"]["UNDECIDABLE_BLOCKING"] != 0:
            raise ValueError("C78 contains undecidable support")
        if any("KAPPA" not in group["kernel_coordinate_id_rule"] for group in payload["witness_groups"]):
            raise ValueError("C78 symbolic coordinate contract missing")
        by_resolution[resolution.label] = {
            "payload_hash": _digest(payload),
            "supported_pairs": pair_count,
            "kernel_coordinates": coordinate_count,
            "support_status": "FROZEN_SYMBOLIC_COORDINATES_ONLY",
        }
    return {"status": C78_STATUS, "public_api_only": True, "resolutions": by_resolution}


def _operator_routes() -> dict[str, Any]:
    """Close only the source-level W3 coefficient, not a mode-space value."""
    c43 = action_contract()
    c55 = instantaneous_fermion_preflight()["source"]
    if tuple(DIRECT_MONOMIAL) != ("b_dagger", "a_dagger", "a", "b"):
        raise ValueError("C55 direct contact ordering changed")
    # C43 denotes the same QCD coupling by ``g``; C55 denotes it ``g_s``.
    # Compare only after that explicit convention-map substitution.
    c43_w3_in_c55_convention = c43["interactions"]["instantaneous_fermion"].replace("g^2", "g_s^2")
    if c43_w3_in_c55_convention != SB_W3:
        raise ValueError("C43/C55 W3 transcription mismatch")
    if c55["coupling_power"] != 2 or c55["symbolic_residual"] not in ("Integer(0)", "0"):
        raise ValueError("C55 coefficient routes do not close")
    return {
        "operator_status": "SOURCE_DERIVED_SYMBOLIC_ONLY",
        "source_transcription": c43["interactions"]["instantaneous_fermion"],
        "coupling_convention_map": "C43 g -> C55 g_s",
        "constrained_fermion_route": c55["SB_W3"],
        "coefficient_routes_agree": True,
        "coupling": "g_s^2 explicitly factored; no physical value selected",
        "inverse_derivative": instantaneous_fermion_preflight()["inverse_derivative"]["routes"][0],
        "operator_hash": symbolic_hash({"C43_in_C55_convention": c43_w3_in_c55_convention, "C55": c55["SB_W3"]}),
    }


def _implementation_inventory() -> tuple[dict[str, Any], ...]:
    """Claim-versus-implementation inventory; exact terms may not be inferred."""
    c50_source = inspect.getsource(finite_box_pminus_kernel)
    signature = str(inspect.signature(finite_box_pminus_kernel))
    # The C50 function contains a single transverse polarization and two
    # quark spinors: it is a b† a† b vertex, not b† a† a b.  This is an
    # interface/type check, not an inference from a numerical result.
    c50_is_three_mode = (
        "_vertex_numerator" in c50_source
        and "finite_cell" in c50_source
        and tuple(inspect.signature(finite_box_pminus_kernel).parameters)
        == ("kq", "kg", "K", "qrel", "mass", "h_out", "h_in", "h_g", "coupling", "total_pplus")
    )
    if not c50_is_three_mode:
        raise ValueError("C50 vertex audit changed; review required")
    return (
        {"capability": "C43/C55 W3 operator coefficient and ordering", "classification": "EXECUTABLE_SYMBOLIC_OBJECT", "status": "PRESENT", "evidence": "C43 action contract + C55 two-route symbolic derivation"},
        {"capability": "direct inverse-partial-plus routing", "classification": "EXECUTABLE_SYMBOLIC_OBJECT", "status": "PRESENT", "evidence": "C55 direct b†a†ab route p_q^+ + k_g^+; Q0/PV policy"},
        {"capability": "C78 physical support/witness/kernel-coordinate domain", "classification": "STRUCTURAL_METADATA_ONLY", "status": "PRESENT_NO_VALUES", "evidence": "immutable public C78 API explicitly returns numerical_value=NOT_EVALUATED"},
        {"capability": "C45 one-particle modes and two-mode basis adapters", "classification": "EXECUTABLE_NUMERICAL_OBJECT", "status": "PRESENT_NONCONTACT_PRIMITIVES", "evidence": "mode library; no W3 four-field assembly"},
        {"capability": "C50 finite-box canonical vertex", "classification": "EXECUTABLE_NUMERICAL_OBJECT", "status": "PRESENT_BUT_INCOMPATIBLE", "evidence": f"signature {signature}; three-mode q→qg b†a†b kernel only"},
        {"capability": "normal-ordered four-mode plane-wave b†a†ab coefficient", "classification": "ABSENT_BLOCKING", "status": BLOCKER, "evidence": "no source-derived finite-cell field-expansion contraction implemented"},
        {"capability": "operator-specific local four-HO contact integral", "classification": "ABSENT_BLOCKING", "status": BLOCKER, "evidence": "C45 overlap primitives are not assembled with W3 momentum/spin/color routing"},
        {"capability": "C77/C78 projected four-mode kernel-coordinate evaluator", "classification": "ABSENT_BLOCKING", "status": BLOCKER, "evidence": "C78 coordinate KAPPA is symbolic by design; no value API exists"},
        {"capability": "bare direct-contact sparse matrix and independent action", "classification": "ABSENT_BLOCKING", "status": BLOCKER, "evidence": "requires all three missing operator-specific objects"},
    )


def evaluate_readiness() -> Any:
    """Return immutable no-go evidence after authenticating all legal inputs."""
    frozen = _c78_freeze()
    routes = _operator_routes()
    inventory = _implementation_inventory()
    blockers = tuple(row for row in inventory if row["classification"] == "ABSENT_BLOCKING")
    if not blockers:
        raise RuntimeError("C79 audit stale: a value evaluator exists and must be separately implemented")
    result = {
        "schema": SCHEMA,
        "baseline": BASELINE,
        "status": STATUS,
        "next": NEXT,
        "blocker": BLOCKER,
        "C78_freeze": frozen,
        "operator_routes": routes,
        "inventory": inventory,
        "blocked_coordinate_domains": {
            label: data["kernel_coordinates"]
            for label, data in frozen["resolutions"].items()
        },
        "prohibited_substitutions": (
            "C50 three-mode q-to-qg vertex",
            "C53 physical vertex values or propagators",
            "C58 self-induced-inertia primitive",
            "post-hoc Hermitian symmetrization",
            "fitted finite-cell normalization",
            "physical coupling or counterterm coefficient",
        ),
        "matrix_status": "NOT_CONSTRUCTED",
        "matrix_free_status": "NOT_CONSTRUCTED",
        "reason": "A direct W3 contact has two gluon fields. The only finite-cell interaction evaluator is C50's one-gluon canonical vertex, so using it would replace the requested local contact with a different operator and cannot establish the four-mode measure, spin/polarization contraction, ordered color product, or four-HO integral.",
    }
    return _freeze(result)


def require_evaluable_contact_kernel() -> None:
    """Hard gate used by downstream code and regression tests."""
    audit = evaluate_readiness()
    if audit["status"] != "C79_SOURCE_DERIVED_BARE_IFERM_CONTACT_MATRIX_READY":
        raise DirectContactKernelUnavailable()
