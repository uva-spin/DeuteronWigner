"""Finite C6 cut/overlap two-cells extending the existing pilot graph."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from ...formal.diagnostics import ArchitectureError


class C6Relation(str, Enum):
    EQUIVALENT_COUNT_ONCE = "EQUIVALENT_COUNT_ONCE"
    OVERLAP_SUBTRACT = "OVERLAP_SUBTRACT"
    ALTERNATIVE_TO = "ALTERNATIVE_TO"
    ADDS_TO = "ADDS_TO"
    REMAINDER_OF = "REMAINDER_OF"


@dataclass(frozen=True)
class TwoCell:
    stable_id: str
    source_ids: tuple[str, ...]
    target_id: str
    relation: C6Relation
    physical_region_id: str


class C6OverlapLedger:
    def __init__(self) -> None:
        self._cells: list[TwoCell] = []

    def add(self, cell: TwoCell) -> None:
        duplicates = [
            item for item in self._cells
            if item.physical_region_id == cell.physical_region_id
            and item.relation == cell.relation
        ]
        if duplicates and cell.relation in (
            C6Relation.EQUIVALENT_COUNT_ONCE,
            C6Relation.OVERLAP_SUBTRACT,
        ):
            raise ArchitectureError("C6.PROV.2", "physical cut/overlap already has an executable two-cell", expected="exactly one relation per physical region", received=cell.physical_region_id)
        self._cells.append(cell)

    def require_independent_channels(self, left: str, right: str) -> None:
        if left == right or {left, right} != {"F_TYPE", "D_TYPE"}:
            raise ArchitectureError("C6.PROV.3", "f/d channels cannot be deduplicated by scalar equality", expected=("F_TYPE", "D_TYPE"), received=(left, right))

    def trace(self) -> dict[str, object]:
        return {
            "cells": [
                {
                    "stable_id": item.stable_id,
                    "source_ids": list(item.source_ids),
                    "target_id": item.target_id,
                    "relation": item.relation.value,
                    "physical_region_id": item.physical_region_id,
                }
                for item in self._cells
            ],
            "general_provenance_2_complex_complete": False,
            "trace_reaches": ["C4_QQQG_STATE", "ORDERED_LINK_PAIR", "CUT_LEDGER", "F_D_COLOR", "SOFT_OVERLAP"],
        }


def reference_provenance() -> dict[str, object]:
    ledger = C6OverlapLedger()
    ledger.add(TwoCell(
        "C6:2CELL:CUT", ("C6:CUT:EIKONAL", "C6:CUT:LF"),
        "C6:CUT:COUNTED_ONCE", C6Relation.EQUIVALENT_COUNT_ONCE,
        "C6:SUPPORT:ACTIVE_GLUON_ONSHELL",
    ))
    ledger.add(TwoCell(
        "C6:2CELL:SOFT", ("C6:UNSUB:OVERLAP", "C6:SOFT:OVERLAP"),
        "C6:SUBTRACTED:FINITE", C6Relation.OVERLAP_SUBTRACT,
        "C6:REGION:SOFT_COLLINEAR_ZERO_BIN",
    ))
    ledger.add(TwoCell(
        "C6:2CELL:ROUTES", ("BOUNDARY_ONLY_RESCATTERING",),
        "JOINT_MICROSCOPIC_SOFT_SECTOR", C6Relation.ALTERNATIVE_TO,
        "C6:REGION:SOFT_ROUTE_OWNERSHIP",
    ))
    ledger.add(TwoCell(
        "C6:2CELL:UV_REMAINDER", ("C6:SUBTRACTED:FINITE",),
        "C6:UV:UNRESOLVED", C6Relation.REMAINDER_OF,
        "C6:REGION:UV_FINITE_MATCHING",
    ))
    return ledger.trace()
