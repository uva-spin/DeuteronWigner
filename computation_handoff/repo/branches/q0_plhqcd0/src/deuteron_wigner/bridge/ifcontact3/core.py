"""C81 detects whether C78 and C80 expose composable public domains.

This is intentionally not a matrix builder.  C78's public package exposes
symbolic kernel-coordinate domains and explicitly labels every coefficient
``NOT_EVALUATED``.  C80 evaluates an explicit raw coordinate, but publishes no
total map from a C78 coordinate ID to that coordinate.  Multiplying either
with an inferred array position or fabricated coefficient would violate both
immutable authority contracts.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any

from ..ifsupport2.core import IFermContactSupportPackage, STATUS as C78_STATUS
from ..ifkernel2.core import ContactKernelPackage, STATUS as C80_STATUS
from ..modes.core import RESOLUTIONS

ROOT=Path(__file__).resolve().parents[4]
BASELINE="0868a88422380339d9d5e0631830ba7528bd776f"
STATUS="C81_IFCONTACT_PAIR_AGGREGATION_INCOMPLETE"
NEXT="C82/IFAGG — materialize immutable per-coordinate projected coefficients and a total C78-coordinate-to-C80 coordinate map before any pair aggregation"
BLOCKER="C81.C78_C80.PUBLIC_COORDINATE_COMPOSITION_CONTRACT"


def _digest(value:Any)->str:
    return sha256(json.dumps(value,sort_keys=True,separators=(",",":"),default=str).encode()).hexdigest()


def _freeze(value:Any)->Any:
    if isinstance(value,dict): return MappingProxyType({k:_freeze(v) for k,v in value.items()})
    if isinstance(value,list): return tuple(_freeze(v) for v in value)
    return value


@dataclass(frozen=True)
class PairAggregationUnavailable(RuntimeError):
    blocker: str=BLOCKER
    def __str__(self): return f"{self.blocker}: public C78 coefficients and C80 coordinate identities are not composable"


def audit_pair_aggregation()->Any:
    c78=IFermContactSupportPackage(); c80=ContactKernelPackage(); rows={}
    expected={"K9_2_N8_b0.40":(16224,28606464),"K11_2_N10_b0.45":(43350,165991250),"K13_2_N12_b0.50":(95256,697394304)}
    for resolution in RESOLUTIONS:
        payload=c78.load_iferm_contact_support_package(resolution.label); pair_count,coordinate_count=expected[resolution.label]
        if payload["counts"]["supported_pairs"]!=pair_count or payload["counts"]["kernel_coordinates"]!=coordinate_count: raise ValueError("C78 immutable count mismatch")
        # Public C78 API is intentionally support-only. Probe a genuine
        # source-ordered witness, rather than assuming this from metadata.
        witness=c78.contact_witnesses(payload["emission_edges"][0]["physical_qg_id"],payload["absorption_edges"][0]["physical_qg_id"],resolution.label)[0]
        coeff=c78.contact_symbolic_coefficients(witness["physical_bra_id"],witness["physical_ket_id"],resolution.label)[0]
        rows[resolution.label]={"support_payload_hash":_digest(payload),"supported_pairs":pair_count,"kernel_coordinates":coordinate_count,"witness_id":witness["id"],"coordinate_id_rule":coeff["kernel_coordinate_domain"]["coordinate_id_rule"],"projected_coefficient":coeff["coefficient"],"projected_value_status":coeff["numerical_value"],"C80_public_operation":"evaluate(ContactKernelCoordinate)","total_coordinate_map_published":False}
        if coeff["numerical_value"]!="NOT_EVALUATED": raise ValueError("C78 contract unexpectedly changed; C81 must be redesigned")
    freeze=c80.input_freeze()
    if freeze["status"]!="C80_INPUTS_FROZEN_COMPLETE": raise ValueError("C80 public root mismatch")
    return _freeze({"baseline":BASELINE,"status":STATUS,"next":NEXT,"blocker":BLOCKER,"C78_status":C78_STATUS,"C80_status":C80_STATUS,"by_resolution":rows,
        "missing_objects":({"object":"immutable C78 per-coordinate projected coefficient record","why":"C78 returns an algebraic string and NOT_EVALUATED rather than exact/certified coefficient and bound"},{"object":"immutable total coordinate map C78:KAPPA -> C80 ContactKernelCoordinate","why":"C80 permits evaluation only after a caller supplies raw mode/color fields; C78 publishes only factorized domain rules"},{"object":"C80 M-squared numerical coefficient","why":"C80 returns symbolic 2*P_plus conversion, so no numeric M2 entry can be aggregated without selecting Pplus"}),
        "forbidden_repairs":("infer coefficient from C77/C74 array position","assign unit projected coefficient","use a C53 propagator","use C58 self-induced inertia","select Pplus or g_s numerically","symmetrize a fabricated matrix"),"matrix_status":"NOT_CONSTRUCTED","unavailable_supported_pairs":sum(x["supported_pairs"] for x in rows.values())})


def require_aggregatable_inputs()->None:
    raise PairAggregationUnavailable()
