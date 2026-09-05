"""Truthful C400.S2 status and supersession records."""

from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from typing import Any, Mapping

C144_DIAGNOSTIC_STATUS = "C144_DIAGNOSTIC_EIGENSTATE_SMOKE_PATH_READY"
C396_BINDING_STATUS = "C396_19_COORDINATE_BINDING_INCOMPLETE"
SECTOR_STATUS = "SECTOR_IDENTITY_UNVERIFIED"
RANK_STATUS = "RANK_NOT_EVALUATED"
FIT_STATUS = "PHYSICAL_FIT_NOT_AUTHORIZED"
OVERALL_STATUS = (
    "PARTIAL_FORWARD_MAP_C144_DIAGNOSTIC_EIGENSTATE_SMOKE_PATH_READY_"
    "C396_19_COORDINATE_BINDING_INCOMPLETE"
)
HISTORICAL_P1C_STATUS = "PHASE_COMPLETE_DIAGNOSTIC_FORWARD_MAP_READY_SCIENCE_REVIEW_NEXT"


def _root(value: Any) -> str:
    return sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), default=str).encode("utf-8")
    ).hexdigest()


def status_supersession_record() -> Mapping[str, Any]:
    """Return the versioned interpretation record for the P1C result.

    The historical file is not modified.  This record narrows what the phrase
    ``forward_map_ready`` may mean in subsequent C400 work.
    """

    record = {
        "schema": "C400-S2-P1C-STATUS-SUPERSESSION-V1",
        "historical_record": {
            "status": HISTORICAL_P1C_STATUS,
            "preserved_immutable": True,
            "historical_forward_map_ready_field": True,
        },
        "superseding_interpretation": {
            "status": OVERALL_STATUS,
            "C144_diagnostic_smoke_path": C144_DIAGNOSTIC_STATUS,
            "C396_forward_map": C396_BINDING_STATUS,
            "sector_identity": SECTOR_STATUS,
            "rank": RANK_STATUS,
            "physical_fit": FIT_STATUS,
            "C144_smoke_path_ready": True,
            "C396_19_coordinate_forward_map_ready": False,
            "state_to_current_observable_path_ready": False,
            "physical_activation_ready": False,
        },
        "forbidden_inferences": (
            "C144 fixture coordinates are C396 coordinates",
            "an unprojected diagnostic eigenpair is a deuteron-sector state",
            "a missing numeric response is physical irrelevance",
            "diagnostic derivative integrity establishes physical rank",
        ),
        "next_owner": "USER_CHATGPT_THEN_CODEX_LIVE_INTEGRATION",
    }
    return deepcopy({**record, "root": _root(record)})


__all__ = [
    "C144_DIAGNOSTIC_STATUS",
    "C396_BINDING_STATUS",
    "SECTOR_STATUS",
    "RANK_STATUS",
    "FIT_STATUS",
    "OVERALL_STATUS",
    "HISTORICAL_P1C_STATUS",
    "status_supersession_record",
]
